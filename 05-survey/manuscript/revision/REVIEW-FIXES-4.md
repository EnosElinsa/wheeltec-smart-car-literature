# Review fixes, round 4: evidence coding, positioning and wheeled evidence - November 5, 2026

This revision follows [REVIEW-FIXES-3.md](REVIEW-FIXES-3.md). It answers the remaining parts of the major items A1-A6 of the internal, simulated two-reviewer review of an earlier draft. That review is a local quality check prepared with language-model tools. It is not journal peer review. The selection stays at 245 works (244 technical studies and one context review). The background references grow from 20 to 25 and the bibliography from 265 to 270 entries.

The review refers to the draft of commit 5249a0f. Its "Table III" (synthesis) is now Table V, its "Table IV" (evidence map) is now Table VI, and its "Table V" (interfaces) is now Table VII. The supplementary module tables are again Tables S3-S7, after the new venue-mix table S1 and the selected-results table S2.

This record covers the evidence coding and its integration into the main paper and the supplement (Groups 1 and 2 of the round and the remaining A1 items). The minor items B10-B21, the AI-use acknowledgment, the audits and the documentation counts follow in a later section of this record.

## Author decisions

- **Second coding.** An independent language-model coder on a different model double-codes a stratified random sample of about 40 works, without access to the primary codes. The manuscript states that this is a language-model second coding and not human inter-rater reliability.
- **Standards without a DOI (decision A, 2026-11-04).** ISO 21448:2022 is cited as an IEEEtran `@standard` entry that carries only the fields shown on the official ISO catalogue page. SAE J3016 has a Crossref DOI record and follows the existing pattern. The decision is recorded in [background-staging.json](background-staging.json).
- **Screening model.** The model, version and prompts of the language-model screening are not supplied. The manuscript describes the screening from the archived records and states that no record names the model or its version.

## Evidence coding (A2, A4, A3 data)

The coding layer is in [06-data/evidence-coding](../../../06-data/evidence-coding/README.md). It was built in five earlier commits of this round: the codebook v1.0 with the pre-registered sample draw and interface-ranking rule (be0a73f, 67872f4), the primary codes of all 245 works with a source location for every coded value that asserts presence (64531cd), the page-located correction of 117 light-card values (69c8711), and the language-model second coding with agreement and adjudication, which led to codebook v1.1 (a7ecaf3).

- **Coding unit.** The publication. A combined attribute counts only when both parts come from one experiment (trial set, table or figure). The any-experiment version is a sensitivity row.
- **Three classes per source.** D1 injected or varied against a comparator, D2 selected for its difficulty without manipulation (including a single-level injection), D3 incidental. "A named degradation condition" means D1 or D2.
- **Nine sources, five groups, six assumptions.** Perceptual degradation and sensor or association faults (A1), terrain and wheel-ground contact (A2), moving agents and map change (A3), learned and semantic inference error (A4, a new fifth source group), communication loss, delay and bandwidth (A5), actuator faults and computation or energy limits (A6).
- **Platform groups.** Target wheeled robot 172, road vehicle 12, other ground robot 13, non-ground, handheld, mixed or unspecified carrier 47 (technical works).
- **Second coding.** 40 works, 8 per principal section, seed 20261105. Before adjudication, kappa over the 13 double-coded attributes has a median of 0.81 (range -0.04 for the drivetrain-dependent effect to 1.00 for incidental sources, which both coders set in the same 3 of 360 source flags). The 112 differing values were resolved with 58 primary values kept, 46 second values adopted and 8 revised in both. The headline count moved from 81 to 80.

## Manuscript changes by item

| Item | Change | Location |
|---|---|---|
| A2 codebook, classes, unit | Sec. III states the codebook, the publication unit with the same-experiment rule, the three classes and the second coding with its kappa range and median, plus the sentence that this is agreement between language-model passes and not human inter-rater reliability. Supplement S6 describes the codebook, S7 the second coding with Table S11. | Sec. III; S6, S7 |
| A2 evidence map | Table VI is rebuilt from the final codes with the publication count and 17 attribute rows in five groups: measurement level, degradation evidence (named, D1, D2 only, D3 only), same-experiment combinations (named, D1, physical, target wheeled), assessment and resources, platform group. The note replaces "need not come from the same experiment" by the same-experiment rule. Column percentages are in Table S8 and `generated/evidence-map.csv`. | `build_data.py`, Table VI, Table S8 |
| A2 headline and sensitivity | IX-A defines the classes. IX-B gives the per-function shares (LOC 1%, MRC 24%, REL 40%, SEM 44%, PLN 64%), the D1 and physical counts, and the share under alternative definitions (D1 with nominal level 5%, any experiment 34%, card-level coding of the earlier draft 25%), assessment depths (30%, 38%, 30%) and platform groups (40% wheeled, 17% other). Table S10 lists 36 sensitivity rows with the four pre-registered robustness findings. | Sec. IX-A, IX-B; Table S10 |
| A2 abstract and conclusion | Both give the per-function range (1 of 67 localization studies to 36 of 56 planning studies) with the pooled share qualified as a statistic of the purposively selected sample. The conclusion adds the physical-robot count (38) and the wheeled-subset share (40%). | Abstract, Sec. XI |
| A4 source per work | Every work carries its addressed sources. 219 of the 244 technical works address at least one coded source. | `primary-codes.csv`, `generated/evidence-codes.csv` |
| A4 matrix | Fig. 1 is now the degradation-source by function matrix (`fig-matrix`, 516 x 244 pt, drawn by `fig_matrix` from `generated/degradation-function-matrix.json`). Rows group the nine sources by assumption. Cells give addressed, named and D1 counts, the platform-group split (W, R, G, N) and shading by the strongest evidence setting. The right column links each assumption to its response families. Table S9 lists the works of every cell. The old taxonomy figure (`fig-taxonomy`) was removed. | Sec. II-B, Fig. 1, Table S9 |
| A4 assumptions listed once | The six assumptions are listed in Fig. 1, which II-B introduces. The abstract and Sec. I describe the organization by sources, assumptions and evidence. | Abstract, Sec. I, II-B |
| A4 multi-cell rule | A work appears in every source row it addresses but only in the column of its principal section (Fig. 1 caption, S6). | Fig. 1, S6 |
| A3 derivation | The Sec. X opening states the pre-registered ranking rule (function pair with one coupling source, sorted by works without direct joint wheeled evidence). Interfaces 1-4 rank 4, 9, 12 and 1 of 32 eligible candidates, and 4, 7, 9 and 1 without the integration-questions stage. The text says that the interfaces remain an agenda proposed by this survey rather than the four highest-ranked candidates. | Sec. X opening, S8 |
| A3 rejected candidates | Seven candidates rank above Interface 3 without being developed. Six are merged into Interface 4 (team communication, two shared-state fault candidates, teammate perception) or Interface 2 (moving agents in semantic choices, learned decisions). One (actuator faults inside one tracking controller) is named in X-E. The internal review's alternatives rank below Interface 3 or fall outside the function pairs (human assistance, 10 works). Reasons are in [data/interface-decisions.json](../data/interface-decisions.json) and Table S13. Function-pair co-occurrence is Table S12. | Sec. X, S8, Tables S12-S13 |
| A3 traceability | Table VII gives each interface its coded works and direct joint wheeled works (15/1, 11/5, 6/1, 17/0). `generated/interface-traceability.csv` lists the contributing works with platform group and evidence level. | Table VII, X-A-D |
| A3.5 positioning | X-A relates Interface 1 to the minimum risk maneuver of automated driving. | Sec. X-A |
| A5 drivetrain | New Table II (`tab:drivetrain`) gives, per drive, the violated kinematic model with references to Eqs. (1)-(3), the degradation effect and the remaining recovery motions, citing the six works coded with a drivetrain-dependent effect. It absorbs the II-A slip sentences and X-E(5). | Sec. II-A, Table II |
| A5 platform groups | The evidence data and Table VI split the four platform groups. The supplementary module tables replace the single dagger by the marks R, G and N. S2 gives the group counts. | Table VI, Tables S3-S7, S2 |
| A5 wheeled basis in Sec. X | Each of X-A-D states its direct wheeled evidence: one study for Interface 1 (the integrity analyses rest on road-vehicle data), five for Interface 2, one for Interface 3 (an OpenStreetMap-grounded navigator that is direct through injected map deviations, which leaves the terrain-pose question with extrapolated evidence only, while the terrain planners do not code localization), none for Interface 4 (its 12 target wheeled works name conditions only in recorded data, replay, online estimation or simulation, if at all). | Sec. X-A-D |
| A5 transfer criteria | Sec. III states when non-wheeled studies are included: their mechanism's inputs exist on a wheeled robot, its assumptions do not rest on the other embodiment, and the evaluation isolates the mechanism. | Sec. III |
| A6 Table I | Rebuilt from [data/related-surveys.json](../data/related-surveys.json) into `generated/table-related-reviews.tex`. Columns: survey and year, platform scope, degradation coverage, recovery or faults, evaluation practice, each taken from the survey's abstract. "Not stated" means that the abstract does not name the topic. Years covered are omitted because the surveys do not state them uniformly. A row for this survey is added. Each row records the URL of its abstract basis (`basis_url`). | Sec. I, Table I |
| A6 search and characterization | Sec. I states how the related surveys were found (targeted searches per function and suggestions of the internal review, not a systematic search), corrects the characterization of the foundation-model survey, and states that the learned-navigation review is also the corpus context review. The traversability-risk review named by the internal review is added. | Sec. I |
| A6 automated driving | A new Sec. I paragraph positions the survey against SAE J3016, ISO 21448 (SOTIF), operational design domain monitoring (defined in one clause) and minimum risk maneuvers (in the terms of the cited study), and states what transfers to wheeled robots and what does not. | Sec. I |
| A1 screening record | Sec. III states that all 220 archived screening decisions of later candidate searches name Codex as reviewer and host, that all but four state a title-and-abstract relevance policy, that part of them record read scope and eligibility gates, and that no record names the model or its version. S1 gives the counts. | Sec. III, S1 |
| A1 venue mix | Table IV (selection) has an IEEE column. Table S1 gives venue type and publisher by stage. The two IEEE-only stages are described neutrally (their records state no reason for the restriction). IEEE works form 72% of the corpus and 64% outside these stages. | Sec. III, Table IV, S1, Table S1 |
| A1 works list | `generated/corpus-inventory.csv` now holds selection stage, stage label, principal section, venue, publisher, publication type, DOI and platform group for every work. `verify_delivery.py` checks the stage, section and group columns. S6 names the list among the released data. | `generated/corpus-inventory.csv`, S6 |
| A1 robustness | The headline share stays between 31% and 34% when any one stage is removed, is 33% in the quota stages against 32% elsewhere, and ranges from 23% to 45% across year bands. Localization keeps the lowest share and planning the highest in every stage, depth and quota subset. | Sec. IX-B, Table S10, S6 |

## Qualitative statements changed by the new codes

The evidence map now rests on the final codes, not on the card fields of the earlier rounds. Five synthesis statements changed:

| Location | Before (card fields) | After (final codes) |
|---|---|---|
| Sec. IV | only 2 of 67 report a task outcome | only 1 of 67 reports a task outcome |
| Sec. V | nearly all report task outcomes, fewer than half under a named condition | task outcomes under a named condition in the same experiment more often than in any other function (36 of 56) |
| Sec. VI | nearly every study reports task outcomes, fewer than a third under a named condition | most report task outcomes (32 of 36), fewer than half in the same experiment (16 of 36) |
| Sec. VII | more than a quarter (13 of 45) | fewer than a quarter (11 of 45), 2 on physical robots |
| Sec. VIII, IX-B | fault management has the largest share | planning and control has the largest share (64% against 40%) |

Pre-registered findings RF2 (fault management highest) and RF3 (task outcomes in at least 90% of planning and semantic works) fail under the final codes. RF1 and RF4 hold under every definition and in every stage, depth and quota subset. Supplement S6 says so. `build_data.py` asserts each new statement, with a comment naming its sentence.

## Background references

Five records join `background-verification.json` in the commit that first cites them (all dated 2021-2026, so the seven pre-2021 foundational exceptions are unchanged):

| Key | Source | Cited in |
|---|---|---|
| `B_DrivingAutomation2021` | SAE J3016_202104, 10.4271/j3016_202104 (Crossref type standard) | Sec. I |
| `B_SOTIF2022` | ISO 21448:2022, official ISO catalogue page, no DOI (decision A) | Sec. I |
| `B_ODDMonitoring2021` | Alsayed, Resende and Bradai, ICAR 2021, 10.1109/icar53236.2021.9659362 | Sec. I |
| `B_MRMFallback2025` | Atoui and Resende, IEEE IV 2025, 10.1109/iv64158.2025.11097617 | Sec. I, X-A |
| `B_TraversabilityRisk2024` | Benrabah et al., Sensors 24(6) 1909, 2024, 10.3390/s24061909 | Sec. I, Table I |

The Crossref records were saved without their cited-reference lists. Fifteen background records committed in earlier rounds still hold a Crossref `reference` list. They were left unchanged and are reported here for an author decision.

## Page budget

The main paper stays at 24 pages. The additions (Table II, the automated-driving paragraph, the coding and screening text of Sec. III, the IX-B sensitivity paragraph, the Sec. X derivation and wheeled-basis sentences) were paid for by removing repetition, with every citation key kept in prose:

- Sec. I: the uncited list of sensing conditions, the semantic-navigator sentence, the long roadmap paragraph, and the 11-row Table I with free-text cells (now one-line objective cells).
- Sec. II: the drivetrain descriptions and slip sentences now carried by Table II, the representation sentences, the closing CBF sentences repeated in IX-D, the representative-system sentences repeated in Sec. I, and the four source-example sentences now carried by Fig. 1.
- Sec. III: the stage narrative that Table IV repeats and the closing paragraph that repeated Sec. I.
- Secs. IV-IX: synthesis sentences that restated Table VI, the V-A dataset descriptions that Table III repeats, and IX-C/IX-D examples that re-described works of Secs. IV-VIII.
- Sec. X: re-descriptions of works reviewed in Secs. IV-VIII, and X-E condensed from five subsubsections (418 words) to one paragraph.
- Fig. 1 is 244 pt high against 293.8 pt for the old taxonomy figure.

Prose words outside floats (counted as in the baseline of the round plan, commands and braces removed), base 8cdfaea to now: I 570 to 773, II 1,124 to 887, III 370 to 627, IV-VIII 6,542 to 6,484, IX 1,326 to 1,452, X 1,452 to 1,193, XI 274 to 283. The abstract has 249 words.

## Scripts

- `build_data.py`: the evidence map, macros and Table VI come from the final codes. New macros cover per-function shares, sensitivity values, interface ranks and traceability counts, IEEE counts per stage and the agreement summary. Table I is generated from `data/related-surveys.json`. The module tables use platform-group marks. The assertions guard every qualitative statement on the codes.
- `verify_delivery.py`: 29 main labels (adds `tab:drivetrain`; `fig:taxonomy` became `fig:matrix`) and 22 supplement labels. The expected set of supplement references from the main text is listed explicitly. The evidence map is recomputed independently from `primary-codes.csv` plus `adjudication-log.csv` and compared with `stats.json`, `generated/evidence-codes.csv` and the rows of Table VI. The script also checks the freeze hashes, the sample redraw, the agreement recomputation and the new inventory columns, and reports `coding` and `second_coding` blocks.
- `build_figures.py`: `fig_matrix` replaces `fig_taxonomy`. Fig. 2 gains the fifth source tag (learned and semantic inference), and its legend no longer refers to Fig. 1 numbering.
- `coding.py`: the agreement-table caption and note are split into shorter sentences.

## Length and verification of this part

- `build_data.py`, `build_figures.py`, `latexmk -gg` of the supplement and the main paper, `verify_delivery.py` and `--sources` pass: 24 pages, 245 corpus citations in prose, 270 resolved references, 29 labels, three figures, seven tables, six unchanged equations, a 17-page supplement with 22 labels, and 741 source artifacts with no hash mismatch. Neither log has an Overfull, undefined or LaTeX Warning line.
- The last page is balanced by `\IEEEtriggeratref{256}`: references 240-255 end at 658 pt and 256-270 at 667 pt.
- All 245 corpus keys and 25 background keys are cited in prose outside floats. The house-style scan of new or changed sentences, captions and table cells is clean, and captions name no colors. Sentence rhythm: 457 sentences, mean 23.3 words, 13.8% under 12 words. The style fingerprint shows no flags.
- Library checks pass: pytest, `build_tables --strict`, `build_indexes --strict`, `check_links` and `check_public_tree --cjk strict`.

## Fixes after the first manuscript check of this part

A local check of the commit above (simulated reviewer, not journal peer review) found sentences that said more than the data behind them. Each finding was fixed as follows.

| Finding | Fix | Location |
|---|---|---|
| 1. Table II note contradicted its citations | The note now reads that, except for the Mecanum studies, corpus citations mark works coded with a drivetrain-dependent effect. `build_data.py` asserts that exactly E02, R33, M39, E04, S07 and N17 carry the effect and that M09 and S48 do not. | Table II |
| 2. Merged-candidate summary | The Sec. X opening lists the six merged candidates by interface: Interface 4 takes team communication, shared-state faults and teammate perception, Interface 2 takes moving agents in semantic choices and learned decisions. `build_data.py` asserts the candidate-to-interface map. | Sec. X opening |
| 3. Screening-policy count | Sec. III says that all 220 archived decisions name Codex as reviewer and host, with a relevance policy stated in all but four, as S1 does. | Sec. III |
| 4. Source-location overclaim | Sec. III limits the locations to values read from a paper and derives platform group and drivetrain from the platform class. S3 adds that platform group, drivetrain, strongest evidence setting, integrity assessment and computation placement follow card fields without a location, and no longer names transcription passages (no final locator uses one). The 06-data README says the same. | Sec. III, S3, `06-data/evidence-coding/README.md` |
| 5. Extrapolated evidence for Interfaces 3 and 4 | X-C says that the single direct study of Interface 3 is direct through injected map deviations rather than pose uncertainty, which leaves the question with extrapolated evidence only. X-D says that the 12 target wheeled works of Interface 4 name conditions only in recorded data, replay, online estimation or simulation, if at all. Both statements are asserted (`M10` D1 on MAP, the level set of the 12 works). | Sec. X-C, X-D |
| 6. Direct-evidence definition | The definition sentence now reads "a named condition of any source". | Sec. X opening |
| 7. All-works list | S6 names the list of all 245 works with selection stage, principal section, venue, publisher and platform group among the released data. | S6 |
| 8. Table I cells | The Firoozi row gives "Not stated" for platform scope, since its abstract names no platform. Every row of `data/related-surveys.json` now has a `basis_url`: the Semantic Scholar paper page for the eight abstracts taken from that index (paper ids confirmed against the Graph API on 2026-11-05) or the Crossref API record for the four deposited abstracts. `build_data.py` asserts the field. | Table I, `data/related-surveys.json` |
| 9. Abstract rank phrasing | The abstract gives each interface its rank (4, 9, 12, 1) among 32 candidate pairs of functions coupled by one source. Three short cuts keep it at 249 words. | Abstract |
| 10. Kappa range endpoints | Sec. III names both ends: -0.04 for the drivetrain-dependent effect and 1.00 for the rarely coded incidental sources. S7 adds that both coders set the same 3 of 360 incidental-source flags. New macros `IncidentalFlags` and `IncidentalUnits` come from the second codes and the frozen primary codes, with assertions on the maximum and the prevalence. | Sec. III, S7 |
| 11. Wording | Sec. I defines the operational design domain in one clause and uses the cited study's terms (minimum risk maneuver, minimum risk condition) in Sec. I and X-A. The recorded J3016 abstract does not contain the term "minimal risk condition", and the text therefore no longer pairs it with the cited study. Sec. III reads "a stratified random sample of 40 works". The Sec. V-F synthesis gives its comparator ("more often than the studies of any other function"). X-E says that human assistance is noted outside the ranked function pairs. S7 names the two rules of codebook v1.1 (primary response family only, narrowed drivetrain-dependent effect). | Sec. I, III, V-F, X-A, X-E, S7 |
| 12. Carry-forward | The acknowledgment, the numeric and claim audits and the remaining page budget stay with the next part of this round (see below). | |

The additions were paid for by cuts of repetition, with every citation key kept: the Sec. X sentence that repeated the Table VII caption (the table reference moved into the first sentence), the II-B sentence that repeated the Fig. 1 caption, a shorter II-B signpost to Fig. 2, and the X-D clause that repeated Table VII. The Table VII float is now defined before the Sec. X opening paragraph, which keeps it at the top of the page after the section heading. The main paper stays at 24 pages, and the last page keeps its balance (references 240-255 end at 658 pt, 256-270 at 667 pt, `\IEEEtriggeratref{256}`). Page 2 ends about three lines short in its right column, since the II-B heading now starts page 3.

## Still open in this round

- Minor items B10, B11 (references to Eqs. (4)-(6)), B14, B15 (reporting checklist), B16 (synthesis-table citations and placement), B18, B19 check, B20 and B21.
- The AI-use acknowledgment, which must also name the language-model primary coding, second coding and adjudication.
- The short-sentence share is 13.8% against the 14% limit, and each last-page column has about 80 pt free, which the checklist table and the acknowledgment must not exceed without matching cuts.
- Numeric, claim and overlap audits for the new and changed sentences, and the README and document counts.
