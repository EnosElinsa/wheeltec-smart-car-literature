# MM-LINS: A Multi-Map LiDAR-Inertial System for Over-Degenerate Environments

## Metadata

| Field | Value |
|---|---|
| ID | E08 |
| Title | MM-LINS: A Multi-Map LiDAR-Inertial System for Over-Degenerate Environments |
| Authors | Yongxin Ma, Jie Xu, Shenghai Yuan, Tian Zhi, Wenlu Yu, Jun Zhou, and Lihua Xie |
| Venue | IEEE Transactions on Intelligent Vehicles, vol. 10, no. 1, pp. 472-482 |
| Year | 2025 (online 2024) |
| Type | journal |
| DOI | [10.1109/tiv.2024.3414852](https://doi.org/10.1109/tiv.2024.3414852) |
| Official URL | https://ieeexplore.ieee.org/document/10557776/ |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2025-MM-LINS-E08/paper.pdf` and `02-fulltext/T1-perception-localization/2025-MM-LINS-E08/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2025-MM-LINS-E08/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: fault-recovery-deployment
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: road-vehicle
- platform: vehicle-mounted RS-LiDAR-16 rig on a campus (five sequences); handheld MID-360 rig in a factory; M2DGR, NCLT, UTBM, and UrbanLoco public sequences
- boundary_platform: yes
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: LiDAR and IMU (Livox MID-360 handheld; RS-LiDAR-16 with KY-INS180-A0 IMU on the vehicle)
- compute: Intel i7-9750H at 2.60 GHz; only module time fractions are reported
- compute_location: not-reported
- summary_result: On M2DGR 07-31 with injected over-degeneracy, MM-LINS reaches 0.322 m ATE versus 23.65 m for FAST-LIO2.
- summary_limitation: The authors state that map fusion accuracy drops significantly when the point clouds overlap only minimally.
- survey_included: yes
- verification_level: light

## Problem

Severe occlusion can make the local map drift irreversibly. The system needs to put the map to sleep, reinitialize, and fuse the maps again after revisiting a common area.

## Mechanism

Over-degeneracy is detected from the eigenvalues of the attitude and translation covariance of a FAST-LIO2-style filter. The active map is then stored as a sleeping map, and a dynamic initialization restarts the system from four LiDAR and IMU frames. In the back end, Scan Context with continuous temporal similarity detects inter-map overlap, and several groups of enhanced constraints fuse the maps through pose graph optimization.

## Baselines and controls

FAST-LIO2, VOXEL-MAP, LIO-SAM, and FAST-LIO-SLAM/SAM; ablations without pose graph optimization and with ordinary pose graph optimization; the degeneracy detection of Zhang and static initialization as alternatives.

## Platform and setup

Seven sequences from M2DGR, NCLT, UTBM, and UrbanLoco with over-degeneracy injected by downsampling. Self-collected data: a handheld rig in a factory and a vehicle on a campus, with the LiDAR physically covered.

## Evidence type and transfer

Real data with artificial degeneracy in playback, and handheld and vehicle-mounted data with physical occlusion. The self-collected ground truth is only the closure error between identical start and end points, not a full-trajectory ATE.

## Sensors

Handheld: Livox MID-360. Vehicle: RS-LiDAR-16 with a KY-INS180-A0 IMU.

## Compute and latency

Intel i7-9750H at 2.60 GHz. Table V gives module time fractions, which do not replace a full per-frame latency. Whether the computer was onboard is not recorded in the legacy extraction.

## Key quantitative results

- M2DGR 07-31: ATE 0.322 m for MM-LINS versus 23.65 m for FAST-LIO2 (legacy location: Table I, page 7; table values not located in the PDF text layer).
- UTBM 04-18: ATE 5.033 m for MM-LINS (legacy location: Table I, page 7; not located in the PDF text layer).
- Factory field test: end-point errors 0.18, 0.05, and 0.31 m (legacy location: Table II; not located in the PDF text layer).
- Campus field test with pose graph optimization: end-point errors 0.092, 1.295, 0.093, 0.051, and 0.132 m; Campus-2 at 1.295 m contradicts the text's summary of errors below 15 cm (legacy location: Table III, page 9; not located in the PDF text layer).

## Stated limitations

- When the point clouds overlap only minimally, map fusion accuracy drops significantly (p. 9).
- Part of the public datasets were modified to simulate over-degeneracy, so those results rest on injected degradation (p. 6).
- The self-collected ground truth is the consistency of start and end points (p. 7).

## Transfer conditions

Legacy reviewer observations: recovery requires revisiting a common area, so the method does not guarantee a continuous accurate pose inside the degenerate segment. The empirical thresholds depend on the sensor. Artificial downsampling is not the same as natural degradation. The text's below-15-cm summary has a counterexample in Table III. A wheeled reuse needs re-tuned degeneracy thresholds and routes that revisit mapped areas.

## Code and data

Code: https://github.com/lian-yue0515/MM-LINS (p. 1). The public benchmarks are available; whether the self-collected data are public was not checked.

## Version family

The paper appeared online in 2024 and in the 2025 volume; both are one MM-LINS paper, dated here by the volume year 2025 and counted once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "Such scenarios can result in over-degeneracy, causing the map to drift." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | qualifies | moderate | Conclusion, p. 9 | "If there is minimal overlap in point clouds, the accuracy of map fusion will be significantly reduced." |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 6, Public datasets.** "we opted to modify part of the public datasets to simulate over-degeneracy."
  The public-dataset results include injected degradation.
- **p. 7, Field testing.** "we ensured consistent start and end points for each test, serving as our ground truth measurement."
  The quantitative reference is the start and end point only.
- **p. 8, Campus field test.** "limiting the error to less than 15 centimeters."
  The text's summary; Table III has Campus-2 at 1.295 m, so it does not hold for every campus sequence.
- **p. 9, Conclusion.** "If there is minimal overlap in point clouds, the accuracy of map fusion will be significantly reduced."
  Recovery depends on map overlap.

## Survey-usable statements

### Supported

- Storing the drifting map as a sleeping map, reinitializing, and fusing maps after revisits recovers a consistent map in the authors' tests, with 0.322 m versus 23.65 m (FAST-LIO2) ATE on M2DGR 07-31 with injected degeneracy.

### Not supported

- MM-LINS keeps campus end-point errors below 15 cm: Campus-2 has 1.295 m.
- MM-LINS keeps an accurate pose during over-degeneracy: the accuracy is restored only after map fusion, which needs overlap.
- The field results are full-trajectory accuracy: only start-end closure errors are reported.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; no legacy quote dropped
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/52d390bbe677ada3302912ae/

## Original abstract

SLAM plays a crucial role in automation tasks, such as warehouse logistics, healthcare robotics, and restaurant delivery. These scenes come with various challenges, including navigating around crowds of people, dealing with flying plastic bags that can temporarily blind sensors, and addressing reduced LiDAR density caused by cooking smoke. Such scenarios can result in over-degeneracy, causing the map to drift. To address this issue, this paper presents a multi-map LiDAR-inertial system (MM-LINS) for the first time. The front-end employs an iterated error state Kalman filter for state estimation and introduces a reliable evaluation strategy for degeneracy detection. If over-degeneracy is detected, the active map will be stored into sleeping maps. Subsequently, the system continuously attempts to construct new maps using a dynamic initialization method to ensure successful initialization upon leaving the over-degeneracy. Regarding the back-end, the Scan Context descriptor is utilized to detect inter-map similarity. Upon successful recognition of a sleeping map that shares a common region with the active map, the overlapping trajectory region is utilized to constrain the positional transformation near the edge of the prior map. In response to this, a constraint-enhanced map fusion strategy is proposed to achieve high-precision positional and mapping results. Experiments have been conducted separately on both public datasets that exhibited over-degenerate conditions and in real-world environments. These tests demonstrated the effectiveness of MM-LINS in over-degeneracy environment.
