# Reinforcement Learned Distributed Multi-Robot Navigation With Reciprocal Velocity Obstacle Shaped Rewards

## Metadata

| Field | Value |
|---|---|
| ID | M38 |
| Title | Reinforcement Learned Distributed Multi-Robot Navigation With Reciprocal Velocity Obstacle Shaped Rewards |
| Authors | Ruihua Han, Shengduo Chen, Shuaijun Wang, Zeqing Zhang, Rui Gao, Qi Hao, and Jia Pan |
| Venue | IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 5896-5903 |
| Year | 2022 |
| Type | journal |
| DOI | [10.1109/lra.2022.3161699](https://doi.org/10.1109/lra.2022.3161699) |
| Official URL | https://ieeexplore.ieee.org/document/9740403/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T4-multi-robot-coordination/2022-RL-distributed-nav-M38/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2022-RL-distributed-nav-M38/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2022-RL-distributed-nav-M38/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: external-pose-source
- platform_class: differential-drive
- platform: Up to eight Turtlebots, described as differential-drive in the text (p. 7); disc robots in OpenAI Gym
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: Neighbor positions and velocities within 4 m (RVO and VO vectors); UWB localization and ROS messaging on hardware
- compute: Mini PC per Turtlebot onboard; training about 10 h on an Intel i7-9700 with a GTX 1080
- compute_location: onboard
- summary_result: On 4, 6, and 8 real Turtlebots in a circle crossing, RL-RVO reaches 1.00, 0.91, and 0.89 success versus 1.00, 0.85, and 0.68 for NH-ORCA over 50 trials.
- summary_limitation: The authors leave navigation under more challenging real-world uncertainties to future work.
- survey_included: yes
- verification_level: light

## Problem

Distributed multi-robot collision avoidance when each differential-drive robot has only local information about neighbors and obstacles. Centralized planners scale poorly and depend on a stable link to the central controller. Classical velocity-obstacle methods such as ORCA are conservative and assume perfect sensing. DRL policies struggle with a varying number of neighbors, the compute cost of raw sensor input, and rewards that do not encode reciprocal velocity constraints.

## Mechanism

RL-RVO trains a shared PPO actor-critic policy. Robots do not communicate with each other; each senses neighbors within 4 m (at most five neighbors). Dynamic agents are encoded as reciprocal velocity obstacle (RVO) vectors and static line obstacles as velocity obstacle (VO) vectors. A bidirectional GRU maps the variable-length sequence to a continuous velocity increment, which is converted to linear and angular velocity for nonholonomic control. The reward uses the RVO and VO area and the expected collision time instead of the distance to obstacles. Training uses OpenAI Gym in the circle scenario only (2 to 4, then 10 disc robots) and takes about 10 h on an Intel i7-9700 with a GTX 1080.

## Baselines and controls

SARL, GA3C-CADRL, and NH-ORCA in simulation; NH-ORCA only on hardware. Ablations remove the RVO input, replace the BiGRU by an LSTM, or use a distance-based reward.

## Platform and setup

- Simulation: Gym circle (9 x 9 m) and random (10 x 10 m) scenes with 6 to 20 robots, 100 episodes each, and a corridor ablation.
- Hardware: up to eight Turtlebots arranged on a circle with random headings. Each robot has a mini PC that computes the velocity and a UWB tag for localization; robots receive neighbor states through ROS. Maximum speed 1 m/s. Tests with 4, 6, and 8 robots, 50 trials, against NH-ORCA.

## Evidence type and transfer

The hardware results close the loop on real differential-drive robots, but localization comes from an external UWB system rather than onboard sensing, and all hardware tests use the circle crossing scenario. Simulation covers more scenes and team sizes up to 20 robots.

## Sensors

Neighbor positions and velocities, encoded as RVO and VO vectors. On hardware, UWB localization and ROS messages supply these states; the policy does not use onboard LiDAR.

## Compute and latency

A mini PC on each Turtlebot computes the velocity. Training took about 10 h on an Intel i7-9700 with a GTX 1080. Per-action compute is lower than for SARL and GA3C-CADRL; the exact values are not recorded in the legacy extraction.

## Key quantitative results

- Hardware success, 4/6/8 robots: RL-RVO 1.00/0.91/0.89 versus NH-ORCA 1.00/0.85/0.68 (no page; table values found only in paper.md).
- Simulation: as the number of robots grows, success rate and average speed fall and travel time rises; RL-RVO stays above the learned baselines in dense cases (p. 6).
- Training time: about 10 h on an Intel i7-9700 with a GTX 1080 (p. 6).

## Stated limitations

- Future work will address navigation problems with more challenging uncertainties in the real world (p. 8).
- GA3C-CADRL and SARL were not compared on hardware because of their high computational cost (p. 7).

## Transfer conditions

Legacy reviewer observations: the policy is trained only in a circle scenario, a global planner is still needed when a static obstacle blocks the goal, heterogeneous sensing is not tested, and the hardware uses external UWB localization rather than onboard LiDAR. A wheeled robot reusing the policy needs neighbor positions and velocities from its own sensing or from a shared localization system.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | direct-support | strong | Sec. VI-B, p. 7 | "Because of the high computational cost of GA3C-CARDL and SARL, we only compare our policy with NH-ORCA using 4, 6, and 8 Turtlebots in the real world experiment with circle scenario." |
| C4 | direct-support | strong | Sec. VI-B, p. 6 | "Generally, as the number of robots increases, the success rate and average speed decrease, whereas the travel time increases." |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI-B, p. 7 | "Each Turtlebot is equipped with a mini PC to compute velocity and a tag to localize itself by the UWB localization system." |

## Page-cited excerpts

- **p. 7, Real-world experiments.** "Because of the high computational cost of GA3C-CARDL and SARL, we only compare our policy with NH-ORCA using 4, 6, and 8 Turtlebots in the real world experiment with circle scenario."
  Learned baselines were too costly for the robots, so the hardware comparison is against NH-ORCA only.
- **p. 6, Results and discussions.** "Generally, as the number of robots increases, the success rate and average speed decrease, whereas the travel time increases."
  Team density degrades every method; the simulated agents are homogeneous discs.
- **p. 7, Real-world experiments.** "The RL-RVO policy is implemented in Turtlebot robots to demonstrate the performance of our policy in the real world."
  The policy closes the loop on real robots.
- **p. 7, Real-world experiments.** "Those experiments use up to 8 differential drive Turtlebots"
  Source of the drive type.
- **p. 7, Real-world experiments.** "Each Turtlebot is equipped with a mini PC to compute velocity and a tag to localize itself by the UWB localization system."
  Localization comes from an external UWB system.
- **p. 8, Conclusion.** "Our future work includes extending such an approach to addressing navigation problems with more challenging uncertainties in the real world."
  The authors' stated open problem.

## Survey-usable statements

### Supported

- An RVO-shaped DRL policy without inter-robot communication reached 0.89 success with eight real Turtlebots in a circle crossing versus 0.68 for NH-ORCA (numbers from a light review; re-check before citing).
- Learned multi-robot baselines can be too costly to run onboard small robots: GA3C-CADRL and SARL were dropped from the hardware comparison.

### Not supported

- RL-RVO was validated with onboard perception: hardware localization is external UWB.
- RL-RVO was validated in cluttered indoor missions on hardware: all hardware trials are circle crossings.
- RL-RVO beats every method on hardware at every team size: with 4 robots it ties NH-ORCA at 1.00 success.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Real robot, Claim summary, Hardware caveat) converted to the English template; the legacy C6 quote with an ellipsis was replaced by contiguous sentences (p. 7) and the C6 row now uses the UWB sentence; the hardware success table has no located page; global-planner and circle-only training notes moved to Transfer conditions because they were not located
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

The challenges to solving the collision avoidance problem lie in adaptively choosing optimal robot velocities in complex scenarios full of interactive obstacles. In this letter, we propose a distributed approach for multi-robot navigation which combines the concept of reciprocal velocity obstacle (RVO) and the scheme of deep reinforcement learning (DRL) to solve the reciprocal collision avoidance problem under limited information. The novelty of this work is threefold: (1) using a set of sequential VO and RVO vectors to represent the interactive environmental states of static and dynamic obstacles, respectively; (2) developing a bidirectional recurrent module based neural network, which maps the states of a varying number ofsurrounding obstacles to the actions directly; (3) developing a RVO area and expected collision time based reward function to encourage reciprocal collision avoidance behaviors and trade off between collision risk and travel time. The proposed policy is trained through simulated scenarios and updated by the actor-critic based DRL algorithm. We validate the policy in complex environments with various numbers of differential drive robots and obstacles. The experiment results demonstrate that our approach outperforms the state-of-art methods and other learning based approaches in terms of the success rate, travel time, and average speed.
