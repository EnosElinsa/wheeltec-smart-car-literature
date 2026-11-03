# JPG-SLAM: Joint Point-Gaussian Splatting Representation for Dense Dynamic SLAM

## Metadata

| Field | Value |
|---|---|
| ID | E20 |
| Title | JPG-SLAM: Joint Point-Gaussian Splatting Representation for Dense Dynamic SLAM |
| Authors | Kunrui Huang, Wennan Yang, Pengwei Zhou, Li Li, and Jian Yao |
| Venue | 2025 IEEE International Conference on Robotics and Automation (ICRA), pp. 5018-5024 |
| Year | 2025 |
| Type | conference |
| DOI | [10.1109/icra55743.2025.11127881](https://doi.org/10.1109/icra55743.2025.11127881) |
| Official URL | https://doi.org/10.1109/icra55743.2025.11127881 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2025-JPG-SLAM-E20/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2025-JPG-SLAM-E20/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2025-JPG-SLAM-E20/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: TUM RGB-D sequences (without IMU) and OpenLORIS ground-robot sequences (with IMU, truncated to about 1000 frames); drive type not recorded in the legacy extraction
- boundary_platform: yes
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: RGB-D camera and IMU; YOLACT dynamic segmentation
- compute: Intel Core i7 12900K at 2.50 GHz (model as printed) with RTX 3090; tracking 239 ms per frame and mapping 2.22 s per frame on OpenLORIS Cafe
- compute_location: desktop-offline
- summary_result: On OpenLORIS, JPG-SLAM reaches 0.29 m mean ATE versus 0.47 m for ORB-SLAM3, 0.42 m for VINS-Mono, and 2.25 m for SplaTAM.
- summary_limitation: The authors state that the system currently lacks a loop closure module.
- survey_included: yes
- verification_level: light

## Problem

Visual-inertial localization and high-quality dense reconstruction in dynamic scenes are optimized together, so that dynamic objects do not break camera tracking.

## Mechanism

Feature-point and IMU tracking are combined with anisotropic Gaussians. YOLACT and multi-view masks separate static regions, represented by 3D Gaussians, from dynamic regions, represented by 4D Gaussians. A covisibility-based local map freezes stable Gaussians and prunes redundant ones.

## Baselines and controls

ORB-SLAM3, VINS-Mono, DynaSLAM, SplaTAM, and offline 4DGS. Ablations without IMU, without the local map, and without 4DGS.

## Platform and setup

TUM RGB-D without IMU. Replay of OpenLORIS ground-robot data with IMU; each sequence is truncated to about 1000 frames because of baseline memory limits.

## Evidence type and transfer

Replay of real ground-robot RGB-D and IMU data, not a new online deployment. The short truncated sequences do not validate long-term operation.

## Sensors

RGB-D camera and IMU; on TUM the IMU factors are disabled. YOLACT segments dynamic objects.

## Compute and latency

The paper reports an Intel Core i7 12900K at 2.50 GHz (model as printed) and an RTX 3090. On OpenLORIS Cafe (Table IV), tracking takes 239 ms per frame, mapping 2.22 s per frame, and the map uses 63 MB. The 237 FPS is a separate rendering metric, not a SLAM frame rate.

## Key quantitative results

- OpenLORIS mean ATE, JPG-SLAM versus ORB-SLAM3, VINS-Mono, and SplaTAM: 0.29 m versus 0.47, 0.42, and 2.25 m (p. 5, Table II).
- TUM mean ATE, JPG-SLAM versus DynaSLAM and SplaTAM: 0.04 m versus 0.06 and 0.22 m (p. 5, Table II).
- OpenLORIS PSNR: 29.06 for JPG-SLAM versus 19.49 for SplaTAM; offline 4DGS reaches 29.70 with ground-truth poses (p. 5).
- Ablations: ATE 0.73 m without IMU versus 0.29 m for the full system; PSNR 23.56 without 4DGS versus 28.83 (p. 6).
- Runtime on OpenLORIS Cafe: tracking 239 ms per frame, mapping 2.22 s per frame, map memory 63 MB, rendering 237 FPS (p. 6, Table IV).

## Stated limitations

- The system currently lacks a loop closure module (p. 6).
- The comparison with 4DGS is unfair because 4DGS needs ground-truth poses for scene initialization (p. 5).

## Transfer conditions

Legacy reviewer observations: without loop closure, long-range drift is a risk. The tracking and mapping speeds do not support a real-time SLAM claim. Truncated tests and a desktop GPU do not show long-term operation on low-compute hardware. A wheeled reuse needs an RGB-D camera with IMU and a GPU.

## Code and data

The text gives no verifiable URL for code or self-collected data. TUM and OpenLORIS are public. No code was run.

## Version family

JPG-SLAM and PG-SLAM (E17) are different works and are not merged by their Gaussian-splatting names.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Abstract, p. 1 | "in order to enhance the adaptability of the system in dynamic environments, we introduced a dynamic region recognition module" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | qualifies | moderate | Limitations, p. 6 | "our system currently lacks a loop closure module" |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 5, Sequence truncation.** "approximately 1000 frames"
  Each OpenLORIS sequence is truncated to about 1000 frames.
- **p. 6, Limitations.** "our system currently lacks a loop closure module"
  The current system has no loop closure.
- **p. 5, Baselines.** "It is important to note that this comparison is unfair as the 4DGS method requires ground truth poses for scene initialization."
  The 4DGS rendering numbers are not a like-for-like comparison.
- **p. 1, Abstract.** "in order to enhance the adaptability of the system in dynamic environments, we introduced a dynamic region recognition module"
  The authors' motivation: dynamic regions need separate treatment.

## Survey-usable statements

### Supported

- Joint feature-point and Gaussian representation with IMU lowers mean ATE on truncated OpenLORIS ground-robot sequences compared with ORB-SLAM3, VINS-Mono, and SplaTAM (0.29 m versus 0.47, 0.42, and 2.25 m; numbers from a light review; re-check before citing).
- The IMU matters in this design: ATE rises from 0.29 m to 0.73 m without it.

### Not supported

- JPG-SLAM runs at 237 FPS: that is the rendering rate; tracking takes 239 ms per frame and mapping 2.22 s per frame.
- JPG-SLAM is validated for long-term operation: sequences are truncated to about 1000 frames and there is no loop closure.
- JPG-SLAM renders better than 4DGS: offline 4DGS reaches 29.70 PSNR with ground-truth poses.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; legacy Table IV quote dropped (a text-layer dump of the table, not found in paper.md); line-break hyphen in "approximately" removed; the authors' unfair-comparison note added as an excerpt to support the 4DGS limitation
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/6172e7e103160a8fea3775c3/

## Original abstract

This paper presents a simultaneous localization and mapping (SLAM) system to provide accurate pose estimation and dynamic scene reconstruction. Our approach proposes a Joint Point-Gaussian Splatting representation, which fully integrates the robustness of isotropic feature points in pose estimation and the flexibility of anisotropic 3D Gaussians in scene representation. This system does not need to suppress the anisotropic representation of Gaussian elements, which enables the mapping module to achieve finer scene representation with lower memory consumption. Additionally, in order to enhance the adaptability of the system in dynamic environments, we introduced a dynamic region recognition module and utilized 3D Gaussian Splatting and 4D Gaussian Splatting representations to represent static and dynamic regions respectively. Furthermore, we developed a local map management strategy for Gaussian Splatting mapping, effectively reducing the memory and computational resource usage in the mapping process. Experiments on public datasets demonstrate that our system achieves state-of-the-art tracking and mapping accuracy compared to existing baselines.
