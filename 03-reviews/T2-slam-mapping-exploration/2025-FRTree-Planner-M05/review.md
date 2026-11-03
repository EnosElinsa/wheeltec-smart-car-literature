# FRTree Planner: Robot Navigation in Cluttered and Unknown Environments With Tree of Free Regions

## Metadata

| Field | Value |
|---|---|
| ID | M05 |
| Title | FRTree Planner: Robot Navigation in Cluttered and Unknown Environments With Tree of Free Regions |
| Authors | Yulin Li, Zhicheng Song, Chunxin Zheng, Zhihai Bi, Kai Chen, Michael Yu Wang, and Jun Ma |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 4, pp. 3811-3818 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3544519](https://doi.org/10.1109/lra.2025.3544519) |
| Official URL | https://ieeexplore.ieee.org/document/10897898/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2025-FRTree-Planner-M05/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2025-FRTree-Planner-M05/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2025-FRTree-Planner-M05/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware
- platform_class: legged
- platform: Unitree Go1 quadruped; simulated maze and random forest
- boundary_platform: yes
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: 3D LiDAR (Livox MID360) on the real robot
- compute: Intel NUC13 (i7-1360P) for the whole real system; Intel i5-13400F in simulation; no latency recorded in the legacy extraction
- compute_location: not-reported
- summary_result: A Unitree Go1 with a MID360 LiDAR traversed a 5 m by 6 m cluttered room with static and dynamic obstacles; simulation values are not recorded in the legacy extraction.
- summary_limitation: No limitation is stated by the authors; the hardware evidence is one quadruped run in a small indoor room.
- survey_included: yes
- verification_level: light

## Problem

Goal-directed navigation in fully unknown cluttered space with limited sensor range, narrow passages, dead ends and bug traps, and changing obstacles, without a prior map. Geometry-agnostic free-space graphs either miss traversable gaps or produce overly conservative detours.

## Mechanism

FRTree incrementally builds a tree of overlapping polytopic free regions from local perception. It prunes nodes whose free-region volume or intersection cannot contain the robot geometry, and greedily selects intermediate goals with a backtracking escape from traps. A geometry-aware bi-level trajectory optimizer, with sum-of-squares (SOS) containment of the robot body in the free-region corridor, generates the local motion. The pipeline has no occupancy or ESDF map; the tree itself encodes the topology.

## Baselines and controls

RRTX and Faster in the random-forest benchmark. Other controls are not recorded in the legacy extraction; not verified.

## Platform and setup

Simulation on an Intel i5-13400F: a maze with narrow passages and dead ends, and a 15 m by 5 m random forest at three obstacle densities, compared with RRTX and Faster by completion rate, path-length ratio, and safety. Real test: a Unitree Go1 quadruped with an onboard MID360 LiDAR and the whole stack on an Intel NUC13 (i7-1360P), traversing a 5 m by 6 m indoor cluttered room with static and dynamic obstacles.

## Evidence type and transfer

The quantitative comparison is in simulation. The hardware evidence is a trajectory shown on the Go1 (Fig. 6) in one small indoor room, not outdoor uneven terrain and not a wheeled chassis.

## Sensors

3D LiDAR (Livox MID360) on the real robot.

## Compute and latency

Intel i5-13400F in simulation and Intel NUC13 with an i7-1360P for the real system. Replanning latency is not recorded in the legacy extraction; not verified.

## Key quantitative results

Not recorded in the legacy extraction; not verified. The legacy card names the simulation metrics (completion rate, path-length ratio, safety) against RRTX and Faster but gives no values.

## Stated limitations

The authors state no limitation; the conclusion reports capability on complex layouts and unknown terrains, not residual failures.

## Transfer conditions

Legacy reviewer observations: free-region quality and passage access are tied to a specific robot geometry, so the tree and the optimizer must be retuned for another footprint. The published hardware is a quadruped with a MID360, not a differential-drive wheeled platform. The real evaluation is a single small indoor room, not outdoor uneven terrain, and residual failure under sensing degradation is not quantified.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. V, p. 8 | "The shortest feasible direction is continuously selected towards the target configuration, enabling safe and efficient navigation while adapting to environmental changes." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV, p. 7 | "In this section, we deployed our framework on a unitree Go1 robot to test its performance in a cluttered indoor environment." |

## Page-cited excerpts

- **p. 8, Conclusion.** "The shortest feasible direction is continuously selected towards the target configuration, enabling safe and efficient navigation while adapting to environmental changes."
  Changing environments are the designed problem; the conclusion does not quantify failures.
- **p. 1, Abstract.** "navigating around dead-end situations, and avoidance of dynamic obstacles without a prior map"
  Dead ends and dynamic obstacles without a prior map are the target conditions.
- **p. 7, Real-world experiment.** "In this section, we deployed our framework on a unitree Go1 robot to test its performance in a cluttered indoor environment."
  The hardware platform is a quadruped, not a wheeled robot.
- **p. 7, Real-world experiment.** "We use the onboard MID360 LiDAR to perceive the point cloud data for dynamic tree updating."
  The real perception is a 3D LiDAR.

## Survey-usable statements

### Supported

- A tree of geometry-checked free regions with a bi-level trajectory optimizer navigates unknown clutter with narrow passages and dead ends without a prior map, shown in simulation and on a Go1 quadruped indoors.

### Not supported

- FRTree is validated on a wheeled robot: the hardware is a Unitree Go1 quadruped.
- FRTree is validated outdoors or on rough terrain: the real test is one 5 m by 6 m indoor room.
- FRTree transfers to any footprint without changes: free-region access depends on the robot geometry.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Claim summary, Hardware caveat) converted to the English template; the legacy card had no verbatim quotes, so excerpts were taken from the abstract and conclusion and from sentences located for legacy facts (p. 7); legacy limitations, which are reviewer observations, moved to Transfer conditions
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

In this work, we present FRTree planner, a novel robot navigation framework that leverages a tree structure of free regions, specifically designed for navigation in cluttered and unknown environments with narrow passages. The framework continuously incorporates real-time perceptive information to identify distinct navigation options and dynamically expands the tree toward explorable and traversable directions. This dynamically constructed tree incrementally encodes the geometric and topological information of the collision-free space, enabling efficient selection of the intermediate goals, navigating around dead-end situations, and avoidance of dynamic obstacles without a prior map. Crucially, our method performs a comprehensive analysis of the geometric relationship between free regions and the robot during online replanning. In particular, the planner assesses the accessibility of candidate passages based on the robot’s geometries, facilitating the effective selection of the most viable intermediate goals through accessible narrow passages while minimizing unnecessary detours. By combining the free region information with a bi-level trajectory optimization tailored for robots with specific geometries, our approach generates robust and adaptable obstacle avoidance strategies in confined spaces. Through extensive simulations and real-world experiments, FRTree demonstrates its superiority over benchmark methods in generating safe, efficient motion plans through highly cluttered and unknown terrains with narrow gaps.
