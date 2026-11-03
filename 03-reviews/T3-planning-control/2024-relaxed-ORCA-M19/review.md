# Relaxing the Limitations of the Optimal Reciprocal Collision Avoidance Algorithm for Mobile Robots in Crowds

## Metadata

| Field | Value |
|---|---|
| ID | M19 |
| Title | Relaxing the Limitations of the Optimal Reciprocal Collision Avoidance Algorithm for Mobile Robots in Crowds |
| Authors | Zhihao Liu, Wenjie Na, Chenpeng Yao, Chengju Liu, and Qijun Chen |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 6, pp. 5520-5527 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3390561](https://doi.org/10.1109/lra.2024.3390561) |
| Official URL | https://ieeexplore.ieee.org/document/10504974/ |
| Theme folder | T3-planning-control |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T3-planning-control/2024-relaxed-ORCA-M19/paper.pdf` and `02-fulltext/T3-planning-control/2024-relaxed-ORCA-M19/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2024-relaxed-ORCA-M19/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, dataset-playback, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: unnamed wheeled mobile robot with Intel RealSense D435i
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Intel RealSense D435i RGB-D camera (pedestrian tracking and speed estimation)
- compute: training on i7-8700 with GTX 1070; real runs on a laptop with i7-10875H and RTX 2070; timing not recorded in the legacy extraction
- compute_location: not-reported
- summary_result: In Gazebo crowds of 8 and 20 pedestrians over 1000 test cases, the method reduced collision probability and ORCA no-solution counts against ORCA baselines; the legacy extraction records no values.
- summary_limitation: No limitation is stated by the authors in the legacy extraction; real crowd tests are short indoor encounters and the mobile base is not named.
- survey_included: yes
- verification_level: light

## Problem

ORCA assumes that each agent takes half the responsibility for avoiding a
collision. This fails when pedestrians do not run ORCA. Multi-constraint ORCA
can be unsolvable, and tuning only the responsibility leads to local optima.

## Mechanism

ORCA is collapsed to a single collision-avoidance constraint. A PPO policy
with self-attention over nearby pedestrians jointly outputs the direction of
the escape velocity and the avoidance responsibility; an auxiliary head
predicts the ORCA velocity. Training pedestrians mix Social Force (80%) and
constant-speed (20%) policies.

## Baselines and controls

ORCA-based baselines, including PORCA and VR-ORCA, are named in the legacy
extraction. The full baseline list is not recorded in the legacy extraction;
not verified.

## Platform and setup

ROS and Gazebo simulation in invisible and visible settings with 8 and 20
pedestrians and 1000 test cases. Real indoor runs track pedestrians with an
Intel RealSense D435i. A quantitative sim-to-real test without retraining
uses the ETH Hotel dataset (200 runs). The chassis make and model are not
stated.

## Evidence type and transfer

The quantitative comparison comes from Gazebo and from ETH Hotel trajectory
replay. The real indoor runs drive the robot with the policy. The legacy
extraction does not record numeric hardware metrics, and it does not say
whether the laptop was carried on the robot, so compute_location is
not-reported.

## Sensors

Intel RealSense D435i RGB-D camera for pedestrian tracking and speed
estimation.

## Compute and latency

Training ran on an i7-8700 with a GTX 1070. The real runs used a laptop with
an i7-10875H and an RTX 2070. Timing is not recorded in the legacy
extraction.

## Key quantitative results

- Simulation covers 8 and 20 pedestrians in invisible and visible settings with 1000 test cases (p. 6).
- Sim-to-real test on ETH Hotel without additional training: 200 runs (p. 8).
- The method reduces collision probability and the average number of ORCA no-solution cases against the baselines, as stated in the abstract; the legacy extraction records no values (p. 1).

## Stated limitations

Not recorded in the legacy extraction; not verified.

## Transfer conditions

Real tests depend on a dedicated RGB-D pedestrian tracker and a laptop with
an RTX 2070; the mobile base is never identified. The crowd tests are short
indoor encounters. ORCA, PORCA, and VR-ORCA still fail when the reciprocity
assumption is false, which is the motivation for the method. These are the
legacy reviewer's observations.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. III-C, p. 3 | "Because ORCA cannot guarantee that pedestrians in the environment will follow ORCA and take half the responsibilities to change their velocities." |
| C3 | direct-support | moderate | Sec. V-E, p. 8 | "Additionally, we use ETH Hotel dataset [22] for quantitative experiments of sim-to-real without additional training." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V-E, p. 8 | "A laptop with i7-10875H and RTX2070 is used to run our method." |

## Page-cited excerpts

- **p. 3, Sec. III-C.** "2) Limitation 2: The reciprocal assumption of ORCA is not valid for the robot in crowds. Because ORCA cannot guarantee that pedestrians in the environment will follow ORCA and take half the responsibilities to change their velocities."
  The motivating failure of ORCA in human crowds.
- **p. 8, Sec. V-E.** "An Intel RealSense D435i RGBD depth camera mounted on the robot is used to achieve tracking and speed estimation of pedestrians."
  The hardware runs need RGB-D pedestrian tracking.
- **p. 8, Sec. V-E.** "A laptop with i7-10875H and RTX2070 is used to run our method."
  Inference uses a discrete-GPU laptop.

## Survey-usable statements

### Supported

- Learning both the escape-velocity direction and the responsibility of a single ORCA constraint reduced collision probability and ORCA no-solution counts in Gazebo crowds (numbers from a light review; re-check before citing).
- The policy was tested on ETH Hotel replay without retraining (200 runs).

### Not supported

- Quantitative hardware results: the legacy extraction records only qualitative real indoor runs.
- Onboard embedded deployment: the method ran on a laptop with an RTX 2070.

## Verification log

- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); all legacy quotes found; legacy limitations (short indoor encounters, baseline failures, sim-to-real remark) moved to Transfer conditions as reviewer observations; GTX 1070 not found by text search
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

The Optimal Reciprocal Collision Avoidance (ORCA) algorithm is widely used for modeling agents in collision avoidance scenarios. However, suffering from limitations such as the improper reciprocal assumption that each agent is supposed to take half the responsibility for collision avoidance, the performance of ORCAbased mobile robots in crowds is not ideal. In this letter, to relax these limitations, we firstly simplify the planning process of ORCA from the principle horizon to solve ORCA being unsolvable in some cases. Then the escape velocity and collision avoidance responsibility are explored simultaneously based on deep reinforcement learning (DRL) to solve the limitation of local optimum caused by only exploring the responsibility in other works. We compare our method with baselines in environments with different numbers of pedestrians and test in different real-world scenarios. The results show that our method is beneficial in reducing the collision probability and the average number of ORCA no solutions for the robot in crowds.
