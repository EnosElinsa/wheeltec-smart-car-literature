# Visual‐Inertial SLAM for Unstructured Outdoor Environments: Benchmarking the Benefits and Computational Costs of Loop Closing

## Metadata

| Field | Value |
|---|---|
| ID | S19 |
| Title | Visual‐Inertial SLAM for Unstructured Outdoor Environments: Benchmarking the Benefits and Computational Costs of Loop Closing |
| Authors | Schmidt, Fabian and Blessing, Constantin and Enzweiler, Markus and Valada, Abhinav |
| Venue | Journal of Field Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1002/rob.22581](https://doi.org/10.1002/rob.22581) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.22581 |
| Theme folder | T6-reliability-deployment |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-SLAM-Loop-Costs-S19/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-SLAM-Loop-Costs-S19/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-SLAM-Loop-Costs-S19/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: localization-mapping
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Authors-recorded UGV garden/park perimeter and lane sequences with seasonal variation (p. 3).
- boundary_platform: no
- degradation: visual-degradation, compute-limit
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: RealSense T265 stereo/IMU; Leica total station supplies position-only reference
- compute: Offline Intel i9-13900HX/64 GB Docker/ROS Noetic evaluation with frame-rate and loop-closure configurations (p. 7).
- compute_location: desktop-offline
- summary_result: Loop-closing benefits and compute demand depend on estimator, route and input rate.
- summary_limitation: Evaluation excludes failed/insufficient-coverage trajectories before mean ATE/RPE; this conditions reported errors on surviving runs (pp. 6-7).
- survey_included: yes
- verification_level: light

## Problem

Loop closure changes both accuracy and resource demand in unstructured outdoor visual-inertial SLAM.

## Mechanism

Benchmarks traditional/learned pipelines with loop closure and input-frame-rate controls; frontend parameters tuned to the test conditions (pp. 6-7).

## Baselines and controls

ORB-SLAM3, VINS-Fusion, OpenVINS variants, Kimera, SVO Pro, HFNet-SLAM and AirSLAM (pp. 1, 6).

## Platform and setup

Authors-recorded UGV garden/park perimeter and lane sequences with seasonal variation (p. 3).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Report failures alongside survivor accuracy; position-only reference cannot independently verify full orientation error.

## Sensors

RealSense T265 stereo/IMU; Leica total station supplies position-only reference.

## Compute and latency

Offline Intel i9-13900HX/64 GB Docker/ROS Noetic evaluation with frame-rate and loop-closure configurations (p. 7).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Evaluation excludes failed/insufficient-coverage trajectories before mean ATE/RPE; this conditions reported errors on surviving runs (pp. 6-7).

## Transfer conditions

Report failures alongside survivor accuracy; position-only reference cannot independently verify full orientation error.

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

- **p. 6, Selected source passage.** "We filter out invalid trajectories to ensure the accuracy and reliability of the analysis by excluding failed runs."
  Adds explicit survivor-bias and compute-placement checks to benchmark interpretation.

## Survey-usable statements

### Supported

- Loop-closing benefits and compute demand depend on estimator, route and input rate. Adds explicit survivor-bias and compute-placement checks to benchmark interpretation.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Report failures alongside survivor accuracy; position-only reference cannot independently verify full orientation error.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 6, 7, 18, 20; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Simultaneous localization and mapping (SLAM) is essential for mobile robotics, enabling autonomous navigation in dynamic, unstructured outdoor environments without relying on external positioning systems. These environments pose significant challenges due to variable lighting, weather conditions, and complex terrain. Visual-Inertial SLAM has emerged as a promising solution for robust localization under such conditions. This paper benchmarks several open-source visual-Inertial SLAM systems, including traditional methods (ORB-SLAM3, VINS-Fusion, OpenVINS, Kimera, and SVO Pro) and learning-based approaches (HFNet-SLAM, AirSLAM), to evaluate their performance in unstructured natural outdoor settings. We focus on the impact of loop closing on localization accuracy and computational demands, providing a comprehensive analysis of these systems’ effectiveness in real-world environments and especially their application to embedded systems in outdoor robotics. Our contributions further include an assessment of varying frame rates on localization accuracy and computational load. The findings highlight the importance of loop closing in improving localization accuracy while managing computational resources efficiently, offering valuable insights for optimizing Visual-Inertial SLAM systems for practical outdoor applications in mobile robotics. The data set and the benchmark code are available under https://github.com/iis-esslingen/vi-slam_lc_benchmark.
