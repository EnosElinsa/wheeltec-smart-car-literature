# Autonomous Navigation With Online Replanning and Recovery Behaviors for Wheeled-Legged Robots Using Behavior Trees

## Metadata

| Field | Value |
|---|---|
| ID | N17 |
| Title | Autonomous Navigation With Online Replanning and Recovery Behaviors for Wheeled-Legged Robots Using Behavior Trees |
| Authors | Alessio De Luca, Luca Muratore, Nikos G. Tsagarakis |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2023 |
| Type | journal |
| DOI | [10.1109/lra.2023.3313052](https://doi.org/10.1109/lra.2023.3313052) |
| Official URL | https://ieeexplore.ieee.org/document/10243138/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2023-BT-Recovery-N17/paper.pdf` and `02-fulltext/T6-reliability-deployment/2023-BT-Recovery-N17/paper.md` (local only); [publisher BibTeX](../../../01-papers/T6-reliability-deployment/2023-BT-Recovery-N17/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: mixed
- platform: CENTAURO hardware and simulation combine wheeled and stepping primitives; retained-scenario simulation results have a conditional denominator.
- boundary_platform: yes
- degradation: terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Perception/elevation maps, wheel-contact and planner-state information
- compute: Onboard hierarchical mapping/planning; hardware uses slower motion and lower local-map rate than simulation
- compute_location: onboard
- summary_result: Behavior-tree supervision executes failure-specific recovery on a hybrid wheeled-legged robot.
- summary_limitation: Persistent planning failures can require human intervention (p. 5).
- survey_included: yes
- verification_level: light

## Problem

Hybrid wheeled-legged navigation needs different responses to contact, planning and stepping failures.

## Mechanism

Behavior-tree supervision selects stopping, wheel repositioning, replanning, reversal and support-polygon reshaping for four named failure modes (pp. 2-5).

## Baselines and controls

Generated simulations exclude infeasible obstacles and failed or excessively slow global plans; physical trials use different motion/map rates (pp. 5-7).

## Platform and setup

CENTAURO hardware and simulation combine wheeled and stepping primitives; retained-scenario simulation results have a conditional denominator.

## Evidence type and transfer

The strongest inspected setting is `closed-loop-hardware`. Compare recovery actions only when the chassis can execute them; conventional wheels cannot inherit stepping or support reshaping.

## Sensors

Perception/elevation maps, wheel-contact and planner-state information.

## Compute and latency

Onboard hierarchical mapping/planning; hardware uses slower motion and lower local-map rate than simulation.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 7).

## Stated limitations

- Persistent planning failures can require human intervention (p. 5).

## Transfer conditions

Compare recovery actions only when the chassis can execute them; conventional wheels cannot inherit stepping or support reshaping.

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
| C5 | partial-support | moderate | p. 5 | "require human intervention to release it" |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 6, Selected source passage.** "were discarded from the results presented in this section"
  Interpret within the experimental setting and transfer conditions above.

- **p. 5, Selected source passage.** "require human intervention to release it"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Behavior-tree supervision executes failure-specific recovery on a hybrid wheeled-legged robot.
- Compare recovery actions only when the chassis can execute them; conventional wheels cannot inherit stepping or support reshaping.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. Persistent planning failures can require human intervention (p. 5).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 2, 3, 4, 5, 6, 7; Selected architecture, four recovery triggers/actions, simulated-scene exclusions, hardware protocol and human-intervention boundary; numeric result tables and whole-system safety not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—Performing** **autonomous** **navigation** **in** **cluttered** **and**
**unstructuredterrainsstillremainsachallengingtaskforleggedand**
**wheeled mobile robots. To accomplish such a task, online planners**
**shall incorporate new terrain information perceived while the robot**
**is moving within its environment. While hybrid mobility robots of-**
**fer high flexibility in traversing challenging terrains by leveraging**
**the advantages of both wheeled and legged locomotion, the effective**
**hybrid planning of the mobility actions that transparently combine**
**both** **modes** **of** **locomotion** **has** **not** **been** **extensively** **explored.** **In**
**this work, we present a hierarchical online hybrid primitive-based**
**planner** **for** **autonomous** **navigation** **with** **wheeled-legged** **robots.**
**The** **framework** **is** **handled** **by** **a** **Behavior** **Tree** **(BT)** **and** **it** **takes**
**into account recovery methods to deal with possible failures during**
**the execution of the navigation/mobility plan. The framework was**
**evaluated in multiple irregular and heavily cluttered simulated en-**
**vironments randomly generated and in real-world trials, using the**
**CENTAURO robot platform. With these experiments, we demon-**
**strated autonomous capabilities without any human intervention,**
**even in case of collision or planner failures.**
