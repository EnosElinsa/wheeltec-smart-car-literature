# Scenario-based motion planning with bounded probability of collision

## Metadata

| Field | Value |
|---|---|
| ID | E25 |
| Title | Scenario-based motion planning with bounded probability of collision |
| Authors | Oscar de Groot, Laura Ferranti, Dariu M. Gavrila, and Javier Alonso-Mora |
| Venue | The International Journal of Robotics Research, vol. 44, no. 9, pp. 1507-1525 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1177/02783649251315203](https://doi.org/10.1177/02783649251315203) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649251315203 |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2025-Scenario-Safe-Planning-E25/paper.pdf` and `02-fulltext/T3-planning-control/2025-Scenario-Safe-Planning-E25/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-Scenario-Safe-Planning-E25/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware, motion-capture-pose, scripted-scenario, few-trials
- platform_class: skid-steer
- platform: Clearpath Jackal (hardware); simulated unicycle robot; simulated car in CARLA
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, integrity-reliability
- sensors: motion capture for robot and pedestrian positions; EKF for pedestrian velocity
- compute: Intel i9 CPU at 2.4 GHz in simulation; SH-MPC 27 ms mean (66 ms maximum) at 20 Hz with eight pedestrians; hardware computer not reported
- compute_location: not-reported
- summary_result: In eight-pedestrian Gaussian simulation, SH-MPC finished in 16.0 s versus 18.4 s (CC-MPC) and 19.2 s (S-MPCC) at equal joint-risk specification, with maximum joint CP 0.0092 against 0.05.
- summary_limitation: The guarantees rely on an accurate uncertainty model, and real-time performance is tied to 2D environments with disc-shaped collision regions and a support limit estimated online.
- survey_included: yes
- verification_level: full

## Problem

Optimization-based planners usually bound the collision probability (CP)
per planning step and per obstacle (marginal chance constraints). Summing
these marginals over a horizon and over many pedestrians misstates the
actual risk of the planned trajectory and makes the plan conservative,
especially in crowds. The paper asks how to bound, in real time, the joint
probability that the whole planned trajectory collides with any obstacle,
for nonlinear robot dynamics and arbitrary (including multimodal)
predicted distributions of obstacle motion.

## Mechanism

Safe Horizon MPC (SH-MPC) turns the joint chance constraint into a scenario
program. Each sampled scenario is one trajectory of all obstacles over the
horizon. The disc collision constraints are linearized around the previous
plan into halfspaces (Eqs. 13-14), and a recursive halfspace-merging
algorithm (Appendix B) reduces them per time step and robot disc to a
free-space polytope. The authors state the pruning takes less than 100 us
and typically reduces the constraint count by a factor of 10^2 to 10^3;
in one simulation example, 10,816 samples gave polytopes of 11 constraints
on average (p. 8). One joint slack variable d keeps the program always
feasible (p. 7).

The support (the scenarios that fix the solution) is estimated during
optimization as the union of active scenario constraints over all solver
iterations (Theorem 1, p. 9). This requires that each iteration solves a
convex problem and that its iterate satisfies the inequality constraints
(Assumptions 2 and 3, pp. 8-9), which the authors state SQP satisfies. The
sample size S is computed offline by bisection of Eq. (10) from the risk
epsilon, the confidence 1 - beta, and an empirically chosen support limit
(Theorem 2, p. 9). Online, if d = 0 and the estimated support does not
exceed the limit, the plan is certified to have joint open-loop CP at most
epsilon and its first input is applied; otherwise the robot decelerates
at 1.0 m/s^2 (Algorithm 1, p. 9, read from the rendered page). The bound
holds with respect to the predicted distribution when a prediction model
supplies it (p. 5).

Settings: Forces Pro SQP with at most 12 iterations, support limit 10,
epsilon = 0.05 and 1 - beta = 0.99, giving S = 1351 (p. 10); horizon
N = 20 with 0.2 s steps (4.0 s) and a 20 Hz control rate (p. 11). A
projection step, and in rare cases a Douglas-Rachford feasibility program,
keeps the previous plan feasible for linearization (p. 10).

## Baselines and controls

All planners share the MPCC cost (Brito et al. 2019), weights (Table 1),
and solver; only the collision constraints differ (p. 11). Baselines are
deterministic MPC (avoids the mean of each mode), S-MPCC (the authors'
earlier scenario method, marginal CP per time step), and CC-MPC (Gaussian
CDF constraint, marginal CP per time step and obstacle) (p. 10). Each
baseline is run at epsilon_k = epsilon, epsilon/N, and, for CC-MPC,
epsilon/NM. Only S-MPCC at epsilon/N (0.0025) and CC-MPC at epsilon/NM
(0.0003125) match SH-MPC's joint-risk specification (pp. 10-11); the other
settings are not provably safe at the joint level. S-MPCC assumes 20
support constraints, which needs S = 75946 at epsilon_k = 0.0025 (p. 11).
The support estimator is compared with the greedy algorithm of Campi et
al. (2018) in a one-static-pedestrian scenario (p. 12). The hardware runs
have no baseline.

## Platform and setup

Simulation (Secs. 6.1-6.7): a kinematic unicycle robot (radius 0.325 m)
among eight pedestrians (radius 0.3 m). The simulated pedestrians follow
exactly the distribution the planner uses: Gaussian constant-velocity
noise with sigma = 0.3 (Sec. 6.5) or a Markov-chain crossing model giving
a 21-mode Gaussian mixture (GMM, Sec. 6.6) (pp. 10-12). Table 2 reports
100 experiments; Table 3 says only that it follows the notation of Table 2,
so its experiment count is not stated. The joint CP of each plan is
checked offline by Monte Carlo with 10^5 samples (p. 11). The sensitivity
study uses 25 experiments per setting (p. 14, Fig. 9).

CARLA (Sec. 6.9): a simulated car with a second-order bicycle model and
three collision discs, among GMM crossing pedestrians, at 10 Hz;
interaction between vehicle and pedestrians is not modeled (p. 14). Only
snapshots and computation time are reported.

Hardware (Sec. 6.8): a Clearpath Jackal among up to three pedestrians in a
7 m x 9 m space, with all positions from motion capture, a reference
velocity of 1.5 m/s, a second-order unicycle model at 20 Hz, epsilon =
0.05 over 20 steps (4 s), 1 - beta = 0.99, and support limit 6 (p. 13).
Figures 10 and 11 show three runs with one pedestrian and three with three
pedestrians; the total number of runs and the run time are not stated. The
skid-steer coding rests on the named Clearpath Jackal, which the
vocabulary lists as skid-steer; the paper does not state the drive type.

## Evidence type and transfer

The tabulated results (Tables 2 and 3) come from simulation in which the
pedestrian distribution is known to the planner, so they test the planner
"in isolation (i.e., without prediction errors)" (p. 10). The hardware
runs close the loop on a Jackal but report only trajectory images, the
count of support-limit exceedances, and the absence of collisions. They
use motion-capture positions, so they do not test onboard perception or
localization. The CP values are maximum open-loop planned-trajectory risks
estimated by Monte Carlo, not observed collision rates in closed loop.

## Sensors

Hardware: motion capture for the robot and all pedestrians; an EKF
estimates pedestrian velocity, and predictions are Gaussian constant
velocity (p. 13). No onboard LiDAR or camera is used by the method.
Simulation uses ground-truth states.

## Compute and latency

Simulation ran on an Intel i9 CPU at 2.4 GHz (p. 11). Planner runtime per
control step, mean (maximum): SH-MPC 27 ms (66 ms) with Gaussian and 27 ms
(67 ms) with GMM pedestrians, at a 50 ms control period (Tables 2 and 3).
CARLA: 88 ms mean, 135 ms maximum at 10 Hz (p. 14). The hardware computer
and runtime are not reported. Support estimation adds negligible runtime,
whereas greedy support estimation grows with S; in Fig. 7 it reaches about
18 s at S = 1000 (p. 13, read from the rendered image).

## Key quantitative results

- Gaussian, eight pedestrians, joint-risk-matched methods: task duration SH-MPC 16.0 (1.9) s versus CC-MPC (epsilon_k = 0.0003125) 18.4 (2.4) s and S-MPCC (epsilon_k = 0.0025) 19.2 (3.2) s; maximum joint CP 0.0092 versus 0.0019 and 0.0002 against the 0.05 bound (18% of the specification for SH-MPC) (p. 11, Table 2).
- Gaussian: minimum distance SH-MPC 0.34 (0.03) m versus 0.32 (0.07) m (CC-MPC) and 0.55 (0.08) m (S-MPCC); runtime 27 (66) ms versus 11 (33) ms and 83 (286) ms (p. 11, Table 2).
- Gaussian, unmatched settings: deterministic MPC took 10.1 s with maximum joint CP 0.9989 and collided in 102 cases, while the other methods did not collide; CC-MPC at epsilon_k = 0.05 reached maximum joint CP 0.2264 (p. 11, Table 2).
- GMM, eight pedestrians, joint-risk-matched methods: duration SH-MPC 16.3 (4.3) s versus CC-MPC 18.8 (4.4) s and S-MPCC 19.6 (3.0) s; maximum joint CP 0.0107 versus 0.0028 and 0.0002; runtime 27 (67) ms versus 106 (323) ms and 73 (131) ms (p. 12, Table 3).
- GMM: deterministic MPC collided 25 times in total; collisions of the other methods are not reported (p. 12).
- Support limit 10 was reached in 2 of 33,564 planner iterations and never exceeded in the Gaussian runs; in the GMM runs it was exceeded six times and the slack was nonzero 50 times (p. 12, Fig. 8).
- Sensitivity (25 experiments per setting): lowering epsilon from 0.2 to 0.0125 lengthens the mean task duration slightly (reaching about 17.5 s); raising N from 10 to 40 lengthens it from about 16 s to about 24 s while the maximum CP stays near 0.01 (p. 14, Fig. 9, read from the rendered image).
- Hardware: the support limit 6 was never exceeded with one pedestrian and was exceeded 30 times in total with three pedestrians; no collisions were observed (p. 13).

## Stated limitations

- The guarantees rely on an accurate model of the uncertainty, which may be hard to obtain for human motion prediction (p. 14).
- The method cannot account for interaction during planning, because the probability measure cannot depend on the optimization variables (p. 14).
- As a local planner it sometimes becomes infeasible when its intended passing maneuver is impossible within the specified risk; multiple maneuvers in parallel are outside the paper's scope (p. 13).
- Because the support limit is likely higher than necessary for many iterations, the trajectories become conservative (p. 9).
- For extremely low risk specifications (epsilon <= 5 x 10^-3), computation may become excessive due to the larger sample size (p. 15).
- Complex obstacle shapes such as objects with sharp corners cannot yet be handled efficiently, and halfspace merging in 3D may be more complicated (p. 15).
- Support estimation requires a solver that convexifies each iteration, such as SQP, and the user must estimate the support limit (p. 15); real-time performance is tied to 2D environments with disc-shaped regions (p. 16).

## Transfer conditions

A wheeled robot must supply a calibrated predictive distribution of
pedestrian motion; the certificate is only as good as that distribution,
and hardware used constant-velocity Gaussian predictions from motion
capture. Replacing motion capture with onboard detection adds detection
and tracking error that the paper does not test. The support limit (10 in
simulation, 6 on hardware) must be re-estimated for the new scenes. The
maximum runtimes (66-67 ms) exceed the 50 ms control period, and the CARLA
maximum (135 ms) exceeds its 100 ms period, so worst-case timing needs a
check on the target computer, whose identity the paper omits for the
Jackal. The fallback is plain deceleration, with no proof that it is safe.

The paper is inconsistent about the slack sign once: p. 7 says that d <= 0
means no sufficiently safe solution was found, while p. 12 calls d > 0 the
infeasible case and Algorithm 1 accepts only d = 0. The Table 3 caption
refers to Sec. 6.5 although the GMM study is Sec. 6.6 (p. 12).

## Code and data

The paper states that the C++/ROS planner "will be released open source"
(pp. 4, 10). A Jupyter notebook (Google Colab link) for sample-size
computation and a video (https://www.youtube.com/watch?v=vyuNMO1giF0) are
cited (notebook p. 9, link p. 16; video p. 10, URL p. 17). No code repository URL is given; release was not
verified.

## Version family

S-MPCC (de Groot et al., RA-L 2021) is the authors' earlier marginal
scenario method and serves here as a baseline, not as a version of this
work. Partitioned scenario replay (de Groot et al., ICRA 2024) is a cited
follow-up. Neither is in this library.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. 6.5, p. 11 | "The deterministic baseline completes the task faster than the other methods but attains a high CP and consequently collides in total in 102 cases, whereas the other methods do not collide." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | weak | Sec. 6.8, p. 13 | "This could be resolved by increasing the support limit when it is exceeded. In our case, slowing down led to safe behavior." |
| C6 | qualifies | moderate | Sec. 7.1, p. 14 | "The guarantees provided in this paper rely on an accurate model of the uncertainty, which may be challenging to obtain" |

## Page-cited excerpts

- **p. 10, Sec. 6.1.** "We assume throughout that the distribution of pedestrian motion is known in order to evaluate the performance of the planner in isolation (i.e., without prediction errors)."
  The tabulated simulation results exclude prediction error by design.
- **p. 11, Sec. 6.5.** "The deterministic baseline completes the task faster than the other methods but attains a high CP and consequently collides in total in 102 cases, whereas the other methods do not collide."
  Ignoring uncertainty is fastest but unsafe; the comparison is in simulation.
- **p. 13, Sec. 6.8.** "We did not observe collisions in any of the experiments."
  The hardware safety evidence is the absence of collisions over an unstated number of runs.
- **p. 14, Sec. 7.** "It cannot yet account for interaction during planning, where the dynamics of the robot and pedestrians directly influence each other"
  Robot-pedestrian interaction is outside the guarantee.
- **p. 15, Sec. 7.2.** "we currently cannot efficiently handle more complex shaped obstacles, such as objects with sharp corners."
  The real-time efficiency depends on disc-shaped collision regions.

## Survey-usable statements

### Supported

- Bounding the joint CP of the whole planned trajectory, instead of per-step and per-obstacle marginals, gave shorter task durations than marginal baselines with the same joint-risk specification in eight-pedestrian simulations (16.0 s versus 18.4 s and 19.2 s, Gaussian).
- Estimating the scenario support from active constraints across SQP iterations certifies each plan online at negligible extra cost, whereas greedy support estimation takes roughly S + 1 times as long.
- SH-MPC kept its runtime at 27 ms mean with a 21-mode GMM, while CC-MPC rose to about 100 ms or more.
- The planner ran closed loop on a Jackal among up to three pedestrians with motion-capture positions, without observed collisions.

### Not supported

- SH-MPC is best on every metric. Table 2: deterministic MPC (10.1 s), CC-MPC at 0.05 (10.3 s), and S-MPCC at 0.05 (15.6 s) are faster; four of six baselines have lower mean runtime (10-13 ms versus 27 ms); S-MPCC at 0.05 (0.36 m) and at 0.0025 (0.55 m) keep larger minimum distances. Table 3: deterministic MPC is faster (11.7 s), and S-MPCC at 0.05 (0.41 m), S-MPCC at 0.0025 (0.42 m), and CC-MPC at 0.0003125 (0.45 m) keep larger minimum distances.
- SH-MPC is safer than the baselines: its maximum joint CP (0.0092 and 0.0107) is higher than that of the risk-matched baselines; the method is less conservative by design.
- The bound holds for real pedestrians: it holds with respect to the predicted distribution, the simulations used the true distribution, and hardware reports no risk or collision statistics.
- The planner meets hard real-time deadlines: maximum runtimes of 66-67 ms exceed the 50 ms period, and 135 ms exceeds the 100 ms CARLA period.
- The method is validated on a real autonomous car: the vehicle results come from CARLA only, with snapshots and computation time.
- The guarantee covers task-level or continuous-time safety: it bounds the open-loop CP of a 4 s discrete-time plan.

## Verification log

- 2026-10-27 | host: Kiro | scope: full text read (Secs. 1-8 and Appendices A-B); Tables 2 and 3, Algorithm 1, and Figs. 7, 8, 9, and 10 read from rendered images of pp. 9, 11, 12, 13, and 14; raw PDF text of pp. 7, 10, and 13 checked; the abstract is copied from the transcription, which joins some words that the PDF prints separately (for example "Optimization-basedplanners") | corrections: rebuilt in English template format; Table 3 experiment count marked as not stated; slack-sign inconsistency located; author limitations separated from reviewer observations; counterexamples added for the comparison claims; coding added (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/6e258cc8ea1987ea10f28e81/

## Original abstract

Robots will increasingly operate near humans that introduce uncertainties in the motion planning problem due to their complex nature. Optimization-basedplanners typically avoid humans through collision avoidance chance constraints. This allows the planner to optimize performance while guaranteeing probabilistic safety. However, existing real-time methods do not consider the actual probability of collision for the planned trajectory but rather its marginalization, that is, the independent collision probabilitiesfor each planning step and/or dynamic obstacle, resulting in conservative trajectories. To address this issue, we introduce a novel real-time capable method termed Safe Horizon MPC that explicitly constrains thejointprobability ofcollision with all obstacles over the duration ofthe motion plan. This is achieved by reformulating the chance-constrainedplanning problem using scenario optimization andpredictive control. Out ofsampled realizations ofhuman motion, we identify which cases affect the optimization. This allows us to certify the planned trajectory in realtime. Our method is less conservative than state-of-the-art approaches, applicable to arbitrary probability distributions of the obstacles’trajectories, computationally tractable and scalable. We demonstrate ourproposed approach using a mobile robot and an autonomous vehicle in an environment shared with humans.
