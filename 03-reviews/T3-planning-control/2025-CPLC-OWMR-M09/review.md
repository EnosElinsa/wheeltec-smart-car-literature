# Constrained Predictive Learning Control for Omnidirectional Wheeled Mobile Robots via Reducing Iteration Horizon

## Metadata

| Field | Value |
|---|---|
| ID | M09 |
| Title | Constrained Predictive Learning Control for Omnidirectional Wheeled Mobile Robots via Reducing Iteration Horizon |
| Authors | Wenxian Wang and Deyuan Meng |
| Venue | IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 15513-15525 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tase.2025.3569611](https://doi.org/10.1109/tase.2025.3569611) |
| Official URL | https://ieeexplore.ieee.org/document/11003108/ |
| Theme folder | T3-planning-control |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T3-planning-control/2025-CPLC-OWMR-M09/paper.pdf` and `02-fulltext/T3-planning-control/2025-CPLC-OWMR-M09/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-CPLC-OWMR-M09/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, numerical
- protocol_caveats: external-pose-source, offboard-compute
- platform_class: omnidirectional
- platform: custom four-Mecanum-wheel omnidirectional robot (STM32F407, Jetson Nano, UWB positioning)
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: IMU (yaw), motor encoders, UWB indoor positioning
- compute: i7-14700HX PC solves the learning problem offline over ROS (277.23 s versus 692.95 s per run in simulation); STM32F407 and Jetson Nano onboard
- compute_location: mixed
- summary_result: After 9 learning iterations on the Mecanum robot, tracking errors stayed below 0.07 m and 0.03 rad; the reducing horizon cut offline solve time from 692.95 s to 277.23 s.
- summary_limitation: The lifted-model optimization is computationally heavy, so the controller suits moderate-length trajectories, and initial-condition assumptions restrict its application.
- survey_included: yes
- verification_level: light

## Problem

The paper targets high-precision repetitive trajectory tracking on a
four-Mecanum omnidirectional wheeled mobile robot. Learning must stay safe
under input-difference constraints, and the computational load grows with the
prediction horizon.

## Mechanism

Constrained predictive learning control (PLC) "learns from the future": it
optimizes over a lifted model with terminal cost and constraints, and its
stability across iterations is analyzed with composite energy functions. A
reducing-iteration-horizon optimization (RIHO) shrinks the horizon until a
user-defined length. Open-loop feedforward inputs are solved offline for each
iteration and then applied on the robot.

## Baselines and controls

Simulation compares PLC with optimal and P-type iterative learning control
(ILC), feedback-linearized PID, and nonlinear model predictive control (NMPC),
under nominal conditions and with time-varying uncertainty.

## Platform and setup

Simulations use a nonlinear robot model. Hardware is a custom Mecanum robot
with an STM32F407 controller and onboard IMU, a Jetson Nano (Ubuntu 18.04),
wheel encoders, and UWB indoor positioning. An i7-14700HX PC solves the PLC
problem offline and communicates over ROS. Hardware learning stopped after 9
iterations. The scene is indoor repetitive tracking, not outdoor navigation.

## Evidence type and transfer

The hardware runs apply the learned feedforward inputs on the robot, so the
evidence is closed-loop hardware for repetitive tracking. The optimization
runs offline on a PC, which is coded as offboard compute, and the robot pose comes from UWB indoor positioning, coded as an external pose source. The legacy
extraction describes PLC as an offline, repetitive feedforward law on a
holonomic Mecanum platform with UWB, not an onboard receding-horizon
navigator.

## Sensors

IMU for yaw, motor encoders, and UWB indoor positioning.

## Compute and latency

The PLC problem is solved offline on an i7-14700HX PC. With the reducing
horizon the offline time was 277.23 s, versus 692.95 s with a constant
horizon (about 60% less). The STM32F407 and Jetson Nano run onboard.

## Key quantitative results

- Hardware tracking errors after 9 iterations: below 0.07 m and 0.03 rad (p. 10).
- Offline computation time: 277.23 s with the reducing horizon versus 692.95 s with a constant horizon (Table I; values found only in the transcription, not on a PDF page).
- The reducing horizon strategy cuts offline computational time by 60% (p. 12).

## Stated limitations

- The computational burden of the optimization problem, including the lifted model, is relatively high (p. 12).
- Because a larger sampling period increases linearization error, the controller is more suitable for moderate-length trajectories (p. 12).
- Linearization, repositioning, and sensor measurement errors prevent the tracking errors from reaching zero, so learning is terminated once performance is acceptable (p. 11).
- The initial condition imposes limitations on the application of the controller (p. 12).
- Future work targets longer trajectories and a theoretical analysis of initial errors (p. 12).

## Transfer conditions

The evidence is repetitive indoor tracking on a holonomic Mecanum robot with
UWB positioning and an offline PC solver. A non-holonomic robot, a
non-repetitive task, or onboard-only compute would need a different setup.
The method needs repeated trials of the same reference trajectory.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | direct-support | strong | Sec. V, p. 12 | "The computational burden associated with the optimization problem (7), including the lifted model, is relatively high." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V, p. 12 | "the proposed controller is more suitable for trajectory tracking tasks involving moderate-length trajectories" |

## Page-cited excerpts

- **p. 12, Sec. V.** "The computational burden associated with the optimization problem (7), including the lifted model, is relatively high."
  The authors' own statement of the compute cost.
- **p. 12, Sec. VI.** "Both numerical simulations and hardware experiments have been conducted to evaluate the performance of the proposed PLC algorithm"
  Names the two evidence settings; the hardware is one Mecanum robot.
- **p. 11, Sec. V.** "prevent the tracking errors from reaching zero"
  Residual errors limit how far learning can go.

## Survey-usable statements

### Supported

- Predictive learning control with input-difference constraints reached sub-0.07 m tracking error after 9 iterations on a Mecanum robot (numbers from a light review; re-check before citing).
- A reducing prediction horizon cut offline solve time by about 60% in simulation.

### Not supported

- Onboard real-time control: the optimization is solved offline on a PC.
- Application to non-repetitive navigation or long trajectories: the authors restrict it to moderate-length repetitive tracking.
- Transfer to non-holonomic or outdoor robots: the evidence is one indoor Mecanum platform with UWB.

## Verification log

- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); legacy C6 excerpt replaced by a limitation sentence that shows the qualification; legacy limitations given pages from text search; Table I times found only in the transcription; abstract copied from the transcription, which drops the "ff" ligature
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

This paper proposes a predictive learning controller for an omnidirectional wheeled mobile robot (OWMR) with the target of achieving high-precision tracking of the desired trajectory within repetitive tasks. A prediction mechanism, based on the concept of “learning from the future,” is presented to accelerate learning convergence. Moreover, a constrained mechanism is leveraged to guarantee learning safety by introducing constraints on the input diference. The stability of OWMR under the proposed predictive learning controller is realized by formulating an optimization problem that incorporates terminal costs and constraints, together with its performance across iterations being evaluated through an analysis method based on composite energy functions. Additionally, a reducing prediction horizon strategy is adopted to mitigate computational burden, which both enhances the suitability and ensures the initial feasibility of the predictive learning controller for real-world applications. Subsequently, our predictive learning controller is implemented on the OWMR, together with several practical discussions for its deployment. Comparative simulations and real-world experiments are conducted to validate the practicality and efectiveness, highlighting its advantages over existing approaches.
