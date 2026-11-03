"""Read original PDF page text, using optional local OCR for image-only pages.

OCR requires PyMuPDF and an English Tesseract model in TESSDATA_PREFIX, the
system tessdata directory, or tmp/ocr/tessdata/eng.traineddata. It never
changes the PDF. Local OCR caches are bound to PDF bytes, model bytes, and
PyMuPDF version. Without a model, image-only pages remain empty and cannot
pass an excerpt match. OCR matches still need visual inspection.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from tools.common import REPO_ROOT


def read_pdf_pages(path: Path, *, tessdata: Path | None = None,
                   cache_dir: Path | None = None) -> list[str]:
    import fitz

    path = Path(path)
    with fitz.open(path) as doc:
        pages = [page.get_text() for page in doc]
        if all(text.strip() for text in pages):
            return pages
        if tessdata is None:
            try:
                tessdata = Path(fitz.get_tessdata())
            except RuntimeError:
                tessdata = REPO_ROOT / "tmp" / "ocr" / "tessdata"
        model = Path(tessdata) / "eng.traineddata"
        if not model.is_file():
            return pages
        pdf_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        model_hash = hashlib.sha256(model.read_bytes()).hexdigest()
        identity = f"pdf-ocr-1:{pdf_hash}:{model_hash}:{fitz.VersionBind}"
        key = hashlib.sha256(identity.encode()).hexdigest()
        cache_dir = cache_dir or REPO_ROOT / "tmp" / "ocr" / "text"
        cache_path = cache_dir / f"{key}.json"
        try:
            cached = json.loads(cache_path.read_text(encoding="utf-8"))
            if not isinstance(cached, dict):
                raise ValueError("OCR cache must be an object")
            texts = cached.get("pages")
            if (cached.get("identity") == identity and isinstance(texts, list)
                    and len(texts) == len(pages) and all(isinstance(t, str) for t in texts)):
                return texts
        except (OSError, ValueError):
            pass
        for i, text in enumerate(pages):
            if not text.strip():
                textpage = doc[i].get_textpage_ocr(
                    language="eng", tessdata=str(tessdata), full=True, dpi=200
                )
                pages[i] = textpage.extractText()
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps({
            "identity": identity, "pdf_sha256": pdf_hash,
            "model_sha256": model_hash, "engine": f"PyMuPDF {fitz.VersionBind}",
            "method": "Tesseract English, full page, 200 dpi; embedded text retained",
            "pages": pages,
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        return pages
