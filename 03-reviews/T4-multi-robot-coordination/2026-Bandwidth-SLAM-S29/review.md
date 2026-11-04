# Bandwidth-Efficient Collaborative SLAM: Mutual Information for Data Selection and Finite-State Entropy for Lossless Compression

## Metadata

| Field | Value |
|---|---|
| ID | S29 |
| Title | Bandwidth-Efficient Collaborative SLAM: Mutual Information for Data Selection and Finite-State Entropy for Lossless Compression |
| Authors | Zhang, Weiqiang and Cheng, Lan and Wei, Jiangxia and Xu, Xinying and Zhang, Zhe and Xin, Bin |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2026.3666939](https://doi.org/10.1109/tase.2026.3666939) |
| Official URL | https://ieeexplore.ieee.org/document/11406164/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Bandwidth-SLAM-S29/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Bandwidth-SLAM-S29/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Bandwidth-SLAM-S29/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: online-hardware
- evidence_all: online-hardware, dataset-playback
- protocol_caveats: offboard-compute
- platform_class: wheeled-unspecified
- platform: Racecar/ZED2 parking-lot experiment plus EuRoC, KITTI and UMA-VI replay (pp. 7, 10-11).
- boundary_platform: no
- degradation: bandwidth-limit
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Stereo/visual keyframes and inertial SLAM input according to benchmark
- compute: Local visual odometry/map on agents with HP Zhan 99 central server for collaborative back-end optimization (pp. 3, 7, 11).
- compute_location: mixed
- summary_result: Selection and coding reduce transmitted data within a centralized collaborative pipeline.
- summary_limitation: Threshold sensitivity varies with visual difficulty; more principled adaptive threshold selection and architecture extension are future work (pp. 9-11).
- survey_included: yes
- verification_level: light

## Problem

Redundant keyframes and repeated transmission content consume collaborative SLAM bandwidth.

## Mechanism

Mutual-information keyframe selection discards data; finite-state entropy coding is lossless only for retained transmissions (pp. 3, 11).

## Baselines and controls

COVINS pipeline, random/heuristic/learned keyframe selection and threshold sweeps; compared keyframe counts are not exactly equal (pp. 7, 10).

## Platform and setup

Racecar/ZED2 parking-lot experiment plus EuRoC, KITTI and UMA-VI replay (pp. 7, 10-11).

## Evidence type and transfer

Strongest coded setting: `online-hardware`. Compression is not a partition/reconnection protocol; selected content is lossy even though coding is lossless.

## Sensors

Stereo/visual keyframes and inertial SLAM input according to benchmark.

## Compute and latency

Local visual odometry/map on agents with HP Zhan 99 central server for collaborative back-end optimization (pp. 3, 7, 11).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Threshold sensitivity varies with visual difficulty; more principled adaptive threshold selection and architecture extension are future work (pp. 9-11).

## Transfer conditions

Compression is not a partition/reconnection protocol; selected content is lossy even though coding is lossless.

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

- **p. 11, Selected source passage.** "lossy selection, lossless refinement"
  Separates information loss from bitstream compression in the communication budget.

## Survey-usable statements

### Supported

- Selection and coding reduce transmitted data within a centralized collaborative pipeline. Separates information loss from bitstream compression in the communication budget.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Compression is not a partition/reconnection protocol; selected content is lossy even though coding is lossless.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 7, 9, 10, 11; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Collaborative SLAM systems allow resource-constrained robots to offload intensive computation to a central server, making real-time mapping and localization feasible. However, this approach introduces significant communication overhead, which can hinder practical deployment due to the high bandwidth required to transmit sensor data. To address this communication bottleneck in large-scale SLAM systems, we propose a novel bandwidth-optimization strategy that enables efficient collaboration between resource-constrained robots and a powerful central server. This strategy leverages mutual-information theory to select and transmit only the most informative keyframes, significantly reducing redundancy. Additionally, we apply finite-state entropy coding to achieve lossless compression of the selected data. Experiments on the public dataset and real-world scene demonstrate that our approach achieves a substantial 78% reduction in bandwidth usage compared to state-of-the-art centralized multi-robot SLAM methods, while maintaining high-precision localization and mapping performance without introducing significant computational overhead.
