# Communication-Robust Asynchronous Distributed LiDAR Collaborative Smoothing and Mapping

## Metadata

| Field | Value |
|---|---|
| ID | R20 |
| Title | Communication-Robust Asynchronous Distributed LiDAR Collaborative Smoothing and Mapping |
| Authors | Jiancheng Wang, Chenyuan Cai, JinQian Tan, and Haoyao Chen |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3655282](https://doi.org/10.1109/lra.2026.3655282) |
| Official URL | https://ieeexplore.ieee.org/document/11358654/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Multi-Proxy-R20/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Multi-Proxy-R20/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Multi-Proxy-R20/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: dataset-playback
- evidence_all: dataset-playback, simulation
- protocol_caveats: none
- platform_class: mixed
- platform: Public S3E and SubT-MRS multi-robot datasets and a multi-robot simulation (p. 6).
- boundary_platform: yes
- degradation: communication-delay-loss, bandwidth-limit, lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: 3D LiDAR with plug-and-play local SLAM front ends
- compute: ROS integration; processor not inspected in this reading.
- compute_location: desktop-offline
- summary_result: Lightweight descriptors and asynchronous ADMM pose-graph optimization keep collaborative LiDAR SLAM accurate under simulated packet loss and latency while cutting bandwidth by over 80% (p. 1).
- summary_limitation: Relies on reasonably stable front-end odometry in highly degenerate environments (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Collaborative LiDAR SLAM back ends assume high-bandwidth, low-latency links.

## Mechanism

STD-based lightweight descriptors feed a progressive inter-robot loop detection with PCM outlier rejection; an asynchronous distributed pose-graph optimizer based on ADMM proceeds without waiting for synchronous estimates; optimization runs in local frames (pp. 3-5).

## Baselines and controls

CoLRIO, DCL and DiSCo-SLAM (p. 6).

## Platform and setup

Dataset accuracy tests, bandwidth measurements and simulated adverse communication (pp. 6-7). Public S3E and SubT-MRS multi-robot datasets and a multi-robot simulation (p. 6).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. Dataset replay and simulated packet loss; no moving-team deployment was inspected.

## Sensors

3D LiDAR with plug-and-play local SLAM front ends.

## Compute and latency

ROS integration; processor not inspected in this reading.

## Key quantitative results

- Under high packet loss and latency, the two-stage distributed Gauss-Seidel solver of DCL fails to converge (p. 7).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The method relies on a reasonably stable front-end odometry in highly degenerate environments (p. 8).

## Transfer conditions

Loss and latency are simulated; consistency after long partitions is not tested.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity; no other version is in the library.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 7, Sec. IV-D.** "High packet-loss and latency disrupts the two-stage distributed Gauss-Seidel solver, causing DCL to fail to converge."
  Baseline failure under modeled communication faults.
- **p. 8, Sec. V.** "During evaluation in highly degenerate environments, our method relies on a reasonably stable front-end odometry, such that individual robots do not suffer from severe degeneracy-induced drift."
  Author-stated dependence.

## Survey-usable statements

### Supported

- Asynchronous distributed optimization tolerates modeled packet loss and latency in collaborative LiDAR SLAM.

### Not supported

- Robustness to front-end degeneracy is not established.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

In large-scale, complex, and communication-constrained environments, efficient multi-robot cooperation places stringent demands on Simultaneous Localization and Mapping (SLAM) systems. Existing Collaborative LiDAR SLAM (C-LSLAM) approaches achieve high localization accuracy but rely on high-bandwidth, low-latency communication, limiting real-time performance, reliability, and scalability. We present Multi-Proxy, an asynchronous, distributed, and decentralized C-LSLAM framework using a progressive loop closure detection strategy. The lightweight descriptor reduces inter-robot communication while maintaining rich collaborative constraints across large variations in viewpoint. Unlike conventional synchronous distributed optimization, Multi-Proxy's back-end employs an asynchronous Alternating Direction Method of Multipliers (ADMM), enabling efficient Asynchronous Distributed Pose Graph Optimization (ADPGO) without waiting for synchronous estimates, ensuring robust real-time performance under communication packet loss or latency. Designed as a collaborative localization plugin, Multi-Proxy integrates seamlessly with existing C-LSLAM systems, enhancing flexibility and scalability. Experiments show that Multi-Proxy outperforms State-Of-The-Art (SOTA) C-LSLAM methods in Absolute Trajectory Error (ATE), Mean Map Entropy (MME), Average Wasserstein Distance (AWD), and Chamfer Distance (CD), while reducing communication bandwidth by over 80%.
