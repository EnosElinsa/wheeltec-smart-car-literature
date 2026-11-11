"""Render a self-contained, offline reading interface for the source catalog."""
from __future__ import annotations

import json
from pathlib import Path


def venue_family(venue: str) -> str:
    """Group annual proceedings and known spelling variants into stable facets."""
    name = venue.casefold()
    for fragment, label in (
        ("international conference on robotics and automation", "ICRA"),
        ("intelligent robots and systems", "IROS"),
        ("conference on robot learning", "CoRL"),
        ("robotics: science and systems", "RSS"),
        ("robotics science and systems", "RSS"),
        ("international journal of robotics research", "The International Journal of Robotics Research"),
    ):
        if fragment in name:
            return label
    return venue.strip() or "Unspecified venue"


def render(entries) -> str:
    fields = (
        "code", "theme", "title", "bibliographic_year", "venue", "doi", "official_url",
        "assessment", "view_group", "kind", "publication_type", "pdf", "bibtex", "markdown",
        "review", "screening_reason", "citation_status", "survey_selected",
    )
    records = []
    for entry in sorted(entries, key=lambda e: e.code):
        row = {key: entry.row.get(key, "") for key in fields}
        row["venue_family"] = venue_family(row["venue"])
        records.append(row)
    payload = json.dumps(records, ensure_ascii=True, separators=(",", ":")).replace("<", "\\u003c")
    template = Path(__file__).with_name("local_index.html").read_text(encoding="utf-8")
    return template.replace("__CATALOG_DATA__", payload)
