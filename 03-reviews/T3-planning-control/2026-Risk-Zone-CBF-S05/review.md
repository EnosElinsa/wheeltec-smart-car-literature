# Safety-Critical Control of Nonholonomic Vehicle Trajectory Tracking via Risk-Aware Zone Control Barrier Functions

## Metadata

| Field | Value |
|---|---|
| ID | S05 |
| Title | Safety-Critical Control of Nonholonomic Vehicle Trajectory Tracking via Risk-Aware Zone Control Barrier Functions |
| Authors | Ma, Yulu and Zeng, Qiang and Liu, Yan-Jun and Quan, Quan and Liu, Lei and Li, Shu and Zhu, Changqi and Zhang, Sai |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2026.3715807](https://doi.org/10.1109/tase.2026.3715807) |
| Official URL | https://ieeexplore.ieee.org/document/11618532/ |
| Theme folder | T3-planning-control |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2026-Risk-Zone-CBF-S05/paper.pdf` and `02-fulltext/T3-planning-control/2026-Risk-Zone-CBF-S05/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2026-Risk-Zone-CBF-S05/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: numerical
- evidence_all: numerical
- protocol_caveats: none
- platform_class: differential-drive
- platform: Numerically simulated nonholonomic wheeled-vehicle tracking with bounded inputs and obstacles; physical experiments remain future work (pp. 8, 10).
- boundary_platform: no
- degradation: actuator-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Feedback state, obstacle relative position and relative velocity; sensor/perception implementation is not validated
- compute: Quadratic-program safety filter in numerical simulations; physical deployment timing not established.
- compute_location: desktop-offline
- summary_result: Relative-motion geometric risk modifies constrained tracking commands in the modeled scenarios.
- summary_limitation: Experimental validation on physical platforms is identified as future work (p. 10).
- survey_included: yes
- verification_level: light

## Problem

Tracking recovery and obstacle avoidance can demand conflicting saturated control inputs.

## Mechanism

Combines input-output/sliding-mode tracking with a relative-motion risk-aware zone CBF safety filter and input-saturation handling (pp. 4-5, 10).

## Baselines and controls

Circular and lemniscate tracking scenarios compare avoidance/tracking behavior; no numerical superiority cells retained (p. 8).

## Platform and setup

Numerically simulated nonholonomic wheeled-vehicle tracking with bounded inputs and obstacles; physical experiments remain future work (pp. 8, 10).

## Evidence type and transfer

Strongest coded setting: `numerical`. The risk measure is geometric, not a calibrated collision probability; invariance depends on the model, available state and feasible bounded inputs.

## Sensors

Feedback state, obstacle relative position and relative velocity; sensor/perception implementation is not validated.

## Compute and latency

Quadratic-program safety filter in numerical simulations; physical deployment timing not established.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Experimental validation on physical platforms is identified as future work (p. 10).

## Transfer conditions

The risk measure is geometric, not a calibrated collision probability; invariance depends on the model, available state and feasible bounded inputs.

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

- **p. 10, Selected source passage.** "Future work will focus on experimental validation of the proposed method on physical platforms."
  Adds a saturation-aware control alternative without treating simulation as hardware safety evidence.

## Survey-usable statements

### Supported

- Relative-motion geometric risk modifies constrained tracking commands in the modeled scenarios. Adds a saturation-aware control alternative without treating simulation as hardware safety evidence.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. The risk measure is geometric, not a calibrated collision probability; invariance depends on the model, available state and feasible bounded inputs.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 5, 8, 10; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

This paper introduces a novel risk-aware zone control barrier function (RAZ-CBF) to solve the integrated problem of safety and precision tracking for nonholonomic wheeled vehicle under input saturation. The control architecture designs a nominal tracking controller (via input-output linearization) with a sliding mode term to expedite tracking recovery when the safety filter diverts control input. This safety filter is realized through the proposed RAZ-CBF, which efficiently quantifies collision risk using a geometric representation and is resolved in real-time via a quadratic programming (QP) framework. Crucially, the novel RAZ-CBF captures the geometric relationship between relative motion and relative position. The control commands are further processed through a saturation function to ensure stability under physical actuation limits. Simulations confirm accurate tracking and agile avoidance under input saturation, showing deployability for real systems.
