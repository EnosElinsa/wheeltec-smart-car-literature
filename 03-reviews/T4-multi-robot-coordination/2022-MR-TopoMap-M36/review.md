# MR-TopoMap: Multi-Robot Exploration Based on Topological Map in Communication Restricted Environment

## Metadata

| Field | Value |
|---|---|
| ID | M36 |
| Title | MR-TopoMap: Multi-Robot Exploration Based on Topological Map in Communication Restricted Environment |
| Authors | Zhaoliang Zhang, Jincheng Yu, Jiahao Tang, Yuanfan Xu, and Yu Wang |
| Venue | IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 10794-10801 |
| Year | 2022 |
| Type | journal |
| DOI | [10.1109/lra.2022.3192765](https://doi.org/10.1109/lra.2022.3192765) |
| Official URL | https://ieeexplore.ieee.org/document/9834084/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T4-multi-robot-coordination/2022-MR-TopoMap-M36/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2022-MR-TopoMap-M36/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2022-MR-TopoMap-M36/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Real wheeled robots with RPLIDAR A1, three RGB cameras, and Jetson Xavier NX (chassis not named; Fig. 8(c)); TurtleBot Burger in Gazebo
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: 2D LiDAR (RPLIDAR A1 on hardware; 360° laser with 7 m range in simulation); panoramic RGB (three 120° cameras on hardware, four 90° cameras in simulation)
- compute: NVIDIA Jetson Xavier NX onboard; timing not recorded
- compute_location: onboard
- summary_result: Versus occupancy-grid sharing schemes, topological-map sharing cuts communication traffic by 84%-90% and raises exploration efficiency by 23%-77% in Gazebo and real-robot tests.
- summary_limitation: The authors state that map building and merging rely heavily on the image-retrieval threshold; exploration fails at 0.65 and map merging fails at 1.
- survey_included: yes
- verification_level: light

## Problem

Multi-robot exploration under restricted bandwidth. Distributed SLAM with occupancy grids typically transfers place descriptors, relative-pose data, and submaps, and grid maps dominate the traffic (about 70% in the cited breakdown). Such traffic can exceed links like underwater acoustic channels. Grid-map sharing is the bottleneck the letter targets.

## Mechanism

Each robot builds a topological map while it moves. A panoramic image descriptor from an image-retrieval network, matched by inner product, decides whether the place is new. A new vertex stores the robot name, an id, the local pose, the descriptor, and unexplored directions cropped from a local LiDAR occupancy grid. Only new vertices and edges are broadcast, and teammates merge maps when descriptors match. Local grids stay onboard for obstacle avoidance and are not shared. Exploration picks an unexplored direction stored on a vertex, and the robot deletes that direction after visiting it. The place-recognition threshold is 0.75 in the reported runs.

## Baselines and controls

RRT exploration and MMPF for exploration time; ScanPerSubmap, ScanPerMatch, and OnlySubmap for communication traffic. A threshold sweep of the image-retrieval algorithm is reported. Other controls are not recorded in the legacy extraction; not verified.

## Platform and setup

- Simulation: Gazebo with two indoor maps (391 m² and 661 m²); TurtleBot Burger with four 90° RGB cameras in a square (360°) and a 360° laser with 7 m range; one and two robots. Timed comparisons use 99% coverage (small map) and 95% coverage (large map).
- Hardware: real robots with an RPLIDAR A1, three 120° RGB cameras forming a panorama, an NVIDIA Jetson Xavier NX, and a separate router per robot for stable links. The chassis model is not named beyond the sensor and compute kit (Fig. 8(c)).

## Evidence type and transfer

The timed and traffic comparisons in the legacy extraction come from Gazebo. The hardware runs close the loop on real wheeled robots, but each robot had its own router, so the hardware does not test a restricted link. Hardware metrics are not recorded in the legacy extraction.

## Sensors

2D LiDAR for the local occupancy grid and panoramic RGB images for place recognition.

## Compute and latency

NVIDIA Jetson Xavier NX onboard each real robot. Timing is not recorded in the legacy extraction.

## Key quantitative results

- Communication traffic: 84%-90% lower than the grid-map schemes (p. 7).
- Topological traffic: 77.3 KB (small map) and 135.3 KB (large map) versus hundreds to about 1400 KB for the grid schemes (no page; table values found only in paper.md).
- Exploration speed-up versus RRT and MMPF: between 1.07x (p. 7) and 2.02x (p. 6), depending on map and team size.
- Exploration efficiency gain of 23%-77% (p. 1, abstract).
- Coverage: 95%-99% for the topological method versus about 99% for the grid methods; trajectories can be longer than MMPF because the policy drives far to open new vertices (no page).

## Stated limitations

- The system relies heavily on the image-retrieval algorithm and the place-recognition parameters; future work will study other visual place-recognition methods, use edges for graph matching, and extend to aerial-ground teams (p. 8).
- Exploration fails when the threshold is reduced to 0.65 (p. 7), and map merging fails when it is set to 1 (p. 7).

## Transfer conditions

Legacy reviewer observation: topological coverage stays below full grid coverage because occupancy maps are not merged online. Each real robot used a separate router, so communication restriction was not reproduced on hardware. A wheeled robot reusing the method needs a panoramic camera rig and a tuned place-recognition threshold.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | strong | Sec. IV-C, p. 7 | "Unlike current trends, our system transfers the vertices and edges of the topological map." |
| C5 | unset | n/a | | |
| C6 | qualifies | strong | Sec. IV-A, p. 6 | "Finally, each robot has a separate router to guarantee stable communication conditions." |

## Page-cited excerpts

- **p. 7, Communication evaluation.** "Unlike current trends, our system transfers the vertices and edges of the topological map."
  Only topological elements are shared, which is the source of the traffic savings.
- **p. 7, Communication evaluation.** "Compared with the grid map methods, our system saves the communication traffic by 84%"
  The traffic saving against grid-map schemes (the printed range runs to 90%).
- **p. 6, Real robot.** "We also implement our system on real robots equipped with an RPLIDAR A1 LIDAR device and three RGB cameras"
  The hardware sensor kit.
- **p. 6, Real robot.** "The robot uses NVIDIA Jetson Xavier NX as computation platform."
  Onboard compute of the real robots.
- **p. 6, Real robot.** "Finally, each robot has a separate router to guarantee stable communication conditions."
  The hardware links were stabilized, so the hardware runs do not test restricted communication.
- **p. 8, Conclusion and future work.** "Our system heavily relies on the image retrieval algorithm and the PR parameters."
  The authors' main stated limitation.

## Survey-usable statements

### Supported

- Sharing only topological vertices and edges, with local grids kept onboard, cut communication traffic by 84%-90% versus grid-map schemes in Gazebo (numbers from a light review; re-check before citing).
- The method ran on real wheeled robots with a 2D LiDAR, panoramic RGB cameras, and a Jetson Xavier NX.

### Not supported

- The method was validated under restricted communication on hardware: each real robot had a separate router for stable links.
- Topological exploration reaches the same coverage as grid methods: coverage is 95%-99% versus about 99%.
- The method is insensitive to tuning: exploration fails at a threshold of 0.65 and map merging fails at 1.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Real robot, Claim summary, Hardware caveat) converted to the English template; the legacy C4 quote was cut before "90%." and the C6 quote before "with 120° FOV" because the full strings do not match paper.md; the C6 row now uses the separate-router sentence (p. 6), which states the limit; the traffic table values and coverage figures have no located page
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Multi-robot exploration in unknown environments is a fundamental task for a multi-robot system, involving inter-robot communication through messages among the robots. However, in a restricted communication environment, the limited communication resources become the system’s bottleneck due to a large amount of data in the occupancy grid map. Hence, to enhance multi-agent exploration in communication-constrained environments, this letter develops a method to build topological maps while the robot moves in the environment and an exploration strategy based on the created topological map. The latter map comprises a set of vertices and edges connecting the vertices, where each vertex represents a specific area embedded with a descriptor extracted by visually observing this area and recognizing it utilizing descriptors. Each robot has its local grid map stored for path planning, not shared between them. Considering the exploration task, a robot’s ability to choose a proper direction depends on the other robot’s locations and the unexplored areas. Our exploration framework is evaluated on the Gazebo simulator and real robots, increasing the exploration efficiency by 23%∼77%. Compared with the occupancy grid map scheme, our method’s data transfer is reduced by 84% 90%.
