# Multi-Robot Collaborative Navigation Framework Based on 3D Voronoi Partitioning in Uneven and Unstructured Environments

## Metadata

| Field | Value |
|---|---|
| ID | F09 |
| Title | Multi-Robot Collaborative Navigation Framework Based on 3D Voronoi Partitioning in Uneven and Unstructured Environments |
| Authors | Hongyang Zhao, Kunyu Xu, Nuo Xu, Xingdong Li, and Jing Jin |
| Venue | Journal of Field Robotics, 43(7), 4531–4548 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1002/rob.70260](https://doi.org/10.1002/rob.70260) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.70260 |
| Theme folder | T4-multi-robot-coordination |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Terrain-Voronoi-F09/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Terrain-Voronoi-F09/paper.md` (local only, not in the public repository); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Terrain-Voronoi-F09/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware, speed-capped
- platform_class: ackermann
- platform: Two Ackermann vehicles with Orin NX 8GB and RoboSense RS-LiDAR-C16; simulated Scout 2.0 vehicles use a different drive model
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: RoboSense RS-LiDAR-C16 point clouds and intensity with A-LOAM poses in hardware; simulated Velodyne HDL-32
- compute: Orin NX 8GB on the hardware vehicles; i9-14900K CPU and 32 GB RAM for simulation; no measured planning latency in selected pages
- compute_location: onboard
- summary_result: Two Ackermann robots completed collaborative navigation in four outdoor terrain scenarios at a 0.6 m/s speed cap.
- summary_limitation: The authors state that experiments used only two robots and identify more efficient task allocation and planning as future work.
- survey_included: yes
- verification_level: light

## Problem

Multiple robots navigating toward a common goal on uneven terrain must avoid both unsuitable ground and redundant or conflicting paths. The paper combines terrain analysis with spatial partitioning and intermediate-goal selection (pp. 1, 3). It narrows G3 by showing geometry-based terrain decisions in physical wheeled collaboration, but does not establish pose-uncertainty-conditioned terrain cost or speed. For G4 it provides a shared-map coordination architecture rather than an evaluated outage/reconnection policy (pp. 6–11, 15).

## Mechanism

Each robot uses A-LOAM mapping; robot-shaped and historical trajectory points are filtered before merging maps through intensity-adjusted FPFH reciprocal matching and SAC-IA registration (pp. 3, 5–6, 13). Robot positions act as dynamic seeds for communication-radius-constrained 3D Voronoi regions. TAPM-IVP fits a local reference plane, forms overlapping grids, separates elevated structure from ground, and classifies terrain using slope, height variation, roughness, and continuity (pp. 6–10). A greedy score combines goal direction, terrain traversability, and path continuity; secondary directions are searched when the primary direction is blocked or occupied (pp. 10–11).

The covariance matrix in reference-plane fitting is formed from terrain points relative to the robot position, with its smallest-eigenvalue eigenvector giving the plane normal (pp. 7–8, Eq. 12). It is not a pose-estimation covariance propagated into planning. The selected scoring and terrain-classification equations use geometry, fitted-plane validity, and current positions; no pose-covariance-conditioned speed or terrain-risk policy is shown (pp. 7–11).

## Baselines and controls

The reported simulation comparison uses single-robot PUTN (Jian et al. 2022) against the collaborative framework. OURS_D removes both TAPM-IVP spatial partitioning and greedy subgoal selection; it is a joint module ablation, so it does not isolate their individual contributions. All methods use the same local planner and path tracker, and each scenario uses common starting/goal conditions across ten independent trials (pp. 11–12). Hardware prose also reports PUTN fitting failures with the C16 LiDAR setup, without a matched repeated-trial hardware result table (p. 16). Table 2 values and plotted performance differences were not independently checked in this light reading.

## Platform and setup

Simulation uses Gazebo scenes and Scout 2.0 robots described as four-wheel differential drive, with simulated Velodyne HDL-32 LiDAR, A-LOAM, and a 0.6 m/s maximum linear speed. Simulations run on an i9-14900K desktop with 32 GB RAM and use three uneven/unstructured scenes, with ten trials per navigation method in each scene (pp. 7, 11–12).

Physical tests instead use two Ackermann vehicles, each equipped with Orin NX 8GB and RoboSense RS-LiDAR-C16, running A-LOAM with the same 0.6 m/s speed cap (p. 13). Four outdoor terrain scenes include gentle slopes, steep/high-gradient slopes, and forest clutter; the authors report both robots completing the collaborative navigation tasks (pp. 15–16). The hardware repeat count, independent ground truth, and quantitative failure statistics are not reported in the selected passages. Do not transfer the simulated Scout drive model to the physical Ackermann vehicles.

## Evidence type and transfer

The strongest evidence is closed-loop navigation by physical wheeled robots. Hardware evidence is described through trajectories, RViz views, and qualitative completion, while the repeated numerical baseline/ablation comparison belongs to simulation (pp. 11–16). This is direct evidence for terrain-aware collaborative route choice at the stated low speed, rather than boundary-platform evidence. Two-robot success does not validate larger-team performance, calibrated terrain safety, or behavior when localization and map registration are corrupted.

## Sensors

Hardware uses RoboSense RS-LiDAR-C16 with A-LOAM; LiDAR geometry and intensity feed mapping and map registration (pp. 6, 13). The simulation instead specifies Velodyne HDL-32 (p. 11). Poses and merged point clouds are shared over ROS (p. 15). Separate ground-truth sensors, wheel odometry/IMU integration, synchronization accuracy, and sensor failure detection were not established in the selected hardware passages.

## Compute and latency

The hardware vehicles carry Orin NX 8GB, while simulation runs on an i9-14900K desktop with 32 GB RAM (pp. 11, 13). ROS uses a Master hosted by one robot or a dedicated host on the common Wi-Fi LAN; robot nodes publish positions and point clouds (p. 15). A ROS Master is the communication architecture, not evidence that every planner executes on that host. The selected pages do not measure map-merge latency, planning frequency, network load, end-to-end control delay, or CPU/memory use. The 0.6 m/s limit is a commanded speed cap, not a timing benchmark.

## Key quantitative results

- Both physical Ackermann robots reportedly completed navigation in four outdoor terrain scenes; their maximum linear velocity was set to 0.6 m/s. The evidence is qualitative trajectories, without hardware repeat counts or numerical baseline statistics (pp. 13, 15–16).
- Simulation tested each method in ten independent trials per scene across three uneven/unstructured scenes; all methods shared the local planner/path tracker and maximum linear speed of 0.6 m/s (pp. 11–12).
- Table 2 reports simulation path length, time, success, collisions, and duplication, but its numeric cells were not independently verified or retained here; hardware completion is not that tabulated comparison (pp. 12, 16).

## Stated limitations

- The authors explicitly note that only two robots were used in both simulation and real-world experiments, while arguing scalability from Voronoi allocation (p. 14).
- The conclusion proposes reinforcement learning or large language models to improve future terrain task allocation, decisions, and planning while reducing computational requirements (p. 16). It gives no dedicated failure-mode limitation analysis.

## Transfer conditions

For G3, reproduce the terrain geometry and vehicle constraints before reuse: ground clearance, footprint, admissible slope, sparse-LiDAR plane fitting, point-cloud intensity behavior, and Ackermann tracking matter. The covariance used for plane fitting is a geometric scatter statistic; introducing pose uncertainty into clearance, traversability cost, or speed would require an additional model and evaluation. Report uncertainty calibration and task outcomes together rather than treating terrain classification as a pose-risk estimate.

For G4, the selected setup assumes positions and maps can be published on a common Wi-Fi LAN and registered into a common frame (pp. 6, 15). The communication-radius restriction limits which terrain points are allocated; it is not evidence of tested packet loss, sustained network partition, reconnection reconciliation, or containment of a bad local map. Those tests and stale-data behavior were not identified in the selected experiments. Validate message age, bad-registration rejection, map divergence, stop/replan behavior, and safe reunion on the target platform before making an outage-resilience claim. Larger-team scaling and the full allocation of computation between vehicles and any host also need measurement.

## Code and data

Figure 9 supplies a demonstration video: [navigation video](https://youtu.be/e8ko6NGstbs) (p. 14); the link was not opened. The data availability statement says, "The authors have nothing to report." (p. 17). An implementation or experiment-log release was not identified in the selected text; availability not verified.

## Version family

The selected text cites PUTN and related Voronoi/planning methods as predecessors and comparators, not as established earlier versions of this exact article. No duplicate conference or preprint version was established in this reading. Count this journal article once as F09.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | strong | Sec. 5.2, p. 15 | "Each robot operates as a ROS node, sharing critical data such as position information and point cloud maps through the publish‐subscribe mechanism." |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. 5.2, p. 14 | "It should be noted that although only two robots are used in both simulation and real‐world experiments, the proposed TAPM‐IVP framework possesses inherent scalability due to its task allocation based on Voronoi partitioning." |

## Page-cited excerpts

- **p. 7, Sec. 4.2.2.** "The covariance matrix for the selected point set is computed as follows:"
  The associated Eq. 12 and following eigenvector interpretation define terrain-plane fitting, not propagation of pose covariance into navigation risk.
- **p. 15, Sec. 5.2.** "We employ a Master‐based ROS communication architecture."
  The accompanying paragraph describes a common Wi-Fi LAN and shared positions/maps; it does not report disconnection or reunion tests.
- **p. 14, Sec. 5.2.** "It should be noted that although only two robots are used in both simulation and real‐world experiments, the proposed TAPM‐IVP framework possesses inherent scalability due to its task allocation based on Voronoi partitioning."
  Experimental scale is two robots; the larger-team claim is an architectural argument.

## Survey-usable statements

### Supported

- Geometry-based terrain analysis, 3D Voronoi allocation, and greedy intermediate-goal selection were integrated into low-speed collaborative navigation by two physical Ackermann robots on uneven outdoor terrain (pp. 6–11, 13–16).
- The system merges maps and publishes robot positions and point clouds through a common ROS/Wi-Fi architecture; a joint module ablation and single-robot baseline are evaluated in simulation (pp. 6, 11–12, 15).

### Not supported

- The reference-plane covariance is not evidence of pose-uncertainty-conditioned terrain cost or speed: the selected equations use geometric terrain features and fitted-plane validity (pp. 7–11).
- No measured tolerance to sustained communication loss, consistent map reunion, or propagation of corrupted local information is established by the selected Wi-Fi hardware or simulation experiments (pp. 11–16).
- The reported two-robot hardware trajectories do not establish statistically quantified safety, larger-team performance, or R680 deployment (pp. 13–16).

## Verification log

- 2026-11-02 | host: Codex | scope: new targeted light reading of physical PDF p. 1 abstract, p. 3 system definition, pp. 5–11 method/setup, pp. 12–16 evaluation/conclusion, and p. 17 data statement; selected prose numbers and excerpts checked; bound MinerU abstract/excerpts checked with review_check --pdf; Table 2 cells and plotted numeric results not independently checked; no whole-paper verification | corrections: new F09 card; physical Ackermann evidence separated from simulated Scout; geometric covariance, two-robot scale, and communication-test boundaries explicit.
- Legacy extraction: none; new targeted follow-up reading.

## Original abstract

Currently, research on cooperative navigation of multi‐robot systems in uneven terrain environments is still relatively scarce. The complex and rugged terrain features often pose significant threats to the navigation performance of each robot, thereby presenting considerable challenges for conducting safe and efficient collaborative operations in such environments. This article proposes a multi‐robot cooperative navigation framework aimed at addressing these challenges on uneven road surfaces. Based on three‐dimensional Voronoi partitioning, a terrain‐aware partitioning strategy (TAPM‐IVP) is introduced, enabling each robot to perform real‐time terrain analysis, categorizing the space into traversable space, non‐traversable space, and free space, thus facilitating task allocation in complex uneven terrain. Based on the partition results of TAPM‐IVP, a greedy heuristic sub‐goal decision method is proposed, which selects safe, non‐redundant, and collision‐free target points, employing a hierarchical generation strategy to guide the robotic system in efficiently navigating in unknown environments, thereby significantly enhancing navigation adaptability and task completion efficiency in uneven scenarios. Finally, both simulations and real‐world experiments validate the feasibility, safety, and efficiency of the proposed framework for cooperative navigation in uneven road conditions.
