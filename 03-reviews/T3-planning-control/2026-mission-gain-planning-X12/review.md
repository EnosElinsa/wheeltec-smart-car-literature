# A Unified Framework for Mission-Gain-Aware Proactive Planning and Control of Autonomous Mobile Robots

## Metadata

| Field | Value |
|---|---|
| ID | X12 |
| Title | A Unified Framework for Mission-Gain-Aware Proactive Planning and Control of Autonomous Mobile Robots |
| Authors | Patrick Sherman and Nicola Bezzo |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 10, pp. 12192-12199 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3730224](https://doi.org/10.1109/lra.2026.3730224) |
| Official URL | https://doi.org/10.1109/lra.2026.3730224 |
| Theme folder | T3-planning-control |
| Batch | supplemental |
| Local files | `01-papers/T3-planning-control/2026-mission-gain-planning-X12/paper.pdf` and `02-fulltext/T3-planning-control/2026-mission-gain-planning-X12/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2026-mission-gain-planning-X12/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: multi-robot
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: motion-capture-pose, scripted-scenario
- platform_class: wheeled-unspecified
- platform: Husarion ROSbot with Bitcraze Crazyflie scout (occlusion); Clearpath Jackal with UFactory Lite6 arm (vibration)
- boundary_platform: no
- degradation: dynamic-objects, terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Intel RealSense RGB-D camera, z-axis IMU; Vicon motion capture for pose
- compute: not recorded in the legacy extraction
- compute_location: not-reported
- summary_result: Over loose debris, the payload stayed intact in 19 of 20 mission-gain runs versus 2 of 20 full-speed baseline runs, with peak acceleration falling from about 4.19 g.
- summary_limitation: No limitation is stated by the authors in the legacy extraction; lab pose came from Vicon, and the occlusion simulations ignored physical collisions.
- survey_included: yes
- verification_level: light

## Problem

In partially known environments, mission success depends jointly on robot
capability, task requirements, and environment properties.
Mutual-information exploration needs an explicit interaction model and does
not encode arbitrary mission metrics such as visibility or vibration.

## Mechanism

A pose-dependent mission-gain is mapped during a scouting phase, distilled
into a Gaussian mixture model (GMM) for transmission, and inserted as a cost
in an MPPI controller that trades goal progress against mission performance.
Map generation is decoupled from control, so a scout (often a faster UAV) can
serve a different action robot.

## Baselines and controls

In the occlusion scenario the baseline follows the shortest path; in the
vibration scenario the baseline drives at full speed. The baseline scout
follows A* to the action goal and assigns zero cost to unobserved cells.

## Platform and setup

Occlusion-aware hallway simulations use 50 trials. Indoor hardware for this
scenario is a Husarion ROSbot with a Bitcraze Crazyflie scout and Vicon pose;
a second ROSbot is the dynamic agent. Vibration-aware simulations use 30
randomized roughness maps. The vibration lab tests use a Clearpath Jackal
with a UFactory Lite6 arm, a RealSense RGB-D camera, Vicon, and a z-axis IMU
over loose debris, 20 runs per case.

## Evidence type and transfer

The hardware runs are closed-loop lab experiments with Vicon pose and a
staged dynamic agent. The drive types of the ROSbot and the Jackal are not
stated in the text found, so the platform is coded as wheeled-unspecified.
The legacy extraction does not record where the controller ran.

## Sensors

RealSense RGB-D camera for object sensing and a z-axis IMU for vibration;
Vicon motion capture provides the pose.

## Compute and latency

Not recorded in the legacy extraction; not verified.

## Key quantitative results

- Occlusion simulations (50 trials): mean minimum discovery distance 6.55 m with mission-gain versus 4.05 m with the shortest path (values not found by text search).
- Vibration lab tests: the payload stayed intact in 19 of 20 mission-gain runs versus 2 of 20 high-velocity baseline runs (p. 8).
- Peak acceleration fell from about 4.19 g at full speed to 2.06 g (slow crossing) or 1.31 g (detour) (p. 8).
- In the occlusion hardware run, naive cornering collided with the dynamic agent while the mission-gain controller took a wider path; no values are recorded in the legacy extraction.

## Stated limitations

- Unobserved cells are assigned zero cost in the example scouting policy, although other default values are possible (p. 3).
- Physical collisions were ignored in the occlusion simulation, which measured only discovery distances (p. 5).
- Future work targets scout efficiency, control-barrier collaboration, larger teams, and uncertainty in mission-gain costs (p. 8).

## Transfer conditions

Lab pose came from Vicon, not onboard SLAM. The framework is one design
pattern for coupling capability, task, and environment, not a universal
novelty claim. Reuse needs a scout that can map the mission-gain in advance
and a channel to send the GMM.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | strong | Sec. I, p. 1 | "Successful completion of unique missions can be challenging due to the combination of: varying capabilities of robots, task specific requirements, and different characteristics of environments." |

## Page-cited excerpts

- **p. 1, Sec. I.** "Successful completion of unique missions can be challenging due to the combination of: varying capabilities of robots, task specific requirements, and different characteristics of environments."
  Ties planning choices to platform capability, task, and environment.
- **p. 8, vibration experiments.** "the payload remained intact in 19 out of 20 runs with the mission-gain framework, compared with only 2 out of 20 runs for the high-velocity baseline."
  The main hardware result of the vibration scenario.
- **p. 5, occlusion-aware simulation.** "Note that physical collisions were ignored in this specific simulation since we were only interested in measuring discovery distances across the trials."
  The occlusion simulation measures discovery distance, not collisions.

## Survey-usable statements

### Supported

- A mission-gain cost map in MPPI kept a fragile payload intact in 19 of 20 runs over debris versus 2 of 20 at full speed (Jackal, Vicon pose; numbers from a light review; re-check before citing).
- Mapping and control can be split between a scout and an action robot through a compact GMM map.

### Not supported

- Collision-safety results from the occlusion simulation: collisions were ignored there.
- Operation with onboard localization: all lab runs used Vicon.

## Verification log

- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); legacy quote found and kept; Vicon pose and the design-pattern remark moved from Stated limitations to Transfer conditions; 4.05 m and 6.55 m not found by text search
- Legacy extraction: automated reviewer (codex), supplemental batch.

## Original abstract

Mobile robots often face challenges operating in partially known environments where success depends on factors such as robot capabilities, task characteristics, and the environment. This letter presents a generalized, modular framework that enables robots to explicitly account for these factors through the concept of a mission-gain: a pose dependent metric quantifying mission performance (e.g. visibility). When the environment can be proactively explored, a cost map encoding the value of the mission-gain is generated and integrated into a cost function for a model predictive path integral (MPPI) controller, which supports arbitrary mission-specific cost functions. The controller generates inputs that balance progress toward the goal with improved mission performance. The map generation is decoupled from the control execution, making the framework modular and well-suited for heterogeneous multi-robot systems. To address transmission demands of large maps, we distill the map into a Gaussian mixture model (GMM) approximation, yielding a representation with far fewer parameters. The approach is validated in simulations and lab experiments across two scenarios: occlusion-aware navigation and vibration minimization over rough-terrain. The results for both scenarios show the mission-gain aware robot successfully reaching the goal while improving mission safety.
