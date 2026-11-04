# R-FAC: Resilient Value Function Factorization for Multirobot Efficient Search With Individual Failure Probabilities

## Metadata

| Field | Value |
|---|---|
| ID | R35 |
| Title | R-FAC: Resilient Value Function Factorization for Multirobot Efficient Search With Individual Failure Probabilities |
| Authors | Hongliang Guo, Qi Kang, Wei-Yun Yau, Chee-Meng Chew, and Daniela Rus |
| Venue | IEEE Transactions on Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3567478](https://doi.org/10.1109/tro.2025.3567478) |
| Official URL | https://ieeexplore.ieee.org/document/10989574/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-R-FAC-R35/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-R-FAC-R35/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-R-FAC-R35/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: multi-robot
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: wheeled-unspecified
- platform: Canonical grid search environments in simulation and S30 searcher robots with embedded LiDAR and camera in a 12-room mock house (pp. 10-15).
- boundary_platform: no
- degradation: actuator-fault
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Target detection assumed perfect in the model; LiDAR and camera on the S30 robots
- compute: Server with RTX 3080 for simulations (p. 10).
- compute_location: not-reported
- summary_result: Log-sum-exp value factorization keeps search performance highest when one or several robots withdraw during execution (pp. 11-13).
- summary_limitation: Assumes a perfect target sensor; malfunctioning robots simply quit the team (p. 15).
- survey_included: yes
- verification_level: light

## Problem

Robots may fail and leave a search team without notice, changing team size during execution.

## Mechanism

The R-FAC paradigm constructs a central value function from individual ones for any team composition; V2DN uses log-sum-exp factorization trained with failure probabilities (pp. 5-9).

## Baselines and controls

VDN, CE-PG, FHPE and MILP planners, with resiliency scores before and during execution (pp. 10-13).

## Platform and setup

Grid-world simulations with preset failure probabilities and a physical proof of concept (pp. 10-15). Canonical grid search environments in simulation and S30 searcher robots with embedded LiDAR and camera in a 12-room mock house (pp. 10-15).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Simulated resiliency benchmarks and a proof-of-concept hardware run.

## Sensors

Target detection assumed perfect in the model; LiDAR and camera on the S30 robots.

## Compute and latency

Server with RTX 3080 for simulations (p. 10).

## Key quantitative results

- Other robots may continue following the previous plan without real-time knowledge of failures (p. 13).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- A perfect sensor is assumed; probabilistic detections are future work (p. 15).

## Transfer conditions

Failure is modeled as withdrawal with known probability; partial degradation and false detections are excluded.

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

- **p. 13, Sec. V-G.** "In practice, when one or several robots fail and quit the team, other robots might not know the information in real time, and they are still following the previously calculated search plan."
  Motivates failure-aware training.
- **p. 15, Sec. VII.** "the robot team is deployed to search for the adversarial moving target, where the target adapts its motion dynamics based on the robot team"
  Future-work item listed beside the perfect-sensor assumption, which the PDF text layer merges into run-on words.

## Survey-usable statements

### Supported

- Team policies can be trained to remain effective when members fail without notification.

### Not supported

- Diagnosis of the failure is not part of the method.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 5, 10, 13, 15; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

This article investigates the resilient multirobot efficient search problem (R-MuRES), which aims at coordinating multiple robots to detect a “nonadversarial” moving target with the minimal expected time. One unique characteristic of R-MuRES among others is the possibility of individual robot’s malfunction and withdrawal from the team during task execution, which results in a variable number of searchers in the deployment phase and entails that the possibility of team member failures must be considered during the planning stage, particularly in the training phase. We propose a resilient value function factorization (R-FAC) paradigm, which constructs the central value function from individual ones in a resilient manner, taking into account individual robots’ failures, and ensures that the constructed central value function has the minimal mean squared temporal difference error across various team compositions. R-FAC stipulates that the individual global maximum principle is satisfied for whichever team configuration and thus any functioning robot contributes positively to the remaining team, as long as it executes the greedy policy with respect to the factorized individual value function. Subsequently, we introduce the variational value decomposition network (V2DN) as one of the instantiated R-FAC algorithms. V2DN employs the log-sum-exp mechanism to construct the central value function from individual ones, enabling it to take a varying number of robots’ individual value functions as inputs. Then, we explain why, specifically for the multirobot search task, the log-sum-exp mechanism is superior to the brute-force summation operation used in the canonical value decomposition network (VDN), and compare V2DN with state-of-the-art MuRES solutions as well as the vanilla VDN algorithm in two canonical MuRES testing environments and show that it achieves the best resiliency score when one or several individual robots quit the team during task execution. Furthermore, we validate V2DN with a real multirobot system in a self-constructed indoor environment as the proof of concept.
