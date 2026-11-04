# LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action

## Metadata

| Field | Value |
|---|---|
| ID | K12 |
| Title | LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action |
| Authors | Dhruv Shah, Błażej Osiński, Brian Ichter, and Sergey Levine |
| Venue | Conference on Robot Learning |
| Year | 2023 (conference 2022) |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v205/shah23b.html |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2023-LM-Nav-K12/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2023-LM-Nav-K12/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2023-LM-Nav-K12/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: teleoperated-mapping, few-trials
- platform_class: wheeled-unspecified
- platform: Clearpath Jackal UGV in two outdoor suburban environments; drive type not stated in the inspected pages (pp. 5-6).
- boundary_platform: no
- degradation: none
- degradation_observed: model-error, visual-degradation
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: Onboard camera images and GPS observations collected while manually driving to build the graph (p. 6)
- compute: Not inspected in this reading; the paper does not state in the inspected pages where GPT-3 is queried.
- compute_location: not-reported
- summary_result: Over 20 instructions covering more than 6 km, LM-Nav finds a successful walk for 85% and needs one disengagement, about 1 per 6.4 km (pp. 6-7).
- summary_limitation: LM-Nav keeps only landmarks and drops verbs and other cues, and its navigation model is specific to outdoor navigation with the Jackal (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Language-conditioned navigation usually needs trajectories annotated with instructions. LM-Nav follows free-form instructions by composing pre-trained models without language-annotated robot data (p. 1).

## Mechanism

A visual navigation model (ViNG) builds a topological graph from prior observations of the environment and executes walks on it. GPT-3 parses an instruction into an ordered list of landmarks, CLIP scores landmark-node associations, and a graph search maximizes a probabilistic objective that combines landmark likelihoods with traversal cost (pp. 1-5).

## Baselines and controls

GPS-Nav (the system without the navigation model), a max-likelihood planner that ignores reachability, alternative language models and alternative detectors (pp. 7-8).

## Platform and setup

In each environment the graph is built by manually driving the robot and collecting image and GPS observations. The system was tested on 20 queries in two environments with a combined length of over 6 km, and goals up to 800 m away (pp. 5-6).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware` on one wheeled robot with a teleoperated prior traversal and 20 queries. Missing landmarks and underexposed images occurred in the trials and are coded as observed. The provisional module `semantic-language-navigation` is confirmed: language and vision-language models select the route that the navigation model executes.

## Sensors

Onboard camera images, with GPS observations used for the prior graph and for the GPS-Nav ablation (pp. 6, 8).

## Compute and latency

Not inspected in this reading. The inspected pages do not state where GPT-3 inference runs.

## Key quantitative results

- 20 instructions over a combined length of more than 6 km in two environments (p. 6).
- LM-Nav generates a successful walk for 85% of the instructions and causes one disengagement, about 1 intervention per 6.4 km (p. 7).
- Goals are up to 800 m away (p. 5).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- LM-Nav relies on landmarks and disregards verbs, prepositions and adverbs, which can be lossy (p. 8).
- The navigation model is specific to outdoor navigation with the Jackal robot, which limits adoption on other embodiments and sensor suites (p. 8).
- The system relies on a pre-built topological graph (p. 3).

## Transfer conditions

A prior teleoperated traversal must exist, and landmark grounding fails for some objects and lighting; a wheeled robot needs its own navigation model and graph.

## Code and data

Code availability was not checked in this targeted reading.

## Version family

Conference on Robot Learning 2022, published in PMLR volume 205 with year 2023; counted once. Its discussion points to a general navigation model across robots, the direction of GNM (K13).

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

- **p. 6, Sec. 5.1.** "In each evaluation environment, we first construct the graph by manually driving the robot and collecting image and GPS observations."
  The prior graph comes from a teleoperated traversal.
- **p. 7, Sec. 5.2.** "LM-Nav generates a successful walk for 85% of them, and causes disengagement only once (an average of 1 intervention per 6.4km of traversals)."
  Headline result over 20 instructions.
- **p. 8, Sec. 6.** "Additionally, LM-Nav uses a VNM that is specific to outdoor navigation with the Jackal robot, which limits wider adoption for other robot embodiments and sensor suites."
  Author-stated embodiment limit.
- **p. 6, Sec. 5.1.** "We tested our system on 20 queries in 2 environments, corresponding to a combined length of over 6km."
  Trial count and scale.

## Survey-usable statements

### Supported

- LM-Nav composes GPT-3, CLIP and a visual navigation model to follow landmark instructions on a Jackal without language-annotated robot data.
- It needed one disengagement over more than 6 km of traversals in 20 queries.

### Not supported

- Twenty queries in two environments do not establish reliability across sites.
- The system does not handle instructions whose meaning lies in verbs or spatial relations.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

Goal-conditioned policies for robotic navigation can be trained on large, unannotated datasets, providing for good generalization to real-world settings. However, particularly in vision-based settings where specifying goals requires an image, this makes for an unnatural interface. Language provides a more convenient modality for communication with robots, but contemporary methods typically require expensive supervision, in the form of trajectories annotated with language descriptions. We present a system, LM-Nav, for robotic navigation that enjoys the benefits of training on unannotated large datasets of trajectories, while still providing a high-level interface to the user. Instead of utilizing a labeled instruction following dataset, we show that such a system can be constructed entirely out of pre-trained models for navigation (ViNG), image-language association (CLIP), and language modeling (GPT-3), without requiring any fine-tuning or language-annotated robot data. LM-Nav extracts landmarks names from an instruction, grounds them in the world via the image-language model, and then reaches them via the (vision-only) navigation model. We instantiate LM-Nav on a real-world mobile robot and demonstrate long-horizon navigation through complex, outdoor environments from natural language instructions.
