"""Render a self-contained, offline reading interface for the source catalog."""
from __future__ import annotations

import json
import re
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


def render(entries, projects=None) -> str:
    fields = (
        "code", "theme", "title", "bibliographic_year", "venue", "doi", "official_url",
        "assessment", "view_group", "kind", "publication_type", "pdf", "bibtex", "markdown",
        "review", "screening_reason", "citation_status", "survey_selected",
    )
    records = []
    for entry in sorted(entries, key=lambda e: e.code):
        # The reading interface describes admitted papers. Excluded/background
        # and pending catalog identities remain in the administrative CSV only.
        if entry.row.get("view_group", "main") not in {"main", "surveys"}:
            continue
        row = {key: entry.row.get(key, "") for key in fields}
        row["venue_family"] = venue_family(row["venue"]) if row["venue"].strip() else ""
        records.append(row)
    payload = json.dumps(records, ensure_ascii=True, separators=(",", ":")).replace("<", "\\u003c")
    template = Path(__file__).with_name("local_index.html").read_text(encoding="utf-8")
    project_payload = json.dumps(projects or {"projects": [], "categories": [], "methods": [], "environments": []},
                                 ensure_ascii=True, separators=(",", ":")).replace("<", "\\u003c")
    folder = Path(__file__).parent
    fragments = {
        "CATALOG_DATA": payload,
        "PROJECT_DATA": project_payload,
        "PROJECT_STYLE": (folder / "project_index.css").read_text(encoding="utf-8"),
        "PROJECT_SCRIPT": (folder / "project_index.js").read_text(encoding="utf-8"),
    }
    # One substitution pass keeps placeholder-like text inside titles verbatim.
    return re.sub(r"__(CATALOG_DATA|PROJECT_DATA|PROJECT_STYLE|PROJECT_SCRIPT)__",
                  lambda match: fragments[match[1]], template)
