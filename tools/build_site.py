"""Build the Pages catalog and readable full texts without copying large LFS files."""
from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import shutil
from urllib.parse import quote, unquote, urlsplit

import bleach
import markdown

from tools.common import REPO_ROOT

REPOSITORY = "EnosElinsa/wheeltec-smart-car-literature"
CATALOG = re.compile(r'(<script id="catalog-data" type="application/json">)(.*?)(</script>)', re.S)
READER_TEMPLATE = Path(__file__).with_name("pages_reader.html")
ALLOWED_TAGS = {
    "a", "abbr", "b", "blockquote", "br", "caption", "code", "dd", "del", "details",
    "div", "dl", "dt", "em", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "i", "img",
    "li", "ol", "p", "pre", "s", "span", "strong", "sub", "summary", "sup", "table",
    "tbody", "td", "th", "thead", "tr", "ul",
}


def source_url(path: str, revision: str, *, media: bool = False, raw: bool = False) -> str:
    """Pin source links to the same commit as the deployed catalog."""
    if not path or path.startswith(("/", "\\")) or "\\" in path:
        raise ValueError(f"Invalid repository path: {path!r}")
    if any(part in {".", ".."} for part in path.split("/")) or urlsplit(path).scheme:
        raise ValueError(f"Invalid repository path: {path!r}")
    encoded = quote(path, safe="/")
    if media:
        return f"https://media.githubusercontent.com/media/{REPOSITORY}/{revision}/{encoded}"
    if raw:
        return f"https://raw.githubusercontent.com/{REPOSITORY}/{revision}/{encoded}"
    return f"https://github.com/{REPOSITORY}/blob/{revision}/{encoded}"


class ReaderLinks(HTMLParser):
    """Resolve sanitized source links relative to the original Markdown folder."""

    def __init__(self, source: str, revision: str, assets: set[str]):
        super().__init__(convert_charrefs=False)
        self.folder = posixpath.dirname(source)
        self.revision = revision
        self.assets = assets
        self.output: list[str] = []

    def resolve(self, value: str) -> str:
        parsed = urlsplit(value)
        if value.startswith("#") or parsed.scheme in {"https", "http", "mailto"}:
            return value
        if parsed.netloc or not parsed.path:
            return ""
        path = posixpath.normpath(posixpath.join(self.folder, unquote(parsed.path)))
        if path.startswith(("../", "/")):
            return ""
        try:
            result = source_url(path, self.revision, media=path in self.assets)
        except ValueError:
            # Some transcriptions contain formula syntax that Markdown interprets
            # as a link. Keep its text without inventing a repository resource.
            return ""
        return result + ("#" + parsed.fragment if parsed.fragment else "")

    def handle_starttag(self, tag, attrs):
        values = []
        for key, value in attrs:
            if value is None:
                continue
            if key in {"href", "src"}:
                value = self.resolve(value)
                if not value:
                    continue
            values.append(f' {key}="{html.escape(value, quote=True)}"')
        if tag == "img":
            values.append(' loading="lazy" decoding="async"')
        self.output.append("<" + tag + "".join(values) + ">")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        self.output.append(f"</{tag}>")

    def handle_data(self, data):
        self.output.append(data)

    def handle_entityref(self, name):
        self.output.append(f"&{name};")

    def handle_charref(self, name):
        self.output.append(f"&#{name};")


def render_fulltext(text: str, source: str, revision: str, assets: set[str]) -> str:
    rendered = markdown.markdown(
        text, extensions=["tables", "fenced_code", "sane_lists", "pymdownx.arithmatex"],
        extension_configs={"pymdownx.arithmatex": {"generic": True}},
    )
    cleaned = bleach.clean(
        rendered, tags=ALLOWED_TAGS,
        attributes={"a": ["href", "title"], "img": ["src", "alt", "title", "width", "height"],
                    "span": ["class"], "div": ["class"],
                    "th": ["align", "colspan", "rowspan"], "td": ["align", "colspan", "rowspan"]},
        protocols={"http", "https", "mailto"}, strip=True,
    )
    parser = ReaderLinks(source, revision, assets)
    parser.feed(cleaned)
    parser.close()
    return "".join(parser.output)


def build(root: Path, out: Path, revision: str) -> dict[str, int]:
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("--revision must be a full Git commit SHA")
    if out.resolve() == root.resolve() or (out.exists() and any(out.iterdir())):
        raise ValueError("The site output must be a new or empty directory")
    page = (root / "INDEX.html").read_text(encoding="utf-8")
    match = CATALOG.search(page)
    if match is None:
        raise ValueError("INDEX.html has no embedded paper catalog")
    records = json.loads(match[2])
    assets = {item["path"]: item for item in json.loads(
        (root / "06-data/reading-assets.json").read_text(encoding="utf-8"))["files"]}
    template = READER_TEMPLATE.read_text(encoding="utf-8")
    outputs: dict[str, bytes] = {}
    for row in records:
        code = row["code"]
        if not re.fullmatch(r"[A-Za-z0-9_-]+", code):
            raise ValueError(f"Invalid paper code: {code!r}")
        source = row["markdown"]
        metadata = assets.get(source)
        if metadata is None or metadata["kind"] != "markdown":
            raise ValueError(f"Unregistered full text: {source}")
        data = (root / source).read_bytes()
        if len(data) != metadata["bytes"] or hashlib.sha256(data).hexdigest() != metadata["sha256"]:
            raise ValueError(f"Full text is missing or differs from its manifest: {source}; run git lfs pull")
        body = render_fulltext(data.decode("utf-8-sig"), source, revision, set(assets))
        fields = {
            "TITLE": html.escape(row["title"]), "CONTENT": body,
            "CATALOG": "../#search=" + quote(code),
            "PDF": html.escape(source_url(row["pdf"], revision, media=True), quote=True),
            "MARKDOWN": html.escape(source_url(source, revision, media=True), quote=True),
            "CITATION": "../citations/" + code + ".bib",
        }
        reader = re.sub(r"__(TITLE|CONTENT|CATALOG|PDF|MARKDOWN|CITATION)__",
                        lambda m: fields[m[1]], template)
        outputs[f"fulltext/{code}.html"] = reader.encode("utf-8")
        citation = row["bibtex"]
        if not citation or PurePosixPath(citation).name != "citation.bib":
            raise ValueError(f"Missing citation for {code}")
        outputs[f"citations/{code}.bib"] = (root / citation).read_bytes()
        row["pdf"] = source_url(row["pdf"], revision, media=True)
        row["markdown"] = f"fulltext/{code}.html"
        row["bibtex"] = f"citations/{code}.bib"
        if row["review"]:
            row["review"] = source_url(row["review"], revision)
    payload = json.dumps(records, ensure_ascii=True, separators=(",", ":")).replace("<", "\\u003c")
    page = CATALOG.sub(lambda m: m[1] + payload + m[3], page)
    page = page.replace("</head>", '<link rel="icon" href="favicon.svg">\n</head>')
    # The remaining authored navigation points at repository documents.
    for path in ("README.md", "01-papers/INDEX.md", "05-survey/manuscript/survey.pdf"):
        url = source_url(path, revision, raw=path.endswith(".pdf"))
        page = page.replace(f'href="{path}"', f'href="{url}"')
    outputs["index.html"] = page.encode("utf-8")
    outputs["INDEX.html"] = outputs["index.html"]
    outputs[".nojekyll"] = b""
    outputs["favicon.svg"] = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
        '<rect width="32" height="32" rx="4" fill="#242b35"/>'
        '<text x="16" y="23" text-anchor="middle" font-family="sans-serif" '
        'font-weight="bold" font-size="23" fill="white">W</text></svg>'
    ).encode("utf-8")
    for path, data in outputs.items():
        target = out / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    (out / "assets").mkdir(exist_ok=True)
    shutil.copyfile(Path(__file__).with_name("pages_reader.css"), out / "assets/reader.css")
    return {"papers": len(records), "files": len(outputs) + 1,
            "bytes": sum(len(data) for data in outputs.values()) + (out / "assets/reader.css").stat().st_size}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    parser.add_argument("--out", type=Path, default=Path("_site"))
    parser.add_argument("--revision", required=True)
    args = parser.parse_args(argv)
    result = build(args.root, args.out, args.revision)
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
