# Tightly-coupled LiDAR-IMU-wheel odometry with an online neural kinematic model learning via factor graph optimization

## Metadata

| Field | Value |
|---|---|
| ID | E04 |
| Title | Tightly-coupled LiDAR-IMU-wheel odometry with an online neural kinematic model learning via factor graph optimization |
| Authors | Taku Okawara, Kenji Koide, Shuji Oishi, Masashi Yokozuka, Atsuhiko Banno, Kentaro Uno, and Kazuya Yoshida |
| Venue | Robotics and Autonomous Systems, vol. 187, article 104929 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1016/j.robot.2025.104929](https://doi.org/10.1016/j.robot.2025.104929) |
| Official URL | https://linkinghub.elsevier.com/retrieve/pii/S0921889025000156 |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2025-Neural-Wheel-LIO-E04/paper.pdf` and `02-fulltext/T1-perception-localization/2025-Neural-Wheel-LIO-E04/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2025-Neural-Wheel-LIO-E04/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: few-trials
- platform_class: skid-steer
- platform: Rover Robotics Rover mini (four-wheel skid-steer)
- boundary_platform: no
- degradation: lidar-degeneracy, wheel-slip, terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: Livox AVIA narrow-FOV LiDAR facing sideways, IMU, four wheel encoders; Livox MID-360 and its IMU only for training labels and reference trajectories
- compute: laptop with Ryzen 9 5900HX and RTX 3060 Laptop GPU; 31 ms total per frame, about 10 ms of it online training
- compute_location: not-reported
- summary_result: On three skid-steer sequences, the method reaches 1.07, 0.25, and 0.41 m ATE versus 3.29, 0.59, and 0.99 m for the same network without online learning.
- summary_limitation: The authors assume that the network is trained in feature-rich areas first and that terrain does not change drastically while entering degenerate areas.
- survey_included: yes
- verification_level: light

## Problem

On skid-steer wheeled robots in geometrically degenerate environments, a fixed linear wheel kinematic model cannot represent high-speed side slip or drifting, and an offline-trained network does not adapt to terrain changes.

## Mechanism

A factor graph jointly optimizes VGICP scan-matching factors, IMU preintegration, and a neural adaptive odometry factor over pose, velocity, IMU biases, and the 100-dimensional weights and biases of an MLP. The network has an offline, general feature extractor and decoder and a small online terrain block. Inputs are the four wheel angular velocities and IMU velocity increments and yaw rate; the output is a 2D twist. The online parameters have a random-walk factor. When the smallest Hessian eigenvalue indicates point cloud degeneracy, the MLP and the IMU biases are frozen so that false supervision does not corrupt them. Implementation: ROS 2 Humble, GTSAM iSAM2, PyTorch and LibTorch.

## Baselines and controls

The fixed network (Ours without online learning), the authors' online full linear model (IEEE Access 2024), FAST-LIO-Multi-Sensor-Fusion, and FAST-LIO2, plus pairings of the same network with parameters of the wrong terrain. The algorithm comparison uses a Livox AVIA facing sideways to restrict the field of view on purpose, so it does not show that FAST-LIO2 fails in all omnidirectional LiDAR settings.

## Platform and setup

A real Rover Robotics Rover mini four-wheel skid-steer robot, driven up to 3 m/s (wheel angular speed 36 rad/s) to induce drifting. Three sequences: a long indoor corridor, brick and indoor-outdoor stone-tile transitions, and concrete to grass. An offline set of eight terrains is split 70/30 into training and validation. The reference trajectory comes from batch optimization of a Livox MID-360 and IMU against a FARO Focus3D X330 prior map, not from an independent motion-capture system. The work is odometry estimation; there is no full autonomous navigation and no test on the reference platform.

## Evidence type and transfer

Real wheeled-robot localization on several terrains with network ablations. Degeneracy is induced by the narrow side-facing field of view and by fewer than 100 points near walls; it is not a statistic of natural failures over many days.

## Sensors

Estimation uses the Livox AVIA facing the robot's Y side (point clouds 10 Hz), an IMU at 200 Hz, and four wheel encoders at 60 Hz. The omnidirectional MID-360 point clouds and its IMU are used only offline for training labels and reference trajectories; the FARO prior map is not an input of the online system. The network regresses only a planar twist; the 3D extension pads zeros and treats roughness through the covariance.

## Compute and latency

Offline training on an i7-13700KF with an RTX 4080 took about 2.5 h (Adam, 3000 epochs). Online timing on a Ryzen 9 5900HX with an RTX 3060 Laptop GPU: about 10 ms for online training and 31 ms for the whole frame, including point cloud preprocessing, preintegration, and optimization (Table 5); fixed network 17 ms, linear model 23 ms, FAST-LIO2 5 ms; the scan period is 100 ms at 10 Hz. The method cannot be called CPU-only or low-power onboard; no tail latency or power is reported. The legacy extraction does not say whether the laptop rode on the robot.

## Key quantitative results

- ATE on the three sequences: proposed method 1.07 ± 0.35, 0.25 ± 0.10, and 0.41 ± 0.18 m versus the fixed network 3.29 ± 2.42, 0.59 ± 0.53, and 0.99 ± 0.51 m and the online linear model 18.80, 2.23, and 0.98 m; the ± values are not explained as confidence intervals of repeated trials (p. 10, Table 4).
- RTE of the proposed method on the three sequences: 0.08, 0.12, and 0.09 m (p. 10, Table 4).
- Network alone, mean over eight terrains, per 1 m: 0.021 m translational RTE and 0.25 deg/m rotational, versus 0.031 m and 0.23 deg/m for a single unified network, so the rotation error is not lower (p. 9, Table 1).
- Sequence 1: 572 of 828 frames degenerate (69%) and 189 of 828 missing (23%); the text and table note say 91%, while 761/828 is about 91.9%; LiDAR is not absent for the whole run (p. 10, Table 3).
- Total processing time per frame: 0.031 s (proposed) versus 0.017 s (fixed network), 0.023 s (online linear model), and 0.005 s (FAST-LIO2) (p. 11, Table 5).

## Stated limitations

- The network must be trained in feature-rich areas before entering degenerate areas, and the terrain must not change drastically during that transition (p. 4).
- Online learning can be unstable under point cloud degeneration, so the MLP is frozen at its pre-degeneracy values (p. 7).
- Adapting the network to other wheeled robot models is future work (p. 12).

## Transfer conditions

Legacy reviewer observations: because the MLP is frozen during degeneracy, the method cannot be claimed to correct the model online when a new terrain and geometric degeneracy occur together. The reference labels come from LiDAR estimation on a prior map, not from an independent high-accuracy ground truth. Only one robot and three short sequences were tested, and the side-facing AVIA stress test does not extend to all sensors or all weather. The durations of Sequences 2 and 3 in Table 3 do not clearly match the 10 Hz frame counts, so outage durations should not be extrapolated. A robot of another size or drive needs retraining and calibration.

## Code and data

The paper gives a summary video and videos of the three sequences on YouTube and a DOI entry for supplementary material; the data are confidential (p. 12). The legacy extraction found no code repository URL. The videos were not watched and training was not reproduced.

## Version family

The authors state that the paper extends their IEEE Access 2024 work on LiDAR-IMU-wheel odometry with online calibration of a full linear kinematic model for skid-steering robots (p. 2). The two are versions of one research line; the 2024 baseline is not an independent replication.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "Environments lacking geometric features (e.g., tunnels and long straight corridors) are challenging for LiDAR-based odometry algorithms because LiDAR point clouds degenerate in such environments." |
| C3 | qualifies | moderate | p. 7 | "Therefore, online learning can be unstable when point cloud-based constraints become unreliable due to point cloud degeneration." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Conclusion, p. 12 | "In future work, we plan to improve versatility of our network to adapt to any type of wheeled robot model" |

## Page-cited excerpts

- **p. 2, Introduction.** "We extend our previous work [5], which jointly solves odometry estimation and online calibration of the full linear model"
  The version link to the authors' linear-model work.
- **p. 4, Assumptions.** "We also assume that the terrain condition does not drastically change while transitioning from feature-rich environments to another environment where LiDAR point clouds can degenerate."
  Limits generalization when new terrain and degeneracy occur together.
- **p. 7, Degeneracy handling.** "Therefore, online learning can be unstable when point cloud-based constraints become unreliable due to point cloud degeneration."
  The MLP is frozen under degeneracy; learning does not continue reliably then.
- **p. 8, Setup.** "we placed the narrow FOV LiDAR toward the Y direction (side) of the robot frame"
  Degeneracy is created on purpose; baseline failures do not generalize to their native configurations.
- **p. 9, Reference trajectory.** "we performed a batch optimization of LiDAR-IMU constraints on a precise prior map."
  The reference is a LiDAR-based batch estimate, not motion capture or a total station.
- **p. 10, Table 4.** "ATEs and RTEs of the odometry estimation algorithms."
  Source of the trajectory errors.
- **p. 11, Timing.** "the processing times of online training for all sequences were approximately 0.01 s on a laptop PC"
  10 ms is the training step only; the whole frame takes 31 ms (Table 5).
- **p. 11, Table 5.** "Comparison of total processing times regarding odometry estimation"
  Source of the per-frame totals.
- **p. 12, Conclusion.** "In future work, we plan to improve versatility of our network to adapt to any type of wheeled robot model"
  Transfer to other wheeled robots is not shown.
- **p. 12, Data.** "The data that has been used is confidential."
  The data are not public.

## Survey-usable statements

### Supported

- On a skid-steer robot with a deliberately narrow LiDAR view, online learning of a neural wheel model in the factor graph reduces ATE from 3.29, 0.59, and 0.99 m (fixed network) to 1.07, 0.25, and 0.41 m.
- Freezing the learned kinematic model when the Hessian indicates LiDAR degeneracy is the mechanism that keeps degenerate scans from corrupting the online training.

### Not supported

- The method keeps learning a correct model during degeneracy: the MLP is frozen then.
- The method runs onboard on low-power hardware: timing is on a laptop with a GPU, 31 ms per frame.
- FAST-LIO2 fails in degenerate settings in general: it was tested only with a side-facing narrow-FOV LiDAR.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; no legacy quote dropped
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/2ef792609d32f7e4609d9517/

## Original abstract

Environments lacking geometric features (e.g., tunnels and long straight corridors) are challenging for LiDAR-based odometry algorithms because LiDAR point clouds degenerate in such environments. For wheeled robots, a wheel kinematic model (i.e., wheel odometry) can improve the reliability of the odometry estimation. However, the kinematic model suffers from complex motions (e.g., wheel slippage, lateral movement) in the case of skid-steering robots particularly because this robot model rotates by skidding its wheels. Furthermore, these errors change nonlinearly when the wheel slippage is large (e.g., drifting) and are subject to terrain-dependent parameters. To simultaneously tackle point cloud degeneration and the kinematic model errors, we developed a LiDAR-IMU-wheel odometry algorithm incorporating online training of a neural network that learns the kinematic model of wheeled robots with nonlinearity. We propose to train the neural network online on a factor graph along with robot states, allowing the learning-based kinematic model to adapt to the current terrain condition. The proposed method jointly solves online training of the neural network and LiDAR-IMU-wheel odometry on a unified factor graph to retain the consistency of all those constraints. Through experiments, we first verified that the proposed network adapted to a changing environment, resulting in an accurate odometry estimation across different environments. We then confirmed that the proposed odometry estimation algorithm was robust against point cloud degeneration and nonlinearity (e.g., large wheel slippage by drifting) of the kinematic model. The summary video is available at: https://www.youtube.com/watch?v=CvRVhdda7Cw
