# Comparison of DSO and ORB‐SLAM3 in Low‐Light Environments With Auxiliary Lighting and Deep Learning Based Image Enhancing

## Metadata

| Field | Value |
|---|---|
| ID | S20 |
| Title | Comparison of DSO and ORB‐SLAM3 in Low‐Light Environments With Auxiliary Lighting and Deep Learning Based Image Enhancing |
| Authors | Crocetti, Francesco and Brilli, Raffaele and Dionigi, Alberto and Fravolini, Mario L. and Costante, Gabriele and Valigi, Paolo |
| Venue | Journal of Field Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1002/rob.22595](https://doi.org/10.1002/rob.22595) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.22595 |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2025-Low-Light-SLAM-S20/paper.pdf` and `02-fulltext/T1-perception-localization/2025-Low-Light-SLAM-S20/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2025-Low-Light-SLAM-S20/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Pioneer3-DX collecting repeated indoor paths using LiDAR-based navigation; evaluated monocular DSO/ORB-SLAM3 are separate from that control loop (pp. 7-8).
- boundary_platform: no
- degradation: visual-degradation
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Monocular camera, controlled LED bars and lux meter; 2D LiDAR/AMCL supplies collection navigation and reference
- compute: Jetson TX1 is specified for acquisition/control; enhancement and VO timing must be distinguished from this hardware identity (pp. 7, 21).
- compute_location: not-reported
- summary_result: The useful illumination/enhancement setting depends on the visual estimator and scene.
- summary_limitation: LUCID lacks outdoor low-light sequences and IMU readings (p. 22).
- survey_included: yes
- verification_level: light

## Problem

Robot-mounted lighting introduces scene-dependent shadows and exposure effects that alter visual odometry.

## Mechanism

Varies auxiliary LED intensity and compares raw and EnlightenGAN-enhanced image sequences with monocular DSO and ORB-SLAM3 (pp. 8, 11, 13).

## Baselines and controls

Raw images, EnlightenGAN, histogram equalization, CLAHE and Retinex variants; best trial selections and failures are described separately (pp. 13, 21).

## Platform and setup

Pioneer3-DX collecting repeated indoor paths using LiDAR-based navigation; evaluated monocular DSO/ORB-SLAM3 are separate from that control loop (pp. 7-8).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. A LiDAR-derived reference and independently driven capture robot support an estimator study, not visual closed-loop recovery. Report enhancement timing separately.

## Sensors

Monocular camera, controlled LED bars and lux meter; 2D LiDAR/AMCL supplies collection navigation and reference.

## Compute and latency

Jetson TX1 is specified for acquisition/control; enhancement and VO timing must be distinguished from this hardware identity (pp. 7, 21).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

LUCID lacks outdoor low-light sequences and IMU readings (p. 22).

## Transfer conditions

A LiDAR-derived reference and independently driven capture robot support an estimator study, not visual closed-loop recovery. Report enhancement timing separately.

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

- **p. 22, Selected source passage.** "it is not possible to set a universal light intensity value that maximizes performance in all cases."
  Adds active illumination as a sensing response and challenges the assumption that brighter or visually enhanced images uniformly improve navigation.

## Survey-usable statements

### Supported

- The useful illumination/enhancement setting depends on the visual estimator and scene. Adds active illumination as a sensing response and challenges the assumption that brighter or visually enhanced images uniformly improve navigation.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. A LiDAR-derived reference and independently driven capture robot support an estimator study, not visual closed-loop recovery. Report enhancement timing separately.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 7, 8, 11, 13, 21, 22; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

In the evolving landscape of robotic navigation, the demand for solutions capable of operating in challenging scenarios, such as low-light environments, is increasing. This study investigates the performance of two state-of-the-art (SOTA) visual simultaneous localization and mapping (VSLAM) algorithms, direct sparse odometry (DSO) and ORBSLAM3, in their monocular implementation, in the dark indoor scenarios where the only light source is provided by an auxiliary light system installed on a robot. A modified Pioneer3-DX robot, equipped with a monocular camera, LED bars, and a lux meter, is utilized to collect a novel data set, “LUCID—Lighting Up Campus Indoor Spaces Data Set,” in real-world, low-light indoor environments. The data set includes image sequences enhanced using a generative adversarial network (GAN) to simulate varying levels of image enhancement. Through comprehensive experiments, we assess the performances of the V-SLAM algorithm, considering the critical balance between maintaining adequate auxiliary illumination and enhancing. This study provides insights into the optimization of robotic navigation in lowlight conditions, paving the way for more robust and reliable autonomous navigation systems.
