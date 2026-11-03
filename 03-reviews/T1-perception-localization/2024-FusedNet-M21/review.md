# FusedNet: End-to-End Mobile Robot Relocalization in Dynamic Large-Scale Scene

## Metadata

| Field | Value |
|---|---|
| ID | M21 |
| Title | FusedNet: End-to-End Mobile Robot Relocalization in Dynamic Large-Scale Scene |
| Authors | Fang-xing Chen, Yifan Tang, Cong Tai, Xue-ping Liu, Xiang Wu, Tao Zhang, and Long Zeng |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 5, pp. 4099-4105 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3372465](https://doi.org/10.1109/lra.2024.3372465) |
| Official URL | https://ieeexplore.ieee.org/document/10457947/ |
| Theme folder | T1-perception-localization |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T1-perception-localization/2024-FusedNet-M21/paper.pdf` and `02-fulltext/T1-perception-localization/2024-FusedNet-M21/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2024-FusedNet-M21/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: pushed-capture
- platform_class: wheeled-unspecified
- platform: PuduBot2 food-delivery robot with a plate-mounted Kinect v2
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: monocular RGB (Kinect v2 as the image source)
- compute: one GeForce RTX 3080 Ti for training and inference; 38.42 ms per image
- compute_location: desktop-offline
- summary_result: Median real-scene relocalization error of 0.31 m and 1.07 degrees versus 0.97 m and 13.1 degrees for FeatLoc and 1.04 m and 3.09 degrees for NetVLAD, from single RGB images.
- summary_limitation: Relocalization error still grows with pedestrian density, and the real scenes lack 360-degree multi-sequence coverage.
- survey_included: yes
- verification_level: light

## Problem

Absolute relocalization from a single RGB frame is needed when map-matching
or feature-based pipelines fail in large, pedestrian-heavy indoor scenes.
Existing end-to-end regressors that use only global CNN features or only
local keypoints degrade as scene dynamics increase.

## Mechanism

FusedNet extracts a NetVLAD-style global embedding and SuperPoint local
features, rejects dynamic keypoints, fuses the two embeddings with
cross-attention, and regresses the pose from one RGB image. For mobile-robot
scenes the head is 3-DoF (x, y, theta). For the 7Scenes camera benchmark the
head is switched to 6-DoF and the dynamic-point rejection module is removed.

## Baselines and controls

The comparators are FeatLoc and NetVLAD on the robot data, and FeatLoc++ on
7Scenes. The legacy extraction records no ablation.

## Platform and setup

The authors collected the moBotReloc dataset: Unity3D supermarket, office,
and house routes, plus real canteen, corridor, lobby, and store sequences.
Real images and poses come from a PuduBot2 food-delivery robot with a Kinect
v2 fixed on its plate. The robot was pushed by hand, and the timestamps of
pose and image data were aligned afterwards. The static 7Scenes benchmark is
also used.

## Evidence type and transfer

The strongest setting is images recorded on a pushed service robot and
processed on a desktop GPU. The results show single-image relocalization
accuracy; they do not show closed-loop navigation or onboard runtime. The
drive type of the PuduBot2 is not recorded, so the platform is coded as
wheeled-unspecified.

## Sensors

Monocular RGB from a Kinect v2. Poses used as labels come from the PuduBot2.

## Compute and latency

Training and inference run on one GeForce RTX 3080 Ti. Inference takes
38.42 ms per image on that GPU. No onboard timing is recorded.

## Key quantitative results

- Median real-scene error: FusedNet 0.31 m and 1.07 degrees versus FeatLoc 0.97 m and 13.1 degrees and NetVLAD 1.04 m and 3.09 degrees; page not located by text search.
- Error rises with the number of pedestrians for every method, more in real images, and FusedNet degrades less than the baselines (p. 6, Fig. 8).
- On static 7Scenes, the 6-DoF translation error is close to FeatLoc++ without that method's synthetic-data strategy (p. 6).
- Inference time: 38.42 ms per image on an RTX 3080 Ti; page not located by text search.

## Stated limitations

- Relocalization error still grows with pedestrian density (p. 6).
- Real scenes are noisier and lack 360-degree multi-sequence coverage, so forward and reverse passes on the same route are used instead (p. 4).
- Data augmentation for 6-DoF generalization is named as future work (p. 7).

## Transfer conditions

The real data come from a pushed robot, not from closed-loop navigation, and
training and timing were run on an RTX 3080 Ti, not onboard. A robot reusing
the method needs scene-specific training data with pose labels from its own
camera height and route. The 3-DoF head assumes planar motion.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. V-C, p. 6 | "We visualize the relationship between error and dynamic, as shown in Fig. 8, the higher the dynamic of the scene, the relocalization performance of each method will be decreased, for which the presence of dynamic objects will bring a lot of perturbation to the extraction of scene image features especially in real scenes." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV-B, p. 4 | "The Kinect v2 camera is fixed on the robot's plate, and the robot is artificially pushed to move, and then we align the timestamps of the pose data and the image data to obtain the real scene dataset." |

## Page-cited excerpts

- **p. 6, Sec. V-C.** "We visualize the relationship between error and dynamic, as shown in Fig. 8, the higher the dynamic of the scene, the relocalization performance of each method will be decreased, for which the presence of dynamic objects will bring a lot of perturbation to the extraction of scene image features especially in real scenes."
  Scene dynamics degrade every tested relocalizer, including the proposed one.
- **p. 4, Sec. IV-B.** "We employ the PuduBot2 food delivery serving robot provided by PuduTech and Kinect v2 camera to acquire pose data and image data respectively. The Kinect v2 camera is fixed on the robot's plate, and the robot is artificially pushed to move, and then we align the timestamps of the pose data and the image data to obtain the real scene dataset."
  The real data are a pushed capture with offline timestamp alignment, not autonomous driving.

## Survey-usable statements

### Supported

- Fusing global and local image features by cross-attention gave lower median relocalization error than FeatLoc and NetVLAD on the authors' pushed-robot data (numbers from a light review; re-check before citing).
- Pedestrian density raises single-image relocalization error for all tested methods.

### Not supported

- FusedNet enables closed-loop navigation or runs onboard: the data were captured by pushing the robot and processed on a desktop GPU.
- FusedNet is better than FeatLoc++ on 7Scenes: the legacy extraction records only that translation is close.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); no legacy quote dropped; offline pushing moved from Stated limitations to Transfer conditions as a reviewer observation; C6 excerpt shortened to its second sentence for the claim row
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

To improve robot relocalization accuracy in both static and dynamic environments, we introduce a novel network, FusedNet, which incorporates a cross-attention to fuse global and local image features for end-to-end relocalization. This approach relies solely on a monocular camera sensor that is fixed on the mobile robot, and directly predicts the absolute pose from the input RGB image. Additionally, we have collected a mobile robot relocalization dataset, termed moBotReloc, consisting of dynamic large-scale scenes, using the Unity 3D simulation platform and a real mobile robot. Through extensive experiments on 7Scenes and moBotReloc, we demonstrate that FusedNet achieves significant accuracy in 6-DoF camera relocalization in static scenes, and exhibits superior relocalization performance in dynamic large-scale scenes for mobile robot applications, outperforming existing end-to-end methods that rely solely on a single global or local feature.
