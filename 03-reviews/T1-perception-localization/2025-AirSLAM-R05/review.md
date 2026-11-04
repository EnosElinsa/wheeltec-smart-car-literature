# AirSLAM: An Efficient and Illumination-Robust Point-Line Visual SLAM System

## Metadata

| Field | Value |
|---|---|
| ID | R05 |
| Title | AirSLAM: An Efficient and Illumination-Robust Point-Line Visual SLAM System |
| Authors | Kuan Xu, Yuefan Hao, Shenghai Yuan, Chen Wang, and Lihua Xie |
| Venue | IEEE Transactions on Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3539171](https://doi.org/10.1109/tro.2025.3539171) |
| Official URL | https://ieeexplore.ieee.org/document/10874215/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2025-AirSLAM-R05/paper.pdf` and `02-fulltext/T1-perception-localization/2025-AirSLAM-R05/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2025-AirSLAM-R05/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: Public visual datasets with onboard, dynamic and low illumination (OIVIO, UMA-VI and others) and map-reuse sequences (pp. 10-14).
- boundary_platform: yes
- degradation: visual-degradation
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Stereo camera and IMU
- compute: 73 Hz on an i9-13900 CPU with RTX 4080 PC and 40 Hz on Jetson AGX Orin (p. 16).
- compute_location: desktop-offline
- summary_result: Point-line features and map reuse improve accuracy and relocalization under illumination changes; the system runs at 40 Hz on an embedded Jetson Orin (pp. 13-16).
- summary_limitation: Relies on enough line features; in unstructured environments the system degrades to a point-only system (p. 17).
- survey_included: yes
- verification_level: light

## Problem

Visual SLAM fails under short-term illumination changes and cannot reuse maps across long-term lighting changes.

## Mechanism

A unified CNN (PLNet) detects keypoints and structural lines, a GNN matches features, and a multistage relocalization reuses a point-line map with a structure graph; networks are accelerated with TensorRT (pp. 3-10).

## Baselines and controls

State-of-the-art VO and vSLAM systems including ORB-SLAM3, OKVIS, Basalt, PL-SLAM and DROID-SLAM (pp. 11-16).

## Platform and setup

Dataset evaluation with onboard, dynamic and low illumination plus an efficiency test on Jetson Orin (pp. 10-16). Public visual datasets with onboard, dynamic and low illumination (OIVIO, UMA-VI and others) and map-reuse sequences (pp. 10-14).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. Dataset replay and an embedded timing test; no closed-loop navigation.

## Sensors

Stereo camera and IMU.

## Compute and latency

73 Hz on an i9-13900 CPU with RTX 4080 PC and 40 Hz on Jetson AGX Orin (p. 16).

## Key quantitative results

- Ours-Jetson runs visual-inertial odometry at 40.3 FPS versus 73.1 FPS for Ours-PC (p. 16, table).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- AirSLAM relies on enough line features and is best suited to man-made environments; it degrades to a point-only system in unstructured environments (p. 17).

## Transfer conditions

Designed for warehouse robots; transfer to vegetation or unstructured terrain loses the line constraints.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

The authors state that this article extends their conference paper AirVO (p. 2); AirVO is not in the library, and this journal article is counted once.

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

- **p. 13, Sec. VII-C.** "The onboard illumination has almost no impact on our AirSLAM and ORB-SLAM3, however, it reduces the accuracy of OKVIS, Basalt, and PL-SLAM."
  Illumination robustness depends on the baseline.
- **p. 17, Sec. VIII.** "In unstructured environments, the system degrades into a point-only system."
  Author-stated scope limit.

## Survey-usable statements

### Supported

- Learned point-line features with map reuse address illumination change at embedded rates.

### Not supported

- Relocalization accuracy is not linked to navigation recovery.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 10, 13, 16, 17; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

In this article, we present an efficient visual simultaneous localization and mapping (SLAM) system designed to tackle both short-term and long-term illumination challenges. Our system adopts a hybrid approach that combines deep learning techniques for feature detection and matching with traditional back-end optimization methods. Specifically, we propose a unified convolutional neural network that simultaneously extracts keypoints and structural lines. These features are then associated, matched, triangulated, and optimized in a coupled manner. In addition, we introduce a lightweight relocalization pipeline that reuses the built map, where keypoints, lines, and a structure graph are used to match the query frame with the map. To enhance the applicability of the proposed system to real-world robots, we deploy and accelerate the feature detection and matching networks using C++ and NVIDIA TensorRT. Extensive experiments conducted on various datasets demonstrate that our system outperforms other state-of-the-art visual SLAM systems in illumination-challenging environments. Efficiency evaluations show that our system can run at a rate of 73 Hz on a PC and 40 Hz on an embedded platform.
