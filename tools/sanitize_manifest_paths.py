"""Replace local MinerU cache paths in ``06-data/fulltext-manifest.json``.

The historical manifest recorded the absolute path of the local parser cache
for each Markdown file. The path identifies the local machine and user, so the
public copy keeps only the content-addressed part of the path, for example
``arp-mineru-cache/<pdf-sha256>/precision/paper.md``. The original file is
kept locally in ``99-archive/superseded/``.

Usage::

    python -m tools.sanitize_manifest_paths
"""

from __future__ import annotations

import json
import re

from tools.common import REPO_ROOT

MANIFEST = REPO_ROOT / "06-data" / "fulltext-manifest.json"
CACHE_PATTERN = re.compile(
    r"^[A-Za-z]:[\\/].*?[\\/]acquire-research-papers[\\/](?P<sha>[0-9a-f]{64})[\\/](?P<rest>.+)$"
)


def sanitize_origin(origin: str) -> str:
    match = CACHE_PATTERN.match(origin)
    if not match:
        return origin
    rest = match.group("rest").replace("\\", "/")
    return f"arp-mineru-cache/{match.group('sha')}/{rest}"


def main() -> int:
    raw = MANIFEST.read_bytes()
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    records = json.loads(raw.decode("utf-8-sig"))
    changed = 0
    for record in records:
        origin = record.get("source_origin", "")
        clean = sanitize_origin(origin)
        if clean != origin:
            record["source_origin"] = clean
            changed += 1
    text = json.dumps(records, indent=2, ensure_ascii=False) + "\n"
    MANIFEST.write_bytes((b"\xef\xbb\xbf" if has_bom else b"") + text.encode("utf-8"))
    print(f"sanitized {changed} source_origin values")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
