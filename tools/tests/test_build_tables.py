"""Tests for tools.build_tables on the pilot fixture tree."""

from __future__ import annotations

import csv
import io

import pytest

from tools import build_tables as bt
from tools import corpus
from tools.library import parse_review
from tools.tests.conftest import PILOTS, UNCODED

HASHES = ["pdf_sha256", "bibtex_sha256", "markdown_sha256"]


def read_csv(data: bytes) -> list[list[str]]:
    return list(csv.reader(io.StringIO(data.decode("utf-8-sig"), newline="")))


def records(data: bytes) -> list[bytes]:
    return data.removeprefix(b"\xef\xbb\xbf").splitlines(keepends=True)


def test_comparison_table_has_one_row_per_review(corpus_root):
    data = bt.build(corpus_root)["corpus-comparison.csv"]
    assert data.startswith(b"\xef\xbb\xbf")
    rows = read_csv(data)
    assert rows[0] == bt.COLUMNS
    assert len(rows) - 1 == len(PILOTS) + 1
    table = {row[0]: dict(zip(bt.COLUMNS, row)) for row in rows[1:]}
    assert set(table) == set(PILOTS) | {UNCODED}
    m39 = table["M39"]
    coding = parse_review(corpus_root / "03-reviews/T1-perception-localization/2022-slip-aware-fusion-M39/review.md").coding
    assert m39["module"] == coding["survey_module"] == "localization-mapping"
    for column in bt.COLUMNS:
        if column in coding:
            assert m39[column] == coding[column], column
    assert (m39["theme"], m39["year"], m39["type"], m39["batch"], m39["key_paper"]) == (
        "T1-perception-localization", "2022", "journal", "baseline-2026-09-18", "yes")
    assert table["E01"]["key_paper"] == "no"
    assert table[UNCODED]["module"] == "" and table[UNCODED]["summary_result"] == ""
    assert table[UNCODED]["venue"] == "Test Venue, With Comma"
    assert bt.build(corpus_root)["corpus-comparison.csv"] == data


def test_paper_index_keeps_original_bytes_and_appends_coding(corpus_root):
    original = (corpus_root / "06-data" / "paper-index.csv").read_bytes()
    first = bt.build(corpus_root)["paper-index.csv"]
    assert first.startswith(b"\xef\xbb\xbf") == original.startswith(b"\xef\xbb\xbf")
    before, after = records(original), records(first)
    assert len(before) == len(after)
    for old, new in zip(before, after):
        body = old.rstrip(b"\r\n")
        assert new.startswith(body + b","), old[:40]
        assert new[len(new.rstrip(b"\r\n")):] == old[len(body):]  # same line ending
    old_rows, new_rows = read_csv(original), read_csv(first)
    width = len(old_rows[0])
    assert new_rows[0] == old_rows[0] + bt.INDEX_COLUMNS
    for old, new in zip(old_rows, new_rows):
        assert new[:width] == old
    header = old_rows[0]
    for name in HASHES:
        column = header.index(name)
        assert [r[column] for r in new_rows] == [r[column] for r in old_rows]
    m39 = next(dict(zip(new_rows[0], r)) for r in new_rows[1:] if r[0] == "M39")
    assert m39["survey_module"] == "localization-mapping"
    assert m39["platform_class"] == "skid-steer"


def test_rerun_does_not_duplicate_columns(corpus_root, tmp_path):
    out = tmp_path / "out"
    assert bt.main(["--root", str(corpus_root), "--out", str(out)]) == 0
    first = (out / "paper-index.csv").read_bytes()
    (corpus_root / "06-data" / "paper-index.csv").write_bytes(first)
    assert bt.main(["--root", str(corpus_root), "--out", str(out)]) == 0
    second = (out / "paper-index.csv").read_bytes()
    assert second == first
    header = read_csv(second)[0]
    assert len(header) == len(set(header))


def test_main_writes_only_to_the_output_folder(corpus_root, tmp_path):
    index = corpus_root / "06-data" / "paper-index.csv"
    original = index.read_bytes()
    out = tmp_path / "tables"
    assert bt.main(["--root", str(corpus_root), "--out", str(out)]) == 0
    assert sorted(p.name for p in out.iterdir()) == ["corpus-comparison.csv", "paper-index.csv"]
    assert index.read_bytes() == original
    assert not (corpus_root / "06-data" / "corpus-comparison.csv").exists()


def test_strict_and_corpus_errors_fail(corpus_root, tmp_path):
    assert bt.main(["--root", str(corpus_root), "--out", str(tmp_path / "a"), "--strict"]) == 1
    (corpus_root / "03-reviews/T1-perception-localization/2026-LODESTAR-E01/review.md").unlink()
    with pytest.raises(corpus.CorpusError):
        bt.build(corpus_root)
    assert bt.main(["--root", str(corpus_root), "--out", str(tmp_path / "b")]) == 1
    assert not (tmp_path / "b").exists()


def test_misplaced_coding_columns_are_rejected():
    text = "code,survey_module,title\r\nM39,x,y\r\n"
    with pytest.raises(ValueError):
        bt.append_coding(text, {})


def test_quoted_fields_keep_their_bytes():
    text = 'code,title,pdf_sha256\r\nM39,"A, ""quoted"" title",abc\r\n'
    out = bt.append_coding(text, {"M39": {"survey_module": "multi-robot"}})
    lines = out.split("\r\n")
    assert lines[1].startswith('M39,"A, ""quoted"" title",abc,multi-robot,')
    assert bt.append_coding(out, {"M39": {"survey_module": "multi-robot"}}) == out
