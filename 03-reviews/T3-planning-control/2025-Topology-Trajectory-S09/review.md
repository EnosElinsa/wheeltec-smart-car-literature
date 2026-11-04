# Topology-Driven Parallel Trajectory Optimization in Dynamic Environments

## Metadata

| Field | Value |
|---|---|
| ID | S09 |
| Title | Topology-Driven Parallel Trajectory Optimization in Dynamic Environments |
| Authors | de Groot, Oscar and Ferranti, Laura and Gavrila, Dariu M. and Alonso-Mora, Javier |
| Venue | IEEE Transactions on Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2024.3475047](https://doi.org/10.1109/tro.2024.3475047) |
| Official URL | https://ieeexplore.ieee.org/document/10706022/ |
| Theme folder | T3-planning-control |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2025-Topology-Trajectory-S09/paper.pdf` and `02-fulltext/T3-planning-control/2025-Topology-Trajectory-S09/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2025-Topology-Trajectory-S09/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: motion-capture-pose
- platform_class: wheeled-unspecified
- platform: Mobile robot among pedestrians with motion-capture robot/pedestrian positions; social-force simulation is a separate setting (pp. 9, 12).
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: External robot and pedestrian poses; Kalman filtering and constant-velocity pedestrian predictions
- compute: Parallel receding-horizon local optimizers; experimental computation placement not retained from selected passages.
- compute_location: not-reported
- summary_result: Explicit alternative maneuver classes improve planning consistency under the inspected dynamic-obstacle protocols.
- summary_limitation: Human-robot interaction modeling and multimodal/non-Gaussian obstacle-motion uncertainty remain open (p. 15).
- survey_included: yes
- verification_level: light

## Problem

A single nonconvex trajectory optimizer can switch inefficiently among competing evasive maneuvers.

## Mechanism

Generates distinct homotopy guidance classes, optimizes class-constrained trajectories in parallel, and executes the lowest-cost feasible trajectory (pp. 1, 3).

## Baselines and controls

Local model-predictive contouring control and shared random pedestrian starts/goals in simulation; hardware uses external tracked states (pp. 9, 12).

## Platform and setup

Mobile robot among pedestrians with motion-capture robot/pedestrian positions; social-force simulation is a separate setting (pp. 9, 12).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Topology diversity does not compensate for missing or inaccurate obstacle predictions. Inspect perception, candidate feasibility and compute deadlines separately.

## Sensors

External robot and pedestrian poses; Kalman filtering and constant-velocity pedestrian predictions.

## Compute and latency

Parallel receding-horizon local optimizers; experimental computation placement not retained from selected passages.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Human-robot interaction modeling and multimodal/non-Gaussian obstacle-motion uncertainty remain open (p. 15).

## Transfer conditions

Topology diversity does not compensate for missing or inaccurate obstacle predictions. Inspect perception, candidate feasibility and compute deadlines separately.

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

- **p. 15, Selected source passage.** "One of the remaining limitations of the framework is the lack of interaction between the humans and the robot."
  Adds a parallel candidate-generation mechanism to compare with reactive barriers and learned semantic trajectory selection.

## Survey-usable statements

### Supported

- Explicit alternative maneuver classes improve planning consistency under the inspected dynamic-obstacle protocols. Adds a parallel candidate-generation mechanism to compare with reactive barriers and learned semantic trajectory selection.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Topology diversity does not compensate for missing or inaccurate obstacle predictions. Inspect perception, candidate feasibility and compute deadlines separately.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 9, 12, 13, 15; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Ground robots navigating in complex, dynamic environments must compute collision-free trajectories to avoid obstacles safely and efficiently. Nonconvex optimization is a popular method to compute a trajectory in real time. However, these methods often converge to locally optimal solutions and frequently switch between different local minima, leading to inefficient and unsafe robot motion. In this work, we propose a novel topology-driven trajectory optimization strategy for dynamic environments that plans multiple distinct evasive trajectories to enhance the robot's behavior and efficiency. A global planner iteratively generates trajectories in distinct homotopy classes. These trajectories are then optimized by local planners working in parallel. While each planner shares the same navigation objectives, they are locally constrained to a specific homotopy class, meaning each local planner attempts a different evasive maneuver. The robot then executes the feasible trajectory with the lowest cost in a receding horizon manner. We demonstrate on a mobile robot navigating among pedestrians that our approach leads to faster trajectories than existing planners.
