# DR‐ICP: Robust LiDAR SLAM Registration for Degenerate Tunnels

## Metadata

| Field | Value |
|---|---|
| ID | S24 |
| Title | DR‐ICP: Robust LiDAR SLAM Registration for Degenerate Tunnels |
| Authors | Qian, Guanyu and Chen, Xuemei and Lu, Chao and Tian, Yihong and Liu, Yueze and Zhao, Xiaoxuan and Yao, Chengda |
| Venue | Journal of Field Robotics |
| Year | 2026 (early access; derived year correction) |
| Type | journal |
| DOI | [10.1002/rob.70362](https://doi.org/10.1002/rob.70362) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.70362 |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-DR-ICP-S24/paper.pdf` and `02-fulltext/T1-perception-localization/2026-DR-ICP-S24/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2026-DR-ICP-S24/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: mixed
- platform: Tunnel acquisition platform with Livox Mid-360; public underground sequences and Gazebo vehicle; drivetrain not established in the selected passages (pp. 8-11).
- boundary_platform: yes
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR; the capture rig includes an IMU, but the evaluated DR-ICP framework does not integrate IMU measurements
- compute: Intel i5-12600KF workstation, LeGO-LOAM extension (p. 8).
- compute_location: desktop-offline
- summary_result: Directional detection changes feature selection and registration within a pure-LiDAR tunnel pipeline.
- summary_limitation: Curved tunnels, altitude drift and fixed descriptor weighting remain limitations; IMU integration is future work (p. 15).
- survey_included: yes
- verification_level: light

## Problem

Long tunnel geometry leaves weak registration directions that ordinary feature selection may not constrain.

## Mechanism

Detects directionality from a spherical normal histogram, selects features with informative angular variation, excludes lines aligned with degeneracy, and weights feature registration (pp. 2, 7-8).

## Baselines and controls

Degeneracy comparisons include Zhang et al. and X-ICP; dataset discussion distinguishes pure-LiDAR methods from FAST-LIO2 using inertial information (pp. 10-11).

## Platform and setup

Tunnel acquisition platform with Livox Mid-360; public underground sequences and Gazebo vehicle; drivetrain not established in the selected passages (pp. 8-11).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Do not infer inertial robustness from the capture hardware. The field reference is a separately collected marker-derived map, not a timestamp-matched global trajectory (p. 15).

## Sensors

LiDAR; the capture rig includes an IMU, but the evaluated DR-ICP framework does not integrate IMU measurements.

## Compute and latency

Intel i5-12600KF workstation, LeGO-LOAM extension (p. 8).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Curved tunnels, altitude drift and fixed descriptor weighting remain limitations; IMU integration is future work (p. 15).

## Transfer conditions

Do not infer inertial robustness from the capture hardware. The field reference is a separately collected marker-derived map, not a timestamp-matched global trajectory (p. 15).

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

The native export is preserved separately; the documented early-access year correction is 2026. Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 15, Selected source passage.** "IMU data have not yet been integrated into the current framework."
  Separates feature-based compensation from added sensing; supplies a counterexample to universal superiority because FAST-LIO2 wins the inspected HILTI sequence discussion.

## Survey-usable statements

### Supported

- Directional detection changes feature selection and registration within a pure-LiDAR tunnel pipeline. Separates feature-based compensation from added sensing; supplies a counterexample to universal superiority because FAST-LIO2 wins the inspected HILTI sequence discussion.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Do not infer inertial robustness from the capture hardware. The field reference is a separately collected marker-derived map, not a timestamp-matched global trajectory (p. 15).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 2, 7, 8, 9, 10, 11, 15; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Light Detection and Ranging (LiDAR) has been extensively deployed in structured environments, such as urban roadways and indoor facilities, owing to its superior ranging accuracy and robust anti-interference capabilities. However, its performance degrades significantly in unstructured environments like underground tunnels, in such scenarios, the scarcity of distinctive geometric features and insufficient spatial constraints frequently induce degeneracy in LiDAR-based Simultaneous Localization and Mapping (SLAM), leading to severe registration drift. To address this challenge, this paper proposes a Degeneracy-Robust Iterative Closest Point (DR-ICP) method that integrates point cloud normal analysis with multi-scale curvature constraints. The proposed approach first utilizes a degeneracy detection mechanism to ascertain the occurrence and direction of degeneracy by exploiting statistical properties of point cloud normals. Building on this detection, an adaptive multi-scale strategy is applied to extract subtle concave-convex and linear features from optimal neighborhoods. Furthermore, a weighted registration scheme ensures reliable alignment in degenerate regions by enhancing the representation of valid features. Extensive simulations and real-world tunnel experiments demonstrate that the proposed DR-ICP effectively identifies degenerate directions and achieves superior robustness and positioning accuracy in complex underground scenarios.
