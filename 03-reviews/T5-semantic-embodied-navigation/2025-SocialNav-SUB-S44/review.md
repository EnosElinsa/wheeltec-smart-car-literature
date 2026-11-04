# SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation

## Metadata

| Field | Value |
|---|---|
| ID | S44 |
| Title | SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation |
| Authors | Munje, Michael Joseph and Tang, Chen and Liu, Shuijing and Hu, Zichao and Zhu, Yifeng and Cui, Jiaxun and Warnell, Garrett and Biswas, Joydeep and Stone, Peter |
| Venue | Conference on Robot Learning |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v305/munje25a.html |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-SocialNav-SUB-S44/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-SocialNav-SUB-S44/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2025-SocialNav-SUB-S44/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: dataset-resource
- evidence_all: dataset-resource
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Recorded human-centered robot navigation scenes; offline VQA and candidate-waypoint selection, not closed-loop robot control (pp. 4, 14).
- boundary_platform: no
- degradation: dynamic-objects, model-error
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Scene images, object-centric/BEV representations and pedestrian position annotations
- compute: Multiple hosted/local VLMs compared offline; full per-model compute deployment not audited.
- compute_location: mixed
- summary_result: Strong VLMs still trail rule-based and human-oracle scene understanding in the inspected benchmark.
- summary_limitation: SCAND university-campus scope and a limited set of models/scenarios restrict benchmark coverage (p. 9).
- survey_included: yes
- verification_level: light

## Problem

A VLM may describe a scene plausibly while misunderstanding social/spatiotemporal relations needed for navigation.

## Mechanism

VQA benchmark compares spatial, spatiotemporal and social answers with human consensus and position-informed rules (pp. 4-7).

## Baselines and controls

Human oracle, average human and rule-based systems; BEV/chain-of-thought prompting ablations (p. 7).

## Platform and setup

Recorded human-centered robot navigation scenes; offline VQA and candidate-waypoint selection, not closed-loop robot control (pp. 4, 14).

## Evidence type and transfer

Strongest coded setting: `dataset-resource`. Rule baselines receive pedestrian positions; VQA agreement must not be treated as a collision rate or safe-control certificate.

## Sensors

Scene images, object-centric/BEV representations and pedestrian position annotations.

## Compute and latency

Multiple hosted/local VLMs compared offline; full per-model compute deployment not audited.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

SCAND university-campus scope and a limited set of models/scenarios restrict benchmark coverage (p. 9).

## Transfer conditions

Rule baselines receive pedestrian positions; VQA agreement must not be treated as a collision rate or safe-control certificate.

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

- **p. 7, Selected source passage.** "they still fall short of human oracle and rule-based performance across key reasoning tasks."
  Adds a concrete counterexample to using model scale or fluent reasoning as evidence of safe social navigation.

## Survey-usable statements

### Supported

- Strong VLMs still trail rule-based and human-oracle scene understanding in the inspected benchmark. Adds a concrete counterexample to using model scale or fluent reasoning as evidence of safe social navigation.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Rule baselines receive pedestrian positions; VQA agreement must not be treated as a collision rate or safe-control certificate.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 5, 7, 9, 14; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Robot navigation in dynamic, human-centered environments requires socially-compliant decisions grounded in robust scene understanding. Recent Vision-Language Models (VLMs) exhibit promising capabilities such as object recognition, common-sense reasoning, and contextual understanding—capabilities that align with the nuanced requirements of social robot navigation. However, it remains unclear whether VLMs can accurately understand complex social navigation scenes (e.g., inferring the spatial-temporal relations among agents and human intentions), which is essential for safe and socially compliant robot navigation. While some recent works have explored the use of VLMs in social robot navigation, no existing work systematically evaluates their ability to meet these necessary conditions. In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SocialNav-SUB), a Visual Question Answering (VQA) dataset and benchmark designed to evaluate VLMs for scene understanding in real-world social robot navigation scenarios. SocialNav-SUB provides a unified framework for evaluating VLMs against human and rule-based baselines across VQA tasks requiring spatial, spatiotemporal, and social reasoning in social robot navigation. Through experiments with state-of-the-art VLMs, we find that while the best-performing VLM achieves an encouraging probability of agreeing with human answers, it still underperforms simpler rule-based approach and human consensus baselines, indicating critical gaps in social scene understanding of current VLMs. Our benchmark sets the stage for further research on foundation models for social robot navigation, offering a framework to explore how VLMs can be tailored to meet real-world social robot navigation needs. An overview of this paper along with the code and data can be found at https://larg.github.io/socialnav-sub.
