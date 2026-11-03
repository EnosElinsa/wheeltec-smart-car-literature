"""Acquired sources share navigation without gaining fabricated review status."""
import csv
import hashlib
import io
import json

import pytest

from tools.build_indexes import build
from tools.catalog import CATALOG_REL
from tools.corpus import CorpusError


def add_source(root, **changes):
    folder = "T1-perception-localization/2023-source-N01"
    record = {
        "id": "N01", "theme": "T1", "title": "A registered source", "year": 2023,
        "venue": "A Journal", "publication_type": "journal-article", "doi": "10.0000/source",
        "acquisition_status": "delivered", "read_scope": "targeted-source-reading",
        "pdf": f"01-papers/{folder}/paper.pdf", "bibtex": f"01-papers/{folder}/citation.bib",
        "markdown": f"02-fulltext/{folder}/paper.md", "pdf_sha256": "a" * 64,
        "bibtex_sha256": "b" * 64, "markdown_sha256": "c" * 64,
    }
    record.update(changes)
    batch = root / "06-data/acquisition-records"
    batch.mkdir(exist_ok=True)
    (batch / "manifest.json").write_text(json.dumps({"records": [record]}), encoding="utf-8")
    (batch / "evidence-notes.md").write_text("# Source notes\n", encoding="utf-8")
    return record


def test_all_sources_share_theme_index_without_entering_survey(corpus_root):
    index = corpus_root / "06-data/paper-index.csv"
    original = hashlib.sha256(index.read_bytes()).hexdigest()
    add_source(corpus_root)
    pages = build(corpus_root)
    for section in ("01-papers", "02-fulltext"):
        page = pages[f"{section}/INDEX.md"]
        assert "## T1-perception-localization · 4" in page
        row = next(line for line in page.splitlines() if line.startswith("| N01 |"))
        assert "Targeted source notes" in row and "[Source notes]" in row
        assert "[Review]" not in row
    assert "| N01 |" not in pages["03-reviews/INDEX.md"]
    catalog = list(csv.DictReader(io.StringIO(pages[CATALOG_REL])))
    source = next(row for row in catalog if row["code"] == "N01")
    assert source["survey_selected"] == "no" and source["review"] == ""
    assert hashlib.sha256(index.read_bytes()).hexdigest() == original


@pytest.mark.parametrize("changes", [{"id": "M39"}, {"doi": "10.1109/lra.2022.3184768"}])
def test_reject_duplicate_library_identities(corpus_root, changes):
    add_source(corpus_root, **changes)
    with pytest.raises(CorpusError, match="duplicate library identity"):
        build(corpus_root)


def test_pending_downloads_do_not_appear_as_registered_sources(corpus_root):
    add_source(corpus_root, acquisition_status="pending")
    assert "| N01 |" not in build(corpus_root)["01-papers/INDEX.md"]


def test_acquired_source_can_be_reviewed_without_duplicate_catalog_row(corpus_root):
    index = corpus_root / "06-data/paper-index.csv"
    row = next(r for r in csv.DictReader(index.open(encoding="utf-8-sig")) if r["code"] == "M39")
    fields = ("pdf", "bibtex", "markdown", "pdf_sha256", "bibtex_sha256", "markdown_sha256")
    add_source(corpus_root, id=row["code"], doi=row["doi"], **{f: row[f] for f in fields})
    pages = build(corpus_root)
    catalog = list(csv.DictReader(io.StringIO(pages[CATALOG_REL])))
    matched = [r for r in catalog if r["code"] == "M39"]
    assert len(matched) == 1
    assert matched[0]["survey_selected"] == "yes" and matched[0]["review"] == row["review"]
    assert matched[0]["source_notes"].endswith("evidence-notes.md")


def test_reviewed_overlap_rejects_changed_source_hash(corpus_root):
    row = next(r for r in csv.DictReader((corpus_root / "06-data/paper-index.csv").open(encoding="utf-8-sig")) if r["code"] == "M39")
    fields = ("pdf", "bibtex", "markdown", "pdf_sha256", "bibtex_sha256", "markdown_sha256")
    source = {f: row[f] for f in fields}
    source["pdf_sha256"] = "0" * 64
    add_source(corpus_root, id=row["code"], doi=row["doi"], **source)
    with pytest.raises(CorpusError, match="conflicting sources"):
        build(corpus_root)
