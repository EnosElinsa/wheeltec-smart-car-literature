# Review fixes, round 4: evidence coding, positioning and wheeled evidence - November 5, 2026

This revision follows [REVIEW-FIXES-3.md](REVIEW-FIXES-3.md). It answers the remaining parts of the major items A1-A6 of the internal, simulated two-reviewer review of an earlier draft. That review is a local quality check prepared with language-model tools. It is not journal peer review. The selection stays at 245 works (244 technical studies and one context review). The background references grow from 20 to 25 and the bibliography from 265 to 270 entries.

The review refers to the draft of commit 5249a0f. Its "Table III" (synthesis) is now Table V, its "Table IV" (evidence map) is now Table VI, and its "Table V" (interfaces) is now Table VII. The supplementary module tables are again Tables S3-S7, after the new venue-mix table S1 and the selected-results table S2.

This record covers the evidence coding and its integration into the main paper and the supplement (Groups 1 and 2 of the round and the remaining A1 items). The minor items B10-B21, the AI-use acknowledgment, the audits and the documentation counts are recorded in the section "Second part: minor items, acknowledgment and audits" below. That part moves Table V into Section IX and adds a checklist as Table VII, so the interface table called Table VII in the first part is now Table VIII.

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
| A5 wheeled basis in Sec. X | Each of X-A-D states its direct wheeled evidence: one study for Interface 1 (the integrity analyses rest on road-vehicle data), five for Interface 2, one for Interface 3 (OPEN, which completes a GPS-disabled campus delivery with no pose-uncertainty term in its traversability cost, which leaves the terrain-pose question with extrapolated evidence only, while the terrain planners do not code localization), none for Interface 4 (its 12 target wheeled works name conditions only in recorded data, replay, online estimation or simulation, if at all). | Sec. X-A-D |
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

## Fixes after the second manuscript check of this part

A second local check of the two commits above (simulated reviewer, not journal peer review) found that the X-C fix for finding 5 named the wrong experiment, plus four wording slips. Each finding was fixed as follows.

| Finding | Fix | Location |
|---|---|---|
| 1. Interface 3's direct study | OPEN (M10) is direct through its GPS-disabled campus delivery, a perceptual condition (adjudication log, PDF p. 11 and p. 8). Its injected map deviations were tested in simulation only (PDF p. 10, Table III). X-C now says that OPEN completes a GPS-disabled campus delivery with no pose-uncertainty term in its traversability cost, which leaves the question with extrapolated evidence only. The traversability cost of its local replanner comes from image segmentation (paper Sec. IV-F). `build_data.py` now asserts `src_selected` = PER, `deg_task_setting` = physical and `level_degradation` = P for M10 in place of the map-deviation codes. The claim ledger of this part carries the corrected basis. | Sec. X-C, `build_data.py` |
| 2. Sentence on the operational design domain | Split in two. Runtime monitors and fallback maneuvers turn these notions into checks and actions during operation. A check of the operational design domain, the conditions that an automated function is designed for, can flag laser scans unsuitable for matching. The first sentence has 14 words, which keeps the short-sentence share unchanged. | Sec. I |
| 3. Table II note on N17 | The note now names the wheel repositioning that reshapes the support polygon (N17 card, pp. 2-5), the case that codebook v1.1 keeps at `yes`, in place of stepping. It uses the source's term "wheeled-legged". | Table II |
| 4. Platform groups "marked in Table VI" | Sec. III says that the platform group is counted in Fig. 1 and Table VI and marked in the supplementary implementation tables. | Sec. III |
| 5. "Part of them also record" | Now "Some also record". | Sec. III |
| 6. Carry-forward | Passed to the next part of this round, as listed below. | |

The X-C sentence names OPEN, which VI-B introduces, in place of a descriptive phrase. This keeps the X-C paragraph at its earlier line count. A first version with the longer phrase moved one line onto page 17 and four references onto page 24, which made a 25th page. The main paper keeps 24 pages and the last-page balance of the first fix pass (references 240-255 end at 658 pt, 256-270 at 667 pt, `\IEEEtriggeratref{256}`).

## Second part: minor items, acknowledgment and audits

The second part of the round (commit "Survey: minor review items, AI-use acknowledgment, audits and round-4 record") applies the minor items B10-B21, both non-blocking findings of the third manuscript check, the AI-use acknowledgment, the numeric, claim and overlap audits, and the documentation counts.

**Numbering after this part.** Table V (responses by function) is now defined at the start of Section IX, where it is first cited. The new reporting checklist is Table VII in IX-F. The interface table of Section X is Table VIII (Table VII in the first part of this record). Tables I-IV and VI keep their numbers.

| Item | Change | Location |
|---|---|---|
| B10 type size | Every text element of Figs. 2 and 3 and Fig. S1 is now set at 7 pt or larger (was 6.2-6.8 pt). The dashed source tags are 1 pt taller. Fig. 3 data labels are upright, with italic kept only for the lane tags. Its task-measure label wraps to two lines clear of the recovery line. Figure heights are unchanged (Fig. 2 224 pt, Fig. 3 202 pt, Fig. S1 150 pt), and grayscale renders were checked. | `scripts/build_figures.py`, Figs. 2, 3, S1 |
| B18 Fig. 2 | The Representation box names Sections IV and V. A dashed link runs from State estimation below the Representation box to Planning and carries marker 3, so Interface 3 is shown as pose uncertainty passed to planning. | Fig. 2 |
| B11 equations | `\eqref` now ties each equation to the prose that uses it: (1) SE2-LIO in IV-C, (2) time-of-flight-wheel odometry in IV-C, (3) memory-event-triggered MPC in V-E, (4) pose uncertainty in X-C, (5) the LiDAR barrier filter in V-D and the barrier proof in IX-D, (6) EKF-SLAM integrity in VIII-B and the alert-limit row of Table VII. Table II keeps its references to (1)-(3). The six equations are byte-identical (hash baseline in `verify_delivery.py`). | Secs. IV, V, VIII, IX, X, Table VII |
| B14 metrics | II-C defines SPL as the episode mean of the shortest path length divided by the longer of the shortest and executed paths, with zero for a failed episode. VI-A uses it once: VLFM reaches 52.5% success and 30.4% SPL on simulated HM3D object search, where success means stopping within 1 m of a target instance in at most 500 steps (PDF p. 5, Table I; p. 2). IV-A states that APE is an ATE from the EVO tool for which the LODESTAR paper states no alignment or summary statistic (PDF p. 5; p. 7, Table V). | Sec. II-C, IV-A, VI-A |
| B21 density | Sentences that chained three or more studies or exceeded 45 words were split in IV-A, IV-C, IV-E, V-B, V-D, V-F, VI-B, VII-B, VII-C and VIII-B. In Sections IV-IX, outside floats, "whereas" falls from 32 to 29 and "although" from 15 to 11. Coined terms are replaced: "shared-state acceptance" by "accepting shared data after reconnection" (abstract, Table VIII), "assignment age" by "the age of team assignments", "conditional map repair" by "estimate repair after reconnection" (Table V). The VII-C heading is now "Rendezvous, Disconnection, and Reconnection" and the X-D heading "Reconnection and Corrupted Shared Information". "Embodiment filter" stays, since VI-C defines it at first use. Several short sentences were joined with a neighbor to keep the short-sentence share within the band. | Secs. III-X, abstract |
| B15 checklist | New Table VII lists 13 reporting elements of a joint evaluation of detection and response: fault model, onset and duration, severity, trial unit, denominator, reference, alarms with the alert limit, event times, detection-to-action delay, computation, controls, executed response and task outcome. The three list sentences of IX-F moved into it (cut C9). `verify_delivery.py` now expects 30 main labels. | Sec. IX-F, Table VII |
| B16 synthesis table | Table V moved from Section VIII to the start of Section IX, before its first citation. Each cell cites two to four representative works that Sections IV-VIII discuss with the property the cell names, and the cell wording is shorter (cut C10). | Sec. IX, Table V |
| B19 check | X-E no longer repeats Section IX or Table VIII. Its opening sentence on benchmarks with controlled severity, which IX-F covers, was removed. | Sec. X-E |
| B20 workflow terms | The supplement no longer says "the library", "evidence cards", "explicitly derived", "official-title/PDF-title variant" or "provenance exceptions remain visible". The sentences now speak of the works already selected, two assessed studies from before 2021, reading records, citation entries rewritten from the publisher's citation file (kept unchanged), a title that differs between publisher page and PDF, and citation changes recorded in the public data. | Supplement S1, S2, S3 |
| Third check, finding 1 | "Their single direct wheeled study" now reads "The single direct wheeled study". | Sec. X-C |
| Third check, finding 2 | The acknowledgment names the language-model coding, the audits carry the claim ledger of the first part, and the short-sentence share and last-page balance hold (see below). | Acknowledgment, audits |

### AI-use acknowledgment

The acknowledgment now reads, in substance: language-model tools screened candidate titles and abstracts (Section III), with the agent Codex named in all archived decisions, and drafted the corpus reading records in Codex and Kiro sessions. Kiro workflow sessions drafted and revised the manuscript and supplement, prepared the internal review of an earlier draft that named the final-stage works, performed the primary evidence coding of Section III with the model claude-opus-5.5, and adjudicated coding differences. The second coding ran in a separate Kiro session with the model gpt-5.6-sol. MinerU and the OXR-1.0 model transcribed the publisher PDFs, with PyMuPDF4LLM extraction for some batches. No record names the model behind the other Codex and Kiro sessions. The authors reviewed all such output and take full responsibility for the content.

Sources of each statement: the screening archive (reviewer and host `codex` in all 220 decisions), the review-card logs (`host: Codex`, `host: Kiro`), `06-data/evidence-coding/second-coder-record.json` (both coding models, taken from the workflow configuration), `06-data/fulltext-manifest.json` (MinerU), the `markdown-extraction.json` records of the S and R batches (OXR-1.0 through vLLM) and the `source-reading.json` records of the N and K batches (PyMuPDF4LLM 0.2.9).

**Uncertainties for the author to resolve before submission:**

1. **Vendor names.** The records name the agents Codex and Kiro but not their vendors, and the acknowledgment names none. IEEE asks for the AI system used. Add vendor names if the author wants them.
2. **Models of the other sessions.** No record names the model behind the screening sessions, the card-drafting sessions, the earlier manuscript drafts or the earlier internal review. The acknowledgment says so instead of guessing.
3. **Source of the two coding models.** claude-opus-5.5 (primary coding) and gpt-5.6-sol (second coding) come from the workflow configuration recorded in `second-coder-record.json`. The second coder's own notes exposed no model identifier. The model of the adjudication session is not recorded and is not named.
4. **Author review of the codes.** The last sentence says that the authors reviewed all such output. No record shows an author review of the 245 primary codes, the adjudication log or the second-coding sample. The author must confirm this or ask for the sentence to be narrowed.
5. **PyMuPDF4LLM.** It is a text-extraction library rather than a language model. It is named because the brief listed it. Remove it if the acknowledgment should cover AI systems only.
6. **Earlier drafting hosts.** The acknowledgment attributes manuscript drafting and revision to Kiro workflow sessions, as the round plan records. If earlier manuscript versions were drafted in Codex sessions, the sentence should name them too.
7. **Internal checks of this round.** The simulated manuscript checks of this round and the planned re-review are Kiro sessions as well. The acknowledgment names only the internal review that named the final-stage works.

### Pre-existing Crossref reference lists

Fifteen committed files in `revision/background-sources/` still hold a Crossref `reference` list: B_CBF2017 (58 entries), B_Cadena2016 (267), B_Campion1996 (27), B_DWA1997 (16), B_FASTLIO22022 (65), B_Foundation2024 (262), B_Habitat2019 (28), B_HumanAware2013 (106), B_KITTI2012 (48), B_Nav22020 (25), B_Nav22020-corrected (25), B_ORBSLAM32021 (83), B_TEB2013 (22), B_TUM2012 (47) and B_Traversability2022 (86). The public-tree rule of this round forbids committing Crossref reference lists, and the five records added in this round omit them. These fifteen files predate the round and were left unchanged for an author decision (strip the `reference` field and update the recorded hashes, or keep them).

### Audits

- **Numeric audit** ([numeric-audit.json](numeric-audit.json)): 29 numerical result sentences in Sections IV-X, 10 of them in checked comparison records, 18 with a page locator, 0 mismatches. The new VLFM numbers were read on PDF pp. 2 and 5. A `round4_changes` list records the removed, merged, shortened and added numerical sentences of both parts of the round, including the screening-archive counts of S1.
- **Claim audit** ([claim-audit.json](claim-audit.json)): 64 critical characterizations re-extracted from the current text. The 10 round-4 corrections join the 9 earlier ones: the statements on the evidence map that changed under the final codes (abstract, Sections I, IV-IX, XI, S1, the Section X opening) and the corrected X-C basis for OPEN (GPS-disabled campus run, PDF p. 11 and p. 8, in place of the simulation-only map deviations). `round4_claims` lists 29 new or changed characterizations of the round with their basis: the Table II drivetrain effects, the direct-evidence statements of X-A to X-D, the background positioning of Section I, the screening and kappa statements of Section III, the VLFM and APE statements, the equation references, the Table V citations and the B21 splits. A further list records the removed or regrouped claims.
- **Overlap audit** ([overlap-report.json](overlap-report.json)): no exact ten-word phrase is shared between the survey and the 267 public source documents (11,166 survey windows).

### Page budget of the second part

The additions (Table VII, the Table V citations, the larger figure type, the equation references, the SPL definition and the VLFM numbers, the APE clause and the longer acknowledgment) were paid for by removing repetition, with every citation key kept in prose:

- IX-F: the three list sentences now carried by Table VII, and the comparison sentence shortened to a reference to the table (cut C9).
- IX-A and IX-B: the sentence that lower error can help explain a task result, the class definitions that repeat Section III, and the integrity-count clause that repeats VIII-E.
- IX-C to IX-E: the simulation-to-outdoor drop of terrain-adaptive MPC (stays in V-A), the small-sample sentence (contingency cut K4, its works stay cited in VI-A and VI-C), and the timing examples that repeat VI-D (cut C12).
- Table V cells and Table VIII row 1 shortened (cuts C10 and C11).
- Sec. I "The main contributions ... are summarized as follows" (part of contingency cut K5), the Sec. II-B signpost to Fig. 2, the Sec. III list of foundational examples, the X-E opening sentence, and a few words in IV, VIII, X and XI that removed one-word last lines.
- The X-D heading now fits on one line.

Prose words outside floats, from the first part of the round to now: I 742 to 736, II 788 to 790, III 620 to 609, IV 1,444 to 1,460, V 1,459 to 1,468, VI 1,185 to 1,210, VII 1,149 to 1,149, VIII 985 to 986, IX 1,406 to 1,206, X 1,132 to 1,118, XI 281 to 280. The abstract has 250 words.

### Length and verification of the second part

- `build_data.py`, `build_figures.py`, `latexmk -gg` of the supplement and the main paper, `verify_delivery.py` and `--sources` pass: 24 pages, 270 resolved references, 30 labels, three figures, eight tables, six unchanged equations, a 17-page supplement with 22 labels and 13 tables, and 741 source artifacts with no hash mismatch. Neither log has an Overfull, undefined or LaTeX Warning line.
- The last page is balanced by `\IEEEtriggeratref{256}`: references 240-255 end at 658 pt and 256-270 at 667 pt.
- All 245 corpus keys and 25 background keys are cited in prose outside floats. The house-style scan of new or changed sentences, captions and table cells is clean, its listed ", and" joins are list joins, and captions name no colors. Sentence rhythm: 451 sentences, mean 23.4 words, 11.3% under 12 words. The style fingerprint shows no flags.
- Library checks pass: pytest, `build_tables --strict`, `build_indexes --strict`, `check_links` and `check_public_tree --cjk strict`.

## Still open after this round

- The author decisions above: the acknowledgment wording and its uncertainties, and the fifteen pre-existing Crossref reference lists.
- The fresh simulated re-review and its comparison with the earlier major items follow as a separate local step and are not part of this record.
- Author information and submission declarations remain incomplete.
