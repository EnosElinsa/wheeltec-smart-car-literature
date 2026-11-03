# Mobile Robot Collision Avoidance Based on Deep Reinforcement Learning With Motion Constraints

## Metadata

| Field | Value |
|---|---|
| ID | M06 |
| Title | Mobile Robot Collision Avoidance Based on Deep Reinforcement Learning With Motion Constraints |
| Authors | Yuting Tao, Mingyang Li, Xiao Cao, and Peng Lu |
| Venue | IEEE Transactions on Intelligent Vehicles, vol. 10, no. 3, pp. 2163-2173 |
| Year | 2025 (online 2024) |
| Type | journal |
| DOI | [10.1109/tiv.2024.3444854](https://doi.org/10.1109/tiv.2024.3444854) |
| Official URL | https://ieeexplore.ieee.org/document/10638222/ |
| Theme folder | T3-planning-control |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T3-planning-control/2025-DRL-collision-avoid-M06/paper.pdf` and `02-fulltext/T3-planning-control/2025-DRL-collision-avoid-M06/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-DRL-collision-avoid-M06/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware, scripted-scenario, speed-capped
- platform_class: differential-drive
- platform: TurtleBot2 with Kobuki base, NUC12, and D435i (text, p. 9); Unity ML-Agents training and Gazebo validation
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: onboard RealSense D435i depth for the policy; IMU and wheel odometry fused by robot_pose_ekf for pose
- compute: training on i7-10875H and RTX 2060; onboard NUC12 on the robot; timing not recorded in the legacy extraction
- compute_location: onboard
- summary_result: The depth-only PPO-LSTM policy is compared with DWA, TEB, and DRL_VO on 50 BARN maps in Gazebo at 0.5 and 1.0 m/s; the legacy card records no values.
- summary_limitation: The authors identify localization accuracy and rapid perception of moving objects as limitations after the real-world trials.
- survey_included: yes
- verification_level: light

## Problem

Mapless collision avoidance for differential-drive robots in dense, unstructured, and pedestrian scenes, without classical global planners or multi-sensor fusion in the policy.

## Mechanism

End-to-end PPO with an LSTM. The observation is a 1-D depth vector, heading, goal, and the previous action. The reward encodes differential-drive motion constraints by preferring high linear speed and low angular speed. Training follows a curriculum in Unity ML-Agents (empty, sparse, dense).

## Baselines and controls

- DWA.
- TEB.
- DRL_VO.

## Platform and setup

Training in Unity on an i7-10875H with an RTX 2060. Zero-shot Gazebo tests on 50 BARN_Dataset maps at maximum speeds of 0.5 and 1.0 m/s (p. 7). Real tests on a TurtleBot2 (Kobuki, NUC12, D435i) with structured, unstructured, and random obstacles and moving pedestrians; mapless localization fuses IMU and odometry with robot_pose_ekf (p. 9). In the hardest trial, pedestrians were required to move no faster than the robot's 0.5 m/s limit (p. 10).

## Evidence type and transfer

The tabulated comparison is a Gazebo simulation; the real-robot runs are closed-loop demonstrations shown as trajectories. The legacy card notes that the policy uses depth only and was not stress-tested against pedestrians faster than 0.5 m/s or against poor odometry.

## Sensors

Onboard Intel RealSense D435i depth for the policy; IMU and wheel odometry fused by an EKF for pose.

## Compute and latency

Training: Intel i7-10875H and NVIDIA RTX 2060 (p. 7). The robot carries a NUC12 onboard computer (p. 9). Decision-making times are not recorded in the legacy extraction.

## Key quantitative results

The legacy extraction records no result values for the BARN comparison or the real-robot trials; not verified.

## Stated limitations

- Localization accuracy and rapid perception of moving objects are identified as limitations (p. 10).
- Pedestrian speed was constrained to no more than the robot's maximum speed of 0.5 m/s (p. 10).

## Transfer conditions

Legacy reviewer observations: the stack is a TurtleBot2 with a D435i and IMU-odometry fusion, not a mapped LiDAR Nav2 platform. Faster pedestrians and poor odometry were not tested.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | V. Conclusion, p. 10 | "However, challenges such as localization accuracy and rapid perception of moving objects have been identified as limitations." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | V. Conclusion, p. 10 | "Extensive validations in Gazebo using the BARN_Dataset map set and real-world experiments have demonstrated the effectiveness of our proposed DRL framework for obstacle avoidance in map-less, unstructured, and complex environments." |

## Page-cited excerpts

- **p. 10, V. Conclusion.** "However, challenges such as localization accuracy and rapid perception of moving objects have been identified as limitations."
  The authors' own limitation after the real trials.
- **p. 10, V. Conclusion.** "Extensive validations in Gazebo using the BARN_Dataset map set and real-world experiments have demonstrated the effectiveness of our proposed DRL framework for obstacle avoidance in map-less, unstructured, and complex environments."
  The claimed scope; the real stack is a TurtleBot2 with depth and IMU-odometry fusion.
- **p. 9, Real-World Setup.** "Localization in mapless environments was achieved through the fusion of Imu and Odom sensors"
  Pose comes from dead reckoning, not a map.
- **p. 7, Algorithm Comparison.** "A subset of 50 maps was randomly chosen from the 300 available in the BARN"
  The simulated benchmark uses 50 of the 300 BARN maps.

## Survey-usable statements

### Supported

- A depth-only PPO-LSTM policy with a differential-drive motion-constraint reward runs mapless on a TurtleBot2 among static clutter and slow pedestrians.
- The authors name localization accuracy and fast perception of moving objects as remaining limitations.

### Not supported

- Robustness to fast pedestrians: pedestrians were limited to 0.5 m/s.
- Quantitative hardware performance: the legacy card records no hardware metrics.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-layout legacy card converted to the template; both legacy quotes found and kept; Year changed from 2025 to 2025 (online 2024) from the PDF first page
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Deep reinforcement learning (DRL), which integrates neural networks with reinforcement learning algorithms, plays a crucial role in enhancing autonomous robot collision avoidance and navigation in various environments, including industrial warehouses, hospitals, urban pedestrian zones, and airport terminals. However, existing research has encountered limitations, such as reliance on conventional algorithms, the need for multi-sensor data fusion, and application in overly simplified or non-random scenarios. To address these challenges, this paper presents a novel end-to-end method that implicitly integrates the mobile robot’s motion constraints to help the agent navigate and avoid obstacles in complex environments. By designing a novel observation space and a Long Short-Term Memory module, our DRL framework can output two continuous actions, which are linear and angular velocities for collision avoidance in dense environments, by only using the depth image from the onboard RGBD camera. To remove the assistance from conventional algorithms, we have designed a novel reward function that takes into account the motion constraints for differential drive robots, promoting higher linear velocity and lower angular velocity, thus for efficient and smooth obstacle avoidance, especially in sparse-obstacle environments. We have extensively validated the proposed framework against stateof-the-art methods using the BARN\_Dataset map set. Furthermore, various real-world scenarios, including structured, unstructured, and random environments, and moving pedestrians, have further demonstrated the effectiveness and robustness of our proposed framework.
