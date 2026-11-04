# SELFI: Autonomous Self-Improvement with RL for Vision-Based Navigation around People

## Metadata

| Field | Value |
|---|---|
| ID | S14 |
| Title | SELFI: Autonomous Self-Improvement with RL for Vision-Based Navigation around People |
| Authors | Hirose, Noriaki and Shah, Dhruv and Stachowicz, Kyle and Sridhar, Ajay and Levine, Sergey |
| Venue | Conference on Robot Learning |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v270/hirose25a.html |
| Theme folder | T6-reliability-deployment |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-SELFI-S14/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-SELFI-S14/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-SELFI-S14/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: teleoperated-mapping, scripted-scenario
- platform_class: wheeled-unspecified
- platform: Indoor prototype robot with organized obstacle/pedestrian comparisons and separate uncontrolled online learning (pp. 6, 14).
- boundary_platform: no
- degradation: dynamic-objects, model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Omnidirectional RGB, extra cameras/visual odometry and AR markers, IMU and bumper
- compute: Jetson Orin AGX policy inference; separate i9/RTX workstation online training. Map/marker infrastructure supplies goal poses (p. 14).
- compute_location: mixed
- summary_result: Online adaptation improves obstacle/social behaviors with intervention-aware evaluation.
- summary_limitation: Extensive reproducible comparisons in naturally populated environments are difficult; organized settings are used for controlled comparisons (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Offline social navigation objectives omit behaviors and conditions encountered during deployment.

## Mechanism

SELFI stabilizes online model-free RL with the model-based objective used by SACSoN offline pretraining (pp. 4-5).

## Baselines and controls

Residual RL, SACSoN fine-tuning and sampling-based planning; organized comparisons because uncontrolled pedestrian traffic is not reproducible (p. 6).

## Platform and setup

Indoor prototype robot with organized obstacle/pedestrian comparisons and separate uncontrolled online learning (pp. 6, 14).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Online improvement depends on teleoperated topological mapping, localization fiducials, collision sensing and a training workstation.

## Sensors

Omnidirectional RGB, extra cameras/visual odometry and AR markers, IMU and bumper.

## Compute and latency

Jetson Orin AGX policy inference; separate i9/RTX workstation online training. Map/marker infrastructure supplies goal poses (p. 14).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Extensive reproducible comparisons in naturally populated environments are difficult; organized settings are used for controlled comparisons (p. 6).

## Transfer conditions

Online improvement depends on teleoperated topological mapping, localization fiducials, collision sensing and a training workstation.

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

- **p. 14, Selected source passage.** "In addition to on-robot compute, we use a workstation for fast, online training."
  Adds learning-time interventions and infrastructure cost to the deployment evaluation, beyond final policy success.

## Survey-usable statements

### Supported

- Online adaptation improves obstacle/social behaviors with intervention-aware evaluation. Adds learning-time interventions and infrastructure cost to the deployment evaluation, beyond final policy success.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Online improvement depends on teleoperated topological mapping, localization fiducials, collision sensing and a training workstation.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 5, 6, 8, 14; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Autonomous self-improving robots that interact and improve with experience are key to the real-world deployment of robotic systems. In this paper, we propose an online learning method, SELFI, that leverages online robot experience to rapidly fine-tune pre-trained control policies efficiently. SELFI applies online model-free reinforcement learning on top of offline model-based learning to bring out the best parts of both learning paradigms. Specifically, SELFI stabilizes the online learning process by incorporating the same model-based learning objective from offline pre-training into the Q-values learned with online model-free reinforcement learning. We evaluate SELFI in multiple real-world environments and report improvements in terms of collision avoidance, as well as more socially compliant behavior, measured by a human user study. SELFI enables us to quickly learn useful robotic behaviors with less human interventions such as pre-emptive behavior for the pedestrians, collision avoidance for small and transparent objects, and avoiding travel on uneven floor surfaces. We provide supplementary videos to demonstrate the performance of our fine-tuned policy on our project page 1.
