# EVORA: Deep Evidential Traversability Learning for Risk-Aware Off-Road Autonomy

## Metadata

| Field | Value |
|---|---|
| ID | K05 |
| Title | EVORA: Deep Evidential Traversability Learning for Risk-Aware Off-Road Autonomy |
| Authors | Xiaoyi Cai, Siddharth Ancha, Lakshay Sharma, Philip R. Osteen, Bernadette Bucher, Stephen Phillips, Jiuguang Wang, Michael Everett, Nicholas Roy, and Jonathan P. How |
| Venue | IEEE Transactions on Robotics |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/tro.2024.3431828](https://doi.org/10.1109/tro.2024.3431828) |
| Official URL | https://ieeexplore.ieee.org/document/10606099/ |
| Theme folder | T3-planning-control |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T3-planning-control/2024-EVORA-K05/paper.pdf` and `02-fulltext/T3-planning-control/2024-EVORA-K05/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2024-EVORA-K05/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, recorded-robot-data, simulation
- protocol_caveats: motion-capture-pose, few-trials
- platform_class: ackermann
- platform: 0.33 m x 0.25 m RC car commanded by speed and steering angle (bicycle model) in an indoor arena; Boston Dynamics Spot outdoors; Husky forest data build the simulation (pp. 6, 14-15).
- boundary_platform: no
- degradation: terrain, model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: RealSense D455 on the RC car with Vicon pose; RealSense D455, Ouster OS0 LiDAR and built-in odometry on Spot (p. 15)
- compute: RC car: onboard Intel Core i7 and RTX 2060, planning at 20 Hz; Spot: Jetson AGX Orin, planning at 5 Hz (pp. 15-16).
- compute_location: onboard
- summary_result: Indoors, CVaR-Dyn with alpha 0.8 gives the best time-to-goal with 100% success over 5 races; avoiding OOD terrain removed human interventions outdoors (pp. 16-17).
- summary_limitation: The pipeline relies on semantic segmentation, and the risk from perception uncertainty must be addressed separately (p. 18).
- survey_included: yes
- verification_level: light

## Problem

Learned traversability costs carry aleatoric uncertainty (terrain that looks alike behaves differently) and epistemic uncertainty (terrain unlike the training data). EVORA quantifies both and plans against them (pp. 1-2).

## Mechanism

A traction predictor outputs Dirichlet-parameterized discrete traction distributions trained with an uncertainty-aware squared Earth Mover's Distance loss, and latent-feature densities flag OOD terrain. An MPPI planner simulates trajectories with the left-tail CVaR of traction (CVaR-Dyn) and adds auxiliary costs for OOD terrain (pp. 2, 5-9).

## Baselines and controls

CVaR-Cost (worst-case expected cost), WayFAST (expected traction), and a planner that assumes nominal traction with vegetation penalties (pp. 9, 15-16).

## Platform and setup

Synthetic benchmark with 5 training, 20 test and 40 OOD environments (p. 10). Hardware: indoor races of an RC car on turf and fake trees, five races of two laps each, with Vicon pose (pp. 14-15); outdoor Spot tests with three round trips per method (p. 16).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. The indoor results rest on motion-capture pose and five races, and the outdoor results on six trials per method. OOD terrain is a designed condition with separate results, so `designed-degradation` is coded with `model-error`. The provisional module `traversability-planning-control` is confirmed. The RC car is coded `ackermann` from its steering-angle bicycle model (p. 15); wheeled evidence takes precedence over Spot.

## Sensors

RC car: RealSense D455 depth camera, with pose and velocity from Vicon. Spot: RealSense D455, Ouster OS0 LiDAR, and Spot's built-in odometry for traction labels (p. 15).

## Compute and latency

The RC car runs traction prediction, planning and elevation mapping onboard on an Intel Core i7 CPU and an RTX 2060 GPU, with planners at 20 Hz (p. 15). Spot uses a Jetson AGX Orin, and the planners reliably plan at 5 Hz (pp. 15-16). Simulations used an Intel Core i9 and an RTX 3070, with CVaR-Cost replanning at 15 Hz (p. 12).

## Key quantitative results

- Indoor races: CVaR-Dyn with alpha 0.8 achieves the best time-to-goal with 100% success over 5 trials (p. 16, Fig. 19 caption).
- Outdoor Spot: CVaR-Dyn with alpha 0.9 achieves the best time-to-goal and success rate over six trials (p. 16).
- Without OOD avoidance the robot gets stuck in local minima and needs human interventions; with it, time-to-goal improves without interventions (p. 17).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The work uses 2-D robot models; six-degree-of-freedom models are needed for more challenging terrain (p. 18).
- The pipeline relies on semantic segmentation and may fail when test environments look too different from training; the risk from perception uncertainty must be addressed separately (p. 18).
- Training requires empirical traction distributions, which may be hard to obtain for high-dimensional features (p. 18).

## Transfer conditions

Pose uncertainty does not enter the terrain decisions: indoor pose comes from Vicon, and outdoor traction labels use Spot's odometry. A wheeled robot with onboard localization must add the effect of pose error separately.

## Code and data

Code availability was not checked in this targeted reading.

## Version family

Extends a preliminary conference version that learned traction distributions and used CVaR of traction (p. 4); that version is not in the library. Counted once.

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

- **p. 15, Sec. IX-A.** "The robot runs onboard traction prediction, motion planning, and online elevation mapping with 0.1 m resolution, but Vicon is used for pose and velocity estimation."
  Indoor hardware results use motion-capture pose, so pose error does not enter the planner.
- **p. 18, Sec. X.** "Therefore, the risk due to the uncertainty in the perception modules needs to be addressed separately"
  Author-stated scope: perception uncertainty is outside the risk model.
- **p. 17, Sec. IX-B.** "In contrast, the planner that avoids OOD terrain achieves better time-to-goal without requiring human interventions."
  OOD avoidance result on the legged platform.
- **p. 15, Sec. IX-B.** "The unicycle model (2) is used for this experiment, and traction values are obtained by comparing the commanded velocities and Spot's built-in odometry."
  Outdoor traction labels depend on the robot's own odometry.

## Survey-usable statements

### Supported

- EVORA plans against traction uncertainty and OOD terrain, but it does not propagate pose uncertainty into terrain decisions.
- Avoiding OOD terrain reduced human interventions in the outdoor Spot tests.

### Not supported

- The indoor results do not show robustness to localization error, because Vicon supplies the pose.
- Five races and six outdoor trials do not establish reliability statistics.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 5, 6, 10, 12, 14, 15, 16, 17, 18; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Traversing terrain with good traction is crucial for achieving fast off-road navigation. Instead of manually designing costs based on terrain features, existing methods learn terrain properties directly from data via self-supervision to automatically penalize trajectories moving through undesirable terrain, but challenges remain in properly quantifying and mitigating the risk due to uncertainty in the learned models. To this end, we present evidential off-road autonomy (EVORA), a unified framework to learn uncertainty-aware traction model and plan risk-aware trajectories. For uncertainty quantification, we efficiently model both aleatoric and epistemic uncertainty by learning discrete traction distributions and probability densities of the traction predictor's latent features. Leveraging evidential deep learning, we parameterize Dirichlet distributions with the network outputs and propose a novel uncertainty-aware squared Earth Mover's Distance loss with a closed-form expression that improves learning accuracy and navigation performance. For risk-aware navigation, the proposed planner simulates state trajectories with the worst-case expected traction to handle aleatoric uncertainty and penalizes trajectories moving through terrain with high epistemic uncertainty. Our approach is extensively validated in simulation and on wheeled and quadruped robots, showing improved navigation performance compared to methods that assume no slip, assume the expected traction, or optimize for the worst-case expected cost.
