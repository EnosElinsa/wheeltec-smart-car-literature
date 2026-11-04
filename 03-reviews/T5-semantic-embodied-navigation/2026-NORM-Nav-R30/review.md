# NORM-Nav: Zero-Shot Mobile Robot Navigation with Natural Language Behavioral Constraints

## Metadata

| Field | Value |
|---|---|
| ID | R30 |
| Title | NORM-Nav: Zero-Shot Mobile Robot Navigation with Natural Language Behavioral Constraints |
| Authors | Dongjie Huo, Junhui Wang, Chao Gao, Yan Qiao, Dong Zhang, and Guyue Zhou |
| Venue | 2026 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2026 |
| Type | conference |
| DOI | [10.1109/icra57385.2026.11696526](https://doi.org/10.1109/icra57385.2026.11696526) |
| Official URL | https://ieeexplore.ieee.org/document/11696526/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-NORM-Nav-R30/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-NORM-Nav-R30/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2026-NORM-Nav-R30/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware
- platform_class: differential-drive
- platform: Simulated four-wheeled differential-drive robot and a physical SCOUT 2.0 with Livox MID-360 and RealSense D455 (pp. 5-6).
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: LiDAR and RGB-D camera
- compute: Onboard AMD R9-7945HX CPU with RTX 4060 GPU (p. 6).
- compute_location: onboard
- summary_result: Language-derived geometric, semantic, directional and velocity costmap layers raise task success and align paths with human references in simulation; hardware tests demonstrate representative behaviors (pp. 6-7).
- summary_limitation: No limitation is stated in the inspected passages; hardware evidence consists of representative demonstrations (p. 7).
- survey_included: yes
- verification_level: light

## Problem

Costmap planners ignore behavioral conventions expressed in natural language.

## Mechanism

An LLM parses instructions into structured constraints; vision-LiDAR perception grounds them; multi-layer costmaps encode semantic, directional and speed constraints and are fused for standard grid planners (pp. 3-5).

## Baselines and controls

BehAV, InstructNav and INF (p. 6).

## Platform and setup

Simulated tasks with region following, avoidance and traversable obstacles, plus real-world demonstrations (pp. 5-7). Simulated four-wheeled differential-drive robot and a physical SCOUT 2.0 with Livox MID-360 and RealSense D455 (pp. 5-6).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Quantitative comparisons are simulated; hardware runs are demonstrations.

## Sensors

LiDAR and RGB-D camera.

## Compute and latency

Onboard AMD R9-7945HX CPU with RTX 4060 GPU (p. 6).

## Key quantitative results

- InstructNav fails with large landmarks such as crosswalks, and BehAV and InstructNav fail to traverse regions misclassified as obstacles (p. 6).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- No limitation statement was found in the inspected passages.

## Transfer conditions

Grounding errors propagate into costs; LLM parsing latency was not inspected.

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

- **p. 6, Sec. V-A.** "2) Real-world Platform: For physical validation, we employ a SCOUT 2.0 differential-drive mobile robot (Fig. 5)."
  Platform and drive type.
- **p. 6, Sec. V-B.** "In the traversable-obstacle task, BehAV and InstructNav fail to traverse regions misclassified as obstacles."
  Baseline failure mode.

## Survey-usable statements

### Supported

- Language constraints can enter standard costmaps as directional and speed layers.

### Not supported

- Hardware success rates are not reported.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Mobile robots operating in human-centered environments must generate not only collision-free paths but also trajectories that follow local behavioral conventions. Conventional costmap-based navigation emphasizes geometric feasibility and often overlooks such requirements, which can result in socially inappropriate behaviors. This paper presents NORM-Nav, a zero-shot framework that integrates natural language behavioral constraints into costmap-based planning. An LLM parses each instruction into structured constraints and grounds them using real-time vision-LiDAR perception. These constraints are encoded as multi-layer costmaps that represent geometric, semantic, directional, and velocity cues and are directly compatible with standard grid-based planners. Simulation and real-world experiments indicate that NORM-Nav improves task success rates and produces trajectories closer to human references than representative baselines. The project website is available at https://ei-nav.github.io/NO RM-Nav.
