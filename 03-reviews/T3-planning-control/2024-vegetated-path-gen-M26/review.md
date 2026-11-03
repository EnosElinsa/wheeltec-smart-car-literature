# Path Generation for Wheeled Robots Autonomous Navigation on Vegetated Terrain

## Metadata

| Field | Value |
|---|---|
| ID | M26 |
| Title | Path Generation for Wheeled Robots Autonomous Navigation on Vegetated Terrain |
| Authors | Zhuozhu Jian, Zejia Liu, Haoyu Shao, Xueqian Wang, Xinlei Chen, and Bin Liang |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 2, pp. 1764-1771 |
| Year | 2024 (online 2023) |
| Type | journal |
| DOI | [10.1109/lra.2023.3334142](https://doi.org/10.1109/lra.2023.3334142) |
| Official URL | https://ieeexplore.ieee.org/document/10320444/ |
| Theme folder | T3-planning-control |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T3-planning-control/2024-vegetated-path-gen-M26/paper.pdf` and `02-fulltext/T3-planning-control/2024-vegetated-path-gen-M26/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2024-vegetated-path-gen-M26/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: skid-steer
- platform: four-wheel differential-drive robot (text: "A four-wheel differential-drive mobile robot", p. 6)
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: RS-Helios 5515 32-beam LiDAR, IMU (camera only for video)
- compute: two Intel NUC i5 2.4 GHz, 16 GB (planner and SLAM separately); global plan 2 Hz, local NMPC 10 Hz
- compute_location: not-reported
- summary_result: In outdoor vegetated trials, PE-RRT* produced shorter paths with larger safety distance than PF-RRT* and RRT*+PrevMap, while Pro-RRT* collided; the legacy extraction records no values.
- summary_limitation: The squared-exponential kernel assumes smooth, continuous ground and vegetation, so support-plane accuracy drops on steeper terrain or more complex vegetation.
- survey_included: yes
- verification_level: light

## Problem

Wheeled navigation on uneven vegetated terrain. LiDAR and camera point clouds
see the vegetation instead of the supporting rigid ground, which produces
unsafe or non-smooth paths.

## Mechanism

PE-RRT* samples circular support planes. Multivariate Gaussian-process
regression fuses proprioceptive pose history (FAST-LIO2 LiDAR-inertial
odometry, wheel and IMU history) with exteroceptive RANSAC surface planes,
weighted by their variances. Traversability uses slope, uncertainty, and
vegetation height, and a safe inflation radius is added to the tree. Local
tracking uses NMPC (CasADi).

## Baselines and controls

The comparators are PF-RRT*, Pro-RRT*, and RRT*+PrevMap (Table I).

## Platform and setup

Real outdoor trials in ROS Melodic, with global planning at 2 Hz and local
NMPC at 10 Hz. The platform is a four-wheel differential-drive robot with an
RS-Helios 5515 32-beam LiDAR, an IMU, a camera used only for the video, and
two Intel NUC i5 computers with 16 GB (one for planning, one for SLAM).
Scenes are a grassy hillside with trees, a garden, and a park.

## Evidence type and transfer

All evidence is closed-loop navigation on the authors' robot outdoors. The
legacy extraction does not record trial counts or whether the NUCs were on
the robot, so compute_location is not-reported. The paper calls the robot
four-wheel differential-drive; by the vocabulary this is coded as
skid-steer.

## Sensors

RS-Helios 5515 32-beam LiDAR with a 70° vertical field of view and an IMU.
The camera only records the front view for the video.

## Compute and latency

Two Intel NUC computers (i5, 2.4 GHz, 16 GB) run the planner and the SLAM
separately. Global planning runs at 2 Hz and local NMPC at 10 Hz.

## Key quantitative results

- Global planning at 2 Hz and local NMPC at 10 Hz in ROS Melodic (p. 6).
- Against PF-RRT*, Pro-RRT*, and RRT*+PrevMap, PE-RRT* gave shorter paths and higher safety distance, and Pro-RRT* collided with a tree; the legacy extraction records no values (p. 7, Table I).

## Stated limitations

- Because of the squared-exponential kernel, the support ground and vegetation layer must be smooth and continuous; support-plane accuracy decreases on steeper terrain or more complex vegetation (p. 7).
- Where sensors are easily blocked in vegetation, UWB-based or vision-based positioning is less accurate or easily lost compared with LiDAR-inertial odometry (p. 7).

## Transfer conditions

The setup splits planning and SLAM across two PCs and uses a 32-beam LiDAR,
which is a heavy sensing and compute budget for a small robot. The method
assumes relatively uniform vegetation for the kernel and depends on
LiDAR-inertial odometry for the pose history.

## Code and data

The paper gives code at https://github.com/jianzhuozhuTHU/PE-RRTstar (p. 1);
not verified whether the repository is available.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. I, p. 1 | "But navigation on uneven vegetated terrain remains a challenging task." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V, p. 6 | "A four-wheel differential-drive mobile robot equipped with RS-Helios 5515 and IMU." |

## Page-cited excerpts

- **p. 1, Sec. I.** "But navigation on uneven vegetated terrain remains a challenging task."
  Vegetation degrades perception of the supporting ground.
- **p. 6, Sec. V.** "A four-wheel differential-drive mobile robot equipped with RS-Helios 5515 and IMU."
  Names the platform and the sensors of the field trials.
- **p. 7, Sec. V.** "When the terrain is steeper, or the vegetation becomes more complex, the accuracy of support plane estimation decreases."
  The authors' own limitation of the kernel assumption.

## Survey-usable statements

### Supported

- Fusing proprioceptive pose history with exteroceptive planes by Gaussian-process regression gave safer and shorter paths than three RRT* variants in outdoor vegetation (numbers from a light review; re-check before citing).
- The method ran in closed loop on a four-wheel robot in three outdoor scenes.

### Not supported

- Reliable support-plane estimates on steep or highly irregular vegetation: the authors state that accuracy drops there.
- Lightweight deployment: the trials used two NUC computers and a 32-beam LiDAR.

## Verification log

- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); legacy C2 excerpt trimmed to its first sentence (the second does not match the PDF text layer); legacy C6 excerpt trimmed to its first sentence because its LiDAR and camera sentences are not found on the PDF page; platform coded skid-steer from the text "four-wheel differential-drive"
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Wheeled robot navigation has been widely used in urban environments, but navigation in wild vegetation is still challenging. External sensors (LiDAR, camera etc.) are often used to construct point cloud map of the surrounding environment, however, the supporting rigid ground used for travelling cannot be detected due to the occlusion of vegetation. This often leads to unsafe or non-smooth paths during the planning process. To address the drawback, we propose the PE-RRT\* algorithm, which effectively combines a novel support plane estimation method and sampling algorithm to generate real-time feasible and safe path in vegetation environments. In order to accurately estimate the support plane, we combine external perception and proprioception, and use Multivariate Gaussian Processe Regression (MV-GPR) to estimate the terrain at the sampling nodes. We build a physical experimental platform and conduct experiments in different outdoor environments. Experimental results show that our method has high safety, robustness, and generalization. The source code is released for the reference of the community.
