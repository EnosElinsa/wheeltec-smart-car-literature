"""Generate the corpus comparison table and append the coding to paper-index.csv.

``06-data/corpus-comparison.csv`` has exactly one row per review, in
``paper-index.csv`` order, with the columns in ``COLUMNS``. Bibliographic
fields (title, year, venue, type, batch) come from ``paper-index.csv``
(``year`` is the bibliographic year), the coding fields from the review's
Survey coding block, ``theme`` is the theme folder, and ``key_paper`` is
``yes`` for the key papers of ``READING_GUIDE.md``. A missing or duplicate
review is an error (see ``tools.corpus``). The file is UTF-8 with BOM and CRLF
line endings, like the other tables in ``06-data``.

Decision on ``paper-index.csv``: the coding is also appended to it. Before
this tool was written, every consumer of the file was searched for in
``tools/``, ``tools/tests/``, and all other scripts of the repository
(``05-survey/manuscript`` excluded). The only reader is
``tools.library.load_index`` (used by ``review_check``, ``locate``, and
``merge_corrections``), which reads the file with ``csv.DictReader`` by column
name; no consumer reads columns by position, so columns added after the last
existing column cannot break any of them. The existing columns, their order,
and every byte of their values, including the ``pdf_sha256``,
``bibtex_sha256``, and ``markdown_sha256`` hashes, stay unchanged: the tool
copies the raw text of the original columns of each record and adds a comma
and the new values before the record's own line ending. The appended columns
(``INDEX_COLUMNS``) form one trailing block; a rerun replaces that block, so
columns are never duplicated.

Usage::

    python -m tools.build_tables                     # write into 06-data/
    python -m tools.build_tables --out tmp/tables    # write both files elsewhere
    python -m tools.build_tables --strict            # uncoded reviews are errors
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
from pathlib import Path

from tools import vocab
from tools.common import REPO_ROOT
from tools.corpus import INDEX_REL, CorpusError, Entry, load_corpus

COLUMNS = [
    "code", "theme", "module", "secondary_modules", "title", "year", "venue", "type", "batch",
    "evidence_type", "evidence_all", "protocol_caveats", "platform_class", "platform",
    "boundary_platform", "sensors", "compute", "compute_location", "degradation",
    "degradation_observed", "evaluation_primary", "evaluation_all", "summary_result",
    "summary_limitation", "survey_included", "verification_level", "key_paper",
]
INDEX_COLUMNS = list(vocab.CODING_FIELDS)
BOM = "\ufeff"


def comparison_rows(entries: list[Entry]) -> list[list[str]]:
    rows = []
    for e in entries:
        fixed = {
            "code": e.code,
            "theme": e.theme,
            "module": e.value("survey_module"),
            "title": e.row.get("title", ""),
            "year": e.row.get("bibliographic_year", ""),
            "venue": e.row.get("venue", ""),
            "type": e.row.get("publication_type", ""),
            "batch": e.row.get("source_batch", ""),
            "key_paper": "yes" if e.key else "no",
        }
        rows.append([fixed[c] if c in fixed else e.value(c) for c in COLUMNS])
    return rows


def comparison_csv(entries: list[Entry]) -> str:
    out = io.StringIO()
    writer = csv.writer(out, lineterminator="\r\n")
    writer.writerow(COLUMNS)
    writer.writerows(comparison_rows(entries))
    return BOM + out.getvalue()


def _records(text: str) -> list[tuple[str, str, list[int]]]:
    """Split CSV text into (record text, line ending, offsets of separating commas)."""
    records = []
    start, commas, quoted, field_start = 0, [], False, True
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if quoted:
            if ch == '"':
                if i + 1 < n and text[i + 1] == '"':
                    i += 1
                else:
                    quoted = False
        elif ch == '"' and field_start:
            quoted = True
        elif ch == ",":
            commas.append(i - start)
            field_start = True
            i += 1
            continue
        elif ch in "\r\n":
            end = i
            if ch == "\r" and i + 1 < n and text[i + 1] == "\n":
                i += 1
            records.append((text[start:end], text[end:i + 1], commas))
            start, commas, field_start = i + 1, [], True
            i += 1
            continue
        field_start = False
        i += 1
    if start < n:
        records.append((text[start:], "", commas))
    return records


def _join(values: list[str]) -> str:
    out = io.StringIO()
    csv.writer(out, lineterminator="").writerow(values)
    return out.getvalue()


def append_coding(text: str, coding: dict[str, dict[str, str]]) -> str:
    """Return the index text with the coding block appended (or replaced)."""
    bom = text.startswith(BOM)
    records = _records(text[1:] if bom else text)
    header = next(csv.reader([records[0][0]]))
    k = len(INDEX_COLUMNS)
    if any(c in header for c in INDEX_COLUMNS):
        if header[-k:] != INDEX_COLUMNS or any(c in header[:-k] for c in INDEX_COLUMNS):
            raise ValueError("paper-index.csv has coding columns outside one trailing block")
        width = len(header) - k
    else:
        width = len(header)
    code_col = header.index("code")
    out = []
    for number, (body, ending, commas) in enumerate(records):
        if number and not body.strip():
            out.append(body + ending)
            continue
        if len(commas) < width - 1:
            raise ValueError(f"paper-index.csv record {number + 1} has fewer columns than the header")
        prefix = body[:commas[width - 1]] if len(commas) >= width else body
        if number == 0:
            values = INDEX_COLUMNS
        else:
            code = next(csv.reader([prefix]))[code_col]
            values = [coding.get(code, {}).get(c, "") for c in INDEX_COLUMNS]
        out.append(prefix + "," + _join(values) + ending)
    return (BOM if bom else "") + "".join(out)


def build(root: Path = REPO_ROOT, strict: bool = False) -> dict[str, bytes]:
    """Return {file name: bytes} for corpus-comparison.csv and paper-index.csv."""
    entries = load_corpus(root, strict)
    index_text = (root / INDEX_REL).read_bytes().decode("utf-8")
    coding = {e.code: e.coding for e in entries}
    return {
        "corpus-comparison.csv": comparison_csv(entries).encode("utf-8"),
        "paper-index.csv": append_coding(index_text, coding).encode("utf-8"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate corpus-comparison.csv and extend paper-index.csv.")
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="library root to read")
    parser.add_argument("--out", type=Path, help="output folder (default: <root>/06-data)")
    parser.add_argument("--strict", action="store_true", help="treat reviews without coding as errors")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    try:
        files = build(root, args.strict)
    except (CorpusError, ValueError) as error:
        problems = error.problems if isinstance(error, CorpusError) else [str(error)]
        sys.stderr.write("".join(f"error: {p}\n" for p in problems))
        return 1
    out = (args.out or root / "06-data").resolve()
    out.mkdir(parents=True, exist_ok=True)
    for name, data in sorted(files.items()):
        (out / name).write_bytes(data)
    rows = len(list(csv.reader(io.StringIO(files["corpus-comparison.csv"].decode("utf-8-sig"))))) - 1
    sys.stdout.write(f"wrote corpus-comparison.csv ({rows} rows) and paper-index.csv to {out.as_posix()}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
