# NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration

## Metadata

| Field | Value |
|---|---|
| ID | K16 |
| Title | NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration |
| Authors | Ajay Sridhar, Dhruv Shah, Catherine Glossop, and Sergey Levine |
| Venue | 2024 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/icra57147.2024.10610665](https://doi.org/10.1109/icra57147.2024.10610665) |
| Official URL | https://ieeexplore.ieee.org/document/10610665/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2024-NoMaD-K16/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2024-NoMaD-K16/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2024-NoMaD-K16/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: LoCoBot in six indoor and outdoor environments; drive type not stated in the inspected pages (pp. 4-5).
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: RGB observations of the past timesteps and an optional goal image (p. 3)
- compute: The policy runs entirely on the edge with a 15x smaller model than the strongest baseline (p. 5); processor not identified in this reading.
- compute_location: onboard
- summary_result: One goal-masked diffusion policy handles exploration and goal reaching in six real environments, improving over subgoal diffusion by over 25% with 15x fewer parameters (pp. 4-6).
- summary_limitation: Goals are specified only as images, and high-level exploration uses a standard frontier strategy (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Exploration and goal-directed navigation are usually handled by separate models. NoMaD trains one policy that can be conditioned on a goal image or run without one (p. 1).

## Mechanism

A Transformer encoder over past observations uses goal masking to condition on an optional goal image, and a diffusion decoder models multimodal collision-free action sequences; a temporal-distance head supports a topological graph for long-horizon exploration (pp. 3-4).

## Baselines and controls

Masked ViNT, VIB, an autoregressive policy, random subgoals, subgoal diffusion and individual undirected or goal-conditioned policies such as BESO and ViNT (pp. 4-5).

## Platform and setup

Training on the GNM and SACSoN datasets, over 100 hours of real-world trajectories including pedestrian-rich environments (p. 4). Evaluation of exploration and goal-conditioned navigation in 6 indoor and outdoor environments on a LoCoBot (pp. 4-5).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware` on one wheeled platform; trial counts per environment were not inspected. The provisional module `semantic-language-navigation` is kept with `traversability-planning-control` as secondary, for the lineage reason recorded for GNM (K13): NoMaD is an image-goal and exploration policy of the same foundation-model family.

## Sensors

RGB images from the robot camera over past timesteps and an optional goal image (p. 3).

## Compute and latency

The model runs entirely on the edge with a 15x smaller model than the strongest baseline (p. 5). The processor was not identified in this reading.

## Key quantitative results

- Training data: over 100 hours from the GNM and SACSoN datasets (p. 4).
- Evaluation in 6 distinct indoor and outdoor environments (p. 4).
- Over 25% improvement over the state of the art in unseen settings with 15x fewer computational resources (p. 6); Table I success and collision values were not re-read from a rendered page.

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Navigation tasks are specified by goal images, which are sometimes not the most natural modality for users (p. 6).
- Exploration uses a standard frontier-based strategy for high-level planning (p. 6).

## Transfer conditions

Language or coordinate goals require an extension that the paper leaves to future work. Results come from one wheeled robot.

## Code and data

Code availability was not checked in this targeted reading.

## Version family

Counted once by the registered ICRA 2024 identity. It follows the ViNT (K14) setup and uses GNM (K13) data.

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

- **p. 4, Sec. IV-C.** "We train NoMaD on a combination of GNM and SACSoN datasets, large heterogeneous datasets collected across a diverse set of environments and robotic platforms, including pedestrian-rich environments, spanning over 100 hours of real-world trajectories"
  Training data scale and sources.
- **p. 6, Sec. VI.** "The navigation tasks are specified via goal images which, though quite general, are sometimes not the most natural modalities for users to employ."
  Author-stated goal-modality limit.
- **p. 4, Sec. V.** "We evaluate NoMaD in 6 distinct indoor and outdoor environments"
  Evaluation scope.
- **p. 5, Sec. V-A.** "Visualizing rollouts of NoMaD deployed in challenging indoor (top) and outdoor (bottom) environments on the LoCoBot platform, showcasing successful exploration trajectories."
  Identifies the deployed platform.

## Survey-usable statements

### Supported

- NoMaD unifies goal-free exploration and goal-conditioned navigation in one diffusion policy that runs on the robot.
- It improved over subgoal-diffusion exploration in six real environments with a smaller model.

### Not supported

- NoMaD does not accept language goals.
- Results on one robot do not establish cross-embodiment transfer for this policy.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 3, 4, 5, 6; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and task-agnostic exploration (i.e., searching for a goal in a novel setting). Typically, these roles are handled by separate models, for example by using subgoal proposals, planning, or separate navigation strategies. In this paper, we describe how we can train a single unified diffusion policy to handle both goal-directed navigation and goal-agnostic exploration, with the latter providing the ability to search novel environments, and the former providing the ability to reach a user-specified goal once it has been located. We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that use subgoal proposals from generative models, or prior methods based on latent variable models. We instantiate our method by using a large-scale Transformer-based policy trained on data from multiple ground robots, with a diffusion model decoder to flexibly handle both goal-conditioned and goal-agnostic navigation. Our experiments, conducted on a real-world mobile robot platform, show effective navigation in unseen environments in comparison with five alternative methods, and demonstrate significant improvements in performance and lower collision rates, despite utilizing smaller models than state-of-the-art approaches.
