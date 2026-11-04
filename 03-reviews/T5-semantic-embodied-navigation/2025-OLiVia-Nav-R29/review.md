# OLiVia-Nav: An Online Lifelong Vision Language Approach for Mobile Robot Social Navigation

## Metadata

| Field | Value |
|---|---|
| ID | R29 |
| Title | OLiVia-Nav: An Online Lifelong Vision Language Approach for Mobile Robot Social Navigation |
| Authors | Siddarth Narasimhan, Aaron Hao Tan, Daniel Choi, and Goldie Nejat |
| Venue | 2025 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2025 |
| Type | conference |
| DOI | [10.1109/icra55743.2025.11128004](https://doi.org/10.1109/icra55743.2025.11128004) |
| Official URL | https://ieeexplore.ieee.org/document/11128004/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-OLiVia-Nav-R29/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-OLiVia-Nav-R29/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2025-OLiVia-Nav-R29/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: few-trials
- platform_class: skid-steer
- platform: Clearpath Jackal in real-world social navigation scenarios (p. 5).
- boundary_platform: no
- degradation: dynamic-objects, model-error
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task
- sensors: Onboard RGB camera and 3D LiDAR (p. 2)
- compute: Training on an NVIDIA H100 (p. 5); deployment compute not inspected.
- compute_location: not-reported
- summary_result: Distilled social-context embeddings track expert trajectories more closely and shorten personal-space violations versus DRL and VLM methods (p. 6).
- summary_limitation: Larger crowded environments remain to be investigated (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Large VLMs reason about social context but respond too slowly for reactive social navigation.

## Mechanism

SC-CLIP distills large-VLM social reasoning into lightweight image and text encoders; a multi-head-attention trajectory planner trained by imitation generates candidates; a selection module chooses one; encoders are updated online for new social scenarios (pp. 2-5).

## Baselines and controls

State-of-the-art DRL and VLM social navigation methods including VLM-Social-Nav (pp. 5-6).

## Platform and setup

Real-world comparison and ablation studies with before/after lifelong-update evaluation (pp. 5-6). Clearpath Jackal in real-world social navigation scenarios (p. 5).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Hardware trials measured mainly against expert trajectories.

## Sensors

Onboard RGB camera and 3D LiDAR (p. 2).

## Compute and latency

Training on an NVIDIA H100 (p. 5); deployment compute not inspected.

## Key quantitative results

- OLiVia-Nav reports lower MSE and Hausdorff loss against expert trajectories than the compared methods (p. 6).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Future work will investigate performance in larger environments with crowds (p. 6).

## Transfer conditions

Online updates require monitoring for forgetting and unsafe adaptation; collision metrics are limited.

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

- **p. 2, Sec. II-D.** "LLM and VLM methods [23], [24] are limited by their slow response times resulting in poor social navigation performance, as they cannot adapt to fast human movements leading to collisions [32]."
  Motivates distillation for response time.
- **p. 6, Sec. VII.** "Future work will investigate the performance of the OLiVia-Nav in larger environments with crowds."
  Scope limit.

## Survey-usable statements

### Supported

- Distilling VLM social reasoning into lightweight encoders addresses query latency on a wheeled robot.

### Not supported

- Online lifelong updates are not shown to be safe under distribution shift.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 5, 6; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Service robots in human-centered environments such as hospitals, office buildings, and long-term care homes need to navigate while adhering to social norms to ensure the safety and comfortability of the people they are sharing the space with. Furthermore, they need to adapt to new social scenarios that can arise during robot navigation. In this paper, we present a novel Online Lifelong Vision Language architecture, OLiVia-Nav, which uniquely integrates vision-language models (VLMs) with an online lifelong learning framework for robot social navigation. We introduce a unique distillation approach, Social Context Contrastive Language Image Pre-training (SC-CLIP), to transfer the social reasoning capabilities of large VLMs to a lightweight VLM, in order for OLiVia-Nav to directly encode social and environment context during robot navigation. These encoded embeddings are used to generate and select robot social compliant trajectories. The lifelong learning capabilities of SC-CLIP enable OLiVia-Nav to update the robot trajectory planning overtime as new social scenarios are encountered. We conducted extensive real-world experiments in diverse social navigation scenarios. The results showed that OLiVia-Nav outperformed existing state-of-the-art DRL and VLM methods in terms of mean squared error, Hausdorff loss, and personal space violation duration. Ablation studies also verified the design choices for OLiVia-Nav.
