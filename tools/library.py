"""Read the paper index and parse review files.

The parser is deliberately simple: a review is a sequence of ``## `` sections
(see ``03-reviews/TEMPLATE.md``). Structured parts (metadata table, survey
coding list, claim table, excerpts) are parsed with line-oriented rules.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path

from tools.common import REPO_ROOT, read_text

INDEX_CSV = REPO_ROOT / "06-data" / "paper-index.csv"

SECTION_ORDER = [
    "Metadata",
    "Survey coding",
    "Problem",
    "Mechanism",
    "Baselines and controls",
    "Platform and setup",
    "Evidence type and transfer",
    "Sensors",
    "Compute and latency",
    "Key quantitative results",
    "Stated limitations",
    "Transfer conditions",
    "Code and data",
    "Version family",
    "Claim relations",
    "Page-cited excerpts",
    "Survey-usable statements",
    "Verification log",
    "Original abstract",
]

_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
_CODING_RE = re.compile(r"^- ([a-z_]+):\s*(.*?)\s*$")
_EXCERPT_RE = re.compile(
    r'^- \*\*pp?\. ?(?P<page>\d+)(?:\s*[-\u2013]\s*(?P<page2>\d+))?(?:,\s*(?P<where>[^*]*?))?\.?\*\*\s*"(?P<text>.+)"\s*$'
)


@dataclass
class Excerpt:
    page: int
    page_end: int
    where: str
    text: str
    line: int


@dataclass
class ClaimRow:
    claim: str
    relation: str
    strength: str
    location: str
    excerpt: str
    line: int


@dataclass
class Review:
    path: Path
    title: str = ""
    sections: list[tuple[str, str, int]] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)
    coding: dict[str, str] = field(default_factory=dict)
    coding_lines: dict[str, int] = field(default_factory=dict)
    claims: list[ClaimRow] = field(default_factory=list)
    excerpts: list[Excerpt] = field(default_factory=list)
    raw: str = ""

    def section(self, name: str) -> str:
        for heading, body, _ in self.sections:
            if heading == name:
                return body
        return ""

    def section_line(self, name: str) -> int:
        for heading, _, line in self.sections:
            if heading == name:
                return line
        return 0

    @property
    def code(self) -> str:
        return self.metadata.get("ID", "")


def load_index(path: Path = INDEX_CSV) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return {row["code"]: row for row in csv.DictReader(handle)}


def strip_cell(value: str) -> str:
    return value.strip().strip("`").strip()


def parse_review(path: Path) -> Review:
    raw = read_text(path)
    review = Review(path=path, raw=raw)
    text = _COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), raw)
    lines = text.splitlines()

    current: str | None = None
    start = 0
    buffer: list[str] = []
    for lineno, line in enumerate(lines, start=1):
        if line.startswith("# ") and not review.title:
            review.title = line[2:].strip()
            continue
        if line.startswith("## "):
            if current is not None:
                review.sections.append((current, "\n".join(buffer).strip(), start))
            current = line[3:].strip()
            start = lineno
            buffer = []
            continue
        if current is not None:
            buffer.append(line)
    if current is not None:
        review.sections.append((current, "\n".join(buffer).strip(), start))

    _parse_metadata(review, lines)
    _parse_coding(review, lines)
    _parse_claims(review, lines)
    _parse_excerpts(review, lines)
    return review


def _section_lines(review: Review, lines: list[str], name: str):
    start = review.section_line(name)
    if not start:
        return
    for lineno in range(start + 1, len(lines) + 1):
        line = lines[lineno - 1]
        if line.startswith("## "):
            break
        yield lineno, line


def _parse_metadata(review: Review, lines: list[str]) -> None:
    for _, line in _section_lines(review, lines, "Metadata"):
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Field"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2:
            review.metadata[cells[0]] = "|".join(cells[1:]).strip()


def _parse_coding(review: Review, lines: list[str]) -> None:
    for lineno, line in _section_lines(review, lines, "Survey coding"):
        match = _CODING_RE.match(line)
        if match:
            review.coding[match.group(1)] = match.group(2)
            review.coding_lines[match.group(1)] = lineno


def _parse_claims(review: Review, lines: list[str]) -> None:
    for lineno, line in _section_lines(review, lines, "Claim relations"):
        if not re.match(r"^\|\s*C\d", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        cells += [""] * (5 - len(cells))
        excerpt = cells[4].strip()
        if excerpt.startswith('"') and excerpt.endswith('"') and len(excerpt) >= 2:
            excerpt = excerpt[1:-1]
        review.claims.append(
            ClaimRow(cells[0], strip_cell(cells[1]), strip_cell(cells[2]), cells[3], excerpt, lineno)
        )


def _parse_excerpts(review: Review, lines: list[str]) -> None:
    for lineno, line in _section_lines(review, lines, "Page-cited excerpts"):
        match = _EXCERPT_RE.match(line)
        if match:
            page = int(match.group("page"))
            page_end = int(match.group("page2") or page)
            review.excerpts.append(
                Excerpt(page, page_end, (match.group("where") or "").strip(), match.group("text"), lineno)
            )


def split_values(value: str) -> list[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


def review_paths(root: Path = REPO_ROOT) -> list[Path]:
    return sorted((root / "03-reviews").glob("T*/*/review.md"))
