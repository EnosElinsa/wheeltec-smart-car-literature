# DynoSAM: Open-Source Smoothing and Mapping Framework for Dynamic SLAM

## Metadata

| Field | Value |
|---|---|
| ID | E15 |
| Title | DynoSAM: Open-Source Smoothing and Mapping Framework for Dynamic SLAM |
| Authors | Jesse Morris, Yiduo Wang, Mikolaj Kliniewski, and Viorela Ila |
| Venue | IEEE Transactions on Robotics, vol. 42, pp. 1178-1197 |
| Year | 2026 (online 2025) |
| Type | journal |
| DOI | [10.1109/tro.2025.3641813](https://doi.org/10.1109/tro.2025.3641813) |
| Official URL | https://ieeexplore.ieee.org/document/11288097/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-DynoSAM-E15/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-DynoSAM-E15/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2026-DynoSAM-E15/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback, simulation
- protocol_caveats: external-pose-source
- platform_class: mixed
- platform: none of the authors' own; KITTI tracking (car), Oxford Multimotion Dataset S4U (handheld camera), simulated Outdoor Cluster, TartanAir Shibuya, and VIODE (UAV-like motion)
- boundary_platform: yes
- degradation: dynamic-objects, visual-degradation
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: stereo or RGB-D images with dense depth, dense optical flow (RAFT), and instance masks (YOLOv8); IMU only on VIODE
- compute: computer not reported; front end about 100 ms per frame plus about 250 ms per object for motion refinement; full-batch back end 80-700 s, 20-frame window about 16 s
- compute_location: not-reported
- summary_result: On OMD S4U, WCME object motion error is 0.71° and 0.02 m versus 0.96° and 0.02 m for VDO-SLAM and 1.1° and 0.03 m for MVO (full batch).
- summary_limitation: The authors state that full-batch optimization is computationally intensive and unsuitable for online use, and that the constant-motion model cannot capture accelerating objects accurately.
- survey_included: yes
- verification_level: full

## Problem

Most visual SLAM systems treat moving objects as outliers and discard them.
Dynamic SLAM also estimates object motions or poses, but there is no
agreement on how to formulate it, object reference frames are defined
differently across systems, and few systems are open source. The paper
provides a common framework for implementing and comparing formulations, a
new pose-based formulation, and an error metric that does not depend on the
object frame definition.

## Mechanism

The basis is the observed (absolute) motion of a rigid body expressed in the
world frame, which moves every point on the object and does not depend on
where the object frame is attached (Sec. III). Two back-end formulations are
implemented in a GTSAM 4.2 factor graph solved with Levenberg-Marquardt:

- World-Centric Motion Estimator (WCME, from VDO-SLAM): camera poses, static
  and dynamic world-frame points, and per-object world-frame motions, linked
  by point measurement factors, camera odometry between-factors, ternary
  object motion factors, and a constant-motion smoothing factor between
  consecutive motions; Huber robust costs. Object trajectories are recovered
  by chaining motions from a first pose (Sec. IV-B).
- World-Centric Pose Estimator (WCPE, new): object poses become the variables,
  with a quaternary motion factor and a pose smoothing factor obtained by
  substituting the pose-change form of the motion; points stay in the world
  frame so that the rigid-body model remains explicit (Sec. IV-C).

The front end takes RGB, instance segmentation, dense optical flow, and dense
depth per frame (RAFT and YOLOv8 in the experiments). It tracks static
features (Shi-Tomasi indoors, ORB outdoors, with ANMS and at least 800
features) and dense per-object features (800 per object), identifies moving
objects by scene flow following Zhang et al., estimates the camera by PnP
with RANSAC and each object motion by the same scheme, then jointly refines
optical flow with pose and motion, and refines each motion with a 3-D point
residual under a strong camera-pose prior, one thread per object (Sec. V-B).
Full-batch and sliding-window back ends are available; loop closure is not
included. The proposed metric ME expresses estimated and ground-truth motions
in the ground-truth object frame (Sec. VI-B2). For VIODE, IMU preintegration is
added to the back end.

## Baselines and controls

- Object motion and pose: VDO-SLAM run by the authors on the same processed
  data (same motion formulation, but g2o, a different front end and
  tracking); MVO results supplied by its authors for S4U and KITTI 00 only;
  ClusterSLAM only as its published average over the Outdoor Cluster
  sequences (RPE only); DynaSLAM II only for per-object ATE on OMD and for
  camera pose, because its KITTI object IDs cannot be aligned without source
  code (p. 11). The text's 91% and 36% gains over DynaSLAM II's reported
  object pose errors (p. 11) are not traceable to a table.
- Camera pose: DynaSLAM II, VDO-SLAM, MVO, and ClusterSLAM (Table I);
  AirDOS with mask and VDO-SLAM on TartanAir (Table II); DynaVINS and
  ORB-SLAM3 in stereo-inertial mode on VIODE (Table III).
- Internal controls: WCME versus WCPE on all sequences, and full batch versus
  a 20-frame sliding window on KITTI 00 and S4U (Table VII). Object-centric
  formulations are in the framework but not reported (p. 6).

## Platform and setup

All results come from playback of public datasets; the authors drive no
robot. Real datasets: nine KITTI tracking sequences (00-06, 18, 20) from a
car, and the OMD sequence swinging_4_unconstrained (S4U), with four swinging
cubes, a handheld camera, and Vicon ground truth. Simulated datasets: four
Outdoor Cluster sequences (L1, L2, S1, S2), seven TartanAir Shibuya sequences
with over 30 moving humans, and six VIODE sequences with full occlusion, low
light, and UAV-like motion (p. 11). Ground truth for objects exists only in
KITTI, Outdoor Cluster, and OMD. Full-batch optimization is used unless stated
otherwise (p. 11). Only objects seen for at least three consecutive frames are
evaluated (p. 12).

## Evidence type and transfer

The evidence is offline estimation on recorded or simulated datasets, so it
shows estimation accuracy, not online behavior on a robot or a navigation
benefit. Object trajectories are anchored at the first ground-truth object
pose for evaluation (pp. 7, 13), which removes object initialization from the
pose results. The downstream reconstruction (DynORecon on S4U, Fig. 11) and
trajectory prediction (Trajectron++ trained and tested on KITTI with DynoSAM
output, Fig. 12) are qualitative and called preliminary by the authors
(p. 17).

## Sensors

Stereo or RGB-D camera with dense depth; dense optical flow and instance
segmentation computed from the images; IMU used only for VIODE. Ground truth
comes from the datasets (Vicon for OMD).

## Compute and latency

The computer is not reported. Fig. 10 (p. 16) gives front-end timings: feature
tracking under 50 ms, joint camera and object motion estimation about 100 ms
per frame, and 3-D motion refinement about 250 ms per object, varying with
the number of points. The full-batch back end takes 80 to 700 s depending on
graph size, and the 20-frame sliding window averages about 16 s (p. 16). The
authors call the front end close to real time and plan incremental inference
for the back end (p. 17).

## Key quantitative results

Tables I-VII were read from rendered page images (pp. 13-16).

- OMD S4U object motion error, WCME versus VDO-SLAM versus MVO: 0.71° versus 0.96° versus 1.1° in rotation and 0.02 m versus 0.02 m versus 0.03 m in translation; WCPE has 1.6° and 0.07 m (p. 14, Table IV). The text reports 34% (rotation) and 21% (translation) improvement over VDO-SLAM on OMD (p. 15); the translation gain is not visible at the table's rounding.
- Average improvement of the WCME over VDO-SLAM: +28% ME rotation, +9% ME translation, -9% object RPE rotation, +4% object RPE translation; over MVO: +49%, +39%, -9%, +12%; over ClusterSLAM (RPE only): +660% and +681% (p. 14, Table V). The ClusterSLAM values equal the ratio of errors times 100 (10.3° versus 1.56°, 8.65 m versus 1.27 m in Table IV), so the percentage convention is not a percent reduction and is not defined.
- KITTI object motion error, WCME versus VDO-SLAM: VDO-SLAM is lower in rotation on 05 (0.48° versus 0.49°) and 18 (0.36° versus 0.6°) and in translation on 00 (0.11 m versus 0.15 m) and 18 (0.16 m versus 0.20 m); translation ties on 03 and 06; the WCME is lower elsewhere, for example 0.39° versus 2.8° on 06 and 0.05 m versus 0.57 m on 20 (p. 14, Table IV).
- Per-object OMD results, DynoSAM (WCME) versus VDO-SLAM: lower ME on all four cubes; versus MVO, MVO is lower on cube 1 (0.542° versus 1.138°, 0.0169 m versus 0.0214 m). Object ATE versus DynaSLAM II: 0.09, 0.21, 0.08, 0.15 m versus 0.41, 0.37, 1.09, 0.28 m, which the text reports as an average 445% improvement (pp. 14-15, Table VI).
- Camera ATE on KITTI, WCME versus DynaSLAM II: higher on 03, 04, 05, 06, and 18 (for example 1.84 m versus 1.09 m on 18) and lower on 00, 01, 02, and 20; on S4U 0.11 m versus 0.05 m for MVO; Outdoor Cluster average 0.34 m versus 0.53 m for ClusterSLAM (p. 13, Table I). Camera RPE differences against the best baseline are at most 0.02° and 0.02 m where DynoSAM is worse (p. 13).
- TartanAir Shibuya camera ATE, WCME versus AirDOS: lower on five of seven sequences (for example 0.19 m versus 0.56 m on VII), higher on II and V (0.04 m versus 0.02 m) (p. 13, Table II).
- VIODE with IMU fusion: DynaVINS has the lowest ATE on all six sequences (0.056-0.194 m versus 0.764-2.560 m for DynoSAM); ORB-SLAM3 fails on three sequences and is lower than DynoSAM on City Day Mid (0.217 m versus 2.515 m). DynoSAM has lower translational RPE on all six sequences and lower rotational RPE on four of six (0.105° versus 0.09° on City Day High and 0.190° versus 0.096° on City Night High are worse). Without the IMU, DynoSAM diverges on the four sequences marked with a dagger; numbers are omitted (pp. 13-14, Table III). Table III bolds DynaVINS's 0.023 m on City Night High although DynoSAM's 0.020 m is lower.
- Full batch versus 20-frame sliding window, average object ME: KITTI 00 1.11° and 0.072 m versus 1.039° and 0.065 m; S4U 0.729° and 0.022 m versus 0.659° and 0.021 m (p. 16, Table VII); Fig. 9 shows larger sliding-window errors at a window overlap (frames 70-85 of KITTI 00). The full-batch values differ from the WCME entries of Table IV (1.29° and 0.15 m on KITTI 00), and the paper does not explain the difference in averaging.
- WCME versus WCPE: the text reports an average difference of 0.06 m and 0.11° and names KITTI 03, 06, and 20 as the only sequences differing by more than one standard deviation (p. 15); in Table IV, however, the 03 ME values are almost identical (0.27° versus 0.26°, 0.15 m versus 0.15 m), although object RPE_t on 03 differs (0.67 m versus 0.19 m), while the ME values of 02 and 18 differ more (for example 0.73 m versus 0.4 m on 02).

## Stated limitations

- Full-batch optimization is computationally intensive and unsuitable for online use (p. 15); at 80-700 s it may not meet real-time requirements (p. 16), and incremental back-end inference is future work (p. 17).
- The constant-motion smoothing model is akin to a constant-velocity model and cannot capture accelerating objects as accurately (p. 17).
- The system is designed for rigid bodies; a more comprehensive approach to nonrigid objects is needed (p. 17).
- Loop closure is not incorporated (p. 11).
- Evaluations of front-end robustness to noisy depth, optical flow, and segmentation are beyond the scope of the paper (p. 8).
- More conservative motion segmentation leaves fewer static tracks and adds rotation bias to visual odometry, raising camera ATE on longer KITTI sequences (p. 13).
- DynaVINS is more robust during total occlusion, which biases DynoSAM's ATE on VIODE (p. 14).
- WCPE is sensitive to object pose initialization from the centroid of partial observations (p. 15).
- VDO-SLAM performs better on KITTI 05, 06, and 18, which the authors attribute to solver and tracking differences and leave for investigation (p. 15).
- The residual and covariance of the world-frame smoothing factor grow with the object's pose; for these smaller-scale experiments the authors set a large smoothing covariance (p. 18).

## Transfer conditions

A wheeled robot needs a stereo or RGB-D camera with dense depth, plus dense
optical flow and instance segmentation; the paper uses RAFT and YOLOv8 but
gives no hardware or runtime for them. The back end, as evaluated, is a
batch solver and does not run online. A sliding window of 20 frames still
took about 16 s on average on an unreported computer, so onboard use on an
embedded computer is not shown. Object trajectories in the pose results were
anchored at ground truth, so a deployed system needs its own object
initialization. Results come from cars, a handheld camera, and simulated
cameras; none was obtained on a ground robot. Where static features vanish
under full occlusion, the visual-only system diverged, and the IMU was needed.

## Code and data

The paper states that code and data are available at
https://github.com/ACFR-RPG/DynOSAM (p. 1), integrated with ROS 2 and
including the evaluation tools (p. 2). All datasets are public. The
repository contents were not checked.

## Version family

The paper builds on the authors' earlier formulation comparison (Morris et
al., ICRA 2024, reference [18]) and on VDO-SLAM (reference [15], arXiv only).
Neither is in this library; this library counts E15 once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. VI-C, p. 14 | "These situations occur in all VIODE sequences and biases DynoSAM’s eventual ATE" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI-E, p. 15 | "This solution, while accurate, is computationally intensive and unsuitable for online use." |

## Page-cited excerpts

- **p. 14, Sec. VI-C.** "These situations occur in all VIODE sequences and biases DynoSAM’s eventual ATE"
  Total occlusion by dynamic objects raises camera ATE; the claim is about VIODE with IMU fusion.
- **p. 15, Sec. VI-E.** "This solution, while accurate, is computationally intensive and unsuitable for online use."
  The tabulated accuracy comes from offline full-batch optimization.
- **p. 17, Sec. VIII.** "this is akin to a constant velocity model, i.e., zero acceleration, which produces locally plausible motion but cannot capture motions of accelerating objects as accurately"
  The smoothing prior limits accuracy for accelerating objects.
- **p. 13, Sec. VI-B3.** "we define the start of each object trajectory using the first ground-truth object pose"
  Object pose evaluation is anchored at ground truth.
- **p. 11, Sec. V-D.** "Finally, we note that loop closure has not been incorporated into the system and is beyond the scope of this work."
  Long-term drift correction is not part of the system.

## Survey-usable statements

### Supported

- A world-frame rigid-body motion formulation in a factor graph estimates
  object motion with 0.71° and 0.02 m error on OMD S4U in full-batch dataset
  playback, below VDO-SLAM and MVO in rotation.
- Expressing motion error in the ground-truth object frame (ME) makes object
  motion errors comparable across systems with different object frames.
- Under total occlusion by dynamic objects, a visual-only dynamic SLAM back end
  diverged on four of six VIODE sequences, and IMU fusion was needed.
- On TartanAir Shibuya, DynoSAM's camera ATE is lower than VDO-SLAM's on all
  seven sequences and lower than AirDOS's on five.

### Not supported

- DynoSAM runs in real time or online: the back end takes 80-700 s in full
  batch and about 16 s per 20-frame window, and the computer is not stated.
- DynoSAM gives the best camera ATE: it is beaten on five of nine KITTI
  sequences by DynaSLAM II, on S4U by MVO, on two of seven TartanAir sequences
  by AirDOS, on all six VIODE sequences by DynaVINS, and on City Day Mid by
  ORB-SLAM3.
- DynoSAM has the best object motion error on every sequence: VDO-SLAM is
  lower on KITTI 05 and 18 in rotation and on 00 and 18 in translation, and
  MVO is lower on OMD cube 1.
- Table V percentages are reductions in error: the ClusterSLAM values are
  error ratios times 100, and the convention is not defined.
- DynoSAM improves navigation or planning: the reconstruction and prediction
  demonstrations are qualitative and preliminary, and no robot is controlled.
- The results hold on a ground robot: no ground-robot data are used.

## Verification log

- 2026-10-30 | host: Kiro | scope: full text read including Appendices A-B; Tables I-VII and Figs. 8-10 read from rendered page images of pp. 13-16; footnotes and dates on p. 1 checked in the raw PDF text | corrections: format rebuilt in English; Table VII value 1.111° corrected to 1.11°; VIODE ATE comparison and IMU divergence scope corrected; ground-truth anchoring moved from limitations to protocol; unsupported version-family link dropped (details in tmp/corrections/E15.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/8d918b4850285962eb548745/

## Original abstract

Traditional visual simultaneous localization and mapping (SLAM) systems focus solely on static scene structures, overlooking dynamic elements in the environment. Although effective for accurate visual odometry in complex scenarios, these methods discard crucial information about moving objects. By incorporating this information into a dynamic SLAM framework, the motion of dynamic entities can be estimated, enhancing navigation whilst ensuring accurate localization. However, the fundamental formulation of dynamic SLAM remains an open challenge, with no consensus on the optimal approach for accurate motion estimation within a SLAM pipeline. Therefore, we developed DynoSAM, an open-source framework for dynamic objects SLAM that enables the efficient implementation, testing, and comparison of various dynamic SLAM optimization formulations. We further propose a novel formulation that encodes rigid-body motion model in object pose estimation as well as an error metric agnostic to object frame definition. DynoSAM integrates static and dynamic measurements into a unified optimization problem solved using factor graphs, simultaneously estimating camera poses, static scene, object motion or poses, and object structures. We evaluate DynoSAM across diverse simulated and real-world datasets, achieving state-of-theart motion estimation in indoor and outdoor environments, with substantial improvements over existing systems. In addition, we demonstrate DynoSAM’s contributions to downstream applications, including 3-D reconstruction of dynamic scenes and trajectory prediction, thereby showcasing potential for advancing dynamic object-aware SLAM systems. Code is open-sourced online.
