# Visual localization in 3D maps: comparing point cloud, mesh, and NeRF representations

## Metadata

| Field | Value |
|---|---|
| ID | S26 |
| Title | Visual localization in 3D maps: comparing point cloud, mesh, and NeRF representations |
| Authors | Zhang, Lintong and Tao, Yifu and Lin, Jiarong and Zhang, Fu and Fallon, Maurice |
| Venue | Autonomous Robots |
| Year | 2026 |
| Type | journal |
| DOI | [10.1007/s10514-025-10232-5](https://doi.org/10.1007/s10514-025-10232-5) |
| Official URL | https://link.springer.com/10.1007/s10514-025-10232-5 |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-Map-Representation-Loc-S26/paper.pdf` and `02-fulltext/T1-perception-localization/2026-Map-Representation-Loc-S26/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2026-Map-Representation-Loc-S26/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: handheld
- platform: Frontier multi-sensor unit on acquired indoor/outdoor walking sequences; not an executed autonomous navigation controller (p. 10).
- boundary_platform: yes
- degradation: scene-change, visual-degradation
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Query camera image; color point-cloud/mesh/NeRF prior map; Hesai LiDAR and cameras used for mapping/reference
- compute: GPU-equipped mobile laptop for localization; prior-map creation and synthetic database generation are separate preparation stages (pp. 1, 5, 10).
- compute_location: desktop-offline
- summary_result: Synthetic-view databases permit camera localization across prior-map representations and unseen travel directions.
- summary_limitation: Missing prior-map regions force localization failure; rendered viewpoint coverage, gradual scene change and low-texture imagery remain limitations (p. 18).
- survey_included: yes
- verification_level: light

## Problem

Dense maps have differing rendering properties, making single-image localization and reverse-direction reuse representation dependent.

## Mechanism

Samples viewpoints in a prior 3D map, renders RGB/depth databases, retrieves candidate views using learned descriptors, and estimates query pose from geometric feature matching (pp. 5, 17-18).

## Baselines and controls

Point cloud, textured mesh and NeRF representations; HLoc, COLMAP and MeshLoc are listed in the evaluation structure; no numerical ranking retained.

## Platform and setup

Frontier multi-sensor unit on acquired indoor/outdoor walking sequences; not an executed autonomous navigation controller (p. 10).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Account for map acquisition, rendering effort and retrieval coverage; a localization success rate does not establish closed-loop mission recovery.

## Sensors

Query camera image; color point-cloud/mesh/NeRF prior map; Hesai LiDAR and cameras used for mapping/reference.

## Compute and latency

GPU-equipped mobile laptop for localization; prior-map creation and synthetic database generation are separate preparation stages (pp. 1, 5, 10).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Missing prior-map regions force localization failure; rendered viewpoint coverage, gradual scene change and low-texture imagery remain limitations (p. 18).

## Transfer conditions

Account for map acquisition, rendering effort and retrieval coverage; a localization success rate does not establish closed-loop mission recovery.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Citation is explicitly derived from publisher RIS/metadata and checked against Crossref; formal issue year 2026. Article identifiers remain in the citation record. Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 18, Selected source passage.** "If a region of the environment is missing from the prior map, localization will fail in that area"
  Adds a representation/preparation tradeoff to the relocalization comparison and bounds claims of reusable prior maps.

## Survey-usable statements

### Supported

- Synthetic-view databases permit camera localization across prior-map representations and unseen travel directions. Adds a representation/preparation tradeoff to the relocalization comparison and bounds claims of reusable prior maps.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Account for map acquisition, rendering effort and retrieval coverage; a localization success rate does not establish closed-loop mission recovery.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 5, 10, 17, 18; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Recent advances in mapping techniques have enabled the creation of highly accurate dense 3D maps during robotic missions, such as point clouds, meshes, or NeRF-based representations. These developments present new opportunities for reusing these maps for localization. However, there remains a lack of a unified approach that can operate seamlessly across different map representations. This paper presents and evaluates a global visual localization system capable of localizing a single camera image across various 3D map representations built using both visual and lidar sensing. Our system generates a database by synthesizing novel views of the scene, creating RGB and depth image pairs. Leveraging the precise 3D geometric map, our method automatically defines rendering poses, reducing the number of database images while preserving retrieval performance. To bridge the domain gap between real query camera images and synthetic database images, our approach utilizes learning-based descriptors and feature detectors. We evaluate the system's performance through extensive real-world experiments conducted in both indoor and outdoor settings, assessing the effectiveness of each map representation and demonstrating its advantages over traditional structure-from-motion (SfM) localization approaches. The results show that all three map representations can achieve consistent localization success rates of 55% and higher across various environments. NeRF synthesized images show superior performance, localizing query images at an average success rate of 72%. Furthermore, we demonstrate an advantage over SfM-based approaches that our synthesized database enables localization in the reverse travel direction which is unseen during the mapping process. Our system, operating in real-time on a mobile laptop equipped with a GPU, achieves a processing rate of 1 Hz.
