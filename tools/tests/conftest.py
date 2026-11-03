"""Shared fixtures: a small library tree built from the six pilot reviews.

The tree is created under ``tmp_path``. It holds the pilot reviews (copied
read-only from the repository), their original bibliographic index fields,
one synthetic review without a coding block, placeholder BibTeX
files, a reading guide, and some per-theme README files.
"""

from __future__ import annotations

import csv
import io
import shutil
from pathlib import Path

import pytest

from tools.common import REPO_ROOT
from tools.vocab import CODING_FIELDS

PILOTS = ["M39", "X07", "E01", "E36", "E50", "M37"]
UNCODED = "M98"
UNCODED_THEME = "T2-slam-mapping-exploration"
UNCODED_FOLDER = f"2023-uncoded-{UNCODED}"
UNCODED_REVIEW = "# An Uncoded Review\n\n## Problem\n\nA review in an older format.\n"

GUIDE = """# Reading guide

| ID and short name | Why first |
|---|---|
| [M39 · slip-aware-fusion](03-reviews/T1-perception-localization/2022-slip-aware-fusion-M39/review.md) | slip |
| [X07 · EKF-SLAM-integrity](03-reviews/T1-perception-localization/2025-EKF-SLAM-integrity-X07/review.md) | integrity |
| [E36 · Commerge](03-reviews/T4-multi-robot-coordination/2026-Commerge-E36/review.md) | merging |

- Route: M39 -> E01 -> M37.
"""


def index_records() -> tuple[bytes, list[bytes], list[str]]:
    """Return the BOM, the header line, and the pilot lines of the real index (raw bytes)."""
    raw = (REPO_ROOT / "06-data" / "paper-index.csv").read_bytes()
    bom = b"\xef\xbb\xbf" if raw.startswith(b"\xef\xbb\xbf") else b""
    lines = raw[len(bom):].splitlines(keepends=True)
    header = next(csv.reader([lines[0].decode("utf-8")]))
    picked = [lines[0]] + [ln for ln in lines[1:] if ln.decode("utf-8").split(",", 1)[0] in PILOTS]
    # Keep this fixture as an input awaiting its first coding append, even
    # after build_tables has extended the real index. Rerun behavior has its
    # own test; the first-append test must not depend on workspace state.
    if header[-len(CODING_FIELDS):] == list(CODING_FIELDS):
        width = len(header) - len(CODING_FIELDS)
        ending = "\r\n" if lines[0].endswith(b"\r\n") else "\n"
        out = io.StringIO(newline="")
        writer = csv.writer(out, lineterminator=ending)
        writer.writerows(row[:width] for row in csv.reader(ln.decode("utf-8") for ln in picked))
        picked = out.getvalue().encode("utf-8").splitlines(keepends=True)
        header = header[:width]
    return bom, picked, header


def uncoded_line(header: list[str], ending: bytes) -> bytes:
    folder = f"{UNCODED_THEME}/{UNCODED_FOLDER}"
    values = {name: "" for name in header}
    values.update({
        "code": UNCODED, "theme": "T2", "title": "An Uncoded Review", "bibliographic_year": "2023",
        "selection_year": "2023", "venue": "Test Venue, With Comma", "publication_type": "journal",
        "source_batch": "baseline-2026-09-18", "doi": "10.0000/test.1",
        "official_url": "https://example.org/paper", "pdf": f"01-papers/{folder}/paper.pdf",
        "bibtex": f"01-papers/{folder}/citation.bib", "review": f"03-reviews/{folder}/review.md",
        "markdown": f"02-fulltext/{folder}/paper.md", "pdf_sha256": "a" * 64,
    })
    out = io.StringIO()
    csv.writer(out, lineterminator="").writerow([values[name] for name in header])
    return out.getvalue().encode("utf-8") + ending


@pytest.fixture
def corpus_root(tmp_path: Path) -> Path:
    root = tmp_path / "library"
    bom, lines, header = index_records()
    ending = b"\r\n" if lines[0].endswith(b"\r\n") else b"\n"
    index = root / "06-data" / "paper-index.csv"
    index.parent.mkdir(parents=True)
    index.write_bytes(bom + b"".join(lines) + uncoded_line(header, ending))
    with index.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert sorted(r["code"] for r in rows) == sorted(PILOTS + [UNCODED])
    for row in rows:
        review = root / row["review"]
        review.parent.mkdir(parents=True)
        if row["code"] == UNCODED:
            review.write_text(UNCODED_REVIEW, encoding="utf-8")
        else:
            shutil.copyfile(REPO_ROOT / row["review"], review)
        bib = root / row["bibtex"]
        bib.parent.mkdir(parents=True, exist_ok=True)
        bib.write_text("@article{x}\n", encoding="utf-8")
    (root / "READING_GUIDE.md").write_text(GUIDE, encoding="utf-8")
    for section in ("01-papers", "03-reviews"):
        for theme in ("T1-perception-localization", "T4-multi-robot-coordination"):
            (root / section / theme / "README.md").write_text("# old\n", encoding="utf-8")
    (root / "02-fulltext" / "T1-perception-localization").mkdir(parents=True)
    (root / "02-fulltext" / "T1-perception-localization" / "README.md").write_text("# old\n", encoding="utf-8")
    return root
