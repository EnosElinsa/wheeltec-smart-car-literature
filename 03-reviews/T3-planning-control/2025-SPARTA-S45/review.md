# Learning Smooth State-Dependent Traversability from Dense Point Clouds

## Metadata

| Field | Value |
|---|---|
| ID | S45 |
| Title | Learning Smooth State-Dependent Traversability from Dense Point Clouds |
| Authors | Dong, Zihao and Papalia, Alan and Jung, Leonard and Spiro, Alenna and Osteen, Philip R and Robison, Christa S. and Everett, Michael |
| Venue | Conference on Robot Learning |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v305/dong25a.html |
| Theme folder | T3-planning-control |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2025-SPARTA-S45/paper.pdf` and `02-fulltext/T3-planning-control/2025-SPARTA-S45/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2025-SPARTA-S45/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials, simulated-agents-on-hardware
- platform_class: skid-steer
- platform: BeamNG.tech tire-deformation training/planning and a Scout Mini skid-steer demonstration; one risky alternative is virtual in the hardware course (pp. 6, 8, 16).
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Dense prior point clouds; Ouster LiDAR/IMU and DLIO for map construction and online pose
- compute: Onboard ROG NUC with Intel Core Ultra 9 and RTX 4070 for the physical demonstration (p. 16).
- compute_location: onboard
- summary_result: Angle-conditioned risk changes route/speed selection without rerunning the network for each approach-angle query.
- summary_limitation: Assumes a prebuilt fully observed point-cloud map; tire deformation is available only in simulation, and geometry-only smoothness assumptions have limits (p. 9).
- survey_included: yes
- verification_level: light

## Problem

The same obstacle has different traversal consequences at different approach angles.

## Mechanism

Predicts reusable Fourier functions on the angle circle for categorical risk-distribution parameters and queries tail risk during planning (p. 3).

## Baselines and controls

Angle-input/angle-free models and elevation costs; simulation tire deformation is a surrogate, while hardware tests compare route choices with a virtual risky alternative (pp. 6, 8).

## Platform and setup

BeamNG.tech tire-deformation training/planning and a Scout Mini skid-steer demonstration; one risky alternative is virtual in the hardware course (pp. 6, 8, 16).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. A virtual risky branch supports route selection, not measured physical damage reduction. Separate simulated tire-risk outcomes from hardware branch-choice evidence.

## Sensors

Dense prior point clouds; Ouster LiDAR/IMU and DLIO for map construction and online pose.

## Compute and latency

Onboard ROG NUC with Intel Core Ultra 9 and RTX 4070 for the physical demonstration (p. 16).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Assumes a prebuilt fully observed point-cloud map; tire deformation is available only in simulation, and geometry-only smoothness assumptions have limits (p. 9).

## Transfer conditions

A virtual risky branch supports route selection, not measured physical damage reduction. Separate simulated tire-risk outcomes from hardware branch-choice evidence.

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

- **p. 9, Selected source passage.** "we assume the environment is fully observable, i.e. a prebuilt point cloud map is accessible during planning."
  Requires the terrain challenge to acknowledge direction-dependent learned traversability and focus on uncertain state, incomplete maps and physical consequence validation.

## Survey-usable statements

### Supported

- Angle-conditioned risk changes route/speed selection without rerunning the network for each approach-angle query. Requires the terrain challenge to acknowledge direction-dependent learned traversability and focus on uncertain state, incomplete maps and physical consequence validation.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. A virtual risky branch supports route selection, not measured physical damage reduction. Separate simulated tire-risk outcomes from hardware branch-choice evidence.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 6, 8, 9, 16; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

A key open challenge in off-road autonomy is that the traversability of terrain often depends on the vehicle’s state. In particular, some obstacles are only traversable from some orientations. However, learning this interaction by encoding the angle of approach as a model input demands a large and diverse training dataset and is computationally inefficient during planning due to repeated model inference. To address these challenges, we present SPARTA, a method for estimating approach angle conditioned traversability from point clouds. Specifically, we impose geometric structure into our network by outputting a smooth analytical function over the 1-Sphere that predicts risk distribution for any angle of approach with minimal overhead and can be reused for subsequent queries. The function is composed of Fourier basis functions, which has important advantages for generalization due to their periodic nature and smoothness. We demonstrate SPARTA both in a high-fidelity simulation platform, where our model achieves a 91% success rate crossing a 40m boulder field (compared to 73% for the baseline), and on hardware, illustrating the generalization ability of the model to real-world settings. Our code will be available at https://github.com/neu-autonomy/SPARTA.
