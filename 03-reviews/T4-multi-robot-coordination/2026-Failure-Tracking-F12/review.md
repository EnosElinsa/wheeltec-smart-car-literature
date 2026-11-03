# Failure-Aware Multi-Robot Coordination for Resilient and Adaptive Target Tracking

## Metadata

| Field | Value |
|---|---|
| ID | F12 |
| Title | Failure-Aware Multi-Robot Coordination for Resilient and Adaptive Target Tracking |
| Authors | Peihan Li, Jiazhen Liu, Yuwei Wu, and Lifeng Zhou |
| Venue | IEEE Transactions on Automation Science and Engineering, 23, 4023–4038 |
| Year | 2026 (online 2025) |
| Type | journal |
| DOI | [10.1109/tase.2025.3647786](https://doi.org/10.1109/tase.2025.3647786) |
| Official URL | https://ieeexplore.ieee.org/document/11313787/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Failure-Tracking-F12/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Failure-Tracking-F12/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Failure-Tracking-F12/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: fault-recovery-deployment
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware, scripted-scenario
- platform_class: aerial
- platform: Crazyflie drones tracking Yahboom ROSMASTER X3 ground vehicles
- boundary_platform: yes
- degradation: sensor-fault, communication-partition
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: range and bearing target observations; inter-robot communication; hardware sensing implementation not specified in targeted pages
- compute: ForcesPro nonlinear solve and velocity control at 10 Hz; drone attitude control at 500 Hz; processor/solver location not reported
- compute_location: not-reported
- summary_result: Across six simulated failure scenarios, adaptive tracking reportedly reduced target-estimation MSE versus vanilla and motion-primitive controls; staged hardware trajectories have no tabulated MSE.
- summary_limitation: The authors identify dynamic danger zones, partial degradation, and more realistic failure models as future work.
- survey_included: yes
- verification_level: light

## Problem

Teams tracking moving targets may lose sensing or communications temporarily or permanently in initially unknown danger zones (pp. 1, 5–6). The paper asks how the connected subgroup and isolated robots can continue the task while discovering those zones. For the survey, it separates recovery after temporary disconnection from permanent loss of a tracking agent. It is primarily an aerial tracking demonstration, with ground vehicles as targets rather than controlled wheeled agents (p. 13).

## Mechanism

Connected robots form a communication league and jointly optimize target-estimation quality, control effort, and soft chance constraints around inferred sensing and communication hazards (pp. 5–7). Weights and sensing-zone clearance adapt with the number of attacked robots; temporary attacks trigger a ten-step conservative cooldown (p. 7). Isolated robots use individual planning. A permanently communication-isolated robot abandons tracking and circles to signal the hazard to observers (pp. 7, 10, 13–14). The target estimator uses an EKF; covariance intersection merges a temporarily disconnected robot's estimate with the league's estimate upon reunion (p. 8). That merge concerns target estimates, not a shared-map reconciliation guarantee.

## Baselines and controls

The simulations compare adaptive planning with a vanilla non-adaptive tracking controller and a motion-primitive controller across sensing, communication, and combined failure modes (pp. 8–12). A separate comparison with Mayya et al. [9] limits benchmarking to permanent sensor failures, the condition considered by that baseline; risk settings were hand-tuned and curves smoothed (p. 12). Hardware pages show the proposed trajectories under staged hazards, not a matched hardware baseline with tabulated tracking errors (pp. 13–14).

## Platform and setup

Simulation includes three tracking robots and three targets under temporary/permanent sensing, communication, and combined danger zones, with 300 steps at 0.1 s in the sensing-failure example (pp. 8–11). Hardware uses three Crazyflie drones tracking three Yahboom ROSMASTER X3 ground vehicles in scenes with initially unknown sensing, communication, or combined zones (pp. 13–14). ForcesPro optimization and velocity control run at 10 Hz; onboard drone attitude control runs at 500 Hz (p. 13). The paper does not identify the drone planner's processor or compute location in those pages.

## Evidence type and transfer

The method drives physical drones in staged tracking scenarios, so the strongest setting is closed-loop hardware. Simulation supplies the tabulated MSE/trace comparison; physical results in the targeted pages are trajectories and snapshots, not the same numeric comparison (pp. 11–14). The ground vehicles are targets, not evidence that this planning controller works on wheeled ground robots. Permanent communication loss can end the isolated robot's tracking contribution, while the rest of the team may continue (pp. 10–11).

## Sensors

The target-tracking model uses range and bearing observations and communication among robots (pp. 3–4, 7). The targeted hardware section names Crazyflie/Crazyswarm and targets but does not specify exactly which physical sensor produced the range/bearing observations or the target ground-truth method (p. 13); those details remain unverified.

## Compute and latency

The paper reports ForcesPro nonlinear optimization and drone velocity commands at 10 Hz and onboard attitude control at 500 Hz in hardware (p. 13). It does not report solver hardware, whether the planner ran onboard or offboard, or an end-to-end failure-detection-to-replan latency in the targeted pages. Do not infer planner placement from the fact that the attitude loop is onboard.

## Key quantitative results

- Simulated sensing, communication, and combined failure cases each include temporary and permanent variants; Table II reports MSE and covariance trace for adaptive, vanilla, and motion-primitive control, but its cells were not independently checked (pp. 11–12, Table II).
- The physical controller ran nonlinear optimization/velocity control at 10 Hz while drone attitude control ran at 500 Hz; these are loop rates, not a measured failure-recovery time (p. 13).
- The benchmark with [9] is restricted to permanent sensing failure; no like-for-like benchmark of [9] on communication or temporary failures is shown (p. 12).

## Stated limitations

- The authors identify mobile or dynamic danger zones, partially degraded sensing, stochastic fault propagation, and multimodal attack patterns as future extensions (p. 14).
- They also propose optimized drone trajectory planning to improve realism and deployment feasibility (p. 14).

## Transfer conditions

Applying the logic to wheeled robots would need a compatible vehicle-dynamics controller, access to range/bearing target estimates, connectivity/failure detection, and a way for teammates to observe an isolated robot's circular signal. The model assumes a uniformly connected communication league with effectively infinite inter-robot range among members and instant sharing after a temporary reconnection (pp. 5, 7). The covariance-intersection step is an estimate-fusion method; it does not prove consistency of maps or state after arbitrary network partitions (p. 8).

## Code and data

The targeted pages cite Crazyswarm and ForcesPro dependencies (pp. 13, 15). A release of this method's code or experiment data was not identified; availability not verified.

## Version family

The journal article builds on earlier temporary-failure optimization [13] and compares with risk-aware tracking [9] (pp. 5, 12); these are related methods, not established duplicate versions. This library counts F12 once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | strong | Sec. IV-B, p. 6 | "The communication ability permits robots to plan as a team, while an isolated member performs individual planning." |
| C5 | partial-support | moderate | Sec. IV-B, p. 6 | "temporary failures (e.g., transient signal dropouts, brief sensor occlusions) warrant adaptive strategies that anticipate recovery" |
| C6 | qualifies | moderate | Sec. V-C, p. 13 | "we use Crazyflie drones [50] as tracking robots and Yahboom ROSMASTER X3 ground vehicles [51] as targets." |

## Page-cited excerpts

- **p. 6, Sec. IV-B.** "The communication ability permits robots to plan as a team, while an isolated member performs individual planning."
  This supports mode switching across a team; it does not ensure a disconnected agent shares a current global state.
- **p. 8, Sec. IV-C.** "To merge the two pieces of information together, we apply CI:"
  This identifies the target-estimate reunion step, not proof of map consistency.
- **p. 10, Sec. V-A2.** "it forfeits its tracking task and enters a circular motion around the communication danger zone."
  The permanent-isolation policy trades that robot's tracking contribution for a passive hazard signal.

## Survey-usable statements

### Supported

- The paper implements mode-dependent target tracking under sensing and communication failures; connected agents coordinate while isolated agents plan individually (pp. 5–8).
- Simulations compare six failure conditions, and staged Crazyflie tests show closed-loop drone trajectories while ground robots serve as targets (pp. 8–14).

### Not supported

- Continuous tracking by a permanently isolated robot is not shown: the robot forfeits tracking and circles (p. 10).
- Covariance intersection after temporary reunion is not a proof of network-wide map consistency, and no wheeled-controller experiment is reported (pp. 8, 13).

## Verification log

- 2026-11-02 | host: Codex | scope: light targeted abstract, model, coordination, evaluation, and conclusion reading on physical pp. 1, 3–8, 10–14; publisher BibTeX and excerpts checked; tables and full paper not independently verified | corrections: new F12 review; permanent isolation, reunion, and aerial-boundary scope made explicit.
- Legacy extraction: none; new follow-up paper reviewed directly from publisher PDF.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

Multi-robot coordination is crucial for autonomous systems, yet real-world deployments often encounter various failures. These include both temporary and permanent disruptions in sensing and communication, which can significantly degrade system robustness and performance if not explicitly modeled. Despite its practical importance, failure-aware coordination remains underexplored in the literature. To bridge the gap between idealized conditions and the complexities of real-world environments, we propose a unified failure-aware coordination framework designed to enable resilient and adaptive multi-robot target tracking under both temporary and permanent failure conditions. Our approach systematically distinguishes between two classes of failures: 1) probabilistic and temporary disruptions, where robots recover from intermittent sensing or communication losses by dynamically adapting paths and avoiding inferred danger zones, and 2) permanent failures, where robots lose sensing or communication capabilities irreversibly, requiring sustained, decentralized behavioral adaptation. To handle these scenarios, the robot team is partitioned into subgroups. Robots that remain connected form a communication group and collaboratively plan using partially centralized nonlinear optimization. Robots experiencing permanent disconnection or failure continue to operate independently through decentralized or individual optimization, allowing them to contribute to the task within their local context. We extensively evaluate our method across a range of benchmark variations and conduct a comprehensive assessment under diverse real-world failure scenarios. Results show that our framework consistently achieves robust performance in realistic environments with unknown danger zones, offering a practical and generalizable solution for the multi-robot systems community.
