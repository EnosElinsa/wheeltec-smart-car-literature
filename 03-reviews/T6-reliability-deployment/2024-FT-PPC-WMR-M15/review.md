# Fault-Tolerant Prescribed Performance Control of Wheeled Mobile Robots: A Mixed-Gain Adaption Approach

## Metadata

| Field | Value |
|---|---|
| ID | M15 |
| Title | Fault-Tolerant Prescribed Performance Control of Wheeled Mobile Robots: A Mixed-Gain Adaption Approach |
| Authors | Jin-Xi Zhang, Jinliang Ding, and Tianyou Chai |
| Venue | IEEE Transactions on Automatic Control, vol. 69, no. 8, pp. 5500-5507 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/tac.2024.3365726](https://doi.org/10.1109/tac.2024.3365726) |
| Official URL | https://ieeexplore.ieee.org/document/10433674/ |
| Theme folder | T6-reliability-deployment |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T6-reliability-deployment/2024-FT-PPC-WMR-M15/paper.pdf` and `02-fulltext/T6-reliability-deployment/2024-FT-PPC-WMR-M15/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2024-FT-PPC-WMR-M15/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: numerical
- evidence_all: numerical
- protocol_caveats: none
- platform_class: differential-drive
- platform: Unnamed differentially driven WMR model (legacy text description)
- boundary_platform: no
- degradation: actuator-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: No sensing stack recorded; high-frequency measurements required for implementation
- compute: MATLAB Simulink, Bogacki-Shampine integration; 0.01 s step, 60 s horizon
- compute_location: not-reported
- summary_result: In numerical circular tracking under partial actuator loss, the legacy extraction reports position error below 0.02 m after 10 s.
- summary_limitation: Errors are bounded within envelopes rather than exactly compensated; high-rate sampling and gain tuning are required.
- survey_included: yes
- verification_level: light

## Problem

Track trajectories with an underactuated differentially driven wheeled mobile robot under partial loss of effectiveness (PLOE) of its actuated wheels. PLOE can invalidate the strong-controllability assumption used by classical fault-tolerant control. Unknown dynamics, input coupling, and disturbances, including modeled uneven-road effects, are also considered.

## Mechanism

Mixed-gain adaptation is combined with robust prescribed-performance control. Wheel-health indices satisfy h_i(t) in (0, 1] and scale the two torques: the modeled fault is partial effectiveness loss, not total actuator failure. Settling time and accuracy are prescribed through an error envelope. The controller uses no parameter identification, function approximation, disturbance estimation, or fault estimation; additive actuator faults are absorbed into the disturbance term.

## Baselines and controls

A controller without mixed-gain adaptation is the comparator under the same simulated faulty WMR conditions. The legacy extraction records tracking until the second fault followed by envelope violation; it does not provide a numerical comparator error.

## Platform and setup

MATLAB Simulink performs numerical integration with a Bogacki-Shampine solver, a 0.01 s step, and a 60 s horizon. A differential-drive WMR model follows a circle, with time-varying effectiveness loss injected on wheel 1 after 2 s and wheel 2 after 30 s. A zero-velocity positioning case is also shown. No physical robot, named chassis, or sensing stack is recorded.

## Evidence type and transfer

The legacy simulation-only label denotes numerical integration of the WMR equations, with no physics or sensor simulation recorded. It illustrates tracking under designed actuator-fault profiles. It does not demonstrate field fault recovery, hardware tolerances, or a complete robot autonomy system.

## Sensors

No sensor suite is specified in the legacy extraction. The authors state that high-frequency sampling sensors are necessary for implementation (p. 7).

## Compute and latency

MATLAB Simulink uses Bogacki-Shampine integration with a 0.01 s step for 60 s. Processor, computation location, and actual controller latency were not recorded. The simulation step is not an onboard timing measurement.

## Key quantitative results

- Numerical circular tracking: the legacy extraction reports position error below 0.02 m for time at or after 10 s under injected partial loss of wheel effectiveness (p. 6; value located, not re-verified).
- The numerical study uses a 0.01 s integration step over 60 s; wheel-effectiveness faults begin after 2 s and 30 s (p. 6).
- The comparator without mixed-gain adaptation violates its envelope after the second fault; numerical error values were not extracted (p. 7, Fig. 11).

## Stated limitations

- The controller regulates error bounds rather than errors themselves; periodic oscillation may remain within the envelopes, and compensation-based design is future work (p. 6, Remark 7).
- Large gains may exceed actuator saturation; implementation needs high-frequency sampling sensors and well-tuned controller parameters (p. 7).

## Transfer conditions

The legacy model is differentially driven and assumes strictly positive wheel effectiveness. Its result should not be extrapolated to complete wheel failure, another drive kinematics, or arbitrary fault profiles. Recovery is implicit tolerance rather than a system-level detector. Hardware sensing rates, gain tuning, actuator saturation, and the full theorem assumptions require separate validation before deployment.

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
| C5 | partial-support | moderate | Abstract, p. 1 | "The resulting control achieves trajectory tracking of the WMR with the predefined settling time and accuracy, against the actuator faults, the model uncertainties, and the disturbances." |
| C6 | qualifies | moderate | Abstract, p. 1 | "The theoretical findings are illustrated by a comparative simulation." |

## Page-cited excerpts

- **p. 1, Abstract.** "The resulting control achieves trajectory tracking of the WMR with the predefined settling time and accuracy, against the actuator faults, the model uncertainties, and the disturbances."
  The stated guarantee concerns tracking under the modeled actuator faults and assumptions.
- **p. 1, Abstract.** "The theoretical findings are illustrated by a comparative simulation."
  The validation setting limits conclusions about hardware reproducibility.

## Survey-usable statements

### Supported

- Mixed-gain adaptation with robust PPC addresses partial wheel-effectiveness loss in a differentially driven WMR model.
- The legacy numerical study illustrates prescribed tracking under designed fault profiles; all numerical citations require rechecking the PDF.

### Not supported

- The method detects faults or demonstrates system-level recovery on a physical robot; faults are tolerated implicitly in a numerical model.
- The controller exactly compensates faults or eliminates all error oscillation; the authors distinguish envelope control from exact compensation.
- The guarantee covers complete actuator loss; the recorded health-index range is strictly positive.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: English template conversion; actual abstract copied verbatim; no legacy verbatim excerpts to retain; C5 narrowed to modeled fault-tolerant control; numerical evidence and partial-loss assumption made explicit; numbers not re-verified
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

This article is concerned with the trajectory tracking control problem for the wheeled mobile robots (WMRs) subject to actuator faults. The challenge lies in the partial loss of effectiveness of the actuated wheels which results in the loss of strong controllability of the WMR, rendering the classical fault-tolerant control methods infeasible. To overcome this obstacle, a novel mixed-gain adaption technique is put forward and is skillfully combined with the robust prescribed performance control method. The resulting control achieves trajectory tracking of the WMR with the predefined settling time and accuracy, against the actuator faults, the model uncertainties, and the disturbances. Moreover, it exhibits significant simplicity, without parameter identification, function approximation, disturbance estimation, or fault estimation. The theoretical findings are illustrated by a comparative simulation.
