# Adaptive High-Order Control Barrier Function-Based Iterative LQR for Real Time Safety-Critical Motion Planning

## Metadata

| Field | Value |
|---|---|
| ID | E24 |
| Title | Adaptive High-Order Control Barrier Function-Based Iterative LQR for Real Time Safety-Critical Motion Planning |
| Authors | Xiangyu Kong, Wentao Ning, Yuanqing Xia, Zhongqi Sun, and Huahui Xie |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 7, pp. 6099-6106 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3398506](https://doi.org/10.1109/lra.2024.3398506) |
| Official URL | https://ieeexplore.ieee.org/document/10522835/ |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2024-HOCBF-iLQR-E24/paper.pdf` and `02-fulltext/T3-planning-control/2024-HOCBF-iLQR-E24/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2024-HOCBF-iLQR-E24/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation, theory-only
- protocol_caveats: external-pose-source, offboard-compute, few-trials
- platform_class: wheeled-unspecified
- platform: wheeled mobile robot with a UWB positioning system (drive type not recorded in the legacy extraction)
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task
- sensors: ultra-wideband positioning system for robot and obstacle poses (up to 50 Hz)
- compute: Intel i5-12400 PC, Python qpsolvers; HOCBF-ILQR inputs within the 0.05 s sampling period
- compute_location: offboard-local
- summary_result: On a UWB-localized wheeled robot, HOCBF-ILQR computes each control input within the 0.05 s sampling period, while RB-ILQR needs at least 0.62 s in simulation.
- summary_limitation: The robot model is assumed known; the authors leave model uncertainty in real-time motion planning to future work.
- survey_included: yes
- verification_level: light

## Problem

In real-time obstacle avoidance with input constraints, a standard HOCBF with fixed parameters can make the safety QP infeasible.

## Mechanism

An unconstrained ILQR first produces a nominal input, and a HOCBF-QP then corrects it as a safety filter. AHOCBF adds a positive auxiliary variable beta that scales the highest-order class-K term and penalizes deviation from beta0. The feasibility result depends on the intermediate psi_i being strictly positive and on the model assumptions.

## Baselines and controls

- HOCBF-ILQR (internal comparison).
- RB-ILQR, in simulation only; it knows the obstacles in advance and has no input bounds.

## Platform and setup

A wheeled robot in hardware experiments. UWB localizes the robot and the obstacles at up to 50 Hz; ROS control runs at 20 Hz with Delta t = 0.05 s. Robot and obstacle radii are 0.35 m and 0.4 m; the goal is 3.9 m away; two obstacles are revealed at 0.75 s and 1.9 s; the dynamic obstacle moves at about 0.4 m/s (p. 6).

## Evidence type and transfer

The legacy card lists safety and feasibility theory, hardware tests with static and moving obstacles, and a computation-time comparison with RB-ILQR in simulation. The robot is driven by the planner, but poses come from UWB and the computation runs on a PC.

## Sensors

UWB external positioning; the tests are not a validation of onboard perception in unknown scenes.

## Compute and latency

Intel i5-12400 PC at 4.40 GHz with Python qpsolvers (p. 6). In both hardware cases, HOCBF-ILQR computes each input within 0.05 s (p. 7). RB-ILQR needs at least 0.62 s, under different comparison conditions (p. 7, Table I).

## Key quantitative results

- Input bound and feasibility: HOCBF-ILQR is feasible at ±0.7 rad/s and infeasible at ±0.65 rad/s, while AHOCBF-ILQR stays feasible at the tighter bounds tested (p. 7, Figs. 8-9).
- Computation time: HOCBF-ILQR computes control inputs within 0.05 s in hardware Cases 1 and 2 (p. 7, Fig. 7); the legacy card notes that this timing should not be attributed to every AHOCBF setting.
- RB-ILQR computation time: at least 0.62 s in simulation with prior obstacle knowledge and no input bounds (p. 7, Table I).

## Stated limitations

- Uncertainties in the robot model are left to future work (p. 8).

## Transfer conditions

Legacy reviewer observations: the experiments are small and low-speed with UWB localization, without stress tests of onboard vision or LiDAR noise and occlusion. The RB-ILQR baseline knows the obstacles in advance and has no input constraints, so its conditions differ from those of the hardware method. No multi-seed safety rates are reported.

## Code and data

Video: https://youtu.be/mcptl9zBVYE (p. 5). The legacy card found no code or data link in the text; not verified.

## Version family

The text does not declare a conference extension. The paper is distinct from the other CBF papers in this batch; the library counts this DOI once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | V-B Experiment platform, p. 6 | "The UWBPS provides localization and attitude information about the robot and obstacles at a maximum frequency of 50 Hz." |

## Page-cited excerpts

- **p. 7, VI-C Computation Time.** "In both cases, control inputs are computed within 0.05 s."
  The timing holds for HOCBF-ILQR in the two reported hardware cases.
- **p. 6, V-B Experiment platform.** "The UWBPS provides localization and attitude information about the robot and obstacles at a maximum frequency of 50 Hz."
  Robot and obstacle states come from an external positioning system.
- **p. 7, RB-ILQR comparison.** "The robot has known the positions of obstacles before moving, and input constraints are not taken into account."
  The RB-ILQR comparison runs under easier, different conditions.
- **p. 7, Fig. 8 caption.** "HOCBF-ILQR encounters the infeasibility issue when the input bound is progressively tightened."
  Shows the infeasibility that AHOCBF addresses.
- **p. 8, Conclusion.** "In future works, we plan to consider the uncertainties in the robot model"
  Model uncertainty is outside the evaluated scope.

## Survey-usable statements

### Supported

- A HOCBF safety filter on top of unconstrained ILQR computes inputs within a 0.05 s sampling period on a PC for a UWB-localized wheeled robot avoiding static and moving obstacles.
- An auxiliary variable in the highest-order HOCBF term keeps the QP feasible under tighter input bounds in the authors' test (±0.65 rad/s; number from a light review, re-check before citing).

### Not supported

- HOCBF-ILQR is faster than RB-ILQR under equal conditions: RB-ILQR ran in simulation with prior obstacle knowledge and no input bounds.
- Onboard real-time performance: the computation ran on a desktop PC.
- Safety rates over repeated trials: none are reported.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; legacy quote trimmed to its second sentence (the first has a line-break hyphen); excerpts added from the platform, baseline, Fig. 8, and conclusion text
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/6c3b7c78bea29f9a0a5b1d62/

## Original abstract

This letter proposes an adaptive high-order control barrier function-based iterative linear quadratic regulator (AHOCBF-ILQR) algorithm for real time safety-critical motion planning. Firstly, we propose a HOCBF-ILQR method, where a HOCBF-based controller is designed as a safety filter of ILQR to guarantee safety. Then, to address the potential infeasibility issue in HOCBF-ILQR, AHOCBF-ILQR is proposed by introducing an auxiliary variable. In AHOCBF-ILQR, only an unconstrained optimization problem and a quadratic programming need to be solved within a sampling interval. The low computation burden significantly enhances the time efficiency of AHOCBF-ILQR. Furthermore, we provide theoretical proof of the safety and feasibility of AHOCBF-ILQR. The algorithms are tested by motion planning experiments for a wheeled mobile robot, where the robot is required to navigate around static or moving obstacles that are unknown in advance. The experimental results show that AHOCBF-ILQR can solve the control inputs within 0.05 s, and ensure safety.
