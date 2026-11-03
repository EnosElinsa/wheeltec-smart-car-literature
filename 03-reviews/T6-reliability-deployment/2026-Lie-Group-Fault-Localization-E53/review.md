# Fault-Tolerant Multimodal Localization of Multirobots on Matrix Lie Groups

## Metadata

| Field | Value |
|---|---|
| ID | E53 |
| Title | Fault-Tolerant Multimodal Localization of Multirobots on Matrix Lie Groups |
| Authors | Mahboubeh Zarei and Robin Chhabra |
| Venue | IEEE Transactions on Robotics, vol. 42, pp. 2459-2477 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tro.2026.3699440](https://doi.org/10.1109/tro.2026.3699440) |
| Official URL | https://ieeexplore.ieee.org/document/11551518/ |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2026-Lie-Group-Fault-Localization-E53/paper.pdf` and `02-fulltext/T6-reliability-deployment/2026-Lie-Group-Fault-Localization-E53/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2026-Lie-Group-Fault-Localization-E53/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: multi-robot, fault-recovery-deployment
- evidence_type: online-hardware
- evidence_all: online-hardware, theory-only
- protocol_caveats: speed-capped, scripted-scenario, few-trials
- platform_class: ackermann
- platform: three AgileX LIMO robots in Ackermann mode
- boundary_platform: no
- degradation: terrain, sensor-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: MPU6050 IMU, wheel encoders, ORBBEC Dabai camera and ArUco markers
- compute: NVIDIA Jetson Nano; measured latency and bandwidth not recorded
- compute_location: onboard
- summary_result: Three fusion tests report fused ANEES of 0.85/0.99/0.89, treating 1500 time steps as independent realizations rather than repeating trials.
- summary_limitation: The three-robot tests do not cover common-prior double counting, which requires at least four robots.
- survey_included: yes
- verification_level: light

## Problem

Relative observations and forwarded information produce correlated estimates and double counting in multirobot localization. Faulty visual markers can also disrupt low-cost inertial/wheel-speed fusion.

## Mechanism

Approximate BCH operations for right-multiplicative Gaussian perturbations support inversion, composition, differencing, averaging, correlated fusion, and constrained fusion on matrix Lie groups. An EKF on SE_2(3) × R^3 × R^3 combines IMU, wheel velocity, and ArUco pseudoposes. Innovation Mahalanobis distance rejects anomalous marker observations. A leader observes fixed markers; two follower types form pseudoposes from upstream states and relative markers. Information paths and cross-covariances are tracked before fusion.

## Baselines and controls

IMU integration; wheel odometry (WO); IMU+WO EKF; IMU+WO+ArUco without fault detection; IMU+WO+ArUco+FD; and two independent estimates versus correlated fusion.

## Platform and setup

Three AgileX LIMO robots use Ackermann mode with a minimum turning radius of 0.4 m. PhaseSpace ground truth uses four overhead cameras and eight LEDs per robot, up to 960 Hz. Fixed/mobile ArUco markers measure 36 cm/8.5 cm. Final tests use 10 cm/s and full lighting. Leader tests include turns and foam terrain; two-/three-robot tests each have two groups. Three fusion tests use near-straight motion. Setup numbers are inherited, not re-verified.

## Evidence type and transfer

Approximate stochastic Lie-group/EKF theory and controlled indoor hardware localization. The legacy extraction does not establish that the evaluated estimator drives navigation, so hardware is coded online-hardware. Time-averaged ANEES uses one run, without independent repeats.

## Sensors

MPU6050 IMU, wheel encoders, ORBBEC Dabai camera/ArUco. Mounted EAI XL2 LiDAR is not fused and is future work. Marker observations and upstream estimates must be simultaneously available; Wi-Fi/Bluetooth carry communication. PhaseSpace provides ground truth.

## Compute and latency

NVIDIA Jetson Nano. Closed-form fusion and real-time operation are claimed, but utilization, latency, and bandwidth measurements were not recorded. Correlated fusion needs the active information topology, cross-covariances, and independent local filters along information paths; three robots do not establish constant overhead at scale.

## Key quantitative results

The following legacy values were located, not re-verified.

- Innovation threshold 40 is used for marker rejection; Figs. 6-10 illustrate visual-outlier rejection and recovery after IMU/WO degradation, without a position-RMSE table (p. 13, setup refinement; pp. 11-15, figures).
- With T = 1500 and n = 3, fused ANEES is 0.85/0.99/0.89 versus IMU/WO 0.22/0.43/0.22. The two independent estimates are 0.93/0.43/1.02 and 0.25/0.64/0.25 (p. 15, Table III).
- Because repeat trials were unavailable, single-run ANEES treats time steps as independent realizations; this does not replace independent-run consistency testing (p. 14, Sec. V-D4).

## Stated limitations

- Fusion tests were conducted only during near-straight motion (p. 14, Sec. V-D4).
- Single-run ANEES treats time steps as independent realizations because repeat experiments were unavailable (p. 14, Sec. V-D4).
- Common-prior double counting requires at least four robots and is not tested by the three-robot experiment (p. 15, Sec. V-D4).

## Transfer conditions

Legacy reviewer observations: Gaussian/small-error BCH approximations and EKF linearization constrain the theory; proofs were not independently rechecked. Detection mainly screens marker pseudopose outliers, rather than arbitrary simultaneous catastrophic IMU/encoder faults. Tests use three low-speed robots, full lighting, restricted indoor marker visibility, and near-straight fusion motion. No quantitative communication delay/loss/disconnection, bandwidth, or scale test is recorded. Three robots cover double counting from common process noise, not common priors. Time-correlated single-run samples do not supply independent-trial statistics.

## Code and data

No paper-specific code/data-release URL was found in the legacy extraction. ROS camera_calibration and aruco_ros are dependencies rather than author implementation releases; availability was not verified.

## Version family

The TRO paper extends Zarei and Chhabra's RA-L 2024 "Consistent fusion of correlated pose estimates on matrix Lie groups" [44], adding general group operations, correlated-measurement cross-covariance recursion, and fault-tolerant multimodal multirobot localization. Count the TRO version once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | qualifies | moderate | Sec. V-D4, Fusion in Localization, p. 15 | "common prior information, which requires at least four robots." |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V-D4, Fusion in Localization, p. 14 | "conducted only during near-straight motion." |

## Page-cited excerpts

- **p. 13, Sec. V-C, Setup Refinement.** "a robot speed of 10 cm/s, and full lighting."
  These controlled speed/lighting conditions limit hardware transfer.
- **p. 14, Sec. V-D4, Fusion in Localization.** "conducted only during near-straight motion."
  The fusion tests do not establish performance on complex trajectories.
- **p. 14, Sec. V-D4, Fusion in Localization.** "we compute a single-run ANEES by treating time steps as independent realizations"
  The statistic is not derived from independent repeated runs.
- **p. 15, Sec. V-D4, Fusion in Localization.** "common prior information, which requires at least four robots."
  The three-robot setup cannot test that source of double counting.

## Survey-usable statements

### Supported

- Lie-group pseudopose fusion with marker-outlier rejection is demonstrated on three low-speed LIMO robots in a fully lit indoor marker environment (light review).

### Not supported

- Large-scale constant-cost localization: three robots are tested and local filters depend on information paths.
- Arbitrary simultaneous IMU, encoder, and marker fault tolerance: the detector primarily screens marker pseudoposes.
- Independent-run statistical consistency or communication-outage robustness: those tests are not recorded.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format conversion; four exact legacy excerpts retained; single-run ANEES, low-speed setup, and three-robot limitations retained
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/94d162b096cda5df966df1d9/
- Legacy provenance: selection_id 94d162b096cda5df966df1d9; PDF SHA-256 c9a13460af74a2049af178f74acab2283229a9f14abd1205a4b80f36451339aa (inherited, not re-hashed).

## Original abstract

Consistent localization of cooperative multirobot systems during navigation presents substantial challenges. This article proposes a fault-tolerant, multimodal localization framework for multirobot systems on matrix Lie groups. We introduce novel stochastic operations to perform composition, differencing, inversion, averaging, and fusion of correlated and noncorrelated estimates on Lie groups, enabling pseudopose construction for filter updates. The method integrates a combination of proprioceptive and exteroceptive measurements from inertial, velocity, and pose (pseudopose) sensors on each robot in an extended Kalman filter (EKF) framework. The prediction step is conducted on the Lie group $\mathbb { S } \mathbb { E } _ { 2 } ( \mathbf { 3 } ) \times \mathbb { R } ^ { 3 } \times \mathbb { R } ^ { 3 }$ , where each robot’s pose, velocity, and inertial measurement biases are propagated. The proposed framework uses body velocity, relative pose measurements from fiducial markers, and inter-robot communication to provide scalable EKF update across the network on the Lie group SE(3)  R<sup>3</sup>. A fault detection module is implemented, allowing the integration of only reliable pseudopose measurements from fiducial markers. We demonstrate the effectiveness of the method through experiments with a network of wheeled mobile robots equipped with inertial measurement units, wheel odometry, and ArUco markers. The comparison results highlight the proposed method’s real-time performance, superior efficiency, reliability, and scalability in multirobot localization, making it well-suited for large-scale robotic systems.
