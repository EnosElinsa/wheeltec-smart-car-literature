# Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild

## Metadata

| Field | Value |
|---|---|
| ID | S41 |
| Title | Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild |
| Authors | Stachowicz, Kyle and Ignatova, Lydia and Levine, Sergey |
| Venue | Conference on Robot Learning |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v270/stachowicz25a.html |
| Theme folder | T6-reliability-deployment |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-LiReN-S41/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-LiReN-S41/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-LiReN-S41/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: differential-drive
- platform: iRobot Create3 with a prepared goal graph, LiDAR localization map, bumper and charging stations (pp. 5-6).
- boundary_platform: no
- degradation: scene-change, model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Fisheye RGB for policy; LiDAR/map for goal selection, bumper for recovery and battery monitoring
- compute: Jetson Orin NX inference, asynchronous Google TPUv4 server training with network model updates (p. 6).
- compute_location: mixed
- summary_result: Continual learning is supported by an explicit recovery and deployment framework.
- summary_limitation: Requires localization for graph goals, supports one fine-tuning task, and does not evaluate concurrent adaptation to multiple new embodiments (p. 8).
- survey_included: yes
- verification_level: light

## Problem

A broad pretrained navigation model needs continuing adaptation and operational support to learn autonomously.

## Mechanism

LiReN offline RL plus online replay, graph goal selection, pseudo-resets, keepout rules, help escalation and charging (pp. 4-6).

## Baselines and controls

Offline/online learning, goal-conditioned behavior cloning and RL-from-scratch comparisons (pp. 6-7).

## Platform and setup

iRobot Create3 with a prepared goal graph, LiDAR localization map, bumper and charging stations (pp. 5-6).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. RGB policy input does not imply a camera-only system; training network, goal map, charging and human escalation are operational dependencies.

## Sensors

Fisheye RGB for policy; LiDAR/map for goal selection, bumper for recovery and battery monitoring.

## Compute and latency

Jetson Orin NX inference, asynchronous Google TPUv4 server training with network model updates (p. 6).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Requires localization for graph goals, supports one fine-tuning task, and does not evaluate concurrent adaptation to multiple new embodiments (p. 8).

## Transfer conditions

RGB policy input does not imply a camera-only system; training network, goal map, charging and human escalation are operational dependencies.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Official citation title uses "Improvement"; the linked publisher PDF uses "Fine-Tuning". This documented title variant is one work; no DOI is invented. Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 6, Selected source passage.** "we also equip our robot with a LiDAR sensor and a map of the environment for localization"
  Supplies a concrete model-to-system comparison for lifelong learning rather than treating adaptation as the whole deployment solution.

## Survey-usable statements

### Supported

- Continual learning is supported by an explicit recovery and deployment framework. Supplies a concrete model-to-system comparison for lifelong learning rather than treating adaptation as the whole deployment solution.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. RGB policy input does not imply a camera-only system; training network, goal map, charging and human escalation are operational dependencies.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Recent works have proposed a number of general-purpose robotic foundation models that can control a variety of robotic platforms to perform a range of different tasks, including in the domains of navigation and manipulation. However, such models are typically trained via imitation learning, which precludes the ability to adapt autonomously through experience that the robot gathers on the job. In this work, our aim is to train general-purpose robotic foundation models in the domain of robotic navigation specifically with the aim of enabling autonomous self-improvement. We show that a combination of pretraining with offline reinforcement learning and a complete system for continual autonomous operation leads to a robotic learning framework that not only starts off with broad and diverse capabilities, but can further specialize and adapt those capabilities in the course of carrying out navigational tasks in a given deployment location. To our knowledge, this result demonstrates the first navigation robot foundation model to continually learn via autonomous interaction in open-world settings.
