"""Load the reviewed corpus for the index and table generators.

Each row of ``06-data/paper-index.csv`` is joined with the survey coding of its
review (``03-reviews/TEMPLATE.md`` format) and with the key-paper flag of
``READING_GUIDE.md``. Used by ``tools.build_indexes`` and ``tools.build_tables``.

* Every index row needs its review file, and every review folder code must
  occur once in the index; otherwise ``CorpusError`` lists the problems.
* A review whose ``## Survey coding`` block is missing or lacks a field keeps
  an empty coding, and a warning naming the file goes to stderr. With
  ``strict=True`` this is an error instead.
* Key papers are the IDs next to a star marker (U+2605), for example
  ``| ★ M39 |`` or ``[★ M39 · slip-aware-fusion](...)``. A guide without any
  star (the 2026-10-25 format) marks key papers as table rows whose first
  cell links an ID to its review, for example ``| [M39 · name](.../review.md) |``.
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from tools import vocab
from tools.common import REPO_ROOT, read_text
from tools.library import parse_review

INDEX_REL = "06-data/paper-index.csv"
GUIDE_REL = "READING_GUIDE.md"
STAR = "\u2605"
_ID = r"[A-Z]\d{2,3}"
_STAR_BEFORE = re.compile(STAR + r"[\s\[*_`]*(" + _ID + r")\b")
_STAR_AFTER = re.compile(r"\b(" + _ID + r")[\s\]*_`]*" + STAR)
_REVIEW_ROW = re.compile(r"^\|\s*\[\s*(" + _ID + r")\b[^\]]*\]\([^)]*review\.md\)")


class CorpusError(Exception):
    def __init__(self, problems: list[str]):
        super().__init__("\n".join(problems))
        self.problems = problems


@dataclass
class Entry:
    row: dict[str, str]
    theme: str
    review: Path | None
    key: bool
    coding: dict[str, str] = field(default_factory=dict)

    @property
    def code(self) -> str:
        return self.row["code"]

    def value(self, name: str) -> str:
        return self.coding.get(name, "")


def read_index(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_key_papers(text: str) -> set[str]:
    """Return the IDs marked as key papers in a reading guide."""
    lines = text.splitlines()
    if STAR in text:
        found = set()
        for line in lines:
            found.update(m.group(1) for m in _STAR_BEFORE.finditer(line))
            found.update(m.group(1) for m in _STAR_AFTER.finditer(line))
        return found
    return {m.group(1) for line in lines if (m := _REVIEW_ROW.match(line))}


def read_coding(path: Path) -> tuple[dict[str, str], list[str]]:
    """Return the complete coding of a review, or ``({}, missing fields)``."""
    coding = parse_review(path).coding
    missing = [name for name in vocab.CODING_FIELDS if not coding.get(name, "").strip()]
    if missing:
        return {}, missing
    return {name: coding[name].strip() for name in vocab.CODING_FIELDS}, []


def load_corpus(root: Path = REPO_ROOT, strict: bool = False) -> list[Entry]:
    """Return one entry per index row, in index order."""
    rows = read_index(root / INDEX_REL)
    problems: list[str] = []
    codes = [row["code"] for row in rows]
    for code in sorted({c for c in codes if codes.count(c) > 1}):
        problems.append(f"{INDEX_REL} lists {code} more than once")

    found: dict[str, list[Path]] = {}
    for path in sorted((root / "03-reviews").glob("T*/*/review.md")):
        found.setdefault(path.parent.name.rsplit("-", 1)[-1], []).append(path)
    for code, paths in sorted(found.items()):
        names = ", ".join(p.relative_to(root).as_posix() for p in paths)
        if len(paths) > 1:
            problems.append(f"duplicate reviews for {code}: {names}")
        if code not in codes:
            problems.append(f"review without a row in {INDEX_REL}: {names}")

    guide = root / GUIDE_REL
    keys = parse_key_papers(read_text(guide)) if guide.is_file() else set()
    entries = []
    for row in rows:
        path = root / row["review"]
        if not path.is_file():
            problems.append(f"missing review for {row['code']}: {row['review']}")
            continue
        coding, missing = read_coding(path)
        if missing:
            what = "no Survey coding block" if len(missing) == len(vocab.CODING_FIELDS) \
                else "Survey coding lacks " + ", ".join(missing)
            message = f"{row['review']}: {what}; coding left empty"
            if strict:
                problems.append(message)
            else:
                sys.stderr.write(f"warning: {message}\n")
        theme = Path(row["review"]).parts[1]
        entries.append(Entry(row, theme, path, row["code"] in keys, coding))
    if problems:
        raise CorpusError(problems)
    return entries
