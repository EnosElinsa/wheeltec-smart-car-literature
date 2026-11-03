# C-CBF: Communication-Aware Control Barrier Functions for Resilient Multi-Robot Connectivity

## Metadata

| Field | Value |
|---|---|
| ID | F13 |
| Title | C-CBF: Communication-Aware Control Barrier Functions for Resilient Multi-Robot Connectivity |
| Authors | Truong-Son Nguyen, Huy-Nhat Cao, Nguyen Huu Thai, and Minh Trien Pham |
| Venue | IEEE Transactions on Automation Science and Engineering, 23, 5596–5614 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2026.3667964](https://doi.org/10.1109/tase.2026.3667964) |
| Official URL | https://ieeexplore.ieee.org/document/11417164/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-C-CBF-F13/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-C-CBF-F13/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-C-CBF-F13/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: simulation
- evidence_all: simulation
- protocol_caveats: none
- platform_class: aerial
- platform: abstract 2D double-integrator agents; ArduPilot quadrotors in network-in-the-loop simulation
- boundary_platform: yes
- degradation: communication-delay-loss, communication-partition
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: simulated relative position and obstacle observations; modeled or ns-3 link reception, RSSI/SINR
- compute: QPs on Intel i9-13900K PC CPU; network-in-the-loop controller at 10 Hz and QP solve below 10 ms
- compute_location: desktop-offline
- summary_result: In an eight-quadrotor network-in-the-loop simulation, the controller ran at 10 Hz with QP solves below 10 ms during jammer stress.
- summary_limitation: The authors state that velocity-level guarantees, model-dependent link estimates, and network-in-the-loop tests require further physical validation.
- survey_included: yes
- verification_level: light

## Problem

Multi-robot motion can preserve geometric separation while losing wireless links under fading, or preserve links by constraining goal progress (pp. 4, 9). The paper places modeled reception probability and collision distance in a distributed barrier-control formulation. It qualifies the survey's connectivity-control discussion by making channel estimation, goal-progress tradeoffs, and constraint relaxation explicit. Its strongest test is simulation, including a packet-network/quadrotor co-simulation, not physical robot hardware (pp. 8, 12, 15).

## Mechanism

Each agent constructs a local QP from its nominal velocity, neighbor states, a distance-based collision barrier, and a communication barrier defined by estimated link reception probability minus a reliability threshold (pp. 5–8). Reception probability is approximated using a Rician fading/SINR model or smooth surrogate. Neighbor controls use last-known values; adaptive nonnegative slack keeps the QP feasible when constraints conflict, at the cost of possible barrier violations (pp. 7–8, 12). The tightened variant needs an estimated model-error margin for its conditional invariance argument (pp. 6–8). Links below the chosen threshold are excluded by the stated execution protocol, so the method is not a guarantee that every pairwise link remains reliable (p. 8).

## Baselines and controls

The JAX simulation compares behavior-based control (goal seeking, obstacle avoidance, cohesion) and decentralized collision-only CBF; a centralized C-CBF also appears in statistical scalability results (pp. 9–12). The authors do not implement an MPC or Laplacian-based comparator under the same fading model (pp. 9, 15). The network-in-the-loop section is a stress test of the proposed controller under a timed jammer, not a reported physical hardware baseline (pp. 12–14).

## Platform and setup

Core experiments use 2D second-order integrator agents in JAX, with simulated relative sensing, polygonal static obstacles, and Rician link degradation. Scenarios include 2, 4, and 12 agents and 100 randomized environments for the scaling comparison (pp. 8–10). The network-in-the-loop test connects ns-3, Gazebo, ArduPilot SITL, and MAVSDK for eight simulated quadrotors in a 30 m × 30 m arena; jamming is staged for 30 s within a 140 s trial (pp. 12–13). The outer-loop controller exchanges commands at 10 Hz, while Gazebo/ArduPilot simulate the aircraft and inner-loop control (p. 12).

## Evidence type and transfer

The 2D tests and ns-3/Gazebo/ArduPilot network-in-the-loop experiment are simulation evidence. The latter adds packet-level network effects and nonlinear simulated aircraft dynamics, but no physical radio, robot, or onboard processor (pp. 12, 15–16). The paper's probabilistic barrier claims depend on accurate or bounded channel-model error, differentiable reliability, feasible velocity control, and inner-loop tracking assumptions (pp. 4–7, 15). Slack and weak-link exclusion qualify any blanket statement that all safety and connectivity constraints always hold (pp. 7–8, 12–13).

## Sensors

Simulated agents receive relative positions of nearby agents and obstacles (p. 8). Link reliability is inferred from modeled Rician fading and, in the network-in-the-loop test, ns-3 per-link measurements (pp. 8, 12). The proposed real deployment would require relative pose and RSSI/SINR or similar telemetry; this was not validated on physical sensors (pp. 6, 16).

## Compute and latency

The authors measure local-QP solve time on an Intel i9-13900K PC CPU, reporting under 10 ms for simulated cases including teams up to 50 agents; this is not an embedded-board timing result (p. 15). In network-in-the-loop simulation, the outer loop and network update at 10 Hz, with reported nominal/jammed QP times below 10 ms (pp. 12, 14). The paper suggests Raspberry Pi or Jetson feasibility but does not report tests on them (p. 15).

## Key quantitative results

- In the eight-quadrotor network-in-the-loop stress test, the authors report QP solve time below 10 ms and a 10 Hz control loop; this is a simulation PC timing, not measured onboard latency (pp. 12, 14–15).
- In the opposing-goal 2-, 4-, and 12-agent scenarios, the controller preserves the modeled links by compacting formation, but goal progress can stall or be delayed (pp. 9–10, Figs. 4–5).
- During staged jamming, only a subset of links met the reliability threshold; the paper describes a usable backbone, not all-pairs connectivity at threshold (p. 13, Table II; table cells not independently checked).

## Stated limitations

- The reliability threshold biases agents toward compact formations, potentially impeding wide-area exploration; threshold and slack penalty need tuning (p. 15).
- The safety argument relies on the fading surrogate; worst-case or non-stationary channel uncertainty remains open, and a rigorous extension from velocity-level abstraction to nonlinear dynamics is absent (p. 15).
- Network-in-the-loop testing does not replace distributed physical hardware deployment; onboard limits and large physical teams remain untested (p. 15).

## Transfer conditions

On a wheeled robot, validate the motion model and wheel-level tracking, relative-neighbor localization, wireless-channel estimation, interference, thresholds, and feasible QP constraints. The paper initially calls the graph undirected but also permits asymmetric directed channels (p. 4), so implementation must define which links and neighbors are enforced. Penalized slack can preserve optimization feasibility while relaxing the original barrier; pruning links below threshold does not recover a missing link automatically (pp. 7–8). Physical packet-delivery and onboard timing must be measured before deployment claims.

## Code and data

The paper says simulations extend GCBF+ in JAX and use ns-3, Gazebo, ArduPilot SITL, and MAVSDK (pp. 8, 12). A release of C-CBF code or trial logs was not identified in the targeted pages; availability not verified.

## Version family

No earlier version of this exact C-CBF article was established from the targeted text. GCBF+ is an implementation framework cited by the authors, not an identified duplicate version. Count this journal article once as F13.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | strong | Sec. IV-C, p. 7 | "each agent constructs and solves its QP locally using only its own state and those of its neighbors." |
| C5 | partial-support | moderate | Sec. V-E, p. 13 | "the swarm re-expands and the number of reliable links rises again." |
| C6 | qualifies | strong | Limitations and scope, p. 15 | "Finally, the Network-in-the-Loop experiments validate the framework under realistic wireless and UAV dynamics, but do not replace a fully distributed hardware deployment." |

## Page-cited excerpts

- **p. 7, Sec. IV-C.** "each agent constructs and solves its QP locally using only its own state and those of its neighbors."
  This supports local information use under the simulation assumptions.
- **p. 8, Sec. IV-C.** "constraints related to agent j are excluded from the QP."
  This limits a reading of all-link connectivity enforcement.
- **p. 15, Limitations and scope.** "Finally, the Network-in-the-Loop experiments validate the framework under realistic wireless and UAV dynamics, but do not replace a fully distributed hardware deployment."
  The authors explicitly distinguish network-in-the-loop simulation from physical validation.

## Survey-usable statements

### Supported

- C-CBF couples modeled wireless reception and collision distance in per-agent QPs, with slack to trade constraint satisfaction against feasibility (pp. 5–8).
- Its strongest test is ns-3/Gazebo/ArduPilot network-in-the-loop simulation; jamming adaptation and PC solve times do not establish a physical robot deployment (pp. 12–15).

### Not supported

- The paper does not show that every link remains above threshold: below-threshold links can be excluded, and the network-in-the-loop results use a subset backbone (pp. 8, 13).
- A claim of unconditional forward invariance despite arbitrary fading, slack, infeasible controls, and nonlinear wheeled dynamics is not supported by the stated assumptions or experiments (pp. 4–8, 15).

## Verification log

- 2026-11-02 | host: Codex | scope: light targeted PDF read of physical pp. 1, 4–16; publisher BibTeX and excerpts checked; Table II cells and full paper not verified | corrections: new F13 review; simulation, conditional guarantee, and weak-link/slack limits explicit.
- Legacy extraction: none; new follow-up paper reviewed directly from publisher PDF.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

Ensuring resilient operation in networked multi-robot systems is critical when both physical safety and wireless communication are challenged by environmental uncertainty or adversarial interference. This paper presents Communication-Aware Control Barrier Function (C-CBF), a scalable control framework that integrates probabilistic communication constraints into safety-critical control synthesis using Control Barrier Functions (CBFs). By modeling wireless degradation via Rician fading, we formulate a reception-aware constraint that is optimized jointly with inter-agent collision avoidance through local Quadratic Programs (QPs). Each robot computes its control input using only neighbor state information. A decoupled approximation of globally coupled constraints ensures real-time feasibility. Adaptive slack variables enable the system to remain feasible even under conflicting demands, enhancing robustness in complex environments. Simulation results demonstrate that C-CBF ensures safe and connected operation across large-scale, cluttered environments under severe fading conditions. A confidence-tightened variant guarantees forward invariance in probability under channel-model mismatch. This leads to graceful degradation of safety without additional runtime cost. This framework provides a scalable foundation for resilient multi-robot autonomy and can be integrated with distributed optimal control solvers in future work.
