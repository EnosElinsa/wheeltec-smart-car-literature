"""Acquired sources share navigation without gaining fabricated review status."""
import csv
import hashlib
import io
import json
import re

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


def test_internal_reference_keeps_review_and_sources_without_manuscript_membership(corpus_root):
    index = corpus_root / '06-data/paper-index.csv'
    before = index.read_bytes()
    rows = list(csv.DictReader(index.open(encoding='utf-8-sig')))
    internal = next(r for r in rows if r['code'] == 'M39')
    (corpus_root / '06-data/survey-inclusion.json').write_text(json.dumps({
        'selected_ids': [r['code'] for r in rows if r['code'] != 'M39'],
        'internal_reference_ids': ['M39'],
    }), encoding='utf-8')
    pages = build(corpus_root)
    catalog = list(csv.DictReader(io.StringIO(pages[CATALOG_REL])))
    retained = next(r for r in catalog if r['code'] == 'M39')
    assert retained['survey_selected'] == 'no'
    assert retained['review'] == internal['review'] and retained['pdf'] == internal['pdf']
    assert 'internal reference' in retained['assessment']
    assert 'M39' in pages['03-reviews/INDEX.md']
    assert index.read_bytes() == before


@pytest.mark.parametrize("state,fields,label", [
    ("registered_with_derived_citation", {"citation_status": "derived", "citation_source": "publisher RIS, confirmed against Crossref"}, "derived citation"),
    ("registered_with_title_variant", {"citation_status": "publisher-raw", "identity_status": "publisher-title-variant-reviewed"}, "publisher title variant"),
])
def test_documented_citation_exceptions_are_visible_without_review_status(corpus_root, state, fields, label):
    add_source(corpus_root, acquisition_status=state, read_scope="not-read", **fields)
    pages = build(corpus_root)
    row = next(line for line in pages["01-papers/INDEX.md"].splitlines() if line.startswith("| N01 |"))
    assert label in row and "[Source notes]" in row
    assert "| N01 |" not in pages["03-reviews/INDEX.md"]
    source = next(r for r in csv.DictReader(io.StringIO(pages[CATALOG_REL])) if r["code"] == "N01")
    assert source["survey_selected"] == "no" and source["review"] == ""
    assert all(source[key] == value for key, value in fields.items() if key in {"citation_status", "identity_status"})


@pytest.mark.parametrize("state,error", [
    ("registered_with_derived_citation", "lacks source attribution"),
    ("registered_with_title_variant", "lacks identity review"),
])
def test_citation_exception_requires_its_evidence_classification(corpus_root, state, error):
    add_source(corpus_root, acquisition_status=state)
    with pytest.raises(CorpusError, match=error):
        build(corpus_root)


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


@pytest.mark.parametrize("state,fields,label", [
    ("registered_with_derived_citation", {"citation_status": "derived", "citation_source": "publisher RIS and Crossref"}, "derived citation"),
    ("registered_with_title_variant", {"citation_status": "publisher-raw", "identity_status": "publisher-title-variant-reviewed"}, "publisher title variant"),
])
def test_review_promotion_preserves_citation_exceptions(corpus_root, state, fields, label):
    row = next(r for r in csv.DictReader((corpus_root / "06-data/paper-index.csv").open(encoding="utf-8-sig")) if r["code"] == "M39")
    sources = {f: row[f] for f in ("pdf", "bibtex", "markdown", "pdf_sha256", "bibtex_sha256", "markdown_sha256")}
    add_source(corpus_root, id=row["code"], doi=row["doi"], acquisition_status=state, **sources, **fields)
    pages = build(corpus_root)
    catalog = list(csv.DictReader(io.StringIO(pages[CATALOG_REL])))
    promoted = next(r for r in catalog if r["code"] == "M39")
    assert len([r for r in catalog if r["code"] == "M39"]) == 1
    assert promoted["survey_selected"] == "yes" and promoted["review"] == row["review"]
    assert label in promoted["assessment"]
    assert all(promoted[k] == v for k, v in fields.items() if k in {"citation_status", "identity_status"})
    index_row = next(line for line in pages["01-papers/INDEX.md"].splitlines() if re.search(r"\| (?:\S+ )?M39 \|", line))
    assert label in index_row and "[Review]" in index_row


def save_catalog_sources(root, *sources):
    from tools.catalog import CATALOG_FIELDS
    rows = list(csv.DictReader(io.StringIO(build(root)[CATALOG_REL])))
    rows.extend(sources)
    path = root / CATALOG_REL
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=CATALOG_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def catalog_source(code='SC-M101', **changes):
    folder = f'T3-planning-control/2026-navigation-{code}'
    row = dict(code=code, theme='T3', title='Navigation source', bibliographic_year='2026',
        venue='A Journal', publication_type='journal', doi='10.0000/' + code,
        pdf=f'01-papers/{folder}/paper.pdf', bibtex=f'01-papers/{folder}/citation.bib',
        markdown=f'02-fulltext/{folder}/paper.md', review='', survey_selected='no',
        view_group='main', library_status='official-pair-verified')
    row.update(changes)
    return row


def test_catalog_roundtrip_keeps_unassessed_sources_and_filters_archive(corpus_root):
    (corpus_root / 'INDEX.html').write_text('', encoding='utf-8')
    save_catalog_sources(corpus_root, catalog_source(),
        catalog_source('SC-M062', view_group='pending', pdf='99-archive/local/pending/paper.pdf', markdown=''),
        catalog_source('SC-M999', view_group='excluded', pdf='', markdown=''))
    first = build(corpus_root)
    assert '| SC-M101 |' in first['01-papers/INDEX.md']
    assert '| SC-M101 |' in first['02-fulltext/INDEX.md']
    assert '| SC-M101 |' not in first['03-reviews/INDEX.md']
    assert 'Not assessed' in first['01-papers/INDEX.md']
    assert '| SC-M062 |' not in first['01-papers/INDEX.md']
    assert '| SC-M999 |' not in first['01-papers/INDEX.md']
    rows = list(csv.DictReader(io.StringIO(first[CATALOG_REL])))
    assert {r['code'] for r in rows} >= {'SC-M101', 'SC-M062', 'SC-M999'}
    assert all(r['survey_selected'] == 'no' for r in rows if r['code'].startswith('SC-'))
    (corpus_root / CATALOG_REL).write_text(first[CATALOG_REL], encoding='utf-8')
    assert build(corpus_root) == first


@pytest.mark.parametrize('changes,error', [
    ({'review': '03-reviews/fake/review.md'}, 'claims a review'),
    ({'survey_selected': 'yes'}, 'claims a review'),
    ({'pdf': '01-papers/batch/research/old/paper.pdf'}, 'outside the shared paper layout'),
    ({'doi': '10.1109/lra.2022.3184768'}, 'duplicate library identity'),
])
def test_saved_catalog_cannot_promote_or_relabel_unassessed_sources(corpus_root, changes, error):
    save_catalog_sources(corpus_root, catalog_source(**changes))
    with pytest.raises(CorpusError, match=error):
        build(corpus_root)
