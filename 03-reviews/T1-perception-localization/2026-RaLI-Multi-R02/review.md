# Range-Aided LiDAR-Inertial Multi-Vehicle Localization and Mapping in Degenerate Environments

## Metadata

| Field | Value |
|---|---|
| ID | R02 |
| Title | Range-Aided LiDAR-Inertial Multi-Vehicle Localization and Mapping in Degenerate Environments |
| Authors | Zhe Jin, and Chaoyang Jiang |
| Venue | IEEE Transactions on Intelligent Vehicles |
| Year | 2026 (DOI year 2024) |
| Type | journal |
| DOI | [10.1109/tiv.2024.3360286](https://doi.org/10.1109/tiv.2024.3360286) |
| Official URL | https://ieeexplore.ieee.org/document/10417045/ |
| Theme folder | T1-perception-localization |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-RaLI-Multi-R02/paper.pdf` and `02-fulltext/T1-perception-localization/2026-RaLI-Multi-R02/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2026-RaLI-Multi-R02/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: multi-robot
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: differential-drive
- platform: Unmanned ground vehicles with differential steering and spring-damped suspension; two-vehicle open-square and three-vehicle complex-environment experiments (p. 8).
- boundary_platform: no
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: RoboSense RS-LiDAR-16, Nooploop UWB ranging and Xsens IMU on each vehicle (p. 8)
- compute: Runtime analysis in Sec. IV-F (p. 13); processor and online execution not inspected in this reading.
- compute_location: not-reported
- summary_result: Range constraints correct pose along the detected degenerate direction and support a low-drift shared map in degenerate multi-vehicle experiments (p. 13).
- summary_limitation: Assumes LiDAR odometry remains non-degenerate in at least one horizontal direction (p. 7).
- survey_included: yes
- verification_level: light

## Problem

LiDAR-inertial odometry drifts in narrow, self-similar environments, and multi-vehicle maps inherit that drift.

## Mechanism

Feature-normal distributions detect degenerate level and direction; inter-vehicle range measurements then correct the pose along that direction. A dynamically chosen anchor vehicle stops, serves as a range anchor and temporary central server, optimizes a global pose graph and broadcasts the merged map (pp. 2, 6-8).

## Baselines and controls

DLO, A-LOAM, LeGO-LOAM, FAST-LIO2, LIO-SAM and LAMP, plus an ablation of degeneration detection (pp. 10-12).

## Platform and setup

Three experiments: odometry analysis with UWB-anchor reference, two vehicles in an open square, and three vehicles in a complex environment (p. 8). Unmanned ground vehicles with differential steering and spring-damped suspension; two-vehicle open-square and three-vehicle complex-environment experiments (p. 8).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Recorded or online robot data in the authors' environments; the reading did not establish whether a controller consumed the shared estimate.

## Sensors

RoboSense RS-LiDAR-16, Nooploop UWB ranging and Xsens IMU on each vehicle (p. 8).

## Compute and latency

Runtime analysis in Sec. IV-F (p. 13); processor and online execution not inspected in this reading.

## Key quantitative results

- Several LiDAR baselines fail or drift in the degenerate experiments, while the range-aided system produces a low-drift global map (pp. 10-13).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The degeneration correction assumes non-degenerate odometry in at least one horizontal direction (p. 7).
- Localization errors are assumed to stem mainly from the degenerate direction (p. 11).

## Transfer conditions

Requires inter-vehicle ranging, a stopped anchor vehicle and a centralized exchange; range geometry and anchor availability limit the correction.

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

- **p. 7, Sec. III-C.** "We assume that LiDAR odometry remains non-degenerate in at least one direction of the horizontal plane."
  States the observability condition of the correction.
- **p. 8, Sec. IV-A.** "Specifically, our experimental vehicles equipped with differential steering and spring-damped suspension, and there is high friction between rubber tires and tiled floors."
  Identifies the drive type and contact conditions of the evaluated vehicles.

## Survey-usable statements

### Supported

- Directional range correction after explicit degeneracy detection is evaluated on a wheeled multi-vehicle team.

### Not supported

- The correction is not shown for degeneracy in all horizontal directions or under communication loss.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 6, 7, 8, 10, 11, 13; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

This paper presents a range-aided LiDAR-inertial multi-vehicle localization and mapping system (RaLI-Multi). Firstly, we propose a LiDAR-inertial odometry with multi-metric weights by fusing observations from an inertial measurement unit (IMU) and a light detection and ranging sensor (LiDAR). The degenerate level and direction are evaluated by analyzing the distribution of normal vectors of feature point clouds and are used to activate the degeneration correction module in which range measurements correct the pose estimation from the degeneration direction. We then design a multi-vehicle SLAM system in which a centralized vehicle receives local maps of each vehicle and the range measurements between vehicles to optimize a global pose graph. The global map is broadcast to other vehicles for localization and mapping updates, and the centralized vehicle is dynamically fungible. Finally, we provide three experiments to verify the effectiveness of the proposed RaLI-Multi. The results show its superiority in degenerate environments.
