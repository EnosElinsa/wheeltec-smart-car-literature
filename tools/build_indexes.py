"""Regenerate a unified source catalog and the library index pages.

Writes ``01-papers/INDEX.md``, ``02-fulltext/INDEX.md``, and
``03-reviews/INDEX.md``, ``06-data/library-catalog.csv``, and every per-theme ``README.md`` that already
exists under ``01-papers/<theme>/``, ``02-fulltext/<theme>/`` (local only),
and ``03-reviews/<theme>/``. Each entry shows ID, year (bibliographic year),
title, venue, type, survey module, evidence type, and platform class, with a
star for the key papers of ``READING_GUIDE.md`` (see ``tools.corpus``).
Source indexes include acquired papers with their assessment status; the
review index lists existing review cards. Acquisition registers are provenance
inputs, while every paper remains in the shared theme directories.

PDFs and ``paper.md`` files are excluded from the public tree, so entries link
to review cards, source notes and ``citation.bib``, link the DOI or official URL
externally, and show the local PDF and Markdown paths as code. Output is
deterministic: themes in name order, entries by year (newest first) and ID,
no timestamps.

Usage::

    python -m tools.build_indexes                      # write into the repository
    python -m tools.build_indexes --out tmp/indexes    # write elsewhere
    python -m tools.build_indexes --strict             # uncoded reviews are errors
"""

from __future__ import annotations

import argparse
import posixpath
import sys
from collections import defaultdict
from pathlib import Path

from tools.common import REPO_ROOT
from tools.corpus import STAR, CorpusError, Entry
from tools.catalog import CATALOG_REL, catalog_csv, load_catalog

SECTIONS = {
    "01-papers": "Publisher PDFs and citations",
    "02-fulltext": "Full-text Markdown transcriptions and referenced figures",
    "03-reviews": "Review cards",
}
SECTION_NOTES = {
    "02-fulltext": "The transcriptions can contain OCR and formula errors; the PDF is the "
                   "authority for numbers, tables, and page numbers.",
    "03-reviews": "Reviews follow [TEMPLATE.md](TEMPLATE.md) and [WORKFLOW.md](WORKFLOW.md).",
}
HEADER = (
    "| ID | Year | Title | Venue | Type | Module | Evidence | Platform | Links | Local files |\n"
    "|---|---:|---|---|---|---|---|---|---|---|\n"
)


def _cell(text: str) -> str:
    return " ".join(text.split()).replace("|", "\\|")


def _link(page_dir: str, target: str) -> str:
    return posixpath.relpath("/" + target, "/" + page_dir)


def _year(entry: Entry) -> int:
    try:
        return int(entry.row.get("bibliographic_year", ""))
    except ValueError:
        return 0


def _row(entry: Entry, page_dir: str, assessment: bool = False) -> str:
    row = entry.row
    links = []
    if row.get("review"):
        links.append(f"[Review]({_link(page_dir, row['review'])})")
    elif row.get("source_notes"):
        links.append(f"[Source notes]({_link(page_dir, row['source_notes'])})")
    links.append(f"[BibTeX]({_link(page_dir, row['bibtex'])})")
    doi = row.get("doi", "").strip()
    url = row.get("official_url", "").strip()
    if doi:
        links.append(f"[DOI](https://doi.org/{doi})")
    if url and (not doi or url.rstrip("/").lower() != f"https://doi.org/{doi}".lower()):
        links.append(f"[Official page]({url})")
    local = " · ".join(f"`{row[field]}`" for field in ("pdf", "markdown") if row.get(field))
    code = f"{STAR} {entry.code}" if entry.key else entry.code
    cells = [
        code, row.get("bibliographic_year", ""), _cell(row.get("title", "")), _cell(row.get("venue", "")),
        row.get("publication_type", ""), entry.value("survey_module"), entry.value("evidence_type"),
        entry.value("platform_class"), " · ".join(links), local,
    ]
    if assessment:
        cells.insert(8, row["assessment"])
    return "| " + " | ".join(cells) + " |\n"


def _table(entries: list[Entry], page_dir: str, assessment: bool = False) -> str:
    ordered = sorted(entries, key=lambda e: (-_year(e), e.code))
    header = HEADER
    if assessment:
        header = HEADER.replace("| Links |", "| Assessment | Links |")
        lines = header.splitlines()
        lines[1] += "---|"
        header = "\n".join(lines) + "\n"
    return header + "".join(_row(e, page_dir, assessment) for e in ordered)


def _legend(entries: list[Entry], to_root: str) -> str:
    keys = sum(e.key for e in entries)
    text = (
        "PDFs and Markdown transcriptions are local only: they are excluded from the public "
        "repository for copyright reasons, so their paths are shown as code, not as links. "
        f"{STAR} marks the {keys} key papers of the [reading guide]({to_root}READING_GUIDE.md). "
        "Module, Evidence, and Platform are the `survey_module`, `evidence_type`, and "
        "`platform_class` values of each review's survey coding "
        f"([vocabulary]({to_root}06-data/vocabulary.md))."
    )
    if any(not e.coding for e in entries):
        text += " Empty coding cells indicate that survey classification is pending."
    if any(e.review is None for e in entries):
        text += " Targeted source notes are distinguished from review cards in the Assessment column."
    return text + "\n"


def section_index(section: str, entries: list[Entry]) -> str:
    by_theme: dict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        by_theme[entry.theme].append(entry)
    parts = [
        f"# {section}\n\n",
        f"{SECTIONS[section]}: {len(entries)} papers. The folders `01-papers`, `02-fulltext`, "
        "and `03-reviews` use the same `<theme>/<year>-<short-name>-<ID>/` layout.",
        f" {SECTION_NOTES[section]}" if section in SECTION_NOTES else "",
        "\n\n[Library overview](../README.md) · [Reading guide](../READING_GUIDE.md)\n\n",
        _legend(entries, "../"),
    ]
    for theme in sorted(by_theme):
        parts.append(f"\n## {theme} · {len(by_theme[theme])}\n\n")
        parts.append(_table(by_theme[theme], section, assessment=section != "03-reviews"))
    return "".join(parts)


def theme_readme(section: str, theme: str, entries: list[Entry]) -> str:
    page_dir = f"{section}/{theme}"
    return "".join([
        f"# {theme}\n\n",
        "[Section index](../INDEX.md) · [Reading guide](../../READING_GUIDE.md)\n\n",
        f"{SECTIONS[section]}: {len(entries)} papers.\n\n",
        _legend(entries, "../../"),
        "\n",
        _table(entries, page_dir, assessment=section != "03-reviews"),
    ])


def build(root: Path = REPO_ROOT, strict: bool = False) -> dict[str, str]:
    """Return the generated pages as {path relative to the root: text}."""
    entries = load_catalog(root, strict)
    themes = sorted({e.theme for e in entries})
    pages = {CATALOG_REL: catalog_csv(entries)}
    for section in SECTIONS:
        if section == "03-reviews":
            selected = [e for e in entries if e.review is not None]
        elif section == "02-fulltext":
            selected = [e for e in entries if e.row.get("markdown")]
        else:
            selected = entries
        pages[f"{section}/INDEX.md"] = section_index(section, selected)
        for theme in themes:
            rel = f"{section}/{theme}/README.md"
            if (root / rel).is_file():
                pages[rel] = theme_readme(section, theme, [e for e in selected if e.theme == theme])
    return pages


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Regenerate the library index pages.")
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="library root to read")
    parser.add_argument("--out", type=Path, help="output root (default: the library root)")
    parser.add_argument("--strict", action="store_true", help="treat reviews without coding as errors")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    try:
        pages = build(root, args.strict)
    except CorpusError as error:
        sys.stderr.write("".join(f"error: {p}\n" for p in error.problems))
        return 1
    out = (args.out or root).resolve()
    for rel, text in sorted(pages.items()):
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
    sys.stdout.write(f"wrote {len(pages)} files under {out.as_posix()}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
