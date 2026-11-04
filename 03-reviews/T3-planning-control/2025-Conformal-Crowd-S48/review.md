# Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling

## Metadata

| Field | Value |
|---|---|
| ID | S48 |
| Title | Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling |
| Authors | Yao, Jianpeng and Zhang, Xiaopan and Xia, Yu and Wang, Zejin and Roy-Chowdhury, Amit and Li, Jiachen |
| Venue | Conference on Robot Learning |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v305/yao25a.html |
| Theme folder | T3-planning-control |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2025-Conformal-Crowd-S48/paper.pdf` and `02-fulltext/T3-planning-control/2025-Conformal-Crowd-S48/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2025-Conformal-Crowd-S48/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: offboard-compute
- platform_class: omnidirectional
- platform: CrowdNav simulation and physical ROSMASTER X3 Mecanum robot using ROS2; physical model transferred without further fine-tuning (pp. 6, 8).
- boundary_platform: no
- degradation: dynamic-objects, model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: RPLIDAR-A1, DR-SPAAM human detection, SORT tracking and GST pedestrian prediction
- compute: Robot connected through a router to a laptop with mobile RTX 3070; perception/control placement includes the offboard dependency (p. 8).
- compute_location: offboard-local
- summary_result: Adaptive prediction uncertainty and constrained learning jointly guide crowd avoidance under tested distribution shifts.
- summary_limitation: Missed detections, arbitrary-shaped static obstacles, residual OOD degradation and incomplete real-world shift coverage remain limitations (p. 9).
- survey_included: yes
- verification_level: light

## Problem

Learned crowd policies degrade when pedestrian speed, behavior or group structure changes.

## Mechanism

Adaptively calibrates prediction uncertainty, includes uncertainty features in the policy, and constrains cumulative intrusion into uncertainty regions during reinforcement learning (p. 3).

## Baselines and controls

Social-force, ORCA, MPC and RL variants with/without adaptive conformal inference and constrained RL; crowd distribution shifts are separated (pp. 6-8).

## Platform and setup

CrowdNav simulation and physical ROSMASTER X3 Mecanum robot using ROS2; physical model transferred without further fine-tuning (pp. 6, 8).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Conformal prediction coverage, an expected/cumulative intrusion constraint and a collision-free trajectory guarantee are different claims; detection failures can remove agents before calibration.

## Sensors

RPLIDAR-A1, DR-SPAAM human detection, SORT tracking and GST pedestrian prediction.

## Compute and latency

Robot connected through a router to a laptop with mobile RTX 3070; perception/control placement includes the offboard dependency (p. 8).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Missed detections, arbitrary-shaped static obstacles, residual OOD degradation and incomplete real-world shift coverage remain limitations (p. 9).

## Transfer conditions

Conformal prediction coverage, an expected/cumulative intrusion constraint and a collision-free trajectory guarantee are different claims; detection failures can remove agents before calibration.

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

- **p. 3, Selected source passage.** "we impose constraints on the cumulative intrusions of the robot into other agents’ uncertainty areas."
  Connects statistical uncertainty to executed crowd navigation while preserving guarantee scope and offboard/perception assumptions.

## Survey-usable statements

### Supported

- Adaptive prediction uncertainty and constrained learning jointly guide crowd avoidance under tested distribution shifts. Connects statistical uncertainty to executed crowd navigation while preserving guarantee scope and offboard/perception assumptions.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Conformal prediction coverage, an expected/cumulative intrusion constraint and a collision-free trajectory guarantee are different claims; detection failures can remove agents before calibration.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 6, 7, 8, 9; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Mobile robots navigating in crowds trained using reinforcement learning are known to suffer performance degradation when faced with out-of-distribution scenarios. We propose that by properly accounting for the uncertainties of pedestrians, a robot can learn safe navigation policies that are robust to distribution shifts. Our method augments agent observations with prediction uncertainty estimates generated by adaptive conformal inference, and it uses these estimates to guide the agent’s behavior through constrained reinforcement learning. The system helps regulate the agent’s actions and enables it to adapt to distribution shifts. In the in-distribution setting, our approach achieves a 96.93% success rate, which is over 8.80% higher than the previous state-of-the-art baselines with over 3.72 times fewer collisions and 2.43 times fewer intrusions into ground-truth human future trajectories. In three out-of-distribution scenarios, our method shows much stronger robustness when facing distribution shifts in velocity variations, policy changes, and transitions from individual to group dynamics. We deploy our method on a real robot, and experiments show that the robot makes safe and robust decisions when interacting with both sparse and dense crowds. Our code and videos are available on https://gen-safe-nav.github.io/.
