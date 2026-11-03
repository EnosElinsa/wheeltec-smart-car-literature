# Spatiotemporal Attention Enhances Lidar-Based Robot Navigation in Dynamic Environments

## Metadata

| Field | Value |
|---|---|
| ID | M22 |
| Title | Spatiotemporal Attention Enhances Lidar-Based Robot Navigation in Dynamic Environments |
| Authors | Jorge de Heuvel, Xiangyu Zeng, Weixian Shi, Tharun Sethuraman, and Maren Bennewitz |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 5, pp. 4202-4209 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3373988](https://doi.org/10.1109/lra.2024.3373988) |
| Official URL | https://ieeexplore.ieee.org/document/10461009/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2024-ST-lidar-nav-M22/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2024-ST-lidar-nav-M22/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2024-ST-lidar-nav-M22/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware
- platform_class: differential-drive
- platform: Kobuki Turtlebot 2 (text: "differential-wheeled robot", p. 5)
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Slamtec RPlidar A3 2D LiDAR (1,440 beams)
- compute: not recorded in the legacy extraction
- compute_location: not-reported
- summary_result: In PyBullet, 86.2% success and 13.8% collisions over 1,000 episodes with two dynamic and one static pedestrian; real Turtlebot 2 tests are qualitative.
- summary_limitation: The authors report slightly lower performance after the shift to iGibson; real tests are qualitative and use AMCL on a prebuilt Gmapping map.
- survey_included: yes
- verification_level: light

## Problem

The paper targets foresighted local navigation among pedestrians with only a
sparse 2D LiDAR and without explicit pedestrian tracking. Pedestrian leg
profiles are hard to associate, and the robot's own motion makes static
structure look dynamic between scans. Richer 3D LiDAR or RGB pipelines need
heavier hardware, and earlier learning methods that assume known pedestrian
states suffer a sim-to-real gap.

## Mechanism

A deep reinforcement learning (DRL) actor-critic local controller maps
min-pooled 2D scans, temporal accumulation group descriptors (TAGD), and the
upcoming A* waypoints to linear and angular velocity. TAGD aligns
consecutive scans with ICP, clusters polar sectors, and exposes the centroid
displacement of moving obstacles. Separate spatial and temporal attention
streams weight LiDAR sectors and TAGDs relative to the path. A map of the
empty environment is available for global A* planning; pedestrians are
unknown local obstacles. Training uses a differential-drive Kobuki
Turtlebot 2 model with a Slamtec RPlidar A3 (1,440 beams; 2.5 cm simulated
noise).

## Baselines and controls

Ablations remove the spatial attention, the temporal attention, or the TAGD.
Baselines include CNN-based LiDAR controllers. The legacy extraction does
not name the individual baselines; not verified.

## Platform and setup

Training ran in PyBullet with a curriculum (300,000 episodes), and
evaluation used 1,000 identically set up episodes. Sim-to-sim transfer was
tested in iGibson social-navigation scenes with ORCA pedestrians. The real
tests used a Kobuki Turtlebot 2 with ROS, a Gmapping occupancy map built
beforehand, and AMCL localization. Scenes were corridors, intersections, and
offices, with overtaking, head-on approach, pedestrians behind blind
corners, and a blocked doorway.

## Evidence type and transfer

The tabulated numbers come from PyBullet and iGibson simulation. The real
Turtlebot 2 tests are closed-loop but qualitative, with no tabulated success
rates. Pose on the real robot comes from AMCL on a prebuilt Gmapping map, not
from online SLAM during the trial.

## Sensors

The method uses a single 2D LiDAR (Slamtec RPlidar A3).

## Compute and latency

Not recorded in the legacy extraction; not verified.

## Key quantitative results

- PyBullet, full method: 86.2% success and 13.8% collision rate, with two dynamic pedestrians (0.6 m/s) and one static pedestrian (Table I).
- Evaluation protocol: 1,000 episodes with identical scene setups for all approaches (p. 5).
- Simulated LiDAR noise: amplitude of 2.5 cm (p. 5).

## Stated limitations

- The generalization evaluation shows slightly decreased performance after the post-training domain shift to iGibson (p. 6, Table I caption).

## Transfer conditions

The controller needs a 2D LiDAR, a map of the empty environment for global
A* planning, and localization (AMCL in the real tests). Walls and
thin-legged furniture dominated the collisions in iGibson, according to the
legacy extraction. The legacy card also notes that TAGD may be perturbed by
swinging legs; this was not located in the text and is not verified. The
real evidence is qualitative, so success rates on a physical robot are not
known.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. I, p. 1 | "explicitly tracking objects instances like pedestrians only by their leg profiles from 2D lidar readings is a hard task" |
| C3 | direct-support | weak | Sec. I, p. 1 | "These approaches suffer from a reality gap that hinders generalization to the real world" |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | weak | Sec. V-G, p. 7 | "the Gmapping package [44], a Simultaneous Localization and Mapping algorithm, was used to build an occupancy grid map of real scenarios upfront for path planning." |

## Page-cited excerpts

- **p. 1, Sec. I.** "explicitly tracking objects instances like pedestrians only by their leg profiles from 2D lidar readings is a hard task"
  Sparse 2D LiDAR limits pedestrian perception; this is the motivation, not a measured result.
- **p. 1, Sec. I.** "These approaches suffer from a reality gap that hinders generalization to the real world"
  The authors' view of learning methods that assume known obstacle states; it does not measure the gap of their own policy.
- **p. 7, Sec. V-G.** "the Gmapping package [44], a Simultaneous Localization and Mapping algorithm, was used to build an occupancy grid map of real scenarios upfront for path planning."
  The real tests rely on a prebuilt map.
- **p. 8, Sec. VI.** "Lastly, we achieve an effortless sim-to-real transfer into dynamic real-world indoor environments."
  The authors' claim of sim-to-real transfer, supported only by qualitative real tests.

## Survey-usable statements

### Supported

- A DRL controller with spatiotemporal attention and TAGD reached 86.2% success over 1,000 PyBullet episodes with two dynamic pedestrians (numbers from a light review; re-check before citing).
- The learned 2D-LiDAR controller ran closed-loop on a real Turtlebot 2 in corridor and office encounters, shown qualitatively.

### Not supported

- The policy has a measured real-world success rate: the real tests are qualitative.
- The policy navigates without a prior map: the real tests used a prebuilt Gmapping map and AMCL.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); the legacy card had no verbatim quotes, so excerpts were taken from the introduction, Sec. V-G, and the conclusion with --find; the "swinging legs" statement was not located and is marked not verified
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Foresighted robot navigation in dynamic indoor environments with cost-efficient hardware necessitates the use of a lightweight yet dependable controller. So inferring the scene dynamics from sensor readings without explicit object tracking is a pivotal aspect of foresighted navigation among pedestrians. In this letter, we introduce a spatiotemporal attention pipeline for enhanced navigation based on 2D lidar sensor readings. This pipeline is complemented by a novel lidar-state representation that emphasizes dynamic obstacles over static ones. Subsequently, the attention mechanism enables selective scene perception across both space and time, resulting in improved overall navigation performance within dynamic scenarios. We thoroughly evaluated the approach in different scenarios and simulators, finding excellent generalization to unseen environments. The results demonstrate outstanding performance compared to state-of-the-art methods, thereby enabling the seamless deployment of the learned controller on a real robot.
