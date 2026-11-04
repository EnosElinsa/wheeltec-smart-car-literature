# Kimera-Multi: Robust, Distributed, Dense Metric-Semantic SLAM for Multi-Robot Systems

## Metadata

| Field | Value |
|---|---|
| ID | K06 |
| Title | Kimera-Multi: Robust, Distributed, Dense Metric-Semantic SLAM for Multi-Robot Systems |
| Authors | Yulun Tian, Yun Chang, Fernando Herrera Arias, Carlos Nieto-Granda, Jonathan P. How, and Luca Carlone |
| Venue | IEEE Transactions on Robotics |
| Year | 2022 |
| Type | journal |
| DOI | [10.1109/tro.2021.3137751](https://doi.org/10.1109/tro.2021.3137751) |
| Official URL | https://ieeexplore.ieee.org/document/9686955/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T4-multi-robot-coordination/2022-Kimera-Multi-K06/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2022-Kimera-Multi-K06/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2022-Kimera-Multi-K06/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Clearpath Jackal UGVs recorded the Medfield and Stata outdoor datasets; EuRoC and photo-realistic simulations add further tests (pp. 12, 14).
- boundary_platform: no
- degradation: data-association-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Forward-facing RealSense D435i RGB-D camera and IMU (p. 14)
- compute: Communication payloads and solution runtime are tabulated in Table II (p. 13); the machine was not identified in this reading.
- compute_location: not-reported
- summary_result: Under 70% synthetic outlier loop closures, GNC with robust initialization reaches 0.003 m ATE versus 2.24 m for PCM; outdoor trajectories reach 860 m per robot (pp. 4, 14).
- summary_limitation: Experiments keep robots constantly in communication range; scenarios with intermittent communication are future work (p. 12).
- survey_included: yes
- verification_level: light

## Problem

Multi-robot SLAM must reject wrong inter-robot loop closures caused by perceptual aliasing and work with limited communication, while producing semantic maps (p. 1).

## Mechanism

Each robot runs Kimera for local trajectory and mesh estimation. When two robots are within communication range they exchange bag-of-words descriptors, verify candidate loop closures, and run a two-stage distributed back-end: GNC-based robust initialization of relative frames, then distributed GNC on top of Riemannian block-coordinate descent (D-GNC). Each robot then deforms its local mesh (pp. 2, 6-8).

## Baselines and controls

Least squares, PCM, PCM followed by D-GNC, D-GNC with naive initialization, early-stopped D-GNC and centralized GNC (pp. 12-13).

## Platform and setup

Synthetic pose graphs with 10% and 70% outlier loop closures over ten Monte Carlo runs (pp. 3-4); photo-realistic simulations and EuRoC (p. 12); two outdoor datasets with three Jackal trajectories each, at Medfield (longest 860 m) and around the Stata Center (each over 500 m) (p. 14).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`; Kimera-Multi processes recorded Jackal data with the robots treated as always in range. The outlier ratio is varied with results per ratio, so `designed-degradation` is coded with `data-association-fault`. The provisional module `multi-robot` is confirmed.

## Sensors

RealSense D435i RGB-D camera and IMU on each Jackal (p. 14); Kimera-VIO uses stereo images and IMU data (p. 6).

## Compute and latency

Table II reports data payloads and runtime (p. 13); its values and the machine were not re-read in this reading.

## Key quantitative results

- Synthetic test with 70% outlier loop closures: PCM 2.24 m ATE, GNC with naive initialization 11.59 m, PCM followed by GNC 0.09 m, GNC 0.003 m (p. 4, Fig. 8 caption).
- Medfield: three robots with 2188 m total trajectory length (p. 2, Fig. 1 caption); the longest trajectory is 860 m (p. 14).
- Both outdoor datasets contain many outlier loop closures, which D-GNC rejects; Stata has fewer inter-robot loop closures (p. 14).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Experiments run with robots constantly in communication range; scenarios with intermittent communication are future work (p. 12).
- On Stata, the lack of inter-robot loop closures limits accuracy, and loop-closure detection is to be improved (p. 15).

## Transfer conditions

Inter-robot measurements are accepted or rejected through GNC weights in robust initialization and D-GNC. Because the experiments keep robots in range, the evidence says nothing about stale or biased data after a partition.

## Code and data

Code availability was not checked in this targeted reading.

## Version family

Extends an earlier Kimera-Multi conference version that used incremental PCM (p. 2); that version is not in the library. The PDF states a date of publication of 20 January 2022 (p. 1), so no earlier online year is recorded; the 2021 in the DOI reflects acceptance in December 2021.

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

- **p. 12, Sec. VII-B.** "In our experiments in this section and Section VII-C, we run Kimera-Multi in a setting, where robots are constantly in communication range, which means that interrobot loop closures are established at the earliest possible time."
  Communication is not intermittent in any reported experiment.
- **p. 12, Sec. VII-B.** "In future work, we plan to further improve our implementation and test our system in scenarios where communication is intermittent."
  Author-stated limit of the communication model.
- **p. 14, Sec. VII-C.** "Both datasets contain many outlier loop closures, which are successfully rejected by D-GNC."
  Acceptance of inter-robot measurements works through robust estimation on recorded data.
- **p. 14, Sec. VII-C.** "collected using a Clearpath Jackal UGV equipped with a forward-facing RealSense D435i RGBD Camera and IMU."
  Carrier of the outdoor datasets; the drive type is not stated.

## Survey-usable statements

### Supported

- Kimera-Multi rejects outlier inter-robot loop closures with distributed GNC on recorded Jackal data.
- Its experiments keep the robots constantly in communication range.

### Not supported

- The paper does not evaluate behavior under intermittent communication or after partitions.
- Kimera-Multi is not shown driving robots in closed loop.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 6, 7, 8, 12, 13, 14, 15; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Multi-robot simultaneous localization and mapping (SLAM) is a crucial capability to obtain timely situational awareness over large areas. Real-world applications demand multi-robot SLAM systems to be robust to perceptual aliasing and to operate under limited communication bandwidth; moreover, it is desirable for these systems to capture semantic information to enable high-level decision-making and spatial artificial intelligence. This article presents Kimera-Multi, a multi-robot system that: 1) is robust and capable of identifying and rejecting incorrect inter- and intrarobot loop closures resulting from perceptual aliasing; 2) is fully distributed and only relies on local (peer-to-peer) communication to achieve distributed localization and mapping; and 3) builds a globally consistent metric-semantic 3-D mesh model of the environment in real time, where faces of the mesh are annotated with semantic labels. Kimera-Multi is implemented by a team of robots equipped with visual-inertial sensors. Each robot builds a local trajectory estimate and a local mesh using Kimera. When communication is available, robots initiate a distributed place recognition and robust pose graph optimization protocol based on a distributed graduated nonconvexity algorithm. The proposed protocol allows the robots to improve their local trajectory estimates by leveraging inter-robot loop closures while being robust to outliers. Finally, each robot uses its improved trajectory estimate to correct the local mesh using mesh deformation techniques. We demonstrate Kimera-Multi in photo-realistic simulations, SLAM benchmarking datasets, and challenging outdoor datasets collected using ground robots. Both real and simulated experiments involve long trajectories (e.g., up to 800 m per robot). The experiments show that Kimera-Multi: 1) outperforms the state of the art in terms of robustness and accuracy; 2) achieves estimation errors comparable to a centralized SLAM system while being fully distributed; 3) is parsimonious in terms of communication bandwidth; 4) produces accurate metric-semantic 3-D meshes; and 5) is modular and can also be used for standard 3-D reconstruction (i.e., without semantic labels) or for trajectory estimation (i.e., without reconstructing a 3-D mesh).
