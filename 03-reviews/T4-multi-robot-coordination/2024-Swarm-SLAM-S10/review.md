# Swarm-SLAM: Sparse Decentralized Collaborative Simultaneous Localization and Mapping Framework for Multi-Robot Systems

## Metadata

| Field | Value |
|---|---|
| ID | S10 |
| Title | Swarm-SLAM: Sparse Decentralized Collaborative Simultaneous Localization and Mapping Framework for Multi-Robot Systems |
| Authors | Lajoie, Pierre-Yves and Beltrame, Giovanni |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2023.3333742](https://doi.org/10.1109/lra.2023.3333742) |
| Official URL | https://ieeexplore.ieee.org/document/10321649/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2024-Swarm-SLAM-S10/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2024-Swarm-SLAM-S10/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2024-Swarm-SLAM-S10/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: online-hardware
- evidence_all: online-hardware, dataset-playback
- protocol_caveats: none
- platform_class: skid-steer
- platform: Online team of AgileX Scout, Scout Mini and Spot, plus public dataset replay; wheeled platforms take coding precedence (p. 7).
- boundary_platform: no
- degradation: bandwidth-limit, communication-partition, data-association-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR/IMU odometry, RGB-D inter-robot loops and ad-hoc gateways
- compute: Jetson AGX Xavier on each real robot; ROS2 decentralized estimation/communication (pp. 1, 7).
- compute_location: onboard
- summary_result: Sparse decentralized estimation supports shared-frame convergence through selected robot encounters.
- summary_limitation: Collaborative domain calibration and place-recognition uncertainty to reduce loop outliers remain future work (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Continuous full connectivity and dense loop exchange do not scale to opportunistic robot teams.

## Mechanism

Tracks neighbors and exchanged data, prioritizes sparse loop constraints and propagates anchor/reference-frame choices across occasional rendezvous (pp. 3, 7).

## Baselines and controls

Greedy versus spectral loop prioritization and successive subset rendezvous in split datasets; online parking-lot demonstration reports communication/computation (pp. 5-7).

## Platform and setup

Online team of AgileX Scout, Scout Mini and Spot, plus public dataset replay; wheeled platforms take coding precedence (p. 7).

## Evidence type and transfer

Strongest coded setting: `online-hardware`. Online mapping does not itself prove that shared estimates control navigation; rendezvous/frame convergence does not establish arbitrary stale/corrupted-update acceptance.

## Sensors

LiDAR/IMU odometry, RGB-D inter-robot loops and ad-hoc gateways.

## Compute and latency

Jetson AGX Xavier on each real robot; ROS2 decentralized estimation/communication (pp. 1, 7).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Collaborative domain calibration and place-recognition uncertainty to reduce loop outliers remain future work (p. 8).

## Transfer conditions

Online mapping does not itself prove that shared estimates control navigation; rendezvous/frame convergence does not establish arbitrary stale/corrupted-update acceptance.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 3, Selected source passage.** "it does not require connectivity maintenance during the whole mission."
  Requires reconnection discussion to acknowledge implemented neighbor/anchor management rather than implying that reconnection mechanisms are absent.

## Survey-usable statements

### Supported

- Sparse decentralized estimation supports shared-frame convergence through selected robot encounters. Requires reconnection discussion to acknowledge implemented neighbor/anchor management rather than implying that reconnection mechanisms are absent.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Online mapping does not itself prove that shared estimates control navigation; rendezvous/frame convergence does not establish arbitrary stale/corrupted-update acceptance.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Collaborative Simultaneous Localization And Mapping (C-SLAM) is a vital component for successful multi-robot operations in environments without an external positioning system, such as indoors, underground or underwater. In this paper, we introduce Swarm-SLAM, an open-source C-SLAM system that is designed to be scalable, flexible, decentralized, and sparse, which are all key properties in swarm robotics. Our system supports lidar, stereo, and RGB-D sensing, and it includes a novel inter-robot loop closure prioritization technique that reduces communication and accelerates convergence. We evaluated our ROS 2 implementation on five different datasets, and in a real-world experiment with three robots communicating through an ad-hoc network.
