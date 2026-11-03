# PG-SLAM: Photorealistic and Geometry-Aware RGB-D SLAM in Dynamic Environments

## Metadata

| Field | Value |
|---|---|
| ID | E17 |
| Title | PG-SLAM: Photorealistic and Geometry-Aware RGB-D SLAM in Dynamic Environments |
| Authors | Haoang Li, Xiangqi Meng, Xingxing Zuo, Zhe Liu, Hesheng Wang, and Daniel Cremers |
| Venue | IEEE Transactions on Robotics, vol. 41, pp. 6084-6101 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3619073](https://doi.org/10.1109/tro.2025.3619073) |
| Official URL | https://ieeexplore.ieee.org/document/11196012/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2025-PG-SLAM-E17/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2025-PG-SLAM-E17/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2025-PG-SLAM-E17/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: Bonn and TUM indoor RGB-D sequences and NeuMan outdoor sequences; carriers not recorded in the legacy extraction
- boundary_platform: yes
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: RGB-D camera; Mask R-CNN segmentation and RAFT optical flow
- compute: hardware model not reported; 1.93 s per frame in total; 2.3 to 2.7 GB GPU and 1.5 to 1.8 GB CPU memory
- compute_location: not-reported
- summary_result: On Bonn, PG-SLAM reaches 6.5 cm mean APE RMSE versus 12.3 cm for RoDyn-SLAM and 34.0 cm for ORB-SLAM3.
- summary_limitation: The authors state that the main limitation is that the method cannot achieve real-time performance.
- survey_included: yes
- verification_level: light

## Problem

RGB-D SLAM in dynamic scenes must recover the camera trajectory and a static and dynamic scene that is consistent in appearance and geometry.

## Mechanism

Gaussians of the foreground are initialized from category shape priors and aligned with MLP deformation or rigid flow. Static local maps are aligned jointly by geometry and appearance. A coarse-to-fine camera estimate uses static and dynamic objects and RAFT optical-flow constraints. The system includes geometric loop closure.

## Baselines and controls

RoDyn-SLAM, ORB-SLAM3, ESLAM, MonoGS, and others. Ablations of static and dynamic camera tracking, the optical-flow constraint, and dynamic Gaussian initialization.

## Platform and setup

Replay of real RGB-D data: Bonn and TUM indoors and NeuMan outdoors. The quadruped and vehicle examples in the separate supplementary material were not read and are outside the verified scope.

## Evidence type and transfer

Replay of real visual data, focused on localization and rendered geometry. There is no new closed-loop navigation on a physical robot.

## Sensors

RGB-D camera, with Mask R-CNN and RAFT. Category shape initialization and learned deformation depend on priors, so there is no guarantee for arbitrary unknown objects.

## Compute and latency

The text reports no hardware model. Table III gives 1.93 s per frame in total versus 0.85 s for MonoGS, 1.42 s for RoDyn-SLAM, and 3.10 s for ESLAM. GPU memory is 2.3 to 2.7 GB and CPU memory 1.5 to 1.8 GB, and old Gaussians can be saved to disk. The method is not real time.

## Key quantitative results

- APE RMSE, PG-SLAM versus RoDyn-SLAM and ORB-SLAM3: Bonn mean 6.5 cm versus 12.3 and 34.0 cm; TUM 4.5 cm versus 5.3 and 10.3 cm; NeuMan 1.45 cm versus 2.54 and 19.50 cm (legacy location: Table II, page 13; the table values are not in the PDF text layer).
- Counterexamples: Bonn mvbox2 7.0 cm for PG-SLAM versus 3.5 cm for ORB-SLAM3; TUM wkhf 11.7 cm for PG-SLAM versus 5.6 cm for RoDyn-SLAM (legacy location: Table II, page 13; not in the PDF text layer).
- Optical-flow constraint ablation: Bonn pstrack 8.0 cm without versus 5.0 cm with; TUM wkxyz 8.6 cm versus 6.8 cm (legacy location: Table V, page 15; not in the PDF text layer).
- Runtime: 1.93 s per frame in total versus 0.85 s for MonoGS, 1.42 s for RoDyn-SLAM, and 3.10 s for ESLAM (legacy location: Table III, page 13; not in the PDF text layer).
- Memory: 2.3 to 2.7 GB GPU and 1.5 to 1.8 GB CPU (p. 13).

## Stated limitations

- The main limitation is that the method cannot achieve real-time performance (p. 16).
- As human movement becomes larger, the human Gaussian initialization becomes more challenging (p. 15).

## Transfer conditions

Legacy reviewer observations: errors of the learned shapes, segmentation, optical flow, and depth affect the results, and the gain shrinks under large motion. The loop closure is described on p. 8, but its effect is in the supplementary material, which was not read; the missing-loop-closure limitation of JPG-SLAM (E20) does not apply here. Generalization to non-rigid objects outside the categories and operation on a low-compute robot are not shown.

## Code and data

The text gives no verifiable repository URL or release status for the method. Bonn and TUM are public. No code was run and the separate supplement was not read.

## Version family

PG-SLAM (T-RO 2025) is an independent work and is not merged with JPG-SLAM (E20).

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "Many methods directly filter out dynamic objects, resulting in incomplete scene reconstruction and limited accuracy of camera localization." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Limitations, p. 16 | "The main limitation of our method is that it cannot achieve real-time performance." |

## Page-cited excerpts

- **p. 16, Limitations.** "The main limitation of our method is that it cannot achieve real-time performance."
  The authors rule out real-time operation of the current method.
- **p. 15, Initialization limitation.** "as the human movement becomes larger, the human Gaussian initialization is more challenging."
  Category shape initialization is harder under larger motion, so robustness to arbitrary non-rigid motion does not follow.
- **p. 13, Runtime.** "the total time cost is not a simple accumulation of the time costs of different modules due to parallel threads."
  The 1.93 s per frame is a total over parallel threads and must not be summed from module times.
- **p. 1, Abstract.** "Many methods directly filter out dynamic objects, resulting in incomplete scene reconstruction and limited accuracy of camera localization."
  The authors' motivation: dynamic objects limit localization and reconstruction.

## Survey-usable statements

### Supported

- Modeling dynamic foreground objects with shape-prior Gaussians and using them for camera tracking lowers mean APE on Bonn, TUM, and NeuMan replay compared with RoDyn-SLAM and ORB-SLAM3 (numbers from a light review; re-check before citing).

### Not supported

- PG-SLAM is best on every sequence: Bonn mvbox2 (ORB-SLAM3 3.5 cm versus 7.0 cm) and TUM wkhf (RoDyn-SLAM 5.6 cm versus 11.7 cm) are counterexamples recorded in the legacy extraction; the full table was not re-checked.
- PG-SLAM runs in real time: the authors state it does not, at 1.93 s per frame.
- PG-SLAM is validated on a robot in closed loop: only dataset replay is in the verified scope.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; no legacy quote dropped (line-break hyphen in "initialization" removed); Table II, III, and V values kept without a page because they are not in the PDF text layer
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/0a526a538f55c210deecfc7f/

## Original abstract

Simultaneous localization and mapping (SLAM) has achieved impressive performance in static environments. However, SLAM in dynamic environments remains an open question. Many methods directly filter out dynamic objects, resulting in incomplete scene reconstruction and limited accuracy of camera localization. The other works express dynamic objects by point clouds, sparse joints, or coarse meshes, which fails to provide a photorealistic representation. To overcome the aforementioned limitations, we propose a photorealistic and geometry-aware red-green-blue-depth (RGB-D) SLAM method based on Gaussian splatting. Our method is composed of three main modules to map the dynamic foreground including nonrigid humans/quadrupeds and rigid items, reconstruct the static background, and localize the camera. To map the foreground, we focus on modeling the deformations and/or motions. We consider the shape priors of humans/quadrupeds and exploit the geometric and appearance constraints of dynamic Gaussians. For background mapping, we design an optimization strategy between neighboring local maps by integrating appearance constraint into geometric alignment. As to camera localization, we leverage both static background and dynamic foreground to increase the number of observations and introduce more constraints. We explore the geometric and appearance constraints by associating 3-D Gaussians with 2-D optical flows and pixel patches. Experiments on extensive real-world datasets demonstrate that our method outperforms state-of-the-art approaches in terms of camera localization and scene mapping.
