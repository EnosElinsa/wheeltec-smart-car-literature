# Circulation-embedded Control Barrier Function for safe navigation: A solution to avoid undesired equilibria and dysfunctional circulation

## Metadata

| Field | Value |
|---|---|
| ID | E22 |
| Title | Circulation-embedded Control Barrier Function for safe navigation: A solution to avoid undesired equilibria and dysfunctional circulation |
| Authors | Shaghayegh Keyumarsi, Made Widhi Surya Atman, and Azwirman Gusrialdi |
| Venue | Robotics and Autonomous Systems, vol. 194, article 105132 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1016/j.robot.2025.105132](https://doi.org/10.1016/j.robot.2025.105132) |
| Official URL | https://linkinghub.elsevier.com/retrieve/pii/S0921889025002295 |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2025-CECBF-E22/paper.pdf` and `02-fulltext/T3-planning-control/2025-CECBF-E22/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-CECBF-E22/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: multi-robot
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: video-only-hardware, motion-capture-pose, offboard-compute, speed-capped, few-trials
- platform_class: differential-drive
- platform: TurtleBot3 Burger (one robot; four robots in the deadlock test)
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: 2D LiDAR (360 samples, 5 Hz, range set to 0.5 m); Vicon motion capture for robot position
- compute: remote Intel i7 PC over Wi-Fi and ROS; 0.02 s step; mean 0.485 ms per step for parameters and QP solve
- compute_location: offboard-local
- summary_result: One TurtleBot3 run passed a nonconvex obstacle with circulation held from about 9 s to 46 s, while the no-hold variant stayed trapped; mean filter runtime 0.485 ms.
- summary_limitation: Feasibility under other system dynamics or added constraints is beyond the paper's scope, and extending circulation to 3D is stated to be challenging.
- survey_included: yes
- verification_level: full

## Problem

A CBF quadratic program (CBF-QP) used as a safety filter can create
undesired equilibria where the rectified input is zero although the nominal
go-to-goal input is not, and the robot slows down near these points. Adding
circulation only briefly can produce "dysfunctional circulation": the robot
loops between circulating and returning to the same trap, especially at
nonconvex obstacles. The paper asks how to remove these equilibria and the
slowdown while keeping a convergence guarantee for a planar robot in an
unknown environment.

## Mechanism

The robot is modeled as a 2D single integrator. The IB-CE-CBFQP (Eq. 11)
minimizes the deviation from the nominal input subject to the CBF
constraint, a linear circulation constraint u_cir^T u >= k_sts, and a box
bound |u|_inf <= u_m/sqrt(2). The circulation direction is the safety
gradient rotated by plus or minus pi/2 (Eqs. 16-17). A sigmoid coefficient
k_cir (Eq. 14) depends on the angle psi between -grad h and the nominal
input and on h relative to a proximity threshold h_c^0, and k_sts (Eq. 12)
maps it to the range from -u_m to k_abs. Inspired by Bug algorithms, a
Boolean Hold_kcir keeps circulation active once k_cir exceeds 1 - epsilon_1,
until the distance to the goal is at least epsilon_2 smaller than at
activation (Algorithm 1, p. 5).

Feasibility (Proposition 1), continuity (Proposition 2), the absence of
equilibria other than the goal (Theorem 1), and convergence (Theorem 2) are
argued for the single integrator under Assumption 1: the state stays where
the tangent T(N(x)) is continuous, the goal lies in that region and in the
safe set, and h measures distance to the unsafe set (p. 3). The convergence
proof is a short argument built on the hold logic, not a Lyapunov analysis
(p. 8).

On hardware, the safety function and its gradient are the mean of a
Gaussian process fitted online to LiDAR returns, from the authors' earlier
work (reference [18]): squared exponential kernel with a noise term, prior
mean 1, unsafe points labelled -1, length scale 0.14 for static and 0.18
for time-varying scenes, sigma = 0.01, and minimum sampling distance 0.05
(p. 9). For the moving-robot test, the constraint includes a -0.4 offset
and outdated data are discarded each step (p. 9). Circulation parameters
are h_c^0 = 0.8, a = 30, k_abs = 0.7 u_m/sqrt(2) (0.07 m/s), psi_1 = pi/8,
and b = 0.67 (p. 9). A near-identity diffeomorphism with a control point
0.06 m ahead of the wheel axle maps the single-integrator input to linear
and angular velocity (p. 9). The nominal controller is proportional with
gain 1.

## Baselines and controls

The only experimental comparator is the authors' own CBF-QP with
circulation but without Hold_kcir (Experiment 2). That run is not a clean
ablation: its Fig. 12 caption gives a speed limit of 0.07 m/s, and the
plotted input norm is capped near 0.07 m/s, while Experiment 1 runs at the
0.1 m/s bound (Figs. 8 and 12, pp. 9 and 11); the start and goal positions
are not stated for either run. The standard CBF-QP is never run: its
equilibria are derived analytically (Sec. 2.2), and the claim that the
four-robot start and goal positions trap all robots under standard CBF-QP
(p. 8) is not shown. Table 1 (p. 2) compares properties of prior methods
([9], [10], [12], [13]) as judged by the authors; none of them is run.

## Platform and setup

All experiments use TurtleBot3 Burger robots in a 5.3 m x 3 m field
(p. 9; the MinerU transcription reads 15.3 m). Robot position comes from
Vicon; LiDAR data arrive at 5 Hz with 1 degree resolution, and the range is
set to 0.5 m. The speed limit is u_m = 0.1 sqrt(2) m/s, so each velocity
component is limited to 0.1 m/s (p. 9). Three scenarios are run, each shown
as one run with trajectory snapshots and time plots: (1) one robot passing
an unknown nonconvex obstacle with Algorithm 1; (2) the same task without
Hold_kcir; (3) four robots on the vertices of a square, each driving to the
opposite vertex so that the paths meet in the center, without communication
(pp. 9-12). The drive type is differential, from the unicycle model of
Eq. (31) and the control point defined relative to the midpoint between the
wheels (pp. 8-9).

## Evidence type and transfer

All results are closed-loop hardware runs: the filter output drives the
robots. Fig. 4 (p. 6) is a schematic, not a simulation result, and the
paper reports no simulation results; a simulation version is only offered in
the repository (p. 14). The evidence is one run per scenario, given as
figures without tabulated metrics, with Vicon positions and an offboard PC.
The paper describes the experiments as using on-board LiDAR in an unknown
environment, but the robot position comes from motion capture, so the runs
do not test the method under onboard localization error. The theory covers
the single integrator only; the unicycle mapping used on hardware is not
covered by the propositions.

## Sensors

A 2D LiDAR on each robot (360 samples per scan, 5 Hz, range limited to
0.5 m) builds the GP safety function. Vicon motion capture provides the
robot position used by the controller (p. 9). No other sensor is used.

## Compute and latency

All computation ran on a remote PC with an Intel i7 processor; control
inputs went to the robots over Wi-Fi as ROS messages, with a 0.02 s step
(p. 9). The QP is solved with DAQP through the qpsolvers package,
warm-started from the previous solution. The time to compute the parameters
and solve Eq. (11) per sample ranged from 0.010 ms to 2.126 ms, with a
mean of 0.485 ms (p. 10). This excludes the GP update, LiDAR processing,
and network delay; no end-to-end latency is reported.

## Key quantitative results

- Experiment 1 (Algorithm 1): circulation activated at about 9 s and stayed active until about 46 s, when the distance to the goal fell below its value at activation; the robot then reached the goal (pp. 9-10, Figs. 5 and 6; k_cir and k_sts curves read from the rendered p. 8 image).
- Experiment 1: the minimum sensed LiDAR distance stays above the robot-radius line throughout, with its lowest value near 0.2 m around 40 s (p. 9, Fig. 7, read from the plot).
- Experiment 1: the input norm drops from the 0.1 m/s bound to roughly 0.05-0.07 m/s during circulation; the authors call this a small drop caused by k_abs = 0.07 m/s, not a significant deceleration (pp. 9-10, Fig. 8, read from the plot).
- Experiment 2 (no Hold_kcir): circulation activates at 18 s, k_cir then switches repeatedly between -1 and 1, and the robot stays confined to the corner where it was first stuck for the plotted 50 s, without collision (pp. 10-11, Figs. 9-12).
- Experiment 3 (four robots, no communication): the central deadlock is resolved and all robots reach their goals; each robot's minimum sensed LiDAR distance stays at or above about 0.28 m, and the input norms decay after about 23 s as the robots arrive (pp. 11-13, Figs. 13-16, read from the rendered p. 13 image).
- Filter runtime per sample (parameters and QP): minimum 0.010 ms, maximum 2.126 ms, mean 0.485 ms on the i7 PC (p. 10).

## Stated limitations

- The detailed feasibility of the CBF with additional restrictive constraints or other system dynamics is beyond the paper's scope; only the effect of the circulation inequality and input bounds is analyzed (p. 6).
- Extending circulation to 3D and higher dimensions is challenging, because a single loop around an obstacle does not ensure exploration of its surface; the authors state that a path-planning method in the reduced space of the obstacle surface would be needed (p. 5, Remark 2).
- The TurtleBot3 Burger did not move for commands around 0.01 m/s or lower, so the input only approaches zero near the goal (p. 10, Remark 3).

## Transfer conditions

The guarantees assume a single integrator, a continuous nonzero safety
gradient along the path (Assumption 1), and a goal with h(x_g) > h_c^0. A
car-like robot needs its own mapping from the planar input; the paper
covers only the differential-drive mapping. All runs used Vicon positions;
with onboard odometry, pose drift would enter the LiDAR-based safety
function, which the paper does not test. The parameters h_c^0, a, b, and
k_abs and the moving-obstacle offset of -0.4 were set for one robot type
and a 0.1 m/s component bound, and no sensitivity study is reported.
The paper contains three internal inconsistencies. The Fig. 12 caption
gives a 0.07 m/s limit against 0.1 m/s elsewhere (see Baselines). The
time-varying constraint is written with "<= 0" (p. 9) while Eq. (11b)
uses ">= 0". The proof of Theorem 2 releases circulation on the distance
to the obstacle (p. 8), while Algorithm 1 uses the distance to the goal.

## Code and data

Code is linked at https://github.com/sh-keyumarsi/Circulation-embedded-CBF
(p. 1, footnote 2). Appendix A states that the repository holds a
simulation implementation that reproduces the experiments, with source code
and generated data (p. 14). The experiment video is at
https://youtu.be/69W5bmbBVcI (pp. 7, 10, 12). The data availability
statement says that no data was used (p. 14). The repository was not
checked.

## Version family

The LiDAR-based GP safety function comes from the same authors' RA-L 2024
paper (reference [18]), which is E26 in this library. E22 adds the
circulation constraint, the hold logic, and the input bounds, so the two
papers are counted separately; E22 should not be cited as independent
evidence for the GP safety function itself.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | weak | Abstract, p. 1 | "CBF-QP is prone to deadlocks, especially in dynamic and multi-agent environments, although it also occurs with convex obstacles" |
| C3 | unset | n/a | | |
| C4 | qualifies | weak | Sec. 6.4, p. 11 | "relying solely on online LiDAR measurements, without any communication between robots or prior knowledge of the environment" |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. 6.2, Remark 3, p. 10 | "The TurtleBot3 burger that we used does not respond to very small linear velocity commands at Nebolab (our Laboratory)." |

## Page-cited excerpts

- **p. 9, Sec. 6.1.** "The robot position was tracked using a Vicon localization system, and all computations were performed on a remote PC equipped with an Intel i7 processor."
  Pose came from motion capture and computation was offboard; neither the localization nor the compute load was onboard.
- **p. 10, Sec. 6.2.** "the minimum runtime recorded was 0.000010 s, the maximum runtime was 0.002126 s, and the average runtime was 0.000485 s."
  The runtime covers parameter computation and the QP solve only, not the GP update or the network link.
- **p. 10, Sec. 6.3.** "Over time, this leads to the robot becoming confined to the same corner where it initially became stuck"
  The no-hold variant fails in one run; the run also used a lower speed bound than Experiment 1.
- **p. 11, Sec. 6.4.** "The initial and goal positions are selected so that the trajectories will intersect at a central point, creating the potential for a deadlock situation."
  The multi-robot deadlock is staged in one symmetric configuration with four robots.

## Survey-usable statements

### Supported

- Holding circulation until the distance to the goal has decreased (a Bug-style memory) let a LiDAR-based CBF filter pass a nonconvex obstacle in one TurtleBot3 run where the same filter without the hold stayed trapped.
- A circulation-embedded CBF-QP resolved a staged four-robot crossing deadlock without communication in one hardware run, with Vicon positions and offboard computation.
- The circulation-embedded QP is cheap to solve: mean 0.485 ms and maximum 2.126 ms per step on a desktop i7, against a 20 ms control step.

### Not supported

- The method outperforms standard CBF-QP or the methods of [9], [10], [12], or [13] in experiments: none of them is run; Table 1 lists properties judged by the authors.
- The method removes all slowdown: the input norm still drops to roughly 0.05-0.07 m/s during circulation (Fig. 8).
- The hold mechanism alone explains the Experiment 2 failure: the no-hold run also used a 0.07 m/s speed bound instead of 0.1 m/s.
- The method works with onboard localization or onboard compute: all runs used Vicon positions and a remote i7 PC.
- The robots succeed reliably: each scenario is one run, with no repetitions, success rates, or varied start and goal positions.
- The guarantees hold for the unicycle robots used: the propositions cover the single integrator only.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read (Secs. 1-7 and Appendix A); raw PDF text of pp. 1, 8-11, and 14 checked for setup values, runtime, and URLs; Table 1 and Figs. 4, 6, 7, 8, 10, 11, 12, 15, and 16 read from rendered images of pp. 2, 6, 8, 9, 11, and 13 | corrections: rebuilt in English template format; ablation no longer described as identical apart from the hold (different speed bound); standard CBF-QP marked as not run; speed-label inconsistency narrowed to the Fig. 12 caption; field size taken from the PDF; limitations restricted to author statements; coding added (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/327d799a7d215b32b1756a70/

## Original abstract

The Control Barrier Function (CBF) is widely adopted in safety-critical applications such as safe navigation in an unknown environment. CBF quadratic program (CBF-QP) is a conventional CBF framework that acts as a safety filter. However, CBF-QP is prone to deadlocks, especially in dynamic and multi-agent environments, although it also occurs with convex obstacles. Specifically, CBF-QP suffers from several challenges, including undesired equilibria, accompanying slowdown behavior around these points, dysfunctional circulation, and becoming trapped in the obstacle. In this paper, we propose a practical solution to address these issues. First, we introduce the foundational principles and parameters for the proposed circulation-embedded CBF algorithm, which incorporates an effective circulation linear inequality constraint into CBF-QP. Moreover, input bounds constraints are incorporated to ensure that the rectified input is readily applicable and optimal. Then, we study the feasibility, continuity, equilibrium points, and convergence of the proposed circulation-embedded CBF-QP algorithm through propositions and formal proofs. Finally, the effectiveness of the proposed algorithm is demonstrated through experiments and comparisons involving unknown nonconvex obstacles and multi-robot scenarios without communication. The source code is released for the reference of the community.
