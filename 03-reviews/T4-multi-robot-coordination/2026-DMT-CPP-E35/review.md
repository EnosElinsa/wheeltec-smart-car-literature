# DMT-CPP: A Delaunay-Graph-Based Framework for Real-Time Multi-Robot Online Target Coverage
## Metadata
| Field | Value |
|---|---|
| ID | E35 |
| Title | DMT-CPP: A Delaunay-Graph-Based Framework for Real-Time Multi-Robot Online Target Coverage |
| Authors | Pengyu Wang, Zikai Wang, Ling Shi, and Max Q.-H. Meng |
| Venue | IEEE Robotics and Automation Letters, vol. 11, pp. 8785-8792 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3699254](https://doi.org/10.1109/lra.2026.3699254) |
| Official URL | https://ieeexplore.ieee.org/document/11543309/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-DMT-CPP-E35/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-DMT-CPP-E35/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2026-DMT-CPP-E35/citation.bib) |
## Survey coding
- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: motion-capture-pose, few-trials
- platform_class: differential-drive
- platform: two TurtleBot3 Burger (2.25 x 2 m) and three TurtleBot4 (5.5 x 4.4 m); simulated robots at 1 m/s
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: OptiTrack motion capture for localization; occupancy cells within 1 m of each robot sent to the planner (sensor not named)
- compute: simulation on i7-10700F; 24.54 ms per coverage step (15 robots, 100 targets, Map 1); hardware planner computer not reported
- compute_location: not-reported
- summary_result: With 100 targets, DMT-CPP cuts coverage completion time by up to 27.10% and 11.31% versus MAC-Planner and ACO-VP in simulation.
- summary_limitation: The authors treat the allocation behavior as a principled heuristic rather than a strict theoretical guarantee; the planner is a centralized entity.
- survey_included: yes
- verification_level: light
## Problem
Multi-robot online coverage of known discrete target positions with locally unknown obstacles, balancing the workload and reducing the cost of cost estimation and replanning.
## Mechanism
A sparse Delaunay graph is built over target and robot positions, with edge costs from grid-based JPS. Allocation alternates K-means clustering with local pairwise reassignment; Dijkstra selects the next target, and JPS plans the detailed path. When a robot runs out of tasks, the graph is rebuilt and tasks are reallocated; obstacle changes update the affected edges. Conflicts between robots are handled by simple priority-based yielding.
## Baselines and controls
MAC-Planner and ACO-VP. Ablations replace the Delaunay graph with 4- or 8-connected grid adjacency, remove the iterative clustering, or remove pairwise reassignment. No baseline is run on the hardware platforms.
## Platform and setup
- Simulation in Python on three maps (80 x 40, 150 x 60, and 120 x 80 m), 5-30 robots, 30-150 targets, nominal coverage time 100 s with standard deviation 20 s; simulated robots move at 1 m/s with a 5 m detection range.
- Hardware: two TurtleBot3 Burger in 2.25 x 2 m and three TurtleBot4 in 5.5 x 4.4 m, both in small motion-capture rooms.
- A central planning entity continuously receives all robot positions and new obstacle observations and sends paths (p. 5).
## Evidence type and transfer
Small-scale centrally coordinated wheeled task coverage on hardware plus large-scale simulation. On hardware, the unknown map is emulated by releasing occupancy information within a range; this is not fully autonomous perception and SLAM and not a test of communication faults. Target coordinates are known in advance.
## Sensors
OptiTrack provides localization on hardware. Only occupancy cells within a 1 m detection range are sent to the planner; the legacy card notes that the paper does not say which onboard sensor measures them, so no LiDAR model can be assumed.
## Compute and latency
Simulation on an i7-10700F. For 15 robots and 100 targets: Map 1 preparation 10.99 +/- 0.45 s and coverage step 24.54 +/- 2.28 ms; Map 2 preparation 15.06 +/- 0.44 s and step 33.62 +/- 2.31 ms. The tens of milliseconds are per coverage step and exclude preparation. The central computer on hardware is not reported.
## Key quantitative results
- 100 targets, experiment 1: completion time up to 27.10% and 11.31% lower than MAC-Planner and ACO-VP (p. 6).
- Experiment 3, 20 robots and 150 targets: 29.1% and 17.36% lower than MAC-Planner and ACO-VP (p. 6).
- Computation, 15 robots and 100 targets: Map 1 preparation 10.99 +/- 0.45 s and coverage step 24.54 +/- 2.28 ms; Map 2 15.06 +/- 0.44 s and 33.62 +/- 2.31 ms (Table I, p. 6 according to the legacy card).
- Hardware: two robots 85 s, 100% target coverage, 18.6 m total path; three robots 312 s, 98.7% coverage, 74.3 m total path; not every hardware run reached 100% (Table II, p. 7 according to the legacy card).
## Stated limitations
- The allocation convergence is treated as a principled heuristic rather than a strict theoretical guarantee (p. 4).
- The planner is implemented as a centralized entity (p. 5).
## Transfer conditions
Legacy reviewer observations:
- The method assumes known targets and real-time central positions and has no mechanism for communication constraints. Bandwidth, packet loss, latency, link loss, and reconnection are not modeled.
- The Delaunay approximation of costs has no general error bound. Inter-robot conflicts are resolved only by priority yielding, without a formal deadlock or collision proof.
- The paper writes the number of path computations for the full cost matrix as (K+1)! on p. 3, which contradicts the quadratic complexity of Remark 1 on p. 4; the factorial wording is not adopted.
- The hardware spaces are small, with no baseline and no repeated statistics.
## Code and data
The legacy extraction found no code or data repository URL in the paper. The algorithm and supplementary material were not run, and availability of the simulation and hardware data was not verified.
## Version family
DMT-CPP (RA-L 2026) is an independent work. MAC-Planner is its direct predecessor baseline, not a duplicate version, and the coverage planning and task allocation modules are not split into two papers.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | qualifies | moderate | p. 5 | "The pseudo-code in Algorithm 1 outlines the implementation details of the DMT-CPP planner as a centralized entity." |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | p. 7 | "all localized by the same OptiTrack system" |
## Page-cited excerpts
- **p. 5, Centralized implementation.** "The pseudo-code in Algorithm 1 outlines the implementation details of the DMT-CPP planner as a centralized entity."
  The planner is centralized; this does not support decentralized or disconnection-robust claims.
- **p. 3, Known targets.** "designated target points, which are marked as known locations and are accessible to robots within the workspace."
  Target positions are known; what is unknown is the obstacles and task progress.
- **p. 4, Guarantee boundary.** "While this behavior is consistently observed in experiments, it is treated as a principled heuristic rather than a strict theoretical guarantee."
  Allocation convergence is empirical, not a global-optimality or convergence guarantee.
- **p. 7, Motion capture.** "all localized by the same OptiTrack system"
  Hardware robots share external motion-capture localization.
- **p. 7, Sensing emulation.** "from cells within a 1-meter detection range of the robots was transmitted, simulating the map-building process in an unknown environment."
  Only cells within 1 m are released to emulate mapping; no real LiDAR SLAM deployment.
- **p. 7, Table II.** "the planner effectively coordinates the robots to perform coverage tasks in the workspace."
  Context of the hardware coverage table; the three-robot run reached 98.7%.
- **p. 6, Table I.** "All three methods exhibit comparable computational costs within the same order of magnitude."
  The per-step milliseconds exclude the preparation stage.
## Survey-usable statements
### Supported
- In simulation with known targets and online-revealed obstacles, Delaunay-graph allocation with K-means and pairwise reassignment reduces completion time by up to 27.10% and 11.31% versus MAC-Planner and ACO-VP (100 targets).
- A central planner drove two and three TurtleBots to 100% and 98.7% target coverage in small motion-capture rooms.
### Not supported
- The method is decentralized or robust to communication loss: it is a centralized planner with continuous position updates.
- The hardware runs show onboard perception and localization: OptiTrack provides poses and occupancy is emulated within 1 m.
- Allocation is provably optimal or convergent: the authors call it a heuristic.
## Verification log
- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; no legacy quote dropped
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/d1f64800a9356017c0f8dfd3/
## Original abstract
In this article, we propose a Delaunay-graph-based Multi-Robot Online Target Coverage Path Planner (DMT-CPP) to enhance multi-robot systems’ performance in online target coverage tasks. We present an innovative task allocation mechanism by maintaining a Delaunay graph according to the real-time condition. By applying K-means clustering and pairwise optimization on this graph, this mechanism can achieve computationally efficient and equitable task distribution. Additionally, we propose a novel path planning mechanism that utilizes the Delaunay graph to determine the coverage target and plan the tracking path, guaranteeing the algorithm’s real-time performance within dynamic workspaces. Extensive comparative experiments demonstrate DMT-CPP’s exceptional coverage efficiency, in terms of reduced coverage completion time, relative to state-of-the-art methods and confirm its effectiveness in real-time applications. Real-world experiments further validate the planner’s effectiveness and robustness in practical implementations.
