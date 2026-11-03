# Real-Time Multilevel Terrain-Aware Path Planning for Ground Mobile Robots in Large-Scale Rough Terrains

## Metadata

| Field | Value |
|---|---|
| ID | M12 |
| Title | Real-Time Multilevel Terrain-Aware Path Planning for Ground Mobile Robots in Large-Scale Rough Terrains |
| Authors | Yuxiang Li, Kun Chen, Yifei Wang, Weifan Zhang, Jiancheng Wang, Haoyao Chen, and Yunhui Liu |
| Venue | IEEE Transactions on Robotics, vol. 41, pp. 4159-4179 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3577015](https://doi.org/10.1109/tro.2025.3577015) |
| Official URL | https://ieeexplore.ieee.org/document/11027468/ |
| Theme folder | T3-planning-control |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T3-planning-control/2025-terrain-aware-plan-M12/paper.pdf` and `02-fulltext/T3-planning-control/2025-terrain-aware-plan-M12/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-terrain-aware-plan-M12/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: tracked
- platform: articulated tracked search-and-rescue robot with flippers; differential-wheeled robot in Gazebo only
- boundary_platform: yes
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: LiDAR, IMU (FAST-LIO2 pose)
- compute: Intel Core i9-10900K CPU, 32 GB RAM, onboard; runtimes not recorded in the legacy extraction
- compute_location: onboard
- summary_result: In simulation and field tests over map volumes up to 1360 m3, the planner outperformed ECTN, PUTN, SSSN, CS, and GEO; the legacy extraction records no values.
- summary_limitation: Terrain-material and friction prediction is out of scope under a quasi-static assumption, and real configuration errors exceed simulated ones because of localization and mapping uncertainty.
- survey_included: yes
- verification_level: light

## Problem

Path planning for high-DoF ground robots, especially articulated tracked
search-and-rescue platforms, on large-scale rough 3D terrain. Tip-over,
contact loss, and multilayer structures break 2.5D maps.

## Mechanism

A two-layer planner. The global layer uses an implicit Gaussian-voxel map
with slope, roughness, and sparsity traversability and a constrained A*
search. The local layer estimates configuration stability iteratively and
geometrically (settling under gravity, support polygon and center of mass)
and commands tracks and flippers. Modular robot abstractions also cover a
differential-wheeled robot with stricter slope and roughness thresholds.
Pose comes from FAST-LIO2 (LiDAR-IMU). Tracks are driven by MPC, flippers by
PID.

## Baselines and controls

The comparators are ECTN, PUTN, SSSN, CS, and GEO.

## Platform and setup

Gazebo models of an articulated tracked robot and a differential-wheeled
robot, with ground-truth odometry and LiDAR in simulation. Real field tests
use the tracked search-and-rescue robot with LiDAR and IMU, with map volumes
up to 1360 m3 (debris, stairs, tent, office, bumps, ramps).

## Evidence type and transfer

Field evidence is closed-loop navigation of the tracked robot. Applicability
to wheeled robots is shown only in simulation. The platform is therefore
coded as tracked, a boundary platform for this survey.

## Sensors

LiDAR and IMU, fused by FAST-LIO2 for pose. Simulation uses ground-truth
odometry.

## Compute and latency

The legacy extraction records an onboard Intel Core i9-10900K CPU with 32 GB
RAM. Planning runtimes are not recorded in the legacy extraction.

## Key quantitative results

- Field maps reached a volume of up to 1360 m3 (p. 18).
- The planner outperformed ECTN, PUTN, SSSN, CS, and GEO across simulated and real terrains; the legacy extraction records no values (p. 14).

## Stated limitations

- Predicting terrain materials and estimating friction coefficients are beyond the scope of the article; the analysis assumes quasi-static dynamics (p. 8).
- Configuration errors in real-world scenes were slightly larger than in simulation because of localization and mapping uncertainty (p. 19).
- Future work: parallelize configuration-stability estimation, add dynamic force analysis to remove the quasi-static assumption, and feed local-layer data back to the global map (p. 20).

## Transfer conditions

The field evidence is an articulated tracked robot with flippers and a
desktop-class onboard PC, not a small differential-drive wheeled chassis.
Wheeled use needs the stricter slope and roughness thresholds that were
tested only in simulation, a 3D LiDAR, and an IMU.

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
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI, p. 11 | "in the real world, the robot was equipped with LiDAR and IMU, with the captured data fed into the SLAM module [42] for pose estimation." |

## Page-cited excerpts

- **p. 11, Sec. VI.** "in the real world, the robot was equipped with LiDAR and IMU, with the captured data fed into the SLAM module [42] for pose estimation."
  Real-world evidence uses the tracked robot; the wheeled robot appears only in Gazebo.
- **p. 8, configuration-stability estimation.** "However, predicting terrain materials and estimating friction coefficients are beyond the scope of this article."
  The stability model ignores terrain material and friction.
- **p. 19, Sec. VI.** "configuration errors in real-world scenes were slightly larger than those observed in simulations due to localization and mapping uncertainty"
  Localization and mapping errors propagate into the stability estimate.

## Survey-usable statements

### Supported

- A global implicit-map planner coupled with local geometric stability estimation planned paths for a tracked robot in field scenes with map volumes up to 1360 m3 (numbers from a light review; re-check before citing).
- Localization and mapping uncertainty increased configuration errors in the field compared with simulation.

### Not supported

- Field validation on a wheeled robot: the wheeled robot appears only in simulation.
- Handling of slippery or deformable ground: friction and terrain material are out of scope.

## Verification log

- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); legacy C6 excerpt trimmed to its second sentence (the first sentence was not checked); legacy limitations given pages from text search; the 1360 m3 value is found on the PDF page but not in the transcription
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Autonomous ground mobile robots rely on their configuration characteristics to prevent tip-overs and collisions, ensuring safe navigation in complex environments. However, complex configurations with specially designed links and joints produce a higher dimensional workspace and bring significant challenges for path planning, especially in large-scale rough terrains. To address this, we propose a real-time multilevel terrain-aware path planning framework that integrates different levels of terrain awareness into the global and local layers. An implicit map representation is introduced at the global layer to enable efficient terrain analysis and path planning, while an iterative geometric evaluation is designed at the local layer to estimate configuration stability and improve path smoothness. By sharing the global layer information with the local layer, the framework enhances path planning efficiency and adaptability in complex environments. Its modular design supports diverse robot configurations and pathfinding algorithms, enabling effective autonomous navigation in large-scale 3-D terrains with online or offline maps. Simulations and real-world experiments demonstrated that our approach outperforms state of the art across diverse environments, including uneven terrains, multilayered structures, and complex debris fields. The results highlighted that our approach provides faster and safer path planning, more accurate and robust configuration-stability estimation, and higher success rates in traversing complex 3-D environments.
