# 3D Foundation Model-Based Loop Closing for Decentralized Collaborative SLAM

## Metadata

| Field | Value |
|---|---|
| ID | S11 |
| Title | 3D Foundation Model-Based Loop Closing for Decentralized Collaborative SLAM |
| Authors | Lajoie, Pierre-Yves and Ramtoula, Benjamin and De Martini, Daniele and Beltrame, Giovanni |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3609204](https://doi.org/10.1109/lra.2025.3609204) |
| Official URL | https://ieeexplore.ieee.org/document/11159173/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2025-Foundation-Loop-Closing-S11/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2025-Foundation-Loop-Closing-S11/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2025-Foundation-Loop-Closing-S11/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Public S3E and GrAco ground-robot sequences replayed on Jetson hardware; the same odometry is supplied to compared pipelines (pp. 4-5).
- boundary_platform: no
- degradation: data-association-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Monocular keyframe pairs for loop registration plus an existing correctly scaled odometry source
- compute: NVIDIA Jetson AGX Xavier processes dataset sequences; using an onboard-class computer does not establish live onboard execution (p. 4).
- compute_location: desktop-offline
- summary_result: Foundation-model loop registration supplies inter-robot constraints while metric odometry anchors their scale.
- summary_limitation: Requires correctly scaled stable odometry; major training-domain changes may require fine-tuning (pp. 7-8).
- survey_included: yes
- verification_level: light

## Problem

Large viewpoint differences obstruct collaborative map overlap and monocular relative poses have scale ambiguity.

## Mechanism

Uses MAST3R image-pair geometry, robust confidence/outlier filtering and pose-graph scale formulations anchored by metric single-robot odometry (pp. 2-5).

## Baselines and controls

Stereo/LiDAR Swarm-SLAM configurations, shared-odometry comparisons and independent/smoothed scale-factor ablations (pp. 4-5).

## Platform and setup

Public S3E and GrAco ground-robot sequences replayed on Jetson hardware; the same odometry is supplied to compared pipelines (pp. 4-5).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. Monocular loop input does not imply monocular-only metric SLAM; odometry supports both scale and confidence.

## Sensors

Monocular keyframe pairs for loop registration plus an existing correctly scaled odometry source.

## Compute and latency

NVIDIA Jetson AGX Xavier processes dataset sequences; using an onboard-class computer does not establish live onboard execution (p. 4).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Requires correctly scaled stable odometry; major training-domain changes may require fine-tuning (pp. 7-8).

## Transfer conditions

Monocular loop input does not imply monocular-only metric SLAM; odometry supports both scale and confidence.

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

- **p. 7, Selected source passage.** "metric-scale odometry from the single-robot systems to anchor the scale of the global map."
  Connects foundation models to compact team estimation while exposing the independent-state assumption required by their confidence and scale treatment.

## Survey-usable statements

### Supported

- Foundation-model loop registration supplies inter-robot constraints while metric odometry anchors their scale. Connects foundation models to compact team estimation while exposing the independent-state assumption required by their confidence and scale treatment.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Monocular loop input does not imply monocular-only metric SLAM; odometry supports both scale and confidence.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 7, 8; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Decentralized Collaborative Simultaneous Localization and Mapping (C-SLAM) techniques often struggle to identify map overlaps due to significant viewpoint variations among robots. Motivated by recent advancements in 3D foundation models, which can register images despite large viewpoint differences, we propose a robust loop closing approach that leverages these models to establish inter-robot measurements. In contrast to resource-intensive methods requiring full 3D reconstruction within a centralized map, our approach integrates foundation models into existing SLAM pipelines, yielding scalable and robust multi-robot mapping. Our contributions include: 1) integrating 3D foundation models to reliably estimate relative poses from monocular image pairs within decentralized C-SLAM; 2) introducing robust outlier mitigation techniques critical to the use of these relative poses and 3) developing specialized pose graph optimization formulations that efficiently resolve scale ambiguities. We evaluate our method against state-of-the-art approaches, demonstrating improvements in localization and mapping accuracy, alongside significant gains in computational and memory efficiency. These results highlight the potential of our approach for deployment in large-scale multi-robot scenarios.
