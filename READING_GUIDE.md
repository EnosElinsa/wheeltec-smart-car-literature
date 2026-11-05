# Key-paper reading guide

This guide gives a reading order for 18 key papers, three per theme. For each paper it states why to read it, the evidence the paper actually reports, and the conditions that limit transfer to the R680. It is a reading order, not a ranking of paper quality.

The 18 papers were selected on October 25, 2026 from the 112-paper corpus of that date, for R680 relevance, representative mechanisms and experimental boundaries. All 18 have full-verification cards. The selection has stayed the same while the library grew to 247 papers through the follow-up selection F01-F15 ([shortlist](06-data/followup-shortlist.md)) and the batches N01-N20, S01-S48, R01-R36 and K01-K16 (see the [changelog](CHANGELOG.md)). The library now has 23 full and 224 light cards. A light card records only the passages that were read, so its numbers must be checked against the PDF before use.

The [review index](03-reviews/INDEX.md) lists every card, and the [paper index](01-papers/INDEX.md) and [full-text index](02-fulltext/INDEX.md) give citations and local file paths. The current cross-paper synthesis is the [survey manuscript](05-survey/manuscript/README.md). Earlier syntheses, including the [six-theme evidence synthesis](04-analysis/evidence-synthesis.md) and the [R680 research roadmap](04-analysis/r680-research-roadmap.md), are listed in the [analysis records](04-analysis/README.md). A robot or computer reported in a paper is not evidence of deployment on the R680.

## T1-perception-localization

| Paper | Why read it | Actual evidence and transfer boundary |
|---|---|---|
| [M39 · slip-aware-fusion](03-reviews/T1-perception-localization/2022-slip-aware-fusion-M39/review.md) | Slip-aware fusion connecting wheel speed and IMU measurements | Clearpath Jackal hardware; a 20 ms estimator period is reported, but processor and compute location are not. Check chassis and sensor assumptions. |
| [E10 · PL-VIWO](03-reviews/T1-perception-localization/2025-PL-VIWO-E10/review.md) | Point-line visual-inertial-wheel fusion | KAIST car-dataset playback on an Intel i7 system with an A1000 GPU; GPU use is unspecified. Check synchronization, extrinsics, and the wheel model. |
| [X07 · EKF-SLAM-integrity](03-reviews/T1-perception-localization/2025-EKF-SLAM-integrity-X07/review.md) | Localization integrity monitoring and fault isolation | Simulation and one vehicle-mounted LiDAR/IMU run; processor and runtime are unreported. Covariance envelopes do not substitute for integrity-risk bounds. |

## T2-slam-mapping-exploration

| Paper | Why read it | Actual evidence and transfer boundary |
|---|---|---|
| [E13 · FIT-SLAM2](03-reviews/T2-slam-mapping-exploration/2025-FIT-SLAM2-E13/review.md) | Traversability and information gain for exploration | Gazebo and one outdoor rover run; Intel i5-13420H experiments, with field compute placement unspecified. Stereo/3D traversability sensing differs from an M10P 2D LiDAR. |
| [E15 · DynoSAM](03-reviews/T2-slam-mapping-exploration/2026-DynoSAM-E15/review.md) | Smoothing and mapping for dynamic SLAM | Dataset playback; computer unspecified and the full-batch back end is unsuitable for online use. Estimation results do not establish closed-loop navigation. |
| [E19 · NGD-SLAM](03-reviews/T2-slam-mapping-exploration/2025-NGD-SLAM-E19/review.md) | Dynamic SLAM without GPU use | TUM/BONN playback on a Ryzen 7 4800H laptop; its RTX 2060 is unused by NGD-SLAM. Reported tracking time excludes concurrent detection; no robot navigation loop is tested. |

## T3-planning-control

| Paper | Why read it | Actual evidence and transfer boundary |
|---|---|---|
| [E22 · CECBF](03-reviews/T3-planning-control/2025-CECBF-E22/review.md) | Stagnation and circulation in CBF-based safe navigation | TurtleBot3 Burger robots with Vicon positions; remote Intel i7 control over Wi-Fi. Retain the model, sensing, and timing assumptions behind the safety constraints. |
| [E25 · Scenario-Safe-Planning](03-reviews/T3-planning-control/2025-Scenario-Safe-Planning-E25/review.md) | Motion planning with collision-probability constraints | Simulation, CARLA, and Jackal hardware with motion capture; simulation uses an Intel i9, while hardware compute is unspecified. Distinguish probability bounds from observed collision statistics. |
| [E26 · LiDAR-CBF](03-reviews/T3-planning-control/2024-LiDAR-CBF-E26/review.md) | Online safety constraints constructed from LiDAR | Three TurtleBot3 Burger robots with Vicon positions; remote Intel i7 control over Wi-Fi. Check field of view, obstacle representation, model, and end-to-end delay. |

## T4-multi-robot-coordination

| Paper | Why read it | Actual evidence and transfer boundary |
|---|---|---|
| [E31 · SlideSLAM](03-reviews/T4-multi-robot-coordination/2025-SlideSLAM-E31/review.md) | Sparse semantic SLAM and autonomous wheeled exploration | Scarab UGVs and Falcon UAVs with onboard i7 CPUs; replay timings use an i7 laptop. Intermittent-communication tests include replay; message size is not throughput. |
| [E36 · Commerge](03-reviews/T4-multi-robot-coordination/2026-Commerge-E36/review.md) | Efficient map merging under resource constraints | Recorded public/in-house data, including real WLAN tests; central-server tiers are desktop i7, mini-PC i5, and Jetson Nano. Server benchmarks do not establish onboard end-to-end autonomy. |
| [E40 · iMESA](03-reviews/T4-multi-robot-coordination/2024-iMESA-E40/review.md) | Distributed incremental collaborative optimization | Synthetic graphs and Nebula graph replay with simulated communication; hardware is unspecified. Convergence is not guaranteed, and outlier loop closures were removed from the real-data graphs. |

## T5-semantic-embodied-navigation

| Paper | Why read it | Actual evidence and transfer boundary |
|---|---|---|
| [E50 · LeLaN](03-reviews/T5-semantic-embodied-navigation/2025-LeLaN-E50/review.md) | Language-conditioned final approach with onboard Orin AGX evidence | Roomba-based robot with a fisheye camera and Orin AGX; training uses an RTX 4090 workstation. The main task has a visible target; obstacle avoidance remains limited. |
| [E47 · VLFM](03-reviews/T5-semantic-embodied-navigation/2024-VLFM-E47/review.md) | Semantic frontier exploration and language/geometry layering | Habitat benchmarks and qualitative Spot demonstrations; real-world models use an RTX 4090 MaxQ laptop with unspecified placement. The low-level PointNav policy requires training. |
| [E44 · OpenIN](03-reviews/T5-semantic-embodied-navigation/2025-OpenIN-E44/review.md) | Updating instance memory for moved household objects | Habitat and an Autolabor robot with Mid-360, Azure Kinect, and ROS move_base; compute placement and GPT-4o latency are unreported. An initial graph is required; evaluate whole-sequence success separately. |

## T6-reliability-deployment

| Paper | Why read it | Actual evidence and transfer boundary |
|---|---|---|
| [E51 · KSFD](03-reviews/T6-reliability-deployment/2025-KSFD-E51/review.md) | Fault diagnosis from kinematic consistency | Numerical tests and Ackermann-rover/quadrotor logs with faults injected afterward; processor and detection delay are unreported. This is not closed-loop takeover after a physical fault. |
| [E59 · GP-Navigation-Recovery](03-reviews/T6-reliability-deployment/2024-GP-Navigation-Recovery-E59/review.md) | Robust planning and recovery in unknown environments | Gazebo Jackal tests and Jackal/Spot hardware case studies; processor and compute placement are unreported. Check the failure definition, recovery trigger, and platform conditions. |
| [E60 · FORTRESS](03-reviews/T6-reliability-deployment/2025-FORTRESS-E60/review.md) | Monitoring and fallback planning under dynamic constraints | ANYmal monitoring data and closed-loop quadrotor fallback; deployment timing names Jetson Nano, but hosted-model access is unspecified. This does not establish wheeled fallback performance. |

## Two reading routes

- **Degraded localization and recovery**: M39 → E10 → X07 → E51 → E26 → E59. Establish data collection and evaluation before choosing an algorithm.
- **Semantic navigation**: E47 → E44 → E50. Compare exploration, memory updates, and final approach as different tasks; their success rates are not directly interchangeable.

The [79 historical follow-up rows](06-data/followup-candidates.csv) remain the original screening queue, including duplicates and corpus overlaps. Title and abstract screening alone establishes neither acquisition nor full-text verification. The [follow-up assessment](06-data/followup-assessment.md) separates evidence that narrows a question from evidence that leaves it open. The six themes organize reading, and a gap in this library does not establish a gap in the research field.
