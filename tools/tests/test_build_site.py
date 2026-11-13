"""Pages deployment must retain source bytes and produce usable, safe reading links."""
import hashlib
import json
import re

import pytest

from tools.build_site import build, render_fulltext, source_url

REVISION = "a" * 40


@pytest.fixture
def site_source(tmp_path):
    root = tmp_path / "repo"
    source = "02-fulltext/T1/2025-test-D01/paper.md"
    citation = "01-papers/T1/2025-test-D01/citation.bib"
    text = b'# Test paper\n\n![Figure](images/figure.png)\n\n| A | B |\n|---|---|\n| 1 | 2 |\n'
    for path, data in ((source, text), (citation, b'@article{test,\r\n title={Test}\r\n}\r\n')):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    row = {"code": "D01", "title": '</script> Test __CONTENT__', "markdown": source,
           "pdf": "01-papers/T1/2025-test-D01/paper.pdf", "bibtex": citation,
           "review": "03-reviews/T1/2025-test-D01/review.md"}
    page = '<a href="README.md">Guide</a><script id="catalog-data" type="application/json">'
    page += json.dumps([row]).replace("<", "\\u003c") + '</script>'
    (root / "INDEX.html").write_text(page, encoding="utf-8")
    manifest = {"files": [{"path": source, "kind": "markdown", "bytes": len(text),
                           "sha256": hashlib.sha256(text).hexdigest()},
                          {"path": "02-fulltext/T1/2025-test-D01/images/figure.png", "kind": "image"}]}
    (root / "06-data").mkdir()
    (root / "06-data/reading-assets.json").write_text(json.dumps(manifest), encoding="utf-8")
    return root, row


def test_site_reads_markdown_only_and_resolves_links(site_source, tmp_path):
    root, original = site_source
    out = tmp_path / "site"
    result = build(root, out, REVISION)
    assert result["papers"] == 1
    assert (out / "index.html").read_bytes() == (out / "INDEX.html").read_bytes()
    assert (out / "citations/D01.bib").read_bytes() == (root / original["bibtex"]).read_bytes()
    page = (out / "index.html").read_text(encoding="utf-8")
    payload = re.search(r'<script id="catalog-data" type="application/json">(.*?)</script>', page, re.S)[1]
    row = json.loads(payload)[0]
    assert row["pdf"] == source_url(original["pdf"], REVISION, media=True)
    assert row["markdown"] == "fulltext/D01.html"
    assert row["bibtex"] == "citations/D01.bib"
    assert row["review"] == source_url(original["review"], REVISION)
    assert row["title"] == original["title"]
    assert '<a href="https://github.com/' in page
    reader = (out / row["markdown"]).read_text(encoding="utf-8")
    assert '<table>' in reader
    assert 'loading="lazy"' in reader
    assert source_url("02-fulltext/T1/2025-test-D01/images/figure.png", REVISION, media=True) in reader
    assert '&lt;/script&gt; Test __CONTENT__' in reader
    assert not (out / "01-papers").exists()
    offline = json.loads(re.search(r'<script id="catalog-data" type="application/json">(.*?)</script>',
                                 (root / "INDEX.html").read_text(), re.S)[1])[0]
    assert offline == original


def test_site_rejects_lfs_pointer_or_modified_fulltext(site_source, tmp_path):
    root, row = site_source
    (root / row["markdown"]).write_text("version https://git-lfs.github.com/spec/v1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="run git lfs pull"):
        build(root, tmp_path / "site", REVISION)
    assert not (tmp_path / "site").exists()


def test_source_html_cannot_execute_scripts_or_use_unsafe_urls():
    source = '<script>alert(1)</script><img src="javascript:alert(1)" onerror="alert(2)">'
    source += '<a href="javascript:alert(3)">link</a><iframe src="https://example.com"></iframe>'
    rendered = render_fulltext(source, "02-fulltext/T1/paper.md", REVISION, set())
    for unsafe in ("<script", "onerror", "javascript:", "<iframe"):
        assert unsafe not in rendered


def test_formula_misread_as_a_link_does_not_break_publication():
    rendered = render_fulltext(r'[k](\Delta p_{i}[k])', "02-fulltext/T1/paper.md", REVISION, set())
    assert 'href=' not in rendered
    assert '>k</a>' in rendered


def test_formulas_keep_tex_for_the_math_renderer():
    rendered = render_fulltext(r'$x_i$ and $^{1}$' + '\n\n$$\\Delta x = x_1-x_0$$',
                               "02-fulltext/T1/paper.md", REVISION, set())
    assert 'class="arithmatex"' in rendered
    assert r'\(x_i\)' in rendered
    assert r'\[\Delta x = x_1-x_0\]' in rendered


@pytest.mark.parametrize("path", ["../private.md", "/root/file.md", "https://example.com", "folder\\file.md"])
def test_source_paths_stay_inside_the_repository(path):
    with pytest.raises(ValueError, match="Invalid repository path"):
        source_url(path, REVISION)


def test_output_must_be_empty_and_revision_must_be_immutable(site_source, tmp_path):
    root, _ = site_source
    with pytest.raises(ValueError, match="full Git commit SHA"):
        build(root, tmp_path / "site", "main")
    with pytest.raises(ValueError, match="new or empty"):
        build(root, root, REVISION)
