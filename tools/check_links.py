"""Check relative Markdown links in the public tree.

Scans every ``.md`` file that is tracked or committable
(``git ls-files --cached --others --exclude-standard``), including the
manuscript under ``05-survey/manuscript/``. Inline links and
images (``[text](target)``, ``[text](<target>)``) and reference definitions
(``[label]: target``) are checked; links in fenced code blocks, inline code,
and HTML comments are ignored. ``http(s):`` and ``mailto:`` links and pure
``#anchors`` are skipped, and ``#fragments`` are stripped.

A link is reported as

* ``broken`` when it does not resolve to an existing file or directory inside
  the repository;
* ``local-only`` when it resolves to a gitignored file (``git check-ignore``),
  which is missing from the public tree: PDFs, ``02-fulltext/`` except
  ``INDEX.md``, the ``99-archive`` zip, and LaTeX build products.

The run prints each problem with file and line, a summary count, and exits
non-zero when any problem exists.

Usage::

    python -m tools.check_links
    python -m tools.check_links --root path/to/library
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

from tools.common import REPO_ROOT, git_candidate_files, read_text

SKIP_PREFIXES: tuple[str, ...] = ()
_SKIP_TARGET = re.compile(r"^(?:https?:|mailto:|#)", re.I)
_INLINE = re.compile(r"\]\(\s*(?:<([^>\n]*)>|([^)\s]*))")
_REFERENCE = re.compile(r"^ {0,3}\[([^\]]+)\]:\s*(?:<([^>\n]*)>|(\S+))")
_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
_CODE_SPAN = re.compile(r"(`+).+?\1")
_COMMENT = re.compile(r"<!--.*?-->", re.S)


@dataclass
class Problem:
    path: str
    line: int
    kind: str
    target: str


@dataclass
class Report:
    files: int = 0
    links: int = 0
    problems: list[Problem] = field(default_factory=list)

    def count(self, kind: str) -> int:
        return sum(1 for p in self.problems if p.kind == kind)


def extract_links(text: str) -> list[tuple[int, str]]:
    """Return (line number, target) for every inline link and reference definition."""
    text = _COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    links = []
    fence = None
    for lineno, line in enumerate(text.splitlines(), start=1):
        match = _FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker[0] * 3
            elif marker.startswith(fence):
                fence = None
            continue
        if fence is not None:
            continue
        line = _CODE_SPAN.sub("", line)
        ref = _REFERENCE.match(line)
        if ref and not ref.group(1).startswith("^"):
            links.append((lineno, ref.group(2) if ref.group(2) is not None else ref.group(3)))
            continue
        for m in _INLINE.finditer(line):
            target = m.group(1) if m.group(1) is not None else m.group(2)
            if target:
                links.append((lineno, target))
    return links


def ignored_paths(root: Path, rels: list[str]) -> set[str]:
    """Return the subset of root-relative paths that Git ignores."""
    if not rels:
        return set()
    result = subprocess.run(
        ["git", "check-ignore", "--stdin", "-z"],
        cwd=root,
        input=("\0".join(rels) + "\0").encode("utf-8"),
        capture_output=True,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return {p for p in result.stdout.decode("utf-8").split("\0") if p}


def check_tree(root: Path = REPO_ROOT) -> Report:
    root = root.resolve()
    report = Report()
    resolved: list[tuple[str, int, str, str]] = []
    for path in git_candidate_files(root):
        rel = path.relative_to(root).as_posix()
        if path.suffix.lower() != ".md" or rel.startswith(SKIP_PREFIXES):
            continue
        report.files += 1
        for lineno, target in extract_links(read_text(path)):
            if _SKIP_TARGET.match(target):
                continue
            report.links += 1
            clean = unquote(target.split("#", 1)[0])
            base = root if clean.startswith("/") else path.parent
            dest = (base / clean.lstrip("/")).resolve()
            try:
                dest_rel = dest.relative_to(root).as_posix()
            except ValueError:
                report.problems.append(Problem(rel, lineno, "broken", target))
                continue
            if not dest.exists():
                report.problems.append(Problem(rel, lineno, "broken", target))
            elif dest_rel != ".":
                resolved.append((rel, lineno, target, dest_rel))
    ignored = ignored_paths(root, sorted({d for _, _, _, d in resolved}))
    for rel, lineno, target, dest_rel in resolved:
        if dest_rel in ignored:
            report.problems.append(Problem(rel, lineno, "local-only", target))
    report.problems.sort(key=lambda p: (p.path, p.line, p.target))
    return report


def format_report(report: Report) -> str:
    lines = [f"{p.path}:{p.line}: {p.kind} link: {p.target}" for p in report.problems]
    lines.append(
        f"Markdown files: {report.files}; relative links: {report.links}; "
        f"broken: {report.count('broken')}; local-only: {report.count('local-only')}"
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check relative Markdown links.")
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    report = check_tree(args.root)
    sys.stdout.write(format_report(report) + "\n")
    return 1 if report.problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
