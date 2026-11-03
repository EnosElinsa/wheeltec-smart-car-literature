# ERPoT: Effective and Reliable Pose Tracking for Mobile Robots Using Lightweight Polygon Maps

## Metadata

| Field | Value |
|---|---|
| ID | M13 |
| Title | ERPoT: Effective and Reliable Pose Tracking for Mobile Robots Using Lightweight Polygon Maps |
| Authors | Haiming Gao, Qibo Qiu, Hongyan Liu, Dingkun Liang, Chaoqun Wang, and Xuebo Zhang |
| Venue | IEEE Transactions on Robotics, vol. 41, pp. 3799-3819 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3577028](https://doi.org/10.1109/tro.2025.3577028) |
| Official URL | https://ieeexplore.ieee.org/document/11024226/ |
| Theme folder | T6-reliability-deployment |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T6-reliability-deployment/2025-ERPoT-M13/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-ERPoT-M13/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-ERPoT-M13/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Eagle 204AKZ and YUHESEN FR-09; drive type not recorded
- boundary_platform: no
- degradation: scene-change
- degradation_observed: dynamic-objects, terrain
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR-only tracking; GPS and IMU used for self-dataset ground truth
- compute: Intel Core i7-11800H, 32 GB RAM; Ubuntu 20.04, ROS Noetic; runtime values not extracted
- compute_location: desktop-offline
- summary_result: On a self-recorded sequence 1.5 years after mapping, the legacy extraction records ERPoT tracking while HDL_localization and SM_MCL fail.
- summary_limitation: Ground segmentation can fail on uneven terrain or low-obstacle clutter, degrading tracking.
- survey_included: yes
- verification_level: light

## Problem

Track pose using only LiDAR in large outdoor and challenging indoor scenes where a dense prior map grows with the environment. The goal is a compact prior that still supports reliable localization on later revisits after environmental change.

## Mechanism

ERPoT reduces dense 3-D LiDAR to sparse 2-D scans through ground removal and obstacle selection. An offline polygon map represents occupancy with multiple polygons; online pose estimation matches points to polygons using point-to-vertex and point-to-edge constraints. The tracker uses the prior map and current LiDAR without camera or IMU input. The legacy extraction records a C/C++ implementation under ROS Noetic.

## Baselines and controls

Six map-based localizers are named: ALOAM_MCL, FLOAM_MCL, KISS_MCL, HDL_localization, SM_MCL, and Range_MCL. Comparisons cover map size, translational and rotational errors, and runtime; numerical scores were not extracted in the legacy card.

## Platform and setup

Offline evaluation uses public and self-recorded LiDAR sequences. Public sets are KITTI car sequences 00/02/05/06/08 with HDL-64E, Newer College handheld OS1-64, and FusionPortable OS1-128 sequences including indoor pedestrians and campus/building scenes. The authors' datasets use Eagle 204AKZ with VLP-32C and YUHESEN FR-09 with Pandar40P. Self dataset-01-3 revisits the map after a year and a half. Ground truth for the self-recorded data uses LIO-SAM with GPS and IMU. No closed-loop navigation trial is recorded.

## Evidence type and transfer

The strongest setting is the authors' recorded robot data, alongside public dataset playback. LiDAR tracking on these sequences does not establish live navigation performance. The recorded ground robots support a wheeled-platform coding, but the legacy card gives no drive type; the car-mounted and handheld public sets are additional transfer boundaries.

## Sensors

The tracker uses LiDAR only: VLP-32C, Pandar40P, HDL-64E, and Ouster OS1-64/128 appear across datasets. GPS and IMU are used for self-dataset ground truth through LIO-SAM, rather than as tracker inputs.

## Compute and latency

The legacy extraction records Intel Core i7-11800H, 32 GB RAM, Ubuntu 20.04, and ROS Noetic for experiments. Processing is offline on recorded data. Runtime comparisons are reported, but no numerical runtime was extracted; hardware details remain legacy information, not re-verified here.

## Key quantitative results

- Self dataset-01-3 is recorded a year and a half after construction of the prior map; the legacy extraction records that ERPoT tracks while HDL_localization and SM_MCL fail (p. 17, Table VIII).
- The legacy evaluation compares ERPoT with six map-based localizers on prior-map size, pose error, and runtime; no numerical metric values were recorded (p. 1, abstract).

## Stated limitations

- Ground segmentation may fail on uneven terrain or cluttered scenes with low obstacles, degrading tracking (p. 19).
- Dependence on ground segmentation reduces versatility relative to methods that do not require this preprocessing (p. 19).
- KITTI RTK ground truth is inconsistent at meter scale and is refined using point-cloud registration in the authors' evaluation (p. 11).

## Transfer conditions

Reuse requires a compatible LiDAR, ground removal and obstacle selection, a prior polygon map, and the ROS/C++ implementation assumptions. Ground extraction quality is a condition for applying the tracking result. The public vehicle and handheld sequences and the authors' robot datasets do not by themselves validate a closed-loop navigation stack on another chassis. Drive-type-specific performance is not established by the legacy record.

## Code and data

The abstract states that the corresponding code is available online (p. 1). A repository URL was not recorded in the legacy extraction; availability was not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. V-A, p. 19 | "In these cases, the ground segmentation process may fail, leading to degraded performance." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Abstract, p. 1 | "Both aspects serve as the foundational pillars for future navigation across diverse mobile platforms equipped with different LiDAR sensors in varied environments." |

## Page-cited excerpts

- **p. 19, Sec. V-A.** "In these cases, the ground segmentation process may fail, leading to degraded performance."
  The surrounding stated limitation concerns uneven terrain and clutter with low obstacles.
- **p. 1, Abstract.** "Both aspects serve as the foundational pillars for future navigation across diverse mobile platforms equipped with different LiDAR sensors in varied environments."
  The mapping and tracking contribution is framed as a basis for future navigation; the legacy evidence remains recorded-data evaluation.

## Survey-usable statements

### Supported

- Compact polygon priors and point-polygon matching support LiDAR-only pose tracking on public and self-recorded datasets.
- The legacy record includes a map revisit after a year and a half and names ground-segmentation failure as a limitation; numerical survey citations require rechecking.

### Not supported

- ERPoT demonstrates closed-loop autonomous navigation on a specific differential-drive chassis; the legacy experiments are offline and the authors' platforms' drive types are not recorded.
- Compact polygon maps eliminate sensitivity to terrain; unreliable ground segmentation can still degrade tracking.
- LiDAR-only tracking means the ground-truth pipeline also excludes GPS and IMU; those sensors are used for the self-recorded reference.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: English template conversion; abstract copied verbatim including transcription spacing; no legacy verbatim excerpts to retain; recorded-robot-data distinguished from public playback and closed-loop operation; drive type left unspecified; numbers not re-verified
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

This article presents an effective and reliable pose tracking solution, termed ERPoT, for mobile robots operating in large-scale outdoor and challenging indoor environments, underpinned by an innovative prior polygon map. Especially, to overcome the challenge that arises as the map size grows with the expansion of the environment, the novel form of a prior map composed of multiple polygons is proposed. Benefiting from the use of polygons to concisely and accurately depict environmental occupancy, the prior polygon map achieves long-term reliable pose tracking while ensuring a compact form. More importantly, pose tracking is carried out under pure LiDAR mode, and the dense 3-D point cloud is transformed into a sparse 2-D scan through ground removal and obstacle selection. On this basis, a novel cost function for pose estimation through point-polygon matching is introduced, encompassing two distinct constraint forms: point-to-vertex and point-to-edge. In this study, our primary focus lies on two crucial aspects: lightweight and compact prior map construction, as well as effective and reliable robot pose tracking. Both aspects serve as the foundational pillars for future navigation across diverse mobile platforms equipped with different LiDAR sensors in varied environments. Comparative experiments based on the publicly available datasets and our self-recorded datasets are conducted, and evaluation results show the superior performance ofERPoT on reliability, prior map size, pose estimation error, and runtime over the other six approaches. The corresponding code can be accessed online.
