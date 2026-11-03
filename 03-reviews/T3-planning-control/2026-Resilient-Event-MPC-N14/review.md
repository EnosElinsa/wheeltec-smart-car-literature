# Resilient Memory-Event-Triggered Predictive Tracking Control for Unmanned Ground Vehicle

## Metadata

| Field | Value |
|---|---|
| ID | N14 |
| Title | Resilient Memory-Event-Triggered Predictive Tracking Control for Unmanned Ground Vehicle |
| Authors | Zhijian Hu, Renjie Ma, Su Zhang, Hao Wang, Xinxin Liu, Dong Zhao |
| Venue | IEEE Transactions on Intelligent Vehicles |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tiv.2026.3662786](https://doi.org/10.1109/tiv.2026.3662786) |
| Official URL | https://ieeexplore.ieee.org/document/11386870/ |
| Theme folder | T3-planning-control |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2026-Resilient-Event-MPC-N14/paper.pdf` and `02-fulltext/T3-planning-control/2026-Resilient-Event-MPC-N14/paper.md` (local only); [publisher BibTeX](../../../01-papers/T3-planning-control/2026-Resilient-Event-MPC-N14/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: fault-recovery-deployment
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, numerical
- protocol_caveats: offboard-compute
- platform_class: ackermann
- platform: The validation is explicitly HIL, not a fully onboard physical degradation trial; the vocabulary has no dedicated HIL category, so closed-loop-hardware is qualified here, consistently with F02.
- boundary_platform: no
- degradation: model-error
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Vehicle feedback in a hardware-in-the-loop Ackermann architecture
- compute: Industrial Intel i7 hosts control; Jetson Nano/STM32 belong to vehicle low-level hardware; HIL sampling period is one second
- compute_location: offboard-local
- summary_result: Memory-triggered MPC reduces repeated solves within a bounded-silence HIL tracking design.
- summary_limitation: The vehicle model assumes no slip and neglects height/tilt effects (p. 2).
- survey_included: yes
- verification_level: light

## Problem

Repeated predictive-control optimization consumes computation even when a new solution is unnecessary.

## Mechanism

Memory-based triggering uses past information and caps the maximum silent interval between MPC updates under a low-speed no-slip vehicle model (pp. 1-2, 7).

## Baselines and controls

Hardware-in-the-loop comparisons with and without triggering were read; physical cyberattack trials and plot values were not verified (pp. 7-9).

## Platform and setup

The validation is explicitly HIL, not a fully onboard physical degradation trial; the vocabulary has no dedicated HIL category, so closed-loop-hardware is qualified here, consistently with F02.

## Evidence type and transfer

The strongest inspected setting is `closed-loop-hardware`. Fewer optimizer calls do not establish proportional energy savings; report control age, actual runtime and computation placement.

## Sensors

Vehicle feedback in a hardware-in-the-loop Ackermann architecture.

## Compute and latency

Industrial Intel i7 hosts control; Jetson Nano/STM32 belong to vehicle low-level hardware; HIL sampling period is one second.

## Key quantitative results

- The HIL sampling period is one second; this describes the experimental loop, not average MPC solve time or physical attack performance (p. 8).

## Stated limitations

- The vehicle model assumes no slip and neglects height/tilt effects (p. 2).

## Transfer conditions

Fewer optimizer calls do not establish proportional energy savings; report control age, actual runtime and computation placement.

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

- **p. 7, Selected source passage.** "hosts the control algorithms"
  Interpret within the experimental setting and transfer conditions above.

- **p. 8, Selected source passage.** "For the experimental validation in the HIL"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Memory-triggered MPC reduces repeated solves within a bounded-silence HIL tracking design.
- Fewer optimizer calls do not establish proportional energy savings; report control age, actual runtime and computation placement.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. The vehicle model assumes no slip and neglects height/tilt effects (p. 2).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 2, 7, 8, 9; Selected contribution, no-slip vehicle assumptions, event-update trade-off, HIL architecture and conclusion; complete recursive-feasibility proof and numeric performance plots not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—Albeit** **model** **predictive** **control** **(MPC)** **has** **been**
**broadlyappliedforthetrajectorytrackingofunmannedgroundve-**
**hicles (UGVs), certain issues still remain to be further investigated,**
**particularly with regard to the tracking stability analysis and com-**
**putational efficiency. This paper formulates the trajectory tracking**
**for** **Ackerman-steering** **UGV** **as** **an** **optimization-constrained** **con-**
**trol** **problem** **within** **the** **MPC** **framework,** **incorporating** **stability**
**analysis** **through** **the** **specification** **of** **terminal** **ingredients.** **To** **re-**
**lax** **the** **computational** **burdens** **of** **MPC** **in** **network** **transmission,**
**this** **paper** **integrates** **historical** **triggered** **signals** **into** **the** **event-**
**triggered** **scheme** **synthesis,** **ensuring** **that** **critical** **moments,** **such**
**as peaks and troughs in the system dynamics, are triggered. Addi-**
**tionally, an upper limit on untriggered signals is imposed to safe-**
**guard** **against** **potential** **abnormal** **behaviors** **on** **event** **generators.**
**The effectiveness of the proposed resilient memory-event-triggered**
**MPC** **algorithm** **is** **validated** **through** **both** **computer** **simulations**
**and** **hardware** **experiments** **of** **tracking** **circular** **and** **“8”-shaped**
**trajectories.**
