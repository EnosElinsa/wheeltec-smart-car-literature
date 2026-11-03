"""PDF evidence extraction keeps scans strict and binds OCR to source bytes."""

import json

import pytest

import fitz


def write_pdf(path, text=""):
    with fitz.open() as doc:
        page = doc.new_page()
        if text:
            page.insert_text((72, 72), text)
        doc.save(path)


def test_native_pdf_does_not_need_ocr(tmp_path):
    from tools.pdftext import read_pdf_pages

    path = tmp_path / "paper.pdf"
    write_pdf(path, "Native evidence on the original PDF page.")
    pages = read_pdf_pages(path, tessdata=tmp_path / "missing", cache_dir=tmp_path / "cache")
    assert "Native evidence" in pages[0]


def test_scan_without_ocr_model_stays_unmatched(tmp_path):
    from tools.pdftext import read_pdf_pages

    path = tmp_path / "scan.pdf"
    write_pdf(path)
    assert read_pdf_pages(path, tessdata=tmp_path / "missing", cache_dir=tmp_path / "cache") == [""]


def test_ocr_cache_is_invalidated_when_pdf_changes(tmp_path, monkeypatch):
    from tools.pdftext import read_pdf_pages

    path = tmp_path / "scan.pdf"
    write_pdf(path)
    tessdata = tmp_path / "tessdata"
    tessdata.mkdir()
    (tessdata / "eng.traineddata").write_bytes(b"test-model")
    calls = []

    class TextPage:
        def extractText(self):
            return "A quote checked from the scanned page."

    def ocr(page, **kwargs):
        calls.append(page.number)
        return TextPage()

    monkeypatch.setattr(fitz.Page, "get_textpage_ocr", ocr)
    cache_dir = tmp_path / "cache"
    options = dict(tessdata=tessdata, cache_dir=cache_dir)
    assert "scanned page" in read_pdf_pages(path, **options)[0]
    assert read_pdf_pages(path, **options)[0] == "A quote checked from the scanned page."
    assert len(calls) == 1
    assert list(cache_dir.glob("*.json"))
    with fitz.open(path) as doc:
        doc.new_page()
        changed = doc.tobytes()
    path.write_bytes(changed)
    assert len(read_pdf_pages(path, **options)) == 2
    assert len(calls) == 3


@pytest.mark.parametrize("bad_cache", ["not json", "[]", "null", "42"])
def test_corrupt_ocr_cache_is_rebuilt(tmp_path, monkeypatch, bad_cache):
    from tools.pdftext import read_pdf_pages

    path = tmp_path / "scan.pdf"
    write_pdf(path)
    tessdata = tmp_path / "tessdata"
    tessdata.mkdir()
    (tessdata / "eng.traineddata").write_bytes(b"test-model")

    class TextPage:
        def extractText(self):
            return "Original scanned-page evidence."

    monkeypatch.setattr(fitz.Page, "get_textpage_ocr", lambda *a, **k: TextPage())
    cache_dir = tmp_path / "cache"
    options = dict(tessdata=tessdata, cache_dir=cache_dir)
    read_pdf_pages(path, **options)
    cache = next(cache_dir.glob("*.json"))
    cache.write_text(bad_cache, encoding="utf-8")
    assert read_pdf_pages(path, **options) == ["Original scanned-page evidence."]
    assert isinstance(json.loads(cache.read_text(encoding="utf-8"))["pages"], list)
