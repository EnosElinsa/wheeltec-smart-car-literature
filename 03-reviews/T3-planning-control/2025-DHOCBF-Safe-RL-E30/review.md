# Differential High Order Control Barrier Function-Based Safe Reinforcement Learning

## Metadata

| Field | Value |
|---|---|
| ID | E30 |
| Title | Differential High Order Control Barrier Function-Based Safe Reinforcement Learning |
| Authors | Xiangyu Kong, Yuanqing Xia, Zhongqi Sun, Di-Hua Zhai, Yunshan Deng, and Sihua Zhang |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 7, pp. 7524-7531 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3575310](https://doi.org/10.1109/lra.2025.3575310) |
| Official URL | https://ieeexplore.ieee.org/document/11018429/ |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2025-DHOCBF-Safe-RL-E30/paper.pdf` and `02-fulltext/T3-planning-control/2025-DHOCBF-Safe-RL-E30/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-DHOCBF-Safe-RL-E30/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: numerical
- evidence_all: numerical, theory-only
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: kinematic model [x, y, v, theta] of a wheeled mobile robot (text, p. 6); no physical robot
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: model states and obstacle positions; no perception
- compute: penalty network of two 256-unit ReLU layers; no hardware, training time, or QP time reported
- compute_location: not-reported
- summary_result: In numerical navigation tests, learned HOCBF penalties reach rewards near the alpha = 8 setting and keep the QP feasible where fixed alpha = 8 becomes infeasible.
- summary_limitation: No limitation is stated by the authors; the evidence is numerical tests of a wheeled kinematic model with one or three obstacles.
- survey_included: yes
- verification_level: light

## Problem

Fixed class-K parameters of an HOCBF make safe RL overly conservative and cause abrupt action changes, and tighter input bounds can make the QP infeasible.

## Mechanism

An MLP with two 256-unit layers outputs stochastic state-dependent penalty functions and is trained together with SAC. A differentiable QP minimally modifies the RL action. The loss combines entropy, Q-value, and a penalty on abrupt action changes; the last-order penalty is restricted to a derived feasible set.

## Baselines and controls

- HOCBF-SAC with alpha1 = alpha2 = 1 (conservative).
- HOCBF-SAC with alpha1 = alpha2 = 8 (less conservative).

## Platform and setup

A wheeled kinematic model [x, y, v, theta] in two scenarios, with one and with three circular obstacles; obstacle positions are sampled from given regions in training and testing. Each scenario uses ten independent training runs, with reward mean and variance curves, and one test instance is shown. No robot photo, sensor, or physical experiment is given.

## Evidence type and transfer

The legacy card lists conditional feasibility and safety theory and numerical navigation tests of the wheeled model. There is no hardware evidence.

## Sensors

The method uses model states and obstacle positions; perception uncertainty is not implemented or evaluated.

## Compute and latency

The penalty network has two 256-unit ReLU layers (p. 4). No CPU, GPU, training time, or QP time is reported.

## Key quantitative results

- Figs. 3-6: rewards approach those of alpha = 8 and exceed those of alpha = 1 while reducing abrupt action changes; there is no reward table, so the legacy card gives no values read from the curves (p. 7).
- Figs. 7-8: with tightened input bounds, the fixed alpha = 8 QP with zero slack becomes infeasible, while the adaptive penalties stay feasible in the shown instance (p. 8). Default penalty range 1 to 8; abrupt-change threshold ||Delta u||^2 = 0.35 (p. 7).

## Stated limitations

The authors state no limitation.

## Transfer conditions

Legacy reviewer observations: the theorems assume that the nominal RL action lies strictly inside the input bounds, that psi_(m-1) > 0, and that the initial state lies in all higher-order sets, so they do not guarantee feasibility for arbitrarily tight inputs. The comparison is mainly against fixed-parameter variants of the same framework, without a common benchmark of external safe-RL systems. No hardware evidence is given, and noise, delay, model error, and compute are not evaluated.

## Code and data

The legacy card found no code or data address in the text; not verified.

## Version family

RA-L 2025. BarrierNet and adaptive CBF work are cited as method background; no version overlap with papers in this batch is declared.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | qualifies | weak | V-C Results and Discussion, p. 7 | "The results shown below are only one instance in the testing phase." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 7, V-C Results and Discussion.** "For each scenario, ten independent training runs are conducted, and the mean and variance of the cumulative rewards are reported."
  The reward curves come from ten training runs per scenario.
- **p. 7, V-C Results and Discussion.** "The results shown below are only one instance in the testing phase."
  The trajectories are single examples, not aggregate safety rates.
- **p. 8, Feasibility.** "the QP in the HOCBF-based safe RL becomes infeasible when the slack variable"
  The fixed-parameter baseline loses feasibility under tightened bounds.

## Survey-usable statements

### Supported

- Learning state-dependent HOCBF penalties together with SAC reduces conservativeness relative to alpha = 1 and keeps the QP feasible under tighter input bounds in numerical tests of a wheeled kinematic model.

### Not supported

- Hardware validation: there is no physical experiment.
- Aggregate collision or safety rates: the trajectories are single test instances.
- Superiority over other safe-RL methods: only fixed-parameter variants of the same framework are compared.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; the legacy quote was found and kept; excerpts added from the results and feasibility text; the legacy limitations are reviewer observations and moved to Transfer conditions
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/a3d7cf1440a944db9cf4f45b/

## Original abstract

Safe reinforcement learning (RL) aims to learn policy while also ensuring the safety constraints. An increasingly common approach is to design a safety filter based on control barrier function (CBF) or high order control barrier function (HOCBF) for the RL policy. A quadratic programming (QP) is then formulated and solved to modify the RL policy, enabling safe exploration. However, directly integrating the safety filter with RL presents two challenges: (1) the conservativeness of safe policy, and (2) potential infeasibility of the QP under bounded input constraints. These issues limit the performance of safe RL. In this letter, we introduce a differential HOCBF constraint by incorporating neural network-based penalty functions into HOCBF. Furthermore, we propose a differential HOCBF-based safe RL framework in which the penalty functions and RL policy are trained concurrently. To address conservativeness, we train penalty functions to maximize long-term rewards while preventing abrupt changes in safe action, thereby achieving ideal performance. To ensure the feasibility ofthe formulated QP under bounded input constraints, we calculate a set for penalty functions and prove that the feasibility is guaranteed if the learned penalty functions remain within the set. Finally, we verify the effectiveness of the proposed framework on the wheeled mobile robot navigation and obstacle avoidance task.
