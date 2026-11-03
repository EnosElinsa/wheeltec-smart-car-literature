# Resilient Online Planning for Mobile Robots With Minimal Relaxation of Signal Temporal Logic Specifications

## Metadata

| Field | Value |
|---|---|
| ID | N15 |
| Title | Resilient Online Planning for Mobile Robots With Minimal Relaxation of Signal Temporal Logic Specifications |
| Authors | Ali Tevfik Buyukkocak, Derya Aksaray |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3563119](https://doi.org/10.1109/lra.2025.3563119) |
| Official URL | https://ieeexplore.ieee.org/document/10972058/ |
| Theme folder | T3-planning-control |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2025-Resilient-STL-N15/paper.pdf` and `02-fulltext/T3-planning-control/2025-Resilient-STL-N15/paper.md` (local only); [publisher BibTeX](../../../01-papers/T3-planning-control/2025-Resilient-STL-N15/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: numerical
- evidence_all: numerical
- protocol_caveats: none
- platform_class: none
- platform: Dynamic-obstacle simulations assess specification repair, not physical fault diagnosis or actuator repair.
- boundary_platform: yes
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Simulated robot states, obstacles and temporal-logic mission specification
- compute: MATLAB optimization and numerical Robotarium; global MILP burden grows with mission size
- compute_location: desktop-offline
- summary_result: Temporal-logic relaxation makes changes to the mission explicit after local correction becomes insufficient.
- summary_limitation: The scalability discussion distinguishes local quadratic programs from more costly global mixed-integer planning (p. 7).
- survey_included: yes
- verification_level: light

## Problem

A disrupted task may require both trajectory correction and an explicit change in mission requirements.

## Mechanism

Local CBF correction precedes global mixed-integer replanning; allowed relaxations include changed task windows and task removal (pp. 1, 6-7).

## Baselines and controls

Numerical case studies compare repair/replanning behavior; they do not constitute physical Robotarium trials (p. 6).

## Platform and setup

Dynamic-obstacle simulations assess specification repair, not physical fault diagnosis or actuator repair.

## Evidence type and transfer

The strongest inspected setting is `numerical`. Report which original requirements were relaxed or abandoned before treating a repaired mission as successful.

## Sensors

Simulated robot states, obstacles and temporal-logic mission specification.

## Compute and latency

MATLAB optimization and numerical Robotarium; global MILP burden grows with mission size.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- The scalability discussion distinguishes local quadratic programs from more costly global mixed-integer planning (p. 7).

## Transfer conditions

Report which original requirements were relaxed or abandoned before treating a repaired mission as successful.

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

- **p. 6, Selected source passage.** "We present numerical simulations to validate our approach"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Temporal-logic relaxation makes changes to the mission explicit after local correction becomes insufficient.
- Report which original requirements were relaxed or abandoned before treating a repaired mission as successful.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. The scalability discussion distinguishes local quadratic programs from more costly global mixed-integer planning (p. 7).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 6, 7, 8; Selected abstract, runtime correction/replanning, simulation setup, comparison/scalability discussion and conclusion. Complete proofs and numerical tables not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—We address the problem of resilient motion planning**
**for** **robots** **operating** **under** **Signal** **Temporal** **Logic** **(STL)** **speci-**
**fications** **in** **dynamic** **environments.** **In** **such** **settings,** **unforeseen**
**events—such as the emergence of dynamic obstacles—can render**
**the** **original** **STL** **specification** **infeasible.** **To** **address** **this,** **we** **pro-**
**pose a reactive framework that enables local corrections or global**
**replanning** **of** **the** **robot’s** **trajectory** **in** **response** **to** **these** **unex-**
**pected occurrences. When the original STL specification becomes**
**unsatisfiable,** **our** **framework** **involves** **minimally** **relaxing** **it** **by**
**extending/shrinking time windows or removing some tasks within**
**theuser’sallowance.Thisstrategyisdesignedtopreventarbitrarily**
**long delays in mission completion and to facilitate the satisfaction**
**of the mission with minimal temporal relaxation (TR). We present**
**theoretical results supporting our framework and demonstrate its**
**effectiveness through high-fidelity simulations.**
