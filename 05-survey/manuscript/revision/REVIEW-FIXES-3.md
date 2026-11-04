# Review fixes, round 3: coverage additions and condensation - November 4, 2026

This revision follows [REVIEW-FIXES-2.md](REVIEW-FIXES-2.md). It answers the coverage items (A8, A9, B17) of the internal, simulated two-reviewer review of an earlier draft. That review is a local quality check prepared with language-model tools. It is not journal peer review. The selection grows from 229 to 245 works (244 technical studies and one context review), the background references from 17 to 20, and the bibliography from 246 to 265 entries.

## Author decisions

The options were presented on 2026-11-04. The author chose:

- **1A, HM3D citation.** The official NeurIPS Datasets and Benchmarks BibTeX export has a citation key with spaces that BibTeX cannot parse. The library keeps the export byte for byte as `citation-original.bib` and uses a derived `citation.bib` that changes only the key. The change and the author's authorization are recorded in the provenance and metadata-evidence files. This is the fourth derived-citation exception, after S24-S26.
- **2A, a separate stage.** The additions form their own "coverage additions" stage in Table III, Section III, supplement S1 and S3, and the AI-use acknowledgment. They are described as works named by an internal review of an earlier draft.
- **(a) Recency sentence.** Section III states the 2025-2026 share, computed by `build_data.py`.
- **(b) Sensitivity sentence.** Supplement S1 gives the degradation-with-task share without the additions (59 of 228, 26%) next to the share with them.
- PyMuPDF4LLM 0.2.9 for local transcription, the codes K01-K16, and three sequential steps with local commits and no push.

## Condensation of Sections IV-VIII

Commit c57938b removed repetition from Sections IV-VIII before the additions. Prose outside floats fell from 7,571 to 5,953 words (-21.4%):

| Section | Before | After | Change |
|---|---:|---:|---:|
| IV | 1,997 | 1,478 | -26.0% |
| V | 1,796 | 1,392 | -22.5% |
| VI | 1,279 | 1,036 | -19.0% |
| VII | 1,285 | 1,009 | -21.5% |
| VIII | 1,214 | 1,038 | -14.5% |

The cuts removed section openers that repeated the supplement tables, synthesis sentences that restated Table IV, subsection closers that restated Sections II, IX or X, and second descriptions of works cited elsewhere. About twenty runs of single-study sentences that share a mechanism were merged. Every corpus work kept a prose citation, and the qualitative statements asserted by `build_data.py` kept their wording. The paper went from 24 to 23 pages.

## Coverage additions (K01-K16)

The library batch is [review-additions-2026-11-04](../../../06-data/review-additions-2026-11-04/README.md). Each work has a targeted light review card that passes `review_check --pdf`. Coding follows the vocabulary of `06-data/vocabulary.md`:

| ID | Work | Cited in | Module | Evidence type | Platform class | Evaluation |
|---|---|---|---|---|---|---|
| K01 | SubT-MRS (CVPR 2024) | Table II, IV-A, IV-B | localization-mapping | dataset-resource | mixed† | residual, designed-degradation |
| K02 | RELLIS-3D (ICRA 2021) | Table II, V-A | traversability-planning-control | dataset-resource | wheeled-unspecified | residual |
| K03 | STEP (RSS 2021) | V-A, X-C | traversability-planning-control | closed-loop-hardware | wheeled-unspecified | closed-loop-task |
| K04 | TartanDrive (ICRA 2022) | Table II, V-A | traversability-planning-control | dataset-resource | road-vehicle† | residual, designed-degradation |
| K05 | EVORA (T-RO 2024) | V-A, X-C | traversability-planning-control | closed-loop-hardware | ackermann | residual, closed-loop-task, designed-degradation |
| K06 | Kimera-Multi (T-RO 2022) | VII-B, X-D | multi-robot | recorded-robot-data | wheeled-unspecified | residual, designed-degradation |
| K07 | LAMP 2.0 (RA-L 2022) | VII-B, X-D | multi-robot | recorded-robot-data | wheeled-unspecified | residual |
| K08 | Team CSIRO Data61 (Field Robotics 2022) | VII-C, X-D | multi-robot | closed-loop-hardware | tracked† | residual, closed-loop-task |
| K09 | Team Explorer (Field Robotics 2022) | VII-C, X-D | multi-robot | closed-loop-hardware | wheeled-unspecified | closed-loop-task |
| K10 | CERBERUS (Science Robotics 2022) | VII-C, X-D | multi-robot | closed-loop-hardware | legged† | closed-loop-task |
| K11 | HM3D (NeurIPS D&B 2021) | Table II, VI-A | semantic-language-navigation | dataset-resource | none† | residual, closed-loop-task |
| K12 | LM-Nav (CoRL 2022, PMLR 2023) | VI-B | semantic-language-navigation | closed-loop-hardware | wheeled-unspecified | residual, closed-loop-task |
| K13 | GNM (ICRA 2023) | VI-B | semantic-language-navigation | closed-loop-hardware | differential-drive | closed-loop-task, designed-degradation |
| K14 | ViNT (CoRL 2023) | VI-B | semantic-language-navigation | closed-loop-hardware | wheeled-unspecified | closed-loop-task |
| K15 | ConceptGraphs (ICRA 2024) | VI-A | semantic-language-navigation | closed-loop-hardware | wheeled-unspecified | residual, closed-loop-task |
| K16 | NoMaD (ICRA 2024) | VI-B | semantic-language-navigation | closed-loop-hardware | wheeled-unspecified | closed-loop-task |

† boundary platform (not a wheeled robot or its data).

All 16 are also cited in the new S1 paragraph. The prose groups them by mechanism: datasets beside the methods they serve, STEP and EVORA as uncertainty-aware terrain risk, the GNM-ViNT-NoMaD lineage with LM-Nav before LeLaN, Kimera-Multi and LAMP 2.0 as outlier-robust inter-robot loop closure, and the three DARPA Subterranean Challenge teams as communication-limited field systems. Legged, aerial, tracked, road-vehicle and simulation platforms are named where these works anchor an argument. Sections I-X gained 807 words of prose outside floats.

The review also named VLMaps, whose 2025 journal extension AVLMaps (S12) is already in the corpus, and NeBula, which exists only as an arXiv preprint. Other named works were not acquired in this stage. S1 states both points.

## Background surveys

Three related surveys join Table I and the survey list of Section I as background references:

| Key | Source | Connection in Table I |
|---|---|---|
| `B_RadarSurvey2024` | Harlow et al., mmWave radar applications in robotics, IEEE T-RO 40, 2024 | Radar as an independent motion source (Section IV-B) |
| `B_AdverseWeather2023` | Zhang et al., perception and sensing for autonomous vehicles under adverse weather, ISPRS J. Photogramm. Remote Sens. 196, 2023 | Sensing degradation traced to recovery and task outcomes (Sections II-B, IV) |
| `B_SafeLearning2022` | Brunke et al., safe learning in robotics, Annu. Rev. Control Robot. Auton. Syst. 5, 2022 | Safety filters judged by the assumptions of their guarantees (Section V-D) |

Each record was fetched from Crossref and saved in `background-sources/` without its cited-reference list. Title, first author, container, volume and the print year used by `citation_scope.py` were checked. All three are from 2022-2024, so the foundational exceptions are unchanged. The Crossref records of the radar and adverse-weather surveys have no abstract, so their scope was taken from the opened IEEE Xplore and ScienceDirect abstract pages. `background-verification.json` now has 25 records, 20 used and 5 excluded.

## Section III, Table III, S1, S3 and acknowledgment

- **Table III:** a row "Coverage additions | 2021-2024 works named in an internal review of an earlier draft | 16" before the total of 245.
- **Section III:** screening-based selection ended on November 3, 2026. A final stage on November 4 added the 16 works, each with a formal publication record, outside the earlier screening. A new sentence states that 173 of the 245 works (71%) date from 2025-2026, a skew to which the stage limited to recent IEEE papers contributes.
- **S1:** the coverage stage joins the list of stages, and the earlier "final stage" is renamed "recent IEEE stage". A new paragraph lists the additions by function, states that they did not come from a systematic search, names VLMaps and NeBula, and gives the sensitivity sentence: without the additions, 59 of 228 technical publications (26%) report task outcomes under a named degradation condition, against 61 of 244 (25%) with them.
- **S3:** the targeted-reading sentence covers the last three stages (48, 36 and 16 works). Four citation records are derived, including the replaced unparsable citation key.
- **Acknowledgment:** a new sentence states that the internal review of an earlier draft, which named the works of the final stage, was prepared with the same language-model tools.

## Corpus-dependent numbers

`build_data.py` computes every number below. The prose statements that carry them were re-read against `generated/stats.json`.

| Quantity | Before | After |
|---|---:|---:|
| Corpus / technical / context review | 229 / 228 / 1 | 245 / 244 / 1 |
| Background references / bibliography | 17 / 246 | 20 / 265 |
| Journal / conference | 195 / 34 | 201 / 44 |
| Light cards (targeted) | 206 (119) | 222 (135) |
| Boundary / wheeled-target works | 68 / 161 | 73 / 172 |
| Degradation testing with task outcomes | 59 (26%) | 61 (25%) |
| Localization studies / task outcome / named degradation / boundary | 66 / 2 / 45 / 36 | 67 / 2 / 46 / 37 |
| Computation placement not reported | 79 | 89 |
| 2025-2026 works | 173 of 229 | 173 of 245 (71%) |

Table V (evidence map), publications / task outcomes / named degradation / both:

| Section | Before | After |
|---|---|---|
| IV | 66 / 2 / 45 / 2 | 67 / 2 / 46 / 2 |
| V | 52 / 49 / 21 / 19 | 56 / 51 / 23 / 20 |
| VI | 30 / 29 / 9 / 8 | 36 / 35 / 10 / 9 |
| VII | 40 / 26 / 24 / 13 | 45 / 29 / 25 / 13 |
| VIII | 40 / 22 / 31 / 17 | 40 / 22 / 31 / 17 |
| All | 228 / 128 / 130 / 59 | 244 / 139 / 135 / 61 |

One qualitative statement changed. The Section VII share of studies with task outcomes under a named degradation condition fell from 13 of 40 (0.325) to 13 of 45 (0.289). "About a third" became "More than a quarter", and the assertion changed from `0.3 <= share <= 0.37` to `0.25 < share < 1/3`. The other assertions hold unchanged: localization task outcomes 2 of 67 (below 0.05), planning and semantic task outcomes 51 of 56 and 35 of 36 (above 0.9), planning named degradation 23 of 56 (below one half), semantic named degradation 10 of 36 (below one third), and fault management with the largest degradation-with-task share (17 of 40). New macros: `\CoverageCount` (16), `\RecentCount` (173), `\RecentShare` (71), and `\DegTaskCountBase`, `\CoreCountBase` and `\DegTaskShareBase` (59, 228, 26). The script asserts the base pair (59, 228).

## Gap claims re-checked (A9)

The review tied two gap claims to the missing works. Both now hold with them:

- **Section X-C.** STEP accounts for localization error in its traversability evaluation (PDF p. 2), and its collision-risk variance comes from the elevation-map variance, which the authors call mainly a function of localization error (p. 5). Its simulation assumes no localization error (p. 7). EVORA uses motion-capture pose indoors (p. 15) and leaves perception uncertainty to separate treatment (p. 18). A new sentence names both. The open question changed from "how uncertainty in pose alters the probability that a wheel-supported footprint lies on the estimated traversable surface under incomplete observation" to "how uncertainty in pose, beyond its share of map variance, alters [that probability] ..., and whether propagating it changes executed outcomes".
- **Table IV, planning gaps.** "Pose uncertainty rarely propagated into terrain decisions" became "Pose uncertainty rarely propagated into terrain decisions, with its effect on outcomes untested".
- **Section X-D.** Kimera-Multi rejects outlier inter-robot loop closures with distributed GNC while its robots stay in communication range (pp. 12, 14). LAMP 2.0 queues data during link loss, sends them as a batch on reconnection and filters loop closures with ICM or GNC (pp. 4-5), without evaluating stale or biased batches separately. Two new sentences state these findings and note that the Subterranean Challenge teams fielded delayed sharing without a controlled test. "The open interface is selective acceptance when ..." became "The open interface is selective acceptance beyond outlier rejection when ...". The Section VII-C version of this gap was already removed in the condensation. The Table IV multi-robot cell ("untested on moving teams") remains true, since none of the added team systems tests what it accepts after a partition.

[claim-audit.json](claim-audit.json) records the before and after texts as corrections.

## Bibliography rendering

`scripts/bib_case.py` now braces "Subterranean Challenge" and "SubT Challenge" as whole phrases and lists Data61, Habitat, Kimera and Matterport as proper names. The titles print as "Team CSIRO Data61's approach to the DARPA Subterranean Challenge", "CERBERUS in the DARPA Subterranean Challenge", "The DARPA SubT Challenge", "Kimera-Multi" and "Habitat-Matterport 3D". The LM-Nav export gives one author as "ichter, brian". `build_data.py` capitalizes that name in `refs.bib` only and records the change in `generated/citation-key-map.json`. The raw BibTeX is unchanged.

## Audits

- [numeric-audit.json](numeric-audit.json) covers 27 numerical sentences (22 before), with no mismatch. The five new sentences take numbers from K01, K02, K07, K12, K14 and K16. Each number was re-read on the cited physical PDF page, and the page locators are recorded. Name tokens with digits (LAMP 2.0, RELLIS-3D, Data61, GPT-3, Go 1, 2.5D) are excluded from number extraction. The two E01 sentences that now cite SubT-MRS keep their E01 comparison record. Numbers outside the audit's unit pattern were also checked on their pages: about 200,000 interactions (K04 p. 1), six and four robots (K13 pp. 2, 4) and five indoor trials (K05 p. 16).
- [claim-audit.json](claim-audit.json) covers 67 sentence claims (61 before) and 68 clause claims (34 matched only by targeted search). The new characterizations of K03, K04, K06, K07, K08, K09, K11 and K12 were checked against their cards and PDF passages. Nine corrections are recorded: the five earlier ones, the three gap claims above, and the Section VII share.

## Length

The main paper has 24 pages, the T-IV maximum. Without a forced column break the last page held references 234-252 in the left column (bottom 748 pt) and 253-265 in the right (bottom 595 pt). `\IEEEtriggeratref{251}` now balances it: references 234-250 end at 676 pt and 251-265 at 667 pt. The supplement grew from 8 to 9 pages with 81 references.

## Follow-up wording fixes
The review of this round approved the changes with three minor wording findings, which were then applied:
- **S1 sensitivity sentence.** "of the 228 technical publications" became "of the 228 purposively selected technical publications", so both shares are marked as statistics of the purposive sample.
- **Table IV, multi-robot gaps.** "Ideal or modeled communication" became "Mostly ideal or modeled communication", since the CSIRO Data61, Explorer and CERBERUS team systems (K08-K10) were fielded under real link loss.
- **Section VI-B, ViNT.** "at a higher inference cost" became "at a higher inference cost than feedforward convolutional policies", the comparison the authors state (ViNT PDF p. 8).

## Verification

- `verify_delivery.py` and `--sources` pass: 24 pages, 245 corpus citations in prose and 265 resolved references, seven foundational exceptions, 28 labels, three figures, six tables, six unchanged equations, a 9-page supplement with 12 labels, and 741 source artifacts with no hash mismatch. Neither log contains an Overfull, undefined or LaTeX Warning line.
- The prose check passes: all 245 corpus keys and 20 background keys are cited in prose outside floats, and 120 new or changed sentences have no house-style hit.
- Sentence rhythm: 461 sentences, mean 23.0 words, median 22, 13% under 12 words, 12% over 35 words. The style fingerprint shows no flags, and the 10-gram overlap screen finds no overlapping phrase with the 267 source documents.
- Library checks pass: pytest, `build_tables --strict`, `build_indexes --strict`, `check_links` and `check_public_tree --cjk strict`.
