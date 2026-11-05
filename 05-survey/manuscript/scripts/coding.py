"""Evidence coding: codebook checks, stratified sample draw, code validation and agreement statistics.

Run from 05-survey/manuscript:
  python scripts/coding.py --check-codebook
  python scripts/coding.py --self-test
  python scripts/coding.py --draw-sample                 # print the draw record as JSON, write nothing
  python scripts/coding.py --draw-sample --check-only    # redraw and compare with the published sampling record
  python scripts/coding.py --check-codes PATH --kind primary|second [--partial]
  python scripts/coding.py --freeze                      # record SHA-256 of the validated primary files
  python scripts/coding.py --import-second CODES_JSON    # convert the second coder's output into the CSV files
  python scripts/coding.py --agreement                   # pre-resolution agreement into generated/

build_data.py calls write_products() to derive the evidence map, matrices, rankings and sensitivity tables, and
write_agreement() for the agreement of the independent second coding with the frozen primary codes.
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


CARD_LOCATOR = re.compile(r'^card: ([^,]+?)(?:,\s*(.*))?$')


def cited_pages(text):
    """Page numbers named by 'p. N' and 'pp. N-M, K' citations in a text."""
    pages = set()
    for m in re.finditer(r'\bpp?\.\s*(\d[\d,\s\-–]*(?:and\s+\d[\d,\s\-–]*)*)', text):
        for part in re.split(r'[,\s]+|and', m.group(1)):
            bounds = re.fullmatch(r'(\d+)[-–](\d+)', part)
            if bounds:
                pages.update(range(int(bounds.group(1)), int(bounds.group(2)) + 1))
            elif part.isdigit():
                pages.add(int(part))
    return pages


def card_blocks(path):
    """The '## ' blocks of a review card, keyed by block name."""
    text = Path(path).read_text(encoding='utf-8')
    return {m.group(1).strip(): m.group(2)
            for m in re.finditer(r'^##\s+(.+?)\s*$(.*?)(?=^##\s|\Z)', text, flags=re.S | re.M)}


def card_locator_pages(loc):
    """Pages that a card locator names, or None when it is not a card locator."""
    m = CARD_LOCATOR.match(loc['locator']) if loc['source'] == 'card' else None
    return cited_pages(m.group(2) or '') if m else None


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


def validate_codes(codes, corpus_rows, codebook, kind, partial=False, locators=None, final=False):
    """Return (errors, warnings). kind 'second' keeps the second coder's values: rule breaks are warnings.
    final=True checks the final codes (frozen codes with the adjudication log applied) against CR20 as well."""
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
    index, work_locators = {}, {}
    for loc in locators or []:
        index.setdefault((loc['code'], loc['attribute'], loc['value']), []).append(loc)
        work_locators.setdefault(loc['code'], []).append(loc)
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
        if final:
            rules.append(('CR20', len(family) == 1))
        if not context and not resource:
            rules.append(('CR13', bool(S['src_addressed']) or bool(code.get('notes', '').strip())))
        if kind == 'primary':
            mixed = by_code[cid]['platform_class'] == 'mixed'
            rules.append(('CR14', (code['mixed_wheeled'] == 'na') == (not mixed)))
            rules.append(('CR15', (code['transfer_basis'] == 'na') == (code['platform_group'] == 'WHL' or context)))
        for rule_id, ok in rules:
            if not ok:
                soft.append(f'{cid}: rule {rule_id} broken')
        # Locators. A light card's card locator names only pages that the named block cites (Section 15).
        depth = code['depth']
        if depth != 'full':
            blocks = card_blocks(R / by_code[cid]['review'])
            for loc in work_locators.get(cid, []):
                if loc['source'] != 'card':
                    continue
                m = CARD_LOCATOR.match(loc['locator'])
                block = blocks.get(m.group(1).strip()) if m else None
                if block is None:
                    soft.append(f"{cid}: card locator {loc['locator']!r} names no block of the card (CR17)")
                elif not card_locator_pages(loc) <= cited_pages(block):
                    soft.append(f"{cid}: card locator {loc['locator']!r} names a page that the block does not cite (CR17)")
        for name, value in required_locators(code, codebook):
            if kind == 'second' and name not in checked:
                continue
            rows = index.get((cid, name, value), [])
            if not rows:
                soft.append(f'{cid}: no locator for {name}={value} (CR17)')
            elif depth == 'light-legacy' and not any(r['source'] in ('pdf', 'transcription') for r in rows):
                soft.append(f'{cid}: light-legacy value {name}={value} needs a pdf or transcription locator (CR17)')
            elif depth == 'light-targeted' and not any(r['source'] != 'card' or card_locator_pages(r) for r in rows):
                soft.append(f'{cid}: light-targeted value {name}={value} needs a page-located locator (CR17)')
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


LOCATOR_PREFIXES = (('PDF p.', 'pdf'), ('card:', 'card'), ('transcription:', 'transcription'),
                    ('source-reading:', 'source-reading'))
ABSENT_VALUES = {'', 'none', 'na', 'no'}


def locator_source(text):
    """Source type of one locator text, read from its prefix (codebook Section 15 formats)."""
    for prefix, source in LOCATOR_PREFIXES:
        if text.startswith(prefix):
            return source
    raise ValueError(f'locator {text!r} has no known prefix')


def adjudication_locators(log, codebook):
    """Locator rows for values that the adjudication log introduces. The deciding locator of a log row may hold
    several locators separated by '; '; each supports every value of the resolved code."""
    forms = {a['name']: a['form'] for a in codebook['attributes']}
    rows = []
    for entry in log:
        if entry['resolved_value'] == entry['primary_value'] or not entry['locator'].strip():
            continue
        value = entry['resolved_value']
        values = value.split('|') if forms[entry['attribute']] in ('set', 'one-or-two') else [value]
        for text in (t.strip() for t in entry['locator'].split('; ')):
            for v in values:
                if v not in ABSENT_VALUES:
                    rows.append({'code': entry['code'], 'attribute': entry['attribute'], 'value': v,
                                 'source': locator_source(text), 'locator': text, 'note': 'adjudication'})
    return rows


# Agreement units fixed in codebook Section 19. Set-valued attributes are scored as binary flags per value.
SET_ATTRIBUTES = ('functions', 'src_addressed', 'src_manipulated', 'src_selected', 'src_incidental')
SINGLE_ATTRIBUTES = ('nominal_control', 'single_level_injection', 'task_setting', 'deg_task_class',
                     'deg_task_setting', 'level_degradation', 'drivetrain_effect')
FLAGGED_UNITS = ('functions', 'src_addressed', 'named_sources')
AGREEMENT_FIELDS = ['attribute', 'unit', 'kind', 'preregistered', 'works', 'n', 'categories_used', 'agreement_pct',
                    'kappa', 'exact_set_pct', 'primary_prevalence', 'second_prevalence', 'disagreements',
                    'works_in_disagreement', 'resolved_primary', 'resolved_second', 'resolved_both', 'changed_primary']
RESOLUTIONS = {'primary-kept': 'resolved_primary', 'second-adopted': 'resolved_second', 'both-revised': 'resolved_both'}


def agreement_rows(primary, second, log, codebook):
    """Pre-resolution agreement of the frozen primary codes with the second codes on the sampled works."""
    codes = sorted(second)
    fn_of = section_function(codebook)
    functions = function_order(codebook)
    sources = codebook['source_order']
    sample_log = [e for e in log if e['scope'] == 'sample']
    by_attribute = {}
    for e in sample_log:
        by_attribute.setdefault(e['attribute'], []).append(e)
    rows = []

    def prevalence(values, order=None):
        if all(isinstance(v, bool) for v in values):
            return f'{sum(values) / len(values):.3f}' if values else ''
        counts = Counter(values)
        order = order or sorted(counts)
        return ' '.join(f'{v}:{counts[v]}' for v in order if counts[v])

    def add(attribute, unit, kind, preregistered, a, b, works, order=None, exact=None, column=None, differing=None):
        """differing: works whose unit values differ (works_in_disagreement) for rows without a log column."""
        kappa = cohen_kappa(a, b)
        row = {'attribute': attribute, 'unit': unit, 'kind': kind, 'preregistered': 'yes' if preregistered else 'no',
               'works': works, 'n': len(a), 'categories_used': len(set(a) | set(b)),
               'agreement_pct': round(100 * percent_agreement(a, b), 1),
               'kappa': 'n/a' if kappa is None else round(kappa, 3),
               'exact_set_pct': '' if exact is None else round(100 * exact, 1),
               'primary_prevalence': prevalence(a, order), 'second_prevalence': prevalence(b, order),
               'disagreements': sum(x != y for x, y in zip(a, b)),
               'works_in_disagreement': '' if differing is None else differing,
               'resolved_primary': '', 'resolved_second': '', 'resolved_both': '', 'changed_primary': ''}
        if column:
            differing = [c for c in codes if primary[c][column] != second[c][column]]
            entries = by_attribute.get(column, [])
            assert sorted(e['code'] for e in entries) == differing, (column, differing)
            for e in entries:
                assert (e['primary_value'], e['second_value']) == (primary[e['code']][column], second[e['code']][column]), e
            counts = Counter(e['resolution'] for e in entries)
            assert set(counts) <= set(RESOLUTIONS), counts
            row['works_in_disagreement'] = len(differing)
            row.update({field: counts[name] for name, field in RESOLUTIONS.items()})
            row['changed_primary'] = sum(e['resolved_value'] != e['primary_value'] for e in entries)
        rows.append(row)
        return row

    # functions: one flag per function over the works whose principal function differs, pooled, exact set.
    pooled_a, pooled_b = [], []
    flag_rows = []
    for f in functions:
        units = [c for c in codes if fn_of.get(primary[c]['principal_section']) != f]
        a = [f in sset(primary[c], 'functions') for c in units]
        b = [f in sset(second[c], 'functions') for c in units]
        pooled_a += a
        pooled_b += b
        flag_rows.append((f, a, b, len(units)))
    exact = sum(sset(primary[c], 'functions') == sset(second[c], 'functions') for c in codes) / len(codes)
    add('functions', 'non-principal function flags, pooled', 'attribute', False, pooled_a, pooled_b, len(codes),
        exact=exact, column='functions')
    for f, a, b, n in flag_rows:
        add('functions', f'flag {f}', 'flag', True, a, b, n)
    # Source-set attributes: one flag per source, pooled over the nine flags of every work, exact set.
    for name in SET_ATTRIBUTES[1:] + ('named_sources',):
        if name == 'named_sources':
            get_p, get_s = (lambda c: named_of(primary[c])), (lambda c: named_of(second[c]))
        else:
            get_p, get_s = (lambda c, n=name: sset(primary[c], n)), (lambda c, n=name: sset(second[c], n))
        a = [s in get_p(c) for c in codes for s in sources]
        b = [s in get_s(c) for c in codes for s in sources]
        same = sum(get_p(c) == get_s(c) for c in codes)
        derived = name == 'named_sources'
        add(name, 'source flags, pooled', 'derived' if derived else 'attribute', name == 'src_manipulated',
            a, b, len(codes), exact=same / len(codes), column=None if derived else name,
            differing=len(codes) - same if derived else None)
        if name in FLAGGED_UNITS:
            for s in sources:
                add(name, f'flag {s}', 'flag', True, [s in get_p(c) for c in codes], [s in get_s(c) for c in codes],
                    len(codes))
    # Response family: the primary family (pre-registered) and, for information, the full value.
    families = [f['id'] for f in codebook['response_families']]
    a = [primary[c]['response_family'].split('|')[0] for c in codes]
    b = [second[c]['response_family'].split('|')[0] for c in codes]
    add('response_family', 'primary family', 'attribute', True, a, b, len(codes), order=families,
        differing=sum(x != y for x, y in zip(a, b)))
    # The full value carries the log accounting: version 1.0 allowed an optional secondary family.
    add('response_family', 'full value, with the optional secondary family of version 1.0', 'additional', False,
        [primary[c]['response_family'] for c in codes], [second[c]['response_family'] for c in codes], len(codes),
        column='response_family')
    # Publication class (derived from the three class columns) and the single-valued attributes.
    a = [publication_class(primary[c]) for c in codes]
    b = [publication_class(second[c]) for c in codes]
    add('publication_class', 'strongest class', 'derived', True, a, b, len(codes), order=['D1', 'D2', 'D3', 'none'],
        differing=sum(x != y for x, y in zip(a, b)))
    for name in SINGLE_ATTRIBUTES:
        add(name, 'value', 'attribute', True, [primary[c][name] for c in codes], [second[c][name] for c in codes],
            len(codes), order=attribute(codebook, name)['values'], column=name)
    return rows


def import_second(codes_json, corpus_rows, codebook):
    """Convert the second coder's codes.json into second-codes.csv and second-locators.csv.
    Given and derived columns come from the paper index, double-coded values are copied unchanged. A format
    repair (whitespace or letter case) is made only when the intended value is unambiguous; any other value
    outside the codebook is kept as 'invalid:<value>'. Returns the repairs and counts."""
    raw = json.loads(Path(codes_json).read_text(encoding='utf-8'))
    by_code = {r['code']: r for r in corpus_rows}
    double = codebook['double_coding']['attributes']
    repairs, out = [], []
    for work in raw['works']:
        row = {c: '' for c in codebook['columns']}
        row.update(derived_values(by_code[work['code']], codebook))
        for name in double:
            allowed = attribute(codebook, name)['values']
            parts = []
            for part in work[name].split('|'):
                fixed = part.strip()
                if fixed not in allowed:
                    fixed = next((v for v in allowed if v.lower() == fixed.lower()), 'invalid:' + part)
                if fixed != part:
                    repairs.append({'code': work['code'], 'attribute': name, 'received': part, 'stored': fixed})
                parts.append(fixed)
            row[name] = '|'.join(parts)
        row['notes'] = work.get('notes', '')
        out.append(row)
    out.sort(key=lambda r: r['code'])
    fields = codebook['second_coder_output']['locator_fields']
    locators = sorted(({k: loc.get(k, '') for k in fields} for loc in raw['locators']),
                      key=lambda l: [r['code'] for r in out].index(l['code']))
    write_csv(SECOND_CODES, codebook['columns'], out)
    write_csv(SECOND_LOCATORS, fields, locators)
    return {'works': len(out), 'locators': len(locators), 'repairs': repairs,
            'codebook_sha256_stated': raw.get('codebook_sha256'), 'schema_version': raw.get('schema_version')}


def check_second_freeze(record):
    """The published second-coding files still match the hashes recorded in freeze.json."""
    for name, expected in record.get('second', {}).get('files', {}).items():
        actual = sha256_file(CODING / name)
        if actual != expected:
            raise AssertionError(f'{name} changed after the freeze ({actual} != {expected})')


def write_agreement(out_dir):
    """Write coding-agreement.csv and table-agreement.tex; return the 'agreement' summary for stats.json."""
    if not SECOND_CODES.is_file():
        return {}
    codebook = load_codebook()
    record = check_freeze()
    assert record and 'second' in record, 'freeze.json has no second-coding record'
    check_second_freeze(record)
    _, primary_rows = load_codes(PRIMARY_CODES)
    _, second_rows = load_codes(SECOND_CODES)
    _, log = load_codes(ADJUDICATION_LOG)
    primary = {r['code']: r for r in primary_rows}
    second = {r['code']: r for r in second_rows}
    rows = agreement_rows(primary, second, log, codebook)
    write_csv(Path(out_dir) / 'coding-agreement.csv', AGREEMENT_FIELDS, rows)
    (Path(out_dir) / 'table-agreement.tex').write_text(table_agreement(rows), encoding='utf-8')
    sample = [e for e in log if e['scope'] == 'sample']
    recheck = [e for e in log if e['scope'] == 'corpus-recheck']
    return {'agreement': {
        'works': len(second), 'codebook_version': codebook['version'],
        'coders': 'Two language-model sessions on different models; not human inter-rater reliability.',
        'disagreements': len(sample), 'works_with_disagreement': len({e['code'] for e in sample}),
        'resolutions': dict(Counter(e['resolution'] for e in sample)),
        'changed_primary': sum(e['resolved_value'] != e['primary_value'] for e in sample),
        'corpus_recheck_changes': len(recheck),
        'rows': [{k: r[k] for k in ('attribute', 'unit', 'kind', 'n', 'categories_used', 'agreement_pct', 'kappa',
                                    'exact_set_pct', 'works_in_disagreement')} for r in rows]}}


# --------------------------------------------------------------------------- derived products

PRIMARY_CODES = CODING / 'primary-codes.csv'
PRIMARY_LOCATORS = CODING / 'primary-locators.csv'
ADJUDICATION_LOG = CODING / 'adjudication-log.csv'
FREEZE = CODING / 'freeze.json'
SECOND_CODES = CODING / 'second-codes.csv'
SECOND_LOCATORS = CODING / 'second-locators.csv'
HUMAN_TAG = 'human-assistance'


def sha256_file(path):
    import hashlib
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def sset(code, name):
    return set(split_set(code[name]))


def named_of(code):
    return sset(code, 'src_manipulated') | sset(code, 'src_selected')


def any_source(code):
    return sset(code, 'src_addressed') | named_of(code) | sset(code, 'src_incidental')


def headline(code):
    return code['deg_task_class'] in ('D1', 'D2')


def direct_wheeled(code):
    return headline(code) and code['deg_task_setting'] == 'physical' and code['platform_group'] == 'WHL'


def task_outcome(code):
    return code['task_setting'] != 'none'


def publication_class(code):
    for name, label in (('src_manipulated', 'D1'), ('src_selected', 'D2'), ('src_incidental', 'D3')):
        if sset(code, name):
            return label
    return 'none'


def final_codes():
    """Frozen primary codes with every logged adjudication applied, and the log."""
    _, primary = load_codes(PRIMARY_CODES)
    _, log = load_codes(ADJUDICATION_LOG)
    return apply_adjudication(primary, log), log


def write_csv(path, fields, rows):
    with Path(path).open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def ratio(k, n):
    return round(k / n, 4) if n else None


def has_level(*levels):
    return lambda c, r: c['level_degradation'] in levels


EVIDENCE_V2 = [  # key, label, test(code, library index row)
    ('publications', 'Publications', lambda c, r: True),
    ('component', 'Component measures (card field)', lambda c, r: 'residual' in r['evaluation_all']),
    ('task_any', 'Task outcome reported', lambda c, r: task_outcome(c)),
    ('task_sim_only', 'Task outcome in simulation only', lambda c, r: c['task_setting'] == 'simulation'),
    ('task_physical', 'Physical task outcome', lambda c, r: c['task_setting'] in ('physical', 'both')),
    ('addressed', 'Degradation source addressed', lambda c, r: bool(sset(c, 'src_addressed'))),
    ('named', 'Named condition (D1 or D2)', lambda c, r: bool(named_of(c))),
    ('manipulated', 'Injected or varied with a comparator (D1)', lambda c, r: bool(sset(c, 'src_manipulated'))),
    ('selected_only', 'Selected condition only (D2)', lambda c, r: bool(sset(c, 'src_selected')) and not sset(c, 'src_manipulated')),
    ('incidental_only', 'Incidental condition only (D3)', lambda c, r: bool(sset(c, 'src_incidental')) and not named_of(c)),
    ('task_named_same', 'Named condition with a task outcome in the same experiment', lambda c, r: headline(c)),
    ('task_manipulated_same', 'D1 condition with a task outcome in the same experiment', lambda c, r: c['deg_task_class'] == 'D1'),
    ('physical_task_named_same', 'Same-experiment combination on a physical robot', lambda c, r: headline(c) and c['deg_task_setting'] == 'physical'),
    ('direct_wheeled_joint', 'Direct joint wheeled evidence', lambda c, r: direct_wheeled(c)),
    ('level_physical', 'Named condition, physical closed loop', has_level('P')),
    ('level_hw_recorded', 'Named condition, online hardware or recorded data', has_level('O', 'R')),
    ('level_replay_sim_num', 'Named condition, replay, simulation, numerical model or resource', has_level('D', 'S', 'N', 'X')),
    ('integrity', 'Integrity or failure-risk assessment', lambda c, r: c['integrity'] == 'yes'),
    ('placement', 'Computation placement reported', lambda c, r: c['placement_reported'] == 'yes'),
    ('group_WHL', 'Target wheeled robot', lambda c, r: c['platform_group'] == 'WHL'),
    ('group_ROAD', 'Road vehicle', lambda c, r: c['platform_group'] == 'ROAD'),
    ('group_GND', 'Other ground robot', lambda c, r: c['platform_group'] == 'GND'),
    ('group_OTH', 'Non-ground, handheld, mixed-carrier or no platform', lambda c, r: c['platform_group'] == 'OTH'),
    ('drivetrain_effect', 'Drivetrain-dependent effect reported', lambda c, r: c['drivetrain_effect'] == 'yes'),
]


def by_function(codes, codebook):
    fn_of = section_function(codebook)
    return {f: [c for c in codes if fn_of.get(c['principal_section']) == f] for f in function_order(codebook)}


def evidence_map_v2(codes, index, codebook):
    groups = by_function(codes, codebook)
    result = {f: {key: sum(bool(test(c, index[c['code']])) for c in group) for key, _, test in EVIDENCE_V2}
              for f, group in groups.items()}
    result['All'] = {key: sum(result[f][key] for f in groups) for key, _, _ in EVIDENCE_V2}
    return result


def strongest_level(codes, codebook):
    levels = [c['level_degradation'] for c in codes if c['level_degradation'] != 'none']
    return max(levels, key=lambda l: level_rank(l, codebook)) if levels else 'none'


def shade_of(level, codebook):
    return 0 if level == 'none' else next(l['shade'] for l in codebook['evidence_levels'] if l['id'] == level)


def primary_family(code):
    return code['response_family'].split('|')[0]


def joined(items):
    return '|'.join(items) or 'none'


def source_function_matrix(codes, codebook):
    """One cell per source and principal section (codebook 'matrix')."""
    fn = section_function(codebook)
    cells = []
    for s in codebook['source_order']:
        for sec in [f['section'] for f in codebook['functions']]:
            col = [c for c in codes if c['principal_section'] == sec]
            addressed = [c for c in col if s in sset(c, 'src_addressed')]
            named = [c for c in col if s in named_of(c)]
            groups = Counter(c['platform_group'] for c in addressed)
            level = strongest_level(named, codebook)
            families = Counter(primary_family(c) for c in addressed)
            cells.append({
                'source': s, 'section': sec, 'function': fn[sec],
                'addressed': len(addressed), 'named': len(named),
                'manipulated': sum(s in sset(c, 'src_manipulated') for c in col),
                'selected': sum(s in sset(c, 'src_selected') for c in col),
                'incidental': sum(s in sset(c, 'src_incidental') for c in col),
                'wheeled_addressed': groups['WHL'], 'road': groups['ROAD'],
                'other_ground': groups['GND'], 'non_ground': groups['OTH'],
                'wheeled_named': sum(c['platform_group'] == 'WHL' for c in named),
                'strongest_level': level, 'shade': shade_of(level, codebook),
                'response_families': joined(f'{k}:{v}' for k, v in sorted(families.items())),
                'codes': joined(c['code'] for c in addressed),
                'named_codes': joined(c['code'] for c in named),
            })
    return cells


def assumption_links(codes, codebook):
    """Assumption -> source -> primary response family of the works that address the source."""
    links = []
    for a in codebook['assumptions']:
        for s in a['sources']:
            works = [c for c in codes if s in sset(c, 'src_addressed')]
            families = Counter(primary_family(c) for c in works)
            for family, count in sorted(families.items(), key=lambda kv: (-kv[1], kv[0])):
                links.append({'assumption': a['id'], 'source': s, 'response_family': family, 'works': count,
                              'pre_registered': 'yes' if family in a['response_families'] else 'no',
                              'codes': joined(c['code'] for c in works if primary_family(c) == family)})
    return links


def pair_list(codebook):
    fl = function_order(codebook)
    return [(fl[i], fl[j]) for i in range(len(fl)) for j in range(i + 1, len(fl))]


def cooccurrence(codes, codebook):
    rows = []
    for a, b in pair_list(codebook):
        works = [c for c in codes if {a, b} <= sset(c, 'functions')]
        rows.append({'function_a': a, 'function_b': b, 'works': len(works),
                     'joint_named_same': sum(headline(c) for c in works),
                     'joint_manipulated_same': sum(c['deg_task_class'] == 'D1' for c in works),
                     'joint_physical_named': sum(headline(c) and c['deg_task_setting'] == 'physical' for c in works),
                     'direct_wheeled_joint': sum(direct_wheeled(c) for c in works),
                     'wheeled_works': sum(c['platform_group'] == 'WHL' for c in works),
                     'strongest_level': strongest_level(works, codebook),
                     'codes': joined(c['code'] for c in works)})
    return rows


def cell_owners(codebook):
    """Candidate id -> interfaces and named alternatives whose pre-registered cells contain it."""
    owners = {}
    ranking = codebook['interface_ranking']
    entries = [(itf['cells'], 'interfaces', itf['id']) for itf in ranking['interfaces']]
    entries += [(alt, 'alternatives', alt['name']) for alt in ranking['named_alternatives']]
    for cells, kind, name in entries:
        for a, b in cells['pairs']:
            for s in cells['sources']:
                owners.setdefault(f'{a}-{b}:{s}', {'interfaces': [], 'alternatives': []})[kind].append(name)
    return owners


def rank_candidates(codes, codebook, key='gap'):
    """All function-pair x source candidates; eligible ones carry a rank (codebook 'interface_ranking')."""
    cands = []
    for a, b in pair_list(codebook):
        for s in codebook['source_order']:
            works = [c for c in codes if {a, b} <= sset(c, 'functions') and s in any_source(c)]
            n, j = len(works), sum(direct_wheeled(c) for c in works)
            cands.append({'candidate_id': f'{a}-{b}:{s}', 'function_a': a, 'function_b': b, 'source': s,
                          'works': n, 'direct_wheeled_joint': j,
                          'wheeled_works': sum(c['platform_group'] == 'WHL' for c in works),
                          'safety_relevant': 'yes' if {'PLN', 'REL'} & {a, b} else 'no',
                          'gap': n - j, 'gap_share': round(1 - j / n, 4) if n else None,
                          'eligible': n >= 3, 'rank': None, 'codes': [c['code'] for c in works]})
    eligible = [c for c in cands if c['eligible']]
    eligible.sort(key=lambda c: (-c[key], c['safety_relevant'] != 'yes', -c['wheeled_works'], c['candidate_id']))
    for i, c in enumerate(eligible):
        c['rank'] = i + 1
    return cands


def best_rank(cands, ids):
    ranks = [c['rank'] for c in cands if c['candidate_id'] in ids and c['rank']]
    return min(ranks) if ranks else None


def interface_ranking(codes, codebook):
    ranking = codebook['interface_ranking']
    owners = cell_owners(codebook)
    main = rank_candidates(codes, codebook)
    integration = codebook['stage_groups']['integration_stage']
    without = rank_candidates([c for c in codes if c['stage'] != integration], codebook)
    share = rank_candidates(codes, codebook, key='gap_share')
    lookup = lambda cands: {c['candidate_id']: c['rank'] for c in cands}
    without_rank, share_rank = lookup(without), lookup(share)
    interfaces = []
    for itf in ranking['interfaces']:
        ids = [c['candidate_id'] for c in main if itf['id'] in owners.get(c['candidate_id'], {}).get('interfaces', [])]
        interfaces.append({'id': itf['id'], 'name': itf['name'], 'cells': ids,
                           'eligible_cells': [c['candidate_id'] for c in main if c['candidate_id'] in ids and c['eligible']],
                           'rank': best_rank(main, ids), 'rank_without_integration_stage': best_rank(without, ids),
                           'rank_by_gap_share': best_rank(share, ids)})
    ranks = [i['rank'] for i in interfaces if i['rank']]
    lowest = max(ranks) if ranks else None
    pairs = {}
    for itf in ranking['interfaces']:
        for a, b in itf['cells']['pairs']:
            pairs.setdefault(f'{a}-{b}', []).append(str(itf['id']))
    for c in main:
        own = owners.get(c['candidate_id'], {'interfaces': [], 'alternatives': []})
        c['rank_without_integration_stage'] = without_rank[c['candidate_id']]
        c['rank_by_gap_share'] = share_rank[c['candidate_id']]
        c['interface'] = joined(str(i) for i in own['interfaces'])
        c['named_alternative'] = joined(own['alternatives'])
        if own['interfaces']:
            c['status'] = 'interface'
        elif not c['eligible']:
            c['status'] = 'ineligible'
        else:
            c['status'] = 'rejected' if lowest and c['rank'] < lowest else 'below'
        note = [f"{c['works']} works, {c['direct_wheeled_joint']} with direct joint wheeled evidence, {c['wheeled_works']} target wheeled"]
        pair = f"{c['function_a']}-{c['function_b']}"
        if pair in pairs and not own['interfaces']:
            note.append(f"function pair of Interface {' and '.join(pairs[pair])} with a source outside its pre-registered cells")
        if c['works'] and not c['wheeled_works']:
            note.append('no target wheeled work')
        if own['alternatives']:
            note.append('named alternative: ' + '; '.join(own['alternatives']))
        c['screen_note'] = '; '.join(note)
    human = [c['code'] for c in codes if HUMAN_TAG in c['notes']]
    alternatives = [{'name': alt['name'], 'cells': [f'{a}-{b}:{s}' for a, b in alt['pairs'] for s in alt['sources']],
                     'rank': best_rank(main, [f'{a}-{b}:{s}' for a, b in alt['pairs'] for s in alt['sources']]),
                     'works': len(human) if not alt['pairs'] else None} for alt in ranking['named_alternatives']]
    ordered = sorted((c for c in main if c['eligible']), key=lambda c: c['rank'])
    return {'candidates': main, 'interfaces': interfaces, 'lowest_interface_rank': lowest,
            'eligible_count': len(ordered), 'top': [c['candidate_id'] for c in ordered[:10]],
            'alternatives': alternatives, 'human_assistance_codes': human,
            'interfaces_are_top4': sorted(ranks) == [1, 2, 3, 4]}


def interface_traceability(codes, ranking):
    order = {c['code']: i for i, c in enumerate(codes)}
    by_code = {c['code']: c for c in codes}
    rows = []
    for itf in ranking['interfaces']:
        members = {}
        for cand in ranking['candidates']:
            if cand['candidate_id'] in itf['cells']:
                for code in cand['codes']:
                    members.setdefault(code, []).append(cand['candidate_id'])
        for code in sorted(members, key=order.get):
            c = by_code[code]
            rows.append({'interface': itf['id'], 'code': code, 'key': 'P_' + code, 'stage': c['stage'],
                         'principal_section': c['principal_section'], 'platform_group': c['platform_group'],
                         'level_degradation': c['level_degradation'], 'deg_task_class': c['deg_task_class'],
                         'deg_task_setting': c['deg_task_setting'],
                         'direct_wheeled': 'yes' if direct_wheeled(c) else 'no',
                         'candidate_id': '|'.join(sorted(members[code]))})
    return rows


def finding_checks(shares, counts, task_shares, functions):
    """Robustness findings RF1-RF4 (codebook 'findings') for one subset."""
    def extreme(target, better):
        if any(counts[f] < 3 for f in functions):
            return 'n/a'
        others = [shares[f] for f in functions if f != target]
        if not all(better(shares[target], v) or shares[target] == v for v in others):
            return 'fails'
        return 'holds (tie)' if shares[target] in others else 'holds'
    rf3 = 'n/a' if min(counts['PLN'], counts['SEM']) < 3 else (
        'holds' if min(task_shares['PLN'], task_shares['SEM']) >= 0.9 else 'fails')
    rf4 = 'n/a' if counts['LOC'] < 3 else ('holds' if task_shares['LOC'] <= 0.05 else 'fails')
    return {'RF1': extreme('LOC', lambda x, y: x < y), 'RF2': extreme('REL', lambda x, y: x > y), 'RF3': rf3, 'RF4': rf4}


def sensitivity_row(row_id, kind, label, subset, measure, codebook):
    functions = function_order(codebook)
    fn_of = section_function(codebook)
    counts = {f: sum(fn_of[c['principal_section']] == f for c in subset) for f in functions}
    hits = {f: sum(bool(measure(c)) for c in subset if fn_of[c['principal_section']] == f) for f in functions}
    tasks = {f: sum(task_outcome(c) for c in subset if fn_of[c['principal_section']] == f) for f in functions}
    shares = {f: hits[f] / counts[f] if counts[f] else 0.0 for f in functions}
    task_shares = {f: tasks[f] / counts[f] if counts[f] else 0.0 for f in functions}
    k = sum(hits.values())
    row = {'row_id': row_id, 'analysis': kind, 'subset': label,
           'definition': row_id if kind in ('definition', 'coding-unit') else 'S-def-headline',
           'numerator': k, 'denominator': len(subset), 'share': ratio(k, len(subset))}
    for f in functions:
        row.update({f: ratio(hits[f], counts[f]), f + '_k': hits[f], f + '_n': counts[f]})
    row.update(finding_checks(shares, counts, task_shares, functions))
    return row


def card_round3(index):
    return lambda c: {'designed-degradation', 'closed-loop-task'} <= {
        x.strip() for x in index[c['code']]['evaluation_all'].split(',')}


def sensitivity(codes, index, codebook):
    """Rows of codebook 'sensitivity' with robustness findings; codes are the technical works."""
    groups = codebook['stage_groups']
    spec = {s['id']: s for s in codebook['sensitivity']}
    definitions = [
        ('S-def-headline', headline),
        ('S-def-D1', lambda c: c['deg_task_class'] == 'D1'),
        ('S-def-D1-nominal', lambda c: c['deg_task_class'] == 'D1' and c['nominal_control'] == 'yes'),
        ('S-def-physical', lambda c: headline(c) and c['deg_task_setting'] == 'physical'),
        ('S-def-with-incidental', lambda c: headline(c) or (bool(sset(c, 'src_incidental')) and task_outcome(c))),
        ('S-unit-any', lambda c: bool(named_of(c)) and task_outcome(c)),
        ('S-card-round3', card_round3(index)),
    ]
    year = lambda c: int(index[c['code']]['bibliographic_year'])
    quota = lambda c: c['stage'] in groups['quota_stages']
    subsets = [(i, 'S-' + i[2:], t) for i, t in (
        ('S-depth-full', lambda c: c['depth'] == 'full'),
        ('S-depth-light-legacy', lambda c: c['depth'] == 'light-legacy'),
        ('S-depth-light-targeted', lambda c: c['depth'] == 'light-targeted'),
        ('S-depth-no-legacy', lambda c: c['depth'] in ('full', 'light-targeted')))]
    subsets += [(f'S-stage-out-{s}', 'S-stage-out-<stage>', (lambda s: lambda c: c['stage'] != s)(s))
                for s in codebook['stage_order']]
    subsets += [(f"S-year-{b['id']}", 'S-year-<band>', (lambda ys: lambda c: year(c) in ys)(set(b['years'])))
                for b in codebook['year_bands']]
    subsets += [('S-quota', 'S-quota', quota), ('S-non-quota', 'S-non-quota', lambda c: not quota(c))]
    subsets += [(f'S-quota-theme-{t}', 'S-quota-theme-<T>',
                 (lambda t: lambda c: quota(c) and index[c['code']]['theme'] == t)(t)) for t in
                ('T1', 'T2', 'T3', 'T4', 'T5', 'T6')]
    subsets += [('S-no-ieee-only', 'S-no-ieee-only', lambda c: c['stage'] not in groups['ieee_only_stages']),
                ('S-no-coverage', 'S-no-coverage', lambda c: c['stage'] != groups['coverage_stage']),
                ('S-platform-WHL', 'S-platform-WHL', lambda c: c['platform_group'] == 'WHL'),
                ('S-platform-WHL-mixed', 'S-platform-WHL-mixed',
                 lambda c: c['platform_group'] == 'WHL' or c['mixed_wheeled'] == 'yes'),
                ('S-platform-non-WHL', 'S-platform-non-WHL', lambda c: c['platform_group'] != 'WHL')]
    rows = [sensitivity_row(i, spec[i]['kind'], 'all technical works', codes, m, codebook) for i, m in definitions]
    for r in rows[1:]:
        r['RF3'], r['RF4'] = rows[0]['RF3'], rows[0]['RF4']
    for row_id, spec_id, test in subsets:
        s = spec[spec_id]
        label = s['subset'] if '<' not in spec_id else row_id[len(spec_id.split('<')[0]):]
        rows.append(sensitivity_row(row_id, s['kind'], label, [c for c in codes if test(c)], headline, codebook))
    return rows


PUBLISHER_COLUMNS = ['IEEE', 'Elsevier', 'Wiley', 'SAGE', 'Springer', 'AAAS', 'RSS', 'PMLR', 'NeurIPS']


def venue_mix(index, codes, codebook):
    out = []
    for stage in codebook['stage_order'] + ['all']:
        works = [index[c['code']] for c in codes if stage == 'all' or c['stage'] == stage]
        pub = Counter(publisher_of(r, codebook) for r in works)
        venues = Counter(r['venue'] for r in works)
        row = {'stage': stage, 'stage_label': codebook['stage_labels'].get(stage, 'All stages'), 'works': len(works),
               'journal': sum(r['publication_type'] == 'journal' for r in works),
               'conference': sum(r['publication_type'] == 'conference' for r in works)}
        row.update({p: pub.get(p, 0) for p in PUBLISHER_COLUMNS})
        row['other'] = sum(v for k, v in pub.items() if k not in PUBLISHER_COLUMNS)
        row['other_publishers'] = joined(f'{k}:{v}' for k, v in sorted(pub.items()) if k not in PUBLISHER_COLUMNS)
        row['IEEE_share'] = ratio(pub.get('IEEE', 0), len(works))
        row['venues'] = '|'.join(f'{k} ({v})' for k, v in sorted(venues.items(), key=lambda kv: (-kv[1], kv[0])))
        out.append(row)
    return out


def group_counts(works, codebook):
    fn_of = section_function(codebook)
    return {f: sum(fn_of.get(c['principal_section']) == f for c in works) for f in function_order(codebook)}


def drivetrain_groups(codes, codebook):
    out = []
    for d in list(dict.fromkeys(codebook['drivetrain_map'].values())) + ['na']:
        works = [c for c in codes if c['drivetrain'] == d]
        effect = [c['code'] for c in works if c['drivetrain_effect'] == 'yes']
        sources = Counter(s for c in works for s in sset(c, 'src_addressed'))
        out.append({'drivetrain': d, 'works': len(works), **group_counts(works, codebook),
                    'named': sum(bool(named_of(c)) for c in works), 'task_named_same': sum(headline(c) for c in works),
                    'direct_wheeled_joint': sum(direct_wheeled(c) for c in works),
                    'drivetrain_effect': len(effect), 'effect_codes': joined(effect),
                    'sources_addressed': joined(f'{k}:{v}' for k, v in sorted(sources.items()))})
    return out


def platform_groups(codes, index, codebook):
    out = []
    for g in codebook['platform_groups']:
        works = [c for c in codes if c['platform_group'] == g['id']]
        classes = Counter(index[c['code']]['platform_class'] for c in works)
        out.append({'group': g['id'], 'name': g['name'], 'mark': g['mark'] or 'none',
                    'platform_classes': joined(f'{k}:{v}' for k, v in sorted(classes.items())),
                    'works': len(works), **group_counts(works, codebook),
                    'task_any': sum(task_outcome(c) for c in works), 'named': sum(bool(named_of(c)) for c in works),
                    'task_named_same': sum(headline(c) for c in works),
                    'physical_task_named_same': sum(headline(c) and c['deg_task_setting'] == 'physical' for c in works),
                    'transfer_mechanism': sum(c['transfer_basis'] == 'mechanism' for c in works),
                    'transfer_counterexample': sum(c['transfer_basis'] == 'counterexample' for c in works),
                    'mixed_wheeled': sum(c['mixed_wheeled'] == 'yes' for c in works)})
    return out


def tex_escape(s):
    return ''.join({'&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
                    '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}.get(ch, ch) for ch in str(s))


def pct_text(value):
    return '--' if value is None else str(round(100 * value))


def table(label, caption, spec, header, body, note=None, star=True, colsep='3.4pt'):
    env = 'table*' if star else 'table'
    lines = [r'\begin{' + env + '}[!t]', r'\centering', r'\caption{' + caption + '}', r'\label{' + label + '}',
             r'\surveytableformat', r'\setlength{\tabcolsep}{' + colsep + '}',
             r'\begin{tabularx}{\linewidth}{' + spec + '}', r'\toprule', header + r' \\', r'\midrule']
    lines += body + [r'\bottomrule', r'\end{tabularx}']
    if note:
        lines.append(r'\par\vspace{3pt}\parbox{\linewidth}{\footnotesize\raggedright ' + note + '}')
    return '\n'.join(lines + [r'\end{' + env + '}']) + '\n'


def bold_row(cells):
    return ' & '.join(r'\textbf{' + c + '}' for c in cells)


def table_venue_mix(rows):
    body = []
    for r in rows:
        if r['stage'] == 'all':
            body.append(r'\midrule')
        other = r['other'] + r['AAAS'] + r['RSS'] + r['NeurIPS']
        cells = [tex_escape(r['stage_label']), r['works'], r['journal'], r['conference'], r['IEEE'], r['Elsevier'],
                 r['Wiley'], r['SAGE'], r['Springer'], r['PMLR'], other, pct_text(r['IEEE_share'])]
        body.append(' & '.join(str(c) for c in cells) + r' \\')
    header = bold_row(['Stage', 'Works', 'Journal', 'Conf.', 'IEEE', 'Elsevier', 'Wiley', 'SAGE', 'Springer', 'PMLR',
                       'Other', r'IEEE \%'])
    return table('tab:venue-mix', 'Venue type and publisher of the selected works by selection stage. The publisher '
                 'follows the DOI prefix, or the official URL host for works without a DOI.',
                 '@{}Yrrrrrrrrrrr@{}', header, body,
                 'Other: AAAS, Robotics: Science and Systems, NeurIPS Datasets and Benchmarks, Field Robotics and '
                 'Tsinghua University Press. The context review is included in its stage.')


def table_evidence_percent(emap, codebook):
    functions = function_order(codebook)
    sections = {f['id']: f['section'] for f in codebook['functions']}
    body = []
    for key, label, _ in EVIDENCE_V2:
        if key == 'component':
            continue
        cells = [str(emap[f][key]) if key == 'publications' else
                 f"{emap[f][key]} ({round(100 * emap[f][key] / emap[f]['publications'])}\\%)" for f in functions + ['All']]
        body.append(tex_escape(label) + ' & ' + ' & '.join(cells) + r' \\')
    header = bold_row(['Attribute'] + [sections[f] for f in functions] + ['All'])
    return table('tab:evidence-percent', 'Evidence attributes of the technical works by principal section. Each '
                 'percentage refers to the works of its column. Attributes overlap.',
                 '@{}Yrrrrrr@{}', header, body)


def cite_list(codes):
    return r'\cite{' + ','.join('P_' + c for c in codes) + '}' if codes else '--'


def table_matrix_works(cells, codebook):
    sections = [f['section'] for f in codebook['functions']]
    names = {s['id']: s['name'] for s in codebook['sources']}
    by = {(c['source'], c['section']): c for c in cells}
    body = []
    for a in codebook['assumptions']:
        for s in a['sources']:
            row = [f"{tex_escape(names[s])} ({a['id']})"]
            row += [cite_list(split_set(by[(s, sec)]['codes'])) for sec in sections]
            body.append(' & '.join(row) + r' \\')
    header = bold_row(['Source (assumption)'] + sections)
    return table('tab:matrix-works', 'Works that address each degradation source, by principal section. A work '
                 'appears in the row of every source it addresses and always in the column of its principal section.',
                 '@{}L{2.3cm}YYYYY@{}', header, body, colsep='3pt')


FINDING_MARK = {'holds': 'yes', 'holds (tie)': 'tie', 'fails': 'no', 'n/a': 'n/a'}


def table_sensitivity(rows, codebook):
    functions = function_order(codebook)
    sections = {f['id']: f['section'] for f in codebook['functions']}
    labels = codebook['stage_labels']
    body = []
    for r in rows:
        name = r['row_id']
        if name.startswith('S-stage-out-'):
            name = 'Without ' + labels[name[len('S-stage-out-'):]]
        cells = [tex_escape(name), f"{r['numerator']}/{r['denominator']}", pct_text(r['share'])]
        cells += [pct_text(r[f]) for f in functions] + [FINDING_MARK[r[k]] for k in ('RF1', 'RF2', 'RF3', 'RF4')]
        body.append(' & '.join(cells) + r' \\')
    header = bold_row(['Row', 'Works', r'\%'] + [sections[f] + r' \%' for f in functions] + ['RF1', 'RF2', 'RF3', 'RF4'])
    return table('tab:sensitivity', 'Sensitivity of the share of technical works that report a named degradation '
                 'condition and a task outcome in the same experiment. Rows vary the definition, the coding unit or '
                 'the subset. RF1-RF4 state whether each pre-registered finding holds.',
                 '@{}Yrrrrrrrcccc@{}', header, body,
                 'Definition rows change the measure and use all technical works. Other rows apply the headline '
                 'measure to a subset. A finding is n/a when a function it compares has fewer than three works in '
                 'the subset. All shares describe the purposively selected sample.', colsep='2.6pt')


def table_cooccurrence(rows):
    body = [' & '.join(str(x) for x in [f"{r['function_a']}--{r['function_b']}", r['works'], r['joint_named_same'],
                                         r['joint_manipulated_same'], r['joint_physical_named'],
                                         r['direct_wheeled_joint'], r['wheeled_works'], r['strongest_level']]) + r' \\'
            for r in rows]
    header = bold_row(['Pair', 'Works', 'Named', 'D1', 'Physical', 'Wheeled joint', 'Wheeled', 'Level'])
    return table('tab:cooccurrence', 'Function-pair co-occurrence with evidence levels. Named, D1 and Physical '
                 'count works with a same-experiment combination of a named condition and a task outcome, a D1 '
                 'condition, or a physical robot. Wheeled joint counts such physical combinations on target wheeled '
                 'robots.', '@{}Yrrrrrrc@{}', header, body, star=False)


def table_candidates(ranking, reasons=None):
    """Eligible candidates ranked at or above the lowest developed interface, plus every interface cell."""
    reasons = reasons or {}
    lowest = ranking['lowest_interface_rank'] or 0
    shown = [c for c in ranking['candidates'] if (c['rank'] and c['rank'] <= lowest) or c['status'] == 'interface']
    shown.sort(key=lambda c: (c['rank'] is None, c['rank'] or 0, c['candidate_id']))
    body = []
    for c in shown:
        status = f"Interface {c['interface']}" if c['status'] == 'interface' else c['status']
        cells = [str(c['rank'] or '--'), tex_escape(c['candidate_id']), str(c['works']), str(c['direct_wheeled_joint']),
                 str(c['wheeled_works']), str(c['gap']), str(c['rank_without_integration_stage'] or '--'),
                 str(c['rank_by_gap_share'] or '--'), status, tex_escape(reasons.get(c['candidate_id'], ''))]
        body.append(' & '.join(cells) + r' \\')
    header = bold_row(['Rank', 'Candidate', 'n', 'j', 'w', 'Gap', 'Rank A', 'Rank B', 'Status', 'Reason'])
    return table('tab:candidates', 'Interface candidates ranked by the pre-registered rule. A candidate is a '
                 'function pair with one coupling source. n counts its works, j the works with direct joint wheeled '
                 'evidence and w the target wheeled works. Rank A drops the integration-questions stage and Rank B '
                 'sorts by gap share.', '@{}rL{1.9cm}rrrrrrL{1.5cm}Y@{}', header, body, colsep='3pt')


AGREEMENT_LABELS = {'functions': 'Functions', 'src_addressed': 'Addressed sources', 'response_family': 'Response family',
                    'src_manipulated': 'Manipulated sources (D1)', 'src_selected': 'Selected sources (D2)',
                    'src_incidental': 'Incidental sources (D3)', 'named_sources': 'Named sources (D1 or D2)',
                    'publication_class': 'Publication class', 'nominal_control': 'Nominal control',
                    'single_level_injection': 'Single-level injection', 'task_setting': 'Task setting',
                    'deg_task_class': 'Same-experiment class', 'deg_task_setting': 'Same-experiment setting',
                    'level_degradation': 'Degradation evidence level', 'drivetrain_effect': 'Drivetrain effect'}


def table_agreement(rows):
    """Supplement table: one row per double-coded attribute and derived unit, before adjudication."""
    flag_kappas = {}
    for r in rows:
        if r['kind'] == 'flag' and r['kappa'] != 'n/a':
            flag_kappas.setdefault(r['attribute'], []).append(r['kappa'])
    body = []
    for r in rows:
        if r['kind'] == 'flag':
            continue
        kappas = flag_kappas.get(r['attribute'])
        flag_range = f'{min(kappas):.2f}--{max(kappas):.2f}' if kappas else '--'
        kappa = r['kappa'] if r['kappa'] == 'n/a' else f"{r['kappa']:.2f}".replace('-', '$-$')
        resolved = ('/'.join(str(r[k]) for k in ('resolved_primary', 'resolved_second', 'resolved_both'))
                    if r['resolved_primary'] != '' else '--')
        cells = [AGREEMENT_LABELS[r['attribute']], tex_escape(r['unit']), str(r['n']), str(r['categories_used']),
                 f"{r['agreement_pct']:.1f}", kappa, '--' if r['exact_set_pct'] == '' else f"{r['exact_set_pct']:.1f}",
                 flag_range, '--' if r['works_in_disagreement'] == '' else str(r['works_in_disagreement']), resolved]
        body.append(' & '.join(cells) + r' \\')
    header = bold_row(['Attribute', 'Unit', 'n', 'Cat.', r'Agr. \%', r'$\kappa$', r'Exact \%', r'Flag $\kappa$',
                       'Works', 'P/S/B'])
    return table('tab:agreement', 'Agreement between the independent second coding and the frozen primary codes '
                 'on the 40 sampled works, before adjudication. Both coders are language-model sessions on '
                 'different models, so the values describe how consistently two such coders apply the codebook to '
                 'shared evidence. They are not human inter-rater reliability.',
                 '@{}L{2.9cm}Yrrrrrrrr@{}', header, body,
                 r'n counts the scored units and Cat. the categories that either coder used. $\kappa$ is unweighted '
                 r"Cohen's kappa (n/a when both coders use one category). Set-valued attributes are scored as one "
                 r'binary flag per value: $\kappa$ and Agr. pool all flag decisions of the attribute (for functions '
                 r'the four non-principal functions of each work), Exact gives the share of works with identical '
                 r'sets, and Flag $\kappa$ the range of the per-flag kappas (functions over the 32 works whose '
                 r'principal function differs, sources over all 40 works). The pre-registered unit of response '
                 r'family is the primary family; the second row compares the full value, which in codebook version '
                 r'1.0 could add an optional secondary family. Named sources and publication class are derived from '
                 r'the three class columns. Works counts the works with differing values and P/S/B how the logged '
                 r'disagreements were resolved: primary kept, second adopted, both revised.', colsep='3pt')


PRODUCT_FILES = ['evidence-codes.csv', 'evidence-map.csv', 'degradation-function-matrix.csv',
                 'degradation-function-matrix.json', 'assumption-links.csv', 'function-pair-cooccurrence.csv',
                 'interface-candidates.csv', 'interface-traceability.csv', 'sensitivity.csv', 'venue-mix-by-stage.csv',
                 'drivetrain-evidence.csv', 'platform-groups.csv', 'table-venue-mix.tex', 'table-evidence-percent.tex',
                 'table-matrix-works.tex', 'table-sensitivity.tex', 'table-cooccurrence.tex', 'table-candidates.tex']


def evidence_code_rows(codes, index, codebook):
    rows = []
    for c in codes:
        r = index[c['code']]
        rows.append({**{k: c[k] for k in codebook['columns'] if k != 'notes'},
                     'key': 'P_' + c['code'], 'stage_label': codebook['stage_labels'][c['stage']],
                     'theme': r['theme'], 'year': r['bibliographic_year'], 'publisher': publisher_of(r, codebook),
                     'named_sources': joined(sorted(named_of(c), key=codebook['source_order'].index)),
                     'publication_class': publication_class(c), 'headline': 'yes' if headline(c) else 'no',
                     'direct_wheeled_joint': 'yes' if direct_wheeled(c) else 'no', 'notes': c['notes']})
    return rows


def check_freeze():
    """Frozen hashes of the primary files; raises when the primary files changed after the freeze."""
    if not FREEZE.is_file():
        return None
    record = json.loads(FREEZE.read_text(encoding='utf-8'))
    for name, expected in record['primary'].items():
        actual = sha256_file(CODING / name)
        if actual != expected:
            raise AssertionError(f'{name} changed after the freeze ({actual} != {expected})')
    return record


def strip_codes(rows, drop=('codes',)):
    return [{k: v for k, v in r.items() if k not in drop} for r in rows]


def write_products(out_dir, rows, decisions_path=None):
    """Write the derived coding products into out_dir; return summaries for stats.json."""
    out_dir = Path(out_dir)
    codebook = load_codebook()
    index = {r['code']: r for r in rows}
    codes, log = final_codes()
    locators = load_codes(PRIMARY_LOCATORS)[1] + adjudication_locators(log, codebook)
    errors, _ = validate_codes(codes, rows, codebook, 'primary', locators=locators, final=True)
    assert not errors, errors[:5]
    freeze = check_freeze()
    technical = [c for c in codes if c['principal_section'] != 'context']
    emap = evidence_map_v2(technical, index, codebook)
    cells = source_function_matrix(technical, codebook)
    links = assumption_links(technical, codebook)
    pairs = cooccurrence(technical, codebook)
    ranking = interface_ranking(technical, codebook)
    trace = interface_traceability(technical, ranking)
    sens = sensitivity(technical, index, codebook)
    venues = venue_mix(index, codes, codebook)
    drive = drivetrain_groups(technical, codebook)
    groups = platform_groups(technical, index, codebook)
    reasons = {}
    if decisions_path and Path(decisions_path).is_file():
        reasons = {d['candidate_id']: d['reason'] for d in json.loads(Path(decisions_path).read_text(encoding='utf-8'))['decisions']}
    for c in ranking['candidates']:
        c['reason'] = reasons.get(c['candidate_id'], '')
    ev_rows = evidence_code_rows(codes, index, codebook)
    write_csv(out_dir / 'evidence-codes.csv', list(ev_rows[0]), ev_rows)
    functions = function_order(codebook)
    em_rows = []
    for key, label, _ in EVIDENCE_V2:
        row = {'attribute': key, 'label': label}
        for f in functions + ['All']:
            row[f] = emap[f][key]
            row[f + '_pct'] = round(100 * emap[f][key] / emap[f]['publications'], 1)
        em_rows.append(row)
    write_csv(out_dir / 'evidence-map.csv', list(em_rows[0]), em_rows)
    write_csv(out_dir / 'degradation-function-matrix.csv', list(cells[0]), cells)
    write_csv(out_dir / 'assumption-links.csv', list(links[0]), links)
    write_csv(out_dir / 'function-pair-cooccurrence.csv', list(pairs[0]), pairs)
    cand_fields = ['candidate_id', 'function_a', 'function_b', 'source', 'works', 'direct_wheeled_joint',
                   'wheeled_works', 'safety_relevant', 'gap', 'gap_share', 'eligible', 'rank',
                   'rank_without_integration_stage', 'rank_by_gap_share', 'interface', 'named_alternative', 'status',
                   'reason', 'screen_note', 'codes']
    write_csv(out_dir / 'interface-candidates.csv', cand_fields,
              [{**{k: c[k] for k in cand_fields if k != 'codes'}, 'eligible': 'yes' if c['eligible'] else 'no',
                'rank': c['rank'] or '', 'rank_without_integration_stage': c['rank_without_integration_stage'] or '',
                'rank_by_gap_share': c['rank_by_gap_share'] or '', 'gap_share': '' if c['gap_share'] is None else c['gap_share'],
                'codes': joined(c['codes'])} for c in ranking['candidates']])
    write_csv(out_dir / 'interface-traceability.csv', list(trace[0]), trace)
    write_csv(out_dir / 'sensitivity.csv', list(sens[0]), sens)
    write_csv(out_dir / 'venue-mix-by-stage.csv', list(venues[0]), venues)
    write_csv(out_dir / 'drivetrain-evidence.csv', list(drive[0]), drive)
    write_csv(out_dir / 'platform-groups.csv', list(groups[0]), groups)
    sections = [f['section'] for f in codebook['functions']]
    columns = {sec: {'technical': sum(c['principal_section'] == sec for c in technical),
                     'wheeled': sum(c['principal_section'] == sec and c['platform_group'] == 'WHL' for c in technical)}
               for sec in sections}
    matrix_json = {'note': 'Generated by scripts/build_data.py from the evidence codes; counts describe the purposively selected sample.',
                   'functions': codebook['functions'], 'sources': codebook['sources'],
                   'source_groups': codebook['source_groups'], 'assumptions': codebook['assumptions'],
                   'response_families': codebook['response_families'], 'platform_groups': codebook['platform_groups'],
                   'shade_steps': codebook['shade_steps'], 'columns': columns,
                   'cells': strip_codes(cells, ()), 'links': links}
    (out_dir / 'degradation-function-matrix.json').write_text(json.dumps(matrix_json, indent=2) + '\n', encoding='utf-8')
    tables = {'table-venue-mix.tex': table_venue_mix(venues), 'table-evidence-percent.tex': table_evidence_percent(emap, codebook),
              'table-matrix-works.tex': table_matrix_works(cells, codebook), 'table-sensitivity.tex': table_sensitivity(sens, codebook),
              'table-cooccurrence.tex': table_cooccurrence(pairs), 'table-candidates.tex': table_candidates(ranking, reasons)}
    for name, text in tables.items():
        (out_dir / name).write_text(text, encoding='utf-8')
    rejected = [c['candidate_id'] for c in sorted(ranking['candidates'], key=lambda c: c['rank'] or 10**6)
                if c['status'] == 'rejected']
    summary = {
        'evidence_map_v2': emap,
        'matrix': {f"{c['source']}-{c['section']}": {k: c[k] for k in ('addressed', 'named', 'manipulated', 'wheeled_addressed',
                                                                        'road', 'other_ground', 'non_ground', 'strongest_level')}
                   for c in cells},
        'cooccurrence': strip_codes(pairs),
        'candidates': {'interfaces': ranking['interfaces'], 'lowest_interface_rank': ranking['lowest_interface_rank'],
                       'eligible_count': ranking['eligible_count'], 'top': ranking['top'],
                       'interfaces_are_top4': ranking['interfaces_are_top4'], 'rejected': rejected,
                       'alternatives': ranking['alternatives'], 'human_assistance_codes': ranking['human_assistance_codes'],
                       'interface_works': dict(Counter(str(t['interface']) for t in trace)),
                       'interface_direct_wheeled': dict(Counter(str(t['interface']) for t in trace if t['direct_wheeled'] == 'yes'))},
        'sensitivity': sens,
        'venue_mix': strip_codes(venues, ('venues',)),
        'drivetrain': drive, 'platform_groups': groups,
        'coding': {'codes': len(codes), 'technical': len(technical), 'adjudications': len(log),
                   'locators': len(load_codes(PRIMARY_LOCATORS)[1]),
                   'frozen': freeze['primary'] if freeze else None,
                   'codebook_version': codebook['version']},
    }
    return summary


def inventory_extra(row, codebook):
    """Selection and venue columns that build_data.py adds to corpus-inventory.csv."""
    return {'selection_stage': row['source_batch'], 'stage_label': codebook['stage_labels'][row['source_batch']],
            'principal_section': principal_of(row, codebook), 'venue': row['venue'],
            'publisher': publisher_of(row, codebook), 'publication_type': row['publication_type'], 'doi': row['doi'],
            'platform_group': group_of(row['platform_class'], codebook)}


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
    parser.add_argument('--freeze', action='store_true', help='write freeze.json for the validated primary files')
    parser.add_argument('--import-second', type=Path, metavar='CODES_JSON',
                        help="convert the second coder's codes.json into second-codes.csv and second-locators.csv")
    parser.add_argument('--agreement', action='store_true',
                        help='write generated/coding-agreement.csv and generated/table-agreement.tex')
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
        if args.kind == 'primary' and Path(args.check_codes).resolve() == PRIMARY_CODES.resolve() and FREEZE.is_file():
            try:
                record = check_freeze()
                print('frozen primary-codes.csv SHA-256', record['primary']['primary-codes.csv'], '(matches)')
            except AssertionError as error:
                print('ERROR', error)
                status = 1
    if args.freeze:
        _, codes = load_codes(PRIMARY_CODES)
        errors, _ = validate_codes(codes, rows, codebook, 'primary', locators=load_codes(PRIMARY_LOCATORS)[1])
        if errors:
            print('ERROR primary codes do not validate; not frozen')
            return 1
        record = {'note': 'SHA-256 of the primary coding files at freeze. Later corrections go through adjudication-log.csv only.',
                  'codebook_version': codebook['version'], 'codebook_md_sha256': sha256_file(CODEBOOK_MD),
                  'codebook_json_sha256': sha256_file(CODEBOOK_JSON), 'rows': len(codes),
                  'locators': len(load_codes(PRIMARY_LOCATORS)[1]),
                  'primary': {'primary-codes.csv': sha256_file(PRIMARY_CODES),
                              'primary-locators.csv': sha256_file(PRIMARY_LOCATORS)}}
        FREEZE.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
        print('frozen', record['primary']['primary-codes.csv'])
    if args.import_second:
        print(json.dumps(import_second(args.import_second, rows, codebook), indent=2))
    if args.agreement:
        summary = write_agreement(M / 'generated')['agreement']
        print(json.dumps({k: v for k, v in summary.items() if k != 'rows'}, indent=2))
    return status


if __name__ == '__main__':
    sys.exit(main())
