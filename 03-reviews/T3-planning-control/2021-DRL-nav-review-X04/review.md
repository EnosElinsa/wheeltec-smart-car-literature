# Deep reinforcement learning based mobile robot navigation: A review

## Metadata

| Field | Value |
|---|---|
| ID | X04 |
| Title | Deep reinforcement learning based mobile robot navigation: A review |
| Authors | Kai Zhu and Tao Zhang |
| Venue | Tsinghua Science and Technology, vol. 26, no. 5, pp. 674-691 |
| Year | 2021 |
| Type | journal |
| DOI | [10.26599/tst.2021.9010012](https://doi.org/10.26599/tst.2021.9010012) |
| Official URL | https://doi.org/10.26599/tst.2021.9010012 |
| Theme folder | T3-planning-control |
| Batch | supplemental |
| Local files | `01-papers/T3-planning-control/2021-DRL-nav-review-X04/paper.pdf` and `02-fulltext/T3-planning-control/2021-DRL-nav-review-X04/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2021-DRL-nav-review-X04/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: survey
- evidence_all: survey
- protocol_caveats: none
- platform_class: none
- platform: none (literature review)
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: not applicable (reviewed work uses 2D and 3D LiDAR, RGB, and RGB-D cameras)
- compute: not applicable (literature review)
- compute_location: not-applicable
- summary_result: Literature review that organizes DRL navigation into four scenarios (local obstacle avoidance, indoor, multi-robot, social navigation); it reports no new experiments.
- summary_limitation: DRL navigation converges poorly when the policy space is too large, so agents are trained in specific scenes; deployment usually needs the training sensors.
- survey_included: context
- verification_level: light

## Problem

DRL is widely applied to mobile-robot navigation, but scenario labels
(mapless versus map-based, visual versus coordinate goals) are inconsistent,
and policies trained in one setting often fail to transfer.

## Mechanism

The review organizes DRL navigation around value-based and policy-based
methods (DQN and DDQN, DDPG, PPO) and a shared MDP or POMDP interface (state,
action, reward). It compares four application scenarios: local obstacle
avoidance, indoor navigation, multi-robot navigation, and social navigation.
It catalogs challenges (partial observation, sparse reward, poor
generalization) and reported remedies (frame stacking and RNN or LSTM memory;
reward shaping, auxiliary tasks, and curricula; domain randomization and
reduced state spaces such as sparse laser input).

## Baselines and controls

Not applicable: literature review with no experiments of its own.

## Platform and setup

Literature synthesis, not a new robot trial. The scenario comparison is
summarized in Table 1 and Fig. 4. Cited sim-to-real cases include a
sparse-laser DDPG policy transferred without fine-tuning and depth from a
monocular camera converted for a policy trained in 2D LiDAR simulation.

## Evidence type and transfer

The paper is a review; its statements summarize cited work. The four-scenario
taxonomy is background for DRL navigation, not evidence that the six theme
folders of this library are exhaustive.

## Sensors

Not applicable. The reviewed work uses 2D and 3D LiDAR, RGB cameras, and
RGB-D or depth cameras.

## Compute and latency

Not applicable (literature review).

## Key quantitative results

- The review compares four application scenarios in Table 1 and Fig. 4; it reports no new quantitative results (p. 7, Table 1).

## Stated limitations

- If the DRL navigation policy space is too large, training is hard to converge, so agents learn in a specific scene and are then generalized to similar scenes (p. 7).
- Most DRL navigation applications must be deployed with the same sensors as in training, and the system may fail under different hardware (p. 9).
- Training in a physical environment is time-consuming and dangerous, so agents are trained in simulation and transferred, and poor generalization is a challenge (p. 14).
- Sparse rewards aggravate data inefficiency, and manually shaped rewards can overfit a scene; pages not recorded in the legacy extraction.

## Transfer conditions

The review is background on learning-based navigation for the survey. Its
challenges (sensor dependence, sim-to-real transfer, sparse rewards) apply to
any learned local planner considered for a wheeled robot.

## Code and data

Not applicable (literature review).

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | partial-support | moderate | Abstract, p. 1 | "Then we systematically compare and analyze the relationship and differences between four typical application scenarios: local obstacle avoidance, indoor navigation, multi-robot navigation, and social navigation." |
| C2 | unset | n/a | | |
| C3 | direct-support | strong | Sec. 5.3.1, p. 14 | "Because training in a physical environment is very time-consuming and dangerous, researchers typically train the agent in a simulation environment and then transfer it to the entity environment." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 1, Abstract.** "In this paper, we review DRL methods and DRL-based navigation frameworks."
  The paper is a review.
- **p. 14, Sec. 5.3.1.** "Poor generalization is another challenge in DRL-based navigation. Because training in a physical environment is very time-consuming and dangerous, researchers typically train the agent in a simulation environment and then transfer it to the entity environment."
  Physical training cost and sim-to-real transfer are stated deployment barriers.
- **p. 9, Sec. 4.1.4.** "In most studies, DRL-based navigation applications must be deployed using the same sensors as those used in the training environment."
  Learned policies depend on the training sensor configuration.

## Survey-usable statements

### Supported

- DRL navigation work is commonly split into local obstacle avoidance, indoor, multi-robot, and social navigation (context citation).
- Reviews of DRL navigation name sim-to-real transfer, sparse rewards, and sensor dependence as deployment barriers.

### Not supported

- Any quantitative comparison of DRL methods: the review reports none of its own.
- Support for the library's six-theme frame: the review covers four DRL-navigation scenarios only.

## Verification log

- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); legacy quotes found and kept; legacy C1 relation "background" is not in the vocabulary and was recoded partial-support (four learning-navigation subareas only); legacy limitations located on pp. 7, 9, and 14
- Legacy extraction: automated reviewer (codex), supplemental batch.

## Original abstract

Navigation is a fundamental problem of mobile robots, for which Deep Reinforcement Learning (DRL) has received significant attention because of its strong representation and experience learning abilities. There is a growing trend of applying DRL to mobile robot navigation. In this paper, we review DRL methods and DRL-based navigation frameworks. Then we systematically compare and analyze the relationship and differences between four typical application scenarios: local obstacle avoidance, indoor navigation, multi-robot navigation, and social navigation. Next, we describe the development of DRL-based navigation. Last, we discuss the challenges and some possible solutions regarding DRL-based navigation.
