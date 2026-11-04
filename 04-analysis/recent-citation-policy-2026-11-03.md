> Stage record: the later [IEEE refresh integration](ieee-refresh-integration-2026-11-03.md) assessed and cited R01-R36 and moved the five foundational exceptions below to the internal library. The current manuscript has 229 selected works and 246 references (seven foundational pre-2021 background references were reinstated for attribution on 2026-11-04), all from 2021-2026.

# Recent citation policy and IEEE refresh

The revised manuscript contains **193 selected works** (192 technical studies and one context review), all from 2021-2026, plus **10 background references**, for **203 resolved references**. Five older references are explicit foundational exceptions. The source library now contains 231 acquired papers and transcriptions, including the original 195 assessed papers; X01 and X15 remain available internally.

The 48-paper expansion remains integrated. This revision removes two replaceable historical comparison examples and six historical background entries, rather than adding unacquired candidates. Recent robot-specific evaluation resources replace the generic historical resource rows; no new numerical performance values are introduced. The seven retained numerical cases and six equations are unchanged.

## References moved out of the manuscript

| Identity | Reason | Preservation |
|---|---|---|
| X01 (1999) | Historical sliding-mode trajectory-tracking example; recent GP/MPC and uncertainty-aware tracking studies already support the comparison. | Indexed PDF, citation, Markdown and review card unchanged; catalog marks internal reference |
| X15 (2016) | Historical social inverse-reinforcement-learning example; recent interaction prediction and social/semantic navigation studies support the current comparison. | Indexed PDF, citation, Markdown and review card unchanged; catalog marks internal reference |
| B_Cadena2016 | Historical SLAM review; current collaborative and method-specific comparisons suffice for the manuscript scope. | Original metadata verification and prior delivery snapshot retained |
| B_LOAM2014 | Historical estimator example; retain ORB-SLAM3 (2021) and FAST-LIO2 (2022) as recent representative baselines. | Original metadata verification and prior delivery snapshot retained |
| B_KITTI2012 | Historical generic driving benchmark; use recent ground-robot datasets in the evaluation-resource comparison. | Original metadata verification and prior delivery snapshot retained |
| B_TUM2012 | Historical generic RGB-D benchmark; use recent robot-specific dataset resources in the current comparison. | Original metadata verification and prior delivery snapshot retained |
| B_Habitat2019 | Historical simulator citation; discuss simulation requirements through recent evaluated systems. | Original metadata verification and prior delivery snapshot retained |
| B_HumanAware2013 | Historical human-aware navigation survey; current learned-navigation/foundation-model reviews and recent social-navigation studies cover the chosen scope. | Original metadata verification and prior delivery snapshot retained |

## Foundational exceptions

| Reference | Why it remains |
|---|---|
| B_Campion1996 | Primary classification and kinematic definitions underlying the wheeled-robot models used in the background. |
| B_DWA1997 | Original definition of dynamic-window local planning, repeatedly used as a named comparator. |
| B_TEB2013 | Original sparse trajectory formulation underlying the named TEB comparator and its recovery variants. |
| B_Nav22020 | Primary source for the navigation-system architecture discussed as a foundational deployment example. |
| B_CBF2017 | Primary source for the barrier-function condition and its assumptions used in the displayed background equation. |

These exceptions support definitions or named baseline mechanisms; they are not used as evidence of current state-of-the-art performance.

## New IEEE acquisition queue

The [new batch](../06-data/ieee-refresh-2026-11-03/README.md) freezes **36 unique 2025-2026 IEEE candidates**, six in each library theme: 23 formal-year 2026 and 13 formal-year 2025 records. They were checked against all existing library DOIs and reviewed using title and abstract evidence. There are 34 journal articles and two individually assessed ICRA papers; proceedings coverage is not exhaustive. Discovery source completion does not imply exhaustive relevance screening.

**Newly delivered official pairs: 36; pending: 0.** The user supplied all official PDFs and raw IEEE BibTeX exports after the earlier Request Rejected block. The installed acquisition skill validated identity and imported all 72 files without contacting the publisher. Original bytes and frozen selection hashes are preserved.

All 36 sources now have OXR-1.0/vLLM Markdown, covering 482 PDF pages with per-page JSON and referenced image assets. Both task-owned server services were stopped after extraction. The [batch guide](../06-data/ieee-refresh-2026-11-03/README.md) records acquisition, coverage and checks. The library total is 231; the new 36 await targeted assessment and are not manuscript members. Current manuscript counts remain 193 selected works / 203 references.

## Validation and limits

The main paper compiles to 33 pages and the supplement to 3. All 203 references resolve; all 193 selected works appear in prose. Source-inclusive verification checks all 585 indexed PDF/citation/Markdown artifacts, including the two internal-only sources, with zero mismatches. The index and comparison CSV bytes are unchanged. The catalog regression suite passes 13 cases, including preservation of internal sources and citation exceptions.

There are no unresolved references, overfull boxes or LaTeX warnings. The main log retains 12 underfull horizontal boxes and the supplement one. Final pages and the revised corpus figure were visually inspected. No new clean public-clone build, human final review, commit, push, publication or submission is claimed. Assessment depth remains 23 full + 172 light cards in the library; the manuscript uses 23 full + 170 light cards, including 87 legacy conversions and 83 targeted readings.

[Current selection](../06-data/survey-inclusion.json) · [Manuscript guide](../05-survey/README.md) · [New candidate selection](../06-data/ieee-refresh-2026-11-03/selection.csv)
