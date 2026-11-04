# Feedback-Guided Hierarchical Transmission for Multi-Robot Mapping Under Bandwidth Constraints

## Metadata

| Field | Value |
|---|---|
| ID | R21 |
| Title | Feedback-Guided Hierarchical Transmission for Multi-Robot Mapping Under Bandwidth Constraints |
| Authors | Guanchong Niu, Shuwake Nuerdaolieti, Jinglei Li, Zewei Jing, Lanxiang Hou, and Jiayi Sun |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3699241](https://doi.org/10.1109/lra.2026.3699241) |
| Official URL | https://ieeexplore.ieee.org/document/11543311/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Hierarchical-Transmission-R21/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Hierarchical-Transmission-R21/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Hierarchical-Transmission-R21/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: handheld
- platform: S3DIS and ScanNet indoor RGB-D datasets with bandwidth sweeps and packet-loss tests (p. 1).
- boundary_platform: yes
- degradation: bandwidth-limit, communication-delay-loss
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Indoor RGB-D scans
- compute: Allocation scales as O(K log(1/epsilon)) in active submaps (p. 5); processor not inspected.
- compute_location: desktop-offline
- summary_result: Layered pose, geometry and semantic transmission with backend feedback recovers map quality with fewer bytes and recovers loop closures earlier under packet loss (p. 8).
- summary_limitation: Round-wise feedback may become stale under higher-latency or asynchronous networks; real wireless links are future work (p. 5).
- survey_included: yes
- verification_level: light

## Problem

Centralized multi-robot mapping must decide which map content to send under scarce, time-varying bandwidth.

## Mechanism

Submaps are split into a pose-and-factor skeleton, entropy-prioritized geometry and semantic labels; convex per-round bandwidth allocation and packet scheduling are reshaped by TLS-GNC loop-closure and Lambda-Field risk feedback from the central back end (pp. 2-5).

## Baselines and controls

Non-hierarchical transmission and prior communication schemes, with a no-feedback ablation (pp. 6-7).

## Platform and setup

Dataset replay with simulated bandwidth and packet loss (pp. 5-7). S3DIS and ScanNet indoor RGB-D datasets with bandwidth sweeps and packet-loss tests (p. 1).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. Dataset replay only; collision risk is an estimated Lambda-Field quantity.

## Sensors

Indoor RGB-D scans.

## Compute and latency

Allocation scales as O(K log(1/epsilon)) in active submaps (p. 5); processor not inspected.

## Key quantitative results

- The alloc&safe feedback policy lowers estimated rendezvous risk and recovers loop closures earlier than baselines under packet loss (p. 8).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Guidance signals may become stale relative to robot motion and queued transmissions under higher-latency or asynchronous networks (p. 5).
- Broader sensing modalities, real-world wireless links and distributed back ends remain future work (p. 5).

## Transfer conditions

Assumes a central server computes feedback after every round; physical deployment is not evaluated.

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

- **p. 5, Sec. III-E.** "Under higher-latency or asynchronous networks, these guidance signals may become stale relative to robot motion and queued transmissions, which is a limitation of the current round-wise feedback design."
  Author-stated staleness limit.
- **p. 8, Sec. V.** "Future work will investigate larger and more heterogeneous robot teams, real-world deployments, and distributed architectures."
  Scope limit.

## Survey-usable statements

### Supported

- Prioritized layered transmission can preserve useful map content under bandwidth limits in replay.

### Not supported

- Estimated collision risk is not a measured safety outcome.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 5, 6, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

As multi-robot mapping systems expand into data-intensive environments, efficient data transmission methods are essential for maintaining global consistency and safety under scarce and time-varying bandwidth. In this work, we propose a Feedback-Guided Hierarchical Transmission framework for centralized multi-robot mapping. In this framework, the submap representation is structured with three layers: L1 extracts the pose-and-factor skeleton to ensure topological consistency with minimal overhead; L2 streams geometric details, prioritized by semantic-weighted entropy reduction to refine the occupancy map; L3 delivers semantic labels to support high-level understanding. To optimize transmission, the backend performs centralized occupancy fusion and employs Truncated Least Squares Graduated Non-Convexity (TLS-GNC) pose-graph optimization and a Lambda-Field risk model to produce guidance signals. These signals dynamically reshape the utility curves of the layers to prioritize loop-closure consistency and safety-critical regions. Experiments are conducted on S3DIS and ScanNet indoor RGB-D datasets to validate the effectiveness of the proposed framework. The performance evaluation under bandwidth sweeps and packet loss tests indicates that our method reaches joint geometry-and-semantics accuracy with fewer bytes, recovers loop closures faster, and lowers estimated collision risk in rendezvous regions compared with non-hierarchical baselines.
