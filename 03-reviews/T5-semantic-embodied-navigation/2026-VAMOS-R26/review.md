# VAMOS: A Hierarchical Vision-Language-Action Model for Capability-Modulated and Steerable Navigation

## Metadata

| Field | Value |
|---|---|
| ID | R26 |
| Title | VAMOS: A Hierarchical Vision-Language-Action Model for Capability-Modulated and Steerable Navigation |
| Authors | Mateo Guaman Castro, Sidharth Rajagopal, Daniel Gorbatov, Matt Schmittle, Rohan Baijal, Octi Zhang, Rosario Scalise, Sidharth Talia, Emma Romig, Celso de Melo, Byron Boots, and Abhishek Gupta |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3734870](https://doi.org/10.1109/lra.2026.3734870) |
| Official URL | https://ieeexplore.ieee.org/document/11692608/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-VAMOS-R26/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-VAMOS-R26/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2026-VAMOS-R26/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Boston Dynamics Spot and the wheeled UW Hound in six indoor and outdoor environments; affordance models trained in Isaac Lab (pp. 5-6).
- boundary_platform: no
- degradation: terrain, model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: RGB images for the VLM planner; local elevation maps for the affordance model
- compute: Inference at 1 Hz on an RTX 3080 laptop (p. 4).
- compute_location: not-reported
- summary_result: A VLM path planner re-ranked by an embodiment affordance model reaches 90% success over 270 trials, versus 53% for a modular stack and 27% for the best generalist (p. 1).
- summary_limitation: The affordance model reasons only in geometric space (p. 8).
- survey_included: yes
- verification_level: light

## Problem

General navigation policies ignore embodiment-specific capabilities such as stair climbing.

## Mechanism

A fine-tuned VLM proposes candidate paths in image space; a capability-aware affordance function learned in simulation from local elevation maps scores and re-ranks them for each robot (pp. 3-4).

## Baselines and controls

A tuned modular navigation stack, generalist navigation models and ViPlanner (pp. 5-7).

## Platform and setup

Real-world trials across six environments and a cross-embodiment test where only the affordance module changes (pp. 5-6). Boston Dynamics Spot and the wheeled UW Hound in six indoor and outdoor environments; affordance models trained in Isaac Lab (pp. 5-6).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop hardware on legged and wheeled robots.

## Sensors

RGB images for the VLM planner; local elevation maps for the affordance model.

## Compute and latency

Inference at 1 Hz on an RTX 3080 laptop (p. 4).

## Key quantitative results

- Affordance modulation raises Hound success from 60% to 90% while Spot remains at 100% (p. 6, Table III).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The affordance model currently reasons only in geometric space (p. 8).

## Transfer conditions

The wheeled robot benefits through an affordance model trained for its own controller; semantic traversability is not modeled.

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

- **p. 6, Sec. IV-C.** "We use the same high-level planner for both Spot and Hound robots, and we swap only the embodiment-specific affordance module."
  Cross-embodiment design.
- **p. 8, Sec. V.** "While our affordance model currently only reasons in geometric space, future work could focus on adding embodiment-specific semantic reasoning about traversability."
  Author-stated limit.

## Survey-usable statements

### Supported

- An embodiment-specific feasibility filter can reject infeasible semantic plans on a wheeled robot.

### Not supported

- Planner latency at 1 Hz is not linked to safety in fast-changing scenes.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 3, 4, 5, 6, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

A fundamental challenge in robot navigation lies in learning policies that generalize across diverse environments while conforming to the unique physical constraints and capabilities of a specific embodiment (e.g., quadrupeds can walk up stairs, but rovers cannot). We propose VAMOS, a hierarchical VLA that decouples semantic planning from embodiment grounding: a generalist planner learns from diverse, open-world data, while a specialist affordance model learns the robot’s physical constraints and capabilities in safe, low-cost simulation. We enabled this separation by carefully designing an interface that lets a high-level planner propose candidate paths directly in image space that the affordance model then evaluates and re-ranks. Across 270 real-world trials spanning six challenging indoor and outdoor environments, VAMOS achieves a 90% average success rate—surpassing both a tuned modular navigation stack (53%) and the best prior generalist (27%). We also show that our hierarchical design enables cross-embodied navigation across legged and wheeled robots and is easily steerable using natural language. Real-world ablations confirm that the specialist model is key to embodiment grounding, enabling a single high-level planner to be deployed across physically distinct wheeled and legged robots. Finally, this model significantly enhances single-robot reliability, achieving $3\times$ higher success rates by rejecting physically infeasible plans.
