# Leveraging motion perceptibility and deep reinforcement learning for visual control of nonholonomic mobile robots

## Metadata

| Field | Value |
|---|---|
| ID | M04 |
| Title | Leveraging motion perceptibility and deep reinforcement learning for visual control of nonholonomic mobile robots |
| Authors | Takieddine Soualhi, Nathan Crombez, Alexandre Lombard, Yassine Ruichek, and Stéphane Galland |
| Venue | Robotics and Autonomous Systems, vol. 189, art. 104920 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1016/j.robot.2025.104920](https://doi.org/10.1016/j.robot.2025.104920) |
| Official URL | https://linkinghub.elsevier.com/retrieve/pii/S0921889025000065 |
| Theme folder | T3-planning-control |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T3-planning-control/2025-motion-perc-DRL-M04/paper.pdf` and `02-fulltext/T3-planning-control/2025-motion-perc-DRL-M04/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-motion-perc-DRL-M04/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Robotnik Summit-XL, four-wheeled nonholonomic robot (text, p. 10; drive type not stated); PyBullet training twin
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: front RGB camera for control; embedded 3D LiDAR with DLO only for evaluation
- compute: training on RTX 3090 and i9-12900KF; onboard RTX 2080 Ti inference about 3 ms, about 2 GB
- compute_location: onboard
- summary_result: Zero-shot on a real Summit-XL in an indoor poster room, the recurrent PPO visual-servoing policy converges with mean errors of about 0.20 m and 7.9 degrees.
- summary_limitation: The authors state that DRL needs simulator training, a deployment bottleneck versus plug-and-play classical visual servoing, and that ground friction lowers real convergence precision.
- survey_included: yes
- verification_level: light

## Problem

Visual servoing of nonholonomic wheeled robots under motion and camera field-of-view constraints: classical image-based and position-based laws can lose the target from some initial poses.

## Mechanism

Recurrent PPO in a POMDP. An auxiliary motion-perceptibility (MoP) head predicts interaction-matrix quantities from RGB images. An inverse-dynamics model supplies Rényi-divergence intrinsic rewards to improve exploration under nonholonomic limits. Actions are body-frame linear and angular velocities.

## Baselines and controls

Not recorded in the legacy extraction; not verified.

## Platform and setup

Policies are trained in PyBullet in an empty room with a poster, with 48 parallel environments. The policy transfers zero-shot to a real Robotnik Summit-XL with a front RGB camera. Pose error is measured by DLO on a pre-built 3D LiDAR map that the policy does not use.

## Evidence type and transfer

Simulation training and evaluation, plus zero-shot closed-loop control of the real robot in an empty indoor room. The legacy card notes that this is not cluttered outdoor terrain or a low-power chassis.

## Sensors

A front RGB camera for control. An embedded 3D LiDAR is used only for DLO pose evaluation.

## Compute and latency

Training: NVIDIA RTX 3090 and Intel i9-12900KF (p. 7). Inference on the robot: NVIDIA RTX 2080 Ti, about 3 ms response time and about 2 GB of memory (p. 12).

## Key quantitative results

- Real-scene mean convergence error: about 0.20 m in position and 7.9 degrees in orientation (p. 10).
- Onboard inference: about 3 ms per response on the RTX 2080 Ti (p. 12).

## Stated limitations

- DRL requires training in simulation, which the authors call a deployment bottleneck compared with plug-and-play classical methods (p. 11).
- Convergence precision is lower in the real environment than in simulation; ground friction affects maneuvers and rendered images miss real-scene details (p. 11).

## Transfer conditions

Legacy observations not located by text search: the policy can oscillate at convergence, and generalization over a wider Gaussian of desired poses degrades. The hardware is a GPU-equipped Summit-XL, not a resource-constrained edge stack, and the scene is an empty indoor room with a poster target.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | direct-support | strong | 6. Conclusion, p. 11 | "Classical methods are plug-and-play and independent of specific environments, whereas DRL often requires training robots in simulation, which constitutes a bottleneck in terms of deployment on real robots." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | 6. Conclusion, p. 11 | "Additionally, we showcase the transferability of our model to a real robot." |

## Page-cited excerpts

- **p. 11, 6. Conclusion.** "Classical methods are plug-and-play and independent of specific environments, whereas DRL often requires training robots in simulation, which constitutes a bottleneck in terms of deployment on real robots."
  The authors name simulator training as the deployment bottleneck.
- **p. 11, 6. Conclusion.** "Additionally, we showcase the transferability of our model to a real robot."
  Transfer is shown on one GPU-equipped robot in one room.
- **p. 11, Real experiments.** "Convergence precision in the real environment is slightly lower than the one obtained in simulation."
  The sim-to-real gap remains measurable.
- **p. 12, Testing.** "We record around a 3 ms response time"
  Inference timing on the onboard RTX 2080 Ti.

## Survey-usable statements

### Supported

- A recurrent PPO policy with a motion-perceptibility auxiliary task transfers zero-shot to a real nonholonomic robot for visual servoing in an indoor room (mean errors about 0.20 m and 7.9 degrees; numbers from a light review, re-check before citing).
- DRL visual servoing needs simulator training, which the authors call a deployment bottleneck.

### Not supported

- Embedded low-power deployment: inference runs on an RTX 2080 Ti.
- Real-world precision equals simulation: the authors report lower precision on the real robot.
- Use in cluttered or outdoor scenes: the real test is an empty indoor room.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-layout legacy card converted to the template; both legacy quotes found and kept; journal highlights removed from the abstract; oscillation and desired-pose generalization notes moved to Transfer conditions because they were not located
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

This paper introduces a novel deep reinforcement learning framework to tackle the problem of visual servoing of nonholonomic mobile robots. The visual control of nonholonomic mobile robots becomes particularly challenging within the classical paradigm of visual servoing, mainly due to motion and visibility constraints, which makes it impossible to reach a given desired pose for certain configurations without losing essential visual information from the camera field of view. Previous work has demonstrated the effectiveness of deep reinforcement learning in addressing various vision-based robotics tasks. In light of this, we propose a framework that integrates deep recurrent policies, intrinsic motivation, and a novel auxiliary task that leverages the interaction matrix, the core of classical visual servoing approaches, to address the problem of vision-based control of nonholonomic robotic systems. Firstly, we analyze the influence of the nonholonomic constraints on control policy learning. Subsequently, we validate and evaluate our approach in both simulated and real-world environments. Our approach exhibits an emergent control behavior that enables the robot to accurately attain the desired pose while maintaining the desired visual content within the camera’s field of view. The proposed method outperforms the state-of-the-art approaches, demonstrating its effectiveness, robustness, and accuracy.
