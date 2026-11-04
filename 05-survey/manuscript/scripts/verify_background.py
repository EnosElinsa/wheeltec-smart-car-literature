"""Acquire read-only Crossref records for separately identified background works.

Never changes a source citation.bib. Raw HTTP bodies and access dates remain in
revision/background-sources; a derived bibliography is generated separately.
"""
import concurrent.futures
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'revision/background-sources'
OUT.mkdir(parents=True, exist_ok=True)
KNOWN = {
    'B_Cadena2016': ('10.1109/TRO.2016.2624754', 'Past, Present, and Future'),
    'B_Campion1996': ('10.1109/70.481750', 'Structural properties'),
    'B_DWA1997': ('10.1109/100.580977', 'dynamic window'),
    'B_TEB2013': ('10.1109/ECMR.2013.6698833', 'Efficient trajectory optimization'),
    'B_Nav22020': ('10.1109/IROS45743.2020.9341207', 'Marathon'),
    'B_LOAM2014': ('10.15607/RSS.2014.X.007', 'LOAM'),
    'B_ORBSLAM32021': ('10.1109/TRO.2021.3075644', 'ORB-SLAM3'),
    'B_FASTLIO22022': ('10.1109/TRO.2022.3141876', 'FAST-LIO2'),
    'B_CBF2017': ('10.1109/TAC.2016.2638961', 'Control Barrier Function'),
    'B_KITTI2012': ('10.1109/CVPR.2012.6248074', 'autonomous driving'),
    'B_TUM2012': ('10.1109/IROS.2012.6385773', 'benchmark'),
    'B_Habitat2019': ('10.1109/ICCV.2019.00943', 'Habitat'),
    'B_Traversability2022': ('10.1109/ACCESS.2022.3202545', 'Survey of Traversability'),
    'B_CSLAM2022': ('10.55417/fr.2022032', 'Towards Collaborative'),
    'B_Foundation2024': ('10.1177/02783649241281508', 'Foundation models'),
    'B_HumanAware2013': ('10.1016/j.robot.2013.05.007', 'Human-aware'),
}
QUERIES = {
    'social-review': 'A Survey of Socially Aware Robot Navigation',
    'terrain-review': 'terrain traversability analysis survey review mobile robots',
    'collaborative-slam-review': 'survey multi robot collaborative simultaneous localization mapping',
    'foundation-review': 'Foundation Models in Robotics Applications Challenges and the Future',
    'integrity-review': 'review integrity monitoring autonomous ground vehicle localization',
}

def fetch(item):
    key, (doi, expected) = item
    path = OUT / (key + '.json')
    if path.exists():
        payload = json.loads(path.read_text(encoding='utf-8'))
        if payload['message'].get('DOI', '').casefold() != doi.casefold():
            path = OUT / (key + '-corrected.json')
            if path.exists():
                payload = json.loads(path.read_text(encoding='utf-8'))
            else:
                response = requests.get('https://api.crossref.org/works/' + doi, timeout=35)
                response.raise_for_status()
                payload = response.json()
                path.write_bytes(response.content)
    else:
        response = requests.get('https://api.crossref.org/works/' + doi, timeout=35)
        response.raise_for_status()
        payload = response.json()
        path.write_bytes(response.content)
    data = payload['message']
    title = ' '.join(data.get('title', []))
    assert expected.casefold() in title.casefold(), (key, title)
    assert doi.casefold() == data['DOI'].casefold()
    assert data.get('author') and data.get('container-title') and data.get('published')
    return {'key': key, 'doi': data['DOI'], 'title': title,
            'raw_record': path.relative_to(ROOT).as_posix(),
            'verified_utc': datetime.now(timezone.utc).isoformat(),
            'scope': 'identity/metadata verified from opened Crossref DOI record; background only'}

def query(item):
    key, terms = item
    path = OUT / ('query-' + key + '.json')
    if path.exists():
        payload = json.loads(path.read_text(encoding='utf-8'))
    else:
        response = requests.get('https://api.crossref.org/works', params={'query.title': terms, 'rows': 4}, timeout=35)
        response.raise_for_status()
        payload = response.json()
        path.write_bytes(response.content)
    return key, [{'doi': d['DOI'], 'title': d.get('title'), 'year': d.get('published'),
                  'venue': d.get('container-title')} for d in payload['message']['items']]

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    records, errors = [], []
    for item in KNOWN.items():
        try:
            result = fetch(item); records.append(result)
            print(json.dumps(result, ensure_ascii=False))
        except Exception as error:
            errors.append(str(error)); print(type(error).__name__, str(error)[:250])
        time.sleep(1.5)
    (ROOT / 'revision/background-verification.json').write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    if errors:
        print('Unresolved background queries:', len(errors))
