# ViNT: A Foundation Model for Visual Navigation

## Metadata

| Field | Value |
|---|---|
| ID | K14 |
| Title | ViNT: A Foundation Model for Visual Navigation |
| Authors | Dhruv Shah, Ajay Sridhar, Nitish Dashora, Kyle Stachowicz, Kevin Black, Noriaki Hirose, and Sergey Levine |
| Venue | Conference on Robot Learning |
| Year | 2023 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v229/shah23a.html |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2023-ViNT-K14/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2023-ViNT-K14/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2023-ViNT-K14/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Five platforms, among them a drone, a Go 1 quadruped, LoCoBot, Vizbot and Jackal; zero-shot exploration is reported for LoCoBot, Go 1, Vizbot and Jackal; drive types not stated (pp. 6-7).
- boundary_platform: no
- degradation: none
- degradation_observed: dynamic-objects
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Monocular camera images; onboard wheel odometry indoors and GPS or satellite imagery outdoors for goal heuristics (pp. 3, 6)
- compute: Training on several multi-GPU workstations (p. 14); deployment hardware not inspected.
- compute_location: not-reported
- summary_result: Trained on over 100 hours from 8 robots, ViNT drives an unseen Go 1 quadruped zero-shot and reaches 80% CARLA success with under one hour of fine-tuning (pp. 4, 7-8).
- summary_limitation: ViNT carries a heavier inference cost than simple convolutional networks, which challenges power-constrained platforms, and it assumes structural similarity across robots (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Visual navigation policies are trained per robot and per task. ViNT is a Transformer-based navigation foundation model meant to be adapted to new robots and goal modalities (pp. 1-2).

## Mechanism

ViNT is trained with an image-goal objective on pooled navigation datasets and predicts relative waypoints in an embodiment-agnostic action space normalized by robot top speed. For exploration, an image diffusion model proposes subgoal images that ViNT grounds and a heuristic scores inside a topological graph; prompt-tuning replaces the goal encoder for GPS waypoints or routing commands (pp. 3-5).

## Baselines and controls

End-to-end imitation and RL policies, a graph-based VIB exploration method, ViNT with random subgoals, GNM, and pre-trained visual representations such as ImageNet and VC-1 (pp. 6-8).

## Platform and setup

Training: over 100 hours of real-world trajectories from existing datasets across 8 robotic platforms (p. 4). Evaluation: coverage and guided exploration in unseen indoor and outdoor environments, zero-shot deployment on four robots, and fine-tuning and adaptation in CARLA (pp. 6-8).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`; the fine-tuning and adaptation tasks run in CARLA simulation. Pedestrians appear during deployment as an observed condition rather than a designed one. The provisional module `semantic-language-navigation` is kept with `traversability-planning-control` as secondary, for the same lineage reason as GNM (K13): ViNT is an image-goal navigation model that accepts other goal modalities through adaptation.

## Sensors

Camera observations and subgoal images; wheel odometry indoors and GPS or passive satellite imagery outdoors provide goal-directed heuristics (p. 6).

## Compute and latency

Training used several workstations with different GPU configurations (p. 14). Deployment hardware was not inspected.

## Key quantitative results

- Training data: over 100 hours from 8 robotic platforms (p. 4).
- Deployed on five robotic platforms, including a drone and a quadruped (p. 6).
- Zero-shot control of a Go 1 quadruped that does not appear in training (p. 7).
- CARLA adaptation: 40% success without fine-tuning and 80% with less than 1 hour of fine-tuning data (p. 8, figure caption).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- ViNT carries a heavier computational burden at inference time, which can challenge power-constrained platforms such as quadcopters (p. 8).
- The Transformer model is significantly costlier at deployment than simpler feedforward convolutional networks (p. 8).
- Cross-robot generalization assumes a degree of structural similarity (p. 8).

## Transfer conditions

The action space hides low-level control behind a robot-specific controller, and goal heuristics need odometry, GPS or satellite images. Inference cost must be checked on the target compute.

## Code and data

Model weights and training code are announced on the project page (pp. 1-2); availability was not checked.

## Version family

CoRL 2023 paper in PMLR volume 229; counted once. It builds on GNM (K13), which it names as closely related, and NoMaD (K16) follows its setup.

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

- **p. 4, Sec. 3.** "The training dataset contains over 100 hours of real-world trajectories sourced entirely from existing datasets, spanning 8 distinct robotic platforms with varying speeds and dynamics."
  Training data scale.
- **p. 8, Sec. 7.** "As with many large-scale models, ViNT carries a heavier computational burden at inference time, which can present a challenge for power-constrained platforms such as quadcopters."
  Author-stated compute limit.
- **p. 6, Sec. 6.1.** "The robots have access to onboard wheel odometry (indoors), GPS coordinates (outdoors), or passive satellite imagery (outdoors), to track their position and use as a goal-directed heuristic."
  Guided exploration depends on external position cues.
- **p. 7, Sec. 6.2.** "Most notably, ViNT successfully generalizes zero-shot to control a Go 1 quadruped, which does not appear during training."
  Cross-embodiment result.

## Survey-usable statements

### Supported

- ViNT, trained on over 100 hours from 8 robots, controlled several robots zero-shot and adapted to new goal modalities with little data.
- Its exploration combines diffusion-proposed subgoals with a topological graph.

### Not supported

- ViNT is not shown to run within the compute of power-constrained platforms; the authors flag this as a limitation.
- The CARLA adaptation results are simulation evidence, not hardware evidence.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 6, 7, 8, 14; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

General-purpose pre-trained models ("foundation models") have enabled practitioners to produce generalizable solutions for individual machine learning problems with datasets that are significantly smaller than those required for learning from scratch. Such models are typically trained on large and diverse datasets with weak supervision, consuming much more training data than is available for any individual downstream application. In this paper, we describe the Visual Navigation Transformer (ViNT), a foundation model that aims to bring the success of general-purpose pre-trained models to vision-based robotic navigation. ViNT is trained with a general goal-reaching objective that can be used with any navigation dataset, and employs a flexible Transformer-based architecture to learn navigational affordances and enable efficient adaptation to a variety of downstream navigational tasks. ViNT is trained on a number of existing navigation datasets, comprising hundreds of hours of robotic navigation from a variety of different robotic platforms, and exhibits positive transfer, outperforming specialist models trained on narrower datasets. ViNT can be augmented with diffusion-based goal proposals to explore novel environments, and can solve kilometer-scale navigation problems when equipped with long-range heuristics. ViNT can also be adapted to novel task specifications with a technique inspired by prompt-tuning, where the goal encoder is replaced by an encoding of another task modality (e.g., GPS waypoints or turn-by-turn directions) embedded into the same space of goal tokens. This flexibility and ability to accommodate a variety of downstream problem domains establish ViNT as an effective foundation model for mobile robotics.
