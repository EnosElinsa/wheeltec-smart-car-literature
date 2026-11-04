# SubT-MRS Dataset: Pushing SLAM Towards All-weather Environments

## Metadata

| Field | Value |
|---|---|
| ID | K01 |
| Title | SubT-MRS Dataset: Pushing SLAM Towards All-weather Environments |
| Authors | Shibo Zhao, Yuanjun Gao, Tianhao Wu, Damanpreet Singh, Rushan Jiang, Haoxiang Sun, Mansi Sarawata, Yuheng Qiu, Warren Whittaker, Ian Higgins, Yi Du, Shaoshu Su, Can Xu, John Keller, Jay Karhade, Lucas Nogueira, Sourojit Saha, Ji Zhang, Wenshan Wang, Chen Wang, and Sebastian Scherer |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/cvpr52733.2024.02137](https://doi.org/10.1109/cvpr52733.2024.02137) |
| Official URL | https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_SubT-MRS_Dataset_Pushing_SLAM_Towards_All-weather_Environments_CVPR_2024_paper.html |
| Theme folder | T1-perception-localization |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T1-perception-localization/2024-SubT-MRS-K01/paper.pdf` and `02-fulltext/T1-perception-localization/2024-SubT-MRS-K01/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2024-SubT-MRS-K01/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-resource
- evidence_all: dataset-resource, recorded-robot-data, simulation
- protocol_caveats: none
- platform_class: mixed
- platform: Aerial, legged and wheeled robots and RC cars share one sensor pack; carriers of individual challenge sequences are not stated in the inspected pages (pp. 1, 4).
- boundary_platform: yes
- degradation: visual-degradation, lidar-degeneracy
- degradation_observed: none
- evaluation_primary: designed-degradation
- evaluation_all: residual, designed-degradation
- sensors: Velodyne VLP-16 LiDAR, four fisheye RGB cameras, FLIR Boson thermal camera, Epson IMU, optional depth camera (pp. 3-4)
- compute: Sensor pack with an NVIDIA Jetson AGX Xavier; the most accurate LiDAR challenge entry took 51.3 s per iteration (pp. 3, 7).
- compute_location: not-reported
- summary_result: Across 29 challenge submissions, average ATE is 1.61 m on mixed degradation versus 0.836 m on geometric degradation; no sensor-fusion entry met the success criteria (pp. 6-7).
- summary_limitation: No limitation is stated by the authors; the limits they report concern the evaluated SLAM systems in caves, aggressive motion and mixed degradation (pp. 7-8).
- survey_included: yes
- verification_level: light

## Problem

SLAM datasets are mostly recorded in controlled conditions, and trajectory error alone does not show whether an estimate stays usable for control. The paper releases a multi-degraded dataset and a velocity-based robustness metric (pp. 1-2).

## Mechanism

Real-world sequences from the DARPA SubT Challenge (2019-2021) and two further years (2022-2023) cover more than 30 scenes with visual, geometric and mixed degradation. Ground truth combines FARO scanner maps with map registration, odometry and IMU constraints. The robustness metric is the area under the F1 curve of velocity error, computed for position and rotation (pp. 1, 4-6).

## Baselines and controls

Challenge submissions from external teams in LiDAR and visual tracks, ranked by ATE and by the robustness metric (pp. 6-8).

## Platform and setup

More than 500 hours and 100 km of trajectories; per-sequence results for urban, tunnel, cave, nuclear, corridor, multi-floor and Block LiDAR sequences, plus simulated sequences derived from TartanAir (pp. 1-2, 6-7). The Block LiDAR sequences alternate LiDAR and visual data loss (p. 7). LODESTAR (E01) evaluates on the Long Corridor and Cavern Handheld sequences of this dataset.

## Evidence type and transfer

Strongest coded setting: `dataset-resource`, backed by the authors' recorded robot data and simulated sequences. Results are reported per named degradation condition, so `designed-degradation` is primary. The provisional module `localization-mapping` is confirmed: the contribution is a SLAM dataset and evaluation metric. The robot carrying each sequence is not stated in the inspected pages, so the platform class is `mixed`.

## Sensors

The sensor pack carries four Leopard Imaging fisheye RGB cameras, a Velodyne puck, an Epson M-G365 IMU and a FLIR Boson thermal camera, synchronized to within 3 ms (p. 3). Ground-truth maps come from a FARO Focus 3D S120 scanner (p. 4).

## Compute and latency

The sensor pack includes an NVIDIA Jetson AGX Xavier (p. 3). Runtimes of challenge entries are reported per team; the most accurate LiDAR entry took 51.3 s per iteration and the leading visual entry 183 s (p. 7). Table 2 device values were not re-read from a rendered page.

## Key quantitative results

- Scale: more than 500 hours and 100 km of trajectories over five years and more than 30 scenes (pp. 1-2).
- Challenge: 29 submissions; five LiDAR and four visual winners; no sensor-fusion submission met the success criteria (p. 6).
- Best LiDAR ATE 0.588 m (51.3 s per iteration) and best visual ATE 0.547 m (183 s per iteration) (p. 7).
- Average ATE on mixed-degradation sequences is 1.61 m versus 0.836 m on geometric degradation (p. 7).
- Average Rp and Rr are 0.290 and 0.473 on mixed degradation versus 0.664 and 0.754 on geometric degradation (p. 8).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- No limitation of the dataset itself is stated in the inspected pages. The authors report that current LiDAR methods struggle in confined caves, that current methods struggle with aggressive motion, and that fusion methods do not select the most informative measurements (pp. 7-8).
- Simulated sequences are included only for evaluation completeness; the dataset itself is real-world data (p. 2).

## Transfer conditions

The degradation labels are per sequence, so per-sequence carriers must be checked in the supplementary material before a result is attributed to a wheeled robot. Ground truth relies on prior scanner maps, which a deployment does not have.

## Code and data

The dataset page https://superodometry.com/datasets is printed on p. 1; availability was not checked.

## Version family

The PDF and BibTeX are the CVF open-access version, which states that it is identical to the accepted version except for the watermark (p. 1). The IEEE DOI 10.1109/cvpr52733.2024.02137 identifies the same paper in IEEE Xplore; its Crossref record has the same title, the same 21 authors and pages 22647-22657. Counted once.

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

- **p. 7, Sec. 4.1.** "These sequences involve alternating periods of LiDAR and Visual data loss, challenging algorithms to promptly detect sensor failures and switch to the other modality for SLAM."
  The Block LiDAR sequences inject modality dropout; they test switching, not recovery of a navigation task.
- **p. 6, Sec. 4.1.** "However, in the sensor fusion track, which addresses both visual and geometric degradation, no submissions met the criteria for success."
  Mixed degradation defeated all fusion entries in the challenge.
- **p. 4, Sec. 3.1.3.** "To address this, we employed diverse robot platforms, including aerial, legged, and wheeled robots, navigating through various environments from urban campuses to medical facilities and natural terrains like caves."
  Platform mix behind the mixed platform coding.

## Survey-usable statements

### Supported

- SubT-MRS provides per-condition SLAM benchmarks for visual, geometric and mixed degradation, including injected modality dropout.
- In the challenge, mixed degradation raised average ATE above that of geometric degradation, and no fusion entry met the success criteria.

### Not supported

- Results on SubT-MRS sequences are not wheeled-robot evidence unless the carrier of the sequence is established.
- The robustness metric is computed offline from velocity error; it is not a closed-loop task outcome.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Simultaneous localization and mapping (SLAM) is a fundamental task for numerous applications such as autonomous navigation and exploration. Despite many SLAM datasets have been released, current SLAM solutions still struggle to have sustained and resilient performance. One major issue is the absence of high-quality datasets including diverse all-weather conditions and a reliable metric for assessing robustness. This limitation significantly restricts the scalability and generalizability of SLAM technologies, impacting their development, validation, and deployment. To address this problem, we present SubT-MRS, an extremely challenging real-world dataset designed to push SLAM towards all-weather environments to pursue the most robust SLAM performance. It contains multi-degraded environments including over 30 diverse scenes such as structureless corridors, varying lighting conditions, and perceptual obscurants like smoke and dust; multimodal sensors such as LiDAR, fisheye camera, IMU, and thermal camera; and multiple locomotions like aerial, legged, and wheeled robots. We developed accuracy and robustness evaluation tracks for SLAM and introduced novel robustness metrics. Comprehensive studies are performed, revealing new observations, challenges, and opportunities for future research.
