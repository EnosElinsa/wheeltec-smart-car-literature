# Riemannian Optimization for Active Mapping With Robot Teams

## Metadata

| Field | Value |
|---|---|
| ID | X08 |
| Title | Riemannian Optimization for Active Mapping With Robot Teams |
| Authors | Arash Asgharivaskasi, Fritz Girke, and Nikolay Atanasov |
| Venue | IEEE Transactions on Robotics, vol. 41, pp. 1077-1097 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3526295](https://doi.org/10.1109/tro.2025.3526295) |
| Official URL | https://doi.org/10.1109/tro.2025.3526295 |
| Theme folder | T4-multi-robot-coordination |
| Batch | supplemental |
| Local files | `01-papers/T4-multi-robot-coordination/2025-Riemannian-active-map-X08/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2025-Riemannian-active-map-X08/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2025-Riemannian-active-map-X08/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping, traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: skid-steer
- platform: Two ClearPath Jackal UGVs and one F1/10 car (hardware); six ClearPath Husky robots in Unity and four Jackals in Gazebo; drive type of the Jackal from the vocabulary example, not from the paper text
- boundary_platform: no
- degradation: none
- degradation_observed: communication-partition
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: RGB-D camera (RealSense D455); 3D LiDAR (Ouster OS1-32) on the Jackals; 2D LiDAR (Hokuyo UST-10LX) on the F1/10 car
- compute: Onboard GTX 1650 (Jackal) and Jetson Xavier NX (F1/10); onboard mapping at about 2.1-2.6 Hz
- compute_location: onboard
- summary_result: No numeric team result is recorded in the legacy extraction; onboard distributed semantic mapping ran at about 2.1-2.6 Hz on two Jackals and an F1/10 car.
- summary_limitation: The authors state that Theorem 1 guarantees only a locally optimal consensus solution, and that extended communication interruptions could make robots revisit explored areas.
- survey_included: yes
- verification_level: light

## Problem

Centralized team mapping fails when the central node fails and needs heavy communication infrastructure. Decentralized active mapping has mostly used linear-Gaussian observations and Euclidean robot states, so map consensus and team-trajectory optimality on non-Euclidean manifolds remain open.

## Mechanism

ROAM (Riemannian optimization for active mapping) is distributed gradient descent on a communication graph with a consensus constraint, and it needs only one-hop communication. Mapping works on categorical map probability mass functions in a semantic octree; planning works on SE(3) viewpoint trajectories. Onboard, RGB-D images are semantically labeled, fused into a 3D semantic point cloud, and merged by octree consensus. A ledger synchronizes planning when a fraction of the robots is ready, and local A* on a 2D occupancy projection executes the viewpoints.

## Baselines and controls

3DMR in the Gazebo office comparison. In Unity, full, hierarchical, and ring communication networks are compared. Other controls are not recorded in the legacy extraction; not verified.

## Platform and setup

- Unity: outdoor village with six ClearPath Husky robots, assumed known poses and perfect semantics, under full, hierarchical, and ring networks.
- Gazebo: indoor office with four Jackals versus 3DMR.
- Hardware: an indoor basement (lobby, corridor, laboratory) with two ClearPath Jackals (Ouster OS1-32, RealSense D455, GTX 1650) and one F1/10 car (Hokuyo UST-10LX, D455, Xavier NX). Semantic segmentation uses ResNet18 trained on SUN RGB-D through TensorRT. Localization uses direct LiDAR odometry on the Jackals and ICP on the F1/10; frames are aligned with an AprilTag, and ROS runs as Wi-Fi multimaster.

## Evidence type and transfer

The hardware run closes the loop on three ground robots in one indoor basement. Intermittent Wi-Fi cutoffs occurred during the run; they were not designed into the evaluation. The simulation results assume known poses and, in Unity, perfect semantics.

## Sensors

RGB-D camera on all robots; 3D LiDAR on the Jackals and 2D LiDAR on the F1/10 car, used for odometry.

## Compute and latency

Onboard GTX 1650 on the Jackals and Jetson Xavier NX on the F1/10 car. Onboard mapping runs at about 2.1-2.6 Hz. Planning latency is not recorded in the legacy extraction.

## Key quantitative results

- Onboard mapping rate: about 2.1-2.6 Hz on the hardware robots (p. 15).
- Other numeric results are not recorded in the legacy extraction; not verified.

## Stated limitations

- Theorem 1 guarantees only a locally optimal consensus solution (p. 9).
- Extended periods of communication interruption could lead to inefficient exploration, because robots may revisit areas their peers already explored; this did not occur in the hardware trial because the robots were far apart (p. 15).
- Future work includes the distance to consensus and suboptimality bounds for nonconvex distances and nonconcave objectives (p. 16), and time-varying communication, unknown robot localization, and adversarial map sharing (p. 16).

## Transfer conditions

Legacy reviewer observation: the bandwidth of octree broadcasts grows with coverage. The hardware run relies on AprilTag frame alignment at the start, LiDAR odometry, and a GPU-class onboard computer for semantic segmentation. A wheeled robot reusing ROAM needs an RGB-D camera, a semantic segmentation network, and a ROS multimaster link.

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
| C4 | direct-support | strong | Sec. VI-D, p. 15 | "During the disconnection period, the robots could not plan collaboratively and relied only on their local maps for planning." |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 15, Real-world experiments.** "During the disconnection period, the robots could not plan collaboratively and relied only on their local maps for planning."
  Communication loss forces local-only planning; in this trial the cutoff did not reduce final coverage because the robots were far apart.
- **p. 15, Real-world experiments.** "Extended periods of communication interruption could lead to inefficient exploration because the robots may revisit already explored areas"
  The authors' statement of the cost of disconnection.
- **p. 9, Multirobot planning.** "Hence, Theorem 1 guarantees only a locally optimal consensus solution."
  Nonconvex SE(3) geometry limits the guarantee to local optimality (the legacy card recorded this as a qualifying C4 relation).
- **p. 16, Conclusion.** "An important future research direction involves analyzing the distance to consensus as well as the suboptimality bounds for ROAM in the case of nonconvex distance measures and nonconcave objective functions."
  The theoretical guarantees are open for the nonconvex case.

## Survey-usable statements

### Supported

- Distributed Riemannian optimization with one-hop communication ran active semantic mapping on two Jackals and an F1/10 car, and robots fell back to local-only planning during Wi-Fi cutoffs.

### Not supported

- ROAM guarantees a globally optimal team plan: Theorem 1 guarantees only a locally optimal consensus solution.
- Communication cutoffs do not hurt ROAM: the trial was unaffected only because the robots were far apart, and the authors state that extended interruptions could cause revisits.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: structured extraction converted to the English template; the legacy card had two C4 rows (direct-support and qualifies), kept as one direct-support row with the Theorem 1 quote moved to the excerpts; limitation pages taken from sentences located for legacy facts (pp. 15, 16); the legacy card records no result values beyond the mapping rate
- Legacy extraction: automated reviewer (codex), supplemental batch.

## Original abstract

Autonomous exploration of unknown environments using a team of mobile robots demands distributed perception and planning strategies to enable efficient and scalable performance. Ideally, each robot should update its map and plan its motion not only relying on its own observations, but also considering the observations of its peers. Centralized solutions to multirobot coordination are susceptible to central node failure and require a sophisticated communication infrastructure for reliable operation. Current decentralized active mapping methods consider simplistic robot models with linear-Gaussian observations and Euclidean robot states. In this work, we present a distributed multirobot mapping and planning method, called Riemannian optimization for active mapping (ROAM). We formulate an optimization problem over a graph with node variables belonging to a Riemannian manifold and a consensus constraint requiring feasible solutions to agree on the node variables. We develop a distributed Riemannian optimization algorithm that relies only on one-hop communication to solve the problem with consensus and optimality guarantees. We show that multirobot active mapping can be achieved via two applications of our distributed Riemannian optimization over different manifolds: distributed estimation of a 3-D semantic map and distributed planning of SE(3) trajectories that minimize map uncertainty. We demonstrate the performance of ROAM in simulation and real-world experiments using a team of robots with RGB-D cameras.
