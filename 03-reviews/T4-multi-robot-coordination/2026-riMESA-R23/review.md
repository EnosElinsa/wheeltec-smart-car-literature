# riMESA: Consensus ADMM for Real-World Collaborative SLAM

## Metadata

| Field | Value |
|---|---|
| ID | R23 |
| Title | riMESA: Consensus ADMM for Real-World Collaborative SLAM |
| Authors | Daniel McGann, and Michael Kaess |
| Venue | IEEE Transactions on Robotics |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tro.2026.3706569](https://doi.org/10.1109/tro.2026.3706569) |
| Official URL | https://ieeexplore.ieee.org/document/11575119/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-riMESA-R23/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-riMESA-R23/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-riMESA-R23/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: dataset-playback
- evidence_all: dataset-playback, simulation
- protocol_caveats: none
- platform_class: mixed
- platform: 2430 synthetic datasets and 28 real-world datasets from COSMO-Bench and Nebula with modeled communication (pp. 16, 18).
- boundary_platform: yes
- degradation: communication-partition, communication-delay-loss, data-association-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR-based C-SLAM factors from benchmark front ends
- compute: Intel Core i9-13900K with 128 GB RAM (p. 18).
- compute_location: desktop-offline
- summary_result: A robust incremental consensus-ADMM back end tolerates outliers, dropouts and latency and improves accuracy over prior back ends by a factor above seven on real-world datasets (p. 1).
- summary_limitation: Convergence is provable only under restrictive conditions; shared-state identification is delegated to the front end (pp. 9, 11).
- survey_included: yes
- verification_level: light

## Problem

C-SLAM back ends need reliable connectivity, excessive computation or fail with outlier measurements.

## Mechanism

Edge-based consensus ADMM is made incremental and asynchronous; the riSAM local solver rejects outliers; a communication handler discards failed exchanges and resynchronizes after two-generals failures (pp. 5-11).

## Baselines and controls

Prior centralized, decentralized and distributed C-SLAM back ends (pp. 11-16).

## Platform and setup

Synthetic scenarios, scale and communication experiments and real-LiDAR benchmark data with Wi-Fi or radio connectivity models (pp. 11-16). 2430 synthetic datasets and 28 real-world datasets from COSMO-Bench and Nebula with modeled communication (pp. 16, 18).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. The real-world experiment replays benchmark data with modeled communication rather than a physical team.

## Sensors

LiDAR-based C-SLAM factors from benchmark front ends.

## Compute and latency

Intel Core i9-13900K with 128 GB RAM (p. 18).

## Key quantitative results

- Communication is initiated at 5 Hz with exchanges of at most 200 ms under connectivity models matched to each dataset (p. 16).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Convergence will be provable only under restrictive conditions that real C-SLAM problems may not satisfy (p. 11).
- Inter-robot front ends are assumed to identify shared state (p. 9).

## Transfer conditions

Physical radios, onboard timing and navigation use of the estimate are outside the evaluation.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

The authors call riMESA a direct extension of iMESA (p. 11), which is library entry [E40](../../T4-multi-robot-coordination/2024-iMESA-E40/review.md). riMESA adds outlier handling, nonblocking communication, environment variables and shared-variable initialization, so both are kept as separate method entries and the survey states their relation.

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

- **p. 16, Sec. VII-F.** "In our final experiment, we seek to evaluate the performance of riMESA on data that (as closely as possible) resembles real-world data."
  Defines the scope of the real-world experiment.
- **p. 9, Sec. V-D.** "We assume that inter-robot measurement front-ends are responsible for identifying this shared state."
  Front-end assumption.

## Survey-usable statements

### Supported

- Consensus ADMM provides an outlier-robust, asynchronous C-SLAM back end under modeled communication failures.

### Not supported

- The paper does not report a physical multirobot deployment of the back end.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 9, 11, 16, 18; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Collaborative simultaneous localization and mapping (C-SLAM) is a fundamental capability for multirobot teams as it enables downstream tasks, such as planning and navigation. However, existing C-SLAM back-end algorithms that are required to solve this problem struggle to address the practical realities of real-world deployments (i.e., communication limitations, outlier measurements, and online operation). In this article, we propose Robust Incremental Manifold Edge-based Separable ADMM (riMESA)—a robust, incremental, and distributed C-SLAM back-end that is resilient to outliers, reliable in the face of limited communication, and can compute accurate state estimates for a multirobot team in real time. Through the development of riMESA, we, more broadly, make an argument for the use of consensus alternating direction method of multipliers as a theoretical foundation for distributed optimization tasks in robotics, such as C-SLAM due to its flexibility, accuracy, and fast convergence. We conclude this work with an in-depth evaluation of riMESA on a variety of C-SLAM problem scenarios and communication network conditions using both synthetic and real-world C-SLAM data. These experiments demonstrate that riMESA is able to generalize across conditions, produce accurate state estimates, operate in real time, and outperform the accuracy of prior works by a factor $>7$ on real-world datasets.
