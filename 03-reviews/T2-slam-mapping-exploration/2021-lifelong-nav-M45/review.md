# A Lifelong Learning Approach to Mobile Robot Navigation

## Metadata

| Field | Value |
|---|---|
| ID | M45 |
| Title | A Lifelong Learning Approach to Mobile Robot Navigation |
| Authors | Bo Liu, Xuesu Xiao, and Peter Stone |
| Venue | IEEE Robotics and Automation Letters, vol. 6, no. 2, pp. 1090-1096 |
| Year | 2021 |
| Type | journal |
| DOI | [10.1109/lra.2021.3056373](https://doi.org/10.1109/lra.2021.3056373) |
| Official URL | https://ieeexplore.ieee.org/document/9345478/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T2-slam-mapping-exploration/2021-lifelong-nav-M45/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2021-lifelong-nav-M45/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2021-lifelong-nav-M45/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: skid-steer
- platform: Clearpath Jackal (text: "four-wheeled differential-drive unmanned ground vehicle", p. 4)
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Velodyne 3D LiDAR converted to a 360-degree 2095-dimensional scan (physical); SICK LMS111 2D LiDAR (simulation)
- compute: Intel Core i5-4570TE onboard; each model trains in under two minutes; at most 600 stored data points
- compute_location: onboard
- summary_result: Over 60 physical trials in three static indoor environments, LLfN reduced traversal time and recoveries versus DWA and avoided the forgetting of sequential training (Table I).
- summary_limitation: The authors state that LLfN fails to learn when the base policy is incompetent everywhere, and leave dynamic obstacles and experience prioritization to future work.
- survey_included: yes
- verification_level: light

## Problem

Classical local planners, such as DWA in ROS `move_base`, do not improve with
experience and may repeat recovery behaviors in the same layout.
Learning-based navigators trained offline need large memory and compute, and
they forget earlier environments (catastrophic forgetting) when the robot
meets a sequence of scenes.

## Mechanism

Lifelong Learning for Navigation (LLfN) keeps a fixed Dijkstra global
planner in `move_base` and uses DWA as the initial local policy. A small MLP
maps the LiDAR scan and a local goal 1 m ahead to linear and angular
velocity. A heuristic scorer flags DWA recoveries (slowing, spinning, backing
up) as suboptimal. Similar successful state-action pairs are drawn from a
300-step streaming buffer into a 300-sample episodic memory. Gradient
Episodic Memory (GEM) projects the updates so that the loss on earlier
environments does not increase. In physical training, the environment ID is
labeled manually; deployment uses one policy per traversal.

## Baselines and controls

The comparators are the initial DWA policy and sequential training without
the forgetting constraint.

## Platform and setup

Simulation used a Clearpath Jackal with a SICK LMS111 (270 degrees,
720-dimensional scan) in three static layouts (dense obstacles, a narrow
passage, and a sharp turn through a door), with 198 evaluation trials. The
physical tests used the same Jackal with a Velodyne LiDAR converted to a
360-degree 2095-dimensional scan, all computation onboard an Intel Core
i5-4570TE, and three concatenated static indoor environments, for 60 trials.

## Evidence type and transfer

The physical tests are closed-loop and fully onboard. The layouts are
static; there are no moving pedestrians. The environment was labeled
manually during training.

## Sensors

A Velodyne 3D LiDAR flattened to a 2D scan on the physical robot; a SICK
LMS111 2D laser scanner in simulation.

## Compute and latency

All computation ran onboard on an Intel Core i5-4570TE CPU. Training each
model took less than two minutes on the robot CPU. At most 600 state-action
data points are stored. No offboard trainer is used.

## Key quantitative results

- Simulation: 198 evaluation trials across three static layouts (p. 5).
- Physical: 60 trials; LLfN reduced traversal time and recoveries versus DWA and avoided the forgetting of sequential training; values not recorded in the legacy extraction (p. 6, Table I).
- Training time: less than two minutes per model on the onboard CPU (p. 6).
- Memory: at most 600 stored data points onboard (p. 5).
- Scan size: 720-dimensional (simulation) and 2095-dimensional (physical) (p. 5).

## Stated limitations

- When the base policy is incompetent everywhere, LLfN fails to learn; active exploration is suggested as future work (p. 6).
- The scoring function is a heuristic specific to the initial policy (DWA); a learnable value function is future work (p. 6).
- Experience prioritization under a limited buffer and extension to dynamic obstacles are future work (p. 6).

## Transfer conditions

The method needs a working base planner whose recoveries can be scored, a
LiDAR scan, and a `move_base`-style global planner. Environment IDs were
labeled by a human during training. The tests used static layouts only.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | weak | Sec. VI, p. 6 | "Other interesting directions include investigating better methods to prioritize experiences for updating the online buffers with a limited budget and extending LLfN to address dynamic obstacles." |
| C3 | direct-support | weak | Sec. VI, p. 6 | "The entire LLfN is also implemented and tested on limited computational resources onboard a physical robot and operates in real time without requiring any off board computation." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V-C, p. 6 | "For training, we manually label the current environment for the learner." |

## Page-cited excerpts

- **p. 6, Sec. VI.** "Other interesting directions include investigating better methods to prioritize experiences for updating the online buffers with a limited budget and extending LLfN to address dynamic obstacles."
  Dynamic obstacles are left as future work.
- **p. 6, Sec. VI.** "The entire LLfN is also implemented and tested on limited computational resources onboard a physical robot and operates in real time without requiring any off board computation."
  Learning runs under an explicit onboard compute budget.
- **p. 6, Sec. V-C.** "For training, we manually label the current environment for the learner."
  Physical training relies on human environment labels.

## Survey-usable statements

### Supported

- Lifelong learning on top of DWA, with GEM against forgetting, ran fully onboard a Jackal and reduced traversal time and recoveries in three static indoor environments (light review; take values from Table I before citing).
- Each model trained in under two minutes on the robot CPU with at most 600 stored data points.

### Not supported

- LLfN handles moving pedestrians: the physical layouts were static and dynamic obstacles are future work.
- LLfN identifies the environment by itself: environment IDs were labeled manually during training.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); the legacy card had no verbatim quotes, so excerpts were taken from the conclusion and from Sec. V-C with --find
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

This letter presents a self-improving lifelong learning framework for a mobile robot navigating in different environments. Classical static navigation methods require environment-specific in-situ system adjustment, e.g., from human experts, or may repeat their mistakes regardless of how many times they have navigated in the same environment. Having the potential to improve with experience, learning-based navigation is highly dependent on access to training resources, e.g., sufficient memory and fast computation, and is prone to forgetting previously learned capability, especially when facing different environments. In this work, we propose Lifelong Learning for Navigation (LLfN) which (1) improves a mobile robot's navigation behavior purely based on its own experience, and (2) retains the robot's capability to navigate in previous environments after learning in new ones. LLfN is implemented and tested entirely onboard a physical robot with a limited memory and computation budget.
