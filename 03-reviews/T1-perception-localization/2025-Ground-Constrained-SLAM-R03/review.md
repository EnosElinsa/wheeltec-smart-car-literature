# Robust Ground Constrained SLAM for Mobile Robot With Sparse-Channel LiDAR

## Metadata

| Field | Value |
|---|---|
| ID | R03 |
| Title | Robust Ground Constrained SLAM for Mobile Robot With Sparse-Channel LiDAR |
| Authors | Shaocong Wang, Fengkui Cao, Ting Wang, Shiliang Shao, and Lianqing Liu |
| Venue | IEEE Transactions on Intelligent Vehicles |
| Year | 2025 (DOI year 2024) |
| Type | journal |
| DOI | [10.1109/tiv.2024.3451137](https://doi.org/10.1109/tiv.2024.3451137) |
| Official URL | https://ieeexplore.ieee.org/document/10654559/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2025-Ground-Constrained-SLAM-R03/paper.pdf` and `02-fulltext/T1-perception-localization/2025-Ground-Constrained-SLAM-R03/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2025-Ground-Constrained-SLAM-R03/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: GroundRobotDataset recorded by a ground robot with sparse-channel LiDAR, IMU and RTK; drive type not stated in the inspected passages (p. 7, Fig. 6).
- boundary_platform: no
- degradation: lidar-degeneracy, terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Sparse-channel 3D LiDAR (VLP-16 class) and IMU gyroscope; RTK or wheel odometry with offline registration as reference (p. 7)
- compute: Runtime section exists (p. 11); processor not inspected in this reading.
- compute_location: desktop-offline
- summary_result: Ground-normal constraints and intensity features reduce vertical drift and corridor degradation relative to baseline LiDAR SLAM on the authors' dataset (p. 11).
- summary_limitation: Ground-change detection can fail when ground changes are below threshold, and only LiDAR and gyroscope are fused (pp. 10-11).
- survey_included: yes
- verification_level: light

## Problem

Sparse-channel LiDAR SLAM drifts vertically and degrades in long corridors and featureless walls.

## Mechanism

A hybrid scan-to-submap ICP and scan-to-map feature matching front end; a ground constraint from the principal normal of planar ground; intensity features; and a factor graph joining feature, IMU pre-integration and ground factors (pp. 3-7).

## Baselines and controls

State-of-the-art LiDAR SLAM baselines including LIO-SAM, and ablations of the ground constraint module (pp. 8-10).

## Platform and setup

Indoor corridor, obstacle-crossing and outdoor sequences, including a tidal-flat field sequence with changing slopes (pp. 7-10). GroundRobotDataset recorded by a ground robot with sparse-channel LiDAR, IMU and RTK; drive type not stated in the inspected passages (p. 7, Fig. 6).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Authors' recorded robot data evaluated offline against RTK or registration-based references.

## Sensors

Sparse-channel 3D LiDAR (VLP-16 class) and IMU gyroscope; RTK or wheel odometry with offline registration as reference (p. 7).

## Compute and latency

Runtime section exists (p. 11); processor not inspected in this reading.

## Key quantitative results

- The method reports lower drift, particularly vertical drift, than the baseline methods on the GroundRobotDataset (p. 11).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- When ground changes are not large enough, failure of ground-change detection may cause drift over time (p. 10).
- Only the LiDAR and IMU gyroscope are used; cameras and wheel encoders are future work (p. 11).

## Transfer conditions

Assumes locally planar ground segments that can be detected; references based on wheel odometry and registration indoors are not independent of LiDAR geometry.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity; no other version is in the library.

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

- **p. 10, Sec. IV-D.** "Therefore, our method has limited performance in such scenarios with small and continuous ground changes."
  Author-stated limit of the ground prior.
- **p. 7, Sec. IV-A.** "For RTK-denied indoor sequences, the groundtruth are collected by the wheel odom combine point cloud offline registration."
  Shows reference dependence for indoor sequences.

## Survey-usable statements

### Supported

- A ground-geometry prior reduces vertical drift with sparse-channel LiDAR on recorded ground-robot data.

### Not supported

- Indoor errors are not measured against a reference independent of LiDAR registration.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 7, 8, 10, 11; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Although LiDAR SLAM has been widely studied over the past decades, it suffers from degradation situation, particularly for sparse-channel LiDAR. This study proposes a hybrid LiDAR SLAM method combining scan to LiDAR-centric sliding submap ICP and scan-to-map feature points matching to adapt to unstructured environments and degraded corridors. First, a ground constraint module based on the principal normal of the planar ground is proposed to avoid vertical drift. To address the lack of geometrical features in corridors and environments with large-scale featureless walls, intensity features combined with geometrical features are adopted for scan-to-map registration. Finally, a joint optimization module integrates the feature correlation, the IMU pre-integration, and the ground constraint into a factor graph to perform low-drift SLAM. Extensive experiments are conducted on the GroundRobotDataset, which include challenging degradation scenarios such as long corridor, obstacle crossing and unstructured outdoor environment with large-size walls in weak texture. Our method achieves better accuracy and robustness than state-of-the-art methods, particularly in inhibiting vertical drift.
