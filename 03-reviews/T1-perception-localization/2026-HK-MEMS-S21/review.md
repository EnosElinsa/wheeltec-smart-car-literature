# HK‐MEMS, a Multi‐Sensor Data Set With MEMS LiDAR on Degenerate and Dynamic Urban Scenarios

## Metadata

| Field | Value |
|---|---|
| ID | S21 |
| Title | HK‐MEMS, a Multi‐Sensor Data Set With MEMS LiDAR on Degenerate and Dynamic Urban Scenarios |
| Authors | Ruan, Jianyuan and Zhang, Dan |
| Venue | Journal of Field Robotics |
| Year | 2026 |
| Type | journal |
| DOI | [10.1002/rob.70136](https://doi.org/10.1002/rob.70136) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.70136 |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-HK-MEMS-S21/paper.pdf` and `02-fulltext/T1-perception-localization/2026-HK-MEMS-S21/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2026-HK-MEMS-S21/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-resource
- evidence_all: dataset-resource
- protocol_caveats: none
- platform_class: mixed
- platform: Handheld rig, mobile robot and public buses; multiple carriers and reference types (pp. 1, 7, 10).
- boundary_platform: yes
- degradation: lidar-degeneracy, dynamic-objects, gnss-denial
- degradation_observed: none
- evaluation_primary: designed-degradation
- evaluation_all: residual, designed-degradation
- sensors: Robosense M1 MEMS and Ouster LiDARs, cameras, IMUs, GNSS/INS; bus-route and barometric references
- compute: Intel NUC is the acquisition computer; selected passages do not establish the computation placement of every benchmark (p. 7).
- compute_location: not-reported
- summary_result: Conditioned urban benchmarks expose sensor-pattern and geometric limitations of existing estimators.
- summary_limitation: Bus-route references have no timestamps; the paper uses geometric alignment and warns that one-sided path RMSE can conceal shortened failed trajectories (pp. 10, 16).
- survey_included: yes
- verification_level: light

## Problem

MEMS scanning patterns and urban degeneracy/dynamics are underrepresented by mechanical-LiDAR benchmarks.

## Mechanism

Provides a calibrated multi-sensor acquisition suite and condition-grouped benchmarks; adapts existing estimators to MEMS timing (pp. 7, 14-15).

## Baselines and controls

F-LOAM, SLAMesh, FAST-LIO2 and LIO-SAM, with LIO-SAM loop closure disabled for the reported comparison (pp. 14-15).

## Platform and setup

Handheld rig, mobile robot and public buses; multiple carriers and reference types (pp. 1, 7, 10).

## Evidence type and transfer

Strongest coded setting: `dataset-resource`. Separate route shape, altitude and time-aligned pose reference; do not treat lane-level route agreement as centimeter-scale trajectory accuracy.

## Sensors

Robosense M1 MEMS and Ouster LiDARs, cameras, IMUs, GNSS/INS; bus-route and barometric references.

## Compute and latency

Intel NUC is the acquisition computer; selected passages do not establish the computation placement of every benchmark (p. 7).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Bus-route references have no timestamps; the paper uses geometric alignment and warns that one-sided path RMSE can conceal shortened failed trajectories (pp. 10, 16).

## Transfer conditions

Separate route shape, altitude and time-aligned pose reference; do not treat lane-level route agreement as centimeter-scale trajectory accuracy.

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

- **p. 10, Selected source passage.** "it does not contain timestamps."
  Changes evaluation guidance: reference completeness and failed-trajectory coverage must accompany pose-error summaries.

## Survey-usable statements

### Supported

- Conditioned urban benchmarks expose sensor-pattern and geometric limitations of existing estimators. Changes evaluation guidance: reference completeness and failed-trajectory coverage must accompany pose-error summaries.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Separate route shape, altitude and time-aligned pose reference; do not treat lane-level route agreement as centimeter-scale trajectory accuracy.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 7, 10, 14, 15, 16, 22; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Public data sets are essential for progress in autonomous robotics. The advancements in sensor technology and evolving application scenarios create ongoing demands for updated benchmarking resources. This paper introduces the HK-MEMS Data set, the first public data set to provide automotive-grade MEMS LiDAR (Micro-Electromechanical Systems Light Detection and Ranging) data in complex urban environments. While MEMS LiDAR has emerged as a cost-effective and durable alternative to mechanical LiDAR for autonomous vehicles, the lack of data sets hinders corresponding research. Our work targets the under-explored robustness challenge of Simultaneous Localization and Mapping (SLAM) in degenerate and dynamic urban scenarios. The data set integrates multi-modal sensors—including MEMS LiDAR, stereo cameras, GNSS, and an Inertial Navigation System (INS)—collected across three platforms: a handheld device, a mobile robot, and public buses exhibiting real-world driving behaviors. Over 187 min (75.4 km) of data were captured, spanning diverse urban scenarios with dynamic objects and degenerate scenarios, such as tunnels, highways, shopping areas, and subway stations. Comprehensive evaluations of this benchmark's state-of-the-art SLAM algorithms reveal significant performance degradation in degenerate and dynamic scenes, highlighting unresolved challenges in real-world deployment. The HK-MEMS Data set provides a comprehensive resource for evaluating emerging MEMS LiDAR technology and establishes a challenging benchmark for advancing robust SLAM methodologies in urban navigation. The data set is openly available at: https://github.com/RuanJY/HK_MEMS_Dataset.
