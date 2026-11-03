# Unveiling Non-Reproducibility in LiDAR-Inertial Odometry

## Metadata

| Field | Value |
|---|---|
| ID | N04 |
| Title | Unveiling Non-Reproducibility in LiDAR-Inertial Odometry |
| Authors | Hongqian Huang, Meng Zhang, Jianchen Hu, Xiaohong Guan |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2025.3636030](https://doi.org/10.1109/lra.2025.3636030) |
| Official URL | https://ieeexplore.ieee.org/document/11266943/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2026-LIO-Reproducibility-N04/paper.pdf` and `02-fulltext/T6-reliability-deployment/2026-LIO-Reproducibility-N04/paper.md` (local only); [publisher BibTeX](../../../01-papers/T6-reliability-deployment/2026-LIO-Reproducibility-N04/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: localization-mapping
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: Repeated runs of recorded sequences test implementation repeatability, including low-channel and degenerate scenes; they are not independent physical missions.
- boundary_platform: yes
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR and IMU recordings with varied channel counts and scene geometry
- compute: Controlled desktop playback, queue/subscriber handling, implementation variants and arithmetic-order experiments
- compute_location: desktop-offline
- summary_result: Repeated playback exposes implementation-dependent estimator variability on identical recorded inputs.
- summary_limitation: A rigorous mathematical explanation of the observed causal relationship remains future work (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Repeated execution on the same input can yield different LiDAR-inertial estimates.

## Mechanism

The authors isolate implementation nondeterminism with repeated playback, deterministic variants and changes in floating-point operation order (pp. 5-8).

## Baselines and controls

Subscribers are initialized before playback and buffering limits frame loss; parameters are empirically tuned rather than uniformly left at defaults (p. 5).

## Platform and setup

Repeated runs of recorded sequences test implementation repeatability, including low-channel and degenerate scenes; they are not independent physical missions.

## Evidence type and transfer

The strongest inspected setting is `dataset-playback`. Disclose queue handling, numerical libraries, tuning and repeatability before attributing a small single-run difference to an algorithmic change.

## Sensors

LiDAR and IMU recordings with varied channel counts and scene geometry.

## Compute and latency

Controlled desktop playback, queue/subscriber handling, implementation variants and arithmetic-order experiments.

## Key quantitative results

- Each system/sequence experiment was repeated 30 times on the same recording; this is an execution-repeatability count, not a count of independent robot missions (p. 5).

## Stated limitations

- A rigorous mathematical explanation of the observed causal relationship remains future work (p. 8).

## Transfer conditions

Disclose queue handling, numerical libraries, tuning and repeatability before attributing a small single-run difference to an algorithmic change.

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

- **p. 5, Selected source passage.** "each experiment was repeated 30 times"
  Interpret within the experimental setting and transfer conditions above.

- **p. 8, Selected source passage.** "a rigorous mathematical explanation of this causal relationship has yet to be established"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Repeated playback exposes implementation-dependent estimator variability on identical recorded inputs.
- Disclose queue handling, numerical libraries, tuning and repeatability before attributing a small single-run difference to an algorithmic change.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. A rigorous mathematical explanation of the observed causal relationship remains future work (p. 8).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 5, 6, 7, 8; Selected abstract, repeatability protocol, implementation ablations, hardware-dependent arithmetic experiment and conclusion; full implementation audit and numerical tables not independently reproduced. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—This** **letter** **presents** **empirical** **research** **on** **the** **non-**
**reproducibility** **of** **light** **detection** **and** **ranging** **sensor** **(LiDAR)-**
**inertial** **odometry** **(LIO)** **systems.** **Although** **the** **LIO** **community**
**has** **made** **commendable** **efforts** **toward** **reproducible** **localization**
**accuracy,** _**noteworthy**_ **non-reproducibility remains, thus hindering**
**a** **fair** **evaluation** **of** **method** **effectiveness.** **To** **better** **understand**
**such** **non-reproducibility,** **we** **first** **define** **non-reproducibility** **and**
**introduce** **a** **quantitative** **criterion** **to** **identify** **noteworthy** **non-**
**reproducibility. We then propose five significant non-deterministic**
**implementations** **that** **are** **included** **in** **state-of-the-art** **LIO** **sys-**
**tems** **and** **present** **solutions** **for** **modifying** **these** **non-deterministic**
**implementations** **into** **deterministic** **ones.** **A** **general** **procedure** **is**
**also introduced to identify and pinpoint non-deterministic imple-**
**mentations,** **regardless** **of** **whether** **they** **are** **covered** **in** **this** **let-**
**ter. Extensive experiments demonstrate that the non-deterministic**
**implementations** **are** **the** **major** **or** **potentially** **sole** **causes** **of** **non-**
**reproducibility under constant experimental conditions. Addition-**
**ally,** **the** **non-reproducibility** **is** **noteworthy** **in** **datasets** **obtained**
**from low-vertical-resolution LiDARs or recorded in geometrically**
**degenerate scenes.**
