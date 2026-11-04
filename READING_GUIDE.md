# Key-paper reading guide

Find local source paths in the [source Markdown index](02-fulltext/INDEX.md) and [PDF and citation index](01-papers/INDEX.md); read the English cards through the [review index](03-reviews/INDEX.md).

Historical selection date: October 25, 2026. These **18 key papers** were selected from the original 112-paper corpus for R680 relevance, representative mechanisms, and experimental boundaries. This is a reading order, not a paper-quality ranking. The November 2 maintenance preserves that selection; all 18 now have full-verification English cards. The original corpus has 23 full-verification cards and 89 light conversions. New targeted light reviews read selected method, setup, evaluation, and limitation passages rather than converting a legacy extraction. A light card's numerical claims must be checked against the PDF before use in the survey.

The [confirmed follow-up selection](06-data/followup-shortlist.md) preserves F01–F15 as a reading route around four integration questions. N01–N20 add motion-prior, recovery, shared-state and evaluation comparisons in the same theme directories. The current library has **231 review cards: 23 full and 208 light**, including 89 historical conversions and 119 targeted readings. S01-S48 are integrated in the [48-paper analysis](04-analysis/survey-expansion-integration-2026-11-03.md), and R01-R36 in the [IEEE refresh analysis](04-analysis/ieee-refresh-integration-2026-11-03.md). Targeted cards retain selected-page scope. Use the [earlier integrated analysis](04-analysis/integrated-evidence.md), [IEEE evidence analysis](04-analysis/ieee-evidence-utilization-2026-11-03.md) and [selection record](06-data/survey-inclusion.json) for the current scope. These additions do not replace the historical 18-paper reading order. The manuscript selects 229 works, all from 2021-2026, while preserving all 231 cards; X01/X15 remain internal references.

Start with the [six-theme evidence synthesis](04-analysis/evidence-synthesis.md), then read the individual cards and PDFs. The synthesis and [R680 research plan](04-analysis/r680-research-roadmap.md) are in English. A paper's published robot or computer is not evidence of deployment on the R680.

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

The [79 historical follow-up rows](06-data/followup-candidates.csv) remain the original screening queue, including duplicates and corpus overlaps. Title/abstract screening alone establishes neither acquisition nor full-text verification. Follow-up assessment distinguishes evidence that narrows a question from evidence that leaves it open; all 15 selected source PDFs are now registered. Six themes organize reading; a gap in this library does not establish a gap in the research field.
