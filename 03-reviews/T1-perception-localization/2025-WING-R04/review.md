# WING: Wheel-Inertial Neural Odometry With Ground Manifold Constraints

## Metadata

| Field | Value |
|---|---|
| ID | R04 |
| Title | WING: Wheel-Inertial Neural Odometry With Ground Manifold Constraints |
| Authors | Chenxing Jiang, Kunyi Zhang, Sheng Yang, Shaojie Shen, Chao Xu, and Fei Gao |
| Venue | IEEE Transactions on Intelligent Vehicles |
| Year | 2025 (DOI year 2024) |
| Type | journal |
| DOI | [10.1109/tiv.2024.3429167](https://doi.org/10.1109/tiv.2024.3429167) |
| Official URL | https://ieeexplore.ieee.org/document/10599809/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2025-WING-R04/paper.pdf` and `02-fulltext/T1-perception-localization/2025-WING-R04/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2025-WING-R04/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: KAIST Urban (cars) and NCLT (wheeled robot) datasets (p. 9).
- boundary_platform: yes
- degradation: wheel-slip
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: IMU and wheel encoders only
- compute: NVIDIA RTX 4090 and Intel Core i9-13900K desktop for runtime evaluation (p. 12).
- compute_location: desktop-offline
- summary_result: Learned IMU de-biasing, wheel-velocity correction and a continuous ground-manifold soft constraint outperform open-source interoceptive-only odometry baselines on two public datasets (p. 12).
- summary_limitation: No limitation is stated in the inspected passages; low-order manifolds can reduce accuracy where the ground departs from the assumption (p. 11).
- survey_included: yes
- verification_level: light

## Problem

Interoceptive-only odometry is needed when cameras, GNSS or LiDAR degrade, but raw wheel and IMU data drift.

## Mechanism

Networks correct IMU biases and wheel-encoder errors from skidding and vertical bouncing and estimate time-varying uncertainty; a dual cubic B-spline ground manifold provides a soft constraint in a space-based sliding-window filter (pp. 4-8).

## Baselines and controls

Learning-based interoceptive-only odometry methods, with ablations of network-corrected velocity, learned covariance and manifold constraints (pp. 9-11).

## Platform and setup

Public driving and robot datasets; no closed-loop or hardware deployment (p. 9). KAIST Urban (cars) and NCLT (wheeled robot) datasets (p. 9).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. Dataset replay. The network is trained on the dataset domains, so transfer to new chassis and terrain is not established.

## Sensors

IMU and wheel encoders only.

## Compute and latency

NVIDIA RTX 4090 and Intel Core i9-13900K desktop for runtime evaluation (p. 12).

## Key quantitative results

- Ablations attribute gains to network-corrected velocity, learned covariance and the continuous manifold constraint (pp. 11-12).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- In some sequences a low-order manifold assumption limits the degrees of freedom and performs worse than no manifold constraint (p. 11).

## Transfer conditions

Requires training data from the target platform and continuous ground; abrupt steps or loose terrain violate the manifold prior.

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

- **p. 11, Sec. VII-C.** "Compared to the segmented manifold, The variation in improvement obtained from using the continuous manifold arises from the extent to which the actual ground adheres to our assumption."
  Benefit depends on the ground satisfying the manifold assumption.
- **p. 10, Sec. VII-C.** "This is because vehicles are more likely to skid during turning, whereas vertical bouncing is relatively rare on smooth urban roads."
  Links learned wheel corrections to the dataset motion regime.

## Survey-usable statements

### Supported

- A learned wheel-inertial fallback with a ground prior improves interoceptive odometry on public data.

### Not supported

- The paper does not show switching to this fallback when exteroceptive sensing fails on a robot.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 9, 10, 11, 12; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

In this paper, we propose an interoceptive-only odometry system for ground robots with neural network processing and soft constraints based on the assumption of a globally continuous ground manifold. Exteroceptive sensors such as cameras, GPS and LiDAR may encounter difficulties in scenarios with poor illumination, indoor environments, dusty areas and straight tunnels. Therefore, improving the pose estimation accuracy only using interoceptive sensors is important to enhance the reliability of navigation system even in degrading scenarios mentioned above. However, interoceptive sensors like IMU and wheel encoders suffer from large drift due to noisy measurements. To overcome these challenges, the proposed system trains deep neural networks to correct the measurements from IMU and wheel encoders, while considering their uncertainty. Moreover, because ground robots can only travel on the ground, we model the ground surface as a globally continuous manifold using a dual cubic B-spline manifold to further improve the estimation accuracy by this soft constraint. A novel space-based sliding-window filtering framework is proposed to fully exploit the $C^{2}$ continuity of ground manifold soft constraints and fuse all the information from raw measurements and neural networks in a yaw-independent attitude convention. Extensive experiments demonstrate that our proposed approach can outperform state-of-the-art learning-based interoceptive-only odometry methods.
