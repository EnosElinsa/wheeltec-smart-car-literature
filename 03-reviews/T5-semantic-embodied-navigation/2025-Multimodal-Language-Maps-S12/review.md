# Multimodal spatial language maps for robot navigation and manipulation

## Metadata

| Field | Value |
|---|---|
| ID | S12 |
| Title | Multimodal spatial language maps for robot navigation and manipulation |
| Authors | Chenguang Huang and Oier Mees and Andy Zeng and Wolfram Burgard |
| Venue | The International Journal of Robotics Research |
| Year | 2025 |
| Type | journal |
| DOI | [10.1177/02783649251351658](https://doi.org/10.1177/02783649251351658) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649251351658 |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-Multimodal-Language-Maps-S12/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-Multimodal-Language-Maps-S12/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2025-Multimodal-Language-Maps-S12/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Indoor wheeled mobile navigation with prebuilt AVLMaps and separate tabletop manipulator tests; Habitat/Matterport3D simulation (pp. 15, 19).
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: RGB-D, camera poses and audio features; staged sounds indicate where they were heard rather than sound-source triangulation
- compute: Mapping explicitly offline; language-generated code calls ROS global/local planning. Complete inference placement not retained (p. 19).
- compute_location: not-reported
- summary_result: A reusable multimodal map supports spatial goal disambiguation and physical goal reaching.
- summary_limitation: Offline pre-exploration cannot react to transient sounds; maps lack in-view and long-term dynamic update mechanisms (p. 22).
- survey_included: yes
- verification_level: light

## Problem

Spatial navigation commands can refer to ambiguous visual, language and sound concepts.

## Mechanism

Anchors pretrained visual-language and audio features to a reusable spatial map, retrieves/fuses goal heatmaps and exposes spatial APIs to an LLM (p. 4).

## Baselines and controls

Modality-specific navigation and foundation-model choices; simulation and physical navigation are separate evaluation settings (pp. 15, 19).

## Platform and setup

Indoor wheeled mobile navigation with prebuilt AVLMaps and separate tabletop manipulator tests; Habitat/Matterport3D simulation (pp. 15, 19).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Goal grounding depends on a valid prepared map and composed module accuracy; a sound-associated location is not an acoustically localized source.

## Sensors

RGB-D, camera poses and audio features; staged sounds indicate where they were heard rather than sound-source triangulation.

## Compute and latency

Mapping explicitly offline; language-generated code calls ROS global/local planning. Complete inference placement not retained (p. 19).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Offline pre-exploration cannot react to transient sounds; maps lack in-view and long-term dynamic update mechanisms (p. 22).

## Transfer conditions

Goal grounding depends on a valid prepared map and composed module accuracy; a sound-associated location is not an acoustically localized source.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 22, Selected source passage.** "Currently, our multimodal spatial language maps lack mechanisms to address both types of dynamics."
  Adds explicit multimodal memory while sharpening the distinction between semantic grounding, map validity and collision safety.

## Survey-usable statements

### Supported

- A reusable multimodal map supports spatial goal disambiguation and physical goal reaching. Adds explicit multimodal memory while sharpening the distinction between semantic grounding, map validity and collision safety.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Goal grounding depends on a valid prepared map and composed module accuracy; a sound-associated location is not an acoustically localized source.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 15, 19, 22; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Grounding language to a navigating agent’s observations can leverage pretrained multimodal foundation models to match perceptions to object or event descriptions. However, previous approaches remain disconnected from environment mapping, lack the spatial precision of geometric maps, or neglect additional modality information beyond vision. To address this, we propose multimodal spatial language maps as a spatial map representation that fuses pretrained multimodal features with a 3D reconstruction of the environment. We build these maps autonomously using standard exploration. We present two instances of our maps, which are visual-language maps (VLMaps) and their extension to audio-visual-language maps (AVLMaps) obtained by adding audio information. When combined with large language models (LLMs), VLMaps can translate natural language commands into open-vocabulary spatial goals (e.g., “in between the sofa and TV”) directly localized in the map, and be shared across different robot embodiments to generate tailored obstacle maps on demand. Building upon the capabilities above, AVLMaps extend VLMaps by introducing a unified 3D spatial representation integrating audio, visual, and language cues through the fusion of features from pretrained multimodal foundation models. This enables robots to ground multimodal goal queries (e.g., text, images, or audio snippets) to spatial locations for navigation. Additionally, the incorporation of diverse sensory inputs significantly enhances goal disambiguation in ambiguous environments. Experiments in simulation and real-world settings demonstrate that our multimodal spatial language maps enable zero-shot spatial and multimodal goal navigation and improve recall by 50% in ambiguous scenarios. These capabilities extend to mobile robots and tabletop manipulators, supporting navigation and interaction guided by visual, audio, and spatial cues. Code and videos are available at https://mslmaps.github.io.
