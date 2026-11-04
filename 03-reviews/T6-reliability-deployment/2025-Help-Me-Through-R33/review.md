# Help Me Through: Imitation Learning Based Active View Planning to Avoid SLAM Tracking Failures

## Metadata

| Field | Value |
|---|---|
| ID | R33 |
| Title | Help Me Through: Imitation Learning Based Active View Planning to Avoid SLAM Tracking Failures |
| Authors | Kanwal Naveed, Wajahat Hussain, Irfan Hussain, Donghwan Lee, and Muhammad Latif Anjum |
| Venue | IEEE Transactions on Robotics |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3582817](https://doi.org/10.1109/tro.2025.3582817) |
| Official URL | https://ieeexplore.ieee.org/document/11049022/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-Help-Me-Through-R33/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Help-Me-Through-R33/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-Help-Me-Through-R33/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: localization-mapping
- evidence_type: online-hardware
- evidence_all: online-hardware, simulation
- protocol_caveats: joystick-driving
- platform_class: differential-drive
- platform: Simulated indoor transitions for training and evaluation; a PeopleBot on a two-wheeled differential-drive Pioneer 3-DX with a laptop webcam in live mode (p. 14).
- boundary_platform: no
- degradation: visual-degradation
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Monocular camera with ORB-SLAM3 tracking
- compute: Timing analysis in Sec. V-F (p. 13); deployment on a connected laptop (p. 14).
- compute_location: offboard-local
- summary_result: Human-supervised imitation learning lets active view planning cross room transitions without visual tracking failure where deep RL fails, after about 50 h of supervision (p. 1).
- summary_limitation: Substantial human supervision is required; in the physical test the robot is teleoperated for path planning and obstacle avoidance (pp. 1, 14).
- survey_included: yes
- verification_level: light

## Problem

Visual SLAM loses tracking at doors, texture-less walls and lobbies, and RL view planners fail to learn these transitions.

## Mechanism

A DQN is first trained from human demonstrations of camera moves that preserve tracking, then optionally fine-tuned online with a new reward; the deployed agent recommends viewpoint actions (pp. 4-9).

## Baselines and controls

Deep RL active view planning (DI-SLAM) and offline-only versus fine-tuned training (pp. 10-13).

## Platform and setup

Large-scale simulated evaluation and a live real-world demonstration (pp. 13-14). Simulated indoor transitions for training and evaluation; a PeopleBot on a two-wheeled differential-drive Pioneer 3-DX with a laptop webcam in live mode (p. 14).

## Evidence type and transfer

Strongest coded setting: `online-hardware`. The physical test runs the agent online on live images, but a human teleoperates path planning and obstacle avoidance.

## Sensors

Monocular camera with ORB-SLAM3 tracking.

## Compute and latency

Timing analysis in Sec. V-F (p. 13); deployment on a connected laptop (p. 14).

## Key quantitative results

- Roughly 20 h of supervision plus 45 h of unsupervised fine-tuning gives encouraging results (p. 1).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Long human supervision is required for transitions (p. 1).
- The real robot is teleoperated for path planning and obstacle avoidance (p. 14).

## Transfer conditions

Strafe actions in simulation do not exist on a nonholonomic base; recommendations must map to feasible wheeled motions.

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

- **p. 14, Sec. V-G.** "The robot is tele-operated for path planning and obstacle avoidance."
  Limits the hardware evidence.
- **p. 4, Sec. II.** "However, failures across transitions have largely eluded attention."
  Problem statement.

## Survey-usable statements

### Supported

- Learning view-planning actions from human demonstrations reduces predictable visual tracking failures in simulation.

### Not supported

- Autonomous navigation with the policy is not demonstrated on hardware.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 5, 13, 14, 15; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Large-scale evaluation of state-of-the-art visual simultaneous localization and mapping (SLAM) has shown that its tracking performance degrades considerably if the camera view is not adjusted to avoid the low-texture areas. Deep reinforcement learning (RL)-based approaches have been proposed to improve the robustness of visual tracking in such unsupervised settings. Our extensive analysis reveals the fundamental limitations of RL-based active view planning, especially in transition scenarios (entering/exiting the room, texture-less walls, and lobbies). In challenging transition scenarios, the agent generally remains unable to cross the transition during training, limiting its ability to learn the maneuver. We propose human-supervised RL training (imitation learning) and achieve significantly improved performance after $\sim50$ h of supervised training. To reduce longer human supervision requirements, we also explore fine-tuning our network with an online learning policy. Here, we use limited human-supervised training ($\sim20$ h), and fine-tune the network with unsupervised training ($\sim45$ h), obtaining encouraging results. We also release our multimodel, human supervised training dataset. The dataset contains challenging and diverse transition scenarios and can aid the development of imitation learning policies for consistent visual tracking. We also release our implementation.
