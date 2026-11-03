# ToF-Wheel Odometry: Navigating Degeneration of Localization With Limited Sensing Capabilities

## Metadata

| Field | Value |
|---|---|
| ID | E02 |
| Title | ToF-Wheel Odometry: Navigating Degeneration of Localization With Limited Sensing Capabilities |
| Authors | Xu Yang, Wenhao Li, Zhengyu Wei, Zening Li, Longxiang Huang, and Bo Wang |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 10, pp. 11410-11417 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3726370](https://doi.org/10.1109/lra.2026.3726370) |
| Official URL | https://ieeexplore.ieee.org/document/11661693/ |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2026-ToF-Wheel-E02/paper.pdf` and `02-fulltext/T1-perception-localization/2026-ToF-Wheel-E02/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2026-ToF-Wheel-E02/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: few-trials
- platform_class: differential-drive
- platform: unnamed differential-drive robot with a forward-facing ToF camera and a Raspberry Pi 4B (self-collected); M3DGR public ground-robot sequences
- boundary_platform: no
- degradation: lidar-degeneracy, terrain, wheel-slip
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: forward-facing ToF camera (model not named) and differential-drive wheel encoders, no gyroscope; on M3DGR the dataset LiDAR replaces the ToF camera
- compute: Raspberry Pi 4B; 12.575 ms mean and 32.902 ms P95 total per-frame update time with at most two feedback iterations
- compute_location: onboard
- summary_result: On four self-collected stress sequences, TWO has 0.046 m mean ATE RMSE versus 0.255 m (fixed-Q) and 0.295 m (scalar-Q) ToF-wheel filters, without a gyroscope.
- summary_limitation: A purely orthogonal, wheel-silent disturbance can be corrected by the ToF update but cannot trigger covariance inflation on its own, as the authors state.
- survey_included: yes
- verification_level: full

## Problem

Wheel odometry on ground robots is violated by slip and by terrain-induced
tilt on slopes and surface transitions. Consumer robots often pair the wheels
with a Time-of-Flight (ToF) camera, whose short range and narrow forward field
of view make the geometry degenerate in places such as corridors. When both
problems coincide, filtering-based odometry can diverge (p. 1). The authors
argue that static or scalar adaptive process noise cannot place the extra
uncertainty in the direction of the motion-model violation, and ask how to
shape the process covariance directionally, gated by how well the ToF update
observes each direction, with a wheel-only motion prior and no IMU (pp. 1-2).

## Mechanism

TWO is an EKF with differential-drive wheel propagation and a ToF update by
probabilistic point-to-plane residuals, solved as a MAP problem on SE(3)
(p. 3). The process covariance increment is the sum of the mapped encoder
noise Q_w, a constant baseline Q_0, and an inflation term Q_infl inferred from
the ToF update (p. 3). The posterior-to-prior correction e_k is split into a
wheel-explainable part, spanned by the forward and yaw directions of the
differential-drive basis B_dd with track width l, and an orthogonal remainder
(lateral, vertical, roll, pitch) (p. 3).

Two scalar gates come from the measurement information matrix J_k. The
geometric score gamma_k is the normalized trace of the gain operator
J_k(I + J_k)^-1, the closed-form best isotropic approximation in the Frobenius
norm; the remainder score eta_k is the same quantity restricted to a fixed
four-dimensional basis of the remainder subspace (pp. 4-5). The authors chose
scalar scores because a full-matrix gate would be computationally complex and
potentially unstable (p. 4). The inflation magnitude beta_k is the truncated
minimizer max(0, psi/d - 1) of a negative log-likelihood of the
wheel-explainable correction, blended with the previous value by gamma_k
(p. 5). The remainder is scaled by eta_k, recombined with the wheel part,
normalized by a reference covariance Q_ref, and turned into a rank-one
inflation spread evenly over the N_k cached wheel steps of the frame and
transported to each step by the SE(3) adjoint (p. 5). Only the
wheel-explainable correction drives beta_k; the remainder shapes the
direction but cannot start inflation (p. 5).

An intra-frame feedback loop then re-propagates the covariance from
P_{k-1|k-1} with the new Q_eff and re-runs the update, with the propagated
mean and local map held fixed, until the posterior and prior converge or a
maximum number of iterations is reached (p. 5); the default limit is two
(p. 7). Fixed parameters for all sequences are 0.2 rad/s wheel-rate noise per
wheel, Q_0 = 10^-8 diag(1, 1, 0, 0, 1, 1), Q_ref = 10^-6 I_6, and reference
variances of 10^-3 rad^2 and 2 x 10^-4 m^2 for the rotation and translation
weights of J_k (pp. 5-6).

## Baselines and controls

The comparison in Table I uses VoxelMap, AKF-LIO, Faster-LIO, and LIWO. TWO
shares the VoxelMap/C3P-VoxelMap point-to-plane backbone, which holds the
geometric front end fixed against VoxelMap (p. 6). On the self-collected
sequences all methods receive the same ToF point cloud; the baselines
propagate from the ToF module's built-in IMU and TWO from the wheel encoders
alone. On M3DGR, which has no ToF camera, TWO's update runs on the same LiDAR
stream as the baselines (p. 6). Baseline parameter settings are not described.

Table II isolates the covariance shaping with a wheel-only filter, a
fixed-Q ToF-wheel filter, and a scalar-Q ToF-wheel filter that rescales the
nominal wheel covariance to match the correction energy, without directional
shaping or feedback (p. 6). The fixed-Q baseline is not defined beyond its
name. The ablation (Table III) compares full TWO with eta = 0, eta = 1,
gamma = 1, beta = 0, and a variant without feedback (p. 7). Table IV varies
the maximum number of feedback iterations (0, 1, 2), and Table V compares TWO
with a static control (Q_w + Q_0, Q_infl disabled) at Q_0 scales of 0.1x to
10x (pp. 7-8). No repeated runs or statistics are reported.

## Platform and setup

Self-collected data were recorded on an unnamed differential-drive platform
with a Raspberry Pi 4B for onboard computation (p. 5). Ground truth comes
from an independent chassis-mounted Livox Mid-360 LiDAR-inertial system that
TWO does not use; the LIO algorithm and the ground-truth accuracy are not
stated (p. 5). Three long indoor or semi-structured sequences (Lobby, Office,
Corridor) serve the cross-method comparison, and four stress sequences
(Slope, Forward Slip + Weak Geometry, Side Slip, Lift/Pose Perturbation)
serve the ablations (p. 5). The paper does not describe how the slip and
lift events were produced, and it gives no sequence lengths, durations, or
speeds. Two public M3DGR sequences with kinematic challenges, Wheel Float and
Sharp Turn, are replayed (p. 5). Each sequence is run once. Table I reports
ATE and RPE at 1 m (p. 6).

## Evidence type and transfer

The self-collected results come from data recorded on the authors' robot.
The paper does not state that TWO ran live while the robot moved, and no
result shows TWO's output driving the robot, so the strongest setting is
recorded robot data; the M3DGR results are dataset playback. On M3DGR a LiDAR
replaces the ToF camera, so the public-data results do not test the ToF
configuration. The stress sequences were designed to expose slip, terrain
transitions, and weak geometry ("experiments are designed to expose these
challenges", p. 5), and results are reported per sequence, so these
conditions are coded as designed degradation; each condition rests on one
sequence. The results show odometry accuracy, not navigation performance.

## Sensors

TWO uses a forward-facing ToF camera (model, resolution, and range not
given) and differential-drive wheel encoders; it uses no gyroscope, while
every baseline has one (p. 6). The ToF module's built-in IMU feeds only the
baselines. The Livox Mid-360 serves only for ground truth (p. 5). On M3DGR,
TWO uses the dataset's LiDAR stream; the LiDAR model is not named in the
paper.

## Compute and latency

Table IV reports total per-frame update times on the Raspberry Pi 4B: 6.665 ms
mean and 15.547 ms P95 with no feedback iteration, 11.096 ms and 26.344 ms with
at most one (0.29 extra passes per frame on average), and 12.575 ms and
32.902 ms with the default limit of two (0.49 extra passes) (p. 8, Table IV).
The Pi 4B is the platform's onboard computer, but the paper does not say
whether the timed runs were live or replayed on the board, and it does not
give the ToF frame rate, so the real-time margin cannot be checked. Where the
M3DGR runs were computed, memory use, and power are not reported.

## Key quantitative results

- Self-collected ATE (m): TWO 0.072, 0.177, and 0.249 on Lobby, Office, and Corridor, versus VoxelMap 0.620, 4.901, 9.705; AKF-LIO 0.239, 4.470, 3.234; Faster-LIO drift failure (omitted), 11.232, 2.290; and LIWO 0.270, 0.618, 0.424 (p. 6, Table I).
- Self-collected RPE@1m (m): TWO 0.061, 0.058, and 0.077; LIWO is lower on Lobby at 0.056, and all other baseline values are higher (p. 6, Table I).
- Average ATE over the available sequences: TWO 0.190 m versus LIWO 0.411, AKF-LIO 1.667, VoxelMap 3.349, and Faster-LIO 3.478 m (Faster-LIO over four sequences) (p. 6, Table I).
- M3DGR ATE/RPE (m): TWO 0.209/0.091 on Wheel Float and 0.242/0.088 on Sharp Turn, versus AKF-LIO 0.190/0.045 and 0.200/0.050, Faster-LIO 0.190/0.045 and 0.201/0.050, LIWO 0.539/0.330 and 0.202/0.053, and VoxelMap 0.983/0.264 and 0.538/0.152 (p. 6, Table I).
- Four-sequence means, TWO versus wheel-only, fixed-Q, and scalar-Q: ATE RMSE 0.046 versus 0.628, 0.255, 0.295 m; ATE P95 0.084 versus 1.170, 0.453, 0.464 m; RPE 0.029 versus 0.118, 0.085, 0.087 m; worst 3-s error 0.084 versus 1.179, 0.459, 0.474 m. The table does not name the four sequences; TWO's values equal the Table III stress averages (p. 6, Table II).
- Ablation averages over the four stress sequences, TWO versus eta = 1, gamma = 1, eta = 0, beta = 0, and without feedback: ATE 0.0455 versus 0.0460, 0.0478, 0.1065, 0.2185, 0.0588 m; RPE 0.0293 versus 0.0307, 0.0300, 0.0670, 0.0795, 0.0370 m (p. 7, Table III).
- Disabling inflation (beta = 0) gives the largest per-sequence losses: ATE 0.043 versus 0.361 m on Forward Slip + Weak Geometry and 0.042 versus 0.284 m on Lift/Pose Perturbation for TWO versus beta = 0; suppressing the remainder (eta = 0) gives 0.072 versus 0.164 m on Side Slip and 0.025 versus 0.099 m on Slope (p. 7, Table III).
- Removing feedback raises ATE by 1.60x on Forward Slip + Weak Geometry (0.069 versus 0.043 m) and 1.50x on Lift/Pose Perturbation (0.063 versus 0.042 m) (p. 7, Table III).
- Mean stress ATE is 0.055, 0.045, and 0.046 m with at most 0, 1, and 2 feedback iterations. The zero-iteration value differs from the 0.0588 m of the without-feedback variant in Table III, and the paper does not say whether the two configurations differ (p. 8, Table IV).
- Full TWO versus the static control at Q_0 scales 0.1x, 0.5x, 1x, 2x, 10x: ATE 0.058, 0.047, 0.046, 0.042, 0.038 versus 0.224, 0.212, 0.219, 0.211, 0.226 m, reductions of 74.3% to 83.2% (p. 8, Table V).

## Stated limitations

- A purely orthogonal, wheel-silent disturbance may still be corrected by the ToF update but cannot trigger inflation on its own, because the remainder alone may reflect degeneracy or sensor error (p. 5).
- On M3DGR the gyroscope-based baselines roughly halve TWO's RPE on Wheel Float and cut it by over 40% on Sharp Turn, which the authors attribute to the gyroscope's direct advantage (p. 6).

## Transfer conditions

The wheel-explainable basis B_dd assumes differential-drive kinematics with a
known track width (p. 3). Skid-steer, Ackermann, or mecanum chassis need a
different basis and were not tested. The method needs a forward depth sensor
with a point-to-plane mapping back end; the ToF camera's specification is not
reported, and with a LiDAR (M3DGR) TWO trails the gyroscope-based LIO methods
in both ATE and RPE. All parameters were fixed across sequences, but how they
were chosen is not stated. The ground truth is itself a LiDAR-inertial
estimate of unreported accuracy, which matters when stress-sequence ATEs are
a few centimeters. The LIO baselines ran on short-range ToF clouds with the
module IMU and undescribed settings, a configuration they were not designed
for. Each condition rests on one run, and the robot, terrain, and slip
magnitudes are not characterized. Adding a gyroscope to TWO was not
evaluated.

## Code and data

The paper states that supplementary downloadable material is available at
the DOI (p. 1); its content was not verified. No code repository is given,
and the paper does not say whether the self-collected data are released.
M3DGR is a public dataset.

## Version family

The paper cites no conference or preprint version, and the library holds one
entry for this work. C3P-VoxelMap (reference [24], with the same first
author) is the mapping backbone, a separate work.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "In filtering-based odometry, these violations frequently trigger divergence when they coincide with constrained geometric observability (e.g., featureless corridors)." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VII-B, p. 6 | "For M3DGR sequences, since the dataset provides no ToF camera at all, TWO's point-to-plane update instead runs on the same LiDAR stream the baselines use." |

## Page-cited excerpts

- **p. 5, Sec. V-C.** "A purely orthogonal, wheel-silent disturbance may still be corrected by the ToF update but cannot independently trigger inflation."
  The authors' own scope limit of the inflation mechanism.
- **p. 5, Sec. VII-A.** "The Mid-360 measurements are used only for ground-truth generation and are not used by TWO."
  The reference trajectory comes from a separate LiDAR-inertial system; its accuracy is not given.
- **p. 6, Sec. VII-B.** "On the self-collected sequences, TWO and the baselines see the same ToF point cloud, and only the motion prior differs, with the baselines propagating from the module's built-in IMU and TWO from the wheel encoders alone."
  The self-collected comparison runs LIO baselines on ToF data with the module IMU.
- **p. 6, Sec. VII-B.** "This gap reflects the gyroscope's direct advantage."
  The authors explain why gyroscope-based baselines have lower RPE on M3DGR.
- **p. 6, Sec. VII-B.** "Scalar-Q underperforms even the static fixed-Q baseline on every metric (e.g., 0.295 vs. 0.255 m ATE RMSE)."
  Isotropic inflation is worse than no adaptation; the directional structure carries the gain.
- **p. 7, Sec. VII-C.** "Omitting feedback increases ATE by 1.60× in Forward Slip + Weak Geometry and 1.50× in Lift/Pose Perturbation."
  The same-frame covariance repair matters most during bursty events.
- **p. 8, Sec. VII-C.** "At every scale, TWO reduces stress-sequence ATE by 74.3–83.2%; the gain therefore cannot be reproduced by globally inflating baseline process uncertainty."
  Tuning Q_0 over two orders of magnitude does not reach the adaptive result on these four sequences.

## Survey-usable statements

### Supported

- With only a forward ToF camera and differential-drive encoders, directional, observability-gated process-covariance inflation gave 0.046 m mean ATE RMSE on four self-collected stress sequences, versus 0.255 m for fixed Q and 0.295 m for scalar Q.
- Isotropic scalar inflation was worse than fixed process noise on every Table II metric, so the direction of the inflation matters, not only its size.
- On three self-collected indoor sequences with a shared ToF point cloud, TWO had lower ATE than VoxelMap, AKF-LIO, Faster-LIO, and LIWO, which propagated from the ToF module's IMU.
- Disabling inflation raised the average stress-sequence ATE from 0.0455 m to 0.2185 m, and suppressing the remainder raised it to 0.1065 m.
- With at most two feedback iterations, a frame update took 12.575 ms on average and 32.902 ms at P95 on a Raspberry Pi 4B.

### Not supported

- TWO is the most accurate method on every sequence: in Table I it has the lowest ATE on 3 of 5 sequences and the lowest RPE on 2 of 5. Counterexamples: Lobby RPE (LIWO 0.056 versus 0.061 m); Wheel Float (AKF-LIO and Faster-LIO 0.190/0.045 versus 0.209/0.091 m); Sharp Turn (AKF-LIO 0.200/0.050, Faster-LIO 0.201/0.050, and LIWO 0.202/0.053 versus 0.242/0.088 m).
- Full TWO beats every ablation variant on every stress sequence: it has the lowest ATE only on Forward Slip + Weak Geometry and the lowest RPE only on Lift/Pose Perturbation. Counterexamples: Slope (eta = 1, 0.024/0.015 versus 0.025/0.017 m); Side Slip (eta = 1, 0.067/0.031, and gamma = 1, 0.070/0.031, versus 0.072/0.032 m); Lift/Pose Perturbation ATE (gamma = 1, 0.041 versus 0.042 m); Forward Slip RPE (eta = 0 and without feedback, 0.017 versus 0.018 m). Full TWO has the best averages.
- The public-data results validate the ToF configuration: M3DGR has no ToF camera, and TWO ran on its LiDAR.
- TWO ran in real time on the robot while it drove: the timing is on the Pi 4B, but live operation and the ToF frame rate are not stated.
- The method improves navigation or task success: no closed-loop run is reported.
- The gains are statistically established: each sequence is run once, without repeated trials or statistics.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read (Secs. I-VIII); raw PDF text of pp. 1 and 5 checked; Tables I-V read from rendered page images of pp. 6-8 (MinerU merges the Faster-LIO and LIWO Sharp Turn cells of Table I with their averages); Figs. 3 and 4 viewed | corrections: rebuilt in English template format; M3DGR comparison completed (gyroscope baselines also have lower ATE); stated limitations restricted to author statements; baselines completed with the fixed-Q definition gap and the Table IV and V controls; supplementary-material statement added; per-sequence counterexamples listed for Tables I and III; Table IV versus Table III inconsistency recorded (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/b4587f74b4dc799253f78e2f/

## Original abstract

Wheel odometry provides an efficient motion prior for ground robots but is prone to transient violations such as wheel slip or terrain-induced tilt. In filtering-based odometry, these violations frequently trigger divergence when they coincide with constrained geometric observability (e.g., featureless corridors). We address this challenge by proposing ToF–Wheel Odometry (TWO), a tightly-coupled filtering framework that integrates wheel kinematics with geometric constraints from Time-of-Flight (ToF) cameras. The primary contribution of this work is a degeneracy-aware, directional covariance-shaping strategy that replaces heuristic online covariance tuning with geometry-conditioned inflation. The core idea is to infer process noise from geometric corrections with a strict reliability check. We decompose the posterior-to-prior correction into a wheel-explainable subspace and an orthogonal remainder. The process covariance is anisotropically adjusted according to the observability of the ToF update: if the geometry is degenerate in non-kinematic directions, the remainder is suppressed as sensor noise; if the geometry is distinct, it is admitted as a valid kinematic violation. Additionally, we introduce an intra-frame feedback loop that retrospectively repairs the process covariance within the current frame to reduce structural lag during bursty disturbances. Extensive experiments on challenging scenarios demonstrate that TWO improves trajectory accuracy and robustness compared to static and adaptive Gaussian filtering, robustly navigating the trade-off between kinematic reliability and limited sensing capabilities.
