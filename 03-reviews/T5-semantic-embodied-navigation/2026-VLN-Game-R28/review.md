# VLN-Game: Vision-Language Equilibrium Search for Zero-Shot Semantic Navigation

## Metadata

| Field | Value |
|---|---|
| ID | R28 |
| Title | VLN-Game: Vision-Language Equilibrium Search for Zero-Shot Semantic Navigation |
| Authors | Bangguo Yu, Yuzhen Liu, Lei Han, Hamidreza Kasaei, Tingguang Li, and Ming Cao |
| Venue | IEEE Transactions on Robotics |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tro.2026.3677047](https://doi.org/10.1109/tro.2026.3677047) |
| Official URL | https://ieeexplore.ieee.org/document/11455365/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-VLN-Game-R28/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-VLN-Game-R28/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2026-VLN-Game-R28/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware, offboard-compute
- platform_class: skid-steer
- platform: Habitat HM3D object-goal and language-goal tasks; Jackal with RealSense D455 and Ouster LiDAR for real-world deployment (pp. 9, 13).
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: RGB-D camera and odometry; LiDAR on the physical robot
- compute: Perception and navigation modules on a computer with an RTX 3060 (p. 13).
- compute_location: not-reported
- summary_result: A 3D object-centric map with game-theoretic VLM disambiguation improves success and efficiency on HM3D object- and language-goal navigation (p. 13).
- summary_limitation: Multi-view target identification and CLIP detection limits constrain navigation performance (p. 11).
- survey_included: yes
- verification_level: light

## Problem

Object-goal navigators ignore attributes and spatial relations in language descriptions.

## Mechanism

Pretrained visual-language features are fused into a 3D object-centric map; frontier exploration selects promising areas; a game-theoretic VLM equilibrium search chooses which candidate matches the description (pp. 4-8).

## Baselines and controls

Zero-shot and learned object-goal and language-goal navigators on HM3D (pp. 8-12).

## Platform and setup

Habitat simulation with RGB-D, odometry and language queries; real-world demonstrations (pp. 9, 13). Habitat HM3D object-goal and language-goal tasks; Jackal with RealSense D455 and Ouster LiDAR for real-world deployment (pp. 9, 13).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Quantitative results are simulated; the hardware section is a deployment demonstration.

## Sensors

RGB-D camera and odometry; LiDAR on the physical robot.

## Compute and latency

Perception and navigation modules on a computer with an RTX 3060 (p. 13).

## Key quantitative results

- Quantitative success rates come from HM3D simulation; the inspected hardware section reports no success rate (pp. 9, 13).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Identifying open-vocabulary targets from multiple views remains challenging (p. 11).
- CLIP limitations constrain overall navigation performance (p. 11).

## Transfer conditions

Simulation uses ideal odometry inputs; physical execution depends on the robot navigation stack.

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

- **p. 13, Sec. IV-B.** "We deployed the agents in the real world and evaluated them on the Jackal Robot platform, which is equipped with a RealSense D455 RGB-D camera and an Ouster lidar, using ROS [80]."
  Hardware setup.
- **p. 11, Sec. IV-A.** "Second, the CLIP model has limitations in detecting all open-vocabulary targets in our tasks, which constrains the overall navigation performance of the robot."
  Author-stated limit.

## Survey-usable statements

### Supported

- Game-theoretic VLM disambiguation improves simulated language-goal navigation.

### Not supported

- Hardware performance is not quantified.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 9, 11, 13; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Following human instructions to explore and search for a specified target in an unfamiliar environment is a crucial skill for mobile service robots. Most of the previous works on object goal navigation have typically focused on a single input modality as the target, which may lead to limited consideration of language descriptions containing detailed attributes and spatial relationships. To address this limitation, we propose VLN-Game, a novel zero-shot framework for visual target navigation that can process object names and descriptive language targets effectively. To be more precise, our approach constructs a 3-D object-centric spatial map by integrating pretrained visual-language features with a 3-D reconstruction of the physical environment. Then, the framework identifies the most promising areas to explore in search of potential target candidates. A game-theoretic vision-language model is employed to determine which target best matches the given language description. Experiments conducted on the Habitat-Matterport 3-D dataset demonstrate that the proposed framework achieves state-of-the-art performance in both object goal navigation and language-based navigation tasks. Moreover, we show that VLN-Game can be easily deployed on real-world robots. The success of VLN-Game highlights the promising potential of using game-theoretic methods with compact vision-language models to advance decision-making capabilities in robotic systems.
