# Fixed-Time Fault-Tolerant Trajectory Tracking Control for a Wheeled Mobile Robot

## Metadata

| Field | Value |
|---|---|
| ID | S15 |
| Title | Fixed-Time Fault-Tolerant Trajectory Tracking Control for a Wheeled Mobile Robot |
| Authors | Ao, Wengang and Yin, Hao and Sun, Shaoxin and Liu, Pengda and Shi, Peng |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2025.3641387](https://doi.org/10.1109/tase.2025.3641387) |
| Official URL | https://ieeexplore.ieee.org/document/11284721/ |
| Theme folder | T6-reliability-deployment |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2026-Fixed-Time-FTC-S15/paper.pdf` and `02-fulltext/T6-reliability-deployment/2026-Fixed-Time-FTC-S15/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2026-Fixed-Time-FTC-S15/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: numerical
- evidence_all: numerical
- protocol_caveats: none
- platform_class: differential-drive
- platform: MATLAB numerical integration of a wheeled/unicycle kinematic and dynamic model; no physical robot test (pp. 2-3, 7).
- boundary_platform: no
- degradation: actuator-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Modeled state/velocity signals; no physical sensing pipeline evaluated
- compute: MATLAB numerical experiments; processor and hardware implementation latency not reported.
- compute_location: desktop-offline
- summary_result: Modeled fault/dead-zone compensation supports practical fixed-time tracking in numerical cases.
- summary_limitation: Dynamic event-triggered control for communication efficiency and neural-network extensions are future work (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Actuator faults and unknown dead zones impair trajectory tracking.

## Mechanism

Adaptive bounded estimates and smoothing combine fixed-time kinematic and dynamic tracking control; the derived result is practical fixed-time stability (pp. 3, 7).

## Baselines and controls

Control law cited as reference [8], tested on circular and linear numerical trajectories (p. 7).

## Platform and setup

MATLAB numerical integration of a wheeled/unicycle kinematic and dynamic model; no physical robot test (pp. 2-3, 7).

## Evidence type and transfer

Strongest coded setting: `numerical`. A bounded tracking proof under the specified model does not establish fault detection, perception robustness or physical convergence time.

## Sensors

Modeled state/velocity signals; no physical sensing pipeline evaluated.

## Compute and latency

MATLAB numerical experiments; processor and hardware implementation latency not reported.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Dynamic event-triggered control for communication efficiency and neural-network extensions are future work (p. 8).

## Transfer conditions

A bounded tracking proof under the specified model does not establish fault detection, perception robustness or physical convergence time.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 7, Selected source passage.** "In this section, numerical simulations are carried out in Matlab for the designed system."
  Separates actuator accommodation from integrity monitoring and measured deployment recovery.

## Survey-usable statements

### Supported

- Modeled fault/dead-zone compensation supports practical fixed-time tracking in numerical cases. Separates actuator accommodation from integrity monitoring and measured deployment recovery.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. A bounded tracking proof under the specified model does not establish fault detection, perception robustness or physical convergence time.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 2, 3, 7, 8; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

This work introduces a fixed-time adaptive fault-tolerant control approach to tackle the trajectory tracking issues in wheeled mobile robots by accounting for unknown dead zones and actuator faults. Firstly, by introducing smoothing functions, bounded estimates, and adaptive parameters, combined with a fixed-time control strategy, actuator faults and the impacts of unknown dead zones are effectively eliminated. Second, an adaptive fault-tolerant control strategy for nonlinear wheeled mobile robot systems is developed. Subsequently, a fixed-time trajectory tracking controller is designed to guarantee system stability and achieve high-precision control for wheeled mobile robots. Furthermore, leveraging the principles of Lyapunov stability theory, this work rigorously establishes the convergence properties of the controller, offering a robust theoretical foundation for ensuring the precision and reliability of trajectory tracking. Finally, the proposed control strategy’s effectiveness and feasibility are validated through simulation outcomes.
