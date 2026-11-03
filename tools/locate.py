"""Look up text in a paper's PDF and full-text Markdown by library code.

Examples::

    python -m tools.locate M39 --info
    python -m tools.locate M39 --find "covariance intersection"
    python -m tools.locate M39 --page 6
    python -m tools.locate M39 --abstract

``--find`` prints the physical PDF pages that contain the phrase (after the
same normalization that ``tools.review_check`` uses) and whether the phrase
occurs in ``paper.md``. Use it to assign page numbers to excerpts.
"""

from __future__ import annotations

import argparse
import re
import sys

from tools.common import REPO_ROOT, read_text
from tools.catalog import load_catalog
from tools.textnorm import NormalizedText, coverage, ngrams, normalize
from tools.pdftext import read_pdf_pages


def pdf_pages(path):
    return read_pdf_pages(path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("code")
    parser.add_argument("--info", action="store_true", help="print index row and file paths")
    parser.add_argument("--find", action="append", default=[], help="phrase to locate (repeatable)")
    parser.add_argument("--page", type=int, action="append", default=[], help="print raw text of a PDF page")
    parser.add_argument("--abstract", action="store_true", help="print the abstract region of paper.md")
    parser.add_argument("--render", type=int, action="append", default=[],
                        help="render a PDF page to tmp/render/<ID>-p<N>.png for reading tables and figures")
    parser.add_argument("--zoom", type=float, default=2.5, help="zoom factor for --render")
    args = parser.parse_args(argv)

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    row = next((entry.row for entry in load_catalog() if entry.code == args.code), None)
    if row is None:
        print(f"unknown code {args.code}")
        return 2
    pdf = REPO_ROOT / row["pdf"]
    md_path = REPO_ROOT / row["markdown"]

    if args.info:
        for key in ("code", "title", "venue", "bibliographic_year", "publication_type", "doi",
                    "official_url", "source_batch", "pdf", "markdown", "bibtex", "review"):
            print(f"{key}: {row.get(key, '')}")
        if pdf.is_file():
            print(f"pdf_pages: {len(pdf_pages(pdf))}")
        print(f"markdown_chars: {len(read_text(md_path)) if md_path.is_file() else 'missing'}")

    pages = pdf_pages(pdf) if (args.find or args.page) and pdf.is_file() else []
    if args.find:
        md = NormalizedText(read_text(md_path)) if md_path.is_file() else None
        norm_pages = [normalize(p) for p in pages]
        for phrase in args.find:
            norm = normalize(phrase)
            exact = [i + 1 for i, p in enumerate(norm_pages) if norm in p]
            fuzzy = []
            if not exact and len(norm.split()) >= 7:
                for i, p in enumerate(norm_pages):
                    window = p + " " + (norm_pages[i + 1] if i + 1 < len(norm_pages) else "")
                    if coverage(norm, ngrams(window.split(), 5), 5) >= 0.8:
                        fuzzy.append(i + 1)
            md_status = md.match(phrase) if md else "no-markdown"
            print(f"phrase: {phrase[:80]}")
            print(f"  pdf pages exact: {exact or '-'}  fuzzy: {fuzzy or '-'}  markdown: {md_status}")

    for number in args.page:
        if 1 <= number <= len(pages):
            print(f"===== PDF page {number} of {len(pages)} =====")
            print(pages[number - 1])
        else:
            print(f"page {number} out of range (1-{len(pages)})")

    if args.render and pdf.is_file():
        import fitz  # PyMuPDF

        out_dir = REPO_ROOT / "tmp" / "render"
        out_dir.mkdir(parents=True, exist_ok=True)
        with fitz.open(pdf) as doc:
            for number in args.render:
                if not 1 <= number <= doc.page_count:
                    print(f"page {number} out of range (1-{doc.page_count})")
                    continue
                pix = doc[number - 1].get_pixmap(matrix=fitz.Matrix(args.zoom, args.zoom))
                target = out_dir / f"{args.code}-p{number}.png"
                pix.save(target)
                print(f"rendered: {target.relative_to(REPO_ROOT).as_posix()}")

    if args.abstract and md_path.is_file():
        text = read_text(md_path)
        match = re.search(r"(?is)(abstract.{0,3000})", text)
        print(match.group(1) if match else text[:3000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
