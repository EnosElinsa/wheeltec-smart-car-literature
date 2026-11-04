# A cooperative approach to Range-Only SLAM with undelayed initialization

## Metadata

| Field | Value |
|---|---|
| ID | S27 |
| Title | A cooperative approach to Range-Only SLAM with undelayed initialization |
| Authors | Lorenzo Bianchi and Francesco Martinelli |
| Venue | Robotics and Autonomous Systems |
| Year | 2026 |
| Type | journal |
| DOI | [10.1016/j.robot.2025.105230](https://doi.org/10.1016/j.robot.2025.105230) |
| Official URL | https://www.sciencedirect.com/science/article/pii/S0921889025003276 |
| Theme folder | T4-multi-robot-coordination |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Range-Only-SLAM-S27/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Range-Only-SLAM-S27/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Range-Only-SLAM-S27/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, numerical
- protocol_caveats: joystick-driving
- platform_class: differential-drive
- platform: Three TurtleBot3 Burger robots with several UWB meshes; joystick collection and offline bag analysis (p. 10).
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: Wheel odometry and inter-robot/robot-landmark UWB ranges; measured distances establish a separate reference
- compute: Jetson Nano acquires ROS 2 bags; the evaluated algorithm runs offline and uses centralized information sharing (pp. 10, 14).
- compute_location: desktop-offline
- summary_result: Cooperative ranges reduce ambiguity in the inspected planar initialization tests.
- summary_limitation: Centralized hypotheses enlarge the initial state and slow initialization; large teams are not recommended (p. 14).
- survey_included: yes
- verification_level: light

## Problem

Range-only localization must initialize unknown robot and landmark positions without angular measurements.

## Mechanism

Multi-hypothesis federated EKF initializes immediately and shares cooperative range information in a centralized state (pp. 1-2, 14).

## Baselines and controls

Independent versus cooperative estimation and known-correct-hypothesis simulation controls (pp. 10-11).

## Platform and setup

Three TurtleBot3 Burger robots with several UWB meshes; joystick collection and offline bag analysis (p. 10).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. All robots/landmarks remain visible; sensors must share a height. Offline estimation cannot substantiate onboard closed-loop navigation.

## Sensors

Wheel odometry and inter-robot/robot-landmark UWB ranges; measured distances establish a separate reference.

## Compute and latency

Jetson Nano acquires ROS 2 bags; the evaluated algorithm runs offline and uses centralized information sharing (pp. 10, 14).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Centralized hypotheses enlarge the initial state and slow initialization; large teams are not recommended (p. 14).

## Transfer conditions

All robots/landmarks remain visible; sensors must share a height. Offline estimation cannot substantiate onboard closed-loop navigation.

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

- **p. 10, Selected source passage.** "Lastly, the bags are analyzed, and the algorithm is executed offline."
  Separates radio-based geometric initialization from communication resilience and exposes the visibility/scaling assumptions.

## Survey-usable statements

### Supported

- Cooperative ranges reduce ambiguity in the inspected planar initialization tests. Separates radio-based geometric initialization from communication resilience and exposes the visibility/scaling assumptions.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. All robots/landmarks remain visible; sensors must share a height. Offline estimation cannot substantiate onboard closed-loop navigation.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 2, 10, 11, 14; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

A 2D cooperative Range-Only SLAM problem is considered in this paper. In addition to odometry, available through noisy encoder readings on the actuated wheels, the robots measure the distances to a set of landmarks in unknown positions within the environment, as well as to other robots. Inter-landmark distances are not assumed to be available. The robots start at unknown locations, with their relative positions also assumed unknown. A Multi-Hypotheses Extended Kalman Filter, endowed with a Federated Information Sharing mechanism, is proposed to solve the problem in a computationally efficient way, without any delay in the initialization of landmark and robot position estimates. Simulation and experimental results are reported in the paper to demonstrate the effectiveness of the proposed approach, showing significant improvements in both steady-state and transient performance compared to the single-robot scenario.
