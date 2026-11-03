# Communication-Efficient Multi-Robot Exploration Using Coverage-Biased Distributed Q-Learning

## Metadata

| Field | Value |
|---|---|
| ID | M25 |
| Title | Communication-Efficient Multi-Robot Exploration Using Coverage-Biased Distributed Q-Learning |
| Authors | Ehsan Latif and Ramviyas Parasuraman |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 3, pp. 2622-2629 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3358095](https://doi.org/10.1109/lra.2024.3358095) |
| Official URL | https://ieeexplore.ieee.org/document/10413563/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T4-multi-robot-coordination/2024-comm-efficient-explore-M25/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2024-comm-efficient-explore-M25/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2024-comm-efficient-explore-M25/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: simulation
- evidence_all: simulation
- protocol_caveats: none
- platform_class: differential-drive
- platform: TurtleBot3 in ROS Gazebo; real TurtleBot3 runs shown only in a video
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: 2D laser scanner (15 m range in simulation); wheel odometry (Gmapping)
- compute: Not reported beyond CPU and RAM usage per method in Gazebo
- compute_location: not-reported
- summary_result: In Gazebo with TurtleBot3 teams, CQLite reached the same mapping efficiency as RRT and DRL explorers with about half the CPU load and 80% less communication.
- summary_limitation: The authors leave reward generality to other multi-robot tasks to future work and assume flat ground and a connected communication graph.
- survey_included: yes
- verification_level: light

## Problem

Cooperative map exploration when robots must share occupancy maps and learning state at every iteration. Frontier-RRT and deep reinforcement learning (DRL) explorers incur high communication payload, CPU, and RAM costs and overlap their coverage. The authors want distributed Q-learning that still covers indoor maps under limited connectivity.

## Mechanism

CQLite is distributed tabular Q-learning with a coverage-biased reward, not a deep policy. Each robot detects frontiers on its local occupancy map, treats the current and next frontier as the MDP state, and updates only the Q-value of the chosen action. Neighbors receive that Q-value and newly found frontiers instead of a full Q-table. Occupancy maps are merged ad hoc (feature-based merge) only when a robot finds no new frontiers. Voronoi subgraphs from Lloyd's algorithm split the remaining coverage. Stated modeling assumptions: flat terrain, omnidirectional ranging, a communication range much larger than the sensing range, and a connected Wi-Fi graph (partial disconnection raises re-exploration). Gmapping, known initial relative poses, `move_base` (Dijkstra plus DWA), and A* on the Q-graph complete the stack.

## Baselines and controls

RRT-based optimized exploration and Voronoi-based DRL exploration. Other controls are not recorded in the legacy extraction; not verified.

## Platform and setup

ROS Gazebo with TurtleBot3 robots: laser range 15 m, fully connected Wi-Fi over 40-60 m, maximum speed 0.5 m/s and π/4 rad/s, ten trials. Worlds: the Gazebo house (about 250 m², 3 robots) and the AWS bookstore (about 100 m², 3 and 6 robots). Metrics: mapping time, path length, exploration percentage, overlap percentage, map SSIM, CPU percentage, RAM, and communication payload.

## Evidence type and transfer

All tabulated metrics come from Gazebo with known initial poses and a fully connected Wi-Fi graph. The authors state that real-world robot experiments confirm the findings, as shown in the attached video; the letter reports no table of real-robot metrics. The phrase "real-life three-robot bookshop scenario" in the discussion sits next to the AWS bookstore Gazebo results. Evidence is therefore coded as simulation.

## Sensors

2D laser scanner and wheel odometry, used through Gmapping.

## Compute and latency

CPU percentage and RAM per method are reported from Gazebo. The processor is not recorded in the legacy extraction; not verified.

## Key quantitative results

- Communication: same mapping efficiency as the comparators with about half the CPU load and 80% less communication overhead, Gazebo (p. 8).
- Average communication payload more than 80% smaller than RRT and DRL, with higher map SSIM, Gazebo (p. 7).
- Mapping time: DRL is faster than CQLite in the house world, where DRL was trained (no page).

## Stated limitations

- Reward generality of CQLite for other multi-robot applications is left to future work (p. 8).
- The exploration model assumes flat ground terrain (p. 3).
- The connectivity graph is assumed connected throughout exploration; under partial disconnection coverage is kept at the cost of increased re-exploration (p. 3).

## Transfer conditions

Legacy reviewer observations: map merging needs a known initial relative pose, omnidirectional sensing and a communication range much larger than the sensing range are modeling assumptions, and severe network partitions are not part of the main trials. DRL can be faster when it is already trained on the same map. A wheeled robot reusing CQLite needs Gmapping-style 2D occupancy mapping and `move_base`; the hardware behavior is shown only in a video.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | direct-support | strong | Sec. V, p. 8 | "This letter proposed CQLite, a distributed Q-learning strategy for multi-robot exploration created to get around the excessive communication and computation complexity and expense of learning-based systems." |
| C4 | direct-support | strong | Sec. II, p. 2 | "in both RRT and DRL, robots share locally explored maps on every iteration and apply map merging" |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. III, p. 3 | "Assumptions: For simplicity, we assume a flat ground terrain environment for exploration." |

## Page-cited excerpts

- **p. 8, Conclusion.** "This letter proposed CQLite, a distributed Q-learning strategy for multi-robot exploration created to get around the excessive communication and computation complexity and expense of learning-based systems."
  CQLite is offered as a lighter alternative to learning-based explorers, not as proof that DRL cannot run on edge hardware.
- **p. 2, Related work.** "in both RRT and DRL, robots share locally explored maps on every iteration and apply map merging"
  Per-iteration map sharing is the communication cost the method targets.
- **p. 2, Related work.** "We reduce this overhead by only sharing and applying map merging in an ad-hoc manner."
  The mechanism behind the communication savings.
- **p. 2, Introduction.** "confirm the findings through real-world robot experiments, as demonstrated in the attached video"
  The hardware evidence is a video, not a metric table.
- **p. 3, Proposed approach.** "Assumptions: For simplicity, we assume a flat ground terrain environment for exploration."
  A stated modeling assumption that limits transfer to rough terrain.

## Survey-usable statements

### Supported

- Sharing only updated Q-values and new frontiers, with ad hoc map merging, cut communication by about 80% and CPU load by about half versus RRT and DRL explorers in Gazebo TurtleBot3 teams (numbers from a light review; re-check before citing).

### Not supported

- CQLite was validated quantitatively on real robots: real-robot evidence is a video only.
- CQLite is robust to network partitions: the simulated Wi-Fi graph is fully connected, and connectivity is an assumption.
- CQLite is faster than DRL everywhere: DRL is faster in the house world on which it was trained.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Real robot, Claim summary, Hardware caveat) converted to the English template; the legacy C4 quote with an ellipsis was split into two contiguous quotes (p. 2); C6 excerpt and limitation pages taken from sentences located for legacy facts (pp. 3, 8); evidence coded as simulation because the hardware runs appear only in a video; the DRL house-world result has no located page
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Frontier exploration and reinforcement learning have historically been used to solve the problem of enabling many mobile robots to autonomously and cooperatively explore complex surroundings. These methods need to keep an internal global map for navigation, but they do not consider the high costs of communication and information sharing between robots. This study offers CQLite, a novel distributed Q-learning technique that minimizes data communication between robots while achieving rapid convergence and thorough coverage in multi-robot exploration. The proposed CQLite method uses ad hoc map merging, and selectively shares updated Q-values at recently identified frontiers to reduce communication costs significantly. The theoretical analysis of CQLite's convergence and efficiency and extensive numerical verification on simulated indoor maps utilizing several robots demonstrate the method's novelty. With over 2 reductions in computation and communication alongside improved mapping performance, CQLite outperformed cutting-edge multi-robot exploration techniques like Rapidly-exploring Random Trees and Deep Reinforcement Learning.
