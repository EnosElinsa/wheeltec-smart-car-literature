# Review fixes, round 5: degradation evidence, interface ranks and drivetrain evidence - November 5, 2026

This revision follows [REVIEW-FIXES-4.md](REVIEW-FIXES-4.md). It answers the major comments M1-M4 and the minor comment m2 of a local, simulated re-review of commit f463649. One language-model reviewer prepared that re-review as a quality check. It is not journal peer review, and its report stays local. The locations it names still apply, since rounds 4 and 5 kept the section, table and figure numbering. The selection stays at 245 works (244 technical studies and one context review) with 25 background references and 270 bibliography entries.

The round has two commits. The first (3a39ce4, "round5 data") corrects evidence codes through the adjudication log and adds a consistency check of the final codes. The second ("round5 ms") changes the manuscript, the supplement, the table strings of the scripts, the audits and this record.

## Author decisions

- **M5 is not addressed.** No human audit of the codes was made. No sentence is added, in the abstract or elsewhere, about human validation of the codes. The existing statements of Section III and supplement S7, that the second coding is a language-model second coding and not human inter-rater reliability, stay unchanged.
- **Acknowledgment unchanged.** The acknowledgment of `survey.tex` is byte-identical to commit b3bf857.
- **Scope.** Only M1-M4 and m2 are addressed. The other minor comments stay for a later round (see "Still open").
- **M3 by a symmetric recheck.** The drivetrain-dependent effect was rechecked in the missed direction too (`no` to `yes`) for every work, not only by narrowing the text.

## Corrected codes

All corrections are rows of [adjudication-log.csv](../../../06-data/evidence-coding/adjudication-log.csv) with scope `review-recheck` and resolver `review-recheck Kiro session`. The frozen primary codes, locators, codebook and second codes are unchanged, and the first 119 lines of the log are byte-identical. Every locator is a physical PDF page that was read for this round. Pages with tables or plots outside the text layer were rendered and viewed.

**M4 level recheck.** The 19 works coded with physical evidence level `P` whose `deg_task_setting` is not physical were read on the page of their physical experiment. A work keeps `P` when a physical closed-loop run under one of its named sources reports a measured quantity of that run in the text, a table or a plotted measure. Video, photographs and trajectory overlays without a measured quantity do not count.

| Code | Before | After | Resolution | Locator (page checked) |
|---|---|---|---|---|
| M04 | P | P | recheck-kept | PDF p. 10, Sec. 5.6.1 |
| M12 | P | P | recheck-kept | PDF p. 18, Fig. 22 |
| E26 | P | P | recheck-kept | PDF p. 7, Table II; PDF p. 8, Fig. 4 |
| M33 | P | P | recheck-kept | PDF p. 10, Sec. 5 |
| E52 | P | P | recheck-kept | PDF p. 8, Table III |
| F06 | P | P | recheck-kept | PDF p. 6, Fig. 8 |
| F02 | P | P | recheck-kept | PDF p. 9, Fig. 8 |
| F09 | P | S | recheck-revised | PDF p. 12, Table 2 (the hardware runs of PDF pp. 13, 15-16 are qualitative) |
| N10 | P | P | recheck-kept | PDF p. 7, Table I |
| S17 | P | P | recheck-kept | PDF p. 17, Fig. 10 |
| S28 | P | P | recheck-kept | PDF p. 12, Fig. 13 |
| R17 | P | P | recheck-kept | PDF p. 10, Fig. 11; PDF p. 11, Figs. 12-13 |
| R29 | P | P | recheck-kept | PDF p. 6, Table I |
| E32 | P | P | recheck-kept | PDF p. 6, Fig. 6 |
| N05 | P | S | recheck-revised | PDF p. 7, Fig. 6 (the campus run of PDF pp. 7-8 reports only planned loop closures and the map) |
| N17 | P | P | recheck-kept | PDF p. 7, Table II |
| S02 | P | P | recheck-kept | PDF p. 7, Sec. 4.2 |
| S16 | P | P | recheck-kept | PDF p. 13, Table 4 |
| R36 | P | P | recheck-kept | PDF p. 11, Table II |

Kept 17, lowered 2. Every work had an experiment with a stated result under a named source.

**M3 drivetrain additions** (`drivetrain_effect` `no` to `yes`, resolution `recheck-revised`):

| Code | Locator (page checked) | Reported effect |
|---|---|---|
| M04 | PDF p. 7, Sec. 5.1 | the nonholonomic robot, unable to move sideways, has difficulty reaching the pose that the omnidirectional robot reaches |
| M09 | PDF p. 3, Sec. II-A | Mecanum rollers lose grip and slip on uneven ground, part of the uncertainty the controller compensates |
| N10 | PDF p. 7, Sec. VI-C | skid-steer motion on asphalt causes cumulative pose drift without the visual NMPC |
| S16 | PDF p. 6, Sec. 3.1.1; PDF p. 7, Sec. 3.1.2 | the recovery planner is built for car-like steering limits and a minimum radius of curvature |

**Locator corrections** (value unchanged, resolution `locator-corrected`, the replaced locator named in the reason):

| Code | Attribute | Value | Replaced locator | New locator |
|---|---|---|---|---|
| E44 | deg_task_class | D1 | card: Key quantitative results, p. 6, Table II | PDF p. 6, Fig. 5 |
| R26 | task_setting | physical | card: Key quantitative results, p. 6, Table III | PDF p. 6, Table II |
| R26 | deg_task_class | D2 | same | PDF p. 6, Table II |
| R26 | deg_task_setting | physical | same | PDF p. 6, Table II |
| R26 | level_degradation | P | same | PDF p. 6, Table II |

The R26 review card cites "(p. 6, Table II)" for the Hound result in place of Table III and carries a new verification-log line. The numeric-audit entry of the R26 sentence now names "R26 PDF p. 6, Table II".

## Manuscript changes by item

| Item | Change | Location |
|---|---|---|
| M1a | The abstract follows the headline count with "Only 27 (11%) inject or vary that condition against a comparator." The conclusion adds "Only 11% obtain this combination under a condition injected or varied against a comparator" and calls the 40% wheeled value "the headline share". | Abstract, Sec. XI |
| M1b | IX-B says that evidence for localization and mapping stops at the estimate, "the natural endpoint of an estimation study", and gives 91% with a named condition and component measures next to the 1% task-outcome share. | Sec. IX-B |
| M1c | IX-B adds that the other 53 headline works lack a comparator, some resting on one physical run per method, as in the LRAE field test (M14, one field exploration mission, PDF p. 7) and the outdoor route of VL-TGS (F05, each method evaluated in a single run, PDF p. 7). | Sec. IX-B |
| M2a | The abstract quotes no ranks and names the four interfaces as the survey's agenda for joint evaluation. The Sec. X opening gives each interface the rank of its best candidate with its coupling source: 4 for Interface 1 and 12 for Interface 3 through perceptual degradation, 9 for Interface 2 through learned inference error (23 through computation limits), 1 for Interface 4 through communication loss. S8 gives the cell ids (LOC-MRC:COM, LOC-REL:PER, PLN-SEM:MOD, LOC-PLN:PER), the rank of PLN-SEM:RES and the 2 works of LOC-PLN:TER, below the eligibility threshold. | Abstract, Sec. X opening, S8 |
| M2b | One sentence in the Sec. X opening and in S8 says that, at equal direct evidence, counting works ranks a candidate with more works above one with fewer, with candidate sizes shaped by the selection stages. One sentence gives Rank B (gap share): 5, 23, 18 and 12, below the actuator-fault candidate PLN-REL:ACT named in X-E. | Sec. X opening, S8 |
| M2c, m2 | "Pre-registered" is replaced. The Sec. X opening says that the rule was fixed in the public codebook before coding (commit 67872f4), S8 that it was fixed in codebook version 1.0 before coding (commit 67872f4). Commit 67872f4 holds codebook version 1.0 and precedes the primary codes (64531cd). The captions of Tables S10 and S13, the note of Table S11, the screen notes of `generated/interface-candidates.csv` and the purpose of `data/interface-decisions.json` use the same wording. The column `preregistered` of `coding-agreement.csv` keeps its name. The 06-data README changed in the first commit. X-D drops ", which places it first in the ranking". | Sec. X, S8, Tables S10, S11, S13, `scripts/coding.py`, `data/interface-decisions.json` |
| M3 | The Table II note says that the corpus has 10 works with a drivetrain-dependent effect under the definition narrowed in codebook version 1.1, after a recheck of all works for missed cases (S7). Table II cites the new works in the cells whose effect or recovery limit they report: M04 with "Sideways moves need rotation", N10 with the skid-steer slip cell and S16 with the Ackermann turning-radius cell. The omnidirectional cell now reads "Mecanum rollers can slip on uneven ground" (M09) and "Another Mecanum study reports no drive-specific effect" (S48), and the note begins "Except for the second Mecanum study". Sec. I lists the "sensing, model, and action requirements, with reported drivetrain effects". X-A drops "often" from "a wheeled robot can often also relocalize or reposition". S7 describes the recheck. | Table II, Sec. I, X-A, S7 |
| M4 | S7 says that the recheck read the PDF pages of the 19 works whose physical evidence level rested on no physical task outcome under a named condition. It kept the level where the physical run states a result under that condition, lowered it for 2 works and corrected the source locations of 2 works. A consistency check of the final codes (CR21) now requires such a stated result for the physical level. Table S8 follows the corrected levels. | S7, Table S8 |

The Table II change for M09 goes beyond a citation. The round-4 cell said that no drive-specific effect is reported on Mecanum bases, which the M09 correction contradicts. The cell keeps both Mecanum studies cited.

## Counts before and after

| Quantity | Before | After |
|---|---|---|
| Adjudication-log rows | 118 | 146 (28 review-recheck rows) |
| Values changed by the log in this round | 0 | 6 (`level_degradation` 2, `drivetrain_effect` 4) |
| Primary locator rows replaced | 0 | 5 (E44 1, R26 4) |
| `\DrivetrainEffectCount` | 6 | 10 |
| Table S8, named condition, physical closed loop | PLN 25 (45%), MRC 6 (13%), all 57 (23%) | PLN 24 (43%), MRC 5 (11%), all 55 (23%) |
| Table S8, named condition, replay, simulation, numerical model or resource | PLN 18 (32%), MRC 15 (33%), all 64 (26%) | PLN 19 (34%), MRC 16 (36%), all 66 (27%) |
| Table S8, drivetrain-dependent effect reported | PLN 1 (2%), REL 2 (5%), all 6 (2%) | PLN 3 (5%), REL 4 (10%), all 10 (4%) |
| `generated/drivetrain-evidence.csv` | skid-steer 2, omnidirectional 0, unspecified 0 | skid-steer 3 (adds N10), omnidirectional 1 (M09), unspecified 2 (M04, S16) |

Unchanged: Fig. 1 and the source-by-function matrix, Table VI, the headline (80 of 244, 33%), D1 27, D2 53, the interface ranks 4, 9, 12 and 1, Rank A 4, 7, 9 and 1, and every earlier macro of `generated/stats.tex` except `\DrivetrainEffectCount`. The level and drivetrain attributes do not enter the ranking or Table VI.

New macros, all computed from the final codes or `generated/interface-candidates.csv`: `DOneSameShare` 11, `DTwoSameCount` 53, `LocNamedShare` 91, `IfaceOneRankB` to `IfaceFourRankB` 5, 23, 18 and 12, `IfaceTwoResRank` 23, `IfaceThreeTerWorks` 2, `DrivetrainRecheckAdded` 4, `LevelRecheckWorks` 19, `LevelRecheckRevised` 2 and `LocatorCorrectionWorks` 2.

## Drivetrain recheck

A keyword screen ran over the review card and the transcription of each of the 239 works coded `drivetrain_effect` = `no`. It flagged a sentence that names a drive (skid steer, differential drive, Ackermann or car-like, Mecanum, omnidirectional, holonomic, tricycle, wheel arrangement, steering geometry, tracked, wheeled-legged) together with an effect term (slip, turning, radius, curvature, lateral or sideways motion, reversing, in-place motion, footprint, steering, feasibility, limits), or a phrase that names an effect by itself (minimum turning radius, nonholonomic, in-place rotation, strafing, side slip, support polygon, cannot move sideways).

- 83 works had hits, with 414 hit sentences (69 from cards). Each sentence was triaged as a mention (133), a case that codebook version 1.1 excludes (151) or a candidate (130).
- K13, N08, N14 and R26 were skipped, since the sample adjudication had already decided their value under version 1.1.
- The candidate passages of 12 works were read on the PDF page. Four became `yes` (M04, M09, N10, S16, table above). Eight stay `no`: M12 (a wheeled against a tracked vehicle, a difference of locomotion), M08 (a nonholonomic motivation in related work), M11 (a generic turning-radius parameter), E22 (a standard unicycle mapping), S02 (in-place rotation as an optimizer behavior), S04 (wheel-speed limits through kinematic models), R04 (turn skidding of road vehicles without a compared wheel arrangement) and S47 (in-place rotation answering the camera field of view).

The screen file holds publisher sentences and stays local. Only `no` to `yes` changes were possible in this direction.

## Page budget

The main paper stays at 24 pages. The additions are the D1 sentence of the abstract (the agenda sentence that replaces the rank sentence and the removed word "individual" keep it at 250 words), the Table II count sentence and the new Mecanum cell, the IX-B endpoint clause, component share and D2 sentence, the Sec. X count, rank and Rank B sentences, and the D1 sentence of the conclusion. They were paid for by cuts of repetition, with every citation key kept:

- O1 (IX-A): the class definitions that repeat Section III became "in the classes D1--D3 of Section III".
- O2 (IX opening): the sentence that repeated the Table VI caption.
- O3 (X-C): the clause on the 6 works of Interface 3, which Table VIII gives.
- O4 (X-A): the sentence on the different trigger objects, which repeats the monitors listed before it.
- O5 (XI): "These dependencies explain why improved component scores alone do not establish more reliable navigation", which repeats the argument of Section IX.
- Two further cuts in the IX opening sentence: the clause "which draws Sections IV--VIII together", which repeats the row labels of Table V, and the redundant "the reviewed" before "functions". Together they freed the line that let the IX-B heading return to the left column of page 13.
- The X-D clause on the first rank and the X opening clause on insufficiently characterized behavior (planned text changes of M2).

The Table II note and the Mecanum cell made Table II about 27 pt taller. With the figure environment of Fig. 1 defined after Table II, page 2 then broke before LaTeX read it, which moved Fig. 1 and every later float one page down and cost one page. The `figure*` block of Fig. 1 is now defined just before Table II in `sections/02-background.tex`, with unchanged content, and Fig. 1 stays at the top of page 3.

Words per section file (counted by the local helper `keys.py words` with commands and braces removed, floats included), b3bf857 to now: I 770 to 773, II 1,539 to 1,577, III 780 to 780, IV-VIII unchanged (6,544), IX 1,850 to 1,847, X 1,526 to 1,568, XI 282 to 283. The supplement source grows from 2,733 to 2,941 words with the S7 and S8 sentences. The abstract has 250 words.

## Scripts

- `scripts/coding.py` (first commit): final locators (`final_locators`, `merge_locators`), the `review_recheck` summary, rule CR21 for the final codes and the command `--check-final`. Second commit: "pre-registered" replaced in the captions of Tables S10 and S13, the note of Table S11, the candidate screen notes and two comments.
- `scripts/build_data.py`: the new macros listed above. New assertions, each with a comment naming its sentence: D1 below half of the headline works, the best eligible cell of each interface and its rank, PLN-SEM:RES eligible in Interface 2, LOC-PLN:TER ineligible with fewer than three works, the gap not increasing down the ranking, PLN-REL:ACT the only Rank B 1 (not an interface, category named-gap) and every interface below it, `DrivetrainEffectCount` = 6 + `DrivetrainRecheckAdded`, every corpus key cited in the Table II float except S48 coded with a drivetrain-dependent effect, M14 and F05 coded D2 with a physical setting, `DTwoSameCount` equal to the D2 count, and the S7 counts (19 level checks, more than one lowered, more than one locator correction, at least one drivetrain addition). The comment of the Interface 4 rank assertion names the Sec. X opening and S8.
- `scripts/verify_delivery.py` (first commit): validates the final codes with the final locators.
- `data/interface-decisions.json`: the purpose names the ranking rule fixed in codebook version 1.0 before coding.

## Audits

- **Numeric audit** ([numeric-audit.json](numeric-audit.json)): 30 numerical result sentences (29 before). The new IX-B sentence on one physical run per method was checked on M14 PDF p. 7 and F05 PDF p. 7. The R26 entry now names "R26 PDF p. 6, Table II". A `round5_changes` list records the added, changed and removed numbers of the abstract, IX-B, the X opening, S8, X-C, X-D, XI, the Table II note and S7.
- **Claim audit** ([claim-audit.json](claim-audit.json)): `round5_claims` lists 15 changed characterizations with their basis: the natural endpoint, the D2 examples, the ranks with their candidates, the count-based rule, Rank B, the rule fixed in commit 67872f4, the X opening sentence, the Table II citations, the Mecanum cell and the count of the note, the Sec. I wording, X-A, X-D, the conclusion and S7. The round-4 Table II claims stay as history, and the round-5 Mecanum entry names the claim it replaces. The `method` field gains one sentence for round 5.

## Length and verification

- `build_data.py`, `coding.py --check-final` (245 rows, 0 errors, 0 warnings, CR21 applies to 17 works), `coding.py --check-codes` on the frozen primary codes (0 errors, freeze hash matches), `coding.py --self-test --check-codebook --draw-sample --check-only`, `build_figures.py` (figure files unchanged), `latexmk -gg` of the supplement and the main paper, `verify_delivery.py` and `--sources` pass: 24 pages, 245 corpus citations in prose, 270 resolved references, 30 labels, three figures, eight tables, six unchanged equations, a 17-page supplement with 22 labels and 13 tables, and 741 source artifacts with no hash mismatch. Neither log has an Overfull, undefined or LaTeX Warning line.
- The last page balances without a trigger (`\IEEEtriggeratref{999}`): references 235-253 and 254-270 both end at 748 pt.
- The abstract has 250 words. All 245 corpus keys and 25 background keys are cited in prose outside floats. The house-style scan of the 30 new or changed sentences and 9 float units is clean. Its five listed ", and" joins are list joins (shares, ranks and cells). Sentence rhythm: 456 sentences, mean 23.32 words, 11.62% under 12 words (455, 23.29 and 11.65% at b3bf857). No "pre-registered" remains in the sections, `survey.tex`, `supplement.tex` or `generated/`.
- The acknowledgment is byte-identical to b3bf857.
- Library checks pass: pytest, `build_tables --strict`, `build_indexes --strict`, `check_links` (0 broken) and `check_public_tree --cjk strict`.

## Still open

- M5 (a human audit of the codes) is not addressed, by author decision.
- The minor comments m1 and m3-m14 of the re-review stay for a later round.
- The level recheck noted that N17 (Table II), M12 (PDF p. 19), R29 and R36 may report physical task outcomes under a named condition that their `deg_task_setting` (simulation or none) does not reflect. This affects neither the level nor CR21 and was not changed in this round.
- Author information and submission declarations remain incomplete.
