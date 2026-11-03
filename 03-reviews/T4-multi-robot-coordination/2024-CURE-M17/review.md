# CURE: A Hierarchical Framework for Multi-Robot Autonomous Exploration Inspired by Centroids of Unknown Regions

## Metadata

| Field | Value |
|---|---|
| ID | M17 |
| Title | CURE: A Hierarchical Framework for Multi-Robot Autonomous Exploration Inspired by Centroids of Unknown Regions |
| Authors | Qingchen Bi, Xuebo Zhang, Jian Wen, Zhangchao Pan, Shiyong Zhang, Runhua Wang, and Jing Yuan |
| Venue | IEEE Transactions on Automation Science and Engineering, vol. 21, no. 3, pp. 3773-3786 |
| Year | 2024 (online 2023) |
| Type | journal |
| DOI | [10.1109/tase.2023.3285300](https://doi.org/10.1109/tase.2023.3285300) |
| Official URL | https://ieeexplore.ieee.org/document/10155622/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T4-multi-robot-coordination/2024-CURE-M17/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2024-CURE-M17/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2024-CURE-M17/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: differential-drive
- platform: Three Pioneer3-DX robots (hardware); Kobuki bases in Gazebo, described with two-wheel differential-drive limits in the legacy extraction
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: 2D laser scanner; wheel odometry (Gmapping)
- compute: One laptop per Pioneer3-DX; simulation on an Intel Core i7-11800H laptop; centroid detection under 10 ms
- compute_location: not-reported
- summary_result: Versus the RRT-based MR-RBE explorer, CURE reduces exploration time by up to 50.7% and path cost by up to 34.4% in Gazebo simulation.
- summary_limitation: The authors state that the centralized architecture makes central-node data transmission grow sharply with team size and leave a distributed version to future work.
- survey_included: yes
- verification_level: light

## Problem

The paper assigns which robot explores which unknown region, so that a team finishes 2D occupancy-grid coverage faster and with less path overlap than frontier-based or RRT-based explorers. Single-robot frontier detection slows down as the map grows, and teams can oscillate between targets and duplicate the same unknown cells.

## Mechanism

CURE is a centralized exploration planner. Its inputs are a merged occupancy map and the robot poses; its outputs are navigation goals. Dynamic Voronoi cells, with each robot as a site, partition the workspace so that teammates stay in disjoint regions. Unknown connected regions inside a per-robot local exploration window (LEW) are represented by their centroids. A global exploration window (GEW) is activated only when no LEW contains a centroid. A parameter-insensitive utility, the area of the unknown region divided by the distance to its centroid, scores candidate centroids, and a steering-cost reselection rule stops back-and-forth goal switching. Gmapping, multi-robot map merging, and the ROS Navigation stack execute the goals.

## Baselines and controls

The comparator is MR-RBE, an RRT-based multi-robot exploration approach. Team size (2 to 7 robots) and laser range (4 to 50 m) are ablated in simulation. Other controls are not recorded in the legacy extraction; not verified.

## Platform and setup

- Simulation: Gazebo with three Kobuki bases carrying a Hokuyo URG-04LX (180° field of view, 50 m range in simulation), speed limits 0.4 m/s and 1.0 rad/s, ROS Melodic. Six indoor maps (house, maze, office, factory, unstructured building, lab), five runs per map, and a coverage stop at 99%.
- Hardware: three Pioneer3-DX robots, each with a laptop and a 2D laser scanner (180° field of view; 6 m range in the mapping run and 8 m in the timed comparison), connected by a wireless LAN, on a structured indoor floor of 17 x 13 m². Two start layouts and three timed runs against MR-RBE.

## Evidence type and transfer

The largest gains (50.7% and 34.4%) come from Gazebo. The hardware runs close the loop on three Pioneer3-DX robots in one structured indoor environment, with three timed runs against MR-RBE. The scenes contain no crowds of pedestrians.

## Sensors

2D laser scanners and wheel odometry, used through Gmapping for occupancy mapping.

## Compute and latency

Each Pioneer3-DX carries a laptop; the legacy extraction does not say where the central planner ran. Simulation ran on an Intel Core i7-11800H laptop with 16 GB RAM. Centroid detection stays under 10 ms on maps up to 30 x 24 m². End-to-end planning latency is not recorded in the legacy extraction.

## Key quantitative results

- Exploration time versus MR-RBE: up to 50.7% lower, Gazebo (p. 8).
- Path cost versus MR-RBE: up to 34.4% lower, Gazebo (p. 2).
- Hardware, three timed runs: average exploration time 32.7% lower than MR-RBE at at least 99% coverage (p. 9).
- Hardware exploration completes in 136 s with a center start and 117 s with a corner start (p. 9).
- Centroid detection time: under 10 ms on maps up to 30 x 24 m² (p. 9).
- Team-size ablation: efficiency improves almost linearly from 2 to 4 robots and only slightly from 4 to 7 robots in the test environment (p. 11).

## Stated limitations

- The architecture is centralized, and the data transmission volume of the central node grows sharply when the team is large; a distributed architecture and lower bandwidth requirements are left to future work (p. 12).
- More than four robots are not necessary for the environment of Fig. 16, because efficiency stops improving notably (p. 11).

## Transfer conditions

Legacy reviewer observations, not located: the method is 2D occupancy-grid exploration, with 3D handled only as a projection of a traversable 3D map onto 2D, and over-long laser ranges raise compute without reducing exploration time. A reuse needs a central node with a reliable link to every robot, a merged 2D map, and the ROS Navigation stack. Heterogeneous teams are not tested (the hardware team is homogeneous). The stack is ROS Melodic with Gmapping, not ROS 2.

## Code and data

A supplementary video is linked in the abstract (https://youtu.be/P5jXKlGQOec). Code availability is not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | strong | Sec. I, p. 1 | "The core problem of multi-robot exploration is how to implement the cooperative strategy and reasonably determine which robot to explore the corresponding unknown region to minimize the overall time." |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI-C, p. 9 | "In this work, we use three Pioneer3-DX robots equipped with a laptop and a 2D laser scanner" |

## Page-cited excerpts

- **p. 1, Introduction.** "The core problem of multi-robot exploration is how to implement the cooperative strategy and reasonably determine which robot to explore the corresponding unknown region to minimize the overall time."
  Target assignment is the multi-robot problem the paper addresses; heterogeneous sensing is not tested.
- **p. 3, Approach overview.** "The architecture of the proposed approach is centralized."
  All goal assignment depends on a central node.
- **p. 9, Real-world experiments.** "In this work, we use three Pioneer3-DX robots equipped with a laptop and a 2D laser scanner"
  The hardware stack behind the real runs: a homogeneous team with 2D lasers and laptops.
- **p. 9, Real-world experiments.** "All robots communicate via a wireless local area network (LAN)."
  The centralized planner relies on a wireless LAN.
- **p. 12, Analysis.** "One limitation of the centralized architecture is that the data transmission volume of the central node will dramatically increase when the number of robots is large."
  The authors' main stated limitation.

## Survey-usable statements

### Supported

- A centralized Voronoi-partition and centroid-based planner cut exploration time by up to 50.7% and path cost by up to 34.4% versus an RRT-based team explorer in Gazebo (numbers from a light review; re-check before citing).
- The approach ran on three Pioneer3-DX robots with 2D lasers over a wireless LAN indoors.

### Not supported

- CURE is a distributed explorer: the architecture is centralized.
- More robots always speed exploration: efficiency stops improving notably beyond four robots in the tested environment.
- CURE handles 3D or unstructured outdoor exploration: the evaluation is 2D occupancy-grid exploration indoors.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Real robot, Claim summary, Hardware caveat) converted to the English template; C6 excerpt and limitation excerpts taken from sentences located for legacy facts (pp. 3, 9, 11, 12); 3D-projection and laser-range notes moved to Transfer conditions because they were not located; Year set to 2024 (online 2023) from the publication date on p. 1; abstract shortened to the abstract paragraph without the Note to Practitioners
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

In this paper, a novel multi-robot autonomous exploration approach CURE is proposed based on dynamic Voronoi diagrams and centroids of unknown connected regions. Compared with existing approaches, the novelty of this work is twofold: 1) Dynamic Voronoi diagram is used for partition of the space being explored to improve the efficiency of multirobot exploration, and then a new parameter-insensitive utility function is elaborately designed to evaluate the information of centroids, which helps guide the robot to explore unknown regions. 2) A hierarchical framework consisting of global and local exploration windows for detecting centroids is designed, wherein the global exploration window is activated to find centroids to guide the robot exploration when there are no centroids in any one local exploration window. We validate the feasibility and exploration efficiency of the proposed approach in various complex simulation scenarios and challenging realworld tasks. All test results show that the exploration time consumption and path cost are reduced by up to 50.7% and 34.4%, respectively, compared with an advanced RRT-based multi-robot exploration approach. (Supplementary video link: https://youtu.be/P5jXKlGQOec)
