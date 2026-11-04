# osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning

## Metadata

| Field | Value |
|---|---|
| ID | R27 |
| Title | osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning |
| Authors | Fujing Xie, Sören Schwertfeger, and Hermann Blum |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3653280](https://doi.org/10.1109/lra.2026.3653280) |
| Official URL | https://ieeexplore.ieee.org/document/11346008/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-osmAG-LLM-R27/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-osmAG-LLM-R27/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2026-osmAG-LLM-R27/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: wheeled-unspecified
- platform: Habitat HM3D-SEM scenes and a campus building with five rooms; the physical robot navigates with ROS move_base (pp. 3, 5-7).
- boundary_platform: no
- degradation: scene-change
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: RGB-D camera; prior map scanned with a handheld 3D scanner app (p. 3)
- compute: Not inspected in this reading.
- compute_location: not-reported
- summary_result: A lightweight semantic map with LLM priors and active detection outperforms dense open-vocabulary maps for relocated or unmapped objects; 27 of 30 real trials reach correct positions (pp. 7-8).
- summary_limitation: Detection is limited by the categories of the underlying models; concealed objects are future work (pp. 4, 8).
- survey_included: yes
- verification_level: light

## Problem

Detailed object maps become outdated when objects move or were never mapped.

## Mechanism

A text-based semantic area graph provides room and viewpoint context; an LLM proposes likely locations; the robot visits response nodes and runs online detection to confirm targets (pp. 3-5).

## Baselines and controls

HOV-SG and ConceptGraph (pp. 5-7).

## Platform and setup

Habitat experiments and 30 real trials with static, relocated and unmapped objects (pp. 5-7). Habitat HM3D-SEM scenes and a campus building with five rooms; the physical robot navigates with ROS move_base (pp. 3, 5-7).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop hardware with a small trial count.

## Sensors

RGB-D camera; prior map scanned with a handheld 3D scanner app (p. 3).

## Compute and latency

Not inspected in this reading.

## Key quantitative results

- Nine of 30 real trials fail, mostly from detection errors; 27 of 30 reach correct positions (pp. 7-8).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- LabelMaker fails to recognize objects outside standard datasets, limiting unrestricted queries (p. 4).
- Searching concealed spaces and grasping are future work (p. 8).

## Transfer conditions

Requires a prior building map and a geometric navigation stack; detection errors dominate failures.

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

- **p. 7, Sec. IV-D.** "5) Failure Analysis: Our experiments resulted in 9 failed cases out of 30 trials, as shown in Fig. 7."
  Trial count and failure count.
- **p. 8, Sec. IV-D.** "Therefore, the system achieved 90% correct robot positioning (27/30), with detection errors accounting for most failures."
  Separates navigation from detection outcome.

## Survey-usable statements

### Supported

- Semantic search that expects moved objects outperforms static dense maps in the tested building.

### Not supported

- Thirty trials do not establish reliability across buildings.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 3, 4, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Recent open-vocabulary robot mapping methods enrich dense geometric maps with pre-trained visual-language features, achieving a high level of detail and guiding robots to find objects specified by open-vocabulary language queries. While the issue of scalability for such approaches has received some attention, another fundamental problem is that high-detail object mapping quickly becomes outdated, as objects get moved around a lot. In this work, we develop a mapping and navigation system for object-goal navigation that, from the ground up, considers the possibilities that a queried object can have moved, or may not be mapped at all. Instead of striving for high-fidelity mapping detail, we consider that the main purpose of a map is to provide environment grounding and context, which we combine with the semantic priors of LLMs to reason about object locations and deploy an active, online approach to navigate to the objects. Through simulated and real-world experiments we find that our approach tends to have higher retrieval success at shorter path lengths for static objects and by far outperforms prior approaches in cases of dynamic or unmapped object queries.
