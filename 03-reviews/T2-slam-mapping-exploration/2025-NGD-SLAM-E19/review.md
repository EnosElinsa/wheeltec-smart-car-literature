# NGD-SLAM: Towards Real-Time Dynamic SLAM without GPU

## Metadata

| Field | Value |
|---|---|
| ID | E19 |
| Title | NGD-SLAM: Towards Real-Time Dynamic SLAM without GPU |
| Authors | Yuhao Zhang, Mihai Bujanca, and Mikel Luján |
| Venue | 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 3467-3473 |
| Year | 2025 |
| Type | conference |
| DOI | [10.1109/iros60139.2025.11246202](https://doi.org/10.1109/iros60139.2025.11246202) |
| Official URL | https://doi.org/10.1109/iros60139.2025.11246202 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2025-NGD-SLAM-E19/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2025-NGD-SLAM-E19/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2025-NGD-SLAM-E19/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: public RGB-D datasets only: TUM highly dynamic sequences (4) and BONN dynamic sequences (9); carriers not described in the paper
- boundary_platform: yes
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: RGB-D camera images and depth at 30 Hz (dataset sensors; camera model not named)
- compute: AMD Ryzen 7 4800H laptop CPU, GPU not used; 16.72 ms mean tracking time per frame, 30.69 ms per keyframe
- compute_location: desktop-offline
- summary_result: On four TUM highly dynamic sequences, ATE RMSE 0.007-0.034 m versus 0.006-0.027 m for non-real-time DFS-SLAM, with 16.72 ms mean tracking time per frame on a laptop CPU.
- summary_limitation: Mask propagation needs RGB-D depth, and dynamic objects outside the detector's classes, or movable objects that are currently static, are not explicitly handled.
- survey_included: yes
- verification_level: full

## Problem

Semantic dynamic SLAM systems mask moving objects with a deep network, but
camera tracking then waits for the network at every frame, and real-time
operation typically needs a GPU (p. 1). The paper asks whether an RGB-D
dynamic SLAM system can keep the accuracy of semantic masking while tracking
faster than the 30 Hz sensor rate on a CPU alone. The authors define real-time
as more than 30 FPS, the sensor rate of the TUM and BONN datasets (p. 2).

## Mechanism

NGD-SLAM is built on ORB-SLAM3 and adds a semantic thread that runs a YOLO
detector with one-slot input and output buffers, so the tracking thread never
waits for the network (pp. 1-3). The YOLO version is described only as "a
relative lightweight YOLO model" (p. 3).

Mask propagation predicts the current dynamic mask from the newest mask in
the output buffer (p. 3): (1) YOLO bounding boxes; (2) depth-based
segmentation inside each box, which assumes a tight box that the object
mostly fills, followed by connected-component labeling and dilation;
(3) sampling of one dynamic keypoint per 15 x 15 pixel cell (the strongest
FAST response, else a random masked pixel); (4) Lucas-Kanade optical-flow
tracking of these points to the current frame, through intermediate frames
when the mask is several frames old; (5) DBSCAN clustering to separate
objects and drop outliers; (6) depth-based reconstruction of each object's
mask. When the buffer is empty, for example when YOLO misses objects in
rotated images, the last predicted mask is propagated instead (pp. 3-4).

The hybrid tracking strategy tracks static keypoints of the last frame with
LK optical flow on non-keyframes and estimates pose by EPnP with RANSAC.
Keyframes extract ORB features (discarding those inside the mask), match map
points projected from an initial pose (the optical-flow pose, else a
constant-velocity prediction), and refine by Levenberg-Marquardt
reprojection-error minimization; ORB keyframe tracking also serves as the
fallback when optical flow fails (p. 4). Keyframes keep the ORB-SLAM3
covisibility graph and local map.

## Baselines and controls

Feature-based dynamic SLAM comparators are DynaSLAM, DS-SLAM, RDS-SLAM,
TRS-SLAM, CFP-SLAM, USD-SLAM, and DFS-SLAM; dense comparators ReFusion and
ACEFusion appear only on BONN (p. 4). On BONN only DynaSLAM and USD-SLAM carry
over from the TUM comparison, because the others were not evaluated on BONN
or are not open source (p. 5). The paper does not state whether the accuracy
values of Tables I and II were re-run by the authors or copied from the source
papers. USD-SLAM and DFS-SLAM have no RPE values in Table I, and USD-SLAM has
no value on four BONN sequences.

Efficiency is compared as a tracking-time ratio to ORB-SLAM2. For the other
methods, the ratio is taken from their source papers, which used various
devices; the NGD-SLAM ratio uses ORB-SLAM2 at about 20 ms on the authors'
laptop (pp. 4-5). The ablation (Table V) adds components to ORB-SLAM3 in
order: YOLO masks at every frame (+YOLO), mask propagation (+MP), and the
hybrid strategy (+MP+HS, the full system). A separate test drops the input
frame rate of DynaSLAM, the only comparator run under this condition, because
the others are closed source (p. 6).

## Platform and setup

All experiments are dataset playback: the four TUM highly dynamic sequences
(f3/w_xyz, w_rpy, w_half, w_static: two people moving around a desk) and nine
BONN sequences (crowds, a person moving a box, people moving side by side,
and a camera following a walking person), both recorded at 30 Hz (p. 4). The
paper does not describe the carrier of either dataset. All frames of each
sequence are processed, also for methods that are not real-time (p. 4). RPE
uses a 1 s interval (p. 4). No robot is used, and no navigation loop is
closed.

## Evidence type and transfer

The results show trajectory accuracy and per-frame tracking time on
recorded RGB-D sequences processed on a laptop. They do not show onboard
operation on a robot, latency under sensor-rate input on embedded hardware,
or any closed-loop navigation effect. The cross-paper efficiency ratio mixes
devices and implementations; only the NGD-SLAM and ORB-SLAM2/3 timings come
from the authors' laptop.

## Sensors

The method needs RGB images and aligned depth: depth is used to segment
objects inside detection boxes and to rebuild propagated masks (p. 3). The
datasets' own ground truth is used for ATE and RPE; the paper does not name
the camera models or the ground-truth system.

## Compute and latency

All experiments run on a laptop with an AMD Ryzen 7 4800H CPU and an NVIDIA
GeForce RTX 2060 GPU; the GPU is not used for NGD-SLAM (p. 4). The average
tracking time is 16.72 ms per frame (about 60 FPS), dominated by cheap
optical-flow tracking on non-keyframes (p. 5). A keyframe takes 30.69 ms on
average (Table IV), within the 33.3 ms budget of 30 FPS. YOLO detection takes
about 30 to 40 ms per frame and is not counted in the tracking time, because
the semantic thread runs concurrently (p. 5). The paper reports no
end-to-end latency including detection, no CPU utilization, no memory use, and
no timing of the local mapping or loop-closing threads.

## Key quantitative results

- ATE RMSE on TUM, NGD-SLAM versus DFS-SLAM (best non-real-time): f3/w_xyz 0.015 versus 0.013 m, w_rpy 0.034 versus 0.027 m, w_half 0.024 versus 0.018 m, w_static 0.007 versus 0.006 m; DFS-SLAM is lowest on all four (p. 5, Table I).
- ATE RMSE on TUM, NGD-SLAM versus CFP-SLAM (near real-time): w_xyz 0.015 versus 0.015 m, w_rpy 0.034 versus 0.041 m, w_half 0.024 versus 0.023 m, w_static 0.007 versus 0.007 m (p. 5, Table I).
- Among the (near) real-time methods of Table I (TRS-SLAM, CFP-SLAM, NGD-SLAM), NGD-SLAM is strictly lowest on 6 of 12 sequence-metric cells (ATE, RPE translation, RPE rotation), tied on 3, and beaten by CFP-SLAM on 3: ATE w_half (0.024 versus 0.023 m), RPE translation w_xyz (0.020 versus 0.019 m/s), RPE rotation w_static (0.262 versus 0.254 deg/s) (p. 5, Table I).
- ATE RMSE on BONN, NGD-SLAM versus ACEFusion (the other real-time method): lower on 5 of 9 sequences (for example mov_no_box 0.016 versus 0.070 m) and higher on 4: crowd 0.024 versus 0.016 m, crowd3 0.033 versus 0.023 m, mov_no_box2 0.036 versus 0.029 m, synchronous 0.028 versus 0.014 m (p. 5, Table II).
- Over all BONN methods, NGD-SLAM has the lowest ATE on 3 of 9 sequences (crowd2 0.025 m, mov_no_box 0.016 m, synchronous2 0.009 m, tied with DynaSLAM) (p. 5, Table II).
- Tracking-time ratio to ORB-SLAM2: NGD-SLAM 0.84 (CPU) versus TRS-SLAM 1.06, CFP-SLAM 1.72, RDS-SLAM 2.00, DS-SLAM 2.07, USD-SLAM 2.77, DFS-SLAM 3.13, and DynaSLAM 15.94 (all CPU + GPU, ratios from the source papers); a ratio below 1.65 counts as real-time (pp. 5-6, Table III, Fig. 5).
- Keyframe tracking time: mask propagation 7.92 ms, optical-flow tracking 3.04 ms, ORB tracking 19.73 ms, total 30.69 ms (p. 6, Table IV).
- Ablation, ATE RMSE of ORB-SLAM3 versus the full system: w_xyz 0.390 versus 0.015 m, w_rpy 0.639 versus 0.034 m, w_half 0.431 versus 0.024 m, w_static 0.096 versus 0.007 m (93-96% lower); time per frame 20 ms (ORB-SLAM3), 54 ms (+YOLO), 28 ms (+MP), 17 ms (+MP+HS) (p. 6, Table V).
- The full system is not the most accurate configuration on every sequence of the ablation: +YOLO and +MP have 0.014 m versus 0.015 m on w_xyz, and +YOLO has 0.023 m versus 0.024 m on w_half (p. 6, Table V).
- DynaSLAM with reduced input frame rate (figure only, values read from the plot): on f3/w_rpy, ATE rises from about 0.036 m at 30 FPS to about 0.052 m at 15 FPS, with tracking failures at 15 and 20 FPS; w_xyz and w_half change little (p. 6, Fig. 6).

## Stated limitations

- Mask propagation relies on RGB-D depth; monocular or stereo use would need a segmentation model or learned depth estimation (p. 6).
- Dynamic instances outside the detector's classes and movable objects that are currently static are not explicitly handled (p. 6).
- Mask propagation typically fails when a dynamic object appears in the current frame but not in the frame used for prediction; the authors rely on optical-flow tracking of static points to limit the effect (p. 4).
- Depth segmentation assumes that the detector gives a tight bounding box that the object mostly fills (p. 3).

## Transfer conditions

A wheeled robot needs an RGB-D camera with depth aligned to the color image
and a multi-core CPU that can run tracking, local mapping, and YOLO inference
concurrently. The 60 FPS figure is the tracking thread on a laptop Ryzen
CPU; YOLO adds 30 to 40 ms per frame in parallel, so the mask
lags the image, and an embedded ARM CPU would need its own timing. The
evaluated scenes are indoor human motion seen by a moving camera; robot
vibration, outdoor depth range, and dynamic object classes other than those
of the detector were not tested. The efficiency comparison with other methods
rests on ratios from papers on different hardware, which the authors call
"relative fair" (p. 4).

## Code and data

The authors state that the code is public at
https://github.com/yuhaozhang7/NGD-SLAM (p. 1); the repository was not
checked. TUM and BONN are public datasets.

## Version family

No other version is in the library. Preprint versions were not checked.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. IV-E, p. 6 | "exhibiting consistently high errors across all sequences" |
| C3 | partial-support | moderate | Abstract, p. 1 | "they typically require GPUs for realtime operation, which restricts their practicality in real-world robotic applications" |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI, p. 6 | "One limitation of our system is that the mask propagation relies on RGB-D inputs for depth information." |

## Page-cited excerpts

- **p. 4, Sec. IV-A.** "The presented results are obtained by processing all frames in the sequence, even for methods that are not real-time."
  Accuracy tables do not penalize slow methods by dropped frames; the frame-drop effect is tested only for DynaSLAM.
- **p. 5, Sec. IV-B.** "when real-time performance is considered, it achieves the highest accuracy overall"
  The authors' summary of Table I; CFP-SLAM is lower or tied on several cells (see Key quantitative results).
- **p. 5, Sec. IV-D.** "while YOLO detection takes approximately 30 to 40 milliseconds per frame, it is not factored into this tracking time"
  The 60 FPS figure covers the tracking thread only, not detection.
- **p. 6, Sec. IV-F.** "errors significantly increase and tracking failures occur due to larger temporal gaps between frames at lower frame rates"
  Shown for DynaSLAM on f3/w_rpy only; the authors only expect a similar effect for other non-real-time methods.
- **p. 6, Sec. VI.** "we do not explicitly handle dynamic instances that do not belong to the classes defined in the detection model or static objects that are movable."
  Unknown classes and currently static movable objects are outside the method.

## Survey-usable statements

### Supported

- Decoupling detection from tracking by propagating older masks with optical flow and depth lets an ORB-SLAM3-based RGB-D system track at 16.72 ms per frame on a laptop CPU without a GPU, on TUM sequences.
- On the TUM highly dynamic sequences, NGD-SLAM ATE (0.007-0.034 m) is close to but above DFS-SLAM (0.006-0.027 m), the most accurate non-real-time method.
- Adding dynamic masks to ORB-SLAM3 lowers TUM ATE by 93-96%, mask propagation cuts per-frame time from 54 ms (masks at every frame) to 28 ms, and the hybrid strategy to 17 ms (p. 6, Table V).
- When a non-real-time system must drop frames to match the sensor rate, accuracy can degrade under fast rotation, as shown for DynaSLAM on f3/w_rpy.

### Not supported

- NGD-SLAM is the most accurate dynamic SLAM method: DFS-SLAM is lower on all four TUM sequences, and NGD-SLAM is lowest on only 3 of 9 BONN sequences.
- NGD-SLAM is the most accurate real-time method on every sequence: CFP-SLAM beats it on 3 of 12 TUM cells, and ACEFusion beats it on 4 of 9 BONN sequences (crowd, crowd3, mov_no_box2, synchronous).
- NGD-SLAM is several times faster than other dynamic SLAM methods on the same hardware: the comparator ratios come from their source papers on other devices.
- NGD-SLAM runs at 60 FPS end to end: YOLO detection (30 to 40 ms) is not included, and keyframes take 30.69 ms.
- NGD-SLAM works on a robot or embedded CPU: only a laptop CPU and dataset playback were tested.
- The full system is the most accurate ablation configuration on every sequence: +YOLO or +MP is lower on w_xyz and w_half.

## Verification log

- 2026-10-27 | host: Kiro | scope: full text read; Tables I-V, Fig. 5, and Fig. 6 read from rendered page images (pp. 5-6); method, setup, timing, and limitation statements checked on pp. 1-6 | corrections: format; efficiency ratio source clarified (comparators from source papers, NGD-SLAM measured locally); limitations restricted to author statements with pages; counterexamples added for best-accuracy claims; review round 1: ablation timing attributed per component after re-reading Table V on the rendered p. 6 (details in tmp/corrections/E19.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/503b270b53e3da2dd705b3d5/

## Original abstract

Many existing visual SLAM methods can achieve high localization accuracy in dynamic environments by leveraging deep learning to mask moving objects. However, these methods incur significant computational overhead as the camera tracking needs to wait for the deep neural network to generate mask at each frame, and they typically require GPUs for realtime operation, which restricts their practicality in real-world robotic applications. Therefore, this paper proposes a real-time dynamic SLAM system that runs exclusively on a CPU. Our approach incorporates a mask propagation mechanism that decouples camera tracking and deep learning-based masking for each frame. We also introduce a hybrid tracking strategy that integrates ORB features with optical flow methods, enhancing both robustness and efficiency by selectively allocating computational resources to input frames. Compared to previous methods, our system maintains high localization accuracy in dynamic environments while achieving a tracking frame rate of 60 FPS on a laptop CPU. These results demonstrate the feasibility of utilizing deep learning for dynamic SLAM without GPU support. Since most existing dynamic SLAM systems are not open-source, we make our code publicly available at: https://github.com/yuhaozhang7/NGD-SLAM
