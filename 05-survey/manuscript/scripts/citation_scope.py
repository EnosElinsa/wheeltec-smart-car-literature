"""Apply explicit manuscript inclusion without removing internal library sources."""
import csv
import json
import re

from bib_case import protect_title


def citation_date(metadata):
    """Crossref date that gives a background record its citation year.

    Final volumes use the print year rather than the online-first year. Crossref standard
    records carry no publication date, so they fall back to the approval date.
    """
    if metadata.get('type') == 'standard':
        return next(metadata[k] for k in ('published-print', 'published', 'approved') if metadata.get(k))
    return metadata.get('published-print', metadata['published']) if metadata.get('volume') else metadata['published']


def background_entry(key, d):
    """BibTeX entry for one opened Crossref record; every field is copied from the record."""
    # Brace-protecting acronyms and proper names keeps them under IEEEtran sentence case.
    # A corporate author (Crossref 'name' without 'family') is braced so BibTeX keeps it whole.
    author = ' and '.join(a['family'] + (', ' + a['given'] if a.get('given') else '') if 'family' in a
                          else '{' + a['name'] + '}' for a in d['author'])
    fields = {'author': author, 'title': protect_title(d['title'][0]),
              'year': str(citation_date(d)['date-parts'][0][0]), 'doi': d['DOI']}
    if d.get('type') == 'standard':
        typ = 'standard'
        fields['organization'] = d['standards-body']['name']
        # Designation derived from the DOI suffix (10.4271/j3016_202104 gives J3016_202104). IEEEtran
        # splits digit runs longer than four into groups of three; an empty group keeps the code intact.
        fields['number'] = re.sub(r'(\d{4})(?=\d)', r'\1{}', d['DOI'].split('/', 1)[1].upper().replace('_', r'\_'))
    else:
        typ = 'inproceedings' if d.get('type') == 'proceedings-article' else 'article'
        fields['booktitle' if typ == 'inproceedings' else 'journal'] = d['container-title'][0]
    for k in ['volume', 'issue', 'page']:
        if d.get(k): fields[{'issue': 'number', 'page': 'pages'}.get(k, k)] = str(d[k]).replace('–', '--')
    fields = {k: v.replace('&amp;', '&').replace('&', r'\&') for k, v in fields.items()}
    return '@' + typ + '{' + key + ',\n' + ',\n'.join('  ' + k + ' = {' + v + '}' for k, v in fields.items()) + '\n}\n'


def load_corpus(root, manuscript):
    all_rows = list(csv.DictReader((root / '06-data/paper-index.csv').open(encoding='utf-8-sig', newline='')))
    inclusion = json.loads((root / '06-data/survey-inclusion.json').read_text(encoding='utf-8'))
    policy = json.loads((manuscript / 'data/citation-scope.json').read_text(encoding='utf-8'))
    indexed = {r['code'] for r in all_rows}
    selected = set(inclusion['selected_ids'])
    internal = set(policy['internal_reference_ids'])
    assert len(indexed) == len(all_rows), 'Duplicate source index identity'
    assert len(selected) == len(inclusion['selected_ids']), 'Duplicate manuscript identity'
    assert selected <= indexed, 'Selected identity missing from source index'
    assert internal == set(inclusion['internal_reference_ids']) == indexed - selected, 'Undeclared manuscript exclusion'
    assert not selected & internal, 'Internal-only source selected for manuscript'
    rows = [r for r in all_rows if r['code'] in selected]
    first, last = policy['primary_years']
    assert all(first <= int(r['bibliographic_year']) <= last for r in rows), 'Corpus source outside primary year window'
    return all_rows, rows, inclusion, policy


def load_background(manuscript, policy):
    all_records = json.loads((manuscript / 'revision/background-verification.json').read_text(encoding='utf-8'))
    excluded = set(policy['excluded_background_keys'])
    assert excluded <= {r['key'] for r in all_records}, 'Unknown background exclusion'
    records = [r for r in all_records if r['key'] not in excluded]
    old = set()
    for record in records:
        metadata = json.loads((manuscript / record['raw_record']).read_text(encoding='utf-8'))['message']
        if citation_date(metadata)['date-parts'][0][0] < policy['primary_years'][0]:
            old.add(record['key'])
    assert old == set(policy['foundational_exceptions']), 'Unjustified foundational exception'
    return records
