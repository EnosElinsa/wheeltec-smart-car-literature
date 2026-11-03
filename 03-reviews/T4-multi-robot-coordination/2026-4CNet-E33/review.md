# 4CNet: A Diffusion Approach to Map Prediction for Decentralized Multirobot Exploration
## Metadata
| Field | Value |
|---|---|
| ID | E33 |
| Title | 4CNet: A Diffusion Approach to Map Prediction for Decentralized Multirobot Exploration |
| Authors | Aaron Hao Tan, Siddarth Narasimhan, and Goldie Nejat |
| Venue | IEEE Transactions on Robotics, vol. 42, pp. 1371-1388 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tro.2026.3666133](https://doi.org/10.1109/tro.2026.3666133) |
| Official URL | https://ieeexplore.ieee.org/document/11399635/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-4CNet-E33/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-4CNet-E33/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2026-4CNet-E33/citation.bib) |
## Survey coding
- survey_module: multi-robot
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: external-pose-source, speed-capped, few-trials
- platform_class: skid-steer
- platform: Clearpath Jackal (two outdoors, two indoors) and one Clearpath Ridgeback indoors; three simulated Jackals in Gazebo
- boundary_platform: no
- degradation: terrain, communication-delay-loss, energy-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: 360-degree Velodyne LiDAR, wheel encoders, IMU, GPS; RTAB-Map mapping
- compute: GTX 1050 GPU on the robots for map prediction (latency not reported); 5.452 s per prediction on an RTX 4090
- compute_location: onboard
- summary_result: In 30 x 30 m simulation with a high energy budget, 4CNet-E covers 58% of the area versus 42% (NPE), 42% (AEM), and 43% (T-AEM).
- summary_limitation: The authors assume that each robot obtains its position in a global frame from onboard GPS.
- survey_included: yes
- verification_level: light
## Problem
Robots with limited energy and communication budgets must predict unknown terrain and irregular obstacles and use low-bandwidth trajectory information from other robots to choose better exploration frontiers.
## Mechanism
A ResNet50 trajectory encoder is pretrained contrastively on map-trajectory pairs. A conditional consistency diffusion U-Net integrates the trajectories through cross-attention and denoises in 30 steps by default. A confidence network (RFC-AEM) predicts per-pixel confidence. Frontier utility combines information, terrain, and distance; navigation uses A* globally and TEB locally. Training uses procedurally generated height maps and A* trajectories.
## Baselines and controls
Map prediction: a map database (DB), AEM, and T-AEM (AEM with the same trajectory encoder). Exploration: NPE, AEM-E, T-AEM-E, and 4CNet-C-E without the confidence network; 4CNet-E-UB uses ground-truth predictions and serves only as an upper bound. Ablations remove the trajectories or the cross-attention and vary the confidence-network depth.
## Platform and setup
- Simulation: Gazebo with three Jackals in 225 m2 and 900 m2 environments.
- Outdoors: 45 x 15 m with two Jackals, three runs per method.
- Indoors: 8.5 x 8.5 m with two Jackals and one Ridgeback, a single case.
- All platforms are low-speed ground robots at about 0.15 m/s.
## Evidence type and transfer
Real multi-robot autonomous exploration plus procedurally generated training and test data and Gazebo simulation. The quantitative hardware results are mainly prediction metrics; the indoor three-robot run is a case study. Predicted coverage must not be read as fully observed coverage.
## Sensors
A 360-degree Velodyne LiDAR (range 1.5 m in simulation and 2.5 m on the robots), encoders, IMU, and GPS; RTAB-Map builds the maps, and a teleoperated reference map serves for evaluation. The legacy card notes that GPS accuracy indoors, or any substitute global localization, is not described.
## Compute and latency
Training on an i9-13900KF with an RTX 4090 and 64 GB. On the RTX 4090, 100 predictions take 5.452 s on average (map prediction network 5.319 s, trajectory encoder 0.0728 s, confidence network 0.0598 s); AEM takes 0.0687 s and DB 85.05 s (p. 13). The robots carry a GTX 1050 for map prediction, but the paper gives no onboard prediction latency, so the RTX 4090 values do not transfer.
## Key quantitative results
- Observed area coverage, 30 x 30 m, high energy budget: 4CNet-E 58% versus NPE 42%, AEM 42%, T-AEM 43%, and 4CNet-C-E 48%; the ground-truth-prediction upper bound is 68% (Table II, p. 12 according to the legacy card).
- Outdoor prediction metrics MSE/OIOU/FSIM/VTS: 4CNet 63.84/0.42/0.39/0.81 versus AEM 80.65/0.16/0.29/0.23 and DB 88.24/0.31/0.27/0.21 (p. 14, Table VI).
- Indoor case: the robots depleted their energy budgets at 324 s with observed coverage of 41%, 34%, and 35%; the rest of the area is predicted (p. 15).
- Runtime: 5.452 s per prediction on an RTX 4090 versus 0.0687 s for AEM and 85.05 s for DB (p. 13).
## Stated limitations
- Each robot is assumed to obtain its position in a global frame from onboard GPS (p. 5).
## Transfer conditions
Legacy reviewer observations:
- Trajectories are exchanged only within sensing range, and the communication success probability (CSP) is a Bernoulli event per trajectory position. On the robots, exchange needed RSSI above -50 dBm; CSP was 50% outdoors and 100% indoors. Byte rates, correlated burst outages, clock errors, and retransmission or consensus guarantees are not reported.
- The training distribution is simulated, and real maps are few. The method depends on GPS and on scale and grid alignment.
- Energy is a simplified distance-plus-climb model that ignores inference energy; budgets are in meters, not measured battery Wh.
- Prediction is slow (5.452 s on an RTX 4090), and the GTX 1050 latency is not reported.
- The utility coefficients appear both as [4, -1, -5] and as alpha = beta = gamma = 0.33 on p. 11, so reproduction parameters are ambiguous.
- No safety guarantee for unknown dynamic obstacles and no all-weather evidence.
## Code and data
The paper gives a demonstration video at https://youtu.be/nA2a3XXL5Dg (p. 16). The legacy extraction found no public repository for the source code or the two training sets; the video was not watched and no code was run.
## Version family
4CNet (T-RO 2026) is an independent work. 4CNet-E is the full exploration architecture of the same article and is not counted as a second paper.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | qualifies | moderate | Runtime, p. 13 | "4CNet exhibited an end-to-end computation time of 5.452 s." |
| C4 | qualifies | moderate | Assumptions, p. 5 | "We assume that each robot is able to obtain its own position with respect to a global frame acquired from an onboard global position system (GPS)." |
| C5 | unset | n/a | | |
| C6 | qualifies | weak | Hardware, p. 14 | "are equipped with a NVIDIA GTX 1050 GPU for running map prediction." |
## Page-cited excerpts
- **p. 5, Global localization assumption.** "We assume that each robot is able to obtain its own position with respect to a global frame acquired from an onboard global position system (GPS)."
  The cooperation relies on global GPS positions, not on purely relative localization.
- **p. 13, Runtime.** "4CNet exhibited an end-to-end computation time of 5.452 s."
  Measured over 100 predictions on an RTX 4090; not a high-rate onboard prediction.
- **p. 14, Real hardware.** "are equipped with a NVIDIA GTX 1050 GPU for running map prediction."
  The robot hardware differs from the RTX 4090 used for timing.
- **p. 15, Observed coverage.** "The exploration was completed at 324 s, where all three robots depleted their energy budget with an area coverage of 41%, 34%, and 35% for R1, R2, and R3, respectively."
  "Completed" means the budgets ran out, not that 100% of the area was observed.
- **p. 12, Table II.** "Table II presents the percentage of area coverage with respect to the three energy budgets"
  Source of the observed-coverage comparison.
## Survey-usable statements
### Supported
- In simulation with irregular obstacles and uneven terrain, diffusion-based map prediction conditioned on teammates' trajectories raises observed coverage under a high energy budget (58% versus 42-43% for NPE, AEM, and T-AEM in 30 x 30 m).
- On real Jackals outdoors, 4CNet's prediction metrics exceed AEM and the map database (for example MSE 63.84 versus 80.65 and 88.24).
### Not supported
- The robots fully observe the environment: the indoor case ended at 41%, 34%, and 35% observed coverage when the budgets ran out.
- The prediction runs at high rate onboard: 5.452 s per prediction on an RTX 4090, and the onboard GTX 1050 latency is not reported.
- The cooperation works without global positioning: each robot uses GPS in a global frame.
## Verification log
- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; no legacy quote dropped
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/e0b9ab9e4a3e416619121a5d/
## Original abstract
Mobile robots in unknown cluttered environments with irregularly shaped obstacles often face energy and communication challenges which directly affect their ability to explore these environments. Existing heuristic and learning-based map prediction methods are unable to generalize to irregular obstacles and uneven terrain, as they rely on single-pass architectures that cannot iteratively refine map predictions or incorporate uncertainty under limited communication and energy constraints. On the other hand, diffusion models perform multipass denoising to reconstruct high-fidelity maps from partial observations, enabling accurate predictions in resource constrained settings. In this article, we introduce a novel deep learning architecture, confidence-aware contrastive conditional consistency model (4CNet), for robot map prediction during decentralized, resource-limited multirobot exploration. 4CNet uniquely incorporates: 1) a conditional consistency model for map prediction in unstructured unknown regions, 2) a contrastive map-trajectory pretraining framework for a trajectory encoder that extracts spatial information from the trajectories of nearby robots during map prediction, and 3) a confidence network to measure the uncertainty of map prediction for effective exploration under resource constraints. We incorporate 4CNet within our proposed robot exploration with map prediction architecture, 4CNet-E. We then conduct extensive comparison studies with 4CNet-E and state-of-the-art heuristic and learning methods to investigate both map prediction and exploration performance in environments consisting of irregularly shaped obstacles and uneven terrain. Results showed that 4CNet-E obtained statistically significant higher prediction accuracy and area coverage with varying environment sizes, number of robots, energy budgets, and communication limitations when compared to database and learning-based methods. Hardware experiments were performed and validated the applicability and generalizability of 4CNet-E in both unstructured indoor and real natural outdoor environments.
