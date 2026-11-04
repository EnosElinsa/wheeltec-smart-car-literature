# Implicit Point-to-Voxel LiDAR-IMU SLAM

## Metadata

| Field | Value |
|---|---|
| ID | S30 |
| Title | Implicit Point-to-Voxel LiDAR-IMU SLAM |
| Authors | Dong, Yan and Xu, Enci and Yang, Junyu and Qiu, Shaoqiang and Wang, Jiong and Han, Bin |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2026.3683446](https://doi.org/10.1109/tase.2026.3683446) |
| Official URL | https://ieeexplore.ieee.org/document/11480788/ |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-Implicit-Voxel-SLAM-S30/paper.pdf` and `02-fulltext/T1-perception-localization/2026-Implicit-Voxel-SLAM-S30/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2026-Implicit-Voxel-SLAM-S30/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Self-built wheeled LiDAR/IMU robot and public unstructured-scene datasets; selected evidence evaluates pose/map outputs (pp. 8-10).
- boundary_platform: no
- degradation: lidar-degeneracy, terrain, model-error
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR and IMU, with voxel features and learned residual uncertainty
- compute: CPU ONNX inference and cached/event-driven voxel features; no complete navigation latency retained (pp. 10, 12).
- compute_location: desktop-offline
- summary_result: Implicit residuals exploit nonplanar geometry under the inspected unstructured-scene tests.
- summary_limitation: In-domain training helps similar data but can reduce generalization elsewhere; genuinely unseen-scene transfer remains future work (p. 12).
- survey_included: yes
- verification_level: light

## Problem

Planar or simple parametric voxel models discard useful constraints in vegetation and curved geometry.

## Mechanism

Predicts point-to-voxel residuals and uncertainty from implicit local geometry, incorporates them into an iterated error-state Kalman filter, and caches updated voxel embeddings (pp. 3, 12).

## Baselines and controls

LIO-SAM, Fast-LIO, Point-LIO, VoxelMap and PV-LIO with shared LiDAR/IMU inputs; a range-limited pillar experiment isolates weak planar support (pp. 8-9).

## Platform and setup

Self-built wheeled LiDAR/IMU robot and public unstructured-scene datasets; selected evidence evaluates pose/map outputs (pp. 8-10).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. More usable residuals and learned observation variance do not establish calibrated protection levels or safe control; verify training distribution and extrinsic assumptions.

## Sensors

LiDAR and IMU, with voxel features and learned residual uncertainty.

## Compute and latency

CPU ONNX inference and cached/event-driven voxel features; no complete navigation latency retained (pp. 10, 12).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

In-domain training helps similar data but can reduce generalization elsewhere; genuinely unseen-scene transfer remains future work (p. 12).

## Transfer conditions

More usable residuals and learned observation variance do not establish calibrated protection levels or safe control; verify training distribution and extrinsic assumptions.

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

- **p. 12, Selected source passage.** "the learned implicit residual model is affected by the training data distribution"
  Extends adaptive registration beyond reweighting fitted planes while preserving the distinction between learned observation uncertainty and operational integrity.

## Survey-usable statements

### Supported

- Implicit residuals exploit nonplanar geometry under the inspected unstructured-scene tests. Extends adaptive registration beyond reweighting fitted planes while preserving the distinction between learned observation uncertainty and operational integrity.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. More usable residuals and learned observation variance do not establish calibrated protection levels or safe control; verify training distribution and extrinsic assumptions.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 8, 9, 10, 12; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Existing LiDAR SLAM methods typically rely on parameterizable explicit local models—planes, quadric surfaces, or Gaussian distributions—to formulate geometric constraints for state estimation. In unstructured environments, however, structures like tree trunks, weeds and uneven terrains are difficult to be precisely represented by simple parametric models, leading to fewer reliable constraints and introducing modeling errors. To address this issue, we propose a novel implicit point-to-voxel observation model that directly predicts residuals and their uncertainty from local voxel geometries without explicit fitting. The resulting measurements are incorporated into an iterated error-state Kalman filter (IESKF) for pose update. To support efficient online retrieval and update of local geometric context, we further introduce an implicit voxel map representation that partitions the map into voxels and maintains an online-updated implicit representation for each voxel. Experiments show that the proposed method provides more stable effective constraints and improves localization accuracy in unstructured scenes, while maintaining real-time performance on a CPU platform.
