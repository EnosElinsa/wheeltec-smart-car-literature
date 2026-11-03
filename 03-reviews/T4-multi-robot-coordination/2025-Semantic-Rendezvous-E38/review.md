# Multi-robot rendezvous in communication-restricted unknown environments via backtracking and semantic frontier-based exploration
## Metadata
| Field | Value |
|---|---|
| ID | E38 |
| Title | Multi-robot rendezvous in communication-restricted unknown environments via backtracking and semantic frontier-based exploration |
| Authors | Matteo Luperto, Mauro Tellaroli, Michele Antonazzi, and Nicola Basilico |
| Venue | Robotics and Autonomous Systems, vol. 194, article 105137 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1016/j.robot.2025.105137](https://doi.org/10.1016/j.robot.2025.105137) |
| Official URL | https://linkinghub.elsevier.com/retrieve/pii/S0921889025002349 |
| Theme folder | T4-multi-robot-coordination |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T4-multi-robot-coordination/2025-Semantic-Rendezvous-E38/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2025-Semantic-Rendezvous-E38/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2025-Semantic-Rendezvous-E38/citation.bib) |
## Survey coding
- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: simulation
- evidence_all: simulation
- protocol_caveats: none
- platform_class: differential-drive
- platform: simulated TurtleBot3 Burger robots in Gazebo (teams of 3, 5, and 8)
- boundary_platform: no
- degradation: communication-partition
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: simulated 10 m 2D LiDAR; Gmapping; semantic regions from an oracle
- compute: not reported (processor, memory, GPU, and per-step time not given)
- compute_location: not-reported
- summary_result: With three robots on three maps, FBE-BT-U(0.5) reduces mean rendezvous time by 43.35% versus FBE, at 6.89% less jointly explored area, in Gazebo simulation.
- summary_limitation: The authors leave empirical evaluation on real multi-robot systems to future work; all results are Gazebo simulations with an oracle for semantic regions.
- survey_included: yes
- verification_level: light
## Problem
Homogeneous robots start at different positions in an unknown indoor map and explore independently, without knowing where teammates are and without an agreed meeting point. Robots can communicate only with an unobstructed line of sight within distance d. Rendezvous means that the whole team forms a multi-hop connected network; physical proximity is a soft constraint, and the robots need not gather at one coordinate (p. 4-5 in the legacy card).
## Mechanism
The usual frontier-based exploration (FBE) utility, frontier length gain minus travel distance, is extended with virtual backtracking frontiers inside the known area. Circular footprints of the time-stamped trajectory expire, and their boundaries become frontiers that make robots re-traverse old areas; only the trajectory record decays, not the SLAM map. After an encounter, the robots merge frontiers and trajectories and elect a leader whom the others follow; the leader removes frontiers covered by other robots' recent trajectories (p. 5-7 in the legacy card). Variants: FBE-BT uses plain backtracking; FBE-BT-U(gamma) raises the utility of frontiers in high-connectivity areas, with gamma = 0.15, 0.3, or 0.5; FBE-BT-A generates backtracking frontiers only in those areas. Defaults: d = 2.7 m, trajectory radius 1.5 m, pose recorded every 2 s, expiry after about 5 min, backtracking frontiers added after 18 s, alpha = 1/4.
## Baselines and controls
The main baseline is the standard FBE of Yamauchi and others. The ablation FBE-U(0.5) adds only the semantic preference without backtracking. No other complete system, such as IR2 or the intermittent rendezvous of da Silva and others, is compared quantitatively; citation is not an experimental baseline.
## Platform and setup
Gazebo simulation only, with no physical robot experiment. The "real multi-robot control setup" of p. 7 is the real ROS software control stack, run in Gazebo. Simulated TurtleBot3 Burger robots at 0.3 m/s with a 10 m 2D LiDAR, Gmapping, and move_base, with simulated sensing and actuation errors; ROS namespaces separate the robot stacks. More than 400 real-time simulation runs on five indoor maps (Ring, Office, Intel, Campus-1, Campus-2), with 3, 5, or 8 robots in some configurations and 10 runs per configuration. Start positions were drawn at random once and then fixed per map. Semantic regions (corridors, halls, large open areas) come from an oracle; they cover 37%, 32%, and 30% of Ring, Office, and Intel.
## Evidence type and transfer
All quantitative results are from simulation. The experiments use idealized formation dynamics: a real leader-follower software implementation initially failed to follow in narrow passages, so this was abstracted away. Team splitting is not simulated, and runs with permanent navigation failure are excluded, with their number not reported; R = 1 is therefore not an end-to-end success rate over all started runs.
## Sensors
Simulated 10 m 2D LiDAR for Gmapping and move_base. Semantic labels come from an oracle; online semantic recognition is neither implemented nor evaluated.
## Compute and latency
Not recorded in the legacy extraction; not verified. The legacy card states that processor, memory, GPU, per-step time, and onboard resources are not reported.
## Key quantitative results
- Three robots, three maps, FBE-BT-U(0.5) versus FBE: mean rendezvous time 43.35% lower and joint explored area 6.89% lower, averaged as relative values per map (p. 10).
- Ring, FBE-BT-U(0.5) versus FBE: 1257.26 s versus 2483.54 s; joint area 0.804 versus 0.914 (p. 10, Tables 1-2).
- Ring, FBE-BT versus FBE: 1652.30 s versus 2483.54 s; R = 1 versus 0.7 (Table 3); when FBE fails to meet, the time of the last complete exploration is used (p. 10).
- Eight robots, FBE-BT versus FBE: Ring 2106.52 s versus 2016.90 s and Office 1309.45 s versus 1251.54 s, 4.44% and 4.63% slower (p. 12).
- Campus-1 and Campus-2, three robots, FBE-BT versus FBE: time 32.76% and 40.31% lower, area 5.04% and 15.30% lower; FBE already reaches R = 1 on both maps (p. 13, Table 4).
- The authors report that all 150 runs of the proposed method in Table 1 and all 60 BT runs in Table 3 met; these sets may share configurations and are not independent trial counts.
## Stated limitations
- Empirical evaluation on real multi-robot systems is future work (p. 13).
- Semantic regions are assumed to come from an oracle (p. 9).
- Runs in which a robot fails permanently in navigation are excluded from the averages (p. 9).
## Transfer conditions
Legacy reviewer observations:
- Baseline times for failed runs do not include the fallback travel to the center.
- The table header calls sigma a variance while the text calls it a standard deviation, and the Intel FBE sigma differs between Tables 1 and 4, so sigma is not used for significance. The p. 11 description of default FBE success on Ring and Office does not match the order of Tables 3 and 4; the tables are used. No significance tests or confidence intervals.
- A high gamma can make robots circle corridors and explore fewer new areas (p. 11 and p. 13, Fig. 14). A larger communication range does not always shorten completion time, because early merging of small clusters reduces the spread of the joint trajectories. Real wireless throughput, latency, and random packet loss are not tested.
- Only the first full-team encounter is handled; this is not a periodic coordination protocol for intermittent connectivity, and there is no finite-time rendezvous guarantee.
- Transfer to a wheeled robot with 2D LiDAR SLAM and move_base can reuse the trajectory cache and start with FBE-BT without semantics. Robot discovery, cross-map frame alignment and frontier exchange, and real leader-follower collision avoidance and recovery must be added; the semantic variant also needs online corridor recognition with noise evaluation.
## Code and data
The paper gives a page with code and full experimental results at https://aislab.di.unimi.it/research/fberendezvous/ (p. 9); the data availability statement says data are available on request. Availability of the page, execution, and data download were not verified.
## Version family
The paper extends the authors' AIxIA 2023 paper [19] and IROS 2024 paper [20] (p. 3); [20] is "Frontier-based exploration for multi-robot rendezvous in communication-restricted unknown environments", pp. 5807-5812, DOI 10.1109/IROS58592.2024.10801321. The journal adds the semantic high-connectivity variants FBE-BT-U and FBE-BT-A, the joint explored area and implicit coordination analysis, and extended simulations. The work is tracked as one research family; the earlier full texts were not compared page by page. IROS 2024 DOI 10.1109/IROS58592.2024.10802343 (E39, da Silva and others) is the external reference [30], not a version of this work.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | partial-support | moderate | Abstract, p. 1 | "Efficient decentralized execution with limited communication and in unknown environments can be essential in several applications" |
| C5 | unset | n/a | | |
| C6 | qualifies | strong | Conclusion, p. 13 | "future work involves conducting empirical evaluations of our approach" |
## Page-cited excerpts
- **p. 3, Introduction.** "paper extends our previous contribution of [19,20]"
  The authors extend their AIxIA 2023 and IROS 2024 papers.
- **p. 6, Method.** "We call these frontiers, formed through information decay,"
  Virtual backtracking frontiers come from time-decayed trajectory records.
- **p. 7, Setup.** "With such a control setup, we perform runs on"
  The ROS control stack runs in Gazebo; all runs are simulated.
- **p. 9, Semantic regions.** "we assume that the robot can query an oracle"
  Semantic regions come from an oracle; prediction errors from sensors are not tested.
- **p. 9, Averaging.** "Our average results do not include runs where one"
  Runs with permanent navigation failure are excluded from the averages.
- **p. 10, Results.** "the total area explored by the MRS is only"
  Faster rendezvous comes with a smaller explored area.
- **p. 12, Team size.** "Results of FBE-BT compared with FBE when a team"
  With eight robots, FBE-BT is 4.44% and 4.63% slower on Ring and Office.
- **p. 13, Conclusion.** "future work involves conducting empirical evaluations of our approach"
  Real multi-robot experiments are future work.
## Survey-usable statements
### Supported
- In Gazebo simulation with three robots and oracle semantic regions, backtracking frontiers that favor high-connectivity areas cut mean rendezvous time by 43.35% versus standard frontier exploration, at 6.89% less explored area.
- Rendezvous speed trades off against explored area in this method family.
### Not supported
- The method is validated on physical robots: all results are Gazebo simulations, and real experiments are future work.
- Backtracking speeds up rendezvous for every team size: with eight robots, FBE-BT is 4.44% and 4.63% slower than FBE on Ring and Office.
- R = 1 is an end-to-end success rate: runs with permanent navigation failure are excluded.
- The semantic variant works with online semantic perception: regions come from an oracle.
## Verification log
- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; no legacy quote dropped
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/a8b15dd85855f0aaa3dbecf6/
## Original abstract
The multi-robot rendezvous problem requires coordinating a team of mobile robots to converge at a common location. Efficient decentralized execution with limited communication and in unknown environments can be essential in several applications, but such real-world robotic features are often not captured by theoretical rendezvous frameworks. In this work, we present an approach to this problem that extends traditional frontierbased exploration strategies to facilitate efficient rendezvous in such conditions. Our method allows robots to backtrack their exploration of the environment and exploit semantic knowledge on the map by prioritizing high-connectivity areas like corridors and hallways. We define and evaluate different variants of our method to study a trade-off between the time taken to perform a rendezvous and the amount of discovered area in the environment. Extensive experimental evaluation in ROS using 3D simulations demonstrates the feasibility of our method and its performance improvements over baselines.
