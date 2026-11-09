"""Combine reviewed papers and acquired sources in one library catalog.

The survey corpus remains a separate selection. Acquisition registers supply
source metadata, not review coding or manuscript inclusion.
"""
from __future__ import annotations

import csv
import io
import json
from pathlib import Path

from tools.common import REPO_ROOT
from tools.corpus import CorpusError, Entry, load_corpus

CATALOG_REL = "06-data/library-catalog.csv"
CATALOG_FIELDS = (
    "code", "theme", "title", "bibliographic_year", "venue", "publication_type",
    "doi", "official_url", "assessment", "survey_selected", "pdf", "bibtex",
    "markdown", "review", "source_notes", "extraction_mode", "pdf_sha256",
    "bibtex_sha256", "markdown_sha256", "citation_status", "identity_status",
    "collection", "kind", "category", "library_status", "view_group",
    "acquisition_state", "citation_source", "pdf_version", "provenance",
    "extraction", "screening_reason", "notes",
)

THEME_DIRS = {
    "T1": "T1-perception-localization", "T2": "T2-slam-mapping-exploration",
    "T3": "T3-planning-control", "T4": "T4-multi-robot-coordination",
    "T5": "T5-semantic-embodied-navigation", "T6": "T6-reliability-deployment",
}


def _merge_saved_catalog(root: Path, entries: list[Entry]) -> None:
    """Retain unassessed and archived records from the single catalog.

    Review cards and acquisition manifests still establish assessed metadata.
    Saved catalog rows cannot change their identities or source bytes, and an
    unassessed row cannot promote itself into the survey or invent a review.
    """
    path = root / CATALOG_REL
    if not path.is_file():
        return
    known = {entry.code: entry for entry in entries}
    dois = {entry.row.get("doi", "").strip().casefold(): entry.code
            for entry in entries if entry.row.get("doi")}
    seen: set[str] = set()
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        code = row["code"]
        if code in seen:
            raise CorpusError([f"duplicate library identity in {CATALOG_REL}: {code}"])
        seen.add(code)
        if code in known:
            current = known[code].row
            fields = ("doi", "pdf", "bibtex", "markdown", "pdf_sha256", "bibtex_sha256", "markdown_sha256")
            if any((row.get(field, "").casefold() != current.get(field, "").casefold())
                   if field == "doi" else (row.get(field, "") != current.get(field, "")) for field in fields):
                raise CorpusError([f"saved catalog conflicts with established sources: {code}"])
            for field in CATALOG_FIELDS[21:]:
                if row.get(field):
                    current[field] = row[field]
            continue
        doi = row.get("doi", "").strip().casefold()
        if doi and doi in dois:
            raise CorpusError([f"duplicate library identity in {CATALOG_REL}: {code}"])
        if row.get("review") or row.get("survey_selected", "no") != "no":
            raise CorpusError([f"unassessed catalog record claims a review or survey membership: {code}"])
        theme = THEME_DIRS.get(row.get("theme", ""))
        if not theme:
            raise CorpusError([f"unknown catalog theme for {code}"])
        group = row.get("view_group")
        if group not in {"main", "surveys", "excluded", "pending"}:
            raise CorpusError([f"unknown catalog group for {code}"])
        if group in {"main", "surveys"}:
            for field, section in (("pdf", "01-papers"), ("bibtex", "01-papers"), ("markdown", "02-fulltext")):
                parts = Path(row.get(field, "")).parts
                if len(parts) != 4 or parts[0] != section or parts[1] != theme:
                    raise CorpusError([f"source outside the shared paper layout: {code}: {field}"])
        row["assessment"] = "Not assessed" if group in {"main", "surveys"} else "Not assessed; " + group
        row["survey_selected"] = "no"
        entries.append(Entry(row, theme, None, False))
        known[code] = entries[-1]
        if doi:
            dois[doi] = code

REGISTERED_SOURCE_STATES = frozenset({
    "delivered", "registered_with_derived_citation", "registered_with_title_variant",
})


def load_catalog(root: Path = REPO_ROOT, strict: bool = False) -> list[Entry]:
    entries = load_corpus(root, strict)
    reviewed = {e.code: e for e in entries}
    ids = set(reviewed)
    inclusion_path = root / '06-data/survey-inclusion.json'
    selected = ids
    if inclusion_path.is_file():
        inclusion = json.loads(inclusion_path.read_text(encoding='utf-8'))
        selected = set(inclusion['selected_ids'])
        internal = set(inclusion.get('internal_reference_ids', []))
        if not selected <= ids or ids - selected != internal or selected & internal:
            raise CorpusError(['survey selection does not account for reviewed internal references'])
    dois = {e.row["doi"].strip().casefold() for e in entries if e.row.get("doi")}
    for entry in entries:
        entry.row["assessment"] = (
            f"{entry.row['verification_level'].capitalize()} review card"
            if entry.row.get("verification_level") else "Review card"
        )
        entry.row["survey_selected"] = "yes" if entry.code in selected else "no"
        if entry.code not in selected:
            entry.row["assessment"] += "; internal reference"
    for manifest in sorted((root / "06-data").glob("*/manifest.json")):
        payload = json.loads(manifest.read_text(encoding="utf-8"))
        # This schema describes acquired papers; other manifests are unrelated.
        if not isinstance(payload, dict) or not isinstance(payload.get("records"), list):
            continue
        notes = manifest.with_name("evidence-notes.md")
        for source in payload["records"]:
            state = source.get("acquisition_status")
            if state not in REGISTERED_SOURCE_STATES:
                continue
            code = source["id"]
            derived = state == "registered_with_derived_citation"
            title_variant = state == "registered_with_title_variant"
            if derived and (source.get("citation_status") != "derived" or not source.get("citation_source")):
                raise CorpusError([f"derived citation lacks source attribution: {code}"])
            if title_variant and source.get("identity_status") != "publisher-title-variant-reviewed":
                raise CorpusError([f"publisher title variant lacks identity review: {code}"])
            doi = source.get("doi", "").strip().casefold()
            if code in reviewed:
                # Acquisition and subsequent assessment describe the same work.
                # Accept that overlap only when identity and source bytes agree.
                row = reviewed[code].row
                fields = ("pdf", "bibtex", "markdown", "pdf_sha256", "bibtex_sha256", "markdown_sha256")
                if doi != row.get("doi", "").strip().casefold() or any(
                    source.get(field, "") != row.get(field, "") for field in fields
                ):
                    raise CorpusError([f"duplicate library identity with conflicting sources in {manifest.relative_to(root)}: {code}"])
                row["source_notes"] = notes.relative_to(root).as_posix() if notes.is_file() else ""
                row["extraction_mode"] = source.get("extraction_mode", "")
                row["citation_status"] = source.get("citation_status", "")
                row["identity_status"] = source.get("identity_status", "")
                if derived:
                    row["assessment"] += "; derived citation"
                elif title_variant:
                    row["assessment"] += "; publisher title variant"
                continue
            if code in ids or (doi and doi in dois):
                raise CorpusError([f"duplicate library identity in {manifest.relative_to(root)}: {code}"])
            pdf = Path(source["pdf"])
            if len(pdf.parts) != 4 or pdf.parts[0] != "01-papers":
                raise CorpusError([f"source outside the shared paper layout: {code}"])
            targeted = source.get("read_scope") == "targeted-source-reading"
            assessment = "Targeted source notes" if targeted else "Source registered"
            if derived:
                assessment += "; derived citation"
            elif title_variant:
                assessment += "; publisher title variant"
            row = {
                "code": code, "theme": source["theme"], "title": source["title"],
                "bibliographic_year": str(source["year"]), "venue": source["venue"],
                "publication_type": "conference" if source["publication_type"] == "proceedings-article" else "journal",
                "doi": source.get("doi", ""), "official_url": source.get("official_url", ""),
                "assessment": assessment,
                "survey_selected": "no", "review": "",
                "source_notes": notes.relative_to(root).as_posix() if (targeted or derived or title_variant) and notes.is_file() else "",
                "extraction_mode": source.get("extraction_mode", ""),
                "citation_status": source.get("citation_status", ""),
                "identity_status": source.get("identity_status", ""),
            }
            row.update({field: source[field] for field in (
                "pdf", "bibtex", "markdown", "pdf_sha256", "bibtex_sha256", "markdown_sha256"
            )})
            entries.append(Entry(row, pdf.parts[1], None, False))
            ids.add(code)
            if doi:
                dois.add(doi)
    _merge_saved_catalog(root, entries)
    return entries


def catalog_csv(entries: list[Entry]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=CATALOG_FIELDS, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    for entry in sorted(entries, key=lambda e: (e.theme, -int(e.row["bibliographic_year"]), e.code)):
        writer.writerow(entry.row)
    return output.getvalue()
