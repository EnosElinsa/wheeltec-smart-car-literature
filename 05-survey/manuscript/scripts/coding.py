"""Evidence coding: codebook checks, stratified sample draw, code validation and agreement statistics.

Run from 05-survey/manuscript:
  python scripts/coding.py --check-codebook
  python scripts/coding.py --self-test
  python scripts/coding.py --draw-sample                 # print the draw record as JSON, write nothing
  python scripts/coding.py --draw-sample --check-only    # redraw and compare with the published sampling record
  python scripts/coding.py --check-codes PATH --kind primary|second [--partial]
"""
import argparse
import csv
import json
import random
import re
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

M = Path(__file__).resolve().parents[1]
from project_paths import literature_root
from citation_scope import load_corpus
R = literature_root(M)
CODING = R / '06-data' / 'evidence-coding'
CODEBOOK_JSON = CODING / 'codebook.json'
CODEBOOK_MD = CODING / 'codebook.md'
KINDS = {'given', 'derived', 'coded'}
FORMS = {'one', 'set', 'one-or-two', 'text'}


def load_codebook(path=CODEBOOK_JSON):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def split_set(value):
    value = (value or '').strip()
    return [] if value in ('', 'none') else value.split('|')


def attribute(codebook, name):
    return next(a for a in codebook['attributes'] if a['name'] == name)


def function_order(codebook):
    return [f['id'] for f in codebook['functions']]


def section_function(codebook):
    return {f['section']: f['id'] for f in codebook['functions']}


def principal_of(row, codebook):
    if row['survey_included'] == 'context':
        return 'context'
    return {f['module']: f['section'] for f in codebook['functions']}[row['survey_module']]


def depth_of(row, codebook):
    rule = codebook['depth_rule']
    if row['verification_level'] == 'full':
        return 'full'
    return 'light-legacy' if row['source_batch'] in rule['legacy_batches'] else 'light-targeted'


def level_of(evidence_type, codebook):
    return next(l['id'] for l in codebook['evidence_levels'] if evidence_type in l['evidence_type'])


def level_rank(level, codebook):
    return next(l['rank'] for l in codebook['evidence_levels'] if l['id'] == level)


def group_of(platform_class, codebook):
    return next(g['id'] for g in codebook['platform_groups'] if platform_class in g['platform_classes'])


def publisher_of(row, codebook):
    if row['doi']:
        return codebook['publisher_prefixes'][row['doi'].split('/')[0]]
    return codebook['publisher_hosts'][row['official_url'].split('/')[2]]


def derived_values(row, codebook):
    """Given and derived columns of one work, computed from its paper-index row."""
    evaluation = {x.strip() for x in row['evaluation_all'].split(',')}
    return {
        'code': row['code'],
        'principal_section': principal_of(row, codebook),
        'stage': row['source_batch'],
        'depth': depth_of(row, codebook),
        'level_strongest': level_of(row['evidence_type'], codebook),
        'integrity': 'yes' if 'integrity-reliability' in evaluation else 'no',
        'placement_reported': 'no' if row['compute_location'] in ('not-reported', 'not-applicable') else 'yes',
        'platform_group': group_of(row['platform_class'], codebook),
        'drivetrain': codebook['drivetrain_map'].get(row['platform_class'], 'na'),
    }


# --------------------------------------------------------------------------- codebook check

def vocabulary_values(heading):
    """Backticked values of the first table under a heading of 06-data/vocabulary.md."""
    lines = (R / '06-data/vocabulary.md').read_text(encoding='utf-8').splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith('### ') and heading in line)
    values = []
    for line in lines[start + 1:]:
        if line.startswith('#'):
            break
        match = re.match(r'\|\s*`([^`]+)`\s*\|', line)
        if match:
            values.append(match.group(1))
    return values


def markdown_attribute_table(text):
    """Rows of the 'Attribute summary' table of codebook.md."""
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith('## ') and line.strip().endswith('Attribute summary'))
    rows, in_table = [], False
    for line in lines[start + 1:]:
        if line.startswith('## ') or (in_table and not line.startswith('|')):
            break
        in_table = in_table or line.startswith('|')
        if line.startswith('| `'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            rows.append({'name': cells[0].strip('`'), 'kind': cells[1], 'form': cells[2],
                         'values': re.findall(r'`([^`]+)`', cells[3]), 'double_coded': cells[4] == 'yes'})
    return rows


def check_codebook(codebook, rows, markdown_text=None):
    errors = []
    sources = [s['id'] for s in codebook['sources']]
    functions = function_order(codebook)
    families = [f['id'] for f in codebook['response_families']]
    levels = [l['id'] for l in codebook['evidence_levels']]
    groups = [g['id'] for g in codebook['platform_groups']]
    if sources != codebook['source_order']:
        errors.append('sources differ from source_order')
    # Vocabulary maps: every degradation value to one source, every platform class to one group.
    for value in vocabulary_values('`degradation` and `degradation_observed`'):
        if value == 'none':
            continue
        hits = [s['id'] for s in codebook['sources'] if value in s['vocabulary']]
        if len(hits) != 1:
            errors.append(f'degradation value {value} maps to {hits}')
    vocabulary_classes = vocabulary_values('`platform_class`')
    for value in vocabulary_classes:
        hits = [g['id'] for g in codebook['platform_groups'] if value in g['platform_classes']]
        if len(hits) != 1:
            errors.append(f'platform_class {value} maps to {hits}')
    mapped = {v for s in codebook['sources'] for v in s['vocabulary']}
    if not mapped <= set(vocabulary_values('`degradation` and `degradation_observed`')):
        errors.append('a source maps an undocumented vocabulary value')
    for row in rows:
        for field in ('degradation', 'degradation_observed'):
            for value in (x.strip() for x in row[field].split(',')):
                if value != 'none' and value not in mapped:
                    errors.append(f"{row['code']} {field} value {value} has no source")
        try:
            publisher_of(row, codebook)
        except KeyError:
            errors.append(f"{row['code']} has no publisher mapping")
        if row['source_batch'] not in codebook['stage_labels']:
            errors.append(f"{row['code']} stage {row['source_batch']} has no label")
        if row['platform_class'] not in vocabulary_classes:
            errors.append(f"{row['code']} platform_class {row['platform_class']} undocumented")
        try:
            level_of(row['evidence_type'], codebook)
        except StopIteration:
            errors.append(f"{row['code']} evidence_type {row['evidence_type']} has no level")
    if list(codebook['stage_labels']) != codebook['stage_order']:
        errors.append('stage_labels order differs from stage_order')
    # Attributes.
    names = [a['name'] for a in codebook['attributes']]
    if names != codebook['columns']:
        errors.append('attribute list differs from columns')
    for a in codebook['attributes']:
        if a['kind'] not in KINDS or a['form'] not in FORMS:
            errors.append(f"{a['name']}: kind or form invalid")
        if not a.get('rule') or not a.get('locator') or not a.get('derivation'):
            errors.append(f"{a['name']}: rule, locator or derivation missing")
        if a['form'] != 'text' and a['name'] != 'code' and not a['values']:
            errors.append(f"{a['name']}: no allowed values")
        if a['double_coded'] and a['kind'] != 'coded':
            errors.append(f"{a['name']}: double-coded but not coded")
    expected = {
        'principal_section': [f['section'] for f in codebook['functions']] + ['context'],
        'stage': codebook['stage_order'],
        'functions': functions + ['none'],
        'src_addressed': sources + ['none'], 'src_manipulated': sources + ['none'],
        'src_selected': sources + ['none'], 'src_incidental': sources + ['none'],
        'response_family': families,
        'level_strongest': levels, 'level_degradation': levels + ['none'],
        'platform_group': groups,
        'drivetrain': list(dict.fromkeys(codebook['drivetrain_map'].values())) + ['na'],
        'depth': ['full', 'light-legacy', 'light-targeted'],
    }
    for name, values in expected.items():
        if attribute(codebook, name)['values'] != values:
            errors.append(f'{name}: values differ from the codebook lists')
    double = [a['name'] for a in codebook['attributes'] if a['double_coded']]
    if double != codebook['double_coding']['attributes']:
        errors.append('double_coding.attributes differs from the double-coded flags')
    single = [a['name'] for a in codebook['attributes'] if not a['double_coded'] and a['name'] not in ('code', 'notes')]
    if single != codebook['double_coding']['not_double_coded']:
        errors.append('double_coding.not_double_coded differs from the attribute flags')
    work_fields = ['code'] + double + ['notes']
    if work_fields != codebook['second_coder_output']['work_fields']:
        errors.append('second_coder_output.work_fields differs from the double-coded attributes')
    # Sources, assumptions, families.
    for s in codebook['sources']:
        owners = [a['id'] for a in codebook['assumptions'] if s['id'] in a['sources']]
        if owners != [s['assumption']]:
            errors.append(f"source {s['id']} assumption mismatch {owners}")
        group = [g['id'] for g in codebook['source_groups'] if s['id'] in g['sources']]
        if group != [s['group']]:
            errors.append(f"source {s['id']} group mismatch {group}")
    for a in codebook['assumptions']:
        for family in a['response_families']:
            if family not in families:
                errors.append(f"assumption {a['id']} names unknown family {family}")
    for f in codebook['response_families']:
        if f['section'] not in [x['section'] for x in codebook['functions']] + ['any', 'context']:
            errors.append(f"family {f['id']} has unknown section")
    ranking = codebook['interface_ranking']
    for cell_owner in ranking['interfaces'] + ranking['named_alternatives']:
        cells = cell_owner.get('cells', cell_owner)
        for pair in cells['pairs']:
            if len(pair) != 2 or pair[0] == pair[1] or functions.index(pair[0]) > functions.index(pair[1]):
                errors.append(f"{cell_owner['name']}: pair {pair} not in function order")
        if not set(cells['sources']) <= set(sources):
            errors.append(f"{cell_owner['name']}: unknown source")
    for key in ('sensitivity', 'findings', 'consistency_rules'):
        ids = [x['id'] for x in codebook[key]]
        if len(ids) != len(set(ids)):
            errors.append(f'{key}: duplicate ids')
    sampling = codebook['sampling']
    if sampling['sections'] != [f['section'] for f in codebook['functions']]:
        errors.append('sampling sections differ from function sections')
    if sampling['per_section'] * len(sampling['sections']) != sampling['sample_size']:
        errors.append('sampling size differs from per-section allocation')
    if not set(codebook['stage_groups']['quota_stages'] + codebook['stage_groups']['ieee_only_stages']) <= set(codebook['stage_order']):
        errors.append('stage group names an unknown stage')
    # The fictional worked example satisfies the rules.
    errors += self_check_example(codebook)
    # Human-readable codebook agrees with this file.
    if markdown_text is not None:
        table = markdown_attribute_table(markdown_text)
        if [t['name'] for t in table] != names:
            errors.append('codebook.md attribute summary differs in names or order')
        for t in table:
            a = attribute(codebook, t['name']) if t['name'] in names else None
            if a is None:
                continue
            if (t['kind'], t['form'], t['double_coded']) != (a['kind'], a['form'], a['double_coded']):
                errors.append(f"codebook.md: {t['name']} kind, form or double-coded flag differs")
            if t['values'] != (a['values'] or []):
                errors.append(f"codebook.md: {t['name']} allowed values differ")
        required = ([str(sampling['seed'])] + sources + families + [x['id'] for x in codebook['consistency_rules']]
                    + [x['id'] for x in codebook['findings']] + [x['id'] for x in codebook['sensitivity']]
                    + [a['id'] for a in codebook['assumptions']] + groups)
        for token in required:
            if f'`{token}`' not in markdown_text and token not in markdown_text:
                errors.append(f'codebook.md does not mention {token}')
        if f"Version {codebook['version']}" not in markdown_text:
            errors.append('codebook.md version differs')
        blocks = re.findall(r'```json\n(.*?)\n```', markdown_text, flags=re.S)
        if [json.loads(b) for b in blocks] != [codebook['second_coder_output']['example']]:
            errors.append('codebook.md output example differs from codebook.json')
    return errors


def self_check_example(codebook):
    """Validate the fictional Z98 and Z99 examples of the output schema against the rules."""
    example = codebook['second_coder_output']['example']
    base = {'survey_module': 'localization-mapping', 'survey_included': 'yes', 'source_batch': 'expansion-2026-10-24',
            'verification_level': 'full'}
    rows = [dict(base, code='Z98', evidence_type='closed-loop-hardware', evaluation_all='residual, closed-loop-task',
                 compute_location='onboard', platform_class='skid-steer'),
            dict(base, code='Z99', evidence_type='dataset-playback', evaluation_all='residual, designed-degradation',
                 compute_location='desktop-offline', platform_class='wheeled-unspecified')]
    by_code = {r['code']: r for r in rows}
    codes = [dict(derived_values(by_code[w['code']], codebook), mixed_wheeled='na', transfer_basis='na', **w)
             for w in example['works']]
    if [c['code'] for c in codes] != [r['code'] for r in rows]:
        return ['example: works differ from Z98 and Z99']
    errors, warnings = validate_codes(codes, rows, codebook, 'primary', partial=True, locators=example['locators'])
    return [f'example: {e}' for e in errors + warnings]


# --------------------------------------------------------------------------- sample draw

def allocation(technical_rows, codebook):
    sampling = codebook['sampling']
    result = {}
    for section in sampling['sections']:
        counts = Counter(depth_of(r, codebook) for r in technical_rows if principal_of(r, codebook) == section)
        full = min(sampling['full_per_section'], counts['full'])
        rest = sampling['per_section'] - full
        light = ['light-legacy', 'light-targeted']
        total = sum(counts[d] for d in light)
        quota = {d: Fraction(rest * counts[d], total) for d in light}
        seats = {d: int(quota[d]) for d in light}
        for d in sorted(light, key=lambda d: (-(quota[d] - seats[d]), light.index(d)))[:rest - sum(seats.values())]:
            seats[d] += 1
        assert all(seats[d] <= counts[d] for d in light), section
        result[section] = {'full': full, **seats}
    return result


def draw_sample(technical_rows, codebook):
    """Deterministic stratified draw of the second-coding sample (codebook 'sampling' rule)."""
    sampling = codebook['sampling']
    seed = sampling['seed']
    alloc = allocation(technical_rows, codebook)
    by_code = {r['code']: r for r in technical_rows}
    stage_sizes = Counter(r['source_batch'] for r in technical_rows)
    required = [s for s in codebook['stage_order'] if stage_sizes[s] >= sampling['min_stage_size']]
    rejected = []
    for k in range(1000):
        rng = random.Random(seed + k)
        picks = []
        for section in sampling['sections']:
            for depth in sampling['depth_order']:
                candidates = sorted(r['code'] for r in technical_rows
                                    if principal_of(r, codebook) == section and depth_of(r, codebook) == depth)
                picks += [(code, section, depth) for code in rng.sample(candidates, alloc[section][depth])]
        missing = [s for s in required if s not in {by_code[c]['source_batch'] for c, _, _ in picks}]
        if not missing:
            break
        rejected.append({'k': k, 'missing_stages': missing})
    else:
        raise RuntimeError('no attempt satisfied the stage coverage')
    works = [{'code': code, 'principal_section': section, 'stage': by_code[code]['source_batch'], 'depth': depth,
              'stratum': f'{section}/{depth}', 'draw_order': i + 1} for i, (code, section, depth) in enumerate(picks)]
    assert len(works) == sampling['sample_size'] == len({w['code'] for w in works})
    return {'seed': seed, 'k': k, 'generator_seed': seed + k, 'python': sys.version.split()[0],
            'allocation': alloc, 'required_stages': required, 'rejected_attempts': rejected, 'works': works}


def technical(rows):
    return [r for r in rows if r['survey_included'] == 'yes']


# --------------------------------------------------------------------------- code validation

def load_codes(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames, list(reader)


def locator_path(codes_path):
    path = Path(codes_path)
    return path.with_name(path.name.replace('codes', 'locators'))


def required_locators(code, codebook):
    """(attribute, value) pairs of one coded work that need a locator row."""
    principal = section_function(codebook).get(code['principal_section'])
    needed = []
    for name in ('functions',):
        needed += [(name, v) for v in split_set(code[name]) if v != principal]
    for name in ('src_addressed', 'src_manipulated', 'src_selected', 'src_incidental', 'response_family'):
        needed += [(name, v) for v in split_set(code[name])]
    for name, absent in (('nominal_control', {'no', 'na'}), ('single_level_injection', {'no'}),
                         ('task_setting', {'none'}), ('deg_task_class', {'none'}), ('deg_task_setting', {'none'}),
                         ('level_degradation', {'none'}), ('drivetrain_effect', {'no'}),
                         ('mixed_wheeled', {'no', 'na', ''}), ('transfer_basis', {'na', ''})):
        if code.get(name, '') not in absent:
            needed.append((name, code[name]))
    if code['principal_section'] == 'context':
        needed = [n for n in needed if n[0] != 'response_family']
    return needed


def validate_codes(codes, corpus_rows, codebook, kind, partial=False, locators=None):
    """Return (errors, warnings). kind 'second' keeps the second coder's values: rule breaks are warnings."""
    errors, warnings = [], []
    soft = warnings if kind == 'second' else errors
    by_code = {r['code']: r for r in corpus_rows}
    order = {name: (attribute(codebook, name)['values'] or []) for name in codebook['columns']}
    families = {f['id']: f['section'] for f in codebook['response_families']}
    function_of = section_function(codebook)
    seen = Counter(c['code'] for c in codes)
    errors += [f'{c}: duplicate row' for c, n in seen.items() if n > 1]
    unknown = set(seen) - set(by_code)
    errors += [f'{c}: not a corpus work' for c in sorted(unknown)]
    if not partial and kind == 'primary' and set(seen) != set(by_code):
        errors.append(f'missing works: {sorted(set(by_code) - set(seen))}')
    index = {}
    for loc in locators or []:
        index.setdefault((loc['code'], loc['attribute'], loc['value']), []).append(loc)
        allowed_sources = codebook['locator_rules']['second_coder_sources' if kind == 'second' else 'sources']
        if loc['source'] not in allowed_sources:
            soft.append(f"{loc['code']}: locator source {loc['source']} not allowed")
        if not loc.get('locator', '').strip():
            soft.append(f"{loc['code']}: empty locator for {loc['attribute']}")
    checked = set(codebook['double_coding']['attributes']) if kind == 'second' else set(codebook['columns'])
    for code in codes:
        if code['code'] not in by_code:
            continue
        cid = code['code']
        derived = derived_values(by_code[cid], codebook)
        for name, value in derived.items():
            if code.get(name) != value:
                errors.append(f'{cid}: {name} is {code.get(name)!r}, derivation gives {value!r} (CR16)')
        bad = False
        for a in codebook['attributes']:
            name, value = a['name'], code.get(a['name'], '')
            if a['form'] == 'text' or name == 'code' or name not in checked:
                continue
            parts = value.split('|') if a['form'] in ('set', 'one-or-two') else [value]
            attribute_bad = False
            for part in parts:
                if kind == 'second' and part.startswith('invalid:'):
                    warnings.append(f'{cid}: {name} kept as {part}')
                    attribute_bad = True
                elif part not in order[name]:
                    errors.append(f'{cid}: {name} value {part!r} not allowed')
                    attribute_bad = True
            bad = bad or attribute_bad
            if a['form'] == 'set' and not attribute_bad:
                if len(parts) != len(set(parts)) or ('none' in parts and len(parts) > 1):
                    errors.append(f'{cid}: {name} malformed set {value!r}')
                elif parts != sorted(parts, key=order[name].index):
                    soft.append(f'{cid}: {name} not in canonical order (CR18)')
            if a['form'] == 'one-or-two' and (len(parts) > 2 or len(parts) != len(set(parts))):
                errors.append(f'{cid}: {name} needs one or two distinct values')
        if bad:
            continue
        S = {n: set(split_set(code[n])) for n in ('functions', 'src_addressed', 'src_manipulated', 'src_selected', 'src_incidental')}
        context = code['principal_section'] == 'context'
        rules = []
        principal = function_of.get(code['principal_section'])
        if context:
            rules.append(('CR01', not S['functions']))
            rules.append(('CR19', not any(S[n] for n in S) and code['response_family'] == 'context'
                          and code['nominal_control'] == 'na' and code['single_level_injection'] == 'no'
                          and code['task_setting'] == code['deg_task_class'] == code['deg_task_setting'] == 'none'
                          and code['level_degradation'] == 'none' and code['drivetrain_effect'] == 'no'))
        else:
            rules.append(('CR01', principal in S['functions']))
        named = S['src_manipulated'] | S['src_selected']
        rules += [
            ('CR02', named <= S['src_addressed']),
            ('CR03', not (S['src_manipulated'] & S['src_selected'] or S['src_manipulated'] & S['src_incidental']
                         or S['src_selected'] & S['src_incidental'])),
            ('CR04', (code['nominal_control'] == 'na') == (not S['src_manipulated'])),
            ('CR05', code['single_level_injection'] == 'no' or bool(S['src_selected'])),
            ('CR06', code['deg_task_class'] != 'D1' or bool(S['src_manipulated'])),
            ('CR06', code['deg_task_class'] != 'D2' or bool(named)),
            ('CR07', (code['deg_task_setting'] == 'none') == (code['deg_task_class'] == 'none')),
            ('CR08', code['deg_task_setting'] != 'physical' or code['task_setting'] in ('physical', 'both')),
            ('CR08', code['deg_task_setting'] != 'simulation' or code['task_setting'] in ('simulation', 'both')),
            ('CR09', (code['level_degradation'] == 'none') == (not named)),
            ('CR10', code['deg_task_setting'] != 'physical' or code['level_degradation'] == 'P'),
        ]
        if code['level_degradation'] != 'none' and code['level_strongest'] != 'X':
            rules.append(('CR11', level_rank(code['level_degradation'], codebook) <= level_rank(code['level_strongest'], codebook)))
        family = code['response_family'].split('|')
        resource = by_code[cid]['evidence_type'] == 'dataset-resource'
        if context:
            rules.append(('CR12', family[0] == 'context'))
        elif resource:
            rules.append(('CR12', family[0] == 'resource'))
        else:
            rules.append(('CR12', families.get(family[0]) == code['principal_section']))
        rules.append(('CR12', all(f not in ('context',) for f in family[1:])))
        if not context and not resource:
            rules.append(('CR13', bool(S['src_addressed']) or bool(code.get('notes', '').strip())))
        if kind == 'primary':
            mixed = by_code[cid]['platform_class'] == 'mixed'
            rules.append(('CR14', (code['mixed_wheeled'] == 'na') == (not mixed)))
            rules.append(('CR15', (code['transfer_basis'] == 'na') == (code['platform_group'] == 'WHL' or context)))
        for rule_id, ok in rules:
            if not ok:
                soft.append(f'{cid}: rule {rule_id} broken')
        # Locators.
        depth = code['depth']
        for name, value in required_locators(code, codebook):
            if kind == 'second' and name not in checked:
                continue
            rows = index.get((cid, name, value), [])
            if not rows:
                soft.append(f'{cid}: no locator for {name}={value} (CR17)')
            elif depth == 'light-legacy' and not any(r['source'] in ('pdf', 'transcription') for r in rows):
                soft.append(f'{cid}: light-legacy value {name}={value} needs a pdf or transcription locator (CR17)')
    return errors, warnings


# --------------------------------------------------------------------------- agreement

def percent_agreement(a, b):
    assert len(a) == len(b)
    return sum(x == y for x, y in zip(a, b)) / len(a) if a else None


def cohen_kappa(a, b):
    """Unweighted Cohen's kappa; None when expected agreement is 1 or there are no units."""
    assert len(a) == len(b)
    n = len(a)
    if n == 0:
        return None
    po = Fraction(sum(x == y for x, y in zip(a, b)), n)
    ca, cb = Counter(a), Counter(b)
    pe = sum(Fraction(ca[c], n) * Fraction(cb[c], n) for c in set(a) | set(b))
    if pe == 1:
        return None
    return float((po - pe) / (1 - pe))


def apply_adjudication(codes, log):
    """Final codes: frozen codes with every logged resolution applied."""
    final = {c['code']: dict(c) for c in codes}
    for entry in log:
        row = final[entry['code']]
        assert row[entry['attribute']] == entry['primary_value'], (entry['code'], entry['attribute'])
        row[entry['attribute']] = entry['resolved_value']
    return [final[c['code']] for c in codes]


# --------------------------------------------------------------------------- command line

def self_test(codebook, technical_rows):
    a = [1] * 10 + [0] * 10
    b = [1] * 7 + [0] * 3 + [1] * 3 + [0] * 7
    assert percent_agreement(a, b) == 0.7
    assert abs(cohen_kappa(a, b) - 0.4) < 1e-12
    assert cohen_kappa(['x'] * 5, ['x'] * 5) is None
    assert cohen_kappa([], []) is None
    assert cohen_kappa(['a', 'b'], ['a', 'b']) == 1.0
    assert draw_sample(technical_rows, codebook) == draw_sample(technical_rows, codebook)
    assert self_check_example(codebook) == []
    codes = [{'code': 'Z99', 'src_selected': 'PER'}]
    log = [{'code': 'Z99', 'attribute': 'src_selected', 'primary_value': 'PER', 'resolved_value': 'none'}]
    assert apply_adjudication(codes, log)[0]['src_selected'] == 'none' and codes[0]['src_selected'] == 'PER'
    print('self-test OK')


def check_only(record):
    manifest = CODING / 'sample-manifest.csv'
    sampling = CODING / 'sampling.json'
    if not manifest.is_file() or not sampling.is_file():
        print('sampling record not published yet: nothing to compare')
        return 2
    _, rows = load_codes(manifest)
    published = json.loads(sampling.read_text(encoding='utf-8'))
    drawn = [{k: str(v) for k, v in w.items()} for w in record['works']]
    if rows != drawn or published.get('seed') != record['seed'] or published.get('k') != record['k']:
        print('redraw differs from the published sampling record')
        return 1
    print(f"redraw matches the published sampling record (seed {record['seed']}, k {record['k']})")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--check-codebook', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--draw-sample', action='store_true')
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--check-codes', type=Path)
    parser.add_argument('--kind', choices=['primary', 'second'], default='primary')
    parser.add_argument('--partial', action='store_true')
    args = parser.parse_args(argv)
    codebook = load_codebook()
    _, rows, _, _ = load_corpus(R, M)
    status = 0
    if args.check_codebook:
        errors = check_codebook(codebook, rows, CODEBOOK_MD.read_text(encoding='utf-8'))
        for e in errors:
            print('ERROR', e)
        if errors:
            status = 1
        else:
            values = {name: dict(sorted(Counter(derived_values(r, codebook)[name] for r in rows).items()))
                      for name in ('depth', 'platform_group', 'principal_section')}
            print('codebook OK', json.dumps(values))
    if args.self_test:
        self_test(codebook, technical(rows))
    if args.draw_sample:
        record = draw_sample(technical(rows), codebook)
        if args.check_only:
            status = max(status, check_only(record))
        else:
            print(json.dumps(record, indent=2))
    if args.check_codes:
        header, codes = load_codes(args.check_codes)
        locators_file = locator_path(args.check_codes)
        locators = load_codes(locators_file)[1] if locators_file.is_file() else []
        errors, warnings = validate_codes(codes, rows, codebook, args.kind, args.partial, locators)
        if header != codebook['columns']:
            errors.insert(0, 'header differs from codebook columns')
        if not locators_file.is_file():
            errors.insert(0, f'locator file {locators_file.name} missing')
        for w in warnings:
            print('WARNING', w)
        for e in errors:
            print('ERROR', e)
        print(f'{len(codes)} rows, {len(errors)} errors, {len(warnings)} warnings')
        status = max(status, 1 if errors else 0)
    return status


if __name__ == '__main__':
    sys.exit(main())
