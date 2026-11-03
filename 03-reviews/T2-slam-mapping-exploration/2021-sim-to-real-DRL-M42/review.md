# A Sim-to-Real Pipeline for Deep Reinforcement Learning for Autonomous Robot Navigation in Cluttered Rough Terrain

## Metadata

| Field | Value |
|---|---|
| ID | M42 |
| Title | A Sim-to-Real Pipeline for Deep Reinforcement Learning for Autonomous Robot Navigation in Cluttered Rough Terrain |
| Authors | Han Hu, Kaicheng Zhang, Aaron Hao Tan, Michael Ruan, Christopher Agia, and Goldie Nejat |
| Venue | IEEE Robotics and Automation Letters, vol. 6, no. 4, pp. 6569-6576 |
| Year | 2021 |
| Type | journal |
| DOI | [10.1109/lra.2021.3093551](https://doi.org/10.1109/lra.2021.3093551) |
| Official URL | https://ieeexplore.ieee.org/document/9468918/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2021-sim-to-real-DRL-M42/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2021-sim-to-real-DRL-M42/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2021-sim-to-real-DRL-M42/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: offboard-compute
- platform_class: skid-steer
- platform: Jaguar 4x4 (text: "skid-steered mobile robot", p. 5)
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Velodyne VLP-16 3D LiDAR; Stereo Labs ZED Mini stereo camera with IMU
- compute: DRL policy on a desktop server (Intel i7-7700K) over Wi-Fi; onboard Intel NUC i5 for elevation mapping and control; Jetson TX2 for ZED pose
- compute_location: offboard-local
- summary_result: A Jaguar 4x4 navigated point to point over a lab pallet-and-ramp course, with higher success and lower travel distance and time than a classical and a deep-learning comparator.
- summary_limitation: The authors state that DRL can overfit the training terrain and generalize poorly to dissimilar terrain; sim-to-real map deviation caused failed real trials.
- survey_included: yes
- verification_level: light

## Problem

The paper addresses point-to-point navigation over 3D cluttered rough
terrain with abrupt changes in elevation and surface normals. Heuristic or
scalar traversability labels drop the robot-terrain interaction (wheel
placement, approach angle). Policies trained in simulation overfit to
appearance and fail to transfer.

## Mechanism

The sim-to-real deep reinforcement learning (DRL) pipeline trains on a
Gazebo mesh reconstructed from the real scene (RTAB-Map RGB-D SLAM plus
Poisson meshing). Observations are domain-invariant: a 5 m × 5 m elevation
map, the distance to the goal, and the orientation, not raw RGB or LiDAR.
Training injects elevation-steepness scaling, motion disturbance, and
Gaussian pose-estimation noise. At deployment, stereo and IMU pose and
VLP-16 points feed elevation mapping, and a closed-loop controller on the NUC
executes the actions. The DRL policy runs on a desktop server (i7-7700K) and
sends actions over Wi-Fi.

## Baselines and controls

The comparators are a classical planner and a deep-learning terrain
traversability method, compared on success rate, travel distance, and time.
A sensitivity analysis varies the sim-to-real strategies; training with
elevation scaling, motion disturbance, and pose noise together (E+MD+P) is
the most robust.

## Platform and setup

The robot is a Jaguar 4x4 skid-steer with a Velodyne VLP-16, a Stereo Labs
ZED Mini (stereo camera and IMU), an Intel NUC i5, and a Jetson TX2 for ZED
pose. The course is a lab terrain of pallets and ramps. Runs include
successful point-to-point tests (for example Test 10) and failures.

## Evidence type and transfer

The real runs are closed-loop, but the policy inference is offboard on a
desktop server over Wi-Fi. The course is a controlled lab terrain, not a
field-scale off-road site. Failures came from vibration and from mismatch
between the simulated and real maps.

## Sensors

Velodyne VLP-16 3D LiDAR and Stereo Labs ZED Mini (stereo camera and IMU).

## Compute and latency

The NUC i5 runs elevation mapping and tracking control; the Jetson TX2 runs
ZED pose estimation; a desktop server with an Intel i7-7700K runs the DRL
module and sends actions over Wi-Fi. Timing is not recorded in the legacy
extraction; not verified.

## Key quantitative results

- The legacy extraction records no numeric results; it reports successful point-to-point runs (for example Test 10) and failed runs (p. 6).
- Comparison: the method performed better than the classical and the deep-learning comparator in success rate and cumulative travel distance and time; values not recorded in the legacy extraction (p. 8).
- Sensitivity analysis: E+MD+P training is the most robust; values not recorded in the legacy extraction (p. 7).

## Stated limitations

- DRL can overfit to the training environment and then have difficulty generalizing to real unstructured environments with dissimilar terrain (p. 8).
- In some tests, repeated vibrations on sudden drops and bumps caused variability in robot decisions (p. 6).
- Limited resolution of RTAB-Map and of the 3D mesh caused deviations between the simulated and real maps; some gaps appeared smaller in simulation, so the policy learned incorrect traversability (p. 6).

## Transfer conditions

The method needs a 3D LiDAR, a stereo-inertial pose source, a mesh of the
target terrain for training, and a server reachable over Wi-Fi for the
policy. Fully onboard policy computation is not shown.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | direct-support | strong | Sec. IV-A, p. 6 | "This deviation caused certain gaps to appear smaller in simulation which led the DRL algorithm to learn incorrect traversability." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV-A, p. 5 | "A server equipped with an Intel i7-7700K CPU runs the DRL module" |

## Page-cited excerpts

- **p. 6, Sec. IV-A.** "This deviation caused certain gaps to appear smaller in simulation which led the DRL algorithm to learn incorrect traversability."
  A measured sim-to-real map gap caused failed real trials.
- **p. 8, Sec. V.** "DRL has the potential limitation of overfitting to a training environment."
  The authors' general limit on generalization to dissimilar terrain.
- **p. 5, Sec. IV-A.** "A server equipped with an Intel i7-7700K CPU runs the DRL module"
  The policy is not computed onboard.
- **p. 5, Sec. IV-A.** "The Jaguar 4x4 skid-steered mobile robot is equipped with a Velodyne VLP-16 3D LiDAR"
  Source of the drive type.

## Survey-usable statements

### Supported

- A DRL navigation policy trained on a mesh of the real scene, with elevation-map observations and domain randomization, transferred to a skid-steer robot on a lab rough-terrain course without real-world training.
- Mesh and map resolution mismatch between simulation and reality caused learned traversability errors and failed trials.

### Not supported

- The policy runs onboard: it ran on a desktop server over Wi-Fi.
- The policy generalizes to field off-road terrain: the authors state that it may not generalize to dissimilar terrain, and the tests used one lab course.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); the legacy card had no verbatim quotes, so excerpts were taken from the conclusion and from Sec. IV-A sentences located with --find; the two legacy C3 records were merged into one claim row
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Robots that autonomously navigate real-world 3D cluttered environments need to safely traverse terrain with abrupt changes in surface normals and elevations. In this letter, we present the development of a novel sim-to-real pipeline for a mobile robot to effectively learn how to navigate real-world 3D rough terrain environments. The pipeline uses a deep reinforcement learning architecture to learn a navigation policy from training data obtained from the simulated environment and a unique combination of strategies to directly address the reality gap for such environments. Experiments in the real-world 3D cluttered environment verified that the robot successfully performed point-to-point navigation from arbitrary start and goal locations while traversing rough terrain. A comparison study between our DRL method, classical, and deep learning-based approaches showed that our method performed better in terms of success rate, and cumulative travel distance and time in a 3D rough terrain environment.
