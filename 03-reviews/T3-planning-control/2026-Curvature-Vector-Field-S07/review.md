# Curvature-Constrained Vector Field for Motion Planning of Nonholonomic Robots

## Metadata

| Field | Value |
|---|---|
| ID | S07 |
| Title | Curvature-Constrained Vector Field for Motion Planning of Nonholonomic Robots |
| Authors | Qiao, Yike and He, Xiaodong and Zhuo, An and Sun, Zhiyong and Bao, Weimin and Li, Zhongkui |
| Venue | IEEE Transactions on Robotics |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tro.2025.3644358](https://doi.org/10.1109/tro.2025.3644358) |
| Official URL | https://ieeexplore.ieee.org/document/11300826/ |
| Theme folder | T3-planning-control |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2026-Curvature-Vector-Field-S07/paper.pdf` and `02-fulltext/T3-planning-control/2026-Curvature-Vector-Field-S07/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2026-Curvature-Vector-Field-S07/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation, numerical
- protocol_caveats: motion-capture-pose, offboard-compute
- platform_class: ackermann
- platform: Physical Ackermann UGV under motion capture and ground-station control; fixed-wing evidence is hardware in the loop (p. 11).
- boundary_platform: no
- degradation: actuator-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: External FZMotion pose feedback in the UGV test; actuator/kinematic limits specified by the planner
- compute: Ground-station UGV planner; onboard computing claim is tested separately in fixed-wing hardware in the loop (p. 11).
- compute_location: offboard-local
- summary_result: Field/controller co-design links curvature feasibility to bounded actuation in the inspected UGV tests.
- summary_limitation: Three-dimensional field planning and curvature-constrained multi-robot motion are proposed as future work (p. 15).
- survey_included: yes
- verification_level: light

## Problem

A feasible vector field and a saturated tracking law must jointly respect nonholonomic curvature limits.

## Mechanism

Blends elementary flows into a curvature-constrained field and co-designs a saturated dynamic-gain controller converging to a target positive limit set (pp. 1, 3, 15).

## Baselines and controls

Numerical comparisons with other vector-field algorithms and two distinct implementation settings; full derivations not audited.

## Platform and setup

Physical Ackermann UGV under motion capture and ground-station control; fixed-wing evidence is hardware in the loop (p. 11).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Convergence/passage through a target set differs from stopping at an arbitrary pose. External pose and communication are part of the UGV demonstration.

## Sensors

External FZMotion pose feedback in the UGV test; actuator/kinematic limits specified by the planner.

## Compute and latency

Ground-station UGV planner; onboard computing claim is tested separately in fixed-wing hardware in the loop (p. 11).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Three-dimensional field planning and curvature-constrained multi-robot motion are proposed as future work (p. 15).

## Transfer conditions

Convergence/passage through a target set differs from stopping at an arbitrary pose. External pose and communication are part of the UGV demonstration.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 11, Selected source passage.** "the ground station executes the motion planning algorithm"
  Adds explicit kinematic feasibility to planner comparisons and prevents transferring fixed-wing HIL onboard evidence to autonomous wheeled sensing.

## Survey-usable statements

### Supported

- Field/controller co-design links curvature feasibility to bounded actuation in the inspected UGV tests. Adds explicit kinematic feasibility to planner comparisons and prevents transferring fixed-wing HIL onboard evidence to autonomous wheeled sensing.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Convergence/passage through a target set differs from stopping at an arbitrary pose. External pose and communication are part of the UGV demonstration.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 8, 11, 14, 15; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Vector fields are advantageous in handling nonholonomic motion planning, as they provide the robot with reference orientation across the workspace. However, additionally incorporating curvature constraints presents challenges due to the interconnection between the design of the curvature-bounded vector field and the tracking controller under limited actuation. In this article, we present a novel framework to co-develop the vector field and the control law, guiding the nonholonomic robot to the target configuration with curvature-bounded trajectory. First, we formulate the problem by introducing the target positive limit set, which allows the robot to either converge to or pass through the target configuration, depending on its dynamics and the specific tasks. Next, we construct a curvature-constrained vector field (CVF) via blending and embedding elementary flows in the workspace. To track such a CVF, a saturated control law with dynamic gains is proposed, under which the tracking error’s magnitude decreases even when saturation occurs. Under the control law, the kinematically constrained nonholonomic robot is guaranteed to track the reference CVF and converge to the target positive limit set with bounded trajectory curvature. Numerical simulations show that the proposed CVF method outperforms other vector-field-based algorithms. Experiments on Ackermann uncrewed ground vehicles and semimphysical fixed-wing uncrewed aerial vehicles demonstrate that the method can be effectively implemented in real-world scenarios.
