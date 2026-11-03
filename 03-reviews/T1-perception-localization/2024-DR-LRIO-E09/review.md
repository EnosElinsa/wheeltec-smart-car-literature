# Degradation Resilient LiDAR-Radar-Inertial Odometry

## Metadata

| Field | Value |
|---|---|
| ID | E09 |
| Title | Degradation Resilient LiDAR-Radar-Inertial Odometry |
| Authors | Morten Nissov, Nikhil Khedekar, and Kostas Alexis |
| Venue | 2024 IEEE International Conference on Robotics and Automation (ICRA), pp. 8587-8594 |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/icra57147.2024.10611444](https://doi.org/10.1109/icra57147.2024.10611444) |
| Official URL | https://doi.org/10.1109/icra57147.2024.10611444 |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2024-DR-LRIO-E09/paper.pdf` and `02-fulltext/T1-perception-localization/2024-DR-LRIO-E09/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2024-DR-LRIO-E09/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: aerial
- platform: RMF-Owl variant flying robot
- boundary_platform: yes
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: VN100 IMU (200 Hz), OS0-128 LiDAR (10 Hz), forward-facing TI IWR6843AOP-EVM radar (10 Hz)
- compute: Intel i7-11800H, multithreaded, real time at 10 Hz
- compute_location: not-reported
- summary_result: In the motion-capture test, DR-LRIO has 0.242 m APE versus 0.268 m (FAST-LIO2), 0.239 m (LIO without radar), and 0.865 m (RIO without LiDAR).
- summary_limitation: The authors report remaining z-drift in both the RIO and DR-LRIO solutions in the tunnel.
- survey_included: yes
- verification_level: light

## Problem

Self-similar tunnels and smoke or fog make LiDAR degenerate, while radar-inertial odometry alone still drifts in yaw and height.

## Mechanism

A fixed-lag factor graph smoother with a 0.75 s window combines IMU preintegration, separate point-to-line and point-to-plane LiDAR factors, and a RANSAC-based radar 3D velocity factor. Keeping LiDAR as individual factors avoids turning a degenerate LiDAR solution into a full 6-DoF prior, so partial information enters along the non-degenerate axes.

## Baselines and controls

FAST-LIO2, LIO without radar, and RIO without LiDAR; radar velocity error is checked against motion capture.

## Platform and setup

An RMF-Owl variant flying robot in the NTNU motion-capture area, a 500 m straight tunnel, and a corridor of about 100 m filled with fog. There is no wheeled-platform experiment.

## Evidence type and transfer

Real flight data. The paper is cross-platform mechanism evidence, not a validation on a wheeled vehicle.

## Sensors

VN100 IMU at 200 Hz, OS0-128 LiDAR at 10 Hz, and a forward-facing TI IWR6843AOP-EVM radar at 10 Hz, hardware-synchronized with known extrinsics; the radar range is at most 15.999 m.

## Compute and latency

C++ with GTSAM, multithreaded, real time at 10 Hz on an Intel i7-11800H; no timing on a Raspberry Pi or similar board. Whether the computer was onboard is not recorded in the legacy extraction.

## Key quantitative results

- Motion-capture test APE: DR-LRIO 0.242 m versus FAST-LIO2 0.268 m, LIO 0.239 m, and RIO 0.865 m (p. 5, Table III).
- Tunnel: RIO and the fusion complete the run while LIO and FAST-LIO2 diverge; there is no full ground-truth ATE (p. 6).
- Fog corridor: the estimate returns to within 1 m of the start point (p. 6).

## Stated limitations

- Some z-drift remains in both the RIO and DR-LRIO solutions in the tunnel (p. 6).
- In the fog environment, an extra heuristic that prefers ground plane features was needed (p. 5).

## Transfer conditions

Legacy reviewer observations: the fog result depends on a low-altitude, man-made scene; the method uses static initialization and known extrinsics; the radar least-squares velocity ignores noise in the independent variables. The tunnel and fog results are mainly qualitative or closure errors, so transfer to ground robots remains to be shown. A wheeled reuse needs a synchronized LiDAR, radar, and IMU with known extrinsics.

## Code and data

Datasets: https://github.com/ntnu-arl/lidar_degeneracy_datasets. Whether the method code is public was not checked.

## Version family

DR-LRIO at ICRA 2024 is one work in this library. It is different from Eq-LRIO (E06) and is not merged with it because of the similar name.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Tunnel, p. 6 | "there remains some z-drift present in both the RIO and DR-LRIO solutions" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Evaluation, p. 2 | "an aerial robot integrating time-synchronized LiDAR, radar and IMU sensing was deployed" |

## Page-cited excerpts

- **p. 2, Evaluation.** "an aerial robot integrating time-synchronized LiDAR, radar and IMU sensing was deployed"
  The experiments come from a flying platform.
- **p. 5, Implementation.** "in the fog environment, in order to boost the performance a feature heuristic was included to prefer plane features found on the ground."
  An extra ground-feature heuristic was used in fog.
- **p. 6, Tunnel.** "there remains some z-drift present in both the RIO and DR-LRIO solutions"
  The fusion still drifts in height.

## Survey-usable statements

### Supported

- Adding radar velocity factors to a factor-graph LiDAR-inertial smoother lets a flying robot complete a self-similar tunnel where LIO and FAST-LIO2 diverge, while keeping APE close to LIO in a well-conditioned motion-capture test (0.242 m versus 0.239 m).

### Not supported

- DR-LRIO is the most accurate method in the motion-capture test: LIO has 0.239 m versus 0.242 m.
- DR-LRIO removes drift in degenerate tunnels: z-drift remains, and no full ground-truth ATE is reported there.
- The method is validated on ground robots: all experiments use an aerial robot.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; no legacy quote dropped
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/daaa1fc06334cda00e9f773c/

## Original abstract

Enabling autonomous robots to operate robustly in challenging environments is necessary in a future with increased autonomy. For many autonomous systems, estimation and odometry remains a single point of failure, from which it can often be difficult, if not impossible, to recover. As such robust odometry solutions are of key importance. In this work a method for tightly-coupled LiDAR-Radar-Inertial fusion for odometry is proposed, enabling the mitigation of the effects of LiDAR degeneracy by leveraging a complementary perception modality while preserving the accuracy of LiDAR in well-conditioned environments. The proposed approach combines modalities in a factor graph-based windowed smoother with sensor information-specific factor formulations which enable, in the case of degeneracy, partial information to be conveyed to the graph along the non-degenerate axes. The proposed method is evaluated in real-world tests on a flying robot experiencing degraded conditions including geometric self-similarity as well as obscurant occlusion. For the benefit of the community we release the datasets presented: https://github.com/ntnu-arl/lidar_degeneracy_datasets.
