# HEIGHT: Heterogeneous Interaction Graph Transformer for Robot Navigation in Crowded and Constrained Environments

## Metadata

| Field | Value |
|---|---|
| ID | R16 |
| Title | HEIGHT: Heterogeneous Interaction Graph Transformer for Robot Navigation in Crowded and Constrained Environments |
| Authors | Shuijing Liu, Haochen Xia, Fatemeh Cheraghi Pouria, Kaiwen Hong, Neeloy Chakraborty, Zichao Hu, Joydeep Biswas, and Katherine Driggs-Campbell |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2026 (DOI year 2025) |
| Type | journal |
| DOI | [10.1109/tase.2025.3646588](https://doi.org/10.1109/tase.2025.3646588) |
| Official URL | https://ieeexplore.ieee.org/document/11305122/ |
| Theme folder | T3-planning-control |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2026-HEIGHT-R16/paper.pdf` and `02-fulltext/T3-planning-control/2026-HEIGHT-R16/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2026-HEIGHT-R16/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: offboard-compute
- platform_class: differential-drive
- platform: TurtleBot 2i in hallway and lounge and a Jackal in atrium and outdoor crowds; low-fidelity simulator for training (pp. 12-13, 18).
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: 2D LiDAR or map-based obstacle points, tracked human positions, robot localization
- compute: Jetson Xavier with a remote host computer on the TurtleBot (p. 18); RTX 4090 desktop for simulation.
- compute_location: mixed
- summary_result: Heterogeneous spatio-temporal graph attention improves success and navigation time over model- and learning-based baselines and transfers zero-shot to four everyday environments (pp. 9-15).
- summary_limitation: Collisions occur when humans abruptly change goals or almost all free paths are blocked (p. 12).
- survey_included: yes
- verification_level: light

## Problem

Crowd navigation policies ignore interactions with static constraints such as corridors and furniture.

## Mechanism

Human and obstacle inputs are separated; a heterogeneous st-graph models robot-human, human-human and obstacle interactions; attention and recurrence form the DRL policy (pp. 4-7).

## Baselines and controls

ORCA, DWA-type model-based planners, DS-RNN, A* with CNN and homogeneous graph ablations (pp. 8-12).

## Platform and setup

Simulation with varying densities and real-world tests without additional training; real humans enter as relative positions only (pp. 4, 12). TurtleBot 2i in hallway and lounge and a Jackal in atrium and outdoor crowds; low-fidelity simulator for training (pp. 12-13, 18).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop hardware with offboard support; obstacle input uses a map and reliable localization.

## Sensors

2D LiDAR or map-based obstacle points, tracked human positions, robot localization.

## Compute and latency

Jetson Xavier with a remote host computer on the TurtleBot (p. 18); RTX 4090 desktop for simulation.

## Key quantitative results

- Failure analysis attributes collisions to sudden human goal changes and to extremely crowded constrained scenes (p. 12).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The robot sometimes cannot switch paths in time because of its speed limit in extremely crowded scenes (p. 12).

## Transfer conditions

Uses map-derived obstacles and reliable localization; human velocities are omitted in the real world.

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

- **p. 5, Sec. III-B.** "The second variant is more robust to occlusions, imperfect human models, and sensor noise, but assumes the availability of a map and reliable localization."
  States the localization assumption of the deployed input.
- **p. 12, Sec. V-C.** "In these cases, due to its speed limit, the robot sometimes cannot switch to an alternative path in time to prevent collisions."
  Failure condition.

## Survey-usable statements

### Supported

- A graph policy that distinguishes humans from static constraints transfers to wheeled hardware in everyday scenes.

### Not supported

- Robustness to localization failure is not tested.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 4, 5, 9, 12, 13, 15, 18; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

We study the problem of robot navigation in dense and interactive crowds with static constraints such as corridors and furniture. Previous methods fail to consider all types of spatial and temporal interactions among agents and obstacles, leading to unsafe and inefficient robot paths. In this article, we leverage a graph-based representation of crowded and constrained scenarios and propose a structured framework to learn robot navigation policies with deep reinforcement learning. We first split the representations of different inputs, and propose a heterogeneous spatio-temporal (st) graph to model distinct interactions among humans, robots, and obstacles. Based on the heterogeneous st-graph, we propose HEIGHT, a novel navigation policy network architecture with different components to capture heterogeneous interactions through space and time. HEIGHT utilizes attention mechanisms to prioritize important interactions and a recurrent network to track changes in the dynamic scene over time, encouraging the robot to avoid collisions adaptively. Through extensive simulation and real-world experiments, we demonstrate that HEIGHT outperforms state-of-the-art baselines in terms of success, navigation time, and generalization to domain shifts in challenging navigation scenarios.
