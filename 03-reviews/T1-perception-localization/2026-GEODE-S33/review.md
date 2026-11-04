# Heterogeneous LiDAR dataset for benchmarking robust localization in diverse degenerate scenarios

## Metadata

| Field | Value |
|---|---|
| ID | S33 |
| Title | Heterogeneous LiDAR dataset for benchmarking robust localization in diverse degenerate scenarios |
| Authors | Zhiqiang Chen and Yuhua Qi and Dapeng Feng and Xuebin Zhuang and Hongbo Chen and Xiangcheng Hu and Jin Wu and Kelin Peng and Peng Lu |
| Venue | The International Journal of Robotics Research |
| Year | 2026 |
| Type | journal |
| DOI | [10.1177/02783649251344967](https://doi.org/10.1177/02783649251344967) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649251344967 |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-GEODE-S33/paper.pdf` and `02-fulltext/T1-perception-localization/2026-GEODE-S33/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2026-GEODE-S33/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-resource
- evidence_all: dataset-resource
- protocol_caveats: none
- platform_class: mixed
- platform: Handheld, UGV, vehicle and sailboat carriers with heterogeneous LiDAR suites; boundary resource rather than one wheeled deployment (pp. 4, 10).
- boundary_platform: yes
- degradation: lidar-degeneracy, terrain, gnss-denial, visual-degradation
- degradation_observed: none
- evaluation_primary: designed-degradation
- evaluation_all: residual, designed-degradation
- sensors: Heterogeneous spinning/nonrepetitive LiDARs, stereo cameras and IMUs; RTK-INS, Vicon, total station and map-derived references
- compute: Acquisition/synchronization hardware is described; benchmark processing placement not retained from selected passages.
- compute_location: not-reported
- summary_result: Heterogeneous degenerate scenes reveal failure modes hidden by conventional nominal-scene accuracy tests.
- summary_limitation: Fixed camera exposure, one-time calibration and imperfect synchronization are documented; some sensor/scene pairs lack a valid reference trajectory (pp. 12, 15).
- survey_included: yes
- verification_level: light

## Problem

Robustness on one sensor or scene does not establish robustness across geometric degeneracy and scanning patterns.

## Mechanism

Organizes diverse degenerate trajectories and sensor suites with scene-dependent calibration, synchronization and reference-generation procedures (pp. 4, 10-12).

## Baselines and controls

FAST-LIO2, DLIO, COIN-LIO, LVI-SAM, R3LIVE, FAST-LIVO and VINS-Fusion are among the inspected benchmark descriptions (p. 12).

## Platform and setup

Handheld, UGV, vehicle and sailboat carriers with heterogeneous LiDAR suites; boundary resource rather than one wheeled deployment (pp. 4, 10).

## Evidence type and transfer

Strongest coded setting: `dataset-resource`. Reference dimensionality and origin vary by sequence. Map-based localization used to construct reference cannot be assumed independent of LiDAR estimation.

## Sensors

Heterogeneous spinning/nonrepetitive LiDARs, stereo cameras and IMUs; RTK-INS, Vicon, total station and map-derived references.

## Compute and latency

Acquisition/synchronization hardware is described; benchmark processing placement not retained from selected passages.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Fixed camera exposure, one-time calibration and imperfect synchronization are documented; some sensor/scene pairs lack a valid reference trajectory (pp. 12, 15).

## Transfer conditions

Reference dimensionality and origin vary by sequence. Map-based localization used to construct reference cannot be assumed independent of LiDAR estimation.

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

- **p. 15, Selected source passage.** "the calibration process is conducted only once per machine."
  Supports severity/sensor-conditioned evaluation and narrows reference-quality assumptions in the pose-to-terrain challenge.

## Survey-usable statements

### Supported

- Heterogeneous degenerate scenes reveal failure modes hidden by conventional nominal-scene accuracy tests. Supports severity/sensor-conditioned evaluation and narrows reference-quality assumptions in the pose-to-terrain challenge.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Reference dimensionality and origin vary by sequence. Map-based localization used to construct reference cannot be assumed independent of LiDAR estimation.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 10, 12, 14, 15; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

The ability to estimate pose and generate maps using 3D LiDAR significantly enhances robotic system autonomy. However, existing open-source datasets lack representation of geometrically degenerate environments, limiting the development and benchmarking of robust LiDAR SLAM algorithms. To address this gap, we introduce GEODE, a comprehensive multi-LiDAR, multi-scenario dataset specifically designed to include real-world geometrically degenerate environments. GEODE comprises 64 trajectories spanning over 64 km across seven diverse settings with varying degrees of degeneracy. The data was meticulously collected to promote the development of versatile algorithms by incorporating various LiDAR sensors, stereo cameras, IMUs, and diverse motion conditions. We evaluate state-of-the-art SLAM approaches using the GEODE dataset to highlight current limitations in LiDAR SLAM techniques. This extensive dataset will be publicly available at https://thisparticle.github.io/geode, supporting further advancements in LiDAR-based SLAM.
