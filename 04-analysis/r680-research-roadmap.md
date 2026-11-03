# R680 research roadmap

Historical organization date: October 25, 2026. This page combines the original direction priorities and expansion evidence to organize reading and experiments; it is not a demonstrated novelty claim. The detailed historical basis is in the [six-theme evidence synthesis](evidence-synthesis.md). For the current library of 127 works, with 23 full and 104 light cards, and the completed targeted follow-up, see the [integrated evidence analysis](integrated-evidence.md). The priority table below preserves the historical roadmap rather than claiming a new experimental ranking.

## Priority order

| Order | Direction | Read first | Question to test |
|---|---|---|---|
| 1 | Degraded localization and integrity-driven navigation recovery | [M39 slip-aware-fusion](../03-reviews/T1-perception-localization/2022-slip-aware-fusion-M39/review.md), [E10 PL-VIWO](../03-reviews/T1-perception-localization/2025-PL-VIWO-E10/review.md), [X07 EKF-SLAM-integrity](../03-reviews/T1-perception-localization/2025-EKF-SLAM-integrity-X07/review.md), [E51 KSFD](../03-reviews/T6-reliability-deployment/2025-KSFD-E51/review.md), [E59 GP-Navigation-Recovery](../03-reviews/T6-reliability-deployment/2024-GP-Navigation-Recovery-E59/review.md) | Log degradation measures, triggered actions, missed alarms/false stops, and navigation-task outcomes in the same chain. |
| 2 | Language/semantic navigation under compute constraints | [E47 VLFM](../03-reviews/T5-semantic-embodied-navigation/2024-VLFM-E47/review.md), [E44 OpenIN](../03-reviews/T5-semantic-embodied-navigation/2025-OpenIN-E44/review.md), [E50 LeLaN](../03-reviews/T5-semantic-embodied-navigation/2025-LeLaN-E50/review.md) | Decide which choices invoke a model and which fall back to geometry; measure onboard latency and fallback behavior. |
| 3 | Traversability, pose uncertainty, and safe planning | [M14 LRAE](../03-reviews/T2-slam-mapping-exploration/2024-LRAE-M14/review.md), [E13 FIT-SLAM2](../03-reviews/T2-slam-mapping-exploration/2025-FIT-SLAM2-E13/review.md), [E26 LiDAR-CBF](../03-reviews/T3-planning-control/2024-LiDAR-CBF-E26/review.md) | Hold the map, speed, and sensing conditions fixed, and jointly measure costs, actions, and task success. |
| 4 | Collaborative exploration and reunion under intermittent communication | [E31 SlideSLAM](../03-reviews/T4-multi-robot-coordination/2025-SlideSLAM-E31/review.md), [E36 Commerge](../03-reviews/T4-multi-robot-coordination/2026-Commerge-E36/review.md), [E40 iMESA](../03-reviews/T4-multi-robot-coordination/2024-iMESA-E40/review.md) | Record disconnection times, message types, consistency after recovery, and task impact; multiple vehicles are required. |

## Implementing the first direction

1. **Collect the baseline:** follow the [R680 baseline collection guide](r680-baseline.md), recording vision/chassis and LiDAR in separate sessions; check TF, timestamps, extrinsics, rates, and dropped frames.
2. **Reproduce offline:** fix the route, speed, map, and fault timing; inject controlled occlusion, message loss, wheel-speed bias, or map changes during rosbag playback.
3. **Establish controls:** compare no risk gate, alarm only, and alarm with recovery; then ablate detection, weight updates, isolation, and recovery.
4. **Evaluate jointly:** record ATE/RPE, missed alarms/false stops, detection lead time, recovery time, task success, takeover count, and computational overhead together.
5. **Validate on hardware:** after offline and simulation checks pass, conduct controlled low-speed tests and preserve the raw logs. This organization work did not start experiments.

## Limits on the conclusions

- Concrete related work already exists for degradation adaptation, fault detection, safe control, and recovery; do not describe these topics as unstudied.
- Switching to ROS 2/Nav2 or a WHEELTEC platform is not itself a contribution. First state the differences in trigger quantity, action, controls, and joint metrics.
- Results using 3D LiDAR, radar, UWB, desktop/remote GPUs, or another chassis are not results for the R680's 2D LiDAR and onboard compute.
- The C1 six-class grouping remains a reading framework. Before formal project approval, read the works closest to the target chain among the [79 historical follow-up candidates](../06-data/followup-candidates.csv); the current integrated analysis records the completed fixed follow-up separately.

The original direction priorities, gap report, and status notes are compressed in the archive for traceability. This page and the six-theme synthesis preserve the historical research entry points; use the current integrated analysis for the updated corpus scope and joint-evaluation questions.
