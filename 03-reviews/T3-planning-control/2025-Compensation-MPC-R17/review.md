# Safe Trajectory Generation for Nonholonomic Multi-Robot Systems: A Compensation-Based MPC Approach

## Metadata

| Field | Value |
|---|---|
| ID | R17 |
| Title | Safe Trajectory Generation for Nonholonomic Multi-Robot Systems: A Compensation-Based MPC Approach |
| Authors | Zhixu Du, Hao Zhang, Peiyu Cui, Zhuping Wang, and Huaicheng Yan |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tase.2025.3613403](https://doi.org/10.1109/tase.2025.3613403) |
| Official URL | https://ieeexplore.ieee.org/document/11176148/ |
| Theme folder | T3-planning-control |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2025-Compensation-MPC-R17/paper.pdf` and `02-fulltext/T3-planning-control/2025-Compensation-MPC-R17/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2025-Compensation-MPC-R17/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, numerical
- protocol_caveats: motion-capture-pose, offboard-compute, few-trials
- platform_class: differential-drive
- platform: Four Quanser Qbot2 robots with motion capture and a host computer (p. 10).
- boundary_platform: no
- degradation: model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: Motion-capture poses
- compute: Host computer; 0.05 s sampling period over 132 steps (p. 10).
- compute_location: offboard-local
- summary_result: An online discrepancy estimator corrects the predictive model of distributed NMPC with CBF, physical and stability constraints in simulation and a four-robot experiment (pp. 8-11).
- summary_limitation: Deadlock during collaborative obstacle avoidance is future work (p. 11).
- survey_included: yes
- verification_level: light

## Problem

Model mismatch and conflicting safety and stability constraints degrade MPC for nonholonomic teams.

## Mechanism

Each robot estimates the discrepancy between its predictive model and actual motion; nonlinear MPC includes CBF, physical and stability constraints with a dynamic safety-stability gain; piecewise Bezier curves smooth trajectories; recursive feasibility and stability are analyzed (pp. 3-8).

## Baselines and controls

A standard framework with an ideal predictive model (p. 8).

## Platform and setup

Numerical simulations and one motion-capture experiment with four robots (pp. 8-10). Four Quanser Qbot2 robots with motion capture and a host computer (p. 10).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Hardware execution with external pose and offboard computation.

## Sensors

Motion-capture poses.

## Compute and latency

Host computer; 0.05 s sampling period over 132 steps (p. 10).

## Key quantitative results

- The experiment ran for 132 sampling steps with a 0.05 s period and a prediction horizon of six (p. 10).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Future work will address deadlock in collaborative obstacle avoidance (p. 11).

## Transfer conditions

Motion capture removes state-estimation error; the discrepancy estimator addresses model error only.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity; no other version is in the library.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 10, Sec. V.** "Experiment: The platform consists of a motion capture system, a host computer, and four Qbot2 robots."
  Experimental conditions.
- **p. 11, Sec. VI.** "Future work will address the deadlock problem that can arise during obstacle avoidance in collaborative multi-robot trajectory generation."
  Author-stated limit.

## Survey-usable statements

### Supported

- Online model-discrepancy compensation can be combined with barrier constraints in team MPC.

### Not supported

- Robustness to estimation error or communication delay is not tested.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 8, 10, 11; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

This article investigates the collaborative trajectory generation problem for nonholonomic multi-robot systems using a compensation-based nonlinear model predictive control (MPC), where the system is subject to unknown uncertainties. A dynamic uncertainty estimator is designed for each robot to estimate the discrepancy between the predictive model and the actual system, enabling adaptive model corrections that enhance the robustness and adaptability of the MPC. By incorporating control Barrier function constraints, physical constraints, and stability constraints, the nonlinear MPC generates feasible, collision-free trajectories. These trajectories are further optimized using piecewise Bézier curves, yielding smoother and more efficient paths. Additionally, a dynamic safety-stability gain is introduced, allowing the MPC to adaptively balance safety and stability based on the system state and obstacle positions. The theoretical results are validated through simulations and experiments, demonstrating the effectiveness of the proposed approach.
