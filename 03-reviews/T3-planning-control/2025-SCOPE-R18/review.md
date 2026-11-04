# SCOPE: Stochastic Cartographic Occupancy Prediction Engine for Uncertainty-Aware Dynamic Navigation

## Metadata

| Field | Value |
|---|---|
| ID | R18 |
| Title | SCOPE: Stochastic Cartographic Occupancy Prediction Engine for Uncertainty-Aware Dynamic Navigation |
| Authors | Zhanteng Xie, and Philip Dames |
| Venue | IEEE Transactions on Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3578234](https://doi.org/10.1109/tro.2025.3578234) |
| Official URL | https://ieeexplore.ieee.org/document/11029153/ |
| Theme folder | T3-planning-control |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2025-SCOPE-R18/paper.pdf` and `02-fulltext/T3-planning-control/2025-SCOPE-R18/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2025-SCOPE-R18/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation, dataset-playback
- protocol_caveats: video-only-hardware
- platform_class: wheeled-unspecified
- platform: Gazebo TurtleBot2 training data, SCAND Jackal and Spot recordings for prediction tests, and a hardware robot in a hallway (pp. 9, 17).
- boundary_platform: no
- degradation: dynamic-objects, compute-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: 2D LiDAR occupancy grids, odometry and AMCL localization
- compute: Embedded inference evaluated on resource-constrained devices; SO-SCOPE up to 89 times faster with eight times less memory (p. 1).
- compute_location: onboard
- summary_result: Stochastic occupancy prediction integrated into costmap navigation improves safe navigation of DWA and DRL-VO policies; distillation makes inference real time on embedded hardware (pp. 1, 15-17).
- summary_limitation: Prediction fails when the robot moves erratically or rotates rapidly under the constant-velocity motion model (p. 12).
- survey_included: yes
- verification_level: light

## Problem

Deterministic occupancy prediction ignores robot, object and static-structure motion and its uncertainty.

## Mechanism

VAE-based predictors condition on robot motion, dynamic objects and a local static map; knowledge distillation and uncertainty quantification yield SO-SCOPE; predicted means and uncertainty enter a costmap for existing planners (pp. 4-8, 15).

## Baselines and controls

Fourteen OGM predictors and model- and learning-based navigation policies with and without prediction (pp. 9-17).

## Platform and setup

Training on simulated data, cross-robot prediction tests on SCAND and simulated and hardware navigation (pp. 9-17). Gazebo TurtleBot2 training data, SCAND Jackal and Spot recordings for prediction tests, and a hardware robot in a hallway (pp. 9, 17).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Hardware runs are demonstrations with AMCL in known maps; quantitative navigation comparisons are mainly simulated.

## Sensors

2D LiDAR occupancy grids, odometry and AMCL localization.

## Compute and latency

Embedded inference evaluated on resource-constrained devices; SO-SCOPE up to 89 times faster with eight times less memory (p. 1).

## Key quantitative results

- The hardware DWA/SCOPE/PU run traveled 76.10 m at 0.42 m/s average speed among walking students (p. 17).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The constant-velocity robot motion model fails when the robot suddenly rotates (p. 12).

## Transfer conditions

Assumes accurate short-term odometry and a 2.5D world; localization uses AMCL in known maps.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

The authors describe this article as an evolution of their earlier SOGMP work (pp. 1-2); that work is not in the library, and this journal article is counted once.

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

- **p. 4, Sec. III-A.** "As the robot moves, we assume that it can obtain accurate estimates of its relative pose and velocity from odometry sensors or other localization algorithms in a short period of time (on the order of 1 s)."
  Pose assumption of the predictor.
- **p. 12, Sec. V-C.** "The first failure case is when the robot moves erratically or rotates rapidly and the robot motion compensation is inaccurate, as shown in Fig. 6(a)."
  Author-stated failure case.

## Survey-usable statements

### Supported

- Predicted occupancy uncertainty can be inserted into existing costmap planners at embedded rates.

### Not supported

- Hardware results do not quantify collision reduction.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 4, 6, 9, 12, 15, 17; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

This article presents a family of Stochastic Cartographic Occupancy Prediction Engines that enable mobile robots to predict the future states of complex dynamic environments. They do this by accounting for the motion of the robot itself, the motion of dynamic objects, and the geometry of static objects in the scene, and they generate a range of possible future states of the environment. These prediction engines are software-optimized for real-time performance for navigation in crowded dynamic scenes, achieving up to 89 times faster inference speed and 8 times less memory usage than other state-of-the-art engines. Three simulated and real-world datasets collected by different robot models are used to demonstrate that these proposed prediction algorithms are able to achieve more accurate and robust stochastic prediction performance than other algorithms. Furthermore, a series of simulation and hardware navigation experiments demonstrate that the proposed predictive uncertainty-aware navigation framework with these stochastic prediction engines is able to improve the safe navigation performance of current state-of-the-art model- and learning-based control policies.
