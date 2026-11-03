# Uncertainty‐aware LiDAR‐based localization for outdoor mobile robots

## Metadata

| Field | Value |
|---|---|
| ID | M16 |
| Title | Uncertainty‐aware LiDAR‐based localization for outdoor mobile robots |
| Authors | Geonhyeok Park and Woojin Chung |
| Venue | Journal of Field Robotics, vol. 41, no. 8, pp. 2790-2804 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1002/rob.22392](https://doi.org/10.1002/rob.22392) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.22392 |
| Theme folder | T1-perception-localization |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T1-perception-localization/2024-UA-LiDAR-loc-M16/paper.pdf` and `02-fulltext/T1-perception-localization/2024-UA-LiDAR-loc-M16/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2024-UA-LiDAR-loc-M16/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Agilex Hunter 2.0
- boundary_platform: no
- degradation: scene-change, dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Velodyne VLP-16 LiDAR, Xsens MTi-30 IMU, Emlid REACH RS+ GNSS
- compute: AMD Ryzen 7 4800H laptop; 0.86 s per map-matching uncertainty query, 0.068 s per LiDAR-inertial odometry step
- compute_location: not-reported
- summary_result: Maximum 2D translation error of 0.43 m across three campus scenarios with outdated maps and dynamic traffic, while the HDL localization comparator needed reinitialization after errors above 5 m.
- summary_limitation: Extended LiDAR dropouts still cause failure, and GNSS gating that assumes an accurate current pose blocks recovery after a failure.
- survey_included: yes
- verification_level: light

## Problem

Outdoor map-matching localization degrades when the normal distributions
transform (NDT) map is outdated, geometrically sparse, or occluded by parked
cars, construction, pedestrians, and vehicles. Feeding inaccurate
map-matching poses into fusion without weights then corrupts the global
estimate.

## Mechanism

NDT map matching supplies a global pose whose covariance is estimated from
the NDT occupancy distribution over a local histogram of x, y, and yaw. This
pose is fused in a sliding-window factor graph with LiDAR-inertial odometry
(IMU preintegration plus LOAM-style edge and plane matching) and a
conservatively gated GNSS unary factor. Map-matching factors run at 0.5 Hz;
GNSS factors run at 0.1 Hz after a 1 m distance gate that assumes the current
pose is already accurate.

## Baselines and controls

The comparators are LIO-SAM with GNSS, HDL localization (NDT), and FAST-LIO
with ICP. An ablation removes the uncertainty weights and the GNSS gating.

## Platform and setup

Data were collected on an Agilex Hunter 2.0 at Korea University. A NovAtel
PwrPak7 RTK receiver and LIO-SAM provided the maps and the ground truth.
There are three campus scenarios: A (map 17 months old; empty parking lot at
night during mapping versus a full lot during localization, plus a new
construction site), B (map 4 months old; urban occlusions), and C (7.1 km
over 1 h 50 min among pedestrians and moving vehicles).

## Evidence type and transfer

All results come from the authors' own robot data on one campus. The legacy
extraction does not record whether the estimator ran online on the robot;
it is coded as recorded robot data, which was not verified. The drive type
of the Hunter 2.0 is not stated in the text found, so the platform is coded
as wheeled-unspecified. The processing ran under ROS on a laptop, not as an
indoor 2D-LiDAR stack.

## Sensors

3D LiDAR (Velodyne VLP-16), IMU (Xsens MTi-30), and consumer GNSS (Emlid
REACH RS+) are used by the method. RTK GNSS (NovAtel PwrPak7) is used only
for maps and ground truth.

## Compute and latency

Runtime was measured on an AMD Ryzen 7 4800H laptop (ROS, C++): 0.86 s per
map-matching uncertainty query and 0.068 s per LiDAR-inertial odometry step.
Whether the laptop was carried on the robot is not recorded in the legacy
extraction.

## Key quantitative results

- Maximum 2D translation error of the proposed method across all scenarios: 0.43 m (p. 11).
- HDL localization (NDT) required reinitialization after its error exceeded 5 m (p. 11).
- Ablation: the uncertainty weights reduced the maximum error in Scenarios A and B, and GNSS gating reduced it in Scenario C; the legacy extraction records no values (p. 11).
- Runtime on the laptop: 0.86 s per map-matching uncertainty query and 0.068 s per LiDAR-inertial odometry step (p. 12).
- Scenario C covers 7.1 km over 1 h 50 min (p. 7).

## Stated limitations

- If LiDAR data are missing for an extended period, localization can fail (p. 13).
- GNSS outlier filtering assumes an accurate current pose, so after a failure even accurate GNSS is filtered out and recovery is difficult (p. 13).
- Rain, fog, and urban-canyon GNSS are discussed as intended use cases of the same uncertainty and gating machinery, not as evaluated conditions (p. 13).

## Transfer conditions

The method needs a 3D LiDAR, an IMU, a GNSS receiver, and a prior NDT map.
The evidence is outdoor campus driving with LiDAR, IMU, and GNSS on a Hunter
2.0, processed on a laptop. A robot with an indoor 2D LiDAR and no GNSS would
need a different map-matching front end. The authors point to explicit
scan-to-map misalignment detectors as future work for recovery.

## Code and data

The abstract gives an experiment video at https://youtu.be/L6p8gwxn4ak. Code
and data release are not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. 4.1, p. 7 | "In Scenario A, the map was built 17 months before localization. The experimental route included a parking lot, which was nearly empty at night when the map was created and almost full during localization. Additionally, a construction site had been newly built, which did not exist at the time of mapping." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | direct-support | moderate | Sec. 4.6, p. 13 | "However, if LiDAR data is missing for an extended period due to sensor failures or other anomalies, it could result in localization failures. Our GNSS outlier filtering strategy assumes that the current pose is quite accurate, which can lead to challenges when attempting to recover from localization failures." |
| C6 | qualifies | weak | Sec. 4.1, p. 7 | "The robot used for the experiment was Hunter 2.0, manufactured by Agilex Robotics." |

## Page-cited excerpts

- **p. 7, Sec. 4.1.** "In Scenario A, the map was built 17 months before localization. The experimental route included a parking lot, which was nearly empty at night when the map was created and almost full during localization. Additionally, a construction site had been newly built, which did not exist at the time of mapping."
  Map aging and layout change are designed into the evaluation.
- **p. 13, Sec. 4.6.** "However, if LiDAR data is missing for an extended period due to sensor failures or other anomalies, it could result in localization failures. Our GNSS outlier filtering strategy assumes that the current pose is quite accurate, which can lead to challenges when attempting to recover from localization failures. Even after LiDAR functionality is restored, it is difficult to recover to the correct location because the inaccurate current pose causes accurate GNSS data to be filtered out."
  The authors' own limitation: the method does not recover from a localization failure.
- **p. 7, Sec. 4.1.** "The robot used for the experiment was Hunter 2.0, manufactured by Agilex Robotics."
  Names the single platform of the evidence; it gives no drive type.

## Survey-usable statements

### Supported

- Weighting NDT map-matching poses by their estimated uncertainty in a factor graph kept the maximum 2D error at 0.43 m on one campus with outdated maps and dynamic traffic (numbers from a light review; re-check before citing).
- Map aging and parking-lot occupancy change were designed into the evaluation (Scenario A, map 17 months old).

### Not supported

- The method recovers from localization failure: the authors state that GNSS gating blocks recovery after a failure.
- The method handles rain, fog, or urban-canyon GNSS: these are discussed as use cases, not evaluated.
- The method runs onboard the robot: the legacy extraction records only a laptop runtime.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); no legacy quote dropped; hardware caveat moved to Evidence type and Transfer conditions
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Accurate and robust localization is essential for autonomous mobile robots. Map matching based on Light Detection and Ranging (LiDAR) sensors has been widely adopted to estimate the global location of robots. However, map‐matching performance can be degraded when the environment changes or when sufficient features are unavailable. Indiscriminately incorporating inaccurate map‐matching poses for localization can significantly decrease the reliability of pose estimation. This paper aims to develop a robust LiDAR‐based localization method based on map matching. We focus on determining appropriate weights that are computed from the uncertainty of map‐matching poses. The uncertainty of map‐matching poses is estimated by the probability distribution over the poses. We exploit the normal distribution transform map to derive the probability distribution. A factor graph is employed to combine the map‐matching pose, LiDAR‐inertial odometry, and global navigation satellite system information. Experimental verification was successfully conducted outdoors on the university campus in three different scenarios, each involving changing or dynamic environments. We compared the performance of the proposed method with three LiDAR‐based localization methods. The experimental results show that robust localization performances can be achieved even when mapmatching poses are inaccurate in various outdoor environments. The experimental video can be found at https://youtu.be/L6p8gwxn4ak.
