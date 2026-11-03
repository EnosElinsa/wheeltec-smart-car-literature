"""Tests for tools.build_indexes on the pilot fixture tree."""

from __future__ import annotations

import posixpath
import re

from tools import build_indexes as bi
from tools.check_links import extract_links
from tools.check_public_tree import CJK_PATTERN
from tools.corpus import STAR

EXPECTED = {
    "06-data/library-catalog.csv",
    "01-papers/INDEX.md",
    "02-fulltext/INDEX.md",
    "03-reviews/INDEX.md",
    "01-papers/T1-perception-localization/README.md",
    "01-papers/T4-multi-robot-coordination/README.md",
    "03-reviews/T1-perception-localization/README.md",
    "03-reviews/T4-multi-robot-coordination/README.md",
    "02-fulltext/T1-perception-localization/README.md",
}


def test_generates_indexes_and_existing_theme_readmes_only(corpus_root):
    assert set(bi.build(corpus_root)) == EXPECTED


def test_output_is_deterministic_and_english(corpus_root):
    first, second = bi.build(corpus_root), bi.build(corpus_root)
    assert first == second
    for text in first.values():
        assert not CJK_PATTERN.search(text)
        assert not re.search(r"\b20\d\d-\d\d-\d\d\b", text)


def test_rows_show_metadata_coding_and_key_flag(corpus_root):
    page = bi.build(corpus_root)["03-reviews/INDEX.md"]
    m39 = next(line for line in page.splitlines() if " M39 |" in line)
    assert m39.startswith(f"| {STAR} M39 | 2022 | Robust Slip-Aware Fusion")
    for value in ("journal", "localization-mapping", "online-hardware", "skid-steer"):
        assert f"| {value} |" in m39
    assert "[DOI](https://doi.org/10.1109/lra.2022.3184768)" in m39
    assert "[Official page](https://ieeexplore.ieee.org/document/9801647/)" in m39
    e01 = next(line for line in page.splitlines() if " E01 |" in line)
    assert e01.startswith("| E01 | 2026 |")
    uncoded = next(line for line in page.splitlines() if " M98 |" in line)
    assert "| journal |  |  |  |" in uncoded
    assert "Test Venue, With Comma" in uncoded
    x07 = next(line for line in page.splitlines() if " X07 |" in line)
    assert "[Official page]" not in x07  # the official URL is the DOI link
    assert "## T1-perception-localization · 3" in page


def test_links_only_to_reviews_bibtex_and_external(corpus_root):
    pages = bi.build(corpus_root)
    allowed_pages = {"README.md", "READING_GUIDE.md", "INDEX.md", "TEMPLATE.md", "WORKFLOW.md", "vocabulary.md"}
    for rel, text in pages.items():
        for _, target in extract_links(text):
            if target.startswith("https://"):
                continue
            name = posixpath.basename(target)
            assert name in {"review.md", "citation.bib"} | allowed_pages, (rel, target)
            if name in {"review.md", "citation.bib"}:
                resolved = (corpus_root / rel).parent / target
                assert resolved.is_file(), (rel, target)
        if " M39 |" in text:
            folder = "T1-perception-localization/2022-slip-aware-fusion-M39"
            assert f"| `01-papers/{folder}/paper.pdf` · `02-fulltext/{folder}/paper.md` |" in text


def test_uncoded_review_warns_and_strict_fails(corpus_root, tmp_path, capsys):
    out = tmp_path / "out"
    assert bi.main(["--root", str(corpus_root), "--out", str(out)]) == 0
    assert "2023-uncoded-M98/review.md" in capsys.readouterr().err
    assert (out / "03-reviews" / "INDEX.md").is_file()
    assert (corpus_root / "03-reviews" / "T1-perception-localization" / "README.md").read_text() == "# old\n"
    assert bi.main(["--root", str(corpus_root), "--out", str(tmp_path / "strict"), "--strict"]) == 1
    assert not (tmp_path / "strict").exists()
