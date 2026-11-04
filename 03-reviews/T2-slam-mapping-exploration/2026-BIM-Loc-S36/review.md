# BIM-Loc: BIM-integrated discrepancy-aware LiDAR-based indoor localization

## Metadata

| Field | Value |
|---|---|
| ID | S36 |
| Title | BIM-Loc: BIM-integrated discrepancy-aware LiDAR-based indoor localization |
| Authors | Yinqiang Zhang and Liang Lu and Yipeng Pan and Maolin Lei and Yuhan Xie and Zhanteng Xie and Xiaowei Luo and Jia Pan |
| Venue | The International Journal of Robotics Research |
| Year | 2026 |
| Type | journal |
| DOI | [10.1177/02783649261462593](https://doi.org/10.1177/02783649261462593) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649261462593 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-BIM-Loc-S36/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-BIM-Loc-S36/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-BIM-Loc-S36/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: handheld
- platform: Handheld construction-site and SLABIM sensor suites plus BIM-robot simulation; real hardware evaluates localization/mapping, not wheeled motion control (pp. 14-15).
- boundary_platform: yes
- degradation: scene-change, data-association-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR and IMU; as-designed BIM structures; camera used only for visualization in the construction recordings
- compute: CPU-only Mini-PC with Intel Core i9-12900, integrated into the sensor suite; sequences used for comparisons (p. 10).
- compute_location: desktop-offline
- summary_result: Discrepancy-aware structural factors support localization against imperfect BIM priors.
- summary_limitation: Requires an approximate initial position and leaves exploration passive during human-operated inspections (p. 21).
- survey_included: yes
- verification_level: light

## Problem

As-designed building geometry differs from the actual constructed or furnished environment.

## Mechanism

Associates scans by multi-hit ray casting, inserts BIM-aware pose-graph factors, and updates hierarchical Bayesian discrepancy maps to limit inconsistent structural constraints (pp. 4-10).

## Baselines and controls

Point-map comparators receive samples of the same BIM surfaces; simulated, construction and office settings vary BIM-reality inconsistency (pp. 10, 14).

## Platform and setup

Handheld construction-site and SLABIM sensor suites plus BIM-robot simulation; real hardware evaluates localization/mapping, not wheeled motion control (pp. 14-15).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Check BIM alignment, missing structures and observation coverage; unknown discrepancy-map regions are not confirmed absent structures.

## Sensors

LiDAR and IMU; as-designed BIM structures; camera used only for visualization in the construction recordings.

## Compute and latency

CPU-only Mini-PC with Intel Core i9-12900, integrated into the sensor suite; sequences used for comparisons (p. 10).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Requires an approximate initial position and leaves exploration passive during human-operated inspections (p. 21).

## Transfer conditions

Check BIM alignment, missing structures and observation coverage; unknown discrepancy-map regions are not confirmed absent structures.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 21, Selected source passage.** "the method requires an approximate initial position to initialize localization"
  Adds explicit map-prior validity reasoning and prevents conflating discrepancy detection with active inspection or autonomous global initialization.

## Survey-usable statements

### Supported

- Discrepancy-aware structural factors support localization against imperfect BIM priors. Adds explicit map-prior validity reasoning and prevents conflating discrepancy detection with active inspection or autonomous global initialization.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Check BIM alignment, missing structures and observation coverage; unknown discrepancy-map regions are not confirmed absent structures.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 10, 14, 15, 18, 21; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Accurate and robust localization is a fundamental requirement for service and inspection robots, particularly in feature-sparse indoor environments where traditional systems struggle due to a lack of distinct landmarks. While prior maps can enhance robustness, precise and compact maps capturing real-world details are often unavailable for new or frequently changing environments. This paper presents BIM-Loc, a novel discrepancy-aware LiDAR-based localization method that directly integrates Building Information Models (BIM) from the design phase. BIM-Loc simultaneously estimates trajectories aligned with the BIM coordinate system and identifies discrepancies between real-world observations and the as-designed BIM in an online fashion. Our core contributions include: (1) a novel multi-hit ray casting strategy for efficient BIM-point data association and projection of 3D observations into 2D texture space; (2) a pose graph optimization framework with BIM-integrated factors that enforces consistency among odometry, sequential scans, and BIM structures; and (3) a hierarchical Bayesian inference module that incrementally updates a continuous 2D surface representation for discrepancy detection, propagating updates from the pixel to the structure level. Extensive evaluations in both simulation and real-world applications demonstrate that BIM-Loc significantly outperforms state-of-the-art map-based methods in localization accuracy and robustness. More experimental results are available at our project website: https://bim-loc.github.io/bim-loc.
