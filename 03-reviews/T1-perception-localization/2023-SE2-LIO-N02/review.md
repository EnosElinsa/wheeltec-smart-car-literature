# Versatile LiDAR-Inertial Odometry With SE(2) Constraints for Ground Vehicles

## Metadata

| Field | Value |
|---|---|
| ID | N02 |
| Title | Versatile LiDAR-Inertial Odometry With SE(2) Constraints for Ground Vehicles |
| Authors | Jiaying Chen, Han Wang, Minghui Hu, Ponnuthurai Nagaratnam Suganthan |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2023 |
| Type | journal |
| DOI | [10.1109/lra.2023.3268584](https://doi.org/10.1109/lra.2023.3268584) |
| Official URL | https://ieeexplore.ieee.org/document/10105944/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2023-SE2-LIO-N02/paper.pdf` and `02-fulltext/T1-perception-localization/2023-SE2-LIO-N02/paper.md` (local only); [publisher BibTeX](../../../01-papers/T1-perception-localization/2023-SE2-LIO-N02/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: online-hardware
- evidence_all: online-hardware, recorded-robot-data
- protocol_caveats: joystick-driving
- platform_class: wheeled-unspecified
- platform: A teleoperated indoor AGV carries LiDAR and the NUC, with Vicon reference; outdoor evaluation uses GPS reference (pp. 6-8).
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: VLP-16 LiDAR and IMU; Vicon indoors and GPS outdoors as references
- compute: Intel NUC i5 on the AGV; complete sensing-to-actuation latency not assessed
- compute_location: onboard
- summary_result: Near-planar LiDAR-inertial estimation explicitly models out-of-plane perturbations.
- summary_limitation: The method can fail when ground slope varies significantly (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Ground vehicles offer near-planar motion priors while still undergoing vertical and attitude perturbations.

## Mechanism

SE2-LIO parameterizes pose on SE(2) and incorporates out-of-plane perturbations into an integrated noise term rather than setting them to zero (pp. 3-4).

## Baselines and controls

Selected indoor/outdoor estimator comparisons were read; numerical table cells and full ablations were not audited (pp. 6-8).

## Platform and setup

A teleoperated indoor AGV carries LiDAR and the NUC, with Vicon reference; outdoor evaluation uses GPS reference (pp. 6-8).

## Evidence type and transfer

The strongest inspected setting is `online-hardware`. Check whether the near-planar prior and perturbation model remain appropriate on the intended slopes; online estimation is distinct from autonomous navigation.

## Sensors

VLP-16 LiDAR and IMU; Vicon indoors and GPS outdoors as references.

## Compute and latency

Intel NUC i5 on the AGV; complete sensing-to-actuation latency not assessed.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- The method can fail when ground slope varies significantly (p. 8).

## Transfer conditions

Check whether the near-planar prior and perturbation model remain appropriate on the intended slopes; online estimation is distinct from autonomous navigation.

## Code and data

Availability and links beyond the publisher artifacts were not independently verified in this targeted reading.

## Version family

One publisher DOI is counted. A comprehensive preprint/extension-family search was not performed in this targeted reading.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | p. 8 | "fail when the slope of the ground varies significantly" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 8, Selected source passage.** "fail when the slope of the ground varies significantly"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Near-planar LiDAR-inertial estimation explicitly models out-of-plane perturbations.
- Check whether the near-planar prior and perturbation model remain appropriate on the intended slopes; online estimation is distinct from autonomous navigation.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. The method can fail when ground slope varies significantly (p. 8).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 3, 4, 6, 7, 8; Selected abstract, SE(2) perturbation model, indoor/outdoor protocols and conclusion; full Jacobian derivation, ablations and numerical table cells not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—LiDAR** **SLAM** **has** **become** **one** **of** **the** **major** **local-**
**ization** **systems** **for** **ground** **vehicles** **since** **LiDAR** **Odometry** **And**
**Mapping (LOAM). Many extension works on LOAM mainly lever-**
**age** **one** **specific** **constraint** **to** **improve** **the** **performance,** **e.g.,** **in-**
**formation from on-board sensors such as loop closure and inertial**
**state; prior conditions such as ground level and motion dynamics.**
**In** **many** **robotic** **applications,** **these** **conditions** **are** **often** **known**
**partially, hence a SLAM system can be a comprehensive problem**
**due** **to** **the** **existence** **of** **numerous** **constraints.** **Therefore,** **we** **can**
**achieve** **a** **better** **SLAM** **result** **by** **fusing** **them** **properly.** **In** **this**
**letter, we propose a hybrid LiDAR-inertial SLAM framework that**
**leverages** **both** **the** **on-board** **perception** **system** **and** **prior** **infor-**
**mation** **such** **as** **motion** **dynamics** **to** **improve** **localization** **perfor-**
**mance.** **In** **particular,** **we** **consider** **the** **case** **for** **ground** **vehicles,**
**which are commonly used for autonomous driving and warehouse**
**logistics.** **We** **present** **a** **computationally** **efficient** **LiDAR-inertial**
**odometry method that directly parameterizes ground vehicle poses**
**on SE(2). The out-of-SE(2) motion perturbations are not neglected**
**but** **incorporated** **into** **an** **integrated** **noise** **term** **of** **a** **novel** **SE(2)-**
**constraints** **model.** **For** **odometric** **measurement** **processing,** **we**
**propose** **a** **versatile,** **tightly** **coupled** **LiDAR-inertial** **odometry** **to**
**achieve** **better** **pose estimation** **than** **traditional** **LiDAR** **odometry.**
**Thorough** **experiments** **are** **performed** **to** **evaluate** **our** **proposed**
**method’s performance in different scenarios, including localization**
**for both indoor and outdoor environments. The proposed method**
**achieves superior performance in accuracy and robustness.**
