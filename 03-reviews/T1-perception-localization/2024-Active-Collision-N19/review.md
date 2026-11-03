# Active Collision-Based Navigation for Wheeled Robots

## Metadata

| Field | Value |
|---|---|
| ID | N19 |
| Title | Active Collision-Based Navigation for Wheeled Robots |
| Authors | Jingjing Li, Jialin Ji, Qianhao Wang, Huan Yu, Yu Pan, Fei Gao |
| Venue | 2024 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/icra57147.2024.10610726](https://doi.org/10.1109/icra57147.2024.10610726) |
| Official URL | https://ieeexplore.ieee.org/document/10610726/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2024-Active-Collision-N19/paper.pdf` and `02-fulltext/T1-perception-localization/2024-Active-Collision-N19/paper.md` (local only); [publisher BibTeX](../../../01-papers/T1-perception-localization/2024-Active-Collision-N19/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: traversability-planning-control
- evidence_type: online-hardware
- evidence_all: online-hardware, simulation
- protocol_caveats: joystick-driving, motion-capture-pose
- platform_class: wheeled-unspecified
- platform: Hardware estimation uses teleoperated collisions in a known map with motion-capture reference; it does not demonstrate the entire active planner on hardware.
- boundary_platform: no
- degradation: sensor-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: IMU and wheel odometry; known LiDAR map; motion capture for hardware reference
- compute: Complete computation placement not established by the selected reading
- compute_location: not-reported
- summary_result: Known-map contact supports pose updates; active contact planning has separate simulation evidence.
- summary_limitation: The inspected hardware protocol uses manually commanded collisions (p. 5); a complete author limitation inventory was not assessed.
- survey_included: yes
- verification_level: light

## Problem

When exteroceptive updates are unavailable, known-map contact can provide an additional observation.

## Mechanism

A differentiable collision observation model is inserted into Kalman and particle filters; a separate planner schedules contacts to reduce estimated uncertainty (pp. 1, 4-6).

## Baselines and controls

Hardware contacts are manually driven; active contact planning is evaluated separately in simulation (pp. 5-6).

## Platform and setup

Hardware estimation uses teleoperated collisions in a known map with motion-capture reference; it does not demonstrate the entire active planner on hardware.

## Evidence type and transfer

The strongest inspected setting is `online-hardware`. Contact permission, known-map validity and tolerable impact are operating conditions; do not equate informative contact with collision-free navigation.

## Sensors

IMU and wheel odometry; known LiDAR map; motion capture for hardware reference.

## Compute and latency

Complete computation placement not established by the selected reading.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 6).

## Stated limitations

A complete author-stated limitation inventory was not assessed in this targeted reading. The inspected implementation and protocol boundaries are recorded under Platform and setup and Transfer conditions.

## Transfer conditions

Contact permission, known-map validity and tolerable impact are operating conditions; do not equate informative contact with collision-free navigation.

## Code and data

Availability and links beyond the publisher artifacts were not independently verified in this targeted reading.

## Version family

One publisher DOI is counted. A comprehensive preprint/extension-family search was not performed in this targeted reading.

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

- **p. 5, Selected source passage.** "we manually remote the robot to randomly collide with"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Known-map contact supports pose updates; active contact planning has separate simulation evidence.
- Contact permission, known-map validity and tolerable impact are operating conditions; do not equate informative contact with collision-free navigation.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. The inspected hardware protocol uses manually commanded collisions (p. 5); a complete author limitation inventory was not assessed.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 4, 5, 6; Selected abstract, active planning, implementation, hardware localization protocol, simulation planner test and conclusion; complete filter derivation not audited. No table numbers retained. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **— Collision** **is** **typically** **avoided** **in** **robot** **navigation**
**for** **safety** **guarantee.** **However,** **when** **a** **robot’s** **exteroceptive**
**sensors** **fail,** **which** **means** **it** **becomes** **”blind”,** **collision** **can**
**actually be leveraged to improve localization performance. Our**
**research** **demonstrates** **the** **informative** **nature** **of** **collisions** **in**
**this** **context.** **Moreover,** **we** **show** **that** **a** **robot** **is** **able** **to** **navigate**
**in** **a** **known** **environment** **with** **only** **proprioceptive** **sensors**
**by** **actively** **colliding** **with** **its** **surroundings** **for** **more** **reliable**
**localization.** **Firstly,** **we** **design** **a** **collision-based** **observation**
**model,** **which** **is** **differentiable** **and** **can** **be** **easily** **applied** **to**
**various** **estimators.** **Secondly,** **we** **integrate** **this** **model** **into** **a**
**collision-aided** **localization** **framework** **and** **implement** **it** **in** **two**
**widely used estimators, the Kalman filter and the particle filter.**
**Thirdly,** **we** **propose** **an** **active** **collision** **path** **planning** **method,**
**which** **effectively** **reduces** **localization** **uncertainty.**
