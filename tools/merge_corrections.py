"""Merge per-paper correction fragments into 06-data/review-corrections.csv.

Reviewers write correction rows for one paper to ``tmp/corrections/<ID>.csv``
(no header; columns ``id, section, issue, old_summary, corrected, pdf_page,
evidence``). This tool validates the fragments and merges them into the
library table, replacing earlier rows of the same paper.

Usage::

    python -m tools.merge_corrections            # merge all fragments
    python -m tools.merge_corrections --check    # validate only
"""

from __future__ import annotations

import argparse
import csv
import io
import sys

from tools.check_public_tree import CJK_PATTERN
from tools.common import REPO_ROOT, read_text
from tools.library import load_index

COLUMNS = ["id", "section", "issue", "old_summary", "corrected", "pdf_page", "evidence"]
TABLE = REPO_ROOT / "06-data" / "review-corrections.csv"
FRAGMENTS = REPO_ROOT / "tmp" / "corrections"


def read_rows(text: str) -> list[list[str]]:
    return [row for row in csv.reader(io.StringIO(text)) if any(cell.strip() for cell in row)]


def validate_fragment(code: str, rows: list[list[str]]) -> list[str]:
    errors = []
    for n, row in enumerate(rows, start=1):
        if row == COLUMNS:
            errors.append(f"{code}: row {n} is a header; fragments have no header")
            continue
        if len(row) != len(COLUMNS):
            errors.append(f"{code}: row {n} has {len(row)} columns, expected {len(COLUMNS)}")
            continue
        if row[0] != code:
            errors.append(f"{code}: row {n} has id {row[0]}")
        if any(CJK_PATTERN.search(cell) for cell in row):
            errors.append(f"{code}: row {n} contains CJK text")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Merge correction fragments.")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    order = list(load_index())
    existing: dict[str, list[list[str]]] = {}
    if TABLE.exists():
        rows = read_rows(read_text(TABLE))
        for row in rows[1:]:
            existing.setdefault(row[0], []).append(row)

    errors: list[str] = []
    merged = 0
    for fragment in sorted(FRAGMENTS.glob("*.csv")) if FRAGMENTS.exists() else []:
        code = fragment.stem
        rows = read_rows(read_text(fragment))
        problems = validate_fragment(code, rows)
        errors.extend(problems)
        if not problems:
            existing[code] = rows
            merged += 1

    if errors:
        sys.stdout.write("\n".join(errors) + "\n")
    if args.check:
        return 1 if errors else 0

    def sort_key(code: str):
        return (order.index(code) if code in order else len(order), code)

    out = io.StringIO()
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(COLUMNS)
    for code in sorted(existing, key=sort_key):
        writer.writerows(existing[code])
    TABLE.write_text(out.getvalue(), encoding="utf-8")
    total = sum(len(v) for v in existing.values())
    sys.stdout.write(f"merged {merged} fragments; table has {total} rows for {len(existing)} papers\n")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
