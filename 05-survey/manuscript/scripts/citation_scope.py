"""Apply explicit manuscript inclusion without removing internal library sources."""
import csv
import json


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
        date = metadata.get('published-print', metadata['published']) if metadata.get('volume') else metadata['published']
        if date['date-parts'][0][0] < policy['primary_years'][0]:
            old.add(record['key'])
    assert old == set(policy['foundational_exceptions']), 'Unjustified foundational exception'
    return records
