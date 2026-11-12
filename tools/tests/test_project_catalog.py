"""Project identity, offline rendering and data-boundary regressions."""
import copy
import json
import re
from pathlib import Path

import pytest

from tools.corpus import Entry
from tools.local_index import render
from tools.project_catalog import load, markdown, validate


ROOT = Path(__file__).resolve().parents[2]


def fixture():
    entry = Entry({'code': 'P1', 'title': 'Test publication', 'view_group': 'main',
                   'doi': '10.1000/test', 'official_url': 'https://example.org/paper',
                   'pdf': '01-papers/test/paper.pdf', 'markdown': '02-fulltext/test/paper.md'},
                  'T1-perception-localization', None, False)
    data = load(ROOT)
    project = copy.deepcopy(data['projects'][0])
    project['papers'] = [{'title': 'Test publication', 'url': 'https://doi.org/10.1000/test',
                          'publication': 'Test, 2025', 'year': '2025', 'paper_codes': ['P1']}]
    data['projects'] = [project]
    return data, entry


def test_rejects_incorrect_or_excluded_publication_association():
    data, entry = fixture()
    assert validate(data, [entry]) is data
    data['projects'][0]['papers'][0]['url'] = 'https://doi.org/10.1000/unrelated'
    with pytest.raises(ValueError, match='identity mismatch'):
        validate(data, [entry])
    data, entry = fixture()
    entry.row['view_group'] = 'excluded'
    with pytest.raises(ValueError, match='Unknown active paper'):
        validate(data, [entry])


@pytest.mark.parametrize('field,value,error', [
    ('repository', 'javascript:alert(1)', 'Invalid project repository'),
    ('category', 'missing', 'Unknown project category'),
    ('methods', ['unverified'], 'Unknown or duplicate project methods'),
    ('environments', ['unverified'], 'Unknown or duplicate project environments'),
])
def test_rejects_unsafe_links_and_unregistered_facets(field, value, error):
    data, _ = fixture()
    data['projects'][0][field] = value
    with pytest.raises(ValueError, match=error):
        validate(data)


def test_duplicate_projects_are_rejected():
    data, _ = fixture()
    data['projects'].append(copy.deepcopy(data['projects'][0]))
    with pytest.raises(ValueError, match='Duplicate or invalid'):
        validate(data)


def test_offline_payload_escapes_injection_and_preserves_project_text():
    data, entry = fixture()
    malicious = '</script><script>window.injected=true</script>'
    data['projects'][0]['description'] = malicious
    page = render([entry], data)
    payload = re.search(r'<script id="project-data" type="application/json">(.*?)</script>', page, re.S).group(1)
    assert '<script>' not in payload
    assert json.loads(payload)['projects'][0]['description'] == malicious
    assert not re.search(r'__(?:PROJECT|CATALOG)_\w+__', page)
    assert 'function projectMatches' in page
    assert '<link rel="stylesheet"' not in page
    assert '<script src=' not in page
    assert page == render([entry], data)


def test_portable_directory_uses_reading_paths_not_sibling_checkout():
    data, entry = fixture()
    page = markdown(data, [entry])
    assert '1 projects' in page
    assert '[PDF](01-papers/test/paper.pdf)' in page
    assert '[Full text](02-fulltext/test/paper.md)' in page
    assert '../wheeltec-ros-textbook' not in page
    assert 'INDEX.html#view=projects' in page


def test_placeholder_text_inside_a_publication_is_preserved():
    data, entry = fixture()
    title = '__PROJECT_SCRIPT__ and __PROJECT_DATA__'
    data['projects'][0]['papers'][0]['title'] = title
    page = render([entry], data)
    payload = re.search(r'<script id="project-data" type="application/json">(.*?)</script>', page, re.S).group(1)
    assert json.loads(payload)['projects'][0]['papers'][0]['title'] == title


def test_committed_directory_retains_all_chapter_projects():
    data = load(ROOT)
    projects = data['projects']
    assert len(projects) == 66
    assert sum('drl' in p['methods'] for p in projects) == 17
    assert len({code for p in projects for ref in p['papers'] for code in ref['paper_codes']}) == 52
    assert all(p['github']['readme_url'].startswith('https://github.com/') for p in projects)
    assert next(p for p in projects if p['id'] == 'navdp')['methods'] == ['learned']
    assert next(p for p in projects if p['id'] == 'sterling')['methods'] == ['learned']
