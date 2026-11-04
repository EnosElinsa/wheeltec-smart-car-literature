# A Coordinated Approach to Control Mechanical and Computing Resources in Mobile Robots

## Metadata

| Field | Value |
|---|---|
| ID | R32 |
| Title | A Coordinated Approach to Control Mechanical and Computing Resources in Mobile Robots |
| Authors | Sajad Shahsavari, Hashem Haghbayan, Antonio Miele, Eero Immonen, and Juha Plosila |
| Venue | IEEE Transactions on Robotics |
| Year | 2025 (DOI year 2024) |
| Type | journal |
| DOI | [10.1109/tro.2024.3492345](https://doi.org/10.1109/tro.2024.3492345) |
| Official URL | https://ieeexplore.ieee.org/document/10746315/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-Mechanical-Compute-Energy-R32/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Mechanical-Compute-Energy-R32/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-Mechanical-Compute-Energy-R32/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Wheeled rover with a DC motor, Jetson TX2 and DAVIS346 event camera in four environment-complexity settings (pp. 2-4, 11).
- boundary_platform: no
- degradation: energy-limit, compute-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Event camera; motor power module and on-chip power sensors
- compute: Jetson TX2 onboard with DVFS control (p. 4).
- compute_location: onboard
- summary_result: Joint runtime control of motor speed and CPU voltage/frequency reduces overall energy consumption by up to 36.34% versus prior methods (p. 1).
- summary_limitation: Communication energy is not considered; GPU acceleration and task migration are future work (pp. 3, 7).
- survey_included: yes
- verification_level: light

## Problem

Separate mechanical and computational energy management is not energy-optimal because vision workload depends on speed.

## Mechanism

Dynamically trained models predict mechanical and computing energy; a knowledge matrix and decision algorithm choose motor speed and DVFS level that satisfy application QoS (pp. 7-10).

## Baselines and controls

Separate optimization of mechanical and computing parts and prior energy managers (p. 12).

## Platform and setup

Low, moderate, high and variable environment complexity with a corner-detection QoS requirement (pp. 4, 11). Wheeled rover with a DC motor, Jetson TX2 and DAVIS346 event camera in four environment-complexity settings (pp. 2-4, 11).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Physical rover experiments with onboard measurement.

## Sensors

Event camera; motor power module and on-chip power sensors.

## Compute and latency

Jetson TX2 onboard with DVFS control (p. 4).

## Key quantitative results

- Separate optimization does not reach the minimum energy because it tunes mechanical and computational parts independently (p. 12).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Communication energy is not considered (p. 7).
- GPU acceleration and task migration on asymmetric CPUs are future work (p. 3).

## Transfer conditions

Energy coupling depends on the perception workload; navigation safety is not part of the objective.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

The authors extend their earlier hill-climbing co-optimization approach (pp. 2, 6); that work is not in the library, and this journal article is counted once.

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

- **p. 7, Sec. III-C.** "Therefore, here the communication energy is not considered at present since it does not represent the main contribution to the overall energy consumption."
  Author-stated scope.
- **p. 12, Sec. V-B.** "Notably, the SO strategy does not reach to minimum energy consumption level, since it tunes the mechanical and computational parts separately."
  Supports joint management.

## Survey-usable statements

### Supported

- Speed and processor settings jointly determine energy use on a wheeled robot running vision workloads.

### Not supported

- The approach is not evaluated with navigation safety constraints.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 7, 11, 12; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Energy management of mechanical and cyber parts in mobile robots consists of two processes operating concurrently at runtime. Both the two processes can significantly improve the robots' battery lifetime and further extend mission time. In each process, information on energy consumption of one of the two parts is captured and analyzed to manipulate various mechanical/computational actuators in a robot, such as motor speed and CPU voltage/frequency. In this article, we show that considering management of mechanical and computational segments separately does not necessarily result in an energy-optimal solution due to their co-dependence; as a consequence, a runtime co-management scheme is required. We propose a proactive energy optimization methodology in which dynamically trained internal models are utilized to predict the future energy consumption for the mechanical and computational parts of a mobile robot, and based on that, the optimal mechanical speed and CPU voltage/frequency are determined at runtime. The experimental results on a ground wheeled robot show up to 36.34% reduction in the overall energy consumption compared to the state-of-the-art methods.
