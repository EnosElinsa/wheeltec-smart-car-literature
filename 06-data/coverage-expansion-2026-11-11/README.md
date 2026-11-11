# Mobile robotics conference papers: coverage expansion

24 additional papers from ICRA 2025 (15) and IROS 2025 (9) broaden coverage across six mobile-robot themes, with four papers per theme. Every paper has a verified official IEEE PDF, native publisher BibTeX and OXR-1.0 transcription. Selection was deduplicated against all 626 existing catalog identities by DOI, official URL and title. Original publisher bytes are preserved.

The catalog contains 650 records and 479 active transcribed reading sets. The 247 assessments and 245 survey selections are unchanged. These papers are registered reading sources; acquisition and transcription do not establish a full-paper scientific assessment.

## Localization and calibration

| Paper | Authors | Venue / year | Main method or contribution |
|---|---|---|---|
| [Universal Online Temporal Calibration for Optimization-Based Visual-Inertial Navigation Systems](https://ieeexplore.ieee.org/document/11127433/) | Yunfei Fan et al. | ICRA 2025 | Online time-offset estimation aligns camera and IMU states within optimization-based navigation; addresses sensor synchronization for mobile robots. |
| [AF-RLIO: Adaptive Fusion of Radar-LiDAR-Inertial Information for Robust Odometry in Challenging Environments](https://ieeexplore.ieee.org/document/11128046/) | Chenglong Qian et al. | ICRA 2025 | Adaptive radar, LiDAR, IMU and GPS fusion targets smoke, tunnels and degraded geometry; directly supports resilient ground-robot odometry. |
| [GLIC-Calib: Targetless and One-Shot Spatial-Temporal Calibration of LiDAR-IMU-Camera for Ground Vehicles](https://ieeexplore.ieee.org/document/11247264/) | Hang Zhao et al. | IROS 2025 | Ground-constrained one-shot extrinsic and temporal calibration covers the LiDAR-IMU-camera configuration used by ground vehicles. |
| [Cal or No Cal? - Real-Time Miscalibration Detection of LiDAR and Camera Sensors](https://ieeexplore.ieee.org/document/11246797/) | Ilir Tahiraj et al. | IROS 2025 | Contrastive calibrated-versus-miscalibrated classification monitors LiDAR-camera alignment with explicit runtime and resource evaluation. |

## SLAM and exploration

| Paper | Authors | Venue / year | Main method or contribution |
|---|---|---|---|
| [Hier-SLAM: Scaling-Up Semantics in SLAM with a Hierarchically Categorical Gaussian Splatting](https://ieeexplore.ieee.org/document/11127775/) | Boying Li et al. | ICRA 2025 | Hierarchical categorical 3D Gaussian semantic SLAM addresses storage, tracking and class scalability for mobile scene mapping. |
| [DVM-SLAM: Decentralized Visual Monocular Simultaneous Localization and Mapping for Multi-Agent Systems](https://ieeexplore.ieee.org/document/11127510/) | Joshua Bird et al. | ICRA 2025 | Decentralized monocular cooperative SLAM shares low-cost visual information for robot localization and mapping; includes real robot evaluation. |
| [KISS-SLAM: A Simple, Robust, and Accurate 3D LiDAR SLAM System With Enhanced Generalization Capabilities](https://ieeexplore.ieee.org/document/11246613/) | Tiziano Guadagnino et al. | IROS 2025 | LiDAR-only graph SLAM combines local scan maps, loop matching and pose graph correction with limited tuning across environments. |
| [TaskExp: Enhancing Generalization of Multi-Robot Exploration with Multi-Task Pre-Training](https://ieeexplore.ieee.org/document/11128456/) | Shaohao Zhu et al. | ICRA 2025 | Multi-task pretraining improves MARL exploration and zero-shot transfer to unknown large-scale maps; covers learned exploration generalization. |

## Planning and control

| Paper | Authors | Venue / year | Main method or contribution |
|---|---|---|---|
| [Certificated Actor-Critic: Hierarchical Reinforcement Learning with Control Barrier Functions for Safe Navigation](https://ieeexplore.ieee.org/document/11127225/) | Junjun Xie et al. | ICRA 2025 | Hierarchical actor-critic reinforcement learning uses control-barrier-derived rewards and theoretical analysis for safe robot navigation. |
| [QuasiNav: Asymmetric Cost-Aware Navigation Planning with Constrained Quasimetric Reinforcement Learning](https://ieeexplore.ieee.org/document/11127346/) | Jumman Hossain et al. | ICRA 2025 | Constrained quasimetric RL represents asymmetric terrain and energy costs, with Clearpath Jackal experiments for outdoor ground navigation. |
| [Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-World Environments](https://ieeexplore.ieee.org/document/11128008/) | Marc Heim et al. | ICRA 2025 | An optimization wrapper converts arbitrary planner sketches into dynamically feasible safe driving trajectories; covers planner deployment on real cars. |
| [Merry-Go-Round: Safe Control of Decentralized Multi-Robot Systems with Deadlock Prevention](https://ieeexplore.ieee.org/document/11245826/) | Wonjong Lee et al. | IROS 2025 | Decentralized collision avoidance uses temporary roundabouts to prevent deadlock, with physical robot experiments in congested navigation. |

## Multi-robot coordination

| Paper | Authors | Venue / year | Main method or contribution |
|---|---|---|---|
| [Maintaining Strong $r$-Robustness in Reconfigurable Multi-Robot Networks Using Control Barrier Functions](https://ieeexplore.ieee.org/document/11127420/) | Haejoon Lee et al. | ICRA 2025 | A control barrier function preserves robust inter-robot communication graphs during motion without imposing a fixed topology. |
| [Efficient Coordination and Synchronization of Multi-Robot Systems Under Recurring Linear Temporal Logic](https://ieeexplore.ieee.org/document/11127554/) | Davide Peron et al. | ICRA 2025 | Offline temporal-logic plans and online synchronization coordinate recurring tasks with ROS2 and nine-robot hardware evaluation. |
| [Realm: Real-Time Line-of-Sight Maintenance in Multi-Robot Navigation with Unknown Obstacles](https://ieeexplore.ieee.org/document/11128211/) | Ruofei Bai et al. | ICRA 2025 | LiDAR-derived line-of-sight constraints and algebraic graph connectivity support distributed exploration with limited inter-robot communication. |
| [Distributed Invariant Kalman Filter for Object-Level Multi-Robot Pose SLAM](https://ieeexplore.ieee.org/document/11128538/) | Haoying Li et al. | ICRA 2025 | Object-level distributed invariant Kalman filtering with covariance intersection addresses unknown cross-robot correlations and communication burden. |

## Semantic and language navigation

| Paper | Authors | Venue / year | Main method or contribution |
|---|---|---|---|
| [Language-Conditioned Offline RL for Multi-Robot Navigation](https://ieeexplore.ieee.org/document/11127288/) | Steven Morad et al. | ICRA 2025 | Language-conditioned offline RL learns direct multi-robot navigation policies from short real-world recordings and tests unseen instructions on five robots. |
| [Improving Zero-Shot ObjectNav with Generative Communication](https://ieeexplore.ieee.org/document/11127870/) | Vishnu Sashank Dorbala et al. | ICRA 2025 | Vision-language communication between overhead and ground agents studies assisted zero-shot object navigation and hallucination-related failures. |
| [Language as Cost: Proactive Hazard Mapping using VLM for Robot Navigation](https://ieeexplore.ieee.org/document/11246665/) | Mintaek Oh et al. | IROS 2025 | VLM scene reasoning predicts hazards and augments geometric navigation costs, addressing proactive risk-aware mobile navigation. |
| [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](https://ieeexplore.ieee.org/document/11246684/) | Dujun Nie et al. | IROS 2025 | A VLM world model, curiosity memory and staged action proposals support zero-shot object-goal navigation in unseen environments. |

## Deployment and evaluation

| Paper | Authors | Venue / year | Main method or contribution |
|---|---|---|---|
| [Arena 4.0: a Comprehensive Ros2 Development and Benchmarking Platform for Human-Centric Navigation Using Generative-Model-Based Environment Generation](https://ieeexplore.ieee.org/document/11127635/) | Volodymyr Shcherbyna et al. | ICRA 2025 | ROS2 navigation benchmarking combines generative scenario creation and annotated assets for human-centric navigation development. |
| [Task-driven SLAM Benchmarking for Robot Navigation](https://ieeexplore.ieee.org/document/11246415/) | Yanwei Du et al. | IROS 2025 | Task-driven SLAM evaluation measures repeatability and map utility during actual robot navigation rather than trajectory accuracy alone. |
| [Towards Robust Sensor-Fusion Ground SLAM: A Comprehensive Benchmark and A Resilient Framework](https://ieeexplore.ieee.org/document/11247507/) | Deteng Zhang et al. | IROS 2025 | M3DGR degradation benchmarks and modular GNSS/RGB-D/LiDAR/IMU/wheel fusion explicitly cover wheel slip, GNSS loss and sensor degradation. |
| [Experimental Evaluation of Radio-aware Semantic Map with 5G-Enabled Mobile Robots](https://ieeexplore.ieee.org/document/11246785/) | Adrian Lendinez et al. | IROS 2025 | 5G radio-aware semantic mapping links measured network quality with navigation and edge-offloading decisions on mobile robots. |

## Implementations and reading scope

The [code evidence](code-evidence.json) records pinned public repositories used for project descriptions in [textbook Chapter 54](https://enoselinsa.github.io/wheeltec-ros-textbook/08-advanced-applications/54-open-source-projects/). Source availability, dependencies and author/paper identity were checked without running training or hardware experiments. The AF-RLIO repository advertised in its abstract could not be resolved during this check; its verified paper is retained, without a claim that its implementation is available. Code availability was useful for this batch but was not a mandatory admission criterion.

## Journal policy and limits

New journal acquisition still requires documented JCR Q1 evidence specifying edition, subject category, journal identity and source. Public ranking pages encountered login/access restrictions or mixed JCR with SJR/CiteScore; these did not meet the evidence requirement. T-RO, IJRR and Science Robotics nominations remain unselected pending that evidence. No new RA-L, Autonomous Robots or Journal of Field Robotics paper was acquired. Conference admission is separate from journal quartiles. This targeted batch does not establish exhaustive coverage of any venue or year.

All 176 physical PDF pages and 196 extracted images are retained locally with per-page JSON and extraction receipts. See the [manifest](manifest.json) for source hashes and [verification](verification.json) for checks. PDFs, full texts, raw source evidence, private acquisition ledgers and rollback backups remain outside the public Git tree. OCR can contain formula, table and numeric errors; check the PDF when using exact results.
