# Predictive Data Acquisition for Lifelong Visual Teach, Repeat and Learn

## Metadata

| Field | Value |
|---|---|
| ID | N06 |
| Title | Predictive Data Acquisition for Lifelong Visual Teach, Repeat and Learn |
| Authors | Tomáš Rouček, Zdeněk Rozsypálek, Jan Blaha, Jiří Ulrich, Tomáš Krajník |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3421193](https://doi.org/10.1109/lra.2024.3421193) |
| Official URL | https://ieeexplore.ieee.org/document/10578334/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2024-Predictive-Data-N06/paper.pdf` and `02-fulltext/T6-reliability-deployment/2024-Predictive-Data-N06/paper.md` (local only); [publisher BibTeX](../../../01-papers/T6-reliability-deployment/2024-Predictive-Data-N06/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Datasets collected by real robots include revisits at later dates; elapsed calendar time is not uninterrupted autonomous service.
- boundary_platform: no
- degradation: none
- degradation_observed: scene-change
- evaluation_primary: residual
- evaluation_all: residual
- sensors: Visual observations from repeated robot traversals
- compute: Recorded-data learning/evaluation; complete autonomous acquisition scheduling not established
- compute_location: desktop-offline
- summary_result: Ambiguity-guided acquisition supports visual representation maintenance on recorded revisits.
- summary_limitation: Locations never revisited create acquisition blind spots; scheduling both where and when to acquire data remains future work (pp. 7-8).
- survey_included: yes
- verification_level: light

## Problem

Visual route representations need useful additional examples as appearance changes.

## Mechanism

Visual matching ambiguity guides selective acquisition of training observations in a teach-repeat-learn pipeline (pp. 1, 5, 7-8).

## Baselines and controls

Witham Wharf and Cestlice revisits provide recorded-data comparisons; numerical performance tables and significance tests were not audited (p. 5).

## Platform and setup

Datasets collected by real robots include revisits at later dates; elapsed calendar time is not uninterrupted autonomous service.

## Evidence type and transfer

The strongest inspected setting is `recorded-robot-data`. Check access, task constraints, acquisition time and maintenance cost before inferring deployment availability from matching improvements.

## Sensors

Visual observations from repeated robot traversals.

## Compute and latency

Recorded-data learning/evaluation; complete autonomous acquisition scheduling not established.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- Locations never revisited create acquisition blind spots; scheduling both where and when to acquire data remains future work (pp. 7-8).

## Transfer conditions

Check access, task constraints, acquisition time and maintenance cost before inferring deployment availability from matching improvements.

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

- **p. 8, Selected source passage.** "pipeline is presented using datasets collected by real robots"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Ambiguity-guided acquisition supports visual representation maintenance on recorded revisits.
- Check access, task constraints, acquisition time and maintenance cost before inferring deployment availability from matching improvements.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. Locations never revisited create acquisition blind spots; scheduling both where and when to acquire data remains future work (pp. 7-8).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 5, 7, 8; Selected abstract, dataset/comparison protocol, deployment discussion and conclusion; complete training pipeline, result tables and significance tests not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—Nowadays, robots can operate in environments which**
**are not tailored for them. This allows their deployments in changing**
**and** **human-populated** **environments,** **which** **recent** **advances** **in**
**machine learning methods enabled. The efficiency of these methods**
**is** **largely** **determined** **by** **the** **quality** **of** **their** **training** **data.** **An**
**up-to-date** **and** **well-balanced** **training** **dataset** **is** **paramount** **for**
**achieving robust robot operation. To achieve long-term operation,**
**the robot has to deal with perpetual environmental changes, forcing**
**it to keep its models up-to-date. We present an exploration method**
**allowing** **a** **mobile** **robot** **to** **gather** **high-quality** **data** **to** **update** **its**
**models both while performing its duties and when idle, maximizing**
**effectivity. The robot evaluates the quality of the data gathered in**
**the past and based on that, it creates preferences which influence**
**how often these locations are visited. This exploration method was**
**integrated with a self-supervised visual teach-and-repeat pipeline.**
**We** **show** **the** **precision** **and** **robustness** **of** **visual-based** **navigation**
**to** **improve** **when** **using** **machine-learned** **models** **trained** **by** **our**
**exploration method. Our research resulted in a robotic navigation**
**system that can not only annotate its training data but also ensure**
**that its training dataset is balanced and up-to-date.**
