"""Tests for tools.corpus: key-paper parsing and corpus loading."""

from __future__ import annotations

import shutil

import pytest

from tools import corpus, vocab
from tools.tests.conftest import PILOTS, UNCODED, UNCODED_FOLDER, UNCODED_THEME

STAR = corpus.STAR

TABLE_GUIDE = """# Guide
| ID | Why |
|---|---|
| [M39 · slip-aware-fusion](03-reviews/T1-perception-localization/2022-slip-aware-fusion-M39/review.md) | slip |
| [E10 · PL-VIWO](03-reviews/T1-perception-localization/2025-PL-VIWO-E10/review.md) | wheel |

- Route: M39 -> E10 -> X07 -> E51; see also [E36](03-reviews/T4/2026-Commerge-E36/review.md).
"""

STAR_GUIDE = f"""# Reading guide

{STAR} marks the key papers.

| ID | Why first |
|---|---|
| {STAR} [M39 · slip-aware-fusion](03-reviews/T1/2022-slip-aware-fusion-M39/review.md) | slip |
| [{STAR} E10 · PL-VIWO](03-reviews/T1/2025-PL-VIWO-E10/review.md) | wheel |
| **{STAR} X07** | integrity |
| E36 {STAR} | merging |
| [E01 · LODESTAR](03-reviews/T1/2026-LODESTAR-E01/review.md) | not a key paper |

- Route: M39 -> E10 -> X07.
"""


def test_key_papers_from_table_links():
    assert corpus.parse_key_papers(TABLE_GUIDE) == {"M39", "E10"}


def test_key_papers_from_star_markers():
    assert corpus.parse_key_papers(STAR_GUIDE) == {"M39", "E10", "X07", "E36"}


def test_star_legend_without_ids_marks_nothing():
    assert corpus.parse_key_papers(f"{STAR} marks key papers.\n| [M39 · x](a/review.md) |\n") == set()


def test_load_corpus_joins_coding_and_keys(corpus_root, capsys):
    entries = corpus.load_corpus(corpus_root)
    assert [e.code for e in entries][:1] == ["E01"]
    by_code = {e.code: e for e in entries}
    assert set(by_code) == set(PILOTS) | {UNCODED}
    assert {c for c, e in by_code.items() if e.key} == {"M39", "X07", "E36"}
    assert by_code["M39"].value("platform_class") == "skid-steer"
    assert by_code["M39"].theme == "T1-perception-localization"
    assert all(set(by_code[c].coding) == set(vocab.CODING_FIELDS) for c in PILOTS)
    assert by_code[UNCODED].coding == {}
    err = capsys.readouterr().err
    assert f"03-reviews/{UNCODED_THEME}/{UNCODED_FOLDER}/review.md" in err
    assert "warning" in err


def test_strict_rejects_review_without_coding(corpus_root):
    with pytest.raises(corpus.CorpusError) as info:
        corpus.load_corpus(corpus_root, strict=True)
    assert any(UNCODED_FOLDER in p for p in info.value.problems)


def test_missing_review_is_an_error(corpus_root):
    (corpus_root / f"03-reviews/{UNCODED_THEME}/{UNCODED_FOLDER}/review.md").unlink()
    with pytest.raises(corpus.CorpusError) as info:
        corpus.load_corpus(corpus_root)
    assert any("missing review" in p and UNCODED in p for p in info.value.problems)


def test_duplicate_review_is_an_error(corpus_root):
    source = corpus_root / "03-reviews/T1-perception-localization/2022-slip-aware-fusion-M39"
    copy = corpus_root / "03-reviews/T2-slam-mapping-exploration/2022-copy-M39"
    shutil.copytree(source, copy)
    with pytest.raises(corpus.CorpusError) as info:
        corpus.load_corpus(corpus_root)
    assert any("duplicate reviews for M39" in p for p in info.value.problems)
