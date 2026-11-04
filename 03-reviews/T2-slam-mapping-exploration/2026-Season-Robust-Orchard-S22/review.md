# A Season‐Robust Long‐Term Localization Method Using Trunk Semantic Features in Dynamic Orchard Environments

## Metadata

| Field | Value |
|---|---|
| ID | S22 |
| Title | A Season‐Robust Long‐Term Localization Method Using Trunk Semantic Features in Dynamic Orchard Environments |
| Authors | Liu, Enbo and Tang, Wei and Huang, Anmin and Zhou, Zeyu and Zhang, Renyuan |
| Venue | Journal of Field Robotics |
| Year | 2026 |
| Type | journal |
| DOI | [10.1002/rob.70159](https://doi.org/10.1002/rob.70159) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.70159 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-Season-Robust-Orchard-S22/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-Season-Robust-Orchard-S22/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-Season-Robust-Orchard-S22/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Orchard mobile robot with summer/winter recordings; control-loop use of the evaluated localization is not established by this reading (p. 12).
- boundary_platform: no
- degradation: scene-change
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Camera/LiDAR trunk extraction for mapping; LiDAR registration and optional differential GNSS for localization; separate GNSS/INS reference
- compute: Intel Core i7-10700TE industrial computer without GPU; mapping/extraction and localization costs have distinct roles (pp. 12, 19).
- compute_location: desktop-offline
- summary_result: Stable trunk landmarks support cross-season localization without rebuilding the whole orchard map.
- summary_limitation: Sparse repetitive trunks weaken global recovery; likelihoods need sufficiently accurate particle prediction, and validation is limited to one orchard (p. 20).
- survey_included: yes
- verification_level: light

## Problem

Seasonal foliage changes undermine localization against full orchard point-cloud maps.

## Mechanism

Builds a static trunk-only semantic map from camera/LiDAR association, predicts particles with motion priors and scan registration, and updates likelihoods with trunk distances and optional GNSS (pp. 5, 20).

## Baselines and controls

The selected discussion contrasts full-map and lightweight-map registration and reports parameter/trunk-selection studies; no individual performance cells were retained (pp. 19-20).

## Platform and setup

Orchard mobile robot with summer/winter recordings; control-loop use of the evaluated localization is not established by this reading (p. 12).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Check trunk inclination, viewpoint coverage and GNSS reference reliability. A fixed extraction threshold validated on flatter terrain may not transfer to slopes (p. 19).

## Sensors

Camera/LiDAR trunk extraction for mapping; LiDAR registration and optional differential GNSS for localization; separate GNSS/INS reference.

## Compute and latency

Intel Core i7-10700TE industrial computer without GPU; mapping/extraction and localization costs have distinct roles (pp. 12, 19).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Sparse repetitive trunks weaken global recovery; likelihoods need sufficiently accurate particle prediction, and validation is limited to one orchard (p. 20).

## Transfer conditions

Check trunk inclination, viewpoint coverage and GNSS reference reliability. A fixed extraction threshold validated on flatter terrain may not transfer to slopes (p. 19).

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

- **p. 20, Selected source passage.** "the current validation is limited to a single orchard."
  Distinguishes removing seasonal nuisance structure from recovering after a large pose error; persistent landmarks alone do not solve kidnapped-robot recovery.

## Survey-usable statements

### Supported

- Stable trunk landmarks support cross-season localization without rebuilding the whole orchard map. Distinguishes removing seasonal nuisance structure from recovering after a large pose error; persistent landmarks alone do not solve kidnapped-robot recovery.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Check trunk inclination, viewpoint coverage and GNSS reference reliability. A fixed extraction threshold validated on flatter terrain may not transfer to slopes (p. 19).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 5, 12, 19, 20; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Localization is pivotal for enabling mobile robots to perform precision agriculture in orchards. However, dynamic factors such as seasonal variations present significant challenges for achieving long-term localization. In dynamic orchard environments, tree trunks remain static and unaffected by seasonal changes, making them ideal landmarks for localization in dynamic scenarios. Therefore, we propose a novel season-robust long-term localization method using trunk semantic features. Firstly, we introduce a semantic extraction module that integrates camera and LiDAR data to capture tree trunk semantic features within a simultaneous localization and mapping (SLAM) framework, thereby generating lightweight static maps that remain invariant to seasonal fluctuations. Upon re-entering the orchard environment, the robot utilizes a particle filtering framework to fuse LiDAR and GNSS data for long-term localization based on the lightweight map. This process involves performing Normal Distribution Transform (NDT) registration on the original point cloud to predict particle states, comparing the trunk point cloud with the lightweight map to compute particle weights from LiDAR measurements, and optionally integrating GNSS measurements to enhance localization accuracy. Finally, we conducted extensive field data collection over a prolonged period in a real orchard environment, encompassing experimental data from both winter and summer. The performance of our proposed localization method, along with its capability to mitigate the effects of seasonal variations, was validated through localization experiments conducted across different seasons. Quantitative results indicate that the average error of the fused localization is 0.16 m, and the root mean square error (RMSE) is 0.18 m.
