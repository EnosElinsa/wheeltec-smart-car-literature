# MonoMPC: Monocular Vision Based Navigation With Learned Collision Model and Risk-Aware Model Predictive Control

## Metadata

| Field | Value |
|---|---|
| ID | R14 |
| Title | MonoMPC: Monocular Vision Based Navigation With Learned Collision Model and Risk-Aware Model Predictive Control |
| Authors | Basant Sharma, Prajyot Jadhav, Pranjal Paul, K.Madhava Krishna, and Arun Kumar Singh |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 (DOI year 2025) |
| Type | journal |
| DOI | [10.1109/lra.2025.3641112](https://doi.org/10.1109/lra.2025.3641112) |
| Official URL | https://ieeexplore.ieee.org/document/11283048/ |
| Theme folder | T3-planning-control |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2026-MonoMPC-R14/paper.pdf` and `02-fulltext/T3-planning-control/2026-MonoMPC-R14/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2026-MonoMPC-R14/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: offboard-compute
- platform_class: skid-steer
- platform: Clearpath Jackal with RealSense D435i used as RGB-only input; quadcopter demonstrations (pp. 6-7).
- boundary_platform: no
- degradation: model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: Monocular RGB; depth estimated by a vision foundation model
- compute: RTX 3080 laptop over local network: 0.01 s planning plus 0.02 s depth; 0.065 s planning on Jetson Orin (pp. 6-7).
- compute_location: offboard-local
- summary_result: A learned clearance distribution with risk-aware MPC cuts collisions by up to seven times versus the ROS navigation stack on estimated depth (p. 7).
- summary_limitation: Lacks temporal memory, which can cause oscillation; dynamic environments are future work (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Collision checking with monocular depth estimates produces false free space and planning failures.

## Mechanism

Estimated depth conditions a learned model of the minimum-clearance distribution for a control sequence; an MMD-based risk enters a sampling-based MPC; the collision model and risk metric are co-trained on safe and unsafe trajectories (pp. 3-5).

## Baselines and controls

ROS navigation stack on estimated depth, MonoNav and NoMaD (p. 7).

## Platform and setup

Cluttered indoor hardware trials and 40 quadcopter runs (pp. 6-7). Clearpath Jackal with RealSense D435i used as RGB-only input; quadcopter demonstrations (pp. 6-7).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop hardware with offboard laptop computation; static obstacles.

## Sensors

Monocular RGB; depth estimated by a vision foundation model.

## Compute and latency

RTX 3080 laptop over local network: 0.01 s planning plus 0.02 s depth; 0.065 s planning on Jetson Orin (pp. 6-7).

## Key quantitative results

- Collisions fall by up to seven times and planning failures are eliminated relative to ROSNAV (p. 7).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The approach ignores past images or point clouds, which can cause oscillatory behavior (p. 8).
- Dynamic environments with time-varying collision models are future work (p. 8).

## Transfer conditions

Calibration of the clearance distribution is learned for the training domain and static scenes.

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

- **p. 8, Sec. V.** "A limitation of our approach is the lack of temporal memory, as it ignores past images or point-clouds."
  Author-stated limit.
- **p. 6, Sec. IV-A.** "The system ran on ROS Noetic with an NVIDIA RTX 3080 GPU laptop connected to the Jackal over a local network."
  Computation placement.

## Survey-usable statements

### Supported

- A learned clearance distribution can be used directly as a risk constraint on a wheeled robot.

### Not supported

- The collision risk is not a calibrated mission collision rate.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 3, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Navigating unknown environments with a single RGB camera is challenging, as the lack of depth information prevents reliable collision-checking. While some methods use estimated depth to build collision maps, we found that depth estimates from vision foundation models are too noisy for zero-shot navigation in cluttered environments. We propose an alternative approach: instead of using noisy estimated depth for direct collision-checking, we use it as a rich context input to a learned collision model. This model predicts the distribution of minimum obstacle clearance that the robot can expect for a given control sequence. At inference, these predictions inform a risk-aware MPC planner that minimizes estimated collision risk. We proposed a joint learning pipeline that co-trains the collision model and risk metric using both safe and unsafe trajectories. Crucially, our joint-training ensures well calibrated uncertainty in our collision model that improves navigation in highly cluttered environments. Consequently, real-world experiments show reductions in collision-rate and improvements in goal reaching and speed over several strong baselines.
