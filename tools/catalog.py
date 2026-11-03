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
    "bibtex_sha256", "markdown_sha256",
)


def load_catalog(root: Path = REPO_ROOT, strict: bool = False) -> list[Entry]:
    entries = load_corpus(root, strict)
    reviewed = {e.code: e for e in entries}
    ids = set(reviewed)
    dois = {e.row["doi"].strip().casefold() for e in entries if e.row.get("doi")}
    for entry in entries:
        entry.row["assessment"] = (
            f"{entry.row['verification_level'].capitalize()} review card"
            if entry.row.get("verification_level") else "Review card"
        )
        entry.row["survey_selected"] = "yes"
    for manifest in sorted((root / "06-data").glob("*/manifest.json")):
        payload = json.loads(manifest.read_text(encoding="utf-8"))
        # This schema describes acquired papers; other manifests are unrelated.
        if not isinstance(payload, dict) or not isinstance(payload.get("records"), list):
            continue
        notes = manifest.with_name("evidence-notes.md")
        for source in payload["records"]:
            if source.get("acquisition_status") != "delivered":
                continue
            code = source["id"]
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
                continue
            if code in ids or (doi and doi in dois):
                raise CorpusError([f"duplicate library identity in {manifest.relative_to(root)}: {code}"])
            pdf = Path(source["pdf"])
            if len(pdf.parts) != 4 or pdf.parts[0] != "01-papers":
                raise CorpusError([f"source outside the shared paper layout: {code}"])
            targeted = source.get("read_scope") == "targeted-source-reading"
            row = {
                "code": code, "theme": source["theme"], "title": source["title"],
                "bibliographic_year": str(source["year"]), "venue": source["venue"],
                "publication_type": "conference" if source["publication_type"] == "proceedings-article" else "journal",
                "doi": source.get("doi", ""), "official_url": source.get("official_url", ""),
                "assessment": "Targeted source notes" if targeted else "Source registered",
                "survey_selected": "no", "review": "",
                "source_notes": notes.relative_to(root).as_posix() if targeted and notes.is_file() else "",
                "extraction_mode": source.get("extraction_mode", ""),
            }
            row.update({field: source[field] for field in (
                "pdf", "bibtex", "markdown", "pdf_sha256", "bibtex_sha256", "markdown_sha256"
            )})
            entries.append(Entry(row, pdf.parts[1], None, False))
            ids.add(code)
            if doi:
                dois.add(doi)
    return entries


def catalog_csv(entries: list[Entry]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=CATALOG_FIELDS, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    for entry in sorted(entries, key=lambda e: (e.theme, -int(e.row["bibliographic_year"]), e.code)):
        writer.writerow(entry.row)
    return output.getvalue()
