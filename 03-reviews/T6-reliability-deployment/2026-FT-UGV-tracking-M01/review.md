# Fault-Tolerant Trajectory Tracking for Unmanned Ground Vehicles via Virtual Error-Based Prescribed Performance Control

## Metadata

| Field | Value |
|---|---|
| ID | M01 |
| Title | Fault-Tolerant Trajectory Tracking for Unmanned Ground Vehicles via Virtual Error-Based Prescribed Performance Control |
| Authors | Jin-Xi Zhang, Jing Zhao, and Pak Kin Wong |
| Venue | IEEE Transactions on Automatic Control, vol. 71, no. 4, pp. 2660-2667 |
| Year | 2026 (online 2025) |
| Type | journal |
| DOI | [10.1109/tac.2025.3628929](https://doi.org/10.1109/tac.2025.3628929) |
| Official URL | https://ieeexplore.ieee.org/document/11224769/ |
| Theme folder | T6-reliability-deployment |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T6-reliability-deployment/2026-FT-UGV-tracking-M01/paper.pdf` and `02-fulltext/T6-reliability-deployment/2026-FT-UGV-tracking-M01/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2026-FT-UGV-tracking-M01/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: numerical
- evidence_all: numerical
- protocol_caveats: none
- platform_class: differential-drive
- platform: Unnamed differentially driven UGV model (text description retained from the legacy extraction)
- boundary_platform: no
- degradation: sensor-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Heading and wheel-speed measurements; position assumed perfectly measured
- compute: No processor or implementation timing recorded
- compute_location: not-reported
- summary_result: In numerical circular tracking with injected sensor faults, the legacy extraction reports position error below 0.02 m after 10 s.
- summary_limitation: Perfect position measurement is assumed despite faults in heading and wheel-speed measurements.
- survey_included: yes
- verification_level: light

## Problem

Track a trajectory with an underactuated differentially driven UGV whose heading and wheel-speed measurements have time-varying drift or bias. Nonlinear dynamics, input coupling, and disturbances are unknown. The method assumes perfect position measurement; the legacy extraction records the authors' statement that accurate control is nearly inaccessible without it under these uncertainties.

## Mechanism

A virtual-error recursive design implements fault-tolerant prescribed-performance control (PPC). A virtual error combines position error and the faulty heading measurement, while intermediate errors stay inside designer-selected envelopes to preassign settling time and accuracy. The law uses bounded control torques without fault diagnosis, disturbance estimation, function approximation, or parameter identification. The light conversion does not establish guarantees beyond the assumptions recorded in the legacy extraction.

## Baselines and controls

Adaptive fuzzy prescribed-performance control (AFPPC) is the named comparator, run on the UGV model under the injected sensor faults and noise. The legacy extraction records envelope loss and instability after the heading fault; a numerical comparator value was not extracted.

## Platform and setup

A comparative numerical study uses a differentially driven UGV model with wheel radius 0.15 m, half-track 0.75 m, body mass 30 kg, and associated inertial parameters. It follows a circular reference under asynchronous heading and wheel-speed faults plus additive measurement noise. No physical chassis, field sensor suite, or hardware trial is recorded.

## Evidence type and transfer

The legacy card calls this simulation-only; under the controlled vocabulary it is numerical integration of a UGV model, without sensor or physics simulation recorded. The result supports fault-tolerant tracking under the model conditions, without demonstrating hardware deployment or navigation among obstacles.

## Sensors

Heading and the two actuated wheels' angular velocities are measured with injected faults. Position is assumed perfectly measured. No LiDAR or vision localization stack is specified.

## Compute and latency

Not recorded in the legacy extraction; not verified.

## Key quantitative results

- Numerical circular tracking: the legacy extraction reports position error below 0.02 m for time at or after 10 s with injected heading and wheel-speed measurement faults (p. 6; the 0.02 value located, not re-verified).
- AFPPC loses the prescribed envelope after the heading fault and becomes unstable in the legacy comparison; no numerical baseline error was extracted (p. 7, Fig. 11).

## Stated limitations

- The position measurement is assumed perfect even though heading and wheel-speed measurements are faulty (p. 2).
- The conclusion names fault-tolerant control of underactuated aerial vehicles as future investigation (p. 8).

## Transfer conditions

The trajectory-tracking result depends on a differentially driven model, perfect position input, and the modeled drift/bias faults. It does not establish tolerance of arbitrary sensor failures or a combined localization-and-control stack. Fault tolerance is implicit in the controller; there is no fault detector or system-level recovery behavior. Hardware timing, actuator limits, sensing, and the theorem's full assumptions require a separate check before reuse.

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
| C5 | partial-support | moderate | Abstract, p. 1 | "It steers the UGV to track the target trajectory with the preassigned rate and accuracy, versus the sensor faults, unknown dynamics, and exogenous disturbances." |
| C6 | qualifies | moderate | Remark 1, p. 2 | "perfect measurement of the UGV position" |

## Page-cited excerpts

- **p. 1, Abstract.** "It steers the UGV to track the target trajectory with the preassigned rate and accuracy, versus the sensor faults, unknown dynamics, and exogenous disturbances."
  This records the stated fault-tolerant control objective under the paper's assumptions.
- **p. 2, Remark 1.** "perfect measurement of the UGV position"
  The perfect-position assumption limits transfer to a robot whose position estimate may itself degrade.

## Survey-usable statements

### Supported

- A virtual-error PPC design addresses modeled heading and wheel-speed measurement drift/bias while assuming perfect position input.
- Its legacy evidence is a comparative numerical UGV study; the reported tracking bound must be rechecked before citation.

### Not supported

- The method detects sensor faults or recovers a failing localization stack; it does not perform diagnosis and assumes perfect position measurement.
- The paper validates an onboard controller on a physical wheeled robot; only numerical model evidence is recorded.
- The control guarantee covers arbitrary sensor failures; the legacy extraction concerns modeled time-varying drift and bias.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: English template conversion; legacy abstract replaced with actual abstract; no legacy verbatim excerpt to retain; abstract and perfect-position excerpts located; claim scope narrowed to match excerpts; numbers not re-verified
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

The problem of trajectory tracking for the underactuated ground vehicle (UGV) subject to the sensor faults is explored in this article. It is focused on the case of the sensor measurements with time-varying drift and bias and the UGV with unknown nonlinear dynamics and inputs coupling, which render the related solutions infeasible. To conquer this challenge, a novel fault-tolerant prescribed performance control approach via a virtual errors-based recursive design is put forward. It steers the UGV to track the target trajectory with the preassigned rate and accuracy, versus the sensor faults, unknown dynamics, and exogenous disturbances. Moreover, no attempt is made for fault diagnosis, disturbance estimation, function approximation, or parameter identification, leading to a control simplicity.
