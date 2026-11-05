# R680 baseline data collection: platform gate

> **Stage record, October 25, 2026.** Its counts and statuses describe that date and are not updated. Current totals are in the [repository README](../README.md).

Historical organization date: October 25, 2026. This page preserves the original data-collection gate. The historical record described full-text review of the selected papers, with relevant follow-up candidates still to be read before project approval; that wording does not imply uniform full verification. The [integrated evidence analysis](integrated-evidence.md) records the later 147-work stage, with 23 full and 124 light cards. Physical data collection has not started.

The operational instructions are in the robot package: `../../wheeltec-ros-source-reference/ros2/navigation/vision-nav/wheeltec_vision_nav/BASELINE.md` (`../../wheeltec-ros-source-reference/ros2/navigation/vision-nav/wheeltec_vision_nav/BASELINE.md`, local only).

## What to record

| Session | Purpose | Do not run concurrently |
|---|---|---|
| V `vision_base` | RGB-D, visual `/odom`, TF, `/imu/data_raw`, `/wheel/odom` | Factory LiDAR mapping/navigation |
| L `lidar` | M10P `/scan` (approximately 12 Hz, `frame_id=laser`) | Application A visual mapping/navigation |

Both bags must pass `check_baseline` before proceeding to nondestructive fault injection and Nav2 recovery (original direction priorities 1 + 2). C1 remains unresolved. The original frozen nearest-work run has been archived with its hashes and records preserved.

## After passing the gate

Copy the bag directories, including `metadata.yaml`, to a data drive outside this repository. Do not commit large bags to Git.
