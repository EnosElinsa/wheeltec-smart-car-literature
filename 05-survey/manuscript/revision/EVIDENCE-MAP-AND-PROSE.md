# Evidence map and prose restructuring - November 4, 2026

This record describes the state after this revision. [ROADMAP-AUDIT-AND-SURVEYS.md](ROADMAP-AUDIT-AND-SURVEYS.md) supersedes its reference count (now 238), table and label counts, Section X description and style measurements.

This revision follows [PAGE-LIMIT-AND-FIGURE-STYLE.md](PAGE-LIMIT-AND-FIGURE-STYLE.md). It turns the corpus coding into a cross-function evidence map, states what the map shows in the main text, and restructures the citation-chain sentences of Sections IV-IX. The selection is unchanged: 229 selected works and 5 background references, 234 references in total, all from 2021-2026.

## Evidence map (Table IV)

Table IV (`tab:evaluation`) previously gave four overall counts. It now counts each evaluation attribute by the section that reviews each of the 228 technical publications:

| Attribute | IV | V | VI | VII | VIII | All |
|---|---:|---:|---:|---:|---:|---:|
| Publications | 66 | 52 | 30 | 40 | 40 | 228 |
| Component measures | 66 | 29 | 13 | 29 | 23 | 160 |
| Task outcomes | 2 | 49 | 29 | 26 | 22 | 128 |
| Degradation testing | 45 | 21 | 9 | 24 | 31 | 130 |
| Degradation testing with task outcomes | 2 | 19 | 8 | 13 | 17 | 59 |
| Integrity/reliability | 3 | 1 | 0 | 1 | 9 | 14 |
| Computation placement reported | 45 | 29 | 17 | 30 | 28 | 149 |

`scripts/build_data.py` computes the map from `survey_module`, `evaluation_all` and `compute_location` in the corpus coding, writes it to `generated/stats.json` and `generated/table-evaluation.tex`, and defines the macros used in the text (`\DegTaskCount`, `\DegTaskShare`, `\LocTaskCount`, `\LocTechCount`, `\LocDegCount`, `\IntegrityCount`, `\FaultIntegrityCount`). It also asserts every qualitative statement that rests on the map, such as "fewer than half" for designed degradation in Section V and "fewer than a third" in Section VI, so a coding change that falsifies a sentence stops the build. `scripts/verify_delivery.py` recomputes the map from the corpus rows, checks every generated table row, and records the map in the verification reports.

The most striking cells were spot-checked against the coding summaries, not against the PDFs: the seven localization studies with physical-robot evidence (only N19 and R11 report task outcomes), and the 21 semantic studies without designed degradation (their conditions are either absent or not reported per condition). No coding was changed.

## Where the map enters the text

- Section IX has a new subsection, "Evidence Across Navigation Functions", with three findings. Localization and mapping evidence stops at the estimate (all 66 studies report component measures and only 2 report a task outcome), whereas planning and semantic studies show the opposite profile. Only 59 publications (26%) report task outcomes under a designed degradation, with fault management having the largest share. Integrity or reliability assessment appears in 14 publications, 9 of them in Section VIII, and 79 publications do not report computation placement.
- The synthesis of each of Sections IV-VIII now ends with the evidence profile of that function.
- The abstract (now 243 words) and the conclusion each gain one sentence with the 26% figure.

## Prose

The citation-chain sentences of Sections IV-IX were regrouped so that each paragraph states the shared mechanism first and the differences after it. Evaluation caveats that Section IX already discusses were removed from Sections IV-VIII instead of being repeated after each method (for example the replay and communication-model caveats of R21, R22 and R23, and the duplicate simulation-to-hardware figures of R13). Workstation and cloud dependencies in Section VI are cited once, together. Two-clause ", and" joins introduced or left by earlier passes were rewritten.

| Measure (`scan.py`, Sections I-XI) | Before | After |
|---|---:|---:|
| Sentences with three or more citations | 48 (9%) | 30 (5%) |
| Longest such sentence | 54 words | 40 words |
| while/whereas per 1000 words | 8.9 | 7.9 |
| while/whereas in Section VII / VIII | 13.4 / 13.6 | 10.4 / 9.3 |

Sentence rhythm (`rhythm.py`): 549 sentences, mean 21.4 words, median 20, 10% under 12 words and 6% over 35 words, within the team band of 21.4-23.8 words and 9-14% short sentences. `style_fingerprint.py` gives a body mean of 21.0 words with 12% short and 6% long sentences and no flags against the house-style band. A first pass that only split sentences fell to a mean of 18.5 words with 16% short sentences, so the final text merges same-paper continuations and keeps comparisons in one sentence. The house-style scan finds no "so", "because", semicolon, ", but", "e.g.", "we", "our", "Hence" or "which means".

## Length

Sections I-XI grew from about 13,110 to 13,670 words. The main paper now has 24 pages, the T-IV maximum, with the last page balanced at 416 pt per column by `\IEEEtriggeratref{227}`. No page slack remains. The planned compression of Section X (a roadmap table and fewer "Broader Challenges" subsections) is the intended source of space for later additions.

## Verification

`python scripts/verify_delivery.py` and `python scripts/verify_delivery.py --sources` pass: 24 pages, 229 corpus citations in prose, 234 resolved references, 26 unique labels, three figures, four tables, six unchanged equations, no unresolved references, no overfull boxes and no LaTeX warnings. The supplement has eight pages and seven tables. The source mode checks 693 local artifacts with no hash mismatch. Table IV and the last reference page were checked visually.
