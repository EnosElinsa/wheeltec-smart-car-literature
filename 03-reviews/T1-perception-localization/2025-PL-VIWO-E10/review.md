# PL-VIWO: A Lightweight and Robust Point-Line Monocular Visual Inertial Wheel Odometry

## Metadata

| Field | Value |
|---|---|
| ID | E10 |
| Title | PL-VIWO: A Lightweight and Robust Point-Line Monocular Visual Inertial Wheel Odometry |
| Authors | Zhixin Zhang, Wenzhi Bai, Liang Zhao, and Pawel Ladosz |
| Venue | 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 15205-15212 |
| Year | 2025 |
| Type | conference |
| DOI | [10.1109/iros60139.2025.11246999](https://doi.org/10.1109/iros60139.2025.11246999) |
| Official URL | https://doi.org/10.1109/iros60139.2025.11246999 |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2025-PL-VIWO-E10/paper.pdf` and `02-fulltext/T1-perception-localization/2025-PL-VIWO-E10/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2025-PL-VIWO-E10/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: road-vehicle
- platform: KAIST Complex Urban Dataset data vehicle (cited dataset [26]; the text refers to "vehicle speed"), 21 sequences urban18-urban38
- boundary_platform: yes
- degradation: none
- degradation_observed: visual-degradation, dynamic-objects
- evaluation_primary: residual
- evaluation_all: residual
- sensors: monocular camera, IMU, and wheel encoders from the dataset; ground-truth source not described in the paper
- compute: Intel Core i7 CPU (model not stated), 32 GB RAM, NVIDIA A1000 GPU; 35 ms average processing time between frames at 80% CPU (Fig. 6)
- compute_location: desktop-offline
- summary_result: PL-VIWO has the lowest position RMSE on 7 of 11 KAIST highway and 4 of 10 city sequences; on urban31, 191.77 m versus 334.15 m for MINS.
- summary_limitation: No limitation is stated by the authors; evaluation is playback of one public car dataset with loop closure and online calibration disabled, and a stereo version is future work.
- survey_included: yes
- verification_level: full

## Problem

Monocular visual-inertial odometry on ground vehicles loses accuracy when
there are few reliable point features (low texture, dynamic scenes) and when
straight planar motion makes some states unobservable. Line features add
constraints, but they cost computation and classical plane-intersection line
triangulation degenerates when the camera moves along the line direction,
which the authors call common for lane markings and curbs in straight urban
driving (p. 5). The paper asks how to add lines and reject dynamic points in a
filter-based visual-inertial-wheel odometry (VIWO) system at low cost.

## Mechanism

PL-VIWO is an MSCKF-based monocular VIWO system built on MINS; it keeps the
MINS IMU and wheel processing (p. 3) and adds two modules.

- Motion Consistency Check (MCC): for each tracked point, the average
  reprojection error over its n observations, using the historical poses of
  the sliding window and the triangulated point, is compared with a threshold;
  points above it are treated as dynamic and excluded from the update
  (pp. 2-3). The threshold value is not given.
- Line pipeline: LSD detection on images downsampled to 0.25 times, with
  segments shorter than 30 pixels discarded (pp. 3-4); classification of
  segments as parallel to the IMU x, y, or z axis through the vanishing points
  of those axes, using angle and distance thresholds; point-line assignment
  when a point projects between the endpoints and lies within 3 pixels of the
  segment (p. 5); and descriptor-free line matching that reuses point tracks
  (same 3D line if two segments share at least two points, or one point plus
  position and direction differences below thresholds) (p. 5).
- Line triangulation: when plane intersection fails, a line is built from the
  two closest triangulated points assigned to it, or from one triangulated
  point plus the axis direction given by the classification and the IMU
  rotation (p. 5). Lines use Plücker coordinates and are updated with the
  same MSCKF null-space projection as points (pp. 3, 5).

At most 150 points are used for visual updates (p. 6).

## Baselines and controls

Comparators are VINS-Mono, PL-VINS, and VIW-Fusion (optimization-based) and
MINS (filter-based), with MINS configured to use only the monocular camera,
IMU, and wheels (p. 6). Because PL-VIWO is MINS plus MCC and lines, MINS
versus PL-VIWO (w/o line) isolates MCC, and PL-VIWO (w/o line) versus PL-VIWO
isolates the line pipeline. The authors tuned the IMU noise of the
optimization-based methods after shared parameters gave them suboptimal
results, and disabled online intrinsic and extrinsic calibration and loop
closure in all algorithms (p. 6). Line triangulation is compared only with
PL-VINS, in plots without counts (p. 7, Fig. 7).

## Platform and setup

All results are playback of the public KAIST Complex Urban Dataset: 11
highway sequences (urban18-25, 35-37; 2.5 to 11.8 km) in Table I and 10 city
sequences (urban26-34 without 35-37, plus urban38; 3.6 to 11.5 km) in Table II
(p. 7). The paper does not say why these sequences were chosen. The carrier is
the dataset's car (cited reference [26]; the text speaks of changes in vehicle
speed, p. 6), not a robot, although the paper targets ground robots. Accuracy
is the RMSE of absolute position and orientation computed with EVO; position
errors above 300 m or unfinished runs are listed as FAIL (p. 6). Table II
contradicts this rule once: on urban31, MINS (334.15 m) and PL-VIWO (w/o line)
(302.19 m) are listed with numbers above 300 m (p. 7, Table II).

## Evidence type and transfer

The evidence is offline dataset playback on a desktop; there is no robot run,
no closed loop, and no embedded hardware. Low texture with straight motion
(highway group) and dynamic objects (city group) are attributed by the
authors to the scene groups, but no sequence was selected, measured, or
varied for these conditions, so they are coded as observed. No wheel-slip,
illumination, or sensor-fault condition is evaluated. The edge-deployment
claim (p. 7) rests on desktop CPU usage, not on an edge device.

## Sensors

Monocular camera, IMU, and wheel odometry from the KAIST dataset; the paper
names no sensor models and does not describe the ground-truth source.
Calibration parameters are fixed because online calibration is disabled
(p. 6).

## Compute and latency

All experiments run on an Intel Core i7 CPU with 32 GB RAM and an NVIDIA
A1000 GPU (6 GB VRAM) under Ubuntu 20.04 (p. 6); the CPU model and any GPU
use by the method are not stated. Filter-based methods run on a single thread
(p. 7). Fig. 6 gives the average processing time between frames (image
processing plus state update for filters, image processing plus optimization
between keyframes for optimization methods) without naming the sequence.
Memory use is not reported.

## Key quantitative results

- Highway position RMSE: PL-VIWO is lowest on 7 of 11 sequences (urban19, 20, 21, 23, 35, 36, 37), for example urban37 (11.8 km) with 136.04 m versus 174.87 m for VIW-Fusion and 197.53 m for MINS; it is beaten on urban18 (47.99 m versus VIW-Fusion 43.60 m), urban22 (49.77 m versus MINS 46.12 m and PL-VIWO w/o line 48.55 m), urban24 (51.32 m versus MINS 47.65 m and w/o line 48.76 m), and urban25 (31.01 m versus VIW-Fusion 29.46 m) (p. 7, Table I).
- Highway orientation RMSE: PL-VIWO is lowest on 8 of 11 sequences and beaten on urban21 (6.43° versus w/o line 6.06°), urban22 (15.80° versus w/o line 15.30°), and urban25 (16.80° versus VIW-Fusion 9.01°); the text's "best accuracy in 8 out of 11 sequences" (p. 6) matches this orientation count, not the position count (p. 7, Table I).
- Highway failures: VINS-Mono fails all 11 highway sequences and PL-VINS fails 9 of 11 (p. 7, Table I).
- City position RMSE: PL-VIWO is lowest on 4 of 10 (urban27 47.67 m, urban31 191.77 m, urban32 65.96 m, urban34 33.60 m) and second on 4 (urban26, 28, 29, 38); VIW-Fusion is lowest on 5 of 10 (urban26 23.86 m, urban28 32.28 m, urban29 42.26 m, urban30 40.72 m, urban38 48.12 m) and PL-VIWO (w/o line) on urban33 (75.29 m) (p. 7, Table II).
- City orientation RMSE: PL-VIWO is lowest on 5 of 10 (urban26, 27, 31, 33, 38) and second on 2 (urban29, 34); the text's "best in 5 out of 10 sequences and second best in 4 out of 10" (p. 6) names no metric and matches neither metric's pair of counts (p. 7, Table II).
- urban31 (11.4 km): PL-VIWO 191.77 m and 11.15° versus MINS 334.15 m and 16.83°, VIW-Fusion 230.15 m, and PL-VIWO (w/o line) 302.19 m; VINS-Mono and PL-VINS fail (p. 7, Table II).
- Table II highlighting is inconsistent once: on urban30 orientation, VIW-Fusion's 5.56° is bold while PL-VIWO (w/o line)'s 5.54° is underlined (p. 7, Table II).
- Feature processing on urban38, PL-VIWO versus PL-VINS: total 15 ms versus 42 ms, point extraction 5 ms versus 10 ms, line extraction 7 ms versus 23 ms, point matching 2.5 ms versus 3.0 ms, line matching 0.5 ms versus 6 ms; 2D feature processing only (p. 8, Table III).
- Average processing time between frames and CPU usage, read from the bar labels: PL-VIWO 35 ms and 80%, PL-VIWO (w/o line) 20 ms and 60%, MINS 20 ms and 60%, VINS-Mono 45 ms and 130%, VIW-Fusion 48 ms and 130%, PL-VINS 100 ms and 170%; lines add 15 ms over the w/o-line variant (p. 6, Fig. 6).
- Line triangulation: PL-VIWO triangulates visibly more lines than PL-VINS on urban23, 28, and 32; the comparison is plots only, with no line counts (p. 7, Fig. 7).

## Stated limitations

- During triangulation, classified lines are assumed to align with their
  IMU-frame axes (p. 4).
- Line matching with one shared point assumes that a line keeps its direction
  and changes position only a little between adjacent frames (p. 5).
- Adding line features and wheel data adds processing time (p. 7).
- A stereo version and further point-line constraints (point-on-line,
  parallel lines) are named as future work (p. 8).

## Transfer conditions

The evidence comes from a car on paved highway and city roads, with
calibration fixed, loop closure off, and tuned IMU noise for the optimization
baselines; a slow indoor or campus robot with different camera height,
speeds, and texture is untested. Axis classification relies on structure
aligned with the vehicle axes (lane markings, curbs, buildings) and on known
camera-IMU extrinsic rotation. Wheel odometry is used through MINS without a
slip model, and no slip condition is tested. The 35 ms per frame and 80% CPU
are desktop Core i7 figures; an ARM computer such as a Raspberry Pi or Jetson
needs its own timing. Position errors of 29 to 192 m on city sequences and 31
to 136 m on highway sequences without loop closure mean the method alone does
not give map-grade accuracy over kilometers.

## Code and data

The source code is stated to be at https://github.com/Happy-ZZX/PL-VIWO
(p. 1); availability and contents were not verified. The KAIST Complex Urban
Dataset is public; the evaluation was not reproduced.

## Version family

No conference, journal, or preprint version of this work was found in the
library; external preprints were not checked. PL-VINS and MINS are separate
baseline works.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. V-A, p. 6 | "Since motion on highways is mostly uniform and linear, the VINS system suffers from degenerate motion." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V, p. 6 | "we disabled the online calibration of both internal and external parameters, as well as the loop closure in all algorithms for fairness." |

## Page-cited excerpts

- **p. 5, Sec. IV-C.** "This issue is particularly common in 2D urban navigation for ground robots, where line features such as lane markings and curbs cannot be triangulated when the robot moves in a straight line."
  The motivation for point-assisted line triangulation; the paper shows more triangulated lines only in plots.
- **p. 6, Sec. V.** "We evaluated the PL-VIWO using the publicly available KAIST Complex Urban Dataset"
  The only evaluation source is one public car dataset.
- **p. 6, Sec. V.** "we disabled the online calibration of both internal and external parameters, as well as the loop closure in all algorithms for fairness."
  Results speak to odometry drift with fixed calibration, not to full SLAM or self-calibration.
- **p. 6, Sec. V-A.** "Our system further improves and achieves the best accuracy in 8 out of 11 sequences after introducing line features."
  The count matches orientation RMSE in Table I; position RMSE is lowest on 7 of 11.
- **p. 7, Sec. V-B.** "This makes our algorithm more suitable for deployment on resource-constrained edge devices."
  An inference from desktop CPU usage; no edge device was tested.

## Survey-usable statements

### Supported

- On KAIST highway playback, where VINS-Mono fails all 11 sequences, adding
  wheel odometry (VIW-Fusion, MINS, PL-VIWO) gives finished runs on every
  sequence (p. 7, Table I).
- A descriptor-free line pipeline that reuses point tracks cuts 2D line
  matching to 0.5 ms versus 6 ms for PL-VINS on urban38 (p. 8, Table III).
- Point-assisted line triangulation lets a monocular VIWO filter use lines
  during straight driving, where plane-intersection triangulation degenerates
  (pp. 5, 7).
- As a single-thread filter, PL-VIWO uses 80% CPU and 35 ms per frame on a
  desktop Core i7, versus 130% to 170% for the optimization-based comparators
  (p. 6, Fig. 6).

### Not supported

- PL-VIWO is the most accurate on every KAIST sequence: in position RMSE it is
  beaten on 4 of 11 highway sequences (urban18, 22, 24, 25) and 6 of 10 city
  sequences (urban26, 28, 29, 30, 33, 38), where VIW-Fusion wins 5 and the
  w/o-line variant 1 (p. 7, Tables I and II).
- Adding lines always improves position accuracy: PL-VIWO has higher position
  RMSE than PL-VIWO (w/o line) on urban22, 24, 30, and 33 (p. 7, Tables I and
  II).
- MCC alone (PL-VIWO w/o line versus MINS) improves position accuracy on every
  sequence: it is worse on 5 of 11 highway sequences (urban18, 21, 22, 23, 24)
  and on urban26 (p. 7, Tables I and II).
- PL-VIWO runs on edge or onboard hardware: only a desktop Core i7 was used
  (pp. 6-7).
- PL-VIWO is robust to wheel slip, illumination change, or sensor faults: none
  of these conditions is evaluated.
- PL-VIWO is validated on a wheeled robot: all data come from a car dataset.

## Verification log

- 2026-10-30 | host: Kiro | scope: full text read (Secs. I-VI); Tables I, II (p. 7), and III (p. 8) and Fig. 6 bar labels (p. 6) read from rendered page images at 2x and 4x zoom, including bold and underline marks (the MinerU transcription shifts the MINS and PL-VIWO cells of Table I and merges Table II cells); Figs. 5, 7, and 8 viewed | corrections: rebuilt in English template format; highway position wins corrected from 8 to 7 of 11 (8 is the orientation count); city win counts split by metric and VIW-Fusion's 5 city position wins added; FAIL-threshold and urban30 highlighting inconsistencies recorded; stated limitations restricted to author statements; platform coded as a road vehicle (boundary); line-ablation and MCC-ablation counterexamples added (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/2e60eecea5d31d54e31071f2/

## Original abstract

This paper presents a novel tightly coupled Filter-based monocular visual-inertial-wheel odometry (VIWO) system for ground robots, designed to deliver accurate and robust localization in long-term complex outdoor navigation scenarios. As an external sensor, the camera enhances localization performance by introducing visual constraints. However, obtaining a sufficient number of effective visual features is often challenging, particularly in dynamic or low-texture environments. To address this issue, we incorporate the line features for additional geometric constraints. Unlike traditional approaches that treat point and line features independently, our method exploits the geometric relationships between points and lines in 2D images, enabling fast and robust line matching and triangulation. Additionally, we introduce Motion Consistency Check (MCC) to filter out potential dynamic points, ensuring the effectiveness of point feature updates. The proposed system was evaluated on publicly available datasets and benchmarked against state-of-the-art methods. Experimental results demonstrate superior performance in terms of accuracy, robustness, and efficiency. The source code is publicly available at: https://github.com/Happy-ZZX/PL-VIWO.
