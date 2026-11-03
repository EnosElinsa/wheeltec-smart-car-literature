# NMPC-Augmented Visual Navigation and Safe Learning Control for Large-Scale Mobile Robots

## Metadata

| Field | Value |
|---|---|
| ID | N10 |
| Title | NMPC-Augmented Visual Navigation and Safe Learning Control for Large-Scale Mobile Robots |
| Authors | Mehdi Heydari Shahna, Pauli Mustalahti, Jouni Mattila |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3669802](https://doi.org/10.1109/lra.2026.3669802) |
| Official URL | https://ieeexplore.ieee.org/document/11419776/ |
| Theme folder | T3-planning-control |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2026-NMPC-Safe-Learning-N10/paper.pdf` and `02-fulltext/T3-planning-control/2026-NMPC-Safe-Learning-N10/paper.md` (local only); [publisher BibTeX](../../../01-papers/T3-planning-control/2026-NMPC-Safe-Learning-N10/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: skid-steer
- platform: Physical trials use a 6,000 kg skid-steering electro-hydrostatic vehicle, with an INS-RTK reference distinct from the visual estimate (p. 5).
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Stereo visual ORB-SLAM3; INS-RTK for experimental reference
- compute: High-level vision/NMPC and low-level electro-hydrostatic actuation; complete compute placement not retained
- compute_location: not-reported
- summary_result: Tracking loss triggers an implemented safety stop and relocalization attempt on a physical vehicle.
- summary_limitation: Failed relocalization leads to a SLAM restart and repetition of the trial (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Visual navigation and learned actuation need a specified response when tracking is lost.

## Mechanism

The system combines ORB-SLAM3, NMPC wheel references, adaptive learned actuator control and a safety supervisor (pp. 5-6).

## Baselines and controls

Trajectory/surface comparisons distinguish high-level vision/NMPC effects from low-level actuation effects; Table I performance cells were not used (pp. 6-7).

## Platform and setup

Physical trials use a 6,000 kg skid-steering electro-hydrostatic vehicle, with an INS-RTK reference distinct from the visual estimate (p. 5).

## Evidence type and transfer

The strongest inspected setting is `closed-loop-hardware`. Stopping and attempting relocalization is implemented; restarting an experiment is distinct from autonomous continuation of that same mission.

## Sensors

Stereo visual ORB-SLAM3; INS-RTK for experimental reference.

## Compute and latency

High-level vision/NMPC and low-level electro-hydrostatic actuation; complete compute placement not retained.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- Failed relocalization leads to a SLAM restart and repetition of the trial (p. 6).

## Transfer conditions

Stopping and attempting relocalization is implemented; restarting an experiment is distinct from autonomous continuation of that same mission.

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
| C5 | partial-support | moderate | p. 6 | "any tracking loss triggered a safety stop and relocalization attempt" |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 6, Selected source passage.** "any tracking loss triggered a safety stop and relocalization attempt"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Tracking loss triggers an implemented safety stop and relocalization attempt on a physical vehicle.
- Stopping and attempting relocalization is implemented; restarting an experiment is distinct from autonomous continuation of that same mission.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. Failed relocalization leads to a SLAM restart and repetition of the trial (p. 6).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 5, 6, 7, 8; Selected abstract, safety/configuration, recovery handling, evaluation and conclusion. Rendered configuration/recovery pp. 5-6 checked; no table-performance numbers retained. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—A** **large-scale** **mobile** **robot** **(LSMR)** **is** **a** **high-order**
**multibody** **system** **that** **often** **operates** **on** **unconsolidated** **terrain,**
**which** **reduces** **traction.** **This** **paper** **presents** **an** **integrated** **navi-**
**gation and control framework for an LSMR that ensures stability**
**andsafety-definedperformanceonslip-proneterrainbycombining**
**high-performance methods. The proposed architecture comprises**
**four main modules: (1) a visual pose-estimation module that fuses**
**onboard** **sensors and** **stereo cameras** **to provide an** **accurate,** **low-**
**latency robot pose, (2) a high-level nonlinear model predictive con-**
**trol (NMPC) that updates the wheel motion commands to correct**
**robot drift from the robot reference pose, (3) a low-level deep neural**
**network control policy that approximates the complex behavior of**
**the wheel-driven actuation mechanism in LSMRs, augmented with**
**robust adaptive control to handle out-of-distribution disturbances,**
**ensuring that the wheels accurately track the updated commands**
**issued** **by** **high-level** **control** **module,** **and** **(4)** **a** **logarithmic** **safety**
**module to monitor the entire robot stack and guarantee safe oper-**
**ation. The proposed actuator-level control framework guarantees**
**uniform** **exponential** **stability** **for** **tracking** **the** **NMPC-generated**
**commands, while the safety module ensures overall system safety**
**during operation. Comparative experiments were conducted on a**
**6,000 kg LSMR actuated by two electro-hydrostatic drives.**
