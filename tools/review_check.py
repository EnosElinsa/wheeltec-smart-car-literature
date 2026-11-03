"""Validate review files against the template, the vocabulary, and the full text.

Checks per review:

* ``sections``: all template sections are present, in template order;
* ``metadata``: ID, DOI, official URL, theme folder, and local paths agree
  with ``06-data/paper-index.csv``;
* ``coding``: every coding field is present and uses allowed values;
* ``links``: relative links resolve and do not point to local-only files;
* ``excerpts``: every page-cited excerpt and claim excerpt occurs in the
  full-text Markdown (and, with ``--pdf``, on the cited PDF page +/- 1);
* ``results``: every key-result bullet cites a PDF page (a warning, not an
  error, for ``verification_level: light``);
* ``abstract``: the original abstract occurs in the full text, unless the
  verification log records ``abstract-waiver: <reason>``;
* ``log``: the verification log has a dated entry by the current host;
* ``language``: no CJK characters;
* ``legacy-path``: archived evidence paths are prefixed with the archive name;
* ``size``: a warning (not an error) when the review exceeds 25,000 bytes
  (UTF-8 with LF line endings, so the result does not depend on checkout).

Usage::

    python -m tools.review_check --all
    python -m tools.review_check 03-reviews/T1-perception-localization/2022-slip-aware-fusion-M39/review.md --pdf
    python -m tools.review_check --all --summary --json report.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from tools import vocab
from tools.check_public_tree import CJK_PATTERN
from tools.common import REPO_ROOT, read_text
from tools.library import SECTION_ORDER, Review, load_index, parse_review, review_paths, split_values
from tools.textnorm import NormalizedText, coverage, ngrams, normalize
from tools.pdftext import read_pdf_pages

VERIFICATION_HOSTS = ("Kiro", "Codex")
ARCHIVE_PREFIX = "99-archive/history-2026-10-25.zip::"
_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
_PAGE_RE = re.compile(r"\bpp?\. ?\d+")
_LEGACY_RE = re.compile(r"(?<![\w/])(?:expansions/2026-10-24/)?evidence/T\d")
_LOG_RE = re.compile(r"^- (\d{4}-\d{2}-\d{2}) \| host: (\S+) \| scope: .+ \| corrections: .+$")
MAX_SUMMARY_WORDS = 35
MAX_REVIEW_BYTES = 25_000


@dataclass
class Issue:
    check: str
    message: str
    line: int | None = None


@dataclass
class Result:
    path: str
    code: str
    issues: list[Issue] = field(default_factory=list)
    warnings: list[Issue] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.issues


class FullTextCache:
    def __init__(self) -> None:
        self._md: dict[Path, NormalizedText] = {}
        self._pdf: dict[Path, list[str]] = {}

    def markdown(self, path: Path) -> NormalizedText | None:
        if path not in self._md:
            if not path.is_file():
                return None
            self._md[path] = NormalizedText(read_text(path))
        return self._md[path]

    def pdf_pages(self, path: Path) -> list[str] | None:
        if path not in self._pdf:
            if not path.is_file():
                return None
            self._pdf[path] = [normalize(text) for text in read_pdf_pages(path)]
        return self._pdf[path]


def check_pdf_page(pages: list[str], excerpt: str, first: int, last: int) -> str:
    norm = normalize(excerpt)
    lo = max(first - 2, 0)
    hi = min(last + 1, len(pages))
    window = " ".join(pages[lo:hi])
    if norm in window:
        return "exact"
    if len(norm.split()) >= 7 and coverage(norm, ngrams(window.split(), 5), 5) >= 0.8:
        return "fuzzy"
    return "missing"


def check_review(path: Path, index: dict, cache: FullTextCache, use_pdf: bool = False) -> Result:
    rel = path.relative_to(REPO_ROOT).as_posix()
    review = parse_review(path)
    folder = path.parent.name
    folder_code = folder.rsplit("-", 1)[-1]
    result = Result(rel, review.code or folder_code)

    def issue(check: str, message: str, line: int | None = None) -> None:
        result.issues.append(Issue(check, message, line))

    def warn(check: str, message: str, line: int | None = None) -> None:
        result.warnings.append(Issue(check, message, line))

    _check_sections(review, issue)
    row = index.get(folder_code)
    if row is None:
        issue("metadata", f"folder code {folder_code} is not in paper-index.csv")
    else:
        _check_metadata(review, row, folder_code, path, issue)
    _check_coding(review, issue, warn)
    _check_links(review, path, issue)
    _check_text_rules(review, issue, warn)
    size = len(path.read_bytes().replace(b"\r\n", b"\n"))
    if size > MAX_REVIEW_BYTES:
        warn("size", f"review has {size:,} bytes; keep it at or below {MAX_REVIEW_BYTES:,} bytes")

    md_path = REPO_ROOT / row["markdown"] if row else None
    pdf_path = REPO_ROOT / row["pdf"] if row else None
    md = cache.markdown(md_path) if md_path else None
    if md is None:
        issue("excerpts", "full-text Markdown not found; excerpts cannot be verified")
    else:
        pages = cache.pdf_pages(pdf_path) if (use_pdf and pdf_path) else None
        if use_pdf and pages is None:
            warn("excerpts", "PDF not found; page check skipped")
        _check_excerpts(review, md, pages, issue, warn)
        _check_abstract(review, md, issue, warn)
    return result


def _check_sections(review: Review, issue) -> None:
    if not review.title:
        issue("sections", "missing level-1 title")
    found = [name for name, _, _ in review.sections]
    for name in found:
        if name not in SECTION_ORDER:
            issue("sections", f"unexpected section '## {name}'", review.section_line(name))
    expected = [name for name in SECTION_ORDER]
    missing = [name for name in expected if name not in found]
    for name in missing:
        issue("sections", f"missing section '## {name}'")
    known = [name for name in found if name in SECTION_ORDER]
    if not missing and known != expected:
        issue("sections", "sections are not in template order")
    for name in expected:
        if name in found and not review.section(name).strip():
            issue("sections", f"section '## {name}' is empty", review.section_line(name))
    survey = review.section("Survey-usable statements")
    if survey and ("### Supported" not in survey or "### Not supported" not in survey):
        issue("sections", "Survey-usable statements needs '### Supported' and '### Not supported'")


def _check_metadata(review: Review, row: dict, folder_code: str, path: Path, issue) -> None:
    meta = review.metadata
    for key in ["ID", "Title", "Authors", "Venue", "Year", "Type", "DOI", "Official URL",
                "Theme folder", "Batch", "Local files"]:
        if not meta.get(key):
            issue("metadata", f"metadata field '{key}' is missing or empty")
    if meta.get("ID") and meta["ID"] != folder_code:
        issue("metadata", f"ID {meta['ID']} does not match folder code {folder_code}")
    doi = (row.get("doi") or "").lower()
    meta_doi = meta.get("DOI", "").lower()
    if doi and doi not in meta_doi:
        issue("metadata", f"DOI does not match paper-index.csv ({doi})")
    if not doi and "none" not in meta_doi:
        issue("metadata", "paper has no DOI; write 'none (see official URL)'")
    url = (row.get("official_url") or "").strip()
    if url and url.rstrip("/") not in meta.get("Official URL", ""):
        issue("metadata", "Official URL does not match paper-index.csv")
    theme_folder = path.parent.parent.name
    if meta.get("Theme folder") and meta["Theme folder"] != theme_folder:
        issue("metadata", f"Theme folder should be {theme_folder}")
    local = meta.get("Local files", "")
    for column in ("pdf", "markdown"):
        if row.get(column) and row[column] not in local:
            issue("metadata", f"Local files should name {row[column]}")
    if review.title and row.get("title"):
        if normalize(review.title) != normalize(row["title"]):
            issue("metadata", "level-1 title differs from paper-index.csv title")


def _check_coding(review: Review, issue, warn) -> None:
    coding = review.coding
    for name, (allowed, multi, none_ok) in vocab.CODING_FIELDS.items():
        line = review.coding_lines.get(name)
        value = coding.get(name, "").strip()
        if not value:
            issue("coding", f"coding field '{name}' is missing or empty", line)
            continue
        if allowed is None:
            if name.startswith("summary_") and len(value.split()) > MAX_SUMMARY_WORDS:
                issue("coding", f"{name} has more than {MAX_SUMMARY_WORDS} words", line)
            continue
        values = split_values(value) if multi else [value]
        if multi and none_ok and values == ["none"]:
            continue
        if multi and "none" in values and len(values) > 1:
            issue("coding", f"{name}: 'none' cannot be combined with other values", line)
        for v in values:
            if v not in allowed:
                issue("coding", f"{name}: '{v}' is not an allowed value", line)
        if not multi and len(split_values(value)) > 1:
            issue("coding", f"{name} takes one value", line)
    for extra in set(coding) - set(vocab.CODING_FIELDS):
        issue("coding", f"unknown coding field '{extra}'", review.coding_lines.get(extra))

    ev, ev_all = coding.get("evidence_type", ""), split_values(coding.get("evidence_all", ""))
    if ev and ev_all and ev not in ev_all:
        issue("coding", "evidence_type must also appear in evidence_all")
    order = vocab.EVIDENCE[:7]
    ranked = [e for e in ev_all if e in order]
    if ev in order and ranked and order.index(ev) > min(order.index(e) for e in ranked):
        issue("coding", "evidence_type must be the strongest value in evidence_all")
    pri, allv = coding.get("evaluation_primary", ""), split_values(coding.get("evaluation_all", ""))
    if pri and allv and pri not in allv:
        issue("coding", "evaluation_primary must also appear in evaluation_all")
    pc, bp = coding.get("platform_class", ""), coding.get("boundary_platform", "")
    if pc in vocab.PLATFORMS and bp in vocab.YES_NO:
        expected = "no" if pc in vocab.WHEELED else "yes"
        if bp != expected:
            issue("coding", f"boundary_platform should be '{expected}' for platform_class {pc}")
    mod = coding.get("survey_module", "")
    if mod and mod in split_values(coding.get("secondary_modules", "")):
        issue("coding", "secondary_modules must not repeat survey_module")


def _check_links(review: Review, path: Path, issue) -> None:
    for lineno, line in enumerate(review.raw.splitlines(), start=1):
        for target in _LINK_RE.findall(line):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            clean = target.split("#", 1)[0]
            resolved = (path.parent / clean).resolve()
            try:
                rel = resolved.relative_to(REPO_ROOT).as_posix()
            except ValueError:
                issue("links", f"link leaves the repository: {target}", lineno)
                continue
            if rel.lower().endswith(".pdf") or (rel.startswith("02-fulltext/") and rel != "02-fulltext/INDEX.md"):
                issue("links", f"link to a local-only file (excluded from the public tree): {target}", lineno)
            elif not resolved.exists():
                issue("links", f"broken link: {target}", lineno)


def _check_text_rules(review: Review, issue, warn) -> None:
    for lineno, line in enumerate(review.raw.splitlines(), start=1):
        if CJK_PATTERN.search(line):
            issue("language", "CJK characters (the review must be in English)", lineno)
        for match in _LEGACY_RE.finditer(line):
            if ARCHIVE_PREFIX not in line[: match.start()] and "zip::" not in line[: match.start()]:
                issue("legacy-path", "archived evidence path without the archive prefix", lineno)
    results = review.section("Key quantitative results")
    start = review.section_line("Key quantitative results")
    light = review.coding.get("verification_level", "").strip() == "light"
    report = warn if light else issue
    for offset, line in enumerate(results.splitlines(), start=1):
        if line.startswith("- ") and not _PAGE_RE.search(line):
            report("results", "key result without a PDF page citation", start + offset + 1)
    log = review.section("Verification log")
    entries = [line for line in log.splitlines() if _LOG_RE.match(line)]
    if not any(_LOG_RE.match(line).group(2) in VERIFICATION_HOSTS for line in entries):
        issue("log", "verification log needs a dated entry with host: Kiro or host: Codex, scope, and corrections")


def _check_excerpts(review: Review, md: NormalizedText, pages, issue, warn) -> None:
    if not review.excerpts:
        issue("excerpts", "no page-cited excerpts found (format: - **p. N, Section.** \"text\")")
    for ex in review.excerpts:
        if "..." in ex.text or "\u2026" in ex.text:
            issue("excerpts", "excerpt contains an ellipsis; quote contiguous text", ex.line)
        status = md.match(ex.text)
        if status == "missing":
            issue("excerpts", f"excerpt not found in full text: \"{ex.text[:60]}\"", ex.line)
        elif status == "fuzzy":
            warn("excerpts", f"excerpt matched only approximately: \"{ex.text[:60]}\"", ex.line)
        if pages is not None:
            page_status = check_pdf_page(pages, ex.text, ex.page, ex.page_end)
            if page_status == "missing":
                issue("excerpts", f"excerpt not found on PDF p. {ex.page} (+/- 1)", ex.line)
            elif page_status == "fuzzy":
                warn("excerpts", f"excerpt matched PDF p. {ex.page} only approximately", ex.line)
    claims = {c.claim: c for c in review.claims}
    for claim in vocab.CLAIMS:
        if claim not in claims:
            issue("excerpts", f"claim table lacks row {claim}")
    for row in review.claims:
        if row.relation not in vocab.RELATIONS:
            issue("coding", f"{row.claim}: relation '{row.relation}' is not allowed", row.line)
        if row.strength not in vocab.STRENGTHS:
            issue("coding", f"{row.claim}: strength '{row.strength}' is not allowed", row.line)
        if row.relation == "unset":
            continue
        if not row.excerpt:
            issue("excerpts", f"{row.claim}: a non-unset relation needs an excerpt", row.line)
            continue
        status = md.match(row.excerpt)
        if status == "missing":
            issue("excerpts", f"{row.claim} excerpt not found in full text", row.line)
        elif status == "fuzzy":
            warn("excerpts", f"{row.claim} excerpt matched only approximately", row.line)


def _check_abstract(review: Review, md: NormalizedText, issue, warn) -> None:
    abstract = review.section("Original abstract")
    if not abstract:
        return
    log = review.section("Verification log")
    if "abstract-waiver:" in log:
        return
    norm = normalize(abstract)
    if norm and norm in md.text:
        return
    score = coverage(norm, md.grams, md.n)
    if score >= 0.85:
        if score < 0.97:
            warn("abstract", f"abstract matches the full text at {score:.0%}")
        return
    issue("abstract", f"abstract matches the full text at only {score:.0%}; copy it verbatim or add 'abstract-waiver: <reason>' to the log")


def run(paths: list[Path], use_pdf: bool) -> list[Result]:
    index = load_index()
    cache = FullTextCache()
    return [check_review(p, index, cache, use_pdf) for p in paths]


def summarize(results: list[Result]) -> str:
    failed = [r for r in results if not r.ok]
    counts = Counter(issue.check for r in results for issue in r.issues)
    lines = [f"Reviews checked: {len(results)}; passed: {len(results) - len(failed)}; failed: {len(failed)}"]
    for check, count in sorted(counts.items()):
        files = len({r.path for r in results for i in r.issues if i.check == check})
        lines.append(f"  {check:<12} {count:>5} issues in {files} reviews")
    return "\n".join(lines)


def details(results: list[Result]) -> str:
    out = []
    for r in results:
        if r.ok and not r.warnings:
            continue
        out.append(f"{r.path} [{r.code}] {'PASS' if r.ok else 'FAIL'}")
        for i in r.issues:
            out.append(f"  ERROR {i.check}{f' (line {i.line})' if i.line else ''}: {i.message}")
        for w in r.warnings:
            out.append(f"  warn  {w.check}{f' (line {w.line})' if w.line else ''}: {w.message}")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate review files.")
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--all", action="store_true", help="check every review under 03-reviews")
    parser.add_argument("--pdf", action="store_true", help="also check excerpt pages against the PDF")
    parser.add_argument("--summary", action="store_true", help="print only the summary")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args(argv)

    paths = review_paths() if args.all else [p.resolve() for p in args.paths]
    if not paths:
        parser.error("give review paths or --all")
    results = run(paths, args.pdf)
    if not args.summary:
        text = details(results)
        if text:
            sys.stdout.write(text + "\n")
    sys.stdout.write(summarize(results) + "\n")
    if args.json:
        payload = [
            {"path": r.path, "code": r.code, "ok": r.ok,
             "issues": [i.__dict__ for i in r.issues], "warnings": [w.__dict__ for w in r.warnings]}
            for r in results
        ]
        args.json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return 0 if all(r.ok for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
