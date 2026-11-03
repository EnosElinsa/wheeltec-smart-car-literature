# WiSER-X: Wireless Signal-Based Decentralized Multi-Robot Exploration Without Explicit Information Exchange
## Metadata
| Field | Value |
|---|---|
| ID | E32 |
| Title | WiSER-X: Wireless Signal-Based Decentralized Multi-Robot Exploration Without Explicit Information Exchange |
| Authors | Ninad Jadhav, Meghna Behari, Robert J. Wood, and Stephanie Gil |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 9, pp. 10983-10990 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3711857](https://doi.org/10.1109/lra.2026.3711857) |
| Official URL | https://ieeexplore.ieee.org/document/11600992/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-WiSER-X-E32/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-WiSER-X-E32/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2026-WiSER-X-E32/citation.bib) |
## Survey coding
- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: offboard-compute, speed-capped, few-trials
- platform_class: differential-drive
- platform: two modified TurtleBots (70 m2 test); two or three robots in the larger-space test; three simulated ground robots in Gazebo
- boundary_platform: no
- degradation: actuator-fault, bandwidth-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: 2D LiDAR (GMapping), Qorvo DWM1001-DEV UWB ranging, rotating dual-antenna Wi-Fi (WSR) angle-of-arrival
- compute: UP-Squared boards onboard for sensing, measurement generation, and SLAM; WiSER-X decisions run offboard in real time; no CPU load reported
- compute_location: mixed
- summary_result: In 20 Gazebo runs per condition, WiSER-X has 58% less coverage overlap than an independent-frontier baseline and 23% more than a full-information-sharing baseline.
- summary_limitation: The authors assume known environment boundaries and known initial global robot positions, and leave intermittent communication to future work.
- survey_included: yes
- verification_level: light
## Problem
Can robots that cannot exchange maps or trajectories infer their teammates' coverage only from wireless pings, so that they reduce redundant exploration and can terminate exploration asynchronously? The paper addresses decentralized multi-robot exploration under severe communication limits.
## Mechanism
UWB time of flight gives range, and phase measurements of a rotating dual-antenna Wi-Fi setup give angle-of-arrival candidates. A PDAF with a 95% gate suppresses multipath, and an HGrid stores teammate positions and their covariances. Frontier utility is the information gain minus the redundant information weighted by the relative-pose uncertainty, combined with distance to select a frontier. A robot whose pings stop is treated as failed, and its earlier coverage area is re-explored (p. 3-5 in the legacy card). The HGrid soft threshold was tuned by hand between 50% and 75% depending on the scene, so coverage and stopping are sensitive to it.
## Baselines and controls
Baseline-1 is explore-lite with independent frontiers. Baseline-2 is RRT-exploration with a full map and a global assigner (an oracle). Baseline-3 is a pre-partitioned divide-and-conquer method, used only in the heterogeneous-speed test. Baselines 1 and 2 stop through a map-merging oracle at 95% coverage, while WiSER-X stops by its own threshold, so the stopping criteria are not equivalent (p. 5-7 in the legacy card).
## Platform and setup
- Simulation: Gazebo 1600 m2 office, three ground robots, 20 runs per condition. Relative measurements are ground truth plus Gaussian noise of 10 cm in range and 5 deg in angle.
- Hardware, small space: 70 m2, two modified TurtleBots with UP-Squared boards, GMapping and TEB, at 0.05 m/s (slow robot 0.01 m/s). UWB at 10 Hz; Wi-Fi uses about 100 packets per 3 s window, with an AOA update every 2 s. Three runs each for the same-speed, heterogeneous-speed, and failure scenarios; the main results are in Fig. 6, and the legacy card did not estimate unlabeled means from the figure.
- Hardware, larger space: 352 m2 in the text and 325 m2 in the Fig. 7 caption (the conflict is kept). Two or three robots, three runs each, LiDAR range 3.5 m, 0.1 m/s, UWB at 1 Hz, Wi-Fi 30 packets/s (about 15 kb/s) (p. 6-7 in the legacy card).
## Evidence type and transfer
The robots explore autonomously in hardware, but the WiSER-X decision module ran offboard because of a compute-board fault, so the hardware evidence is not fully onboard (p. 7 in the legacy card). "Without explicit information exchange" still means wireless packets and ranging: the method assumes that pings are received in all areas and that the environment boundary and each robot's initial global position are known (p. 2-3 in the legacy card). No collision rate, CPU use, or dense dynamic-crowd test is reported.
## Sensors
LiDAR for GMapping, a Qorvo DWM1001-DEV UWB module for range, and a rotating dual-antenna Wi-Fi setup (WSR) for bearing. In simulation, relative measurements are simulated from ground truth with added noise.
## Compute and latency
Sensing, measurement generation, and SLAM ran onboard on UP-Squared boards; WiSER-X decisions ran offboard in real time. The legacy card records no CPU utilization or latency numbers.
## Key quantitative results
- Coverage overlap in simulation: 58% lower than Baseline-1 (independent frontiers) and 23% higher than Baseline-2 (full information sharing) (p. 7).
- Exploration time versus Baseline-1: 1.65 times faster, about 34% time saved (p. 7).
- Autonomous termination in simulation: 93% total coverage (standard deviation 3.6%) in about 365 s; the abstract's "full coverage" is not a per-run 100% guarantee (p. 7).
- Heterogeneous speeds: 140 s (about 34%) saved versus the partitioning baseline; the legacy card gives 140 +/- 9 s (p. 7).
- Single random robot failure at 50-70% of exploration: about 10% +/- 4.25% of the map would otherwise be lost, and the method recovers it (p. 7).
- The statement "Baseline-2 takes 56% longer" is ambiguous against the paper's own comparison sentences and is not used for further calculation (p. 7).
## Stated limitations
- The method assumes known environment boundaries and that robots know their own initial global positions (p. 3).
- The conclusion lists intermittent communication as future work (p. 7).
## Transfer conditions
Legacy reviewer observations: the ambiguity between packet loss and robot failure, unknown boundaries, and accumulated drift are not resolved. Raw hardware logs, confidence intervals, and significance tests are not reported. The ROS, GMapping, and TEB interfaces match a typical wheeled research robot stack, but the method needs extra UWB and rotating dual-antenna radio hardware; packet loss, initial coordinates, thresholds, and the true onboard load must be checked, and the method cannot be reproduced with an existing LiDAR alone.
## Code and data
The authors provide https://github.com/Harvard-REACT/wiserx_explore, based on the C++ explore-lite package (p. 1). Code execution, data completeness, and hardware driver compatibility were not verified.
## Version family
The RA-L article and the project of the same title are counted as one work.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | moderate | Abstract, p. 1 | "Simulation results show that WiSER-X achieves 58% less overlap than a zeroinformation-sharing baseline and only 23% more overlap than a full-information-sharing baseline." |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Assumptions, p. 3 | "known environment boundaries, and (ii) robots know their own" |
## Page-cited excerpts
- **p. 3, Assumptions.** "known environment boundaries, and (ii) robots know their own"
  The method assumes known boundaries and known initial global positions of each robot.
- **p. 7, Simulation results.** "93% total map coverage (3.6% standard deviation) in approximately 365 seconds"
  Mean over 20 simulated runs with autonomous termination; coverage is not 100% in every run.
- **p. 7, Baselines.** "Baselines 1 and 2 use a map-merging oracle to terminate exploration"
  The baselines stop through an oracle at 95% merged coverage, unlike WiSER-X.
- **p. 1, Abstract.** "Hardware experiments further validate the feasibility of WiSER-X using onboard sensing."
  The hardware claim covers onboard sensing; the decision module itself ran offboard according to the legacy card.
## Survey-usable statements
### Supported
- In Gazebo with three robots, inferring teammate coverage from UWB and Wi-Fi relative-position estimates cuts coverage overlap by 58% versus independent frontier exploration, at 23% more overlap than full information sharing.
- Wireless-signal relative positioning can replace map exchange for coordination when pings are received everywhere and boundaries and initial positions are known.
### Not supported
- The method guarantees full coverage in every run: autonomous termination reached 93% +/- 3.6% on average in simulation.
- The method runs fully onboard in hardware: the WiSER-X decision module ran offboard.
- The method needs no communication: it relies on ping packets and ranging radios in all areas.
## Verification log
- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; legacy quote "The WiSER-X algorithm was executed offboard in realtime" dropped because the PDF text layer of p. 7 has no word spaces there (the fact is kept in the prose)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/6a3111584b803097a3e02df6/
## Original abstract
We present WiSER-X (Wireless Signal-based Efficient multi-Robot eXploration), a fully decentralized algorithm that enables a team of autonomous robots to coordinate the exploration of unknown environments under severe communication limitations, using only signal ping packets. WiSER-X uses inter-robot relative position estimates, obtained from onboard wireless signal–based sensors, to guide exploration decisions and minimize redundant coverage, resulting in global coordination from local decision-making. The algorithm supports asynchronous exploration termination without requiring a shared global map, adapts to heterogeneous robot behaviors, and remains robust to complete failures while ensuring full coverage. Simulation results show that WiSER-X achieves 58% less overlap than a zeroinformation-sharing baseline and only 23% more overlap than a full-information-sharing baseline. Hardware experiments further validate the feasibility of WiSER-X using onboard sensing.
