# SCALE: Self-Correcting Visual Navigation for Mobile Robots via Anti-Novelty Estimation

## Metadata

| Field | Value |
|---|---|
| ID | S38 |
| Title | SCALE: Self-Correcting Visual Navigation for Mobile Robots via Anti-Novelty Estimation |
| Authors | Chen, Chang and Liu, Yuecheng and Zhuang, Yuzheng and Mao, Sitong and Xue, Kaiwen and Zhou, Shunbo |
| Venue | 2024 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/icra57147.2024.10610847](https://doi.org/10.1109/icra57147.2024.10610847) |
| Official URL | https://ieeexplore.ieee.org/document/10610847/ |
| Theme folder | T6-reliability-deployment |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2024-SCALE-S38/paper.pdf` and `02-fulltext/T6-reliability-deployment/2024-SCALE-S38/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2024-SCALE-S38/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: skid-steer
- platform: Scout-mini in three outdoor urban scenarios, with manually collected scenario-specific data (p. 5).
- boundary_platform: no
- degradation: model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Forward RGB; wheel odometry used in data preparation; installed LiDAR is explicitly unused
- compute: NVIDIA Jetson Xavier onboard; offline IQL/affordance/novelty learning (p. 5).
- compute_location: onboard
- summary_result: Anti-novelty recovery reduces intervention need in the inspected urban deployments.
- summary_limitation: More challenging or unknown environments remain future work (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Unfamiliar observations can break visual goal localization and lead a learned policy toward collisions.

## Mechanism

IQL goal-conditioned policy, affordance trajectory generation and RND future-novelty scoring choose a route toward familiar observations (pp. 2-4).

## Baselines and controls

Open-world visual navigation methods and recovery/representation ablations (pp. 5-6).

## Platform and setup

Scout-mini in three outdoor urban scenarios, with manually collected scenario-specific data (p. 5).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Familiarity is relative to collected training data; low novelty is not a geometric clearance bound or calibrated integrity probability.

## Sensors

Forward RGB; wheel odometry used in data preparation; installed LiDAR is explicitly unused.

## Compute and latency

NVIDIA Jetson Xavier onboard; offline IQL/affordance/novelty learning (p. 5).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

More challenging or unknown environments remain future work (p. 6).

## Transfer conditions

Familiarity is relative to collected training data; low novelty is not a geometric clearance bound or calibrated integrity probability.

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

- **p. 5, Selected source passage.** "The 3D LIDAR on the robot is not used in this work."
  Makes a learned recovery action distinct from ordinary goal following and from physical safety verification.

## Survey-usable statements

### Supported

- Anti-novelty recovery reduces intervention need in the inspected urban deployments. Makes a learned recovery action distinct from ordinary goal following and from physical safety verification.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Familiarity is relative to collected training data; low novelty is not a geometric clearance bound or calibrated integrity probability.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 6; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Although visual navigation has been extensively studied using deep reinforcement learning, online learning for real-world robots remains a challenging task. Recent work directly learned from offline dataset to achieve broader generalization in the real-world tasks, which, however, faces the out-of-distribution (OOD) issue and potential robot localization failures in a given map for unseen observation. This significantly drops the success rates and even induces collision. In this paper, we present a self-correcting visual navigation method, SCALE, that can autonomously prevent the robot from the OOD situations without human intervention. Specifically, we develop an image-goal conditioned offline reinforcement learning method based on implicit Q-learning (IQL). When facing OOD observation, our novel localization recovery method generates the potential future trajectories by learning from the navigation affordance, and estimates the future novelty via random network distillation (RND). A tailored cost function searches for the candidates with the least novelty that can lead the robot to the familiar places. We collect offline data and conduct evaluation experiments in three real-world urban scenarios. Experiment results show that SCALE outperforms the previous state-of-the-art methods for open-world navigation with a unique capability of localization recovery, significantly reducing the need for human intervention. Code is available at https://github.com/KubeEdge4Robotics/ScaleNav.
