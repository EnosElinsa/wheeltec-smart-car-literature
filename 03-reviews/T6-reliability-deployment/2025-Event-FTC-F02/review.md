# Event-Triggered Fault-Tolerant Tracking Control for Autonomous Ground Vehicle via Descriptor Reduced-Order Observer

## Metadata

| Field | Value |
|---|---|
| ID | F02 |
| Title | Event-Triggered Fault-Tolerant Tracking Control for Autonomous Ground Vehicle via Descriptor Reduced-Order Observer |
| Authors | Renjie Ma, Yan Yu, Su Zhang, and Peng Shi |
| Venue | IEEE Transactions on Intelligent Transportation Systems, vol. 26, no. 7, pp. 10308-10319 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tits.2025.3548150](https://doi.org/10.1109/tits.2025.3548150) |
| Official URL | https://ieeexplore.ieee.org/document/10927615/ |
| Theme folder | T6-reliability-deployment |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T6-reliability-deployment/2025-Event-FTC-F02/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Event-FTC-F02/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-Event-FTC-F02/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, numerical
- protocol_caveats: offboard-compute, speed-capped, scripted-scenario, few-trials
- platform_class: ackermann
- platform: Unnamed car-like AGV with steering front axle (bicycle model, p. 2; hardware-in-loop setup, p. 8)
- boundary_platform: no
- degradation: actuator-fault, sensor-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Vehicle posture outputs in the model; physical sensor suite not established in the passages read
- compute: Jetson Nano plus Windows/Ubuntu PCs over LAN; STM32 lower controller; individual timing not established
- compute_location: mixed
- summary_result: The numerical example reports 85.64% triggering efficiency versus a 100% time-trigger rate; hardware-in-loop setpoint tests span five single and three sequential initial postures.
- summary_limitation: The tested initial-posture range is narrow; complex real faults and extreme conditions remain to be investigated.
- survey_included: yes
- verification_level: light

## Problem

Track a prescribed vehicle setpoint despite sensor and actuator faults while reducing control transmissions. The targeted model is a low-speed car-like vehicle, rather than a fault-tolerant localization-and-navigation stack.

## Mechanism

A reduced-order descriptor sliding-mode observer reconstructs tracking-error states and physical faults. Estimated error dynamics feed an event-triggered tolerant controller; stability conditions support co-design of observer gains, controller gains, and trigger parameters. The proof details and all matrix inequalities were not audited in this light reading.

## Baselines and controls

Numerical comparison uses time-triggered control with a nominal 100% triggering rate. The paper explains that direct comparison with controllers [3] and [38] is inappropriate because their model/fault formulations differ. No hardware baseline performance metric was established in the passages read.

## Platform and setup

Section IV-A numerically evaluates a vehicle at 0.3 m/s with 0.2 m wheelbase and prescribed sinusoidal fault/disturbance signals. Section IV-B calls the experiment hardware-in-loop: ROS and a local network connect Jetson Nano and Windows/Ubuntu PCs to STM32 and the AGV. Single-setpoint tracking uses five initial postures; sequential setpoint tracking uses three. The hardware figure and text were read on p. 8; no field autonomy claim is made.

## Evidence type and transfer

The experiment text describes practical AGV motion and feedback tracking, supporting closed-loop hardware with a substantial HiL/offboard-compute caveat. The numerical result and plotted fault signals are separate evidence. Injected faults and a LAN-connected laboratory stack do not establish spontaneous component failure or long-term recovery in the field.

## Sensors

The observer uses measured posture-related model outputs, with additive sensor-fault and disturbance channels. Physical sensing devices, ground truth, and sensor calibration were not established in the selected setup passages; not verified.

## Compute and latency

The HiL upper-computer layer combines the vehicle Jetson Nano with Windows and Ubuntu PCs; STM32 and AGV hardware form the lower layer (p. 8, Fig. 7). The exact allocation of observer/controller modules and end-to-end timing were not established. A reduced transmission count is not a measured reduction in CPU time or end-to-end network latency.

## Key quantitative results

- The numerical text reports tracking-state convergence at about 11 s under its selected fault signals (p. 7); plot values were not independently verified.
- The numerical text reports 85.64% triggering efficiency versus a 100% time-trigger rate (p. 7). The meaning of this label was preserved; it is not recast as 85.64% traffic saved.
- HiL evaluation spans five initial postures for one setpoint and three for sequential setpoints (pp. 8-9). Repeated trials and hardware error statistics were not established.

## Stated limitations

- The initial-posture range is relatively narrow and does not cover all scenarios; slower or incomplete convergence can occur under more complex or extreme conditions (p. 10).
- Real sensor faults and disturbances can be more complex and unpredictable than the experimental model (p. 10).

## Transfer conditions

The model assumes low-speed rolling without slip (p. 2). System matrices are known, an observability/invariant-zero condition is required, and fault/disturbance magnitude bounds inform design (p. 3). These are conditions on the analysis, not general tolerance of all physical faults. Another vehicle needs suitable steering kinematics, sensing, fault channels, and verified implementation timing. Hardware-in-loop results do not validate rough terrain, collision avoidance, lost network connectivity, or fault recovery across a full autonomy stack.

## Code and data

The paper links experiment videos https://youtu.be/4aqSejbu4HE and https://youtu.be/fW3E4FxjJAY (pp. 8-9). They were not opened or independently checked. Code/data availability was not established in this reading.

## Version family

Publisher PDF and unmodified BibTeX identify the July 2025 IEEE T-ITS article; online publication is March 14, 2025. Related conference/preprint versions were not checked.

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

- **p. 1, Abstract.** "First, allowing for the AGV kinematics and the setpoint tracking objective, we design a reduced-order descriptor sliding mode observer to synchronously reconstruct the tracking error states as well as physical faults."
  This supports model-based estimation and fault-tolerant tracking, without claiming system-level recovery.
- **p. 2, Section II-A.** "Within the context of low-speed motion, we assume that both wheels can roll without slipping [3]."
  The no-slip kinematic assumption limits terrain and wheel-slip transfer.
- **p. 8, Section IV-B.** "In this subsection, we aim at performing a hardware-in-loop (HiL) experimental study of AGV to validate the effectiveness and potential of Procedure 1."
  The authors explicitly identify the experimental protocol as HiL.
- **p. 10, Section IV-B.** "the range of initial postures considered in the experiments is relatively narrow and does not comprehensively cover all potential scenarios."
  The authors limit the tested initial conditions.

## Survey-usable statements

### Supported

- A descriptor reduced-order observer and event-triggered controller combine modeled fault estimation with setpoint tracking.
- The authors report a numerical example and LAN-connected AGV hardware-in-loop tests under a limited initial-posture set.

### Not supported

- The method validates field recovery from arbitrary physical failures: faults are modeled and the authors limit the experiment's scope.
- The model handles wheel slip: low-speed no-slip rolling is assumed.
- The numerical 85.64% label establishes that much traffic saved or reduced CPU use: the paper calls it triggering efficiency and no timing audit was performed.

## Verification log

- 2026-11-02 | host: Codex | scope: targeted light reading of selected PDF passages: PDF p. 1 identity/abstract; p. 12 last-page layout; selected Section II model/assumptions on pp. 2-3; Section IV numerical and HiL setup on pp. 7-9; author limitations and Section V on p. 10; rendered p. 8 read for Fig. 7 protocol only, not numerical plots; excerpts matched to the cited physical PDF pages; no whole-paper or complete numerical verification | corrections: new targeted light card; no legacy review; HiL evidence, mixed compute, no-slip/known-model assumptions, and numerical-only triggering metric separated
- New follow-up acquisition; no legacy extraction. Metadata checked against the publisher PDF and unmodified publisher BibTeX. The original MinerU transcription is preserved; final transcription-bound validation is recorded below.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

Autonomous ground vehicles (AGVs) play an important role in transportation, environmental exploration, and so on. However, they may suffer from inevitable sensor and actuator faults which degenerate the setpoint tracking performance. Within this context, this paper focuses on the issues of deploying event-triggered fault-tolerant controller based on reduced-order descriptor observer. First, allowing for the AGV kinematics and the setpoint tracking objective, we design a reduced-order descriptor sliding mode observer to synchronously reconstruct the tracking error states as well as physical faults. Then, we develop an event-triggered communication scheme in the control center side, leading to the tolerant controller by virtue of reconstructed tracking error dynamics with an improved transmission efficiency. In addition, we perform the strict theoretical guarantee of both estimation stability and tracking stability, based on which, the estimator and controller gains in conjunction with event trigger parameters are codesigned. Finally, the correctness and effectiveness of theoretical derivation are examined by the experimental study of setpoint tracking of AGV.
