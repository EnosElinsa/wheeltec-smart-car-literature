# M2DGR: A Multi-Sensor and Multi-Scenario SLAM Dataset for Ground Robots

## Metadata

| Field | Value |
|---|---|
| ID | M41 |
| Title | M2DGR: A Multi-Sensor and Multi-Scenario SLAM Dataset for Ground Robots |
| Authors | Jie Yin, Ang Li, Tao Li, Wenxian Yu, and Danping Zou |
| Venue | IEEE Robotics and Automation Letters, vol. 7, no. 2, pp. 2266-2273 |
| Year | 2022 (online 2021) |
| Type | journal |
| DOI | [10.1109/lra.2021.3138527](https://doi.org/10.1109/lra.2021.3138527) |
| Official URL | https://ieeexplore.ieee.org/document/9664374/ |
| Theme folder | T1-perception-localization |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T1-perception-localization/2022-M2DGR-M41/paper.pdf` and `02-fulltext/T1-perception-localization/2022-M2DGR-M41/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2022-M2DGR-M41/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-resource
- evidence_all: dataset-resource, recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: custom three-layer ground robot (unnamed chassis) with a Velodyne VLP-32C sensor suite
- boundary_platform: no
- degradation: visual-degradation, gnss-denial
- degradation_observed: none
- evaluation_primary: designed-degradation
- evaluation_all: residual, designed-degradation
- sensors: Velodyne VLP-32C LiDAR, fish-eye RGB cameras, RealSense D435i, thermal infrared camera, event camera, IMU, consumer GNSS; RTK/INS, Vicon, and laser tracker for ground truth
- compute: not recorded in the legacy extraction
- compute_location: not-reported
- summary_result: On seven of 36 sequences, visual SLAM fails in darkness and no tested system tracks a lift ride; LIO-SAM reaches 1247 m ATE on Lift04.
- summary_limitation: Sensors are synchronized in software, with cameras triggered through the API, and the lift and dark-room sequences remain unsolved by the evaluated systems.
- survey_included: yes
- verification_level: light

## Problem

Existing SLAM benchmarks mostly come from cars or UAVs. Daily failure modes
of ground robots are missing or have unreliable ground truth: textureless or
dark rooms, long corridors, GNSS loss between outdoors and indoors, taking a
lift, and abrupt zigzag motion. OpenLORIS, for example, uses LiDAR SLAM as
ground truth.

## Mechanism

The paper contributes a dataset and benchmark, not a new estimator. A custom
three-layer ground robot records synchronized multi-sensor ROS bags
(software synchronization, below 10 ms among cameras). Sensors: six surround
fish-eye RGB cameras (FLIR CM3-U3-13Y3C), a sky-pointing fish-eye, a
RealSense D435i visual-inertial sensor, a Gaode PLUG 617 infrared camera, an
Inivation DVXplorer event camera, a Velodyne VLP-32C, a Handsfree A9 IMU, a
Ublox M8T GNSS receiver, and an Xsens MTi-680G RTK/INS. Indoor ground truth
comes from a Vicon Vero 2.2 or a Leica Nova MS60; outdoor ground truth from
the RTK/INS. There are 36 sequences, about 1.2 TB and 10.7 km, on the SJTU
campus (street, circle, gate, walk, hall, door, lift, room, room-dark).

## Baselines and controls

Evaluated systems: A-LOAM, LeGO-LOAM, LINS, LIO-SAM, ORB-SLAM3 (pinhole,
fish-eye, and thermal), CubemapSLAM, VINS-Mono, Multicol-SLAM, and RTKLIB
single-point positioning (SPP).

## Platform and setup

Seven sequences (Street02, Street06, Street07, Roomdark06, Hall05, Door01,
Lift04) are evaluated with absolute trajectory error (ATE). The sequences
cover indoor halls and dark rooms, outdoor campus streets, an indoor-outdoor
door transition, a lift ride with a floor change, night driving, and abrupt
motion.

## Evidence type and transfer

The contribution is a dataset recorded on the authors' ground robot, with
benchmark runs of existing systems. No new onboard estimator is claimed. The
chassis is not named and its drive type is not recorded, so the platform is
coded as wheeled-unspecified. The legacy extraction gives the size as about
1.2 TB, while the abstract says about 1 TB; the value was not re-checked.

## Sensors

3D LiDAR (Velodyne VLP-32C), multiple fish-eye RGB cameras, an RGB-D and
visual-inertial sensor (RealSense D435i), a thermal infrared camera, an
event camera, an IMU, and consumer GNSS. RTK/INS, Vicon, and a laser 3D
tracker provide ground truth.

## Compute and latency

Not recorded in the legacy extraction; not verified.

## Key quantitative results

- The dataset has 36 sequences (p. 1); the legacy extraction gives about 1.2 TB and 10.7 km, which text search did not locate.
- Camera synchronization error is below 10 ms (p. 4).
- Visual methods fail in darkness and low light; thermal ORB-SLAM3 is more robust there but some infrared views are textureless (p. 6).
- No tested system tracks a lift ride; LIO-SAM reaches an ATE of 1247 m on Lift04 after an IMU-LiDAR mismatch; page not located by text search.
- On Door01, GNSS SPP looks numerically plausible, but the indoor fix has failed (p. 7).
- On Street07 with zigzag motion and braking, most vision systems fail and the LiDAR ATE is large (p. 7).
- Multicol-SLAM on three fish-eye cameras loses track almost everywhere (p. 7).

## Stated limitations

- Synchronization is in software, not hardware; the cameras are triggered through the API (p. 4).
- The lift and dark-room sequences remain unsolved by the evaluated systems (p. 6).

## Transfer conditions

A custom collection robot and ROS bags are the contribution; no new onboard
estimator is claimed. Results describe how existing SLAM systems fail on
this robot's sensor suite and campus, not how a specific method performs on
another robot.

## Code and data

The abstract states that the dataset and tools are public at
https://github.com/SJTU-ViSYS/M2DGR; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. IV, p. 7 | "The results indicate that the state-of-the-art SLAM systems, both visual and LiDAR ones, may perform well on existing benchmark tests, they still require significant improvement to be applied to ground robots in daily life." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | weak | Sec. V, p. 7 | "We release M2DGR, a large-scale multi-sensor dataset focusing on ground robots' localization and mapping tasks. Our dataset contains a large pool ofsensory information to encourage breakthroughs in multi-sensor fusion on SLAM." |

## Page-cited excerpts

- **p. 7, Sec. IV.** "The results indicate that the state-of-the-art SLAM systems, both visual and LiDAR ones, may perform well on existing benchmark tests, they still require significant improvement to be applied to ground robots in daily life."
  Benchmark scores of existing systems do not transfer to daily ground-robot scenarios.
- **p. 7, Sec. V.** "We release M2DGR, a large-scale multi-sensor dataset focusing on ground robots' localization and mapping tasks. Our dataset contains a large pool ofsensory information to encourage breakthroughs in multi-sensor fusion on SLAM."
  The contribution is data, not an estimator; "ofsensory" is the transcription's spelling.

## Survey-usable statements

### Supported

- On M2DGR, existing visual SLAM fails in darkness, no evaluated system tracks a lift ride, and GNSS fixes fail indoors (numbers from a light review; re-check before citing).
- Ground-robot daily scenarios (dark rooms, lifts, indoor-outdoor transitions) remain hard for state-of-the-art SLAM.

### Not supported

- M2DGR proposes or validates a new estimator: it is a dataset and benchmark.
- The dataset is hardware-synchronized: synchronization is in software.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); no legacy quote dropped; "dataset, not an algorithm paper" moved from Stated limitations to Transfer conditions; size of 1.2 TB in the legacy extraction differs from the abstract's about 1 TB (flagged, not resolved)
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

We introduce M2DGR: a novel large-scale dataset collected by a ground robot with a full sensor-suite including six fish-eye and one sky-pointing RGB cameras, an infrared camera, an event camera, a Visual-Inertial Sensor (VI-sensor), an inertial measurement unit (IMU), a LiDAR, a consumer-grade Global Navigation Satellite System (GNSS) receiver and a GNSS-IMU navigation system with real-time kinematic (RTK) signals. All those sensors were well-calibrated and synchronized, and their data were recorded simultaneously. The ground truth trajectories were obtained by the motion capture device, a laser 3D tracker, and an RTK receiver. The dataset comprises 36 sequences (about 1 TB) captured in diverse scenarios including both indoor and outdoor environments. We evaluate state-of-the-art SLAM algorithms on M2DGR. Results show that existing solutions perform poorly in some scenarios. For the benefit of the research community, we make the dataset and tools public. The webpage of our project is https://github.com/SJTU-ViSYS/M2DGR.
