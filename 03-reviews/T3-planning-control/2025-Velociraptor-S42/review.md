# Velociraptor: Leveraging Visual Foundation Models for Label-Free, Risk-Aware Off-Road Navigation

## Metadata

| Field | Value |
|---|---|
| ID | S42 |
| Title | Velociraptor: Leveraging Visual Foundation Models for Label-Free, Risk-Aware Off-Road Navigation |
| Authors | Triest, Samuel and Sivaprakasam, Matthew and Aich, Shubhra and Fan, David and Wang, Wenshan and Scherer, Sebastian |
| Venue | Conference on Robot Learning |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v270/triest25a.html |
| Theme folder | T3-planning-control |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T3-planning-control/2025-Velociraptor-S42/paper.pdf` and `02-fulltext/T3-planning-control/2025-Velociraptor-S42/paper.md` (local only); [citation.bib](../../../01-papers/T3-planning-control/2025-Velociraptor-S42/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Off-road wheeled driving on a long test loop and separate staged OOD-obstacle course, with safety-operator corrections (pp. 7-8).
- boundary_platform: no
- degradation: terrain, model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Camera visual-foundation-model features and LiDAR geometry projected to bird-eye maps
- compute: Learned map construction and MPPI control; exact deployed processor/complete latency not retained from selected passages.
- compute_location: not-reported
- summary_result: Visual-geometric maps influence both route and speed choices, with operator corrections reported in physical trials.
- summary_limitation: Occlusions, distance-consistent features, coarse projection and the inability to specify approach direction/minimum speed remain limitations (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Geometry-only costs miss low geometric obstacles while coarse semantics can overpenalize traversable vegetation.

## Mechanism

Learns costmaps from expert driving, speed distributions from expert speeds and epistemic novelty from feature density; quantile-controlled costs/speeds guide MPPI (pp. 4-5).

## Baselines and controls

Original/tuned ALTER geometry, semantic and learned variants; held-out-site trajectory matching is separated from physical intervention/speed/bumpiness tests (pp. 6-8).

## Platform and setup

Off-road wheeled driving on a long test loop and separate staged OOD-obstacle course, with safety-operator corrections (pp. 7-8).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Label-free training still uses expert driving. Physical risk parameters differ from offline tests; interventions must remain part of the outcome.

## Sensors

Camera visual-foundation-model features and LiDAR geometry projected to bird-eye maps.

## Compute and latency

Learned map construction and MPPI control; exact deployed processor/complete latency not retained from selected passages.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Occlusions, distance-consistent features, coarse projection and the inability to specify approach direction/minimum speed remain limitations (p. 8).

## Transfer conditions

Label-free training still uses expert driving. Physical risk parameters differ from offline tests; interventions must remain part of the outcome.

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

- **p. 8, Selected source passage.** "we cannot produce certain behaviors such as approaching logs from certain angles, or going at a minimum speed."
  Adds executed uncertainty-aware terrain decisions, while distinguishing novelty/demonstration-speed uncertainty from pose-to-footprint risk.

## Survey-usable statements

### Supported

- Visual-geometric maps influence both route and speed choices, with operator corrections reported in physical trials. Adds executed uncertainty-aware terrain decisions, while distinguishing novelty/demonstration-speed uncertainty from pose-to-footprint risk.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Label-free training still uses expert driving. Physical risk parameters differ from offline tests; interventions must remain part of the outcome.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Traversability analysis in unstructured environments is a challenging task that requires understanding of multi-modal inputs such as camera and LiDAR. Measurements from these sensors are often sparse, noisy, and difficult to interpret, particularly in the off-road setting. Existing traversability analysis systems are very engineering-intensive, often requiring hand-tuning of rules and manual annotation of semantic labels. Furthermore, existing methods for analyzing traversability risk and uncertainty are computationally expensive or not well-calibrated. We propose Velociraptor, a traversability analysis system that performs [veloci]ty-informed, [r]isk-[a]ware [p]erception and [t]raversability for [o]ff-[r]oad driving without any human annotations. We achieve this via the use of visual foundation models (VFM s) and geometric mapping to produce a rich visual-geometric representation of the robot’s local environment. We then leverage this representation to produce costmaps, speedmaps, and uncertainty maps using state-of-the-art fully self-supervised techniques. Our approach enables intelligent high-speed off-road navigation with zero human annotation, and with about forty minutes of expert data, outperforms several geometric and semantic traversability baselines, both in offline and real-world robot trials across multiple challenging off-road sites.
