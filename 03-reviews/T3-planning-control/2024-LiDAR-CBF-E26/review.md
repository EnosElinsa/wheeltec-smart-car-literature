# LiDAR-Based Online Control Barrier Function Synthesis for Safe Navigation in Unknown Environments

## Metadata

| Field | Value |
|---|---|
| ID | E26 |
| Title | LiDAR-Based Online Control Barrier Function Synthesis for Safe Navigation in Unknown Environments |
| Authors | Shaghayegh Keyumarsi, Made Widhi Surya Atman, and Azwirman Gusrialdi |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 2, pp. 1043-1050 |
| Year | 2024 (online 2023) |
| Type | journal |
| DOI | [10.1109/lra.2023.3339059](https://doi.org/10.1109/lra.2023.3339059) |
| Official URL | https://ieeexplore.ieee.org/document/10339852/ |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2024-LiDAR-CBF-E26/paper.pdf` and `02-fulltext/T3-planning-control/2024-LiDAR-CBF-E26/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2024-LiDAR-CBF-E26/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: motion-capture-pose, offboard-compute, speed-capped, few-trials
- platform_class: differential-drive
- platform: three TurtleBot3 Burger robots
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: sensor-fault
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: 2D LiDAR (360 beams at 1 degree, 5 Hz, 1 m range used); robot pose from Vicon
- compute: remote Intel i7 PC; GP plus QP 7.96 ms mean, 21.11 ms maximum per step
- compute_location: offboard-local
- summary_result: In one run of three TurtleBot3 Burgers at 0.15 m/s, the GP-CBF filter avoided static and dynamic obstacles; GP plus QP took 7.96 ms mean, 21.11 ms maximum.
- summary_limitation: QP feasibility relies on unconstrained inputs (input constraints may make it infeasible); safety across data updates needs a fast update rate; LiDAR anomaly detection is out of scope.
- survey_included: yes
- verification_level: full

## Problem

A control barrier function (CBF) needs a safety function whose superlevel
set is the safe set, which is not available when the environment is unknown.
Earlier online-learned CBFs for unknown environments accumulate labelled
samples or need prior knowledge about obstacles, and the authors state that
they apply only to static environments. The paper builds a LiDAR-based safety
function online, from the current scan only, so that a CBF quadratic program
(QP) can filter a nominal controller around static and moving obstacles.

## Mechanism

The safety function h(x) is the posterior mean of a Gaussian process (GP)
over the robot position. The GP prior has a constant mean of +1 (safe unless
data say otherwise) and a squared exponential kernel with scalar length scale
l, unit signal scale, and a noise term sigma_N. Training points are only
obstacle-edge positions from the current LiDAR scan, labelled -1, and an edge
point is added only if it lies farther than d_sample from the points already
accepted (eq. 14). The data set is rebuilt at every scan and nothing is
stored. The GP variance is not used; the authors argue it would require more
frequent sampling (p. 4). Proposition 1 shows that h is 1 beyond a distance
d_safe set by the kernel and approaches -1 at sampled edges.

The control is the QP min ||u - u_nom||^2 subject to the single CBF
constraint (16b), with gamma(h) = h^3 in the experiments. When no obstacle is
detected, the nominal input is applied directly (Remark 1). The theoretical
preconditions are a control-affine model, robot state known at time t, a safe
start, and unconstrained inputs. Under these, Proposition 2 states that h is
a valid CBF and the QP is feasible, and Proposition 3 states forward
invariance of the switching zero-superlevel set, under Assumption 1 that the
state stays in the intersection of consecutive safe sets during each data
update. The authors state that a speed upper limit for a given sampling time
and d_safe is computable (p. 5), but they do not give its value. On the
unicycle robots, a go-to-goal controller (gain 0.8) drives a virtual point
ahead of the robot through a near-identity diffeomorphism; the offset r is
not reported. Parameters: l = 0.17 (d_safe = 0.558 m), sigma_N = 0.01,
d_max = 1, and d_sample = 0.05 (the last two without units in the paper).

## Baselines and controls

No experimental baseline is run. Table I (p. 6) compares the method in words
with a sparse Bayesian classifier CBF [16], a supervised machine-learning
(support vector machine) CBF [13], and the Gaussian CBF of [17] by data
acquisition, single-pass or accumulative data collection, prior knowledge,
and applicability to time-varying environments. The table is a design
comparison, with no measured data size, runtime, or safety outcome for the
comparators. There is no ablation, for example of d_sample, l, or the
variance term.

## Platform and setup

Closed-loop hardware only; there is no simulation. Three TurtleBot3 Burger
robots run concurrently in a 5.3 m by 3 m field with static obstacles; each
robot goes to its own goal and treats the other two as dynamic obstacles.
The environment is unknown to the robots except for their safe start
positions. The speed limit is 0.15 m/s, and the robot radius is 0.089 m.
Robot positions come from Vicon. The LiDAR runs at 5 Hz with 1 degree
resolution (M = 360). The paper reports one experiment of about 21 s
(Fig. 4 time axis), with snapshots at 5.4 s, 9.7 s, and 16 s (Fig. 3) and a
video. The drive type is from the text: the abstract calls the robots
unicycle-type, and eq. (20) is the unicycle model.

## Evidence type and transfer

The CBF filter rectifies the nominal command sent to the physical robots, so
the evidence is closed-loop hardware. The safety outcome rests on one
three-robot run shown in snapshots, minimum-distance plots, and a video;
there is no repeated-trial statistic, collision count, or success rate. The
only tabulated metrics are data size and computation time (Table II). The
setting has low speed, external motion-capture pose, and offboard compute, so
it does not show the effect of onboard localization error or onboard
processing on the safety guarantee. The robots' mutual avoidance is the
designed dynamic-obstacle condition; the robots do not communicate. LiDAR
noise from reflective surfaces and fast rotation was met during the run and
is coded as observed (a spurious near-zero range reading).

## Sensors

Each robot's onboard 2D LiDAR provides the obstacle edges (only returns
closer than d_max are used). The robot state used in eq. (22) and in the
controller comes from Vicon localization. No camera, IMU, or odometry is used
by the method.

## Compute and latency

All computation runs on a remote PC with an Intel i7 processor, and the
control input is sent to each robot over Wi-Fi as ROS messages (p. 6). Per
control step, Table II (p. 7) gives a GP time (data acquisition, GP training,
and evaluation of h and its gradient) of 7.66 ms mean and 21.11 ms maximum,
and a GP plus QP time of 7.96 ms mean and 21.11 ms maximum. The minimum of
0 ms is the no-obstacle branch that applies the nominal input. The paper does
not report network latency, end-to-end command delay, memory use, or the
processor model beyond "Intel i7".

## Key quantitative results

- Data size per step: 0, 119, and 153 detected edges (minimum, mean, maximum) versus 0, 30, and 43 training points after the sampling-distance rule (p. 7, Table II, read from the rendered page).
- Computation per step on the remote PC: GP 7.66 ms mean and 21.11 ms maximum; GP plus QP 7.96 ms mean and 21.11 ms maximum; 0 ms when no obstacle is detected (p. 7, Table II).
- The three robots head toward their goals and avoid collision with static and dynamic obstacles; the text does not state that they reached their goals (p. 7, Figs. 3 and 4).
- The red and blue robots detect each other between 2.9 s and 9.8 s, and the red and green robots from 9.7 s to the end of the run (p. 7).
- In Fig. 4(b), the blue robot's minimum LiDAR distance drops for a moment below the dashed minimum-safe-distance line near t = 4 s; the authors attribute the jump to LiDAR noise, and the reading recovers at the next scan (pp. 7-8, Fig. 4).
- In the other curves of Fig. 4, the minimum distance stays above the dashed line; the plots carry no tabulated minimum-distance values (p. 8, Fig. 4).

## Stated limitations

- Adding control input constraints to the QP may make it infeasible for a general control-affine system (p. 5).
- The forward-invariance result needs Assumption 1, which the authors say is ensured in practice by a smaller sampling time, for example a faster LiDAR; a speed upper limit exists for a given sampling time and d_safe (p. 5).
- With a slow update rate, a larger d_safe (larger l) is recommended, while narrow entrances need a smaller l (p. 8, Remark 2).
- The QP remains feasible unless the LiDAR senses zero distance to a sampled edge, which the authors call rare (p. 7).
- LiDAR readings are noisy, sensitive to reflective surfaces, and noisier at high rotational speed; anomaly detection on LiDAR readings is left out of scope (pp. 7-8).
- The GP variance is not included in the safety function (p. 4).
- Resolving CBF deadlock with high-level planner features is future work (p. 8).

## Transfer conditions

The guarantee assumes known state and unconstrained inputs, while the test
used Vicon pose and a 0.15 m/s speed limit on 0.089 m radius robots. On a
robot with onboard LiDAR odometry or AMCL, pose error moves every obstacle
edge in eq. (22), and its effect on h is not studied. Real wheel speed and
acceleration limits break the unconstrained-input precondition of
Proposition 2, so a deployment needs a fallback when the QP becomes
infeasible. With l = 0.17, h starts to drop 0.558 m from an obstacle, which
can block narrow corridors (Remark 2), and the speed limit that satisfies
Assumption 1 at 5 Hz is not computed. The control mapping is written for
unicycle kinematics; an Ackermann robot would need a different model and
nominal controller. Runtime figures are for a desktop Intel i7, not an
embedded computer. There is a single CBF constraint for all obstacles, and
no deadlock handling.

## Code and data

The paper links an experiment video (https://youtu.be/T_68wJbRJgY, p. 7). It
does not state that code or data are released. The article is published
under a CC BY 4.0 license (p. 1).

## Version family

No conference version, preprint, or extension is named in the paper or found
in the library. The paper is counted once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Sec. V-B, p. 7 | "Reflective surfaces result in larger inconsistencies in the LiDAR readings." |
| C3 | partial-support | weak | Abstract, p. 1 | "Additionally, online learning is needed for the robot to maneuver in an unknown environment which leads to dealing with the sampled data set size, memory, and computational complexity." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV-B, p. 5 | "Note that for general control affine system (1) adding control input constraints to the QP (16) may potentially lead to infeasibility." |

## Page-cited excerpts

- **p. 4, Sec. IV-A.** "It should be noted that the formulation does not incorporate the variance since including it would require more frequent sampling, contradicting the goal of efficient sampling."
  The safety function uses the GP mean only, so model uncertainty does not enlarge the margin.
- **p. 5, Sec. IV-B.** "The above assumption can be ensured in practice by having a smaller sampling time (for example using a LiDAR with a fast update rate)."
  The invariance result depends on update rate and speed; the paper does not check the assumption for its 5 Hz LiDAR.
- **p. 6, Sec. V-A.** "All computations are done remotely on a PC with an Intel i7 processor."
  The runtime figures are offboard desktop figures, not onboard ones.
- **p. 7, Sec. V-B.** "The GP is relatively fast because of having a small dataset and no sparsification method is required."
  The speed comes from the bounded single-scan data set (at most 43 points in the run).
- **p. 7, Sec. V-B.** "It is worth noting the QP in (16) remains feasible unless the LiDAR senses zero distance to a sampled obstacle edge which is a rare occurrence."
  The authors qualify the feasibility statement of Proposition 2 for the experiment.
- **p. 8, Sec. V-B.** "One optional way to deal with this issue is to have the anomaly detection on the LiDAR reading but we leave this as it is beyond the scope of this letter."
  Spurious LiDAR readings are handled only by rebuilding the data set at the next scan.
- **p. 8, Sec. VI.** "In the future, we aim to add high-level planner features like resolving dead-lock situations of CBFs to our algorithm."
  Deadlock is not handled.

## Survey-usable statements

### Supported

- A CBF safety filter can be built online from the current LiDAR scan alone, with a GP whose prior mean is +1 and whose training set holds only sparsified obstacle edges labelled -1, without storing past data.
- In one three-robot TurtleBot3 Burger run at 0.15 m/s with Vicon pose and a remote Intel i7 PC, the filter kept the robots clear of static obstacles and of each other.
- The sampling-distance rule reduced the GP training set to at most 43 points (mean 30) from up to 153 detected edges, with GP plus QP time of 7.96 ms mean and 21.11 ms maximum on the remote PC.

### Not supported

- The method is collision-free over repeated trials or has a measured safety rate: one run is reported, without statistics.
- The method runs in real time onboard a small robot: all computation ran on a remote Intel i7 PC over Wi-Fi.
- The method works with onboard localization: robot pose came from Vicon.
- The method is faster or safer than the CBFs of [13], [16], and [17]: Table I is a qualitative design comparison without experiments on the comparators.
- The robots reached their goals: the text states only that they headed toward their goals and avoided collision.
- The safety guarantee holds for robots with input limits or at higher speed: Proposition 2 assumes unconstrained inputs, and the speed limit for Assumption 1 is not computed.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read; Table II read from the rendered p. 7 image; Fig. 4 read from the rendered p. 8 image; Proposition 1 and setup text checked on pp. 4-7 | corrections: rewritten in English to the template; goal arrival not stated; author limitations separated from reviewer observations; online year added; unitless parameters noted (details in tmp/corrections/E26.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/e5e553e157c86b205c63b76d/

## Original abstract

This letter presents a novel extension of the control barrier function (CBF) as the low-level safety controller for autonomous mobile robots navigating in unknown environments. The main challenges of implementing CBF in real-world situations arise from the absence of a model or the lack of an exact one for the environment. Additionally, online learning is needed for the robot to maneuver in an unknown environment which leads to dealing with the sampled data set size, memory, and computational complexity. We address these challenges by designing an online non-parametric LiDAR-based safety function using the Gaussian process (GP). It is both efficient in data size and eliminates the requirement to store previous data. Then, a CBF is synthesized using the proposed safety function to rectify the safe control input. The effectiveness of the LiDAR-based CBF synthesis for navigation in unknown environments was validated by conducting experiments on unicycle-type robots.
