# NVMS-SLAM: Normal Vector-Based Multi-Session LiDAR SLAM in Indoor Environments

## Metadata

| Field | Value |
|---|---|
| ID | S01 |
| Title | NVMS-SLAM: Normal Vector-Based Multi-Session LiDAR SLAM in Indoor Environments |
| Authors | Ma, Yongxin and Zhao, Chengwei and Xu, Jie and Li, Yixuan and Zhang, Xuanxuan and Yuan, Shenghai and Xie, Lihua |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2026.3682733](https://doi.org/10.1109/tase.2026.3682733) |
| Official URL | https://ieeexplore.ieee.org/document/11479301/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-NVMS-SLAM-S01/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-NVMS-SLAM-S01/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-NVMS-SLAM-S01/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: multi-robot
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: legged
- platform: Unitree Go2 with MID-360 in office buildings; public handheld SLABIM sequences and Gazebo simulation (pp. 7, 10).
- boundary_platform: yes
- degradation: data-association-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: 3D LiDAR and IMU; surface normals derived from point clouds
- compute: Intel Core i9-10940X desktop; online odometry/pose-graph stages and offline normal-vector bundle adjustment (pp. 7, 11).
- compute_location: desktop-offline
- summary_result: Normal-aware association preserves thin-wall structure in the inspected multi-session mapping tests.
- summary_limitation: Dynamic-object removal and larger multi-floor deployments are identified as future work (p. 11).
- survey_included: yes
- verification_level: light

## Problem

Opposite faces of thin indoor walls can be associated or voxelized together, destroying useful geometric constraints.

## Mechanism

Stores primary/secondary normal-bearing surfaces, uses density-encoded scan context for inter-session matching, and refines a joint pose graph with normal-aware bundle adjustment (pp. 3-7).

## Baselines and controls

Disco-SLAM, DCL-SLAM and LAMM in multi-session comparisons; continuity/initialization and bundle-adjustment ablations (pp. 7, 10).

## Platform and setup

Unitree Go2 with MID-360 in office buildings; public handheld SLABIM sequences and Gazebo simulation (pp. 7, 10).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Separate online localization from offline map refinement; Go2 data do not establish wheeled closed-loop collision avoidance.

## Sensors

3D LiDAR and IMU; surface normals derived from point clouds.

## Compute and latency

Intel Core i9-10940X desktop; online odometry/pose-graph stages and offline normal-vector bundle adjustment (pp. 7, 11).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Dynamic-object removal and larger multi-floor deployments are identified as future work (p. 11).

## Transfer conditions

Separate online localization from offline map refinement; Go2 data do not establish wheeled closed-loop collision avoidance.

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

- **p. 11, Selected source passage.** "the NV-BA serves as an offline post-processing step"
  Adds a representation-specific data-association response to the persistent-map comparison; map consistency is not a demonstrated navigation safety outcome.

## Survey-usable statements

### Supported

- Normal-aware association preserves thin-wall structure in the inspected multi-session mapping tests. Adds a representation-specific data-association response to the persistent-map comparison; map consistency is not a demonstrated navigation safety outcome.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Separate online localization from offline map refinement; Go2 data do not establish wheeled closed-loop collision avoidance.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 4, 7, 10, 11; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Multi-session SLAM is essential for long-term robotic operations in indoor environments such as warehouses, office buildings, and industrial facilities. However, the thin walls separating enclosed spaces in such environments introduce a challenge known as the double-sided issue, where point clouds from opposite sides are mistakenly associated as a single surface during single-session mapping, and are prone to being grouped into the same voxel during voxelization in multi-session map fusion, leading to poor voxel planarity, which causes voxel invalidation and reduces the available constraints for global optimization. To address this, we propose NVMS-SLAM, a normal vector-based multi-session LiDAR SLAM system tailored for indoor environments. For single-session mapping, an extended voxel map is designed to preserve normal vector information and to distinguish between primary and secondary surfaces, thereby improving data association. At the multi-session level, a density-encoded indoor scan-context descriptor is introduced for robust loop closure. In addition, a two-stage global map fusion strategy is adopted, combining joint pose graph optimization and normal vector-based bundle adjustment to ensure globally consistent mapping. Experiments on simulated datasets and real-world environments demonstrate that NVMS-SLAM can effectively resolve the double-sided issue at both the single-session and multi-session stages. The code and datasets will be released on GitHub (https://github.com/lian-yue0515/NVMS-SLAM) for further research.
