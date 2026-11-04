# A Real-Time Degeneracy Sensing and Compensation Method for Enhanced LiDAR SLAM

## Metadata

| Field | Value |
|---|---|
| ID | S31 |
| Title | A Real-Time Degeneracy Sensing and Compensation Method for Enhanced LiDAR SLAM |
| Authors | Liao, Zongbo and Zhang, Xuanxuan and Zhang, Tianxiang and Li, Zhi and Zheng, Zhenqi and Wen, Zhichao and Li, You |
| Venue | IEEE Transactions on Intelligent Transportation Systems |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tits.2024.3524394](https://doi.org/10.1109/tits.2024.3524394) |
| Official URL | https://ieeexplore.ieee.org/document/10892345/ |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2025-Degeneracy-Compensation-S31/paper.pdf` and `02-fulltext/T1-perception-localization/2025-Degeneracy-Compensation-S31/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2025-Degeneracy-Compensation-S31/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Own campus/xhl robot recordings plus R3LIVE, Hilti and Newer College sequences; human operators follow predefined routes (p. 8).
- boundary_platform: no
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR and IMU with calibrated extrinsics and time synchronization
- compute: Real-time estimator is reported; exact benchmark processor/placement was not retained from selected passages.
- compute_location: desktop-offline
- summary_result: Detected degeneracy triggers state compensation using the inertial channel.
- summary_limitation: The initial data-collection phase can miss degeneracy and compromise later assessments (p. 7).
- survey_included: yes
- verification_level: light

## Problem

A fixed degeneracy threshold may not transfer across environments and LiDAR scanning patterns.

## Mechanism

Separates translational/rotational condition-number factors, adapts degeneracy decisions using DBSCAN, and fuses transformed IMU motion into the affected LiDAR state (pp. 3, 7).

## Baselines and controls

The selected experiments compare degeneracy factors and thresholding across solid-state/spinning sensor sequences; no numeric table cells retained.

## Platform and setup

Own campus/xhl robot recordings plus R3LIVE, Hilti and Newer College sequences; human operators follow predefined routes (p. 8).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. DBSCAN decisions require an initialized history; adaptation does not remove the need for IMU quality, extrinsic calibration and timing.

## Sensors

LiDAR and IMU with calibrated extrinsics and time synchronization.

## Compute and latency

Real-time estimator is reported; exact benchmark processor/placement was not retained from selected passages.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

The initial data-collection phase can miss degeneracy and compromise later assessments (p. 7).

## Transfer conditions

DBSCAN decisions require an initialized history; adaptation does not remove the need for IMU quality, extrinsic calibration and timing.

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

- **p. 7, Selected source passage.** "if the LiDAR degenerates during this initial phase, our algorithm may fail to accurately detect such degeneracy."
  Provides an implemented detection-to-estimation response while qualifying claims of threshold-free immediate robustness.

## Survey-usable statements

### Supported

- Detected degeneracy triggers state compensation using the inertial channel. Provides an implemented detection-to-estimation response while qualifying claims of threshold-free immediate robustness.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. DBSCAN decisions require an initialized history; adaptation does not remove the need for IMU quality, extrinsic calibration and timing.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 7, 8, 11; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

LiDAR is widely used in Simultaneous Localization and Mapping (SLAM) and autonomous driving. The LiDAR odometry is of great importance in multi-sensor fusion. However, in some unstructured environments, the point cloud registration cannot constrain the poses of the LiDAR due to its sparse geometric features, which leads to the degeneracy of multi-sensor fusion accuracy. To address this problem, we propose a novel real-time approach to sense and compensate for the degeneracy of LiDAR. Firstly, this paper introduces the degeneracy factor with clear meaning, which can measure the degeneracy of LiDAR. Then, the Density-Based Spatial Clustering of Applications with Noise (DBSCAN) clustering method adaptively perceives the degeneracy with better environmental generalization. Finally, the degeneracy perception results are utilized to fuse LiDAR and IMU, thus effectively resisting degeneracy effects. Experiments on our dataset show the method’s high accuracy and robustness and validate our algorithm’s adaptability to different environments and LiDAR scanning modalities.
