# ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning

## Metadata

| Field | Value |
|---|---|
| ID | K15 |
| Title | ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning |
| Authors | Qiao Gu, Ali Kuwajerwala, Sacha Morin, Krishna Murthy Jatavallabhula, Bipasha Sen, Aditya Agarwal, Corban Rivera, William Paul, Kirsty Ellis, Rama Chellappa, Chuang Gan, Celso Miguel de Melo, Joshua B. Tenenbaum, Antonio Torralba, Florian Shkurti, and Liam Paull |
| Venue | 2024 IEEE International Conference on Robotics and Automation (ICRA) |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/icra57147.2024.10610243](https://doi.org/10.1109/icra57147.2024.10610243) |
| Official URL | https://ieeexplore.ieee.org/document/10610243/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | review-additions-2026-11-04 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2024-ConceptGraphs-K15/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2024-ConceptGraphs-K15/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2024-ConceptGraphs-K15/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, dataset-playback
- protocol_caveats: video-only-hardware, cloud-model
- platform_class: wheeled-unspecified
- platform: Clearpath Jackal UGV in the REAL Lab for navigation queries; Boston Dynamics Spot Arm for pick and place; Replica scenes for quantitative tests (p. 5).
- boundary_platform: no
- degradation: scene-change
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task
- sensors: RGB-D input for mapping; the Jackal carries a VLP-16 LiDAR and a forward-facing RealSense D435i camera (p. 5)
- compute: SAM, CLIP, LLaVA and GPT-4 (gpt-4-0613); the authors note that LVLM and proprietary LLM inference costs may be significant (pp. 4, 6).
- compute_location: not-reported
- summary_result: An open-vocabulary 3D scene graph from 2D foundation models supports language queries; on the Jackal, an LLM redirects search after a target object is moved (pp. 4-6).
- summary_limitation: Node captions inherit LVLM errors, small or thin objects are missed or duplicated, and LVLM and proprietary LLM inference costs may be significant (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Dense open-vocabulary 3D maps store a feature per point, scale poorly and lack the object structure needed for dynamic updates and planning (p. 2).

## Mechanism

From posed RGB-D frames, class-agnostic masks (SAM) are embedded with CLIP and associated across views into 3D object nodes; an LVLM (LLaVA) captions each node, and an LLM infers relationships between adjoining nodes to form edges. For a task, the LLM reads JSON object descriptions and selects the relevant object, whose pose is passed to a navigation or grasping pipeline (pp. 2-4).

## Baselines and controls

Scene-graph accuracy of ConceptGraphs and a detector variant on Replica; open-vocabulary segmentation against privileged and zero-shot methods such as ConceptFusion; CLIP-based versus LLM-based retrieval (pp. 4-5).

## Platform and setup

Quantitative: Replica scenes and a real scan of the REAL Lab with staged items; retrieval queries on both (p. 5). Hardware: Jackal object search with moved targets and an LLM-based traversability task, Spot pick and place, and localization with map updates in the supplementary video (pp. 5-6).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`, but the robot demonstrations are qualitative; the tabulated results come from Replica and the lab scan. A moved target is a designed scene change without per-condition metrics, so `designed-degradation` is not coded. The provisional module `semantic-language-navigation` is confirmed. The Jackal takes coding precedence over Spot; its drive type is not stated.

## Sensors

RGB-D frames with poses for mapping (pp. 2-3); the Jackal carries a VLP-16 LiDAR and a forward-facing RealSense D435i camera (p. 5).

## Compute and latency

The implementation uses SAM, CLIP, LLaVA and GPT-4 (gpt-4-0613) (p. 4). Runtimes were not inspected; the authors note that multiple LVLM and proprietary LLM inferences may be costly (p. 6).

## Key quantitative results

- Replica scene-graph, segmentation and retrieval results are tabulated in Tables I-III (pp. 4-5); values were not re-read from rendered pages.
- Retrieval queries: 5 affordance and negation queries per Replica scene type and 10 per type for the lab scan (p. 5).
- Jackal object search: when the target is not at its mapped location, the LLM proposes a likely container, such as a laundry bag or shoe rack (p. 6, Fig. 3).

Numbers above come from the inspected text passages; table and figure values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Node captioning inherits errors of current LVLMs such as LLaVA (p. 6).
- The scene graph occasionally misses small or thin objects and makes duplicate detections, which affects downstream planning (p. 6).
- Building and querying the graph requires multiple LVLM and proprietary LLM inferences, whose computational and economic costs may be significant (p. 6).

## Transfer conditions

Map updates for moved objects are shown only qualitatively; a wheeled robot would need its own safety layer, because the LLM traversability judgment decides which objects the robot may push.

## Code and data

The project webpage is referenced on p. 1; code availability was not checked.

## Version family

Counted once by the registered ICRA 2024 identity. osmAG-LLM (R27) uses ConceptGraphs as a baseline.

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

- **p. 5, Sec. III-D.** "we carry out navigation experiments in the REAL Lab scene with a Clearpath Jackal UGV. The robot is equipped with a VLP-16 LiDAR and a forward-facing Realsense D435i camera."
  Hardware platform for the navigation demonstrations.
- **p. 5, Sec. III-E.** "Using an LVLM [56], the robot then checks if the object is at the expected location. If not, it queries an LLM to find a new plausible location given the captions of the other objects in the representation."
  Handling of a moved target object.
- **p. 6, Sec. III-H.** "Second, our 3D scene graph occasionally misses small or thin objects and makes duplicate detections."
  Author-stated mapping limitation.
- **p. 6, Sec. III-G.** "During this process, previously observed objects are removed if they are not observed by the robot and new objects can also be added."
  Map updating during relocalization, shown only in video.

## Survey-usable statements

### Supported

- ConceptGraphs builds an object-level open-vocabulary 3D scene graph that an LLM can query to choose navigation targets.
- On a Jackal, it re-plans an object search when the target has moved, in qualitative demonstrations.

### Not supported

- The hardware demonstrations give no success rates.
- Robustness to changed scenes is not quantified.

## Verification log

- 2026-11-04 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 6; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages unless named; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-04 review-additions batch.

## Original abstract

For robots to perform a wide variety of tasks, they require a 3D representation of the world that is semantically rich, yet compact and efficient for task-driven perception and planning. Recent approaches have attempted to leverage features from large vision-language models to encode semantics in 3D representations. However, these approaches tend to produce maps with per-point feature vectors, which do not scale well in larger environments, nor do they contain semantic spatial relationships between entities in the environment, which are useful for downstream planning. In this work, we propose ConceptGraphs, an open-vocabulary graph-structured representation for 3D scenes. ConceptGraphs is built by leveraging 2D foundation models and fusing their output to 3D by multi-view association. The resulting representations generalize to novel semantic classes, without the need to collect large 3D datasets or finetune models. We demonstrate the utility of this representation through a number of downstream planning tasks that are specified through abstract (language) prompts and require complex reasoning over spatial and semantic concepts. To explore the full scope of our experiments and results, we encourage readers to visit our project webpage.
