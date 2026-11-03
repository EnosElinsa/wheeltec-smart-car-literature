# Multi-Robot Collaborative SLAM (Multi-SLAM) With Distributed Lightweight Predictive Frontier Exploration (LPFE)
## Metadata
| Field | Value |
|---|---|
| ID | E34 |
| Title | Multi-Robot Collaborative SLAM (Multi-SLAM) With Distributed Lightweight Predictive Frontier Exploration (LPFE) |
| Authors | Achala Athukorala, Billy Pik Lik Lau, Khattiya Pongsirijinda, Chau Yuen, and U-Xuan Tan |
| Venue | IEEE Robotics and Automation Letters, vol. 11, pp. 2274-2281 |
| Year | 2026 (online 2025) |
| Type | journal |
| DOI | [10.1109/lra.2025.3645990](https://doi.org/10.1109/lra.2025.3645990) |
| Official URL | https://ieeexplore.ieee.org/document/11303573/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Multi-SLAM-LPFE-E34/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Multi-SLAM-LPFE-E34/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2026-Multi-SLAM-LPFE-E34/citation.bib) |
## Survey coding
- survey_module: multi-robot
- secondary_modules: localization-mapping, traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: skid-steer
- platform: mini four-wheel skid-steer robots (4 in a 160 m2 office, 8 in a 1300 m2 corridor); Gazebo robots in simulation
- boundary_platform: no
- degradation: bandwidth-limit, compute-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: RPLiDAR A3M1 (hardware); simulated 10 m, 180-degree laser
- compute: LattePanda Alpha with Core m3-7Y30 and 8 GB onboard; simulation on i9-12900H, 64 GB, RTX 3070 Ti; LPFE plans at 0.3 Hz
- compute_location: onboard
- summary_result: In simulation, LPFE with Multi-SLAM explores on average 1.7 and 1.4 times faster than RRT and MMPF, with 65% and 38% less overlap.
- summary_limitation: The authors state that deterministic peer inference degrades gradually with longer disconnections and only maintains coordination in short outages.
- survey_included: yes
- verification_level: light
## Problem
Low-compute ground-robot fleets need low-bandwidth global map merging and less redundant exploration and coordination cost.
## Mechanism
Multi-SLAM builds on slam_toolbox with a two-layer graph: a dense local localization graph and a sparsely sampled global pose-scan graph. Each robot broadcasts LocalizedScan messages with scans and poses, and every robot optimizes the global graph independently. LPFE lets each robot compute N wavefront potential fields from the common map and robot positions, assign frontiers by a deterministic prediction, and add a repulsive potential; no extra goal-negotiation messages are sent.
## Baselines and controls
RRT and MMPF (also called SMMR in the paper) ground-robot exploration. All simulations use the paper's Multi-SLAM, so the comparison isolates the frontier assignment strategy, not the collaborative mapping itself. RACER is related work only and explicitly not a direct performance baseline.
## Platform and setup
- Simulation: Gazebo, 274, 578, and 2070 m2 maps with 2, 3, and 6 robots in the five configurations of Fig. 8, 15 runs each, 225 runs in total.
- Hardware: mini four-wheel skid-steer robots, 4 robots in a 160 m2 office and 8 robots in a 1300 m2 outdoor corridor, ROS 2 Humble navigation. The comparison algorithms were not deployed on hardware because the onboard compute was insufficient.
- Communication: Rajant DX2 2.4 GHz peer-to-peer mesh without a central access point.
## Evidence type and transfer
Real low-compute wheeled multi-robot autonomous exploration plus simulated comparisons. The legacy card records no test on the reference platform and no real disconnection stress test.
## Sensors
RPLiDAR A3M1 on the hardware robots; a 10 m, 180-degree laser in simulation. The legacy card records no external localization system.
## Compute and latency
Hardware: LattePanda Alpha with Core m3-7Y30 and 8 GB. Simulation: i9-12900H, 64 GB, RTX 3070 Ti. LPFE plans at 0.3 Hz, MMPF at 1 Hz, and RRT at 100 Hz, so the cumulative CPU time comparison mixes call-frequency differences and is not a per-call complexity comparison.
## Key quantitative results
- Simulation, versus RRT and MMPF: on average 1.7 and 1.4 times faster, 33% and 10% shorter distance, and 65% and 38% less overlap (p. 6).
- Cumulative CPU time on average 7 and 10 times lower than RRT and MMPF; this depends on the different planning frequencies (p. 6).
- Large map: LPFE 249 s CPU and 28.4 MB versus MMPF 2952 s and 497.4 MB; with 6 robots on the large map, RRT did not finish in any of 15 runs within 30 minutes (p. 6).
- Hardware: 4 robots in a 160 m2 office finished in 45 s, and 8 robots in a 1300 m2 corridor in 210 s; no hardware baseline or variance (Table I, p. 7 according to the legacy card).
- Bandwidth: 8 KB/s per robot for map sharing; the comparison with more than 450 KB/s (about 50 times) refers to map-merger methods in the paper's text, which were not run on the same hardware (p. 7).
## Stated limitations
- The deterministic inference of peer behavior degrades gradually with longer disconnections but maintains coordination in short outages (p. 4).
- The real deployment runs only LPFE with Multi-SLAM, because the onboard compute cannot run MMPF or RRT in real time (p. 7).
## Transfer conditions
Legacy reviewer observations:
- There is no global-optimality guarantee. Shared maps and stale positions affect the deterministic inference, and recovery after disconnection is only described qualitatively; disconnection duration, packet loss, latency, and consistency recovery are not quantified. Initial cross-robot frame calibration, synchronization, and probabilistic convergence are not given.
- "No extra goal messages" does not mean no communication: robots still share the scan-pose graph and last known positions.
- The hardware runs list no repetition counts, variance, ATE, or failure rate.
- The trial configuration on p. 6 is worded ambiguously; 225 runs correspond to the five Fig. 8 configurations times three methods times 15 runs, not to a full Cartesian product.
## Code and data
https://github.com/acachathuranga/LPFE ; the paper states a full ROS 1 and ROS 2 implementation. Supplementary material was not read and the repository was not run.
## Version family
The 2025 online version and the 2026 issue are the same Multi-SLAM plus LPFE article; the two modules are not two independent works.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | moderate | p. 4 | "The deterministic inference of peer behavior degrades gradually with longer disconnections but maintains coordination in short-term outages." |
| C5 | unset | n/a | | |
| C6 | partial-support | moderate | p. 7 | "only our LPFE algorithm with Multi-SLAM is deployed" |
## Page-cited excerpts
- **p. 4, Disconnection.** "The deterministic inference of peer behavior degrades gradually with longer disconnections but maintains coordination in short-term outages."
  The disconnection behavior is described qualitatively; durations and packet loss are not quantified.
- **p. 5, Information prerequisite.** "This deterministic inference mechanism allows robots to anticipate peer selections from the shared map and last known positions"
  The inference needs a shared map and last known positions, so communication is not zero.
- **p. 6, Planning frequencies.** "The planning frequency of MMPF and RRT algorithms are set to 1 Hz and 100 Hz respectively"
  LPFE plans at 0.3 Hz, so cumulative CPU savings depend on call frequency.
- **p. 7, Real deployment.** "only our LPFE algorithm with Multi-SLAM is deployed"
  The low-compute hardware runs only the proposed method; comparisons are in simulation.
- **p. 7, Bandwidth.** "During exploration, the bandwidth consumption per robot is 8 KB/s."
  The 8 KB/s is shared map data; LPFE sends no plans.
- **p. 7, Table I.** "The exploration completion times for these two environments are presented in Table I."
  Source of the hardware completion times; no hardware baseline or variance.
## Survey-usable statements
### Supported
- On low-compute skid-steer robots (Core m3 onboard), Multi-SLAM with LPFE completed real exploration with 4 robots in 160 m2 in 45 s and 8 robots in 1300 m2 in 210 s, using 8 KB/s per robot.
- In simulation with the same Multi-SLAM, deterministic predictive frontier assignment explores 1.7 and 1.4 times faster than RRT and MMPF.
### Not supported
- The method works without communication: robots share scans, poses, and positions.
- LPFE beats the baselines on real hardware: the baselines were not deployed on hardware.
- The CPU savings are per-call complexity gains: the planners run at different frequencies.
- Coordination stays intact under long disconnections: the authors state that it degrades with longer disconnections.
## Verification log
- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; no legacy quote dropped
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/324bd79124968ac1233ed5c2/
## Original abstract
Autonomous mobile robot systems have been extremely useful in exploration tasks for inspection and surveying of unknown environments, where map quality and exploration speed are often important factors. To effectively increase the exploration speed, multi-robot systems and collaborative exploration have been gaining attention in recent years. However, multi-robot exploration introduces two main challenges: 1) shared mapping between the robots; and 2) efficient coordination between the robots. Towards efficient and practical multi-robot exploration, this work proposes a new Distributed Multi-Robot Collaborative SLAM (Multi-SLAM) framework and a Lightweight Predictive Frontier Exploration (LPFE) to enable ground robot fleets to explore unknown environments faster and efficiently. Our Multi-SLAM approach generates a graph based globally optimized map using information from all robots in the environment in a network bandwidth efficient manner, while our LPFE coordinates the exploration of the robots using a deterministic, inference-based heuristic, allowing robots to anticipate one another’s actions without explicit communication. The experimental results demonstrate that our pipeline outperforms traditional frontier exploration approach, as well as state-of-the-art planners for ground robots, with up to 70% reduction in exploration times, with up to 13 less CPU usage and up to 50 less network bandwidth usage. We also present our Multi-SLAM and LPFE code-base which we have extensively tested in real-world robot fleets in different environments.
