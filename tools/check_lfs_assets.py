"""Verify the published reading assets, as LFS pointers or materialized bytes."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

from tools.common import REPO_ROOT

MANIFEST = '06-data/reading-assets.json'
_SOURCE = re.compile(r'(?:01-papers/T[1-6]-[^/]+/[^/]+/paper\.pdf|'
                     r'02-fulltext/T[1-6]-[^/]+/[^/]+/(?:paper\.md|images/[^/]+\.(?:png|jpg)))\Z')
_POINTER = re.compile(rb'version https://git-lfs.github.com/spec/v1\noid sha256:([a-f0-9]{64})\nsize ([0-9]+)\n\Z')


def load_assets(root: Path) -> dict[str, dict]:
    path = root / MANIFEST
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    assets = {}
    for item in data['files']:
        rel = item['path']
        expected_kind = 'pdf' if rel.endswith('/paper.pdf') else 'markdown' if rel.endswith('/paper.md') else 'image'
        if (not _SOURCE.fullmatch(rel) or '..' in Path(rel).parts or '\\' in rel
                or rel in assets or not re.fullmatch(r'[a-f0-9]{64}', item['sha256'])
                or type(item['bytes']) is not int or item['bytes'] <= 0
                or item['kind'] != expected_kind):
            raise ValueError('Invalid reading-asset manifest entry: ' + rel)
        assets[rel] = item
    return assets


def verify_file(path: Path, expected: dict, require_materialized: bool = False) -> str:
    with path.open('rb') as stream:
        header = stream.read(200)
        pointer = _POINTER.fullmatch(header)
        if pointer:
            if require_materialized:
                raise ValueError('LFS object has not been downloaded: ' + expected['path'])
            if pointer[1].decode() != expected['sha256'] or int(pointer[2]) != expected['bytes']:
                raise ValueError('LFS pointer does not match manifest: ' + expected['path'])
            return 'pointer'
        stream.seek(0)
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    if path.stat().st_size != expected['bytes'] or digest != expected['sha256']:
        raise ValueError('Reading bytes do not match manifest: ' + expected['path'])
    return 'materialized'


def verify(root: Path, require_materialized: bool = False) -> dict:
    assets = load_assets(root)
    if not assets:
        raise ValueError('No published reading assets registered')
    rows = list(csv.DictReader((root / '06-data/library-catalog.csv').open(encoding='utf-8-sig')))
    active = [r for r in rows if r['view_group'] in {'main', 'surveys'}]
    expected_sources = set()
    folders = set()
    for row in active:
        for field in ['pdf', 'markdown']:
            rel = row[field]
            if rel not in assets or assets[rel]['sha256'] != row[field + '_sha256']:
                raise ValueError('Catalog/reading-asset conflict: ' + row['code'])
            expected_sources.add(rel)
        folders.add(str(Path(row['markdown']).parent).replace('\\', '/'))
    actual_sources = {p for p in assets if p.endswith(('/paper.pdf', '/paper.md'))}
    if actual_sources != expected_sources:
        raise ValueError('Registered reading sources differ from admitted catalog')
    counts = {'pointer': 0, 'materialized': 0}
    for rel, item in assets.items():
        if item['kind'] == 'image' and rel.split('/images/')[0] not in folders:
            raise ValueError('Image outside admitted reading folders: ' + rel)
        counts[verify_file(root / rel, item, require_materialized)] += 1
    # Verify that Git attributes actually use the LFS clean/smudge filter.
    proc = subprocess.run(['git', 'check-attr', '-z', '--stdin', 'filter'], cwd=root,
                          input=('\0'.join(assets) + '\0').encode(), capture_output=True, check=True)
    triples = proc.stdout.decode().rstrip('\0').split('\0')
    filters = {triples[i]: triples[i+2] for i in range(0, len(triples), 3)}
    if any(filters.get(p) != 'lfs' for p in assets):
        raise ValueError('A registered reading asset is missing the Git LFS filter')
    return {'status': 'passed', 'papers': len(active), 'assets': len(assets),
            'bytes': sum(a['bytes'] for a in assets.values()), **counts}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=REPO_ROOT)
    parser.add_argument('--materialized', action='store_true')
    args = parser.parse_args(argv)
    try:
        result = verify(args.root.resolve(), args.materialized)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        parser.exit(1, str(exc) + '\n')
    print(json.dumps(result))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
