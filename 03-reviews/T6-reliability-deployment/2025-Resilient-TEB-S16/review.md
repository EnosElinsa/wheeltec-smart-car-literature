# Resilient Timed Elastic Band Planner for Collision‐Free Navigation in Unknown Environments

## Metadata

| Field | Value |
|---|---|
| ID | S16 |
| Title | Resilient Timed Elastic Band Planner for Collision‐Free Navigation in Unknown Environments |
| Authors | Kulathunga, Geesara and Yilmaz, Abdurrahman and Huang, Zhuoling and Hroob, Ibrahim and Arunachalam, Hariharan and Guevara, Leonardo and Klimchik, Alexandr and Cielniak, Grzegorz and Hanheide, Marc |
| Venue | Journal of Field Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1002/rob.22602](https://doi.org/10.1002/rob.22602) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.22602 |
| Theme folder | T6-reliability-deployment |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-Resilient-TEB-S16/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Resilient-TEB-S16/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-Resilient-TEB-S16/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Agilex Hunter2.0 at a strawberry farm and matched Gazebo environment; no drive-type audit retained (p. 9).
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Trimble RTK-GPS and local point clouds with ground removal/spatiotemporal voxel mapping
- compute: Onboard NUC i7-10710U, C++ ROS2 navigation plugins (p. 9).
- compute_location: onboard
- summary_result: A planner fallback changes the feasible initialization before local refinement.
- summary_limitation: Broader ROS2 comparisons and integration with fixed-horizon NMPC remain future work (p. 14).
- survey_included: yes
- verification_level: light

## Problem

A local trajectory optimizer can become infeasible as obstacles invalidate its initial path.

## Mechanism

RTEB invokes hybrid A* for a feasible reinitialization, soft-constraint smoothing and Voronoi obstacle treatment within the ROS2 stack (pp. 4, 6, 8).

## Baselines and controls

TEB and NMPC in the same ROS2 stack; wider recent baselines omitted because implementations were unavailable (pp. 9, 14).

## Platform and setup

Agilex Hunter2.0 at a strawberry farm and matched Gazebo environment; no drive-type audit retained (p. 9).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Recovery addresses planner infeasibility with reliable localization/mapping inputs; it does not repair arbitrary sensor or actuator failures.

## Sensors

Trimble RTK-GPS and local point clouds with ground removal/spatiotemporal voxel mapping.

## Compute and latency

Onboard NUC i7-10710U, C++ ROS2 navigation plugins (p. 9).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Broader ROS2 comparisons and integration with fixed-horizon NMPC remain future work (p. 14).

## Transfer conditions

Recovery addresses planner infeasibility with reliable localization/mapping inputs; it does not repair arbitrary sensor or actuator failures.

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

- **p. 13, Selected source passage.** "a hybrid A* algorithm to re-initialize the TEB planner when it encounters failure situations."
  Provides a concrete trigger-to-replanning recovery chain and a comparison-availability caveat.

## Survey-usable statements

### Supported

- A planner fallback changes the feasible initialization before local refinement. Provides a concrete trigger-to-replanning recovery chain and a comparison-availability caveat.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Recovery addresses planner infeasibility with reliable localization/mapping inputs; it does not repair arbitrary sensor or actuator failures.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 6, 8, 9, 13, 14; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

In autonomous navigation, trajectory replanning, refinement, and control command generation are essential for effective motion planning. This paper presents a resilient approach to trajectory replanning addressing scenarios where the initial planner’s solution becomes infeasible. The proposed method incorporates a hybrid A* algorithm to generate feasible trajectories when the primary planner fails and applies a soft constraints-based smoothing technique to refine these trajectories, ensuring continuity, obstacle avoidance, and kinematic feasibility. Obstacle constraints are modeled using a dynamic Voronoi map to improve navigation through narrow passages. This approach enhances the consistency of trajectory planning, speeds up convergence, and meets real-time computational requirements. In environments with around 30% or higher obstacle density, the ratio of free space before and after placing new obstacles, the RESILIENT TIMED ELASTIC BAND (RTEB) planner achieves approximately 20% reduction in traverse distance, traverse time, and control effort compared to the timed elastic band (TEB) planner and nonlinear model predictive control (NMPC) planner. These improvements demonstrate the RTEB planner’s potential for application in field robotics, particularly in agricultural and industrial environments, where efficient and resilient navigation is crucial.
