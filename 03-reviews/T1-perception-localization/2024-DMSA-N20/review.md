# DMSA - Dense Multi Scan Adjustment for LiDAR Inertial Odometry and Global Optimization

## Metadata

| Field | Value |
|---|---|
| ID | N20 |
| Title | DMSA - Dense Multi Scan Adjustment for LiDAR Inertial Odometry and Global Optimization |
| Authors | David Skuddis, Norbert Haala |
| Venue | 2024 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/icra57147.2024.10610818](https://doi.org/10.1109/icra57147.2024.10610818) |
| Official URL | https://ieeexplore.ieee.org/document/10610818/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2024-DMSA-N20/paper.pdf` and `02-fulltext/T1-perception-localization/2024-DMSA-N20/paper.md` (local only); [publisher BibTeX](../../../01-papers/T1-perception-localization/2024-DMSA-N20/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: Public construction/campus sequences and a bicycle-trailer recording provide offline pose comparisons with sequence-specific references.
- boundary_platform: yes
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: 3D LiDAR and IMU; dataset references and GNSS/inertial reference for the authors recording
- compute: Intel i9-12900K; processing takes 1.5-4 times recording duration in the reported implementation (p. 6)
- compute_location: desktop-offline
- summary_result: Dense multi-scan adjustment is evaluated offline with explicit sensor-adaptation and runtime qualifications.
- summary_limitation: Numerical Jacobians are identified as a runtime bottleneck; the implementation is slower than recording time (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Joint registration must handle overlap and dynamic geometry across multiple scans.

## Mechanism

DMSA fits common grid-cell distributions to multiple scans, reducing their joint scatter in continuous-trajectory and keyframe optimization (pp. 1-2).

## Baselines and controls

Baselines use defaults with a LiLi-OM preprocessing adaptation; unsupported sensor adaptation is N/A, distinct from a run failure (pp. 5-6).

## Platform and setup

Public construction/campus sequences and a bicycle-trailer recording provide offline pose comparisons with sequence-specific references.

## Evidence type and transfer

The strongest inspected setting is `recorded-robot-data`. Check sensor compatibility, initialization, reference alignment and runtime; dense optimization accuracy does not establish live control-loop feasibility.

## Sensors

3D LiDAR and IMU; dataset references and GNSS/inertial reference for the authors recording.

## Compute and latency

Intel i9-12900K; processing takes 1.5-4 times recording duration in the reported implementation (p. 6).

## Key quantitative results

- Processing takes 1.5-4 times recording duration on an Intel i9-12900K; numerical Jacobians are identified as the bottleneck (p. 6). No APE table cells were used.

## Stated limitations

- Numerical Jacobians are identified as a runtime bottleneck; the implementation is slower than recording time (p. 6).

## Transfer conditions

Check sensor compatibility, initialization, reference alignment and runtime; dense optimization accuracy does not establish live control-loop feasibility.

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

- **p. 6, Selected source passage.** "between 1.5 and 4 times the recording time"
  Interpret within the experimental setting and transfer conditions above.

- **p. 6, Selected source passage.** "we used the default settings"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Dense multi-scan adjustment is evaluated offline with explicit sensor-adaptation and runtime qualifications.
- Check sensor compatibility, initialization, reference alignment and runtime; dense optimization accuracy does not establish live control-loop feasibility.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. Numerical Jacobians are identified as a runtime bottleneck; the implementation is slower than recording time (p. 6).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 2, 5, 6; Selected dense-registration mechanism, sensor-platform description, benchmark/reference setup, runtime and conclusion; full optimization derivation and numerical error table cells not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **— We** **propose** **a** **new** **method** **for** **fine** **registering**
**multiple** **point** **clouds** **simultaneously.** **The** **approach** **is** **char-**
**acterized** **by** **being** **dense,** **therefore** **point** **clouds** **are** **not** **re-**
**duced** **to** **pre-selected** **features** **in** **advance.** **Furthermore,** **the**
**approach** **is** **robust** **against small** **overlaps and** **dynamic objects,**
**since** **no** **direct** **correspondences** **are** **assumed** **between** **point**
**clouds.** **Instead,** **all** **points** **are** **merged** **into** **a** **global** **point**
**cloud,** **whose** **scattering** **is** **then** **iteratively** **reduced.** **This** **is**
**achieved** **by** **dividing** **the** **global** **point** **cloud** **into** **uniform** **grid**
**cells** **whose** **contents** **are** **subsequently** **modeled** **by** **normal**
**distributions.** **We** **show** **that** **the** **proposed** **approach** **can** **be**
**used** **in** **a** **sliding** **window** **continuous** **trajectory** **optimization**
**combined** **with** **IMU** **measurements** **to** **obtain** **a** **highly** **accurate**
**and** **robust** **LiDAR** **inertial** **odometry** **estimation.** **Furthermore,**
**we** **show** **that** **the** **proposed** **approach** **is** **also** **suitable** **for**
**large** **scale** **keyframe** **optimization** **to** **increase** **accuracy.** **We**
**provide** **the** **source** **code** **and** **some** **experimental** **data** **on**
**https://github.com/davidskdds/DMSA_LiDAR_SLAM.git.**
