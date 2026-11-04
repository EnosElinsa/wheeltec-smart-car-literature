# Sem-NaVAE: Semantically-Guided Outdoor Mapless Navigation via Generative Trajectory Priors

## Metadata

| Field | Value |
|---|---|
| ID | R25 |
| Title | Sem-NaVAE: Semantically-Guided Outdoor Mapless Navigation via Generative Trajectory Priors |
| Authors | Gonzalo Olguín, and Javier Ruiz-del-Solar |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3703234](https://doi.org/10.1109/lra.2026.3703234) |
| Official URL | https://ieeexplore.ieee.org/document/11560929/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-Sem-NaVAE-R25/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-Sem-NaVAE-R25/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2026-Sem-NaVAE-R25/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: few-trials
- platform_class: wheeled-unspecified
- platform: Husarion Panther UGV with 64-channel Ouster LiDAR, RGB camera, IMU and GPS-RTK on 120-240 m campus and park routes (pp. 1, 5).
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: LiDAR, RGB camera, IMU, GPS-RTK
- compute: NVIDIA RTX4060 laptop on the data-collection platform (p. 5); deployment placement not verified.
- compute_location: not-reported
- summary_result: CVAE candidate trajectories scored by open-vocabulary segmentation reach 90% success on 120-240 m routes, within 7% of a map-based upper bound (p. 1).
- summary_limitation: Evaluation is limited to campus and park-like environments with few repeated trials per route (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Mapless outdoor navigation needs multimodal motion proposals that respect semantic preferences.

## Mechanism

A conditional VAE generates diverse trajectories, kinematic and collision filters remove infeasible ones, a lightweight VLM segmentation scores candidates by language-specified preferences, and a local planner executes velocity commands with asynchronous updates (pp. 2-5).

## Baselines and controls

Regression and geometric baselines including MTG and a map-based upper bound (p. 6).

## Platform and setup

Real-world outdoor routes in unseen environments (pp. 5-7). Husarion Panther UGV with 64-channel Ouster LiDAR, RGB camera, IMU and GPS-RTK on 120-240 m campus and park routes (pp. 1, 5).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop hardware with few repeated trials per route.

## Sensors

LiDAR, RGB camera, IMU, GPS-RTK.

## Compute and latency

NVIDIA RTX4060 laptop on the data-collection platform (p. 5); deployment placement not verified.

## Key quantitative results

- Success exceeds the nearest baseline by 10% (p. 1).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The real-world evaluation is geographically limited to campus and park-like environments (p. 8).
- Few repeated trials per route call for more extensive testing of edge cases (p. 8).

## Transfer conditions

Semantic scoring depends on segmentation quality and image projection of candidates.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity; no other version is in the library.

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

- **p. 8, Sec. V.** "First, while our real-world evaluation covers extensive routes, it is geographically limited to campus and park-like environments."
  Author-stated scope.
- **p. 5, Sec. IV-A.** "To train the generative model, we collected a real-world dataset using a Husarion Panther UGV equipped with a 64-channel Ouster LiDAR, a generic RGB camera, IMU, GPS-RTK and a NVIDIA RTX4060 laptop."
  Platform and sensors.

## Survey-usable statements

### Supported

- Semantic selection over geometrically filtered candidates is executed on a wheeled robot outdoors.

### Not supported

- Collision safety under perception error is not quantified.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 5, 6, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

This work presents a mapless navigation approach for outdoor applications. It combines the exploratory capacity of conditional variational autoencoders (CVAEs) to generate trajectories and the semantic segmentation capabilities of a lightweight visual language model (VLM) to select the trajectory to execute. Open-vocabulary segmentation is used to score and select the generated trajectories based on natural language, and a state-of-the-art local planner executes velocity commands. One of the key features of the proposed approach is its ability to generate a large variability of trajectories and select them to navigate in real-time. In real-world outdoor experiments, Sem-NaVAE achieves a 90% success rate across routes of 120–240 m in unseen environments, outperforming the nearest baseline by 10% while remaining within 7% of a map-based upper bound.
