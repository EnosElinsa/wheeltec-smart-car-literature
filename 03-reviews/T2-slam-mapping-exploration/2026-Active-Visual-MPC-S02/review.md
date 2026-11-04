# Active visual SLAM using potential fields and model predictive control

## Metadata

| Field | Value |
|---|---|
| ID | S02 |
| Title | Active visual SLAM using potential fields and model predictive control |
| Authors | Alice Hierholz and Vincent Reß and Nils Hentschel and Andreas Gienger and Norbert Haala and Oliver Sawodny |
| Venue | Control Engineering Practice |
| Year | 2026 |
| Type | journal |
| DOI | [10.1016/j.conengprac.2026.106897](https://doi.org/10.1016/j.conengprac.2026.106897) |
| Official URL | https://www.sciencedirect.com/science/article/pii/S0967066126001413 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-Active-Visual-MPC-S02/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-Active-Visual-MPC-S02/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-Active-Visual-MPC-S02/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: skid-steer
- platform: Six-wheel skid-steering robot in an indoor construction-like environment; pedestrians and barrier changes are demonstrated (pp. 5, 7).
- boundary_platform: no
- degradation: dynamic-objects, scene-change
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: ZED X stereo camera and visual SLAM feeding probabilistic occupancy mapping
- compute: Jetson AGX Orin perception plus Intel i7 control computer; C++ ROS Noetic and CasADi/IPOPT MPC (p. 5).
- compute_location: onboard
- summary_result: Potential-field MPC executes exploration and responds to demonstrated environmental changes on wheeled hardware.
- summary_limitation: Residual map uncertainty, careful parameter tuning and limited comparative/repeated evaluation remain open (pp. 7-8).
- survey_included: yes
- verification_level: light

## Problem

Exploration goal selection and feasible trajectory generation can conflict when handled as separate stages.

## Mechanism

Constructs Gaussian occupied/frontier/unknown-cell potential fields from an occupancy map and optimizes nonholonomic motion with multistage MPC (pp. 3-5).

## Baselines and controls

The conclusion explicitly leaves systematic benchmarking against representative baselines and broader repeated trials for future work (pp. 7-8).

## Platform and setup

Six-wheel skid-steering robot in an indoor construction-like environment; pedestrians and barrier changes are demonstrated (pp. 5, 7).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. A demonstrated active-SLAM loop is not a calibrated pose-uncertainty-aware controller; test how potential weights alter narrow-passage feasibility.

## Sensors

ZED X stereo camera and visual SLAM feeding probabilistic occupancy mapping.

## Compute and latency

Jetson AGX Orin perception plus Intel i7 control computer; C++ ROS Noetic and CasADi/IPOPT MPC (p. 5).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Residual map uncertainty, careful parameter tuning and limited comparative/repeated evaluation remain open (pp. 7-8).

## Transfer conditions

A demonstrated active-SLAM loop is not a calibrated pose-uncertainty-aware controller; test how potential weights alter narrow-passage feasibility.

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

- **p. 7, Selected source passage.** "As the approach relies on carefully tuned parameters, future research will address their automated adjustment."
  Extends integrated exploration examples while limiting comparative claims to what the hardware demonstration establishes.

## Survey-usable statements

### Supported

- Potential-field MPC executes exploration and responds to demonstrated environmental changes on wheeled hardware. Extends integrated exploration examples while limiting comparative claims to what the hardware demonstration establishes.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. A demonstrated active-SLAM loop is not a calibrated pose-uncertainty-aware controller; test how potential weights alter narrow-passage feasibility.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 4, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Active Simultaneous Localization and Mapping (SLAM) enables robots to autonomously explore unknown environments while building a map and localizing themselves. In indoor construction sites, this capability can support efficient and safe exploration as a basis for subsequent automated construction processes. This paper presents an integrated Active Visual SLAM approach combining potential fields with Model Predictive Control (MPC). The framework builds on ORB-SLAM3, extended with a trajectory generation module that first produces a dense 2D Probabilistic Occupancy Grid Map. A behavioral exploration strategy then employs potential fields modeled as multivariate Gaussian distributions to attract the robot toward unexplored and frontier regions while repelling it from occupied areas. A discrete, nonlinear multi-stage MPC generates feasible trajectories by optimizing the robot’s trajectory over the global potential field online, ensuring compliance with specified optimization goals, and enforcing collision avoidance as well as non-holonomic constraints. Experiments with a six-wheel skid-steering robot in a test environment resembling indoor construction sites demonstrate effective exploration and robustness to dynamic changes, validating the approach in real-world scenarios.
