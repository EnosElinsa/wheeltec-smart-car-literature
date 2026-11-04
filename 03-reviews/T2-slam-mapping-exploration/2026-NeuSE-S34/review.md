# NeuSE: Neural SE(3)-equivariant embedding for long-term object-based simultaneous localization and mapping

## Metadata

| Field | Value |
|---|---|
| ID | S34 |
| Title | NeuSE: Neural SE(3)-equivariant embedding for long-term object-based simultaneous localization and mapping |
| Authors | Jiahui Fu and Yilun Du and Kurran Singh and Joshua B Tenenbaum and John J Leonard |
| Venue | The International Journal of Robotics Research |
| Year | 2026 |
| Type | journal |
| DOI | [10.1177/02783649251355966](https://doi.org/10.1177/02783649251355966) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649251355966 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-NeuSE-S34/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-NeuSE-S34/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-NeuSE-S34/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, simulation
- protocol_caveats: none
- platform_class: skid-steer
- platform: RGB-D recordings from a Clearpath Jackal in controlled object-layout changes, additional handheld sequences and synthetic scenes (pp. 10, 18).
- boundary_platform: no
- degradation: scene-change
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Partial object point clouds/RGB-D, segmentation, object associations and optional external odometry
- compute: Category-specific simulation training on RTX 3090 GPUs; training hardware does not establish onboard inference placement (p. 10).
- compute_location: not-reported
- summary_result: Object embeddings supply pose constraints and change-aware map updates under tested layout changes.
- summary_limitation: Category-specific training restricts open-set use and scaling to scenes with previously unknown object categories (p. 27).
- survey_included: yes
- verification_level: light

## Problem

Object relocation and changing viewpoints undermine persistent associations and metric mapping.

## Mechanism

Uses category-level SE(3)/scale-equivariant object embeddings to derive camera-pose constraints, update pose graphs and maintain change-aware object maps (pp. 7, 27).

## Baselines and controls

Controlled synthetic transforms, object addition/removal/relocation, and operation with external SLAM/odometry are inspected; complete comparator tables not audited.

## Platform and setup

RGB-D recordings from a Clearpath Jackal in controlled object-layout changes, additional handheld sequences and synthetic scenes (pp. 10, 18).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Requires reliable segmentation and associations within trained categories; simulated training and recorded Jackal data do not establish autonomous response to a changed map.

## Sensors

Partial object point clouds/RGB-D, segmentation, object associations and optional external odometry.

## Compute and latency

Category-specific simulation training on RTX 3090 GPUs; training hardware does not establish onboard inference placement (p. 10).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Category-specific training restricts open-set use and scaling to scenes with previously unknown object categories (p. 27).

## Transfer conditions

Requires reliable segmentation and associations within trained categories; simulated training and recorded Jackal data do not establish autonomous response to a changed map.

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

- **p. 27, Selected source passage.** "requiring category-specific training for each type of object before being applied to a scene."
  Distinguishes map-change accommodation from semantic open-set generality and from an executed navigation recovery policy.

## Survey-usable statements

### Supported

- Object embeddings supply pose constraints and change-aware map updates under tested layout changes. Distinguishes map-change accommodation from semantic open-set generality and from an executed navigation recovery policy.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Requires reliable segmentation and associations within trained categories; simulated training and recorded Jackal data do not establish autonomous response to a changed map.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 7, 10, 18, 27; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

We present NeuSE, a novel Neural SE(3)-Equivariant Embedding for objects, and illustrate how it supports object-based Simultaneous Localization and Mapping (SLAM) for consistent spatial understanding with long-term scene changes. NeuSE is a set of latent object embeddings created from partial object observations. It serves as a compact point cloud surrogate for complete object models, encoding the full shape, scale, and transform information about an object. In addition, the inferred latent code is both SE(3) and scale equivariant, enabling strong generalization to objects of both unseen sizes and different SE(3) poses. This makes NeuSE particularly effective in real-world scenarios where objects may vary in size or spatial configuration. With NeuSE, relative frame transforms can be directly derived from inferred latent codes. Our proposed SLAM paradigm, using NeuSE for object shape, size, and pose characterization, can operate independently or in conjunction with typical SLAM systems. It directly infers SE(3) camera pose constraints that are compatible with general SLAM pose graph optimization, while maintaining a lightweight, object-centric map that adapts to real-world changes. Our evaluation is conducted on synthetic and real-world sequences with changes in both controlled and uncontrolled settings, featuring multi-category objects of various shapes and sizes. Our approach demonstrates improved localization capability and change-aware mapping consistency when working either independently or as a complement to common SLAM pipelines.
