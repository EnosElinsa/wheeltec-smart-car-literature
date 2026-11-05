"""Derive manuscript data without modifying the evidence library."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

M = Path(__file__).resolve().parents[1]
from project_paths import literature_root
from citation_scope import background_entry, load_background, load_corpus, load_record
from bib_case import protect_entry
import coding
R = literature_root(M)
G = M / 'generated'
G.mkdir(exist_ok=True)

def text_digest(path):
    """SHA-256 of a text file with CRLF normalized to LF, independent of the checkout line endings."""
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def tex(s):
    s = str(s).replace('–', '--').replace('—', '---').replace('‐', '-')
    return ''.join({'&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_',
                    '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}',
                    '\\': r'\textbackslash{}'}.get(c, c) for c in s)

all_rows, rows, inclusion, citation_policy = load_corpus(R, M)
by_id = {r['code']: r for r in rows}
comparison = list(csv.DictReader((R / '06-data/corpus-comparison.csv').open(encoding='utf-8-sig', newline='')))
assert [r['code'] for r in comparison] == [r['code'] for r in all_rows]
comparison = [r for r in comparison if r['code'] in by_id]
assert len(rows) == len(by_id) == len(comparison) == len(inclusion['selected_ids'])
assert set(by_id) == set(inclusion['selected_ids'])
assert [r['code'] for r in comparison] == [r['code'] for r in rows]
assert {r['survey_included'] for r in rows} <= {'yes', 'context'}
verification = load_background(M, citation_policy)
legacy_light = sum(r['verification_level'] == 'light' and r['source_batch'] in
                   {'baseline-2026-09-18', 'supplemental', 'expansion-2026-10-24'} for r in rows)
stats = {field: dict(sorted(Counter(r[field] for r in rows).items())) for field in [
    'source_batch', 'publication_type', 'bibliographic_year', 'survey_module', 'evidence_type',
    'platform_class', 'boundary_platform', 'verification_level', 'evaluation_primary', 'compute_location', 'survey_included']}
stats['evaluation_all'] = dict(sorted(Counter(x.strip() for r in rows for x in r['evaluation_all'].split(',')).items()))
technical_rows = [r for r in rows if r['survey_included'] == 'yes']
assert all(r['evidence_type'] != 'survey' for r in technical_rows)
stats['evaluation_technical'] = dict(sorted(Counter(
    x.strip() for r in technical_rows for x in r['evaluation_all'].split(',')
).items()))
stats['evaluation_denominator'] = len(technical_rows)
# Evidence map: evaluation attributes by the section that reviews each technical publication.
EVIDENCE_MODULES = ['localization-mapping', 'traversability-planning-control', 'semantic-language-navigation',
                    'multi-robot', 'fault-recovery-deployment']
evidence_map = {}
for module in EVIDENCE_MODULES:
    group = [r for r in technical_rows if r['survey_module'] == module]
    attrs = [{x.strip() for x in r['evaluation_all'].split(',')} for r in group]
    evidence_map[module] = {
        'publications': len(group),
        'residual': sum('residual' in a for a in attrs),
        'closed-loop-task': sum('closed-loop-task' in a for a in attrs),
        'designed-degradation': sum('designed-degradation' in a for a in attrs),
        'degradation-with-task': sum({'designed-degradation', 'closed-loop-task'} <= a for a in attrs),
        'integrity-reliability': sum('integrity-reliability' in a for a in attrs),
        'placement-reported': sum(r['compute_location'] != 'not-reported' for r in group),
        'wheeled-target': sum(r['boundary_platform'] == 'no' for r in group),
    }
assert sum(v['publications'] for v in evidence_map.values()) == len(technical_rows)
for attribute, count in stats['evaluation_technical'].items():
    assert sum(v[attribute] for v in evidence_map.values()) == count
stats['evidence_map_card'] = evidence_map
stats['corpus_count'] = len(rows)
stats['indexed_library_count'] = len(all_rows)
stats['internal_reference_count'] = len(citation_policy['internal_reference_ids'])
stats['citation_scope_sha256'] = text_digest(M / 'data/citation-scope.json')
stats['inclusion_sha256'] = text_digest(R / '06-data/survey-inclusion.json')
stats['source_index_sha256'] = digest(R / '06-data/paper-index.csv')
stats['comparison_sha256'] = digest(R / '06-data/corpus-comparison.csv')
# Evidence coding layer (06-data/evidence-coding): final codes (frozen primary codes plus the adjudication log),
# matrices, interface ranking, sensitivity and venue mix. The evidence map of Table VI and every sample statistic
# in the prose come from these codes. The card-based map above remains a sensitivity row (S-card-round3).
stats.update(coding.write_products(G, rows, decisions_path=M / 'data/interface-decisions.json'))
# Pre-resolution agreement of the language-model second coding with the frozen primary codes (40 sampled works).
stats.update(coding.write_agreement(G))
stats['evidence_map'] = stats['evidence_map_v2']
(G / 'stats.json').write_text(json.dumps(stats, indent=2) + '\n', encoding='utf-8')
batches = stats['source_batch']
modules = stats['survey_module']
macros = {'CorpusCount':len(rows), 'CoreCount':len(technical_rows), 'ContextCount':len(rows)-len(technical_rows), 'BackgroundCount':len(verification),
          'BaselineCount':batches['baseline-2026-09-18'], 'SupplementCount':batches['supplemental'], 'ExpansionCount':batches['expansion-2026-10-24'],
          'FollowupCount':batches['followup-2026-11-02'], 'IEEECount':batches['ieee-supplement-2026-11-03'],
          'SurveyExpansionCount':batches.get('survey-200plus-2026-11-03',0),
          'IEEERefreshCount':batches.get('ieee-refresh-2026-11-03',0), 'JournalCount':stats['publication_type']['journal'],
          'ConferenceCount':stats['publication_type']['conference'], 'FullCount':stats['verification_level']['full'], 'LightCount':stats['verification_level']['light'],
          'LegacyLightCount':legacy_light, 'TargetedLightCount':stats['verification_level']['light']-legacy_light,
          'BoundaryCount':stats['boundary_platform']['yes'], 'TargetCount':stats['boundary_platform']['no'],
          'ClosedCount':stats['evidence_type']['closed-loop-hardware'],
          'RecordedCount':stats['evidence_type']['recorded-robot-data'],
          'PlaybackCount':stats['evidence_type']['dataset-playback'],
          'OnlineCount':stats['evidence_type']['online-hardware'],
          'SimulationCount':stats['evidence_type']['simulation'],
          'NumericalCount':stats['evidence_type']['numerical'],
          'ResourceCount':stats['evidence_type']['dataset-resource'],
          'SurveyCount':stats['evidence_type']['survey'],
          'LocalizationCount':modules['localization-mapping'],'PlanningCount':modules['traversability-planning-control'],
          'SemanticCount':modules['semantic-language-navigation'],'MultiCount':modules['multi-robot'],'ReliabilityCount':modules['fault-recovery-deployment'],
          'LegacyRecords':58583,'LegacyReviewable':43086,'LegacyUnreviewed':43041,
          'LegacyJournals':17,'LegacySlices':102,'HistoricalQueue':79,
          'QuerySlices':34,'QueryIncomplete':7,
          'OnboardCount':stats['compute_location']['onboard']}
# Final selection stage (works named by an internal review of an earlier draft).
COVERAGE_BATCH = 'review-additions-2026-11-04'
macros['CoverageCount'] = batches.get(COVERAGE_BATCH, 0)
macros['RecentCount'] = sum(r['bibliographic_year'] in {'2025', '2026'} for r in rows)
macros['RecentShare'] = round(100 * macros['RecentCount'] / len(rows))

# Evidence statistics from the final evidence codes (statistics of the purposively selected sample).
V2 = stats['evidence_map_v2']
FUNCTIONS = ['LOC', 'PLN', 'SEM', 'MRC', 'REL']
PREFIX = {'LOC': 'Loc', 'PLN': 'Pln', 'SEM': 'Sem', 'MRC': 'Mrc', 'REL': 'Rel'}
def pct(k, n):
    return round(100 * k / n)
def vshare(f, key):
    return V2[f][key] / V2[f]['publications']
assert V2['All']['publications'] == len(technical_rows)
for f in FUNCTIONS:
    e, p = V2[f], PREFIX[f]
    macros.update({p + 'TechCount': e['publications'], p + 'TaskCount': e['task_any'], p + 'NamedCount': e['named'],
                   p + 'SameCount': e['task_named_same'], p + 'SameShare': pct(e['task_named_same'], e['publications']),
                   p + 'PhysSameCount': e['physical_task_named_same'], p + 'IntegrityCount': e['integrity'],
                   p + 'NonWheeledCount': e['publications'] - e['group_WHL']})
A = V2['All']
macros.update({'DegTaskCount': A['task_named_same'], 'DegTaskShare': pct(A['task_named_same'], A['publications']),
               'TaskAnyCount': A['task_any'], 'NamedCount': A['named'], 'AddressedCount': A['addressed'],
               'ManipulatedCount': A['manipulated'], 'SelectedOnlyCount': A['selected_only'],
               'IncidentalOnlyCount': A['incidental_only'],
               'DOneSameCount': A['task_manipulated_same'], 'PhysSameCount': A['physical_task_named_same'],
               'DirectWheeledCount': A['direct_wheeled_joint'], 'IntegrityCount': A['integrity'],
               'ComputeUnreported': A['publications'] - A['placement'],
               'GroupWHL': A['group_WHL'], 'GroupROAD': A['group_ROAD'], 'GroupGND': A['group_GND'], 'GroupOTH': A['group_OTH'],
               'DrivetrainEffectCount': A['drivetrain_effect']})
SENS = {r['row_id']: r for r in stats['sensitivity']}
def sens_share(row_id):
    return pct(SENS[row_id]['numerator'], SENS[row_id]['denominator'])
assert SENS['S-def-headline']['numerator'] == A['task_named_same']
macros.update({'DOneNominalShare': sens_share('S-def-D1-nominal'), 'AnyUnitShare': sens_share('S-unit-any'),
               'IncidentalShare': sens_share('S-def-with-incidental'),
               'DegTaskCountCard': SENS['S-card-round3']['numerator'], 'DegTaskShareCard': sens_share('S-card-round3'),
               'DepthFullShare': sens_share('S-depth-full'), 'DepthLegacyShare': sens_share('S-depth-light-legacy'),
               'DepthTargetedShare': sens_share('S-depth-light-targeted'),
               'WhlShare': sens_share('S-platform-WHL'), 'NonWhlShare': sens_share('S-platform-non-WHL'),
               'QuotaShare': sens_share('S-quota'), 'NonQuotaShare': sens_share('S-non-quota'),
               'NoIEEEOnlyShare': sens_share('S-no-ieee-only')})
stage_out = [sens_share(i) for i in SENS if i.startswith('S-stage-out-')]
year_rows = [sens_share(i) for i in SENS if i.startswith('S-year-')]
macros.update({'StageMinShare': min(stage_out), 'StageMaxShare': max(stage_out),
               'YearMinShare': min(year_rows), 'YearMaxShare': max(year_rows)})
# Sensitivity without the coverage additions (Supplement S1).
base = SENS['S-no-coverage']
macros.update({'DegTaskCountBase': base['numerator'], 'CoreCountBase': base['denominator'],
               'DegTaskShareBase': sens_share('S-no-coverage')})
assert (macros['DegTaskCountBase'], macros['CoreCountBase']) == (76, 228)           # S1 sensitivity sentence
assert macros['CoreCountBase'] == len(technical_rows) - batches[COVERAGE_BATCH]
# Interface ranking (Sec. X and Supplement S8).
CAND = stats['candidates']
IFACE = {i['id']: i for i in CAND['interfaces']}
NUMBER = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
for i, word in NUMBER.items():
    macros.update({'Iface' + word + 'Rank': IFACE[i]['rank'], 'Iface' + word + 'RankA': IFACE[i]['rank_without_integration_stage'],
                   'Iface' + word + 'Works': CAND['interface_works'][str(i)],
                   'Iface' + word + 'Direct': CAND['interface_direct_wheeled'].get(str(i), 0)})
macros.update({'CandidateCount': CAND['eligible_count'], 'RejectedCount': len(CAND['rejected']),
               'IfaceBestRank': min(i['rank'] for i in IFACE.values()), 'IfaceWorstRank': CAND['lowest_interface_rank'],
               'HumanAssistCount': len(CAND['human_assistance_codes'])})
assert not CAND['interfaces_are_top4']                       # Sec. X opening: the four interfaces do not rank 1-4
TRACE = list(csv.DictReader((G / 'interface-traceability.csv').open(encoding='utf-8', newline='')))
direct_codes = {i: [t['code'] for t in TRACE if t['interface'] == str(i) and t['direct_wheeled'] == 'yes'] for i in NUMBER}
assert direct_codes[1] == ['R11'] and direct_codes[3] == ['M10'] and direct_codes[4] == []   # Sec. X-A, X-C, X-D
assert max(NUMBER, key=lambda i: len(direct_codes[i])) == 2                                  # Sec. X-B: "the most ... of the four"
assert IFACE[4]['rank'] == 1                                                                 # Sec. X-D: "first in the ranking"
whl_four = [t for t in TRACE if t['interface'] == '4' and t['platform_group'] == 'WHL']
assert {t['level_degradation'] for t in whl_four} <= {'R', 'D', 'O', 'S', 'none'}           # Sec. X-D: "only in recorded data, ..."
macros['IfaceFourWhl'] = len(whl_four)
EV = {r['code']: r for r in csv.DictReader((G / 'evidence-codes.csv').open(encoding='utf-8', newline=''))}
assert not any({'RES', 'COM'} & set(EV[t['code']]['named_sources'].split('|'))
               for t in TRACE if t['interface'] == '2')                     # Sec. X-B: no computation limit or delay named
assert all(EV[k]['functions'] == 'PLN' and EV[k]['direct_wheeled_joint'] == 'yes'
           for k in ('K03', 'K05', 'R13', 'R15'))                           # Sec. X-C: terrain planners without LOC
assert EV['M10']['src_selected'] == 'PER' and EV['M10']['deg_task_setting'] == 'physical' \
    and EV['M10']['level_degradation'] == 'P'                       # Sec. X-C: direct through the GPS-disabled campus run
assert sorted(k for k, e in EV.items() if e['drivetrain_effect'] == 'yes') == sorted(('E02', 'R33', 'M39', 'E04', 'S07', 'N17',
                                                                                     'M04', 'M09', 'N10', 'S16'))
assert EV['S48']['drivetrain_effect'] == 'no' and EV['M09']['drivetrain_effect'] == 'yes' \
    and all(EV[k]['drivetrain'] == 'omnidirectional' for k in ('M09', 'S48'))  # Table II: the two Mecanum studies (M09 yes after the review recheck)
assert {t['code']: t['platform_group'] for t in TRACE if t['interface'] == '1' and t['code'] in ('X07', 'M28')} == \
    {'X07': 'ROAD', 'M28': 'ROAD'}                                                          # Sec. X-A: road-vehicle integrity analyses
DECISIONS = json.loads((M / 'data/interface-decisions.json').read_text(encoding='utf-8'))['decisions']
category = {d['candidate_id']: d['category'] for d in DECISIONS}
rejected = CAND['rejected']
assert all(c in category for c in rejected)                                                  # every higher-ranked candidate has a reason
assert sum(category[c] == 'merged' for c in rejected) == 6 and sum(category[c] == 'named-gap' for c in rejected) == 1
merged = {d['candidate_id']: d['interface'] for d in DECISIONS if d['category'] == 'merged'}
assert merged == {'PLN-MRC:COM': 4, 'LOC-MRC:SFA': 4, 'MRC-REL:SFA': 4, 'LOC-MRC:PER': 4,
                  'PLN-SEM:DYN': 2, 'PLN-REL:MOD': 2}               # Sec. X opening: the merged cases listed per interface
# Headline count of the frozen primary codes before adjudication (Supplement S7).
_, primary_codes = coding.load_codes(coding.PRIMARY_CODES)
macros['DegTaskCountPrimary'] = sum(c['deg_task_class'] in ('D1', 'D2') for c in primary_codes if c['principal_section'] != 'context')
# Venue mix (Sec. III).
VENUE = {r['stage']: r for r in stats['venue_mix']}
ieee_only = coding.load_codebook()['stage_groups']['ieee_only_stages']
macros.update({'IEEEShare': pct(VENUE['all']['IEEE'], VENUE['all']['works']),
               'IEEEOnlyCount': sum(VENUE[s]['works'] for s in ieee_only),
               'IEEEShareRest': pct(VENUE['all']['IEEE'] - sum(VENUE[s]['IEEE'] for s in ieee_only),
                                    VENUE['all']['works'] - sum(VENUE[s]['works'] for s in ieee_only))})
assert all(VENUE[s]['IEEE'] == VENUE[s]['works'] for s in ieee_only)
for stage, name in [('baseline-2026-09-18', 'Baseline'), ('supplemental', 'Supplement'), ('expansion-2026-10-24', 'Expansion'),
                    ('followup-2026-11-02', 'Followup'), ('ieee-supplement-2026-11-03', 'Targeted'),
                    ('survey-200plus-2026-11-03', 'SurveyExpansion'), ('ieee-refresh-2026-11-03', 'Refresh'),
                    (COVERAGE_BATCH, 'Coverage')]:
    macros[name + 'IEEE'] = VENUE[stage]['IEEE']
macros['TotalIEEE'] = VENUE['all']['IEEE']
# Language-model second coding (Sec. III and Supplement S7): pre-adjudication agreement on the double-coded attributes.
AGREE = stats['agreement']
double = [r for r in AGREE['rows'] if r['kind'] == 'attribute']
kappas = sorted(r['kappa'] for r in double)
assert len(double) == 13 and all(isinstance(k, float) for k in kappas)
fmt = lambda k: f'{k:.2f}'.replace('-', '$-$')
macros.update({'SampleCount': AGREE['works'], 'KappaMedian': fmt(kappas[len(kappas) // 2]), 'KappaMin': fmt(kappas[0]),
               'KappaMax': fmt(kappas[-1]), 'AgreeMin': f"{min(r['agreement_pct'] for r in double):.1f}",
               'AgreeMax': f"{max(r['agreement_pct'] for r in double):.1f}",
               'DisagreeCount': AGREE['disagreements'], 'ResolvedPrimary': AGREE['resolutions']['primary-kept'],
               'ResolvedSecond': AGREE['resolutions']['second-adopted'], 'ResolvedBoth': AGREE['resolutions']['both-revised'],
               'ChangedPrimary': AGREE['changed_primary'],
               'HeadlineKappa': fmt(next(r['kappa'] for r in double if r['attribute'] == 'deg_task_class'))})
AGREE_CSV = {r['attribute'] + '|' + r['unit']: r for r in csv.DictReader((G / 'coding-agreement.csv').open(encoding='utf-8', newline=''))}
assert (AGREE_CSV['drivetrain_effect|value']['primary_prevalence'], AGREE_CSV['drivetrain_effect|value']['second_prevalence']) == \
    ('yes:1 no:39', 'yes:4 no:36')                                   # Supplement S7: "four works ... to one"
assert [r['attribute'] for r in sorted(double, key=lambda r: r['kappa'])[:2]] == ['drivetrain_effect', 'nominal_control']
# Sec. III and Supplement S7: the kappa range runs from the drivetrain effect to incidental sources, which both
# coders set in the same few source flags.
assert [r['attribute'] for r in double if r['kappa'] == kappas[-1]] == ['src_incidental']
incidental = next(r for r in double if r['attribute'] == 'src_incidental')
_, second_codes = coding.load_codes(coding.SECOND_CODES)
frozen = {c['code']: c for c in primary_codes}
flags = lambda c: {(c['code'], s) for s in coding.split_set(c['src_incidental'])}
inc_second = set().union(*(flags(c) for c in second_codes))
inc_primary = set().union(*(flags(frozen[c['code']]) for c in second_codes))
assert inc_second == inc_primary and incidental['works_in_disagreement'] == 0
assert len(inc_second) / incidental['n'] < 0.01                      # Sec. III: "the rarely coded incidental sources"
assert incidental['n'] == len(second_codes) * len(coding.load_codebook()['source_order'])
macros.update({'IncidentalFlags': len(inc_second), 'IncidentalUnits': incidental['n']})
assert AGREE['corpus_recheck_changes'] == 6                          # Supplement S7: "six further values"

# Qualitative statements that rest on the evidence codes (each comment names the sentence).
same = {f: vshare(f, 'task_named_same') for f in FUNCTIONS}
assert vshare('LOC', 'task_any') < 0.05                         # Sec. IV synthesis, IX-B: "only n of N ... task outcome"
assert V2['LOC']['task_any'] == 1                               # Sec. IV synthesis, IX-B: singular "reports"
assert V2['LOC']['component'] == V2['LOC']['publications']      # Sec. IX-B: "all ... report component measures"
assert min(same, key=same.get) == 'LOC' and max(same, key=same.get) == 'PLN'   # abstract, Sec. I, IX-B, XI: "from LOC to PLN"
assert [f for f in sorted(FUNCTIONS, key=same.get)] == ['LOC', 'MRC', 'REL', 'SEM', 'PLN']   # Sec. IX-B order of shares
assert vshare('PLN', 'task_any') > 0.5 and vshare('SEM', 'task_any') > 0.5   # Sec. V, VI: "most ... report task outcomes"
assert vshare('SEM', 'task_named_same') < 0.5                   # Sec. VI: "fewer than half"
assert vshare('MRC', 'task_named_same') < 0.25                  # Sec. VII: "fewer than a quarter"
assert V2['REL']['integrity'] > A['integrity'] / 2              # Sec. VIII, IX-B: "n of the N integrity assessments"
assert vshare('LOC', 'group_WHL') < 0.5                         # Sec. IV synthesis: non-wheeled carriers
robust = [r for i, r in SENS.items() if i.startswith(('S-stage-out-', 'S-depth-')) or i in ('S-quota', 'S-non-quota')]
assert all(r['RF1'] in ('holds', 'holds (tie)') and r['RF4'] == 'holds' for r in robust)   # Sec. IX-B robustness sentence
assert all(r['RF2'] == 'fails' for r in robust)                 # Sec. IX-B: planning, not fault management, is highest
assert all(max(FUNCTIONS, key=lambda f: r[f]) == 'PLN' for r in robust)   # Sec. IX-B: "... and planning the highest"
definitions = [r for i, r in SENS.items() if i.startswith(('S-def-', 'S-unit-', 'S-card-'))]
assert all(r['RF1'] == 'holds' and r['RF4'] == 'holds' for r in definitions)               # Supplement S6: "under every definition"
assert [i for i, r in SENS.items() if r['RF1'] == 'fails'] == ['S-year-2026']               # Supplement S6: "RF1 fails only ... 2026"
assert [i for i, r in SENS.items() if r['RF4'] == 'fails'] == ['S-quota-theme-T2']          # Supplement S6: "RF4 only in one quota theme"
assert SENS['S-def-headline']['RF2'] == SENS['S-def-headline']['RF3'] == 'fails'            # Supplement S6: RF2 and RF3 fail
assert SENS['S-card-round3']['RF2'] == 'holds'                                              # Supplement S6: card coding supported RF2
assert sum(r['RF1'] == 'holds (tie)' for r in robust) == 1 and SENS['S-depth-full']['RF1'] == 'holds (tie)'
(G / 'stats.tex').write_text('% Generated by scripts/build_data.py; counts describe this sample.\n' +
    '\n'.join('\\newcommand{\\'+k+'}{'+(v if isinstance(v, str) else f'{v:,}')+'}' for k,v in macros.items())+'\n', encoding='utf-8')

# Preserve each original publisher entry except the necessarily unique citation key.
# Listed author names that a publisher export gives in lowercase are capitalized in refs.bib only.
AUTHOR_CASE = {'K12': ('ichter, brian', 'Ichter, Brian')}
keymap, blocks = [], ['% DERIVED bibliography. Source citation.bib files remain byte-identical.\n']
for row in rows:
    raw = (R / row['bibtex']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == row['bibtex_sha256']
    source = raw.decode('utf-8-sig').strip().replace('\r\n','\n').replace('\r','\n')
    source = '\n'.join(line.rstrip() for line in source.splitlines())
    matches = list(re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,', source))
    assert len(matches) == 1, row['code']
    match = matches[0]; old = match.group(1); new = 'P_' + row['code']
    source = source[:match.start(1)] + new + source[match.end(1):]
    source = source.replace('&amp;', '&')
    source = re.sub(r'(?<!\\)&', lambda _match: r'\&', source)
    source = protect_entry(source)
    transformation = 'unique citation key; line endings and trailing whitespace normalized; HTML ampersand decoded and LaTeX ampersand escaped; acronyms, mixed-case names and listed proper names in the title brace-protected for IEEEtran sentence case (scripts/bib_case.py); publisher fields retained'
    if row['code'] in AUTHOR_CASE:
        lower_name, name = AUTHOR_CASE[row['code']]
        assert source.count(lower_name) == 1, row['code']
        source = source.replace(lower_name, name)
        transformation += '; lowercase author name "' + lower_name + '" capitalized'
    blocks.append('% '+row['code']+'; raw source SHA-256: '+row['bibtex_sha256']+'\n'+source+'\n')
    keymap.append({'code':row['code'],'key':new,'raw_key':old,'raw_bibtex':row['bibtex'],
                   'raw_sha256':row['bibtex_sha256'],'formal_year':row['bibliographic_year'],
                   'transformation':transformation})
blocks.append('% ===== Verified background references (not in reviewed corpus) =====\n')
for item in verification:
    # Derived context entries: metadata fields are copied from the opened DOI record or official catalogue page.
    blocks.append(background_entry(item['key'], load_record(M, item)))
(M / 'refs.bib').write_text('\n'.join(blocks), encoding='utf-8')
(G / 'citation-key-map.json').write_text(json.dumps(keymap,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

selected = {
 'localization': ['M16','E01','E02','E03','E08','N02','E16','N20','F04','F11','S24','S37','S46'],
 'planning': ['M14','M29','M40','N08','E13','E21','E22','E25','N12','F08','S09','S42','S45'],
 'semantic': ['M07','N09','E44','E47','E48','E49','E50','F05','F06','S12','S40','S44'],
 'multi-robot': ['X08','N07','N11','E36','E40','F03','F09','F12','F14','F15','S10','S25','S29'],
 'reliability': ['N10','N16','M35','M37','E51','N17','F01','F02','F07','S16','S38','S41'],
}
titles = {'localization':'Localization and mapping: representative mechanisms, sensing, and evaluation settings',
          'planning':'Traversability, planning, and control: representative mechanisms, sensing, and evaluation settings',
          'semantic':'Semantic and language-guided navigation: representative mechanisms, sensing, and evaluation settings',
          'multi-robot':'Multi-robot coordination: representative mechanisms, sensing, and evaluation settings',
          'reliability':'Reliability and recovery: representative mechanisms, sensing, and evaluation settings'}
ev = {'closed-loop-hardware':'Hardware','recorded-robot-data':'Acquired data','dataset-playback':'Replay',
      'online-hardware':'Online estimate','dataset-resource':'Dataset','simulation':'Sim.',
      'numerical':'Numerical','survey':'Review','theory-only':'Theory'}
outcomes = {'closed-loop-task':'Task outcome','residual':'Component error','designed-degradation':'Degradation testing',
            'integrity-reliability':'Integrity/reliability'}
compute = {'desktop-offline':'Desktop evaluation','onboard':'Onboard','not-reported':'Unspecified','cloud':'Cloud',
           'mixed':'Mixed placement','offboard-local':'Local offboard','not-applicable':'Not applicable'}
# Publication-facing summaries: mechanisms are explained in the cited sections.
method_inputs = {
 'N02': 'Near-planar pose with stochastic out-of-plane perturbations. Inputs: 3D LiDAR, IMU',
 'N20': 'Joint grid-distribution fitting over multiple scans. Inputs: 3D LiDAR, IMU',
 'N08': 'Direction-dependent quasi-static terrain costs. Inputs: LiDAR terrain map, FAST-LIO pose',
 'N12': 'Adaptive spherical tubes for prescribed-time reach-avoid. Inputs: robot state, online unsafe-set geometry',
 'N09': 'VLM frontier allocation with geometric goal execution. Inputs: RGB-D, shared map, robot states',
 'N07': 'Submodular loop-edge selection after coverage planning. Inputs: prior topo-metric graph',
 'N11': 'Range-consistency localization-error reconstruction. Inputs: emulated ranges, reported poses',
 'N10': 'Tracking-loss stop and relocalization; restart after failure. Inputs: stereo vision, actuator feedback',
 'N13': 'Fault prediction and withdrawal before complete failure. Inputs: simulated behavior and fault channels',
 'N16': 'Zonotopic detection and fault-class separation. Inputs: yaw rate, odometry, sideslip, steering angle',
 'N17': 'Behavior-tree supervision and failure-specific recovery. Inputs: terrain maps, contacts, planner status',
 'N18': 'Path-conditioned predictive anomaly detection. Inputs: planned path, RGB, LiDAR',
 'M16': 'Uncertainty-weighted prior-map matching with LIO and gated GNSS. Inputs: 3D LiDAR, IMU, GNSS',
 'E01': 'Selective historical anchoring and point selection under degeneracy. Inputs: 3D LiDAR, IMU',
 'E02': 'Directional process-covariance inflation from geometric corrections. Inputs: time-of-flight camera and wheels; LiDAR replaces depth in replay',
 'E03': 'Region- and degeneracy-dependent sensor fusion. Inputs: LiDAR, IMU, UWB, wheel encoders',
 'E08': 'Map hibernation, reinitialization, and pose-graph registration. Inputs: LiDAR/IMU from handheld and vehicle rigs',
 'E10': 'Consistency rejection and point-assisted line triangulation. Inputs: monocular images, IMU, wheel encoders',
 'E16': 'Semantic-cluster persistence estimation and map filtering. Inputs: 3D LiDAR, semantic labels',
 'E19': 'Asynchronous dynamic-object masking and mask propagation. Inputs: RGB-D streams',
 'F04': 'Degeneracy-triggered introduction of visual constraints. Inputs: LiDAR, camera, IMU',
 'F11': 'Uneven-terrain localization and mapping benchmark. Inputs: LiDAR, RGB-D, IMU, GNSS; mixed reference systems',
 'M14': 'Unknown-region safety classification and route optimization. Inputs: 3D LiDAR',
 'M29': 'Heading-dependent accessible-range prediction for TEB planning. Inputs: LiDAR history',
 'M40': 'Semantic terrain segmentation combined with elevation costs. Inputs: RGB images, 3D LiDAR',
 'M33': 'Offline GP residual learning for feedback-linearized MPC. Inputs: RTK GPS, IMU',
 'E13': 'Keyframe-linked frontiers and information-aware adaptive roadmaps. Inputs: RGB-D/LiDAR (simulation); stereo depth (hardware)',
 'E21': 'Switching between onboard linear and cloud nonlinear MPC. Inputs: externally measured poses',
 'E22': 'CBF constraints with circulation and hold logic. Inputs: 2D LiDAR, external robot pose',
 'E25': 'Scenario constraints on joint collision risk with deceleration fallback. Inputs: robot/pedestrian poses and velocity estimates',
 'E28': 'Infrastructure-based hazard inference added to navigation cost. Inputs: RGB-D cameras and environmental sensors',
 'F08': 'Environment-level calibration of obstacle inflation for constrained planning. Inputs: RGB-D point clouds, VIO',
 'M07': 'Cue-triggered VLM judgments used as social DWA costs. Inputs: RGB images, LiDAR',
 'M20': 'Language-model exploration directions with independent target grounding. Inputs: RGB-D',
 'E44': 'Carrier--object memory with visibility-dependent updates. Inputs: RGB-D, language/image queries, SLAM pose',
 'E47': 'Image--language similarity projected into a frontier value map. Inputs: RGB-D, odometry',
 'E48': 'Hierarchical retrieval over floor, room, and object graphs. Inputs: RGB-D, LiDAR-derived poses',
 'E49': 'Multiscale video memory and discrete action prediction. Inputs: monocular RGB video, instruction',
 'E50': 'Receding-horizon language-conditioned velocity prediction. Inputs: RGB image, text instruction',
 'F05': 'VLM selection among generated trajectories with local DWA control. Inputs: LiDAR, RGB, velocity, GPS',
 'F06': 'Group-aware routing with predictive barrier-constrained control. Inputs: 2D LiDAR, RGB images',
 'X08': 'One-hop consensus for semantic mapping and viewpoint planning. Inputs: RGB-D, LiDAR',
 'E31': 'Sparse object/odometry exchange and loop-closure frame alignment. Inputs: RGB-D or LiDAR, object labels, VIO/LIO',
 'E33': 'Diffusion-based map prediction from shared trajectories. Inputs: LiDAR, wheel encoders, IMU, GPS',
 'E36': 'Descriptor matching and scan selection before submap registration. Inputs: 3D LiDAR, LIO poses',
 'E40': 'Incremental local factor graphs with shared-variable consensus. Inputs: odometry and inter-robot factors',
 'F03': 'Residual-based fault isolation and correlation-aware map repair. Inputs: LiDAR, wheel odometry; GNSS initialization',
 'F09': 'Terrain-aware 3D Voronoi allocation and subgoal selection. Inputs: LiDAR, A-LOAM poses',
 'F12': 'Failure-dependent tracking modes and target-state fusion. Inputs: target range/bearing and inter-robot messages',
 'F14': 'Intersection allocation from shared position histories. Inputs: LiDAR localization and low-bandwidth radio',
 'F15': 'Similarity-pose-graph fusion for monocular scale correction. Inputs: camera, inter-rover UWB ranges',
 'M01': 'Virtual-error prescribed-performance tracking under sensing faults. Inputs: heading, wheel speeds; exact position assumed',
 'M15': 'Mixed-gain adaptation under partial wheel-effectiveness loss. Inputs: modeled tracking states',
 'M28': 'Association-fault hypotheses for undetected lateral-error risk. Inputs: LiDAR landmarks, IMU',
 'M35': 'Joint pose/reliability estimation with global relocalization. Inputs: 2D LiDAR, odometry or inertial navigation',
 'M37': 'Long-term service, docking, and remote human supervision. Inputs: LiDAR, RGB-D, docking and home sensors',
 'E51': 'Kinematic residuals for sensor-fault diagnosis. Inputs: inertial channels and an inertial-aided position substitute',
 'E53': 'Lie-group fusion with cross-covariance propagation and marker rejection. Inputs: IMU, wheels, camera markers',
 'E55': 'CBF control over candidate sensing or actuation faults. Inputs: modeled state channels; trusted heading in the wheeled example',
 'E58': 'Cyclic scheduling of operating and charging periods. Inputs: known durations and station availability',
 'E59': 'GP prediction of planner failure with stop--relocate--resume recovery. Inputs: LiDAR-based mapping',
 'F01': 'Prior-line-map localization with an error protection level. Inputs: monocular images, IMU, prior 3D lines',
 'F02': 'Observer-based fault estimation and event-triggered tracking. Inputs: vehicle-posture outputs in the model',
 'F07': 'Action-consistency and VLM progress monitoring. Inputs: external RGB-D and mobile-base motion capture',
}
display_names = {
 'N08':'Anisotropic exploration', 'N07':'Active graph exploration', 'N11':'Range integrity',
 'N10':'Visual NMPC recovery', 'N13':'Predictive swarm recovery', 'N16':'Set-based LPV diagnosis',
 'N17':'Behavior-tree recovery',
 'M16':'Uncertainty-aware localization', 'M29':'CADNet', 'M33':'GP-MPC',
 'E21':'Vehicle--cloud MPC', 'E25':'Safe Horizon MPC',
 'E28':'Environment-centric risk', 'F08':'Perceive With Confidence',
 'M20':'LGX', 'X08':'ROAM', 'F03':'Collaborative map repair',
 'F09':'TAPM-IVP', 'F12':'Failure-aware tracking', 'F14':'Cross-rank',
 'M01':'Virtual-error tracking', 'M15':'Mixed-gain tracking',
 'M28':'Particle-filter integrity', 'M35':'Reliable MCL',
 'M37':'Long-term home deployment', 'E53':'Lie-group localization',
 'E55':'Fault-aware CBF control', 'E58':'Persistent charging',
 'E59':'GP-based recovery', 'F01':'Line-map integrity', 'F02':'Event-triggered tracking',
}
dimension_names = {
 'residual':'Component measures', 'closed-loop-task':'Task outcomes',
 'designed-degradation':'Degradation testing', 'integrity-reliability':'Integrity/reliability',
}
evaluation_focus = {
 'N02':'Pose error; slope-model boundary', 'N20':'Pose error, runtime, sensor compatibility',
 'N08':'Exploration, travel cost, body roll', 'N12':'Reach-avoid and prescribed-time behavior',
 'N09':'HM3D search; separate hardware demos', 'N07':'Simulated coverage and graph objective',
 'N11':'Error reconstruction with emulated ranges', 'N10':'Tracking; stop/relocalization handling',
 'N13':'Foraging with assumed maintenance', 'N16':'Detectability and isolability under injected faults',
 'N17':'Recovery on retained scenarios; human-rescue boundary', 'N18':'Prediction on recordings; rosbag timing',
 'M16':'Pose error and covariance estimates', 'E01':'Absolute pose error and runtime',
 'E02':'Trajectory error across covariance variants', 'E03':'Localization error across fusion modes',
 'E08':'Trajectory error and map registration', 'E10':'Trajectory error and line-feature ablation',
 'E16':'Registration and map persistence', 'E19':'Trajectory error and tracking runtime',
 'F04':'Trajectory error under modality failure', 'F11':'Localization/mapping error and runtime',
 'M14':'Exploration time and travel cost', 'M29':'Traversability prediction and navigation',
 'M40':'Terrain segmentation and navigation success', 'M33':'Lateral and heading tracking error',
 'E13':'Exploration time, pose error, and runtime', 'E21':'Tracking and collision outcomes',
 'E22':'Obstacle avoidance and escape from equilibria', 'E25':'Task duration and planned collision risk',
 'E28':'Hazard exposure and task success', 'F08':'Collision-free outcomes and calibration',
 'M07':'Task success, collisions, and social behavior', 'M20':'Object-search success',
 'E44':'Success across sequential object queries', 'E47':'Goal success and path efficiency',
 'E48':'Object retrieval and navigation success', 'E49':'Goal success and path efficiency',
 'E50':'Target arrival and action-generation time', 'F05':'Outdoor traversal and model-response time',
 'F06':'Social disturbance, travel time, and jerk', 'X08':'Distributed mapping and exploration',
 'E31':'Inter-robot registration error', 'E33':'Coverage and energy-budget trade-off',
 'E36':'Map-merging error and transmitted data', 'E40':'Estimation error with limited communication',
 'F03':'Pose/map error and fault isolation', 'F09':'Success, travel cost, and path duplication',
 'F12':'Target-state error during failures', 'F14':'Exploration under intermittent reception',
 'F15':'Pose error and monocular scale correction', 'M01':'Tracking error under sensing faults',
 'M15':'Tracking error under actuator loss', 'M28':'Undetected lateral-error risk',
 'M35':'Reliability estimates and relocalization', 'M37':'Service outcomes and interruptions',
 'E51':'Fault-isolation residual patterns', 'E53':'Localization error and consistency',
 'E55':'Constraint satisfaction under modeled faults', 'E58':'Operating time and charging schedules',
 'E59':'Navigation success with/without recovery', 'F01':'Pose error and protection-level coverage',
 'F02':'Tracking error and update frequency', 'F07':'Failure detection and nominal alarms',
}

method_inputs.update({
 'S24':'Directional feature selection and weighting. Inputs: LiDAR; capture IMU not integrated',
 'S37':'Subspace decoupling and directional preconditioning. Inputs: LiDAR registration constraints',
 'S46':'Semantic neural-process elevation and uncertainty. Inputs: LiDAR, image semantics, poses',
 'S09':'Parallel optimization of homotopy alternatives. Inputs: externally tracked robot/pedestrian states',
 'S42':'Expert-trained cost, speed, and novelty maps for MPPI. Inputs: RGB features, LiDAR geometry',
 'S45':'Angle-conditioned risk queried during planning. Inputs: prepared point cloud, LiDAR/IMU pose',
 'S12':'Multimodal spatial retrieval and goal APIs. Inputs: offline RGB-D/pose/audio map, instructions',
 'S40':'Interaction-grounded terrain costs and DWA. Inputs: RGB, LiDAR, proprioception, GPS, aerial images',
 'S44':'Social scene-understanding VQA benchmark. Inputs: recorded images, pedestrian annotations',
 'S10':'Sparse loop prioritization and decentralized inference. Inputs: local odometry, loop observations',
 'S25':'Joint motion and observation scheduling. Inputs: relative marker observations, IMU',
 'S29':'Lossy keyframe selection and lossless coding. Inputs: visual/inertial keyframes',
 'S16':'Hybrid A* reinitialization and local smoothing. Inputs: RTK pose, voxel obstacle map',
 'S38':'Affordance prediction and anti-novelty recovery. Inputs: RGB at deployment; offline robot data',
 'S41':'Online RL with resets, goals, and charging. Inputs: RGB policy; LiDAR/map, bumper for supervision',
})
display_names.update({'S24':'DR-ICP','S37':'Decoupled registration','S46':'Semantic neural processes',
 'S09':'Homotopy MPC','S42':'Visual-geometric MPPI','S45':'SPARTA','S12':'AVLMaps',
 'S40':'VLM-GroNav','S44':'SocialNav-SUB','S10':'Swarm-SLAM','S25':'Planned synchronization',
 'S29':'Bandwidth-efficient SLAM','S16':'RTEB','S38':'SCALE','S41':'LiReN'})
evaluation_focus.update({
 'S24':'Tunnel pose error; pure-LiDAR scope', 'S37':'Registration; missing-information boundary',
 'S46':'Elevation error and uncertainty; calibration needed', 'S09':'Dynamic avoidance; external pose',
 'S42':'Interventions, speed, and terrain response', 'S45':'Simulated tire risk; virtual risky hardware branch',
 'S12':'Multimodal goals; prepared-map validity', 'S40':'Outdoor task outcomes; GPS/cloud dependencies',
 'S44':'Human/rule agreement; no closed-loop control', 'S10':'Online collaborative estimation; team exchange',
 'S25':'Formation and check-in cost; modeled non-idealities', 'S29':'Bandwidth/accuracy tradeoff; central back end',
 'S16':'Planner recovery; TEB/NMPC comparisons', 'S38':'Visual recovery and intervention need',
 'S41':'Adaptation with operational resets and infrastructure',
})

CODEBOOK = coding.load_codebook()
# Platform-group marks of the module tables (R road vehicle, G other ground robot, N non-ground or no platform).
GROUP_MARK = {g['id']: g['mark'] for g in CODEBOOK['platform_groups']}
for module, codes in selected.items():
    lines = [r'\begin{table*}[t]',r'\centering',r'\caption{'+titles[module]+r'.}',
             r'\label{tab:'+module+'}',r'\surveytableformat',
             r'\begin{tabularx}{\linewidth}{@{}L{2.7cm}YL{3.35cm}L{3.45cm}@{}}',r'\toprule',
             r'\textbf{Work} & \textbf{Mechanism and inputs} & \textbf{Evaluation setting}\par\textit{Evaluated quantities} & \textbf{Platform}\par\textit{Computation} \\',r'\midrule']
    for code in codes:
        r = by_id[code]
        sensors = method_inputs[code]
        assert sensors.count('(') == sensors.count(')'), code
        mechanism, separator, inputs = sensors.partition('. Inputs: ')
        assert separator, code
        platform = r['platform_class'].replace('ackermann','Ackermann').replace('wheeled-unspecified','wheeled (drive unspecified)').replace('road-vehicle','road vehicle').replace('-',' ')
        mark = GROUP_MARK[coding.group_of(r['platform_class'], CODEBOOK)]
        name = r'\textbf{'+tex(display_names.get(code, r['short_name']))+r'}~\cite{P_'+code+'}'+(r'\textsuperscript{'+mark+'}' if mark else '')
        settings = ', '.join(ev[x.strip()] for x in r['evidence_all'].split(','))
        if code == 'F02':
            settings = 'Hardware-in-the-loop, Numerical'
        if code == 'N11':
            settings = 'Online monitor (mixed reality), Sim.'
        if code != codes[0]:
            lines.append(r'\addlinespace[3pt]')
        mechanism_cell = r'\surveytableinputs{'+tex(mechanism)+'.}{'+tex(inputs)+'}'
        setting_cell = r'\surveytablepair{'+tex(settings)+'}{'+tex(evaluation_focus[code])+'}'
        placement = compute[r['compute_location']]
        if code == 'N09':
            placement = 'Onboard pose; offboard perception/planning'
        if code == 'N11':
            placement = 'Central ground station; emulated ranges'
        if code == 'N18':
            placement = 'Recorded-data processing'
        platform_cell = r'\surveytablepair{'+tex(platform)+'}{'+tex(placement)+'}'
        lines.append(name+' & '+mechanism_cell+' & '+setting_cell+' & '+platform_cell+r' \\')
    lines += [r'\bottomrule',r'\end{tabularx}',r'\surveyplatformnote',r'\end{table*}']
    (G / ('table-'+module+'.tex')).write_text('\n'.join(lines)+'\n',encoding='utf-8')

# Table VI (evidence map) from the final evidence codes. Rows and keys are checked by verify_delivery.py.
EVALUATION_ROWS = [
    (None, [('Publications', 'publications')]),
    ('Measurement level', [('Component measures', 'component'), ('Task outcome', 'task_any'),
                           ('Physical task outcome', 'task_physical')]),
    ('Degradation evidence', [('Named condition (D1 or D2)', 'named'),
                              ('Injected or varied, D1', 'manipulated'), ('Selected only, D2', 'selected_only'),
                              ('Incidental only, D3', 'incidental_only')]),
    ('Same experiment', [('Named condition and task outcome', 'task_named_same'),
                         ('D1 condition and task outcome', 'task_manipulated_same'),
                         ('On a physical robot', 'physical_task_named_same'),
                         ('On a target wheeled robot', 'direct_wheeled_joint')]),
    ('Assessment and resources', [('Integrity or failure risk', 'integrity'),
                                  ('Computation placement', 'placement')]),
    ('Platform group', [('Target wheeled robot', 'group_WHL'), ('Road vehicle (R)', 'group_ROAD'),
                        ('Other ground robot (G)', 'group_GND'), ('Non-ground or none (N)', 'group_OTH')]),
]
stats['evaluation_table_keys'] = [key for _, keys in EVALUATION_ROWS for _, key in keys]
(G / 'stats.json').write_text(json.dumps(stats, indent=2) + '\n', encoding='utf-8')
lines = [r'\begin{table}[!ht]',r'\centering',
         r'\caption{Coded evidence attributes of the \CoreCount{} technical publications, by the section that reviews each publication. Attributes overlap, and the context review is excluded.}',
         r'\label{tab:evaluation}',r'\surveytableformat',r'\setlength{\tabcolsep}{3.2pt}',r'\renewcommand{\arraystretch}{1.04}',
         r'\begin{tabularx}{\linewidth}{@{}Yrrrrrr@{}}',r'\toprule',
         r'\textbf{Attribute} & \textbf{IV} & \textbf{V} & \textbf{VI} & \textbf{VII} & \textbf{VIII} & \textbf{All} \\',r'\midrule']
def evidence_row(label, key):
    values = [V2[f][key] for f in FUNCTIONS]
    total = str(V2['All'][key]) if key == 'publications' else f"{V2['All'][key]} ({pct(V2['All'][key], len(technical_rows))}\\%)"
    return label+' & '+' & '.join(str(v) for v in values)+' & '+total+r' \\'
for group, keys in EVALUATION_ROWS:
    if group:
        lines.append(r'\addlinespace[2pt]')
        lines.append(r'\multicolumn{7}{@{}l}{\textit{'+group+r'}} \\')
    for label, key in keys:
        lines.append(evidence_row(label, key))
lines += [r'\bottomrule',r'\end{tabularx}',
          r'\par\vspace{3pt}\parbox{\linewidth}{\footnotesize\raggedright Counts are per publication. A same-experiment row counts a publication only when the condition and the task outcome come from one experiment. Percentages refer to all \CoreCount{} publications. Table~\ref{S-tab:evidence-percent} gives column percentages.}',
          r'\end{table}']
(G / 'table-evaluation.tex').write_text('\n'.join(lines)+'\n',encoding='utf-8')

# Table I (related surveys) from data/related-surveys.json; scopes follow each survey's abstract.
related = json.loads((M / 'data/related-surveys.json').read_text(encoding='utf-8'))
background_keys = {item['key'] for item in verification}
lines = [r'\begin{table*}[t]', r'\centering',
         r"\caption{Related surveys characterized from their abstracts. ``Not stated'' means that the abstract does not name the topic, which does not exclude coverage in the body of the survey.}",
         r'\label{tab:related-reviews}', r'\surveytableformat',
         r'\begin{tabularx}{\linewidth}{@{}L{4.1cm}L{3.4cm}L{3.5cm}L{2.0cm}Y@{}}', r'\toprule',
         r'\textbf{Survey} & \textbf{Platform scope} & \textbf{Degradation coverage} & \textbf{Recovery or faults} & \textbf{Evaluation practice} \\',
         r'\midrule']
for item in related['rows']:
    key = item['key']
    assert key in background_keys or key == 'P_X04', key
    assert item['basis_url'].startswith(('https://www.semanticscholar.org/paper/', 'https://api.crossref.org/works/')), key
    if key.startswith('B_'):
        record = load_record(M, next(v for v in verification if v['key'] == key))
        assert record['DOI'].lower() == item['doi'], key
    else:
        assert by_id[key[2:]]['doi'].lower() == item['doi'], key
    cells = [tex(item['survey']) + ' (' + item['year'] + r')~\cite{' + key + '}'] + [tex(item[c]) for c in ('platform', 'degradation', 'recovery', 'evaluation')]
    lines.append(' & '.join(cells) + r' \\')
own = related['this_survey']
lines += [r'\midrule', ' & '.join([tex(own['survey']) + ' (' + own['year'] + ')'] + [tex(own[c]) for c in ('platform', 'degradation', 'recovery', 'evaluation')]) + r' \\',
          r'\bottomrule', r'\end{tabularx}', r'\end{table*}']
(G / 'table-related-reviews.tex').write_text('\n'.join(lines) + '\n', encoding='utf-8')

result_cases = json.loads((M / 'data/within-study-comparisons.json').read_text(encoding='utf-8'))
lines = [r'\begin{table*}[!t]', r'\centering',
         r'\caption{Selected results and within-study comparisons. Table and figure numbers in the first column refer to the cited papers. Each row retains its own metric and protocol.}',
         r'\label{tab:selected-results}',r'\surveytableformat',
         r'\begin{tabularx}{\linewidth}{@{}L{2.8cm}L{4.3cm}L{4.4cm}Y@{}}',r'\toprule',
         r'\textbf{Study / source} & \textbf{Protocol and measure} & \textbf{Reported result} & \textbf{Interpretation} \\',r'\midrule']
for i, case in enumerate(result_cases):
    assert case['code'] in by_id and case['physical_pdf_pages']
    assert by_id[case['code']]['pdf_sha256'] == case['pdf_sha256']
    source_pdf = R / by_id[case['code']]['pdf']
    if source_pdf.exists():
        assert digest(source_pdf) == case['pdf_sha256']
    if i:
        lines.append(r'\addlinespace[3pt]')
    study = tex(case['name'])+r'~\cite{P_'+case['code']+r'}\par '+tex(case['source_artifact'])
    lines.append(' & '.join([study, tex(case['protocol_measure']), tex(case['result']), tex(case['interpretation'])])+r' \\')
lines += [r'\bottomrule',r'\end{tabularx}',r'\end{table*}']
(G / 'table-selected-results.tex').write_text('\n'.join(lines)+'\n',encoding='utf-8')

modules = ['localization-mapping','traversability-planning-control','semantic-language-navigation','multi-robot','fault-recovery-deployment']
labels = ['Localization / mapping','Planning / control','Semantic navigation','Multi-robot','Reliability / recovery']
years = sorted({int(r['bibliographic_year']) for r in rows})
# Cross-tab for scripts/build_figures.py (Fig. S1).
crosstab = {'years': years, 'modules': modules, 'labels': labels,
            'counts': {m: [sum(1 for r in rows if r['survey_module'] == m and int(r['bibliographic_year']) == y) for y in years] for m in modules}}
(G / 'corpus-year-module.json').write_text(json.dumps(crosstab, indent=2) + '\n', encoding='utf-8')

codebook = coding.load_codebook()
inventory_extra = ['selection_stage','stage_label','principal_section','venue','publisher','publication_type','doi','platform_group']
with (G / 'corpus-inventory.csv').open('w',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['code','key','title','formal_year','module','evidence','boundary','verification','source_pdf_sha256','source_bib_sha256','source_md_sha256']+inventory_extra)
    writer.writeheader()
    for r in rows:
        writer.writerow(dict(code=r['code'],key='P_'+r['code'],title=r['title'],formal_year=r['bibliographic_year'],module=r['survey_module'],evidence=r['evidence_type'],boundary=r['boundary_platform'],verification=r['verification_level'],source_pdf_sha256=r['pdf_sha256'],source_bib_sha256=r['bibtex_sha256'],source_md_sha256=r['markdown_sha256'],**coding.inventory_extra(r, codebook)))
print(json.dumps({'corpus_entries':len(rows),'background_entries':len(verification),
                  'generated_tables':len([p for p in G.glob('table-*.tex') if p.name != 'table-gaps.tex']),
                  'source_index_sha256':stats['source_index_sha256']}))

gap_path = R / '06-data/gap-priority.csv'
if gap_path.exists():
    gaps = list(csv.DictReader(gap_path.open(encoding='utf-8-sig', newline='')))
    def priority(g):
        return (-int(g['evidence_maturity']), int(g['unvalidated_interface_count']), int(g['test_feasibility_grade']))
    assert [g['gap_id'] for g in sorted(gaps, key=lambda g:(priority(g),g['gap_id']))] == ['G1','G2','G3','G4']
    ranks = {key:i+1 for i,key in enumerate(sorted(set(priority(g) for g in gaps)))}
    lines = [r'\begin{table}[t]',r'\centering',
             r'\caption{Analytic prototype ordering. Maturity $m$: 2 denotes a relevant executed wheeled mechanism, 1 mainly complementary or boundary evidence for the distinctive failure setting. Interfaces $k$ are declared design links; feasibility grade increases with proposed instrumentation burden. Sort by descending $m$, then ascending $k$ and feasibility grade. These are reproducible judgments, not measured success scores.}',
             r'\label{tab:gaps}',r'\footnotesize',r'\begin{tabular}{@{}clccc@{}}',r'\toprule',r'Rank & Question & $m$ & $k$ & Feas. \\',r'\midrule']
    names = {'G1':'Localization to recovery','G2':'Semantic reasoning and fallback','G3':'Pose belief and terrain action','G4':'Partition, reunion, fault spread'}
    for g in gaps:
        assert int(g['priority_rank']) == ranks[priority(g)]
        lines.append(g['priority_rank']+' & '+tex(names[g['gap_id']])+' & '+g['evidence_maturity']+' & '+g['unvalidated_interface_count']+' & '+g['test_feasibility_grade']+r' \\')
    lines += [r'\bottomrule',r'\end{tabular}',r'\end{table}']
    (G / 'table-gaps.tex').write_text('\n'.join(lines)+'\n',encoding='utf-8')
