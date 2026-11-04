# E2-BKI: Evidential Ellipsoidal Bayesian Kernel Inference for Uncertainty-Aware Gaussian Semantic Mapping

## Metadata

| Field | Value |
|---|---|
| ID | R08 |
| Title | E2-BKI: Evidential Ellipsoidal Bayesian Kernel Inference for Uncertainty-Aware Gaussian Semantic Mapping |
| Authors | Junyoung Kim, Minsik Jeon, Jihong Min, Kiho Kwak, and Junwon Seo |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3653367](https://doi.org/10.1109/lra.2026.3653367) |
| Official URL | https://ieeexplore.ieee.org/document/11352513/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-E2-BKI-R08/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-E2-BKI-R08/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-E2-BKI-R08/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: Off-road and urban outdoor datasets including RELLIS-3D and an OffRoad dataset (pp. 5-7).
- boundary_platform: yes
- degradation: terrain, model-error
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR point clouds with camera-based semantic segmentation
- compute: Intel i7-12700H laptop CPU, averaged over five runs (p. 7).
- compute_location: desktop-offline
- summary_result: Evidential semantics, Gaussian primitives and geometry-aligned kernels improve semantic mapping and uncertainty calibration under sparse inputs and limited training data (pp. 6-7).
- summary_limitation: Predictive uncertainties require further calibration, and open-set extension is future work (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Continuous semantic mapping propagates unreliable predictions, misaligned kernels and noisy distant points through outdoor maps.

## Mechanism

Evidential deep learning estimates semantic uncertainty; observations are aggregated into anisotropic Gaussian primitives that are merged and pruned; ellipsoidal kernels steer Bayesian kernel inference along local geometry (pp. 3-5).

## Baselines and controls

S-BKI and evidential semantic mapping (EBS), with component ablations on RELLIS-3D (pp. 6-7).

## Platform and setup

Dataset evaluation with sparsity and limited-training robustness studies (p. 7). Off-road and urban outdoor datasets including RELLIS-3D and an OffRoad dataset (pp. 5-7).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. Dataset replay of mapping; no planner or controller consumes the uncertainty.

## Sensors

LiDAR point clouds with camera-based semantic segmentation.

## Compute and latency

Intel i7-12700H laptop CPU, averaged over five runs (p. 7).

## Key quantitative results

- E2-BKI retains the most robust performance under input sparsity and limited semantic training data in the reported comparisons (p. 7, Fig. 6).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Future work includes more calibrated predictive uncertainties, refined uncertainty definitions and open-set settings (p. 8).

## Transfer conditions

Uncertainty calibration is evaluated for mapping, not for risk-sensitive traversal decisions.

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

- **p. 8, Fig. 7.** "While S-BKI produces incorrect semantics with uncalibrated uncertainty estimates, E2-BKI recovers the correct semantic labels and explicitly flags these challenging regions with higher uncertainty."
  Qualitative uncertainty behavior in one mapped scene; the authors still list better calibration as future work (p. 8).

## Survey-usable statements

### Supported

- Semantic map uncertainty can be modeled jointly with geometry for outdoor robots.

### Not supported

- The calibrated uncertainty is not shown to change robot motion.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Semantic mapping aims to construct a 3D semantic representation of the environment, providing essential knowledge for robots operating in complex outdoor settings. While Bayesian Kernel Inference (BKI) addresses discontinuities of map inference from sparse sensor data, existing semantic mapping methods suffer from various sources of uncertainties in challenging outdoor environments. To address these issues, we propose an uncertainty-aware semantic mapping framework that handles multiple sources of uncertainties, which significantly degrade mapping performance. Our method estimates uncertainties in semantic predictions using Evidential Deep Learning and incorporates them into BKI for robust semantic inference. It further aggregates noisy observations into coherent Gaussian representations to mitigate the impact of unreliable points, while employing geometry-aligned kernels that adapt to complex scene structures. These Gaussian primitives effectively fuse local geometric and semantic information, enabling robust, uncertainty-aware mapping in complex outdoor scenarios. Comprehensive evaluation across diverse off-road and urban outdoor environments demonstrates consistent improvements in mapping quality, uncertainty calibration, representational flexibility, and robustness, while maintaining real-time efficiency.
