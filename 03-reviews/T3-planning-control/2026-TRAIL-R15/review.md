# Off-Road Navigation via Implicit Neural Representation of Terrain Traversability

## Metadata

| Field | Value |
|---|---|
| ID | R15 |
| Title | Off-Road Navigation via Implicit Neural Representation of Terrain Traversability |
| Authors | Yixuan Jia, Qingyuan Li, and Jonathan P. How |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3685928](https://doi.org/10.1109/lra.2026.3685928) |
| Official URL | https://ieeexplore.ieee.org/document/11488492/ |
| Theme folder | T3-planning-control |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2026-TRAIL-R15/paper.pdf` and `02-fulltext/T3-planning-control/2026-TRAIL-R15/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2026-TRAIL-R15/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: skid-steer
- platform: AgileX Scout Mini with ZED 2i and Ouster OS1-32 in forest and grassland; training data from a Clearpath Husky A300 (p. 6).
- boundary_platform: no
- degradation: terrain
- degradation_observed: wheel-slip
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: RGB camera and LiDAR
- compute: RTX 4090 workstation for timing (p. 4); onboard hardware compute not inspected.
- compute_location: not-reported
- summary_result: An implicit terrain representation with gradient-based path and speed optimization succeeds in vegetation and geometric-obstacle cases where geometric and learned baselines fail (pp. 6-7).
- summary_limitation: Sensor occlusion and field-of-view limits are the main failure mode (p. 7).
- survey_included: yes
- verification_level: light

## Problem

Short-horizon samplers cannot reason over full path geometry or adapt speed to terrain-induced vibration.

## Mechanism

An implicit neural representation fuses RGB and LiDAR into continuous terrain attributes and vibration-related costs; its spatial gradients drive trajectory optimization of path geometry and speed (pp. 2-4).

## Baselines and controls

MPPI with geometric costs and WayFASTER on hardware; additional simulation-only baselines (pp. 4-6).

## Platform and setup

Simulation and short- and long-path field experiments; the training platform differs from the deployment platform (pp. 4-7). AgileX Scout Mini with ZED 2i and Ouster OS1-32 in forest and grassland; training data from a Clearpath Husky A300 (p. 6).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop field trials; interventions are counted, and five were caused by traction loss on wet ground (p. 7).

## Sensors

RGB camera and LiDAR.

## Compute and latency

RTX 4090 workstation for timing (p. 4); onboard hardware compute not inspected.

## Key quantitative results

- Five interventions were attributed to limited traction on wet ground with stock tires (p. 7).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Sensor occlusion and field-of-view limitations are a main failure mode; temporal fusion is future work (p. 7).

## Transfer conditions

Learned vibration costs reflect the training platform; deployment on a lighter robot introduces mass and vibration shift.

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

- **p. 6, Sec. V.** "Training on Husky data and deploying on Scout Mini thus introduces a platform distribution shift (e.g., mass and vibration scale), providing an additional generalizability test."
  Cross-platform transfer condition.
- **p. 7, Sec. V-C.** "After conducting more tests in the area, we observed that sensor occlusion and field-of-view limitations are a main failure mode of TRAIL."
  Author-stated failure mode.

## Survey-usable statements

### Supported

- Continuous traversability gradients can jointly optimize route and speed in executed off-road navigation.

### Not supported

- Traction loss is not modeled by the terrain representation.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 6, 7; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Autonomous off-road navigation requires robots to estimate terrain traversability from onboard sensors and plan motion accordingly. Conventional approaches typically rely on sampling-based planners such as MPPI to generate short-term control actions that aim to minimize traversal time and risk measures derived from the traversability estimates. These planners can react quickly but optimize only over a short look-ahead window, limiting their ability to reason about the full path geometry, which is important for navigating in challenging off-road environments. Moreover, they lack the ability to adjust speed based on the terrain-induced vibrations, which is important for smooth navigation on challenging terrains. In this letter, we introduce TRAIL (Traversability with an Implicit Learned Representation), an off-road navigation framework that leverages an implicit neural representation to model terrain properties as a continuous field that can be queried at arbitrary locations. This representation yields spatial gradients that enable integration with a novel gradient-based trajectory optimization method that adapts the path geometry and speed profile based on terrain traversability.
