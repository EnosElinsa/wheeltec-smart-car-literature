# Universal Low-Complexity Safe Tracking Control and Its Application to Time-Independent Path Following of Nonholonomic Mobile Robots

## Metadata

| Field | Value |
|---|---|
| ID | S08 |
| Title | Universal Low-Complexity Safe Tracking Control and Its Application to Time-Independent Path Following of Nonholonomic Mobile Robots |
| Authors | Mu, Dianrui and Hua, Changchun and Chen, Jiannan and Li, Yafeng and Zhu, Lingchen and Liu, Fucai |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tase.2025.3586138](https://doi.org/10.1109/tase.2025.3586138) |
| Official URL | https://ieeexplore.ieee.org/document/11075828/ |
| Theme folder | T3-planning-control |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2025-Low-Complexity-Tracking-S08/paper.pdf` and `02-fulltext/T3-planning-control/2025-Low-Complexity-Tracking-S08/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2025-Low-Complexity-Tracking-S08/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, numerical
- protocol_caveats: motion-capture-pose, offboard-compute
- platform_class: wheeled-unspecified
- platform: Nonholonomic mobile robot with wheel encoders and NOKOV pose tracking; automatic and human-shared lane following (p. 9).
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: Motion-capture position/attitude and wheel encoders; no IMU/current sensor on the evaluated robot
- compute: MATLAB controller on a console connected wirelessly to the robot (p. 9).
- compute_location: offboard-local
- summary_result: The controller limits output states despite out-of-bound reference requests in the tested lane-following settings.
- summary_limitation: Multi-robot/platooning extension is left for future work; no broader author-stated limitation was retained from the selected conclusion (p. 10).
- survey_included: yes
- verification_level: light

## Problem

Planner or human references can request motion beyond a prescribed lane/state safety set.

## Mechanism

Uses constrained/shared-constrained functions in a universal tracking controller; maps lane restrictions to heading constraints for time-independent following (pp. 1-3, 6).

## Baselines and controls

Automatic and shared-control scenarios deliberately include reference commands outside the constraints (pp. 8-9).

## Platform and setup

Nonholonomic mobile robot with wheel encoders and NOKOV pose tracking; automatic and human-shared lane following (p. 9).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. A prescribed lane/state set is not a perception-derived dynamic collision model. Hardware claims depend on external pose and wireless offboard control.

## Sensors

Motion-capture position/attitude and wheel encoders; no IMU/current sensor on the evaluated robot.

## Compute and latency

MATLAB controller on a console connected wirelessly to the robot (p. 9).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Multi-robot/platooning extension is left for future work; no broader author-stated limitation was retained from the selected conclusion (p. 10).

## Transfer conditions

A prescribed lane/state set is not a perception-derived dynamic collision model. Hardware claims depend on external pose and wireless offboard control.

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

- **p. 9, Selected source passage.** "the proposed controller runs in Matlab while collecting experimental data."
  Separates reference-error accommodation from fault diagnosis and from uncertain-obstacle safety.

## Survey-usable statements

### Supported

- The controller limits output states despite out-of-bound reference requests in the tested lane-following settings. Separates reference-error accommodation from fault diagnosis and from uncertain-obstacle safety.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. A prescribed lane/state set is not a perception-derived dynamic collision model. Hardware claims depend on external pose and wireless offboard control.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 2, 3, 6, 8, 9, 10; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

The existing shared control schemes and automatic control schemes are almost designed separately. Based on the designed constrained function and shared-constrained function, this paper proposes a universal control framework for high-order strict-feedback systems that can achieve safe tracking control with very low algorithm complexity regardless of whether the reference signal exceeds safety constraints, combining the flexibility of manual operating with the persistence and security of automatic control. A universal safe tracking control theorem is presented to prove the security of system operation. Furthermore, based on the proposed universal safe tracking control method, a novel time-independent path following control method with lane constraints is proposed for nonholonomic mobile robots by converting lane constraints into heading angle constraints, thus achieving automatic/auxiliary adaptive cruise control and lane keeping. Simulation and experimental results are provided to demonstrate the practical applicability of this method.
