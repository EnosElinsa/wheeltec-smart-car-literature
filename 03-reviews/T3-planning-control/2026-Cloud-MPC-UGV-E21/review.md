# Vehicle-Cloud Cooperative Trajectory Planning via Switched Model Predictive Control for UGVs in Unstructured Transportation Environment

## Metadata

| Field | Value |
|---|---|
| ID | E21 |
| Title | Vehicle-Cloud Cooperative Trajectory Planning via Switched Model Predictive Control for UGVs in Unstructured Transportation Environment |
| Authors | Rong Wang, Dong Chen, Nan Li, Hang Gao, Yunfeng Hu, Yongfu Li, Hong Chen, and Xun Gong |
| Venue | IEEE Transactions on Intelligent Transportation Systems, vol. 27, no. 8, pp. 9517-9528 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tits.2026.3679729](https://doi.org/10.1109/tits.2026.3679729) |
| Official URL | https://ieeexplore.ieee.org/document/11480935/ |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2026-Cloud-MPC-UGV-E21/paper.pdf` and `02-fulltext/T3-planning-control/2026-Cloud-MPC-UGV-E21/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2026-Cloud-MPC-UGV-E21/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation, theory-only
- protocol_caveats: motion-capture-pose, offboard-compute, simulated-agents-on-hardware, video-only-hardware, few-trials
- platform_class: ackermann
- platform: small-scale Ackermann UGV in a 3 m by 3 m test site (drive type from the text, p. 10); Gazebo/ROS vehicle model in simulation
- boundary_platform: no
- degradation: dynamic-objects, communication-delay-loss
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: NOKOV optical motion capture for robot and obstacle poses
- compute: Intel i7-10700 PC for simulation and cloud NMPC; onboard computer for LMPC; 0.1 s update period
- compute_location: mixed
- summary_result: In Gazebo simulation with up to 0.2 s delay, switched onboard LMPC and cloud NMPC lowers collision rate by 32%-77% relative to standalone planners.
- summary_limitation: The authors place wireless timeouts and dropouts outside the operational design domain; round-trip latency above 0.2 s triggers a fail-safe stop.
- survey_included: yes
- verification_level: light

## Problem

Cloud NMPC has more computing power, but network latency harms local obstacle avoidance. Onboard LMPC runs in real time, but its linear approximation is conservative. The paper combines both for UGV trajectory planning in unstructured environments.

## Mechanism

Hybrid A* gives the global reference. An onboard LMPC and a cloud NMPC optimize in parallel. A risk-based switching policy picks the candidate trajectory with the lower weighted risk over obstacle safety, tracking, and heading feasibility. The models assume a planar low-speed bicycle model and a preset constant speed. A round-trip delay above 0.2 s or packet loss triggers a safe stop.

## Baselines and controls

- Standalone LMPC (no delay).
- Standalone NMPC, with the same delay and with ideal zero delay.

## Platform and setup

Simulation: two 4 m by 4 m Gazebo/ROS scenes, each with 100 runs over random initial configurations of dynamic obstacles; uplink and downlink delays are artificially buffered up to 0.2 s. Hardware: a small Ackermann vehicle in a 3 m by 3 m site, NOKOV optical localization, static physical obstacles, and a virtual dynamic obstacle.

## Evidence type and transfer

The legacy card lists a conditional finite-time boundedness discussion, statistics over 100 simulation runs per scene, and a feasibility test on a scaled Ackermann vehicle. The hardware test shows trajectories that reach the goal and avoid obstacles, without repeated-trial safety rates. The collision-rate reduction is a simulation result.

## Sensors

NOKOV motion capture measures the robot and the obstacles. The method assumes accurate localization and short-term obstacle prediction; it is not a demonstration of onboard perception in unknown scenes.

## Compute and latency

Simulation and cloud: Intel i7-10700 at 2.9 GHz with 16 GB (p. 7). LMPC uses OSQP (ADMM); NMPC uses Acados with HPIPM and RTI; horizon 40 steps; update period 0.1 s. The text names the onboard computer a Raspberry Pi 4B but also describes it as a 6-core NVIDIA Carmel CPU with 8 GB (p. 10); the legacy card flags this as a hardware-description inconsistency that needs clarification by the authors. On the onboard computer, one LMPC step takes 6 to 8 times longer than on the PC; the legacy card notes that most but not all steps fit in the 0.1 s period.

## Key quantitative results

- Collision rate: cooperative framework 32% to 77% lower than a single planner across traffic conditions, as a relative reduction in simulation, not zero collisions (p. 9).
- Single-step LMPC computation time: onboard computer 6- to 8-fold the PC time for identical scenarios (p. 10).

## Stated limitations

- Wireless communication timeouts or dropouts are outside the operational design domain; latency above the 0.2 s threshold switches the vehicle to a fail-safe stop (p. 6).

## Transfer conditions

Legacy reviewer observations: the safe stop on network failure is not shown to be reachable from every position. The stability discussion relies on the terminal stability conditions of each MPC and on bounded switching jumps, giving finite-time boundedness rather than an unconditional asymptotic stability or safety proof. On hardware the dynamic obstacle is virtual, the delay is artificially buffered, and the test site is small. Constant speed, accurate localization, and obstacle prediction limit transfer. The hardware inconsistency and the tolerance-based feasible-solution mechanism need clarification before reproduction.

## Code and data

Video: https://youtu.be/yoaIMrOZkfc (p. 10). The legacy card found no code or data release in the text; not verified.

## Version family

The paper explicitly extends the authors' earlier vehicle-cloud cooperative tracking work [29], adding non-convex obstacle-avoidance constraints, a dedicated risk metric, and hardware experiments (the earlier version had only unconstrained tracking in simulation). The library counts this journal paper once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | qualifies | weak | Remark 2, p. 6 | "Scenarios involving wireless communication timeouts or dropouts are considered outside the operational design domain of the cooperative planning system." |
| C6 | qualifies | moderate | Real-vehicle experiments, p. 10 | "a virtual dynamic obstacle is simulated in the scenario to ensure it moves strictly along the trajectory specified by the system." |

## Page-cited excerpts

- **p. 9, IV-B Performance Evaluation of Transportation Tasks.** "reduces the collision rate by 32% to 77% compared to a single planner"
  The 32%-77% figure is a relative reduction from simulation, not a hardware collision rate.
- **p. 6, Remark 2.** "Scenarios involving wireless communication timeouts or dropouts are considered outside the operational design domain of the cooperative planning system."
  Network failure is handled by stopping, not by the cooperative planner.
- **p. 10, Real-vehicle experiments.** "a virtual dynamic obstacle is simulated in the scenario to ensure it moves strictly along the trajectory specified by the system."
  The hardware dynamic obstacle is virtual and scripted.
- **p. 10, Real-vehicle experiments.** "6- to 8-fold"
  The onboard LMPC step is several times slower than on the PC.

## Survey-usable statements

### Supported

- Running onboard LMPC and delayed cloud NMPC in parallel with risk-based switching lowers the simulated collision rate by 32%-77% relative to either planner alone, for delays up to 0.2 s (number from a light review; re-check before citing).
- The hardware test is a feasibility demonstration on a small Ackermann vehicle with motion capture and a virtual dynamic obstacle.

### Not supported

- The framework is safe under network outages: timeouts and dropouts are outside the operational design domain and trigger a stop.
- Hardware collision statistics: the hardware test reports no repeated-trial safety rate.
- The onboard hardware is clearly identified: the text names a Raspberry Pi 4B and describes an NVIDIA Carmel CPU.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; legacy quote trimmed to the part found on the PDF page (ligatures in "different traffic"); excerpts added from Remark 2 and the hardware section
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/d9920090d920b14d747deb94/

## Original abstract

Recent advances in cloud computing and vehicleto-everything (V2X) communication have created significant opportunities for intelligent transportation systems (ITS), particularly for tackling complex, high-level autonomous navigation tasks in unstructured environment that exceed the capabilities of onboard computing alone. However, the inherent uncertainty and latency of current wireless networks present a critical challenge to the safe deployment of cloud-based computation in safety-critical vehicular applications. To overcome these limitations, we propose a vehicle–cloud cooperative planning framework built on a parallel planning architecture. This approach simultaneously harnesses onboard and cloud resources: a lightweight linear model predictive control (LMPC) runs locally on the vehicle for fast, low-latency responses, while a more computationally intensive nonlinear model predictive control (NMPC) executes on the cloud for enhanced foresight and optimality. A risk-based switching policy dynamically selects the optimal outputs of both planners, ensuring real-time adaptability and robustness in complex, unstructured trafic scenarios. Extensive simulation studies demonstrate that the proposed cooperative framework reduces collision probabilities by 32%–77% compared to standalone planners across diverse scenarios. The framework’s practical feasibility and realworld viability are further substantiated through experiments conducted on a purpose-built, scalable real-vehicle testing platform, marking a critical extension of our collaborative research from simulation to physical implementation.
