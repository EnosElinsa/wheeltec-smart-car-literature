# Robust Lifelong Indoor LiDAR Localization Using the Area Graph

## Metadata

| Field | Value |
|---|---|
| ID | S03 |
| Title | Robust Lifelong Indoor LiDAR Localization Using the Area Graph |
| Authors | Xie, Fujing and Schwertfeger, Sören |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2023.3334158](https://doi.org/10.1109/lra.2023.3334158) |
| Official URL | https://ieeexplore.ieee.org/document/10321673/ |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2024-AGLoc-S03/paper.pdf` and `02-fulltext/T1-perception-localization/2024-AGLoc-S03/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2024-AGLoc-S03/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: mixed
- platform: Two acquired indoor LiDAR sequences; carrier drivetrain is not established by the selected passages (p. 6).
- boundary_platform: yes
- degradation: scene-change, lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Hesai PandarQT LiDAR; WiFi/barometer initialization; LIO-SAM reference and AMCL auxiliary odometry
- compute: Intel Core i5-9300H laptop, C++/ROS evaluation (p. 6).
- compute_location: desktop-offline
- summary_result: Architecture-based localization reduces dependence on movable clutter under a supplied Area Graph.
- summary_limitation: No additional author-stated limitation was retained from the selected discussion; initialization and map assumptions are reported as transfer conditions.
- survey_included: yes
- verification_level: light

## Problem

Clutter changes make detailed indoor maps expensive to maintain while repeated corridor geometry weakens matching.

## Mechanism

Matches clutter-filtered scans to Area Graph wall/door polygons, uses WiFi/barometer to restrict global hypotheses, and applies weighted point-to-line ICP with corridorness downsampling (p. 2).

## Baselines and controls

AMCL with occupancy-grid or rendered Area Graph maps and different odometry inputs; LeGO-LOAM and filtering/weighting ablations (pp. 6-7).

## Platform and setup

Two acquired indoor LiDAR sequences; carrier drivetrain is not established by the selected passages (p. 6).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Needs a structural map and broad initial location; LIO-SAM is the pose reference, so the benchmark is not an independent external-ground-truth test.

## Sensors

Hesai PandarQT LiDAR; WiFi/barometer initialization; LIO-SAM reference and AMCL auxiliary odometry.

## Compute and latency

Intel Core i5-9300H laptop, C++/ROS evaluation (p. 6).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

No additional author-stated limitation was retained from the selected discussion; initialization and map assumptions are reported as transfer conditions.

## Transfer conditions

Needs a structural map and broad initial location; LIO-SAM is the pose reference, so the benchmark is not an independent external-ground-truth test.

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

- **p. 6, Selected source passage.** "We use LIO-SAM’s [10] trajectory as our ground truth"
  Qualifies claims that long-term localization always requires dense-map revision; emphasizes prior semantics and reference dependence.

## Survey-usable statements

### Supported

- Architecture-based localization reduces dependence on movable clutter under a supplied Area Graph. Qualifies claims that long-term localization always requires dense-map revision; emphasizes prior semantics and reference dependence.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Needs a structural map and broad initial location; LIO-SAM is the pose reference, so the benchmark is not an independent external-ground-truth test.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 2, 6, 7; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Lifelong indoor localization in a given map is the basis for navigation of autonomous mobile robots. In this letter, we address the problem of robust localization in cluttered indoor environments like office spaces and corridors using 3D LiDAR point clouds in a given Area Graph, which is a hierarchical, topometric semantic map representation that uses polygons to demark areas such as rooms, corridors or buildings. This representation is very compact, can represent different floors of buildings through its hierarchy and provides semantic information that helps with localization, like poses of doors and glass. In contrast to this, commonly used map representations, such as occupancy grid maps or point clouds, lack these features and require frequent updates in response to environmental changes (e.g. moved furniture), unlike our approach, AGLoc, which matches against lifelong architectural features such as walls and doors. For that we apply filtering to remove clutter from the 3D input point cloud and then employ further scoring and weight functions for localization. Given a broad initial guess from WiFi and barometer localization, our experiments show that our global localization and the weighted point to line ICP pose tracking perform very well, even when compared to localization and SLAM algorithms that use the current, feature-rich cluttered map for localization.
