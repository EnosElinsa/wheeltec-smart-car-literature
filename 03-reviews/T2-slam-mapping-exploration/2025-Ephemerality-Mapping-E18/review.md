# Ephemerality Meets Lidar-Based Lifelong Mapping

## Metadata

| Field | Value |
|---|---|
| ID | E18 |
| Title | Ephemerality Meets Lidar-Based Lifelong Mapping |
| Authors | Hyeonjae Gil, Dongjae Lee, Giseop Kim, and Ayoung Kim |
| Venue | 2025 IEEE International Conference on Robotics and Automation (ICRA), pp. 3312-3319 |
| Year | 2025 |
| Type | conference |
| DOI | [10.1109/icra55743.2025.11127618](https://doi.org/10.1109/icra55743.2025.11127618) |
| Official URL | https://doi.org/10.1109/icra55743.2025.11127618 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2025-Ephemerality-Mapping-E18/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2025-Ephemerality-Mapping-E18/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2025-Ephemerality-Mapping-E18/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: LT-Parking (six sessions), MulRan DCC and KAIST, SemanticKITTI 00/01/02, MulRan 2019 and HeLiPR 2023; carriers not recorded in the legacy extraction
- boundary_platform: yes
- degradation: dynamic-objects, scene-change
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: 3D LiDAR with per-session SC-LIO-SAM trajectories (SuMa poses for KITTI)
- compute: not reported
- compute_location: not-reported
- summary_result: On MulRan DCC alignment, ELite reaches 0.942 AC, 0.111 RMSE, and 0.162 CD versus 0.738, 0.182, and 0.306 for LT-mapper.
- summary_limitation: The authors evaluate the cross-session map update only qualitatively, and a threshold tailors the preservation versus update trade-off to the application.
- survey_included: yes
- verification_level: light

## Problem

Quasi-static structures change between sessions and make the map outdated. Local removal of dynamic objects and long-term global updates need to be handled together.

## Mechanism

Per-scan ray-based Bayesian local ephemerality and cross-session global ephemerality. Alignment starts from Scan Context and refines with forward and backward persistence-weighted GICP. Five update classes and density factors maintain a lifelong map, a static map, and a delta map.

## Baselines and controls

Registration: ICP and LT-mapper. Dynamic object removal: Removert, ERASOR, DUFO, and BeautyMap. KITTI runs with the KITTI-provided and the SuMa trajectories; an ablation of the threshold tau.

## Platform and setup

Replay of LT-Parking (six sessions), MulRan DCC and KAIST, and SemanticKITTI 00, 01, and 02. Map update from MulRan 2019 to HeLiPR 2023.

## Evidence type and transfer

Replay of real cross-session data. Inter-session changes have no labels, so the update evaluation is qualitative. There is no closed-loop navigation on a real robot.

## Sensors

3D LiDAR with per-session SC-LIO-SAM trajectories, plus KITTI and SuMa poses. No semantic network is needed; human motion is not modeled explicitly.

## Compute and latency

The text reports no hardware, complete runtime, or peak memory, so low-compute real-time deployment cannot be inferred from the mapping algorithm.

## Key quantitative results

- MulRan DCC alignment, ELite versus LT-mapper: AC 0.942 versus 0.738, RMSE 0.111 versus 0.182, CD 0.162 versus 0.306 (p. 5, Table I).
- SemanticKITTI 02 with SuMa poses and tau = 0.5: F1 86.77% for ELite versus 84.04% for BeautyMap (p. 5, Table II).
- Counterexample: on SemanticKITTI 00, DUFO reaches 98.64%, above ELite at 98.41% (p. 5, Table II).

## Stated limitations

- The map update across sessions has no inter-session labels and is evaluated qualitatively (p. 4).
- The threshold tau tailors the trade-off between preservation and update to the application (p. 6).

## Transfer conditions

Legacy reviewer observations (not located in the paper): errors of the initial loop closure affect alignment, and removal results are sensitive to the input poses. With few observations, a new wall is hard to tell from a parked object. Map changes across years are shown only qualitatively, and the heat map for navigation is a suggestion, not closed-loop evidence. A wheeled reuse needs a 3D LiDAR and a per-session SLAM trajectory.

## Code and data

Code: https://github.com/dongjae0107/ELite (p. 1). The datasets are public. Running the repository and the completeness of any self-collected data were not checked.

## Version family

ELite (ICRA 2025) is an independent work. LT-mapper is a baseline; ProbPer-LiLo (E16) and the lifelong 3D mapping work are not merged into its family.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Abstract, p. 1 | "Map elements are typically classified as static or dynamic, but cases like parked cars indicate the need for more detailed categories than binary." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | qualifies | weak | Map update evaluation, p. 4 | "we conduct a qualitative evaluation" |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 4, Map update evaluation.** "we conduct a qualitative evaluation"
  The cross-session update has no labeled quantitative ground truth; the same passage states the lack of inter-session labels.
- **p. 6, Threshold.** "This threshold acts as a convenient way to tailor"
  The threshold is an application trade-off, so the update is not parameter-free.
- **p. 1, Abstract.** "Map elements are typically classified as static or dynamic, but cases like parked cars indicate the need for more detailed categories than binary."
  The authors' motivation for two-stage ephemerality.

## Survey-usable statements

### Supported

- Two-stage ephemerality improves multi-session alignment over LT-mapper on MulRan DCC (AC 0.942 versus 0.738; numbers from a light review; re-check before citing).

### Not supported

- ELite is best in dynamic object removal on every sequence: DUFO is higher on SemanticKITTI 00 (98.64% versus 98.41%).
- The long-term map update is quantitatively validated: it is evaluated qualitatively.
- ELite improves robot navigation: no closed-loop navigation is reported.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; no legacy quote dropped; reviewer observations moved from limitations to Transfer conditions
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/0f743491258433d9004ac8e7/

## Original abstract

Lifelong mapping is crucial for the long-term deployment of robots in dynamic environments. In this paper, we present ELite, an ephemerality-aided LiDAR-based lifelong mapping framework which can seamlessly align multiple session data, remove dynamic objects, and update maps in an end-toend fashion. Map elements are typically classified as static or dynamic, but cases like parked cars indicate the need for more detailed categories than binary. Central to our approach is the probabilistic modeling of the world into two-stage ephemerality, which represent the transiency of points in the map within two different time scales. By leveraging the spatiotemporal context encoded in ephemeralities, ELite can accurately infer transient map elements, maintain a reliable up-to-date static map, and improve robustness in aligning the new data in a more finegrained manner. Extensive real-world experiments on long-term datasets demonstrate the robustness and effectiveness of our system. The source code is publicly available for the robotics community: https://github.com/dongjae0107/ELite.
