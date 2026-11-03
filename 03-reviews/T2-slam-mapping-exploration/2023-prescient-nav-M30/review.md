# Prescient Collision-Free Navigation of Mobile Robots With Iterative Multimodal Motion Prediction of Dynamic Obstacles

## Metadata

| Field | Value |
|---|---|
| ID | M30 |
| Title | Prescient Collision-Free Navigation of Mobile Robots With Iterative Multimodal Motion Prediction of Dynamic Obstacles |
| Authors | Ze Zhang, Hadi Hajieghrary, Emmanuel Dean, and Knut Åkesson |
| Venue | IEEE Robotics and Automation Letters, vol. 8, no. 9, pp. 5488-5495 |
| Year | 2023 |
| Type | journal |
| DOI | [10.1109/lra.2023.3296333](https://doi.org/10.1109/lra.2023.3296333) |
| Official URL | https://ieeexplore.ieee.org/document/10185133/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2023-prescient-nav-M30/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2023-prescient-nav-M30/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2023-prescient-nav-M30/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: simulation
- evidence_all: simulation
- protocol_caveats: scripted-scenario
- platform_class: wheeled-unspecified
- platform: simulated Mobile Industrial Robot MiR100 in Gazebo (no drive type found in the text)
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: none modeled; the occupancy grid map is given and sensor measurement is out of scope
- compute: NVIDIA GTX 1650 Max-Q, about 0.3 s prediction per object; Intel i7-9750H, MPC about 0.05 s with a 0.5 s timeout
- compute_location: desktop-offline
- summary_result: Over 100 stochastic simulated warehouse runs, MPC-WTA* reached 95% success in scenario 1 (Table I); in Gazebo, TEB solved in 0.726 s versus 0.412 s.
- summary_limitation: The authors leave physical evaluation on a robot fleet, faster prediction and MPC convergence, and handling of vision-system delay to future work.
- survey_included: yes
- verification_level: light

## Problem

The paper addresses proactive collision-free navigation among pedestrians
with stochastic behavior in warehouse and factory aisles. Passive
stop-or-detour behavior of automated guided vehicles and local planners such
as DWA or TEB do not feed multimodal forecasts of human motion into the
control loop.

## Mechanism

A deep network trained with EWTA, AWTA, and SWTA losses on simulated
warehouse trajectories outputs multimodal motion predictions (MMPs) of each
dynamic obstacle on an occupancy grid. The prediction is repeated for each
future time offset. A nonlinear model predictive control (MPC) solver
(OpEn/PANOC) tracks a reference path under hard and soft constraints from
static geometry and inflated multimodal human hypotheses. The pipeline is
implemented in Python and ROS, and the occupancy map is assumed given. Three
modeling assumptions separate the prediction-control integration from full
perception.

## Baselines and controls

The comparators are MPC with constant-velocity prediction (MPC-CV), DWA, and
DWA with constant-velocity prediction (DWA-CV). In the ROS/Gazebo test, the
comparator is TEB, with its prediction horizon adjusted to match clearance
and smoothness.

## Platform and setup

All evaluation is in simulation. Two warehouse scenarios (an intersection
approach, and a parallel walk followed by a sudden turn) were run 100 times
each with stochastic simulated pedestrians. A Gazebo and RViz evaluation used
a simulated MiR100 against TEB. No physical robot trial is reported.

## Evidence type and transfer

All results are simulation. The paper's "real-world simulation" is a
ROS/Gazebo test, not a hardware trial. The pedestrian scenarios are designed
by the authors. Timing comes from a laptop GPU and CPU.

## Sensors

No sensor is modeled. The authors place sensor measurement out of scope and
assume a given occupancy map and obstacle observations from a vision
system.

## Compute and latency

Prediction takes about 0.3 s per object on an NVIDIA GTX 1650 Max-Q, and the
deep-learning inference is not optimized. MPC takes about 0.05 s when idle,
with a timeout of up to 0.5 s, on an Intel i7-9750H. In Gazebo, TEB averaged
0.726 s per solve versus 0.412 s for the method.

## Key quantitative results

- MPC-WTA* success rate in scenario 1: 95%, average over 100 runs (Table I).
- Evaluation protocol: two warehouse scenarios, 100 runs each (p. 6).
- Prediction inference: about 0.3 s per object on GTX 1650 Max-Q (p. 7).
- MPC solve time: about 0.05 s when idle (p. 7); timeout up to 0.5 s (p. 6).
- Gazebo test, average solving time: method 0.412 s versus TEB 0.726 s (p. 7).

## Stated limitations

- The deep-learning prediction is not optimized and runs on a low-performance GPU; in practice the number of predicted objects should be limited (p. 7).
- When the penalty method reaches the maximum solving time, a feasible solution is not guaranteed; a monitor on the loss function and a local sensor or brake system are proposed for a physical implementation (p. 7).
- Future work: faster and more accurate prediction networks, faster MPC convergence, handling of the always present vision delay, and evaluation in a physical scenario with a fleet of mobile robots (p. 8).

## Transfer conditions

The approach assumes a given occupancy map and obstacle observations; the
perception and delay of a real vision system are not modeled. Prediction
cost grows per object, and solver timeouts need a safety fallback on a real
robot. The TEB comparison is a Gazebo/ROS test, not a pedestrian field
trial.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. VI-C, p. 7 | "However, when the robot encounters highly dynamic obstacles such as humans, the TEB method lacks agility in responding to changes in the obstacle" |
| C3 | direct-support | moderate | Sec. VI-B, p. 7 | "On NVIDIA GTX 1650 Max-Q, the inference time is about 0.3 seconds per object." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VII, p. 8 | "Finally, we plan to evaluate the approach in a physical scenario for a fleet of mobile robots." |

## Page-cited excerpts

- **p. 7, Sec. VI-C.** "However, when the robot encounters highly dynamic obstacles such as humans, the TEB method lacks agility in responding to changes in the obstacle"
  Highly dynamic humans limit the TEB comparator in the ROS warehouse test.
- **p. 7, Sec. VI-B.** "On NVIDIA GTX 1650 Max-Q, the inference time is about 0.3 seconds per object."
  Learned prediction is compute-bound per object.
- **p. 8, Sec. VII.** "Finally, we plan to evaluate the approach in a physical scenario for a fleet of mobile robots."
  No physical evaluation is reported.
- **p. 8, Sec. VII.** "The approach is shown to outperform other non-deep-learning approaches and is also evaluated in Python using ROS under warehouse scenes and shows feasibility and safety."
  The authors' summary of the evidence: comparisons against non-deep-learning methods in simulation.

## Survey-usable statements

### Supported

- Coupling multimodal pedestrian motion prediction with nonlinear MPC reached 95% success in a simulated warehouse intersection scenario over 100 stochastic runs (numbers from a light review; re-check before citing).
- Learned multimodal prediction cost about 0.3 s per object on a laptop GPU, which limits the number of predicted obstacles.

### Not supported

- The approach was validated on a physical robot: all results are simulation, and physical tests are future work.
- The approach handles perception delay: vision delay is not modeled and is listed as future work.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); the legacy card had no verbatim quotes, so excerpts were taken from the conclusion and from Sec. VI sentences located with --find; reviewer remarks moved from Stated limitations to Evidence type and Transfer conditions
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

To explore safe interactions between a mobile robot and dynamic obstacles, this letter presents a comprehensive approach to collision-free navigation in dynamic indoor environments. The approach integrates Multimodal Motion Predictions (MMPs) of dynamic obstacles with predictive control for obstacle avoidance. MMP is achieved by a deep-learning method that predicts multiple plausible future positions. By repeating the MMP for each time offset in the future, multi-time-step MMPs are obtained. A nonlinear Model Predictive Control (MPC) solver uses the prediction outcomes to achieve collision-free trajectory tracking for the mobile robot. The proposed integration of multimodal motion prediction and trajectory tracking outperforms other non-deep-learning methods in complex scenarios. The approach enables safe interaction between the mobile robot and stochastic dynamic obstacles.
