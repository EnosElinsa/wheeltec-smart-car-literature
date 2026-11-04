# Efficiently closing loops in LiDAR-based SLAM using point cloud density maps

## Metadata

| Field | Value |
|---|---|
| ID | S35 |
| Title | Efficiently closing loops in LiDAR-based SLAM using point cloud density maps |
| Authors | Saurabh Gupta and Tiziano Guadagnino and Benedikt Mersch and Niklas Trekel and Meher V. R. Malladi and Cyrill Stachniss |
| Venue | The International Journal of Robotics Research |
| Year | 2026 |
| Type | journal |
| DOI | [10.1177/02783649261449269](https://doi.org/10.1177/02783649261449269) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649261449269 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-Density-Map-Loops-S35/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-Density-Map-Loops-S35/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-Density-Map-Loops-S35/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: Own instrumented-car/backpack recordings; public rooftop-car and Segway sequences; no single carrier dominates the selected settings (pp. 10-11).
- boundary_platform: yes
- degradation: scene-change, data-association-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR and locally consistent odometry; ground-aligned density projections and ORB descriptors
- compute: Loop retrieval/runtime is evaluated separately; processor placement not retained in this targeted reading.
- compute_location: desktop-offline
- summary_result: Density-map place recognition supports cross-session and heterogeneous-LiDAR map alignment in the inspected settings.
- summary_limitation: Depends critically on locally consistent odometry and a detectable ground plane; degenerate local maps and cluttered/off-road scenes can degrade performance (p. 28).
- survey_included: yes
- verification_level: light

## Problem

Cross-session and cross-LiDAR appearance changes and repeated geometry undermine reliable loop closure.

## Mechanism

Aggregates local maps using KISS-ICP, aligns them to a ground plane, preserves point density in bird-eye projections, prunes self-similar ORB features, and retrieves/aligns candidate maps (pp. 5-10).

## Baselines and controls

Public MulRan/HeLiPR/NCLT and self-recorded cross-sensor/temporal tests; ground-alignment and self-similarity pruning ablations are described.

## Platform and setup

Own instrumented-car/backpack recordings; public rooftop-car and Segway sequences; no single carrier dominates the selected settings (pp. 10-11).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Loop closure cannot be assumed to repair every corrupted front-end map; inspect projection geometry and candidate validation before accepting a global constraint.

## Sensors

LiDAR and locally consistent odometry; ground-aligned density projections and ORB descriptors.

## Compute and latency

Loop retrieval/runtime is evaluated separately; processor placement not retained in this targeted reading.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Depends critically on locally consistent odometry and a detectable ground plane; degenerate local maps and cluttered/off-road scenes can degrade performance (p. 28).

## Transfer conditions

Loop closure cannot be assumed to repair every corrupted front-end map; inspect projection geometry and candidate validation before accepting a global constraint.

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

- **p. 28, Selected source passage.** "The pipeline relies on locally consistent LiDAR odometry to generate local maps"
  Adds an efficient cross-sensor loop representation while exposing its dependence on the map consistency it is intended to improve.

## Survey-usable statements

### Supported

- Density-map place recognition supports cross-session and heterogeneous-LiDAR map alignment in the inspected settings. Adds an efficient cross-sensor loop representation while exposing its dependence on the map consistency it is intended to improve.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Loop closure cannot be assumed to repair every corrupted front-end map; inspect projection geometry and candidate validation before accepting a global constraint.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 5, 10, 11, 28; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Consistent maps are key for most autonomous mobile robots, and they often use SLAM approaches to build such maps. Loop closures via place recognition help to maintain accurate pose estimates by mitigating global drift, and are thus key for realizing an effective SLAM system. This paper presents a robust loop closure detection pipeline for outdoor SLAM with LiDAR-equipped robots. Our method handles various LiDAR sensors with different scanning patterns, fields of view, and resolutions. It generates local maps from LiDAR scans and aligns them using a ground alignment module to handle both planar and non-planar motion of the LiDAR, ensuring applicability across platforms. The method uses density-preserving bird’s-eye-view projections of these local maps and extracts ORB feature descriptors for place recognition. It stores the feature descriptors in a binary search tree for efficient retrieval, and self-similarity pruning addresses perceptual aliasing in repetitive environments. Extensive experiments on public and self-recorded datasets demonstrate accurate loop closure detection, long-term localization, and cross-platform multi-map alignment, agnostic to the LiDAR scanning patterns, fields of view, and motion profiles. We provide the code for our pipeline as open-source software at https://github.com/PRBonn/MapClosures.
