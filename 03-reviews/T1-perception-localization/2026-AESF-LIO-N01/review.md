# AESF-LIO: Adaptive Error-State Fusion LiDAR-Inertial Odometry for Ground Vehicles in Structured Environments

## Metadata

| Field | Value |
|---|---|
| ID | N01 |
| Title | AESF-LIO: Adaptive Error-State Fusion LiDAR-Inertial Odometry for Ground Vehicles in Structured Environments |
| Authors | Zhishuai Huang, Chao Sun, Jianghao Leng, Bo Wang |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3685919](https://doi.org/10.1109/lra.2026.3685919) |
| Official URL | https://ieeexplore.ieee.org/document/11488584/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-AESF-LIO-N01/paper.pdf` and `02-fulltext/T1-perception-localization/2026-AESF-LIO-N01/paper.md` (local only); [publisher BibTeX](../../../01-papers/T1-perception-localization/2026-AESF-LIO-N01/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: road-vehicle
- platform: Simulation, public sequences and real-vehicle data support an estimator comparison; no controller consuming the estimate was established by this reading.
- boundary_platform: yes
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: 3D LiDAR and IMU
- compute: Selected runtime discussion; evaluation placement treated as desktop processing, not a demonstrated navigation control loop
- compute_location: desktop-offline
- summary_result: Adaptive fusion separates ground and non-ground corrections in estimator evaluations.
- summary_limitation: Validation mainly covers relatively flat urban environments (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Imbalanced ground and non-ground geometry can bias a joint point-to-plane pose update.

## Mechanism

AESF-LIO estimates ground and non-ground error-state corrections separately and adaptively weights their fusion, including roll and pitch contributions (p. 5).

## Baselines and controls

The selected evaluation compares LiDAR-inertial estimators across simulation, public datasets and vehicle recordings; individual error cells and ablations were not audited (pp. 5, 8).

## Platform and setup

Simulation, public sequences and real-vehicle data support an estimator comparison; no controller consuming the estimate was established by this reading.

## Evidence type and transfer

The strongest inspected setting is `recorded-robot-data`. Check segmentation quality and geometric rank; reweighting existing LiDAR returns supplies no independent sensing channel.

## Sensors

3D LiDAR and IMU.

## Compute and latency

Selected runtime discussion; evaluation placement treated as desktop processing, not a demonstrated navigation control loop.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- Validation mainly covers relatively flat urban environments (p. 8).

## Transfer conditions

Check segmentation quality and geometric rank; reweighting existing LiDAR returns supplies no independent sensing channel.

## Code and data

Availability and links beyond the publisher artifacts were not independently verified in this targeted reading.

## Version family

One publisher DOI is counted. A comprehensive preprint/extension-family search was not performed in this targeted reading.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | p. 8 | "mainly validated in relatively flat urban environments" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 8, Selected source passage.** "mainly validated in relatively flat urban environments"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Adaptive fusion separates ground and non-ground corrections in estimator evaluations.
- Check segmentation quality and geometric rank; reweighting existing LiDAR returns supplies no independent sensing channel.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. Validation mainly covers relatively flat urban environments (p. 8).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 5, 8; Selected abstract, adaptive weighting, evaluation setup, runtime discussion and conclusion; complete derivation, ablations and numerical tables not audited. No performance numbers retained. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—In** **LiDAR-based** **Simultaneous** **Localization** **and**
**Mapping (SLAM) systems for vehicles, the point-to-plane Iterative**
**Closest Point (ICP) method is widely used for scan matching. This**
**approach** **incorporates** **all** **planar** **points** **into** **a** **single** **objective**
**function** **for** **optimization,** **yet** **does** **not** **explicitly** **distinguish** **the**
**differences in the constraints that ground and non-ground points**
**impose** **on** **the** **pose** **variables.** **Ground** **points** **primarily** **constrain**
**the** **z** **translation** **as** **well** **as** **roll** **and** **pitch,** **whereas** **non-ground**
**points** **predominantly** **constrain** **horizontal** **translation** **and** **yaw.**
**The** **constraints** **provided** **by** **non-ground** **points** **on** **the** **z** **transla-**
**tion,** **roll,** **and** **pitch** **depend** **on** **their** **spatial** **distribution** **and** **can**
**be** **weak** **for** **z** **in** **environments** **dominated** **by** **vertical** **structures.**
**When one point type dominates in number while providing weak**
**constraints** **on** **certain** **pose** **variables,** **the** **joint** **optimization** **may**
**become** **biased,** **resulting** **in** **insufficient** **refinement** **of** **the** **weakly**
**constrained variables and degraded odometry accuracy. To address**
**this** **issue** **within** **a** **point-to-plane** **ICP** **framework,** **this** **letter** **pro-**
**poses a LiDAR-inertial odometry system that separately minimizes**
**point-to-plane** **residuals** **for** **ground** **and** **non-ground** **points** **and**
**adaptively fuses their corresponding error states to improve pose**
**accuracy.** **The system** **employs** **ground** **segmentation** **to** **divide the**
**point** **cloud** **into** **ground** **points** **and** **non-ground** **points;** **it** **then**
**computes the error state vectors for ground and non-ground points**
**separately and updates the pose using an adaptive weighted fusion**
**strategy.** **Experiments** **in** **simulation,** **on** **public** **datasets,** **and** **in**
**real-vehicle** **experiments** **demonstrate** **that** **the** **proposed** **method**
**significantly** **improves** **accuracy** **compared** **with** **advanced** **SLAM**
**baselines.**
