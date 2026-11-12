"""Pre-publication guard for the public repository tree.

The check scans every file that is tracked or would be added by
``git add -A`` and reports five classes of problems:

* ``size``: a file larger than the size limit (default 50 MB);
* ``forbidden-path``: unregistered source artifacts, private archives and
  ``.env`` files. Registered reading assets are allowed through Git LFS;
* ``absolute-path``: a local absolute path inside a user profile folder
  (Windows drive paths, ``/home/<name>/``, or ``/Users/<name>/``);
* ``secret``: a string that looks like a credential;
* ``cjk``: CJK characters outside localized reading pages and registered
  verbatim full texts. Authored research prose stays English-only.

The first four checks always fail the run. The CJK check fails the run only
with ``--cjk strict``; ``--cjk report`` lists the files without failing.
Secret matches are reported by location only; the matched text is never
printed.

Usage::

    python -m tools.check_public_tree --cjk report
    python -m tools.check_public_tree --cjk strict --json report.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from tools.common import REPO_ROOT, git_candidate_files, is_text_path, read_text
from tools.check_lfs_assets import load_assets

SIZE_LIMIT_BYTES = 50 * 1024 * 1024

FORBIDDEN_PREFIXES = (
    "99-archive/superseded/",
    "99-archive/local/",
)
ALLOWED_IN_FULLTEXT = {"02-fulltext/INDEX.md"}
# The manuscript is self-authored: its compiled PDFs and figure PDFs may be published.
SELF_AUTHORED_PDFS = {"05-survey/manuscript/survey.pdf", "05-survey/manuscript/supplement.pdf"}
MANUSCRIPT_FIGURES = "05-survey/manuscript/figures/"
# The local reading UI serves Chinese-speaking readers. This exception applies
# only to its labels, never to research prose or path/secret/source guards.
LOCALIZED_UI_PATHS = {"tools/local_index.html", "INDEX.html"}

ABSOLUTE_PATH_PATTERNS = [
    re.compile(r"(?i)\b[a-z]:(?:\\\\|\\|/)+users(?:\\\\|\\|/)+"),
    re.compile(r"/home/[A-Za-z0-9_.-]+/"),
    re.compile(r"/Users/[A-Za-z0-9_.-]+/"),
]

SECRET_PATTERNS = [
    re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{22,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(
        r"(?i)\b(?:api[_-]?key|access[_-]?token|secret[_-]?key|client[_-]?secret|"
        r"password|passwd)\b\s*[:=]\s*[\"']?[A-Za-z0-9/+_\-]{16,}"
    ),
]

CJK_PATTERN = re.compile(
    "["
    "\u3000-\u303f"  # CJK symbols and punctuation
    "\u3040-\u30ff"  # Hiragana and Katakana
    "\u3400-\u4dbf"  # CJK Extension A
    "\u4e00-\u9fff"  # CJK Unified Ideographs
    "\uac00-\ud7af"  # Hangul syllables
    "\uf900-\ufaff"  # CJK compatibility ideographs
    "\uff00-\uffef"  # Half-width and full-width forms
    "\U00020000-\U0002a6df"  # CJK Extension B
    "]"
)


@dataclass
class Finding:
    check: str
    path: str
    line: int | None = None
    detail: str = ""


@dataclass
class Report:
    files_scanned: int = 0
    findings: list[Finding] = field(default_factory=list)

    def by_check(self, check: str) -> list[Finding]:
        return [f for f in self.findings if f.check == check]

    def to_dict(self) -> dict:
        checks = ["size", "forbidden-path", "absolute-path", "secret", "cjk"]
        return {
            "files_scanned": self.files_scanned,
            "counts": {c: len(self.by_check(c)) for c in checks},
            "cjk_files": sorted({f.path for f in self.by_check("cjk")}),
            "findings": [f.__dict__ for f in self.findings],
        }


def is_forbidden_path(rel: str, reading_assets: set[str] | None = None) -> str | None:
    """Return a reason when the relative POSIX path must not be published."""
    name = rel.rsplit("/", 1)[-1]
    if reading_assets and rel in reading_assets:
        return None
    if rel.lower().endswith(".pdf") and rel not in SELF_AUTHORED_PDFS and not (
        rel.startswith(MANUSCRIPT_FIGURES) and rel.count("/") == MANUSCRIPT_FIGURES.count("/")
    ):
        return "publisher PDF"
    if rel.startswith("02-fulltext/") and rel not in ALLOWED_IN_FULLTEXT and not (
        rel.count('/') == 2 and name == 'README.md'
    ):
        return "full-text transcription or figure"
    for prefix in FORBIDDEN_PREFIXES:
        if rel.startswith(prefix):
            return f"local-only folder {prefix}"
    if rel.startswith("99-archive/") and rel.lower().endswith(".zip"):
        return "historical archive"
    if name == ".env" or name.startswith(".env."):
        return "environment file"
    return None


def scan_text(rel: str, text: str, report: Report, source_text: bool = False) -> None:
    """Scan one decoded text file for path, secret, and CJK findings."""
    cjk_lines = 0
    for lineno, line in enumerate(text.splitlines(), start=1):
        for pattern in ABSOLUTE_PATH_PATTERNS:
            if pattern.search(re.sub(r'https?://[^\s<>]+', '', line)):
                report.findings.append(Finding("absolute-path", rel, lineno))
                break
        for pattern in SECRET_PATTERNS:
            if pattern.search(line):
                report.findings.append(
                    Finding("secret", rel, lineno, "possible credential (value not shown)")
                )
                break
        if not source_text and rel not in LOCALIZED_UI_PATHS and CJK_PATTERN.search(line):
            cjk_lines += 1
            if cjk_lines <= 3:
                report.findings.append(Finding("cjk", rel, lineno))
    if cjk_lines > 3:
        report.findings.append(Finding("cjk", rel, None, f"{cjk_lines} lines in total"))


def scan_files(root: Path, files: list[Path], size_limit: int = SIZE_LIMIT_BYTES) -> Report:
    report = Report()
    reading_assets = set(load_assets(root))
    for path in files:
        rel = path.relative_to(root).as_posix()
        report.files_scanned += 1
        size = path.stat().st_size
        if size > size_limit and rel not in reading_assets:
            report.findings.append(Finding("size", rel, None, f"{size / 1048576:.1f} MB"))
        reason = is_forbidden_path(rel, reading_assets)
        if reason:
            report.findings.append(Finding("forbidden-path", rel, None, reason))
        if is_text_path(path) and size <= size_limit:
            scan_text(rel, read_text(path), report, source_text=rel in reading_assets)
    return report


def failed(report: Report, cjk_mode: str) -> bool:
    hard = ["size", "forbidden-path", "absolute-path", "secret"]
    if any(report.by_check(c) for c in hard):
        return True
    return cjk_mode == "strict" and bool(report.by_check("cjk"))


def format_report(report: Report, cjk_mode: str) -> str:
    data = report.to_dict()
    lines = [f"Files scanned: {data['files_scanned']}"]
    for check, count in data["counts"].items():
        mode = "report-only" if check == "cjk" and cjk_mode == "report" else "strict"
        lines.append(f"  {check:<15} {count:>5}  ({mode})")
    for finding in report.findings:
        if finding.check == "cjk" and cjk_mode == "report":
            continue
        where = f"{finding.path}:{finding.line}" if finding.line else finding.path
        lines.append(f"  [{finding.check}] {where} {finding.detail}".rstrip())
    if data["cjk_files"]:
        lines.append(f"Files containing CJK text: {len(data['cjk_files'])}")
        if cjk_mode == "report":
            lines.extend(f"  {p}" for p in data["cjk_files"])
    lines.append("RESULT: " + ("FAIL" if failed(report, cjk_mode) else "PASS"))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    parser.add_argument("--cjk", choices=["report", "strict"], default="strict")
    parser.add_argument("--json", type=Path, help="write the full report as JSON")
    parser.add_argument("--size-limit-mb", type=float, default=50.0)
    args = parser.parse_args(argv)

    root = args.root.resolve()
    files = git_candidate_files(root)
    report = scan_files(root, files, int(args.size_limit_mb * 1024 * 1024))
    if args.json:
        args.json.write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")
    sys.stdout.write(format_report(report, args.cjk) + "\n")
    return 1 if failed(report, args.cjk) else 0


if __name__ == "__main__":
    raise SystemExit(main())
