# A GP-based Robust Motion Planning Framework for Agile Autonomous Robot Navigation and Recovery in Unknown Environments

## Metadata

| Field | Value |
|---|---|
| ID | E59 |
| Title | A GP-based Robust Motion Planning Framework for Agile Autonomous Robot Navigation and Recovery in Unknown Environments |
| Authors | Nicholas Mohammad, Jacob Higgins, and Nicola Bezzo |
| Venue | 2024 IEEE International Conference on Robotics and Automation (ICRA), pp. 2418-2424 |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/icra57147.2024.10610382](https://doi.org/10.1109/icra57147.2024.10610382) |
| Official URL | https://ieeexplore.ieee.org/document/10610382/ |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2024-GP-Navigation-Recovery-E59/paper.pdf` and `02-fulltext/T6-reliability-deployment/2024-GP-Navigation-Recovery-E59/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2024-GP-Navigation-Recovery-E59/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware, scripted-scenario, few-trials
- platform_class: skid-steer
- platform: Clearpath Jackal UGV (simulation and hardware); Boston Dynamics Spot quadruped (one hardware case)
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, integrity-reliability
- sensors: 270-degree 2D LiDAR (simulation); Velodyne LiDAR (Jackal) and Ouster LiDAR (Spot) with Gmapping for map and state
- compute: planner front-end under 1 ms, back-end typically over 100 ms, GP inference under 10 ms; processor not reported
- compute_location: not-reported
- summary_result: In 120 Gazebo runs (four room worlds, three goals, 10 runs each), success with recovery was never below without, for example 0.8 versus 0.3 (1 m doorways, dense, goal 0).
- summary_limitation: No limitation is stated by the authors; future work lists distributional learning, planner switching, and dynamic obstacles, and hardware evidence is two snapshot case studies.
- survey_included: yes
- verification_level: full

## Problem

A receding-horizon safe-corridor motion planner with hard constraints can
fail at runtime when previously occluded obstacles appear: the numerical
back-end then finds no feasible trajectory, and repeated failures within the
planning horizon can end in a collision. The paper asks how to predict such
planner failures before they happen and how to recover autonomously to a
state from which the planner is likely to succeed, in an unknown environment.

## Mechanism

The base planner (policy Pi) has a front-end that runs Jump Point Search (JPS)
on the occupancy map and builds a corridor C of convex H-polytopes, and a
back-end that optimizes N cubic Bezier segments inside the corridor with the
FASTER solver, altered to use the MINVO basis. A tracking MPC executes the
trajectory and predicts future states over a horizon T_F (pp. 2-3).
Front-end failures are checked directly by running JPS (under 1 ms); the
learned part estimates the back-end failure probability after a front-end
success (p. 3). The features are the minimum time-to-intersect t_C from the
robot position and velocity to the hyperplanes of the current polytope
(capped at a user value gamma_t when not approaching) and the corridor size
|C|. Training data were binned on these features to obtain empirical failure
probabilities, and GP regression with an RBF kernel was fitted; the posterior
mean is used as the failure probability (pp. 4-5). The text refers to "the
GP regressions" in the plural and future work aims to eliminate "multiple GP
regressions" (pp. 5-6); the number of GP models is not stated. The risk
rho_tau is the expected number of planner failures over the MPC-predicted
states, the sum of the per-state failure probabilities (Eq. 12). When rho_tau
exceeds a threshold psi_rho, the robot stops, samples N_p candidate positions
in a free-space polytope C_r around itself with hit-and-run Markov chain
Monte Carlo, converts them to states at rest, rejects the batch when all
failure probabilities exceed eta, picks the state with the lowest expected
failure (Eq. 13), drives there with a go-to-goal MPC constrained to C_r, and
then hands back to the nominal planner (p. 5). Values of T_F, N_p, eta, and
gamma_t are not reported.

The paper has two internal inconsistencies, recorded here once: Sec. V calls
the model a "GP classification model" although Sec. IV-C describes GP
regression (p. 5), and rho_tau is described as "the expected number of
collisions" although Z_tau counts planner failures (p. 5).

## Baselines and controls

The only comparator is the same motion planner without failure detection
and recovery, in simulation (Fig. 6). No other recovery method, soft-
constrained planner, or reactive monitor is compared numerically. The
feature choice is supported by plots of empirical failure probability against
t_C and |C| (Fig. 4(a), (b)), not by an ablation. In hardware, the
without-recovery behavior is described in text only ("both cases lead to
pathplanning failures, which in turn lead to collisions", p. 6); no
without-recovery run is shown with numbers.

## Platform and setup

Simulation: Gazebo on Ubuntu 20.04 with ROS Noetic, a Clearpath Jackal UGV
with a 270-degree 2D LiDAR (p. 5). Training data came from the Poisson random
forest dataset of reference [18]: 10 forest worlds with 90 start and goal
pairs each, with back-end success or failure logged at every planning
iteration (p. 4); the number of data points is not reported. Validation used
four room worlds outside the training set, combining 1 m or 2 m doorways with
sparse or dense obstacles, one start and three goals per world, and 10 runs
per goal, for 120 simulations (pp. 5-6). Robot speeds are not reported.

Hardware: two case studies (p. 6). A Jackal drives around an occluding
corner toward hidden obstacles (Fig. 7), and a Spot quadruped meets an
unexpected dead end (Fig. 1). The GP was trained only on simulation data, and
the threshold was psi_rho = 3 expected failures. The authors state that
further experiments are in the supplementary material and website, which
were not checked.

The paper calls the Jackal a "differential drive UGV" (p. 6); the coding uses
skid-steer because the vocabulary lists the Clearpath Jackal as skid-steer and
Fig. 7(a) shows the four-wheel Jackal. The varied factors (doorway width,
obstacle density, occlusion) have no value in the degradation vocabulary, so
degradation is none; the worlds differ, but no named degradation condition is
reported.

## Evidence type and transfer

Closed-loop hardware is the strongest setting: the planner and recovery
drive the Jackal and the Spot. That evidence is two staged scenarios shown as
snapshots and trajectory plots, with no success count, trial number, or
timing. All numbers come from the 120 simulation runs. The learned failure
probability is checked only by plots of learned against empirical failure
distributions in held-out simulated worlds for |C| = 2 and |C| = 3 (Fig. 4(c),
(d)); no calibration error or detection rate is given.

## Sensors

The method uses an occupancy map and the robot state. In simulation these
come from a 270-degree 2D LiDAR; in hardware, from a Velodyne LiDAR on the
Jackal and an Ouster LiDAR on the Spot, through Gmapping SLAM, which provides
both the map and the state estimate (pp. 5-6). No separate ground-truth
sensor is described.

## Compute and latency

The planner front-end typically runs in under 1 ms and the back-end
typically takes over 100 ms, which the authors give as the reason for not
testing future states by running the solver (p. 3). GP inference takes under
10 ms (p. 4). The processor, where the computation runs on the robots, the
planning rate, and the time spent in recovery are not reported.

## Key quantitative results

Success rates read from the rendered Fig. 6 image (p. 6); each bar is a
fraction of 10 runs. Values are with recovery versus without recovery.

- 1 m doorways, dense: 0.8 versus 0.3 (goal 0), 0.8 versus 0.6 (goal 1), 1.0 versus 0.7 (goal 2) (p. 6, Fig. 6).
- 2 m doorways, dense: 1.0 versus 0.6 (goal 0), 1.0 versus 0.9 (goal 1), 0.9 versus 0.9 (goal 2) (p. 6, Fig. 6).
- 1 m doorways, sparse: 1.0 versus 0.9 (goal 0), 0.9 versus 0.7 (goal 1), 1.0 versus 1.0 (goal 2) (p. 6, Fig. 6).
- 2 m doorways, sparse: 1.0 versus 1.0 (goal 0), 1.0 versus 1.0 (goal 1), 1.0 versus 0.9 (goal 2) (p. 6, Fig. 6).
- Summed over the 12 combinations, these readings give 114 versus 95 successes of 120; the totals are the reviewer's sums from the figure, not numbers printed in the paper (p. 6, Fig. 6).
- Hardware threshold psi_rho = 3 expected failures over the MPC-predicted trajectory; no hardware success rate is reported (p. 6).
- Training set: 10 forest worlds with 90 start and goal pairs each (p. 4).

## Stated limitations

The paper has no limitations section. The authors state these scope points:

- Future work: distributional learning for failure detection to remove the need for multiple GP regressions, planner switching within a Simplex Architecture, and dynamic obstacles (p. 6).
- Recovery candidates are converted to states by assuming the vehicle starts from rest, a choice justified by a smaller sample space and by practice (p. 5).
- The expected value is used as the risk metric for its simplicity and speed, and other risk metrics may be used (p. 5).

## Transfer conditions

The features are specific to a hard-constrained safe-corridor planner (the
time-to-intersect with the current polytope and the corridor size), so the
GP predicts failures of that planner, not collisions in general and not
failures of soft-constrained or sampling planners. Reuse needs the same
planner structure or new training data for another back-end. The posterior
mean is used as a probability without the variance, and the paper reports no
calibration metric, so the threshold psi_rho = 3 is a tuned value, not a
risk bound. The evaluation contains only static obstacles; dynamic obstacles
are future work. The hardware cases give no repetition counts, so the
sim-to-real claim rests on two demonstrations. On a smaller wheeled platform,
the timing (back-end over 100 ms) and the processor need to be measured,
because the paper does not report the hardware.

## Code and data

The paper refers to supplementary material and a website with all
experiments (p. 6) but prints no URL. No code or data release is stated. Not
verified beyond the paper.

## Version family

No other version of this work is in the library. Reference [1] (lessons from
the ICRA 2022 BARN challenge, coauthored by two of the authors) and reference
[2] (the authors' IROS 2022 occlusion-based frontier method) are background
work, not versions of this paper.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Sec. VI, p. 6 | "Without the proposed approach, both cases lead to pathplanning failures, which in turn lead to collisions." |
| C3 | partial-support | weak | Sec. I, p. 1 | "These approaches often rely on complex deep learning models which require exhaustive real world training data to detect the safety of future states." |
| C4 | unset | n/a | | |
| C5 | direct-support | moderate | Abstract, p. 1 | "In order to achieve a high level of robust autonomy, these robots should be able to proactively predict and recover from such failures." |
| C6 | qualifies | weak | Sec. VI, p. 6 | "Presented in this paper are two experiments with two real robotics platforms" |

## Page-cited excerpts

- **p. 3, Sec. IV-B.** "Additionally, the time to run the back-end is typically > 100ms, which is too large to directly test multiple future points for failure."
  The reason for learning a failure predictor instead of running the solver on future states.
- **p. 5, Sec. IV-C.** "These plots show the learned distributions closely match the test distribution, demonstrating that the GP models generalize well to new environments."
  The only check of the learned probabilities is visual, for two corridor sizes, in simulated worlds.
- **p. 5, Sec. IV-D.** "We make this choice because it significantly reduces the sample space and sampling only positions was enough to find recovery states in practice."
  Recovery states are sampled at rest; the robot must be able to stop first.
- **p. 6, Sec. V.** "creating 30 test points per world, for 120 simulations total."
  The success rates in Fig. 6 rest on 10 runs per goal and world.
- **p. 6, Sec. VI.** "Without the proposed approach, both cases lead to pathplanning failures, which in turn lead to collisions."
  The hardware without-recovery outcome is stated in text, without a reported run count.
- **p. 6, Sec. VII.** "Additionally, we would like to utilize this approach for planner switching within a Simplex Architecture and incorporate dynamic obstacles."
  Dynamic obstacles are outside the evaluated scope.

## Survey-usable statements

### Supported

- A GP over two corridor features (time-to-intersect and corridor size) predicts back-end failures of a safe-corridor planner and triggers a stop-and-recover behavior.
- In 120 Gazebo runs, the planner with failure detection and recovery reached the goal at least as often as without it in each of 12 world-goal combinations; the largest gap was 0.8 versus 0.3 (1 m doorways, dense, goal 0).
- A failure predictor trained only in simulation was used without retraining on a Jackal and a Spot in two staged hardware cases.

### Not supported

- Recovery improves success in every world and goal: it ties the no-recovery planner in 4 of 12 combinations (2 m sparse goals 0 and 1, 1 m sparse goal 2, 2 m dense goal 2), and it stays below 1.0 in 4 combinations (1 m sparse goal 1, 2 m dense goal 2, 1 m dense goals 0 and 1).
- The method has a measured hardware success rate or collision reduction: the hardware evidence is two snapshot cases without counts.
- The GP failure probability is calibrated or bounds the collision risk: only visual distribution plots are given and the threshold is a tuned expected failure count.
- The method outperforms other recovery or monitoring methods: the only comparator is the same planner without recovery.
- The method handles dynamic obstacles: they are named as future work.

## Verification log

- 2026-10-27 | host: Kiro | scope: full text read (pp. 1-6; references on p. 7 skipped); Fig. 6 success rates read from the rendered p. 6 image (cropped at 5x zoom); Fig. 4 and Fig. 7 checked on the rendered pp. 5-6 images; all numbers and excerpts located with tools.locate | corrections: format converted to the English template; reviewer observations moved from limitations to Transfer conditions; full Fig. 6 grid added with counterexamples; two internal inconsistencies of the paper recorded (details in tmp/corrections/E59.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/4dfef52aad952fae31be84cd/

## Original abstract

For autonomous mobile robots, uncertainties in the environment and system model can lead to failure in the motion planning pipeline, resulting in potential collisions. In order to achieve a high level of robust autonomy, these robots should be able to proactively predict and recover from such failures. To this end, we propose a Gaussian Process (GP) based model for proactively detecting the risk of future motion planning failure. When this risk exceeds a certain threshold, a recovery behavior is triggered that leverages the same GP model to find a safe state from which the robot may continue towards the goal. The proposed approach is trained in simulation only and can generalize to real world environments on different robotic platforms. Simulations and physical experiments demonstrate that our framework is capable of both predicting planner failures and recovering the robot to states where planner success is likely, all while producing agile motion.
