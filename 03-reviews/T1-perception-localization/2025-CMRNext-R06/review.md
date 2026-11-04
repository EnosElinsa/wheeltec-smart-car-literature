# CMRNext: Camera to LiDAR Matching in the Wild for Localization and Extrinsic Calibration

## Metadata

| Field | Value |
|---|---|
| ID | R06 |
| Title | CMRNext: Camera to LiDAR Matching in the Wild for Localization and Extrinsic Calibration |
| Authors | Daniele Cattaneo, and Abhinav Valada |
| Venue | IEEE Transactions on Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3546784](https://doi.org/10.1109/tro.2025.3546784) |
| Official URL | https://ieeexplore.ieee.org/document/10908048/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2025-CMRNext-R06/paper.pdf` and `02-fulltext/T1-perception-localization/2025-CMRNext-R06/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2025-CMRNext-R06/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: road-vehicle
- platform: Autonomous-driving datasets including KITTI; in-house self-driving perception car, quadruped and quadcopter recordings for zero-shot tests (pp. 7-8, 15).
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: Monocular camera with a LiDAR map or LiDAR scan; camera intrinsics required
- compute: Workstation with RTX 2080 Ti for runtime; not real time (pp. 17).
- compute_location: desktop-offline
- summary_result: Camera-to-LiDAR matching generalizes zero-shot to new sensor setups, with median 6.21 cm and 0.23 degree localization error on KITTI sequence 00 (p. 17).
- summary_limitation: Trained only on driving data, not yet real time, and training requires ground-truth poses and correct intrinsics (p. 17).
- survey_included: yes
- verification_level: light

## Problem

Learned camera-in-LiDAR-map localization and calibration usually overfit to one sensor setup.

## Mechanism

Point-pixel matching is reformulated as optical flow between camera images and projected LiDAR, followed by PnP with RANSAC for the relative pose; iterative refinement and temporal aggregation support calibration (pp. 3-7, 15).

## Baselines and controls

CMRNet, I2D-Loc, I2D-Loc++ and LCCNet among camera-dependent and agnostic methods (pp. 9-14).

## Platform and setup

Four driving datasets plus three in-house platforms; localization experiments provide an initial pose per frame (pp. 7-10). Autonomous-driving datasets including KITTI; in-house self-driving perception car, quadruped and quadcopter recordings for zero-shot tests (pp. 7-8, 15).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Offline evaluation on driving data and in-house recordings; no closed-loop navigation.

## Sensors

Monocular camera with a LiDAR map or LiDAR scan; camera intrinsics required.

## Compute and latency

Workstation with RTX 2080 Ti for runtime; not real time (pp. 17).

## Key quantitative results

- Median translation and rotation errors of 6.21 cm and 0.23 degrees on KITTI sequence 00 (p. 17).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Generalization to off-road or mining environments is likely limited because training uses driving datasets (p. 17).
- The method is not yet capable of real-time performance (p. 17).
- Training requires ground-truth poses and correct intrinsic parameters (p. 17).

## Transfer conditions

Localization requires an initial pose hypothesis and a current LiDAR map; off-road wheeled robots fall outside the training domain.

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

- **p. 10, Sec. IV-H.** "However, in real-world scenarios, this initial pose might not always be available, such as in GNSS-denied environments."
  Qualifies the per-frame initial-pose assumption.
- **p. 17, Sec. V.** "Second, while our method is faster than existing camera-agnostic approaches, it is not yet capable of real-time performance."
  Author-stated runtime limit.

## Survey-usable statements

### Supported

- Cross-modal camera-to-LiDAR-map matching transfers across sensor setups without retraining.

### Not supported

- The method is not shown in real-time navigation or under map change.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 7, 8, 10, 15, 17; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Light detection and rangings (LiDARs) are widely used for mapping and localization in dynamic environments. However, their high cost limits their widespread adoption. On the other hand, monocular localization in LiDAR maps using inexpensive cameras is a cost-effective alternative for large-scale deployment. Nevertheless, most existing approaches struggle to generalize to new sensor setups and environments, requiring retraining or fine-tuning. In this article, we present CMRNext, a novel approach for camera-LiDAR matching that is independent of sensor-specific parameters, generalizable, and can be used in the wild for monocular localization in LiDAR maps and camera-LiDAR extrinsic calibration. CMRNext exploits recent advances in deep neural networks for matching cross-modal data and standard geometric techniques for robust pose estimation. We reformulate the point-pixel matching problem as an optical flow estimation problem and solve the perspective-n-point problem based on the resulting correspondences to find the relative pose between the camera and the LiDAR point cloud. We extensively evaluate CMRNext on six different robotic platforms, including three publicly available datasets and three in-house robots. Our experimental evaluations demonstrate that CMRNext outperforms existing approaches on both tasks and effectively generalizes to previously unseen environments and sensor setups in a zero-shot manner.
