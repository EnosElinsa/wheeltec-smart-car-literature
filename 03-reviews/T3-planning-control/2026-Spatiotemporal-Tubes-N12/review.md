# Real-Time Spatiotemporal Tubes for Dynamic Unsafe Sets

## Metadata

| Field | Value |
|---|---|
| ID | N12 |
| Title | Real-Time Spatiotemporal Tubes for Dynamic Unsafe Sets |
| Authors | Ratnangshu Das, Siddhartha Upadhyay, Pushpak Jagtap |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2025.3645667](https://doi.org/10.1109/lra.2025.3645667) |
| Official URL | https://ieeexplore.ieee.org/document/11302778/ |
| Theme folder | T3-planning-control |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2026-Spatiotemporal-Tubes-N12/paper.pdf` and `02-fulltext/T3-planning-control/2026-Spatiotemporal-Tubes-N12/paper.md` (local only); [publisher BibTeX](../../../01-papers/T3-planning-control/2026-Spatiotemporal-Tubes-N12/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation, numerical
- protocol_caveats: none
- platform_class: omnidirectional
- platform: The target-time separation assumption conditions feasibility; full proofs and result-table cells were not audited.
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Robot state and online obstacle information
- compute: Selected hardware and randomized computational protocols; complete computation placement not retained
- compute_location: not-reported
- summary_result: Adaptive tubes provide prescribed-time reach-avoid control under stated dynamics and feasibility conditions.
- summary_limitation: Paths need not be shortest; global planning and explicit input constraints remain future work (pp. 7-8).
- survey_included: yes
- verification_level: light

## Problem

Reach-avoid control must react to moving unsafe sets within a prescribed time.

## Mechanism

The controller adapts the center and radius of a spherical spatiotemporal tube under pure-feedback dynamics, known input-coupling sign and bounded disturbances (pp. 2-3).

## Baselines and controls

An omnidirectional hardware example is separate from quadrotor simulation and randomized computational comparisons (p. 6).

## Platform and setup

The target-time separation assumption conditions feasibility; full proofs and result-table cells were not audited.

## Evidence type and transfer

The strongest inspected setting is `closed-loop-hardware`. Nonholonomic kinematics, saturation and attainable inputs must satisfy a compatible model before applying the reach-avoid guarantee.

## Sensors

Robot state and online obstacle information.

## Compute and latency

Selected hardware and randomized computational protocols; complete computation placement not retained.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- Paths need not be shortest; global planning and explicit input constraints remain future work (pp. 7-8).

## Transfer conditions

Nonholonomic kinematics, saturation and attainable inputs must satisfy a compatible model before applying the reach-avoid guarantee.

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

- **p. 8, Selected source passage.** "explicit input constraints"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Adaptive tubes provide prescribed-time reach-avoid control under stated dynamics and feasibility conditions.
- Nonholonomic kinematics, saturation and attainable inputs must satisfy a compatible model before applying the reach-avoid guarantee.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. Paths need not be shortest; global planning and explicit input constraints remain future work (pp. 7-8).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 2, 3, 6, 7, 8; Selected system/tube assumptions, case studies, comparison protocol and limitations; complete safety/convergence proofs and numerical tables not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—This** **paper** **presents** **a** **real-time** **control** **framework**
**for** **nonlinear** **pure-feedback** **systems** **with** **unknown** **dynamics** **to**
**satisfy reach-avoid-stay tasks within a prescribed time in dynamic**
**environments. To achieve this, we introduce a real-time spatiotem-**
**poral tube (STT) framework. An STT is defined as a time-varying**
**ball in the state space whose center and radius adapt online using**
**only** **real-time** **sensory** **input.** **A** **closed-form,** **approximation-free**
**control** **law** **is** **then** **derived** **to** **constrain** **the** **system** **output** **within**
**the** **STT,** **ensuring** **safety** **and** **task** **satisfaction.** **We** **provide** **for-**
**mal** **guarantees** **for** **obstacle** **avoidance** **and** **prescribed-time** **task**
**completion. The effectiveness and scalability of the framework are**
**demonstrated through simulations and hardware experiments on a**
**mobile robot and an aerial vehicle, navigating in cluttered dynamic**
**environments.**
