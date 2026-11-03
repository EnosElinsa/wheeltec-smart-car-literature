# Hierarchical Open-Vocabulary 3D Scene Graphs for Language-Grounded Robot Navigation

## Metadata

| Field | Value |
|---|---|
| ID | E48 |
| Title | Hierarchical Open-Vocabulary 3D Scene Graphs for Language-Grounded Robot Navigation |
| Authors | Abdelrhman Werby, Chenguang Huang, Martin Büchner, Abhinav Valada, and Wolfram Burgard |
| Venue | Proceedings of Robotics: Science and Systems (RSS 2024) |
| Year | 2024 |
| Type | conference |
| DOI | [10.15607/rss.2024.xx.077](https://doi.org/10.15607/rss.2024.xx.077) |
| Official URL | https://roboticsconference.org/2024/program/papers/77/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2024-HOV-SG-E48/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2024-HOV-SG-E48/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2024-HOV-SG-E48/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation, dataset-playback
- protocol_caveats: external-pose-source, cloud-model
- platform_class: legged
- platform: Boston Dynamics Spot (real two-story office); Habitat agent on HM3DSem
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task
- sensors: Azure Kinect RGB-D camera; 3D LiDAR for FAST-LIO2 poses with loop closure
- compute: not reported (CLIP ViT-H-14, SAM, DBSCAN, GPT-3.5 queries; no CPU or GPU, mapping or query time)
- compute_location: not-reported
- summary_result: Real Spot, two-story office: object queries retrieved 29/41 (70.7%) and navigated 23/41 (56.1%); storage 1493 MB versus 6068 MB for VLMaps over eight scenes.
- summary_limitation: The authors state that graph construction is time-consuming and unsuitable for real-time mapping, and that the method assumes a static environment.
- survey_included: yes
- verification_level: light

## Problem

Dense point-wise vision-language feature maps need much storage and lack floor and room concepts, which makes it hard to ground instructions with nested spatial qualifiers in navigable object locations.

## Mechanism

Given RGB-D, accurate odometry, and a global reference point cloud, SAM masks are back-projected and merged into 3D segments through an overlap graph. CLIP features of the full frame, the crop with background, and the mask without background are weighted and projected onto reference points; DBSCAN keeps the majority cluster as the object feature. Floors are split by a height histogram and rooms by BEV morphology and watershed; rooms are classified with CLIP features of 10 K-means representative views. The result is a building-floor-room-object hierarchy with a cross-floor Voronoi navigation graph. GPT-3.5 decomposes an instruction into floor, room, and object and retrieves level by level.

## Baselines and controls

- ConceptFusion and ConceptGraphs for Replica and ScanNet semantic segmentation, with matched OVSeg and ViT-H-14 backbones.
- MinkowskiNet trained on full ScanNet as a privileged supervised reference.
- Hydra for HM3DSem region segmentation.
- GPT-3.5 and GPT-4 for room classification, privileged (ground-truth object classes) and unprivileged (HOV-SG predicted classes).
- VLMaps and ConceptGraphs for object semantic AUC top-k and storage; ConceptGraphs gets privileged floor information for hierarchical queries.
- Ablations of DBSCAN and of CLIP features with and without background.

## Platform and setup

- Mapping and semantics: 8 Replica scenes and 5 ScanNet scenes.
- HM3DSem: 8 scenes with 1-3 floors, random walks collected manually and mapped with accurate odometry; Habitat navigation in already mapped scenes.
- Real world: Boston Dynamics Spot in a two-story office; RGB-D and LiDAR data are collected first to build the map, then 41 object, 9 room, and 2 floor language queries are executed (p. 10). No wheeled hardware evidence.

## Evidence type and transfer

Offline semantic and retrieval evaluation on recorded RGB-D datasets and simulated scans, Habitat navigation in mapped scenes, and real Spot retrieval and navigation statistics. The scene graph is static and prebuilt; there is no online exploration of unknown space or long-term dynamic update.

## Sensors

The real Spot carries a calibrated Azure Kinect RGB-D camera and a 3D LiDAR; FAST-LIO2 with loop closure gives poses, and the extrinsics give camera poses (p. 10). The method relies on accurate odometry and a reference point cloud. The cross-floor graph connects floors through camera trajectories already recorded on the stairs; it does not discover stair traversability autonomously.

## Compute and latency

The models are CLIP ViT-H-14 (1024-dimensional) with an OVSeg ViT-L-14 comparison, SAM, DBSCAN, and GPT-3.5 queries. Query decomposition depends on the external GPT-3.5 service; hosting and network/query latency are not reported, so all-onboard operation is not established. The main text reports no CPU or GPU model, mapping or query time, or real-time rate. The authors state that graph construction is time-consuming and unsuitable for real-time mapping (p. 11). Table VII reports representation storage in MB, not peak runtime memory.

## Key quantitative results

- Table I, ViT-H-14: Replica mIoU / F-mIoU / mAcc 0.231 / 0.386 / 0.304; ScanNet 0.222 / 0.303 / 0.431; ConceptGraphs mIoU 0.18 / 0.16; supervised MinkowskiNet on ScanNet mIoU 0.42 remains higher (p. 6, Table I).
- Table II: floor count and boundaries correct in all 8 HM3DSem scenes at a 0.5 m threshold; room region precision 84.10% and recall 83.59% versus Hydra 86.18% / 77.55% (p. 7, Table II).
- Table III: room classification strict / human-approximate accuracy, HOV-SG 73.93 / 84.10%, predicted objects with GPT-4 59.47 / 62.55%, ground-truth objects with GPT-4 79.86 / 84.25%; all methods use ground-truth room regions (p. 8, Table III).
- Table IV: AUC top-k over 1624 classes with IoU > 50% matched objects, HOV-SG 84.88, ConceptGraphs 84.07, VLMaps 56.20; at top-250 / 500 HOV-SG 69.95 / 80.86 is slightly below ConceptGraphs 70.85 / 81.55 (p. 9, Table IV).
- Table V: (object, room, floor) retrieval 28.00% versus 16.31% for ConceptGraphs with privileged floors, navigation 37.32%; (object, room) retrieval 31.48% versus 29.26%, navigation 40.41%. Retrieval uses top-5 at IoU > 0.1, and navigation success (< 1 m) differs from retrieval (p. 10, Table V).
- Table VI, real Spot: objects 41 queries, retrieval 29 (70.7%), navigation 23 (56.1%); rooms 5 of 9 (55.6%) for both; floors 2 of 2 (100%) (p. 10, Table VI).
- Table VII: total storage over 8 scenes VLMaps 6068 MB, ConceptGraphs 1638 MB, HOV-SG 1493 MB, about 75.4% below VLMaps and 8.9% below ConceptGraphs; in scene 00862 HOV-SG uses 479 MB versus 474 MB for ConceptGraphs (p. 11, Table VII).
- Table VIII: Replica mIoU without DBSCAN 0.212 versus 0.231 for the full method (p. 11, Table VIII).

## Stated limitations

- Graph construction is time-consuming, which makes the method unsuitable for real-time mapping (p. 11).
- The method assumes a static environment and cannot handle dynamic environments (p. 11).

## Transfer conditions

Legacy reviewer observations:
- The legacy card records room-segmentation failures on mixed kitchen and living-room layouts, and a target behind a wall but within 1 m counted as a failure; these notes have no verified page and are not attributed here as author-stated limitations.
- A prebuilt global map, accurate localization, and recorded stair trajectories are prerequisites; this differs from unknown-environment exploration such as VLFM, and stair reachability was not tested on a wheeled platform.
- Room classification uses ground-truth regions, and the approximate accuracy relies on human judgment.
- The object evaluation keeps only predictions matched at IoU > 50%, which excludes missed or badly segmented objects; VLMaps borrows HOV-SG masks, and AUC is not a full retrieval or navigation success rate.
- Hierarchical retrieval depends on correct GPT-3.5 decomposition and CLIP embeddings; a wrong room choice propagates to the object. Nine room and two floor queries on hardware do not support broad generalization.
- The 75% reduction is relative to the dense VLMaps representation; it is not a 75% runtime-memory reduction or a speedup.
- The 13-page PDF has the main text and references only; the supplementary sections cited as S.* are not included and were not read.

## Code and data

The paper provides code, the evaluation protocol, and trial videos at https://hovsg.github.io (p. 1, 11). Replica, ScanNet, and HM3DSem are public benchmarks. The current completeness of the resources was not checked, and the code was not run.

## Version family

The RSS 2024 paper and its project page or preprint of the same title count as one work. The paper does not claim to extend an earlier conference version. ConceptGraphs and VLMaps are baselines, not versions of this work.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | qualifies | moderate | Sec. V, p. 11 | "it assumes a static environment and thus cannot handle dynamic environments." |
| C6 | qualifies | moderate | Sec. V, p. 11 | "time-consuming, rendering the method unsuitable for real-time mapping." |

## Page-cited excerpts

- **p. 11, Sec. V Conclusion.** "time-consuming, rendering the method unsuitable for real-time mapping."
  The authors state that mapping is not real-time; query-time navigation does not imply real-time map updates.
- **p. 11, Sec. V Conclusion.** "it assumes a static environment and thus cannot handle dynamic environments."
  A static environment is an assumption; long-term dynamic maintenance is not shown.
- **p. 7, Sec. IV-B Scene Graph Evaluation on Habitat 3D Semantics.** "all methods rely on ground truth room segmentation"
  The room-classification comparison uses ground-truth regions, so 84.10% is not a full-stack room-understanding rate.

## Survey-usable statements

### Supported

- A floor-room-object open-vocabulary scene graph supports language queries with spatial qualifiers and cuts representation storage by about 75% relative to dense VLMaps features over eight HM3DSem scenes.
- On a real Spot in a two-story office, hierarchical queries retrieved 29 of 41 objects and navigated to 23 of 41.

### Not supported

- HOV-SG maps in real time or handles dynamic scenes: the authors state the opposite.
- HOV-SG beats ConceptGraphs at every rank: it is slightly lower at top-250 and top-500, and it uses more storage in scene 00862.
- Floor recognition is reliable in general: two real floor queries and eight simulated scenes.
- The 84.10% room accuracy is end to end: it uses ground-truth room regions.
- The method was validated on a wheeled robot: the hardware is a legged Spot.

## Verification log

- 2026-11-02 | host: Codex | scope: independent light-audit follow-up; query-decomposition dependency and limitation attribution checked; numerical results not re-verified | corrections: added cloud-model caveat and unreported hosting/latency boundary; moved unlocated legacy notes to Transfer conditions
- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; the legacy Table VI, Table VII, and Table I row-string excerpts were moved to Key quantitative results instead of excerpts (the Table I row string is not in paper.md); the room-segmentation and behind-the-wall limitations have no recorded page
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/94ed309956e8503bc69906cd/

## Original abstract

Recent open-vocabulary robot mapping methods enrich dense geometric maps with pre-trained visual-language features. While these maps allow for the prediction of point-wise saliency maps when queried for a certain language concept, largescale environments and abstract queries beyond the object level still pose a considerable hurdle, ultimately limiting languagegrounded robotic navigation. In this work, we present HOV-SG, a hierarchical open-vocabulary 3D scene graph mapping approach for language-grounded indoor robot navigation. Leveraging open-vocabulary vision foundation models, we first obtain state-of-the-art open-vocabulary segment-level maps in 3D and subsequently construct a 3D scene graph hierarchy consisting of floor, room, and object concepts, each enriched with openvocabulary features. Our approach is able to represent multistory buildings and allows robotic traversal of those using a cross-floor Voronoi graph. HOV-SG is evaluated on three distinct datasets and surpasses previous baselines in open-vocabulary semantic accuracy on the object, room, and floor level while producing a 75% reduction in representation size compared to dense open-vocabulary maps. In order to prove the efficacy and generalization capabilities of HOV-SG, we showcase successful long-horizon language-conditioned robot navigation within realworld multi-story environments. We provide code and trial video data at: https://hovsg.github.io.
