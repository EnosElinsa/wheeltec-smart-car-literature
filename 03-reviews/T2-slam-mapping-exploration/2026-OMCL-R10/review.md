# OMCL: Open-Vocabulary Monte Carlo Localization

## Metadata

| Field | Value |
|---|---|
| ID | R10 |
| Title | OMCL: Open-Vocabulary Monte Carlo Localization |
| Authors | Evgenii Kruzhkov, Raphael Memmesheimer, and Sven Behnke |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3653333](https://doi.org/10.1109/lra.2026.3653333) |
| Official URL | https://ieeexplore.ieee.org/document/11347000/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-OMCL-R10/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-OMCL-R10/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-OMCL-R10/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: semantic-language-navigation
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: Matterport3D sequences from VLMaps, Replica rooms and SemanticKITTI outdoor sequences (pp. 4-6).
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: RGB camera for localization with map-scaled odometry; maps from posed RGB-D images or aligned point clouds
- compute: NVIDIA RTX 3090 GPU (p. 5).
- compute_location: desktop-offline
- summary_result: Open-vocabulary feature likelihoods enable cross-modal Monte Carlo localization and language-initialized global localization on indoor and outdoor datasets (pp. 5-7).
- summary_limitation: Lacks online map updates and requires map-scaled odometry (p. 7).
- survey_included: yes
- verification_level: light

## Problem

Localization fails when the map and the robot use different sensors or closed-set semantics.

## Mechanism

CLIP-type features are stored in an octree map; a particle filter scores pose hypotheses by ray casting map features into the image and comparing them with current features; a text prompt about nearby objects initializes the particles (pp. 2-4).

## Baselines and controls

Open-vocabulary and feed-forward localization approaches including Pi-Long, and ablations of rays and feature extractors (pp. 5-7).

## Platform and setup

Dataset evaluation in room-scale, building-scale and outdoor scenes (pp. 4-6). Matterport3D sequences from VLMaps, Replica rooms and SemanticKITTI outdoor sequences (pp. 4-6).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. Dataset replay; no physical robot.

## Sensors

RGB camera for localization with map-scaled odometry; maps from posed RGB-D images or aligned point clouds.

## Compute and latency

NVIDIA RTX 3090 GPU (p. 5).

## Key quantitative results

- Localization generalizes across Matterport3D, Replica and SemanticKITTI in the reported APE comparisons (pp. 5-6).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- OMCL lacks online map updates and requires map-scaled odometry (p. 7).

## Transfer conditions

Requires a prepared feature map and metric odometry; moved objects change the feature consistency that the likelihood assumes.

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

- **p. 7, Sec. V.** "OMCL lacks online map updates and requires map-scaled odometry."
  Author-stated limits.

## Survey-usable statements

### Supported

- Open-vocabulary features can serve as a cross-modal localization likelihood.

### Not supported

- Robustness to changed object layouts is not established without map updates.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 5, 6, 7; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Robust robot localization is an important prerequisite for navigation, but it becomes challenging when the map and robot measurements are obtained from different sensors. Prior methods are often tailored to specific environments, relying on closed-set semantics or fine-tuned features. In this work, we extend Monte Carlo Localization with vision-language features, allowing OMCL to robustly compute the likelihood of visual observations given a camera pose and a 3D map created from posed RGB-D images or aligned point clouds These open-vocabulary features enable us to associate observations and map elements from different modalities, and to natively initialize global localization through natural language descriptions of nearby objects. We evaluate our approach using Matterport3D and Replica for indoor scenes and demonstrate generalization on SemanticKITTI for outdoor scenes.
