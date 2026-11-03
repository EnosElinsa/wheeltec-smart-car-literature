# Estimation of Slip Ratio and Side Slip Angle of Wheeled Planetary Rovers Based on Trace Imprint

## Metadata

| Field | Value |
|---|---|
| ID | N03 |
| Title | Estimation of Slip Ratio and Side Slip Angle of Wheeled Planetary Rovers Based on Trace Imprint |
| Authors | Nan Li, Junlong Guo, Liang Ding, Chenghua Tian, Chuan Zhou, Haibo Gao |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3581084](https://doi.org/10.1109/lra.2025.3581084) |
| Official URL | https://ieeexplore.ieee.org/document/11044427/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2025-Trace-Slip-N03/paper.pdf` and `02-fulltext/T1-perception-localization/2025-Trace-Slip-N03/paper.md` (local only); [publisher BibTeX](../../../01-papers/T1-perception-localization/2025-Trace-Slip-N03/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Rover wheel testbed experiments use preserved imprints on deformable sandy terrain; this is not closed-loop rover recovery.
- boundary_platform: no
- degradation: terrain, wheel-slip
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Camera images of lugged-wheel traces; testbed measurements provide reference slip
- compute: Laptop processing on a rover wheel testbed; onboard controller integration is future work
- compute_location: desktop-offline
- summary_result: Trace images support joint slip and sideslip estimation on a rover wheel testbed.
- summary_limitation: Imprint features fail at sufficiently high slip on sand, and the method excludes crushed stone and muddy terrain (pp. 7-8).
- survey_included: yes
- verification_level: light

## Problem

Longitudinal slip and lateral drift both matter on soft cross slopes.

## Mechanism

The estimator extracts trace units, contours and relative angles, then uses lug/soil imprint geometry to infer slip ratio and sideslip together (pp. 1, 3).

## Baselines and controls

Selected testbed and failure-boundary passages were read; result-table error cells were not transcribed (pp. 6-8).

## Platform and setup

Rover wheel testbed experiments use preserved imprints on deformable sandy terrain; this is not closed-loop rover recovery.

## Evidence type and transfer

The strongest inspected setting is `recorded-robot-data`. Usable lug geometry, camera visibility and preserved traces are measurement conditions; controller integration still needs verification.

## Sensors

Camera images of lugged-wheel traces; testbed measurements provide reference slip.

## Compute and latency

Laptop processing on a rover wheel testbed; onboard controller integration is future work.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- Imprint features fail at sufficiently high slip on sand, and the method excludes crushed stone and muddy terrain (pp. 7-8).

## Transfer conditions

Usable lug geometry, camera visibility and preserved traces are measurement conditions; controller integration still needs verification.

## Code and data

Availability and links beyond the publisher artifacts were not independently verified in this targeted reading.

## Version family

One publisher DOI is counted. A comprehensive preprint/extension-family search was not performed in this targeted reading.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | p. 7 | "when the wheel slip ratio exceeded 0.6 on sandy terrain" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 7, Selected source passage.** "when the wheel slip ratio exceeded 0.6 on sandy terrain"
  Interpret within the experimental setting and transfer conditions above.

- **p. 8, Selected source passage.** "not applicabletocrushedstone floors or muddy terrain"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Trace images support joint slip and sideslip estimation on a rover wheel testbed.
- Usable lug geometry, camera visibility and preserved traces are measurement conditions; controller integration still needs verification.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. Imprint features fail at sufficiently high slip on sand, and the method excludes crushed stone and muddy terrain (pp. 7-8).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 3, 6, 7, 8; Selected abstract, trace formation, image processing, rover testbed, failure boundary and conclusion; full soil-interaction derivation and numerical result tables not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—This** **letter** **proposes** **a** **method** **to** **estimate** **the** **wheel**
**slip ratio and side slip angle of wheeled rovers by processing images**
**of wheel trace imprints. The proposed method extracts structural**
**features** **from** **trace** **imprint** **images,** **such** **as** **the** **trace** **unit,** **trace**
**contour,** **and** **angle** **between** **the** **centerline** **of** **the** **trace** **unit** **and**
**contour.** **The** **relationships** **between** **the** **structural** **trace** **imprint**
**features** **and** **the** **wheel** **slip** **ratio** **and** **side** **slip** **angle** **have** **been**
**revealed after a study of the underlying mechanism of trace imprint**
**formation,withconsiderationofthekinematicsofthewheellugand**
**lug-soil interaction.** **These relationships are then** **used to** **estimate**
**wheel** **slip** **ratio** **and** **side** **slip** **angle.** **Compared** **with** **the** **existing**
**estimationmethods,theproposedmethodcanestimatelongitudinal**
**slippage** **and** **lateral** **drift** **simultaneously** **that** **typically** **occur** **in**
**planetary rovers during traverse of cross slopes. The effectiveness**
**of** **the** **proposed** **method** **has** **been** **demonstrated** **by** **experiments**
**using a rover wheel test-bed under various conditions.**
