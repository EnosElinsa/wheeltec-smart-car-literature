# Visual-Inertial-Wheel Odometry With Wheel-Aided Maximum-a-Posteriori Initialization for Ground Robots

## Metadata

| Field | Value |
|---|---|
| ID | M24 |
| Title | Visual-Inertial-Wheel Odometry With Wheel-Aided Maximum-a-Posteriori Initialization for Ground Robots |
| Authors | Wugen Zhou, Youqi Pan, Junbin Liu, Tao Wang, and Hongbin Zha |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 5, pp. 4814-4821 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3386448](https://doi.org/10.1109/lra.2024.3386448) |
| Official URL | https://ieeexplore.ieee.org/document/10494859/ |
| Theme folder | T1-perception-localization |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T1-perception-localization/2024-VIWO-MAP-M24/paper.pdf` and `02-fulltext/T1-perception-localization/2024-VIWO-MAP-M24/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2024-VIWO-MAP-M24/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: video-only-hardware
- platform_class: wheeled-unspecified
- platform: unnamed wheeled robot with RealSense D455 and NVIDIA Xavier; KAIST Urban vehicle and OpenLORIS wheeled-robot datasets
- boundary_platform: no
- degradation: visual-degradation
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: monocular or stereo camera, IMU, wheel encoders
- compute: Intel Core i9 3.6 GHz desktop, about 30 ms (KAIST) and 12.5 ms (OpenLORIS) per frame; NVIDIA Xavier on the authors' robot
- compute_location: mixed
- summary_result: OpenLORIS mean initialization scale error 3.18% versus 12.84% for ORB-SLAM3; KAIST trajectory error below 0.2% of length on four sequences.
- summary_limitation: Wheel slippage during initialization can yield a less accurate state, and the planar bundle adjustment assumes approximately planar ground.
- survey_included: yes
- verification_level: light

## Problem

Visual-inertial odometry on ground robots has unobservable metric scale
under straight, constant-acceleration motion, fails to initialize at high
speed, and loses tracking when vision drops under illumination change or low
texture.

## Mechanism

Wheel-encoder readings are tightly coupled with IMU preintegration.
Initialization is a three-step maximum-a-posteriori (MAP) estimate:
vision-only, then inertial-wheel, then visual-inertial-wheel. During visual
failure the estimator propagates with inertial-wheel joint kinematics. Wheel
residuals and an approximately planar ground constraint enter the local and
global bundle adjustment.

## Baselines and controls

The main comparator is ORB-SLAM3. On KAIST urban39 the method of Liu et al.
with online multi-sensor calibration is also compared. A variant without the
planar constraint serves as an ablation.

## Platform and setup

(i) KAIST Urban vehicle sequences with stereo camera, IMU, wheel encoder, and
GPS ground truth. (ii) OpenLORIS indoor wheeled-robot sequences with a
RealSense D435i, wheel encoder, and LiDAR, including market and corridor
sequences with illumination and texture stress. (iii) The authors' wheeled
robot with a RealSense D455 (with IMU) and an NVIDIA Xavier; its results are
shown only in a video.

## Evidence type and transfer

All tabulated numbers come from public datasets (a road vehicle and an
indoor wheeled robot). The authors' own robot experiment is reported only
in a video without metrics; the legacy extraction does not record whether
the estimator ran online during that experiment, so it is coded as recorded
robot data, which was not verified. The chassis model and drive type are not
named.

## Sensors

Monocular or stereo camera, IMU, and wheel encoders: the KAIST vehicle stereo
camera, IMU, and wheel encoders; the OpenLORIS RealSense D435i and wheel
encoders; a RealSense D455 on the authors' robot. GPS (KAIST) provides ground
truth only.

## Compute and latency

Public-dataset timing is from a desktop Intel Core i9 at 3.6 GHz with 64 GB:
about 30 ms per frame (33 Hz) on KAIST and 12.5 ms (80 Hz) on 848x480
OpenLORIS images. The authors' robot carries an NVIDIA Xavier; no timing is
recorded for it.

## Key quantitative results

- KAIST: ORB-SLAM3 initialization fails on urban26 and urban33, while the proposed MAP initialization succeeds in about 1.5 s (p. 5).
- KAIST: trajectory positional error below 0.2% of the trajectory length on the four reported sequences, about 40% better with the planar constraint (p. 6).
- KAIST urban39: the method of Liu et al. with online multi-sensor calibration is more accurate than the proposed method (p. 6).
- OpenLORIS: mean initialization scale error 3.18% versus 12.84% for ORB-SLAM3 (p. 7).
- OpenLORIS: ORB-SLAM3 cannot finish market1 and corridor5 under illumination and texture stress, while the proposed odometry continues (p. 8).
- Timing: about 30 ms per frame (33 Hz) on KAIST (p. 6) and 12.5 ms (80 Hz) on OpenLORIS (p. 8), both on the desktop CPU.

## Stated limitations

- Wheel slippage during initialization can yield a less accurate state (p. 8).
- The planar bundle adjustment assumes that the robot moves on approximately planar ground (p. 8).

## Transfer conditions

Public-dataset numbers are from a desktop CPU. The authors' own run is on an
Xavier with a D455, and the chassis is not named. The planar constraint
needs approximately planar ground, and wheel slip during initialization
lowers accuracy.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. I, p. 2 | "Moreover, we employ wheel measurements to aid IMU in obtaining robust tracking when the visual observation fails due to illumination changes or low-texture regions." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | weak | Sec. V-D, p. 8 | "All experiments are performed on a wheeled robot, equipped with a realsense D455 (with IMU) and an Nvidia Xavier processor." |

## Page-cited excerpts

- **p. 2, Sec. I.** "Moreover, we employ wheel measurements to aid IMU in obtaining robust tracking when the visual observation fails due to illumination changes or low-texture regions."
  Visual failure under illumination change and low texture motivates the inertial-wheel propagation.
- **p. 8, Sec. V-D.** "All experiments are performed on a wheeled robot, equipped with a realsense D455 (with IMU) and an Nvidia Xavier processor."
  The only own-robot evidence; it names no chassis, and its results are shown in a video.

## Survey-usable statements

### Supported

- Wheel-aided MAP initialization initialized on KAIST sequences where ORB-SLAM3 failed, and reduced the OpenLORIS mean scale error from 12.84% to 3.18% (numbers from a light review; re-check before citing).
- Inertial-wheel propagation kept tracking on OpenLORIS sequences where ORB-SLAM3 lost track under illumination and texture stress.

### Not supported

- The method is the most accurate on every KAIST sequence: Liu et al. are more accurate on urban39.
- The method was validated quantitatively on the authors' own robot: that experiment is shown only in a video.
- The method handles wheel slip or non-planar ground: the authors name both as limits.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); no legacy quote dropped; the Liu et al. urban39 comparison moved from Stated limitations to Key quantitative results
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

In recent years, Visual-Inertial Odometry (VIO) has demonstrated remarkable results using low-cost and complementary sensors. However, these methods often encounter initialization failure and suffer reduced robustness or low trajectory accuracy under challenging scenarios. In this letter, we propose a visual-inertial-wheel odometry that provides robust and accurate initialization and high-accuracy estimates for ground robots. We propose a novel Maximum-a-Posteriori (MAP) initialization, coupled with wheel encoder measurements, to address the unobservable scales of the visual-inertial-only initialization when the vehicle moves straight at the beginning. Moreover, we leverage the wheel readings to construct an inertial-wheel joint propagation and optimization, leading to robust pose tracking when encountering weak visual observations. Additionally, we incorporate wheel measurements and planar constraints into the local and global Bundle Adjustment (BA) for positioning, significantly enhancing localization accuracy when the robot moves on an approximately planar ground. Experiments on the public datasets demonstrate the effectiveness and efficiency of our initialization, the robustness of pose tracking, and the improved accuracy of the entire trajectory.
