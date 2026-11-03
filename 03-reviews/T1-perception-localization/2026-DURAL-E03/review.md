# DURAL: Degradation‐Resistant Robust Adaptive Localization by LiDAR‐Inertial‐UWB‐Wheel Fusion for Coal Mine Robots

## Metadata

| Field | Value |
|---|---|
| ID | E03 |
| Title | DURAL: Degradation‐Resistant Robust Adaptive Localization by LiDAR‐Inertial‐UWB‐Wheel Fusion for Coal Mine Robots |
| Authors | Kun Hu, Menggang Li, Zhiwen Jin, Chaoquan Tang, Eryi Hu, and Gongbo Zhou |
| Venue | Journal of Field Robotics, vol. 43, no. 5, pp. 3559-3577 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1002/rob.70200](https://doi.org/10.1002/rob.70200) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.70200 |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2026-DURAL-E03/paper.pdf` and `02-fulltext/T1-perception-localization/2026-DURAL-E03/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2026-DURAL-E03/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, simulation
- protocol_caveats: few-trials
- platform_class: wheeled-unspecified
- platform: CUMT_5 coal mine robot (real tunnel); Husky in Gazebo (simulation)
- boundary_platform: no
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: Robosense 32-beam LiDAR, Xsens-G710 IMU, p440 UWB, wheel odometry (real robot); Velodyne 16-beam LiDAR in simulation
- compute: Intel Core i7 industrial PC, 32 GB RAM, GTX 1050 Ti; 5.627 ms mean per frame on the real tunnel data
- compute_location: not-reported
- summary_result: In a real coal mine tunnel, DURAL-Full reaches 0.167 m APE inside UWB coverage and 6.525% RPE outside it, versus 0.185 m and 20.648% for DURAL-UWB.
- summary_limitation: The authors state that threshold generalization, computational cost, and the effect of anchor deployment are not fully analyzed.
- survey_included: yes
- verification_level: light

## Problem

Long, repetitive coal mine tunnels make LiDAR odometry degenerate, UWB covers only a limited range, and wheel odometry suffers from terrain and slip. The paper asks how to keep localization with a small number of UWB anchors.

## Mechanism

A 36-dimensional iterated error-state Kalman filter (IESKF) fuses IMU propagation, LiDAR point-to-plane constraints, UWB position and range residuals, and wheel-speed residuals with a nonholonomic constraint (NHC) and lever-arm compensation. The filter switches between LiDAR-inertial-UWB (LIU) and LiDAR-inertial (LIO) modes according to a predefined spherical UWB coverage region. Outside the coverage, degeneracy is detected from the eigenvalues and directions of the pose covariance sub-block; when a threshold is exceeded, wheel speed is added (LIW mode). The four sensors are therefore not always used together, and the switching depends on thresholds. The UWB anchors are surveyed with a total station, which defines the global frame.

## Baselines and controls

Ablations DURAL-Full, DURAL-UWB, DURAL-Wheel, and DURAL-Base, and the baselines FAST-LIO2, DLIO, IG-LIO, LIO-SAM, and LIW_OAM. Only configurations that contain UWB report absolute APE inside the coverage; the others are compared by RPE, so the results are not a single absolute-error ranking.

## Platform and setup

Simulation: a Gazebo Husky in three degraded scenes (Tunnel, Plane, Ring). Real robot: CUMT_5 in a coal mine tunnel at a nominal 0.3 m/s and at most 0.2 rad/s, with 15 total-station ground-truth points; the construction blueprint serves as the map reference, and the authors acknowledge deviations between blueprint and as-built tunnel. Four UWB anchors with surveyed coordinates are used; the farthest valid point is at (34.963, 0, 2.249). The legacy extraction records no repetition over several days or mines and no closed-loop autonomous inspection task.

## Evidence type and transfer

Quantitative results come from simulated degraded scenes and from localization and mapping runs on data of a real ground coal mine robot. There is no deployment on the reference platform, and no test of recovery from long simultaneous failures of several real sensors.

## Sensors

Real robot: Robosense 32-beam LiDAR, Xsens-G710 IMU, p440 UWB, and wheel speed; simulation: Velodyne 16-beam LiDAR. The time offsets between the four sensors are assumed known (pre-calibrated or synchronized); LiDAR and IMU are hardware-synchronized and the extrinsics are pre-calibrated. The NHC assumes near-zero lateral and vertical velocity; no separate wheel-slip detector is proposed. Absolute UWB coordinates depend on fixed anchors surveyed with a total station.

## Compute and latency

All methods ran on the same industrial PC with an Intel Core i7 (exact model not reported), 32 GB DDR4 RAM, and a GTX 1050 Ti. Table 6 reports the mean time per frame, including preprocessing, state estimation, and map update: DURAL-Full 5.627 ms on the real tunnel and 5.714, 3.502, and 4.924 ms on the simulated Tunnel, Plane, and Ring; FAST-LIO2 3.725 ms on the real tunnel. Tail latency, power, reduced-compute settings, and long-term map growth are not reported. The legacy extraction does not say whether the PC was on the robot.

## Key quantitative results

- Real tunnel, DURAL-Full: 0.167 m APE inside the UWB coverage and 6.525% RPE outside it (rounded to 6.53% in the abstract); DURAL-UWB 0.185 m and 20.648%; DURAL-Wheel RPE 8.546% (p. 16, Table 4).
- The percentage RPE has no stated segment length or normalization in the legacy extraction, and the APE rests on 15 ground-truth points; neither is a full-trajectory metric ATE (p. 12).
- Map accuracy against the blueprint with a 20 cm correspondence filter: AC 6.456 cm and CD 0.631 cm for DURAL-Full; AC is a map-point error, not a pose error (p. 17, Table 5).
- Simulation, DURAL-Full in Tunnel, Plane, and Ring: ATE 0.695, 0.513, and 0.421 m; RPE 0.006, 0.015, and 0.009 m (simulated RPE in meters, real RPE in percent) (p. 11, Table 3).
- Mean time per frame: DURAL-Full 5.627 ms versus FAST-LIO2 3.725 ms on the real tunnel (p. 18, Table 6).

## Stated limitations

- The authors acknowledge that threshold generalization, computational cost, and the effect of anchor deployment are not fully analyzed (p. 18).
- In the real tunnel only translational degeneracy along the X axis is analyzed and rotational degeneracy is disregarded (p. 15).
- The data are not publicly available (p. 18).

## Transfer conditions

Legacy reviewer observations: adaptive mode selection does not mean adaptive thresholds (translation threshold 0.4 in simulation and 0.13 on the real robot). UWB use is decided from a preset spherical region and the state position, not from an assessment of non-line-of-sight or anchor faults. The near-zero side-slip assumption of the NHC needs checking under strong slip or bumps, and there is no guarantee for recovery when wheel and LiDAR fail together. The blueprint reference has construction deviations, and the 20 cm filter may hide unmatched regions. A reuse needs known sensor time offsets, surveyed anchors, and a re-tuned degeneracy threshold.

## Code and data

The data are available from the corresponding author on request because of privacy or ethical restrictions (p. 18). The legacy extraction found no code repository URL in the paper. Code and supplementary material were not checked.

## Version family

The authors cite their earlier multimodal coal mine SLAM work (Li et al., Remote Sensing 2023); this paper adds wheel speed and degeneracy-based mode switching. The earlier work is not counted as an independent replication. No conference version is stated.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "uneven or slippery terrain degrades wheel odometer accuracy; and long, feature‐poor tunnels reduce light detection and ranging (LiDAR) effectiveness" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | p. 3 | "we assume that the time offsets between the four sensors (LiDAR, IMU, Wheel, and UWB) are known" |

## Page-cited excerpts

- **p. 3, Calibration prerequisite.** "we assume that the time offsets between the four sensors (LiDAR, IMU, Wheel, and UWB) are known"
  Time offsets are a prerequisite; the method does not calibrate them online.
- **p. 4, UWB anchors.** "The positions of UWB anchors are calibrated using a total station"
  The global frame depends on pre-deployed, surveyed anchors.
- **p. 12, Ground truth.** "trajectory assessment employs 15 ground‐truth points"
  The real-robot APE rests on 15 points.
- **p. 13-14, Map evaluation.** "A correspondence distance threshold of 0.2 m is established, with irrelevant points excluded via ground‐truth map alignment."
  Map metrics depend on a 20 cm threshold and alignment to the blueprint.
- **p. 15, Degeneracy direction.** "Given the exclusive occurrence of translational degradation along the X‐axis in tunnel environments, rotational degradation is disregarded."
  The real test does not show detection of arbitrary 6-DoF degeneracy.
- **p. 15, Runtime scope.** "average processing time per frame, including sensor preprocessing, state estimation, and map update"
  Timing covers the whole frame, not only the filter update.
- **p. 16, Table 4.** "Quantitative analysis of APE (m) and RPE (%)."
  Table 4 mixes APE inside and RPE outside the UWB coverage.
- **p. 17, Table 5.** "Mapping accuracy (AC) (cm) and chamfer distance (CD) (cm)"
  Map accuracy, not localization accuracy.
- **p. 18, Table 6.** "Average time consumption per frame across real‐world and simulated data sets"
  Mean values only; no worst case or power.
- **p. 18, Data availability.** "The data are not publicly available due to privacy or ethical restrictions."
  The data cannot be called public.

## Survey-usable statements

### Supported

- In one real coal mine tunnel, LiDAR-inertial-UWB-wheel fusion reaches 0.167 m APE inside UWB coverage and 6.525% RPE outside it, with 15 ground-truth points.
- Wheel odometry with a nonholonomic constraint is used as a fallback when LiDAR degeneracy is detected outside UWB coverage.

### Not supported

- DURAL achieves a full-trajectory metric ATE of 0.167 m: the value is APE inside the UWB coverage only.
- The degeneracy detection adapts its thresholds or handles rotational degeneracy on real data: the thresholds are fixed per setting and only X-axis translation was analyzed.
- The data or code are public: data are on request only and no code URL was found.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; runtime excerpt trimmed to the part found on the PDF page
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/60d72158f3ceb02ea4a50643/

## Original abstract

Simultaneous Localization and Mapping (SLAM) in large‐scale, complex, global positioning system (GPS)‐denied underground coal mines poses significant challenges. In these environments, abnormal conditions hinder sensor performance: GPS unavailability impedes scene reconstruction and geographic referencing; uneven or slippery terrain degrades wheel odometer accuracy; and long, feature‐poor tunnels reduce light detection and ranging (LiDAR) effectiveness. To address these challenges, we propose DURAL, a multimodal SLAM framework based on the Iterated Error‐State Kalman Filter that fuses multiple sensors from coal mine robots to overcome individual sensor limitations. First, LiDAR‐inertial odometry is tightly coupled with Ultra‐Wideband (UWB) absolute positioning constraints to establish an absolute coordinate system. Next, the wheel odometer is integrated through tight coupling, enhanced by nonholonomic constraints and vehicle lever arm compensation, to mitigate performance degradation beyond the UWB measurement range. Finally, an adaptive fusion mode switching mechanism dynamically adjusts sensor constraints based on UWB coverage and environmental conditions. Experimental results indicate that our method achieves state‐of‐the‐art accuracy and robustness in both simulated tunnel environments and real‐world underground coal mines. In real‐world experiments, the system attains an absolute pose error of 0.167 m within the UWB range, maintains a relative pose error of 6.53% outside this range, and improves mapping accuracy to 6.456 cm, significantly outperforming existing approaches in challenging mining scenarios.
