# Mobile Robot Navigation Using Hand-Drawn Maps: A Vision Language Model Approach

## Metadata

| Field | Value |
|---|---|
| ID | S39 |
| Title | Mobile Robot Navigation Using Hand-Drawn Maps: A Vision Language Model Approach |
| Authors | Tan, Aaron Hao and Fung, Angus and Wang, Haitong and Nejat, Goldie |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3577456](https://doi.org/10.1109/lra.2025.3577456) |
| Official URL | https://ieeexplore.ieee.org/document/11027320/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-HAM-Nav-S39/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-HAM-Nav-S39/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2025-HAM-Nav-S39/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: cloud-model
- platform_class: skid-steer
- platform: Clearpath Jackal with ZED Mini in campus indoor/outdoor user studies; wheeled/legged photorealistic simulation (pp. 5-6).
- boundary_platform: no
- degradation: data-association-fault
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Camera landmarks and GMapping occupancy grid; hand-drawn topological prior
- compute: GPT-4o API for map association/planning; A* and TEB execute the metric navigation layer (pp. 6-7).
- compute_location: mixed
- summary_result: Sketch-based topological guidance tolerates imperfect drawing in the evaluated user/task settings.
- summary_limitation: Cloud API access and stop-and-go waiting for VLM outputs limit operation (p. 7).
- survey_included: yes
- verification_level: light

## Problem

Hand-drawn instructions contain scale distortion and missing landmarks.

## Mechanism

Selective visual association aligns observations to a sketch; a predictive parser infers missing landmarks before metric execution (pp. 3-5).

## Baselines and controls

MapGPT language-only instructions and simulated architecture ablations; user input protocols differ (pp. 5-7).

## Platform and setup

Clearpath Jackal with ZED Mini in campus indoor/outdoor user studies; wheeled/legged photorealistic simulation (pp. 5-6).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. User-study benefits depend on sketch versus one-shot verbal input; landmark prediction needs geometric checks before motion.

## Sensors

Camera landmarks and GMapping occupancy grid; hand-drawn topological prior.

## Compute and latency

GPT-4o API for map association/planning; A* and TEB execute the metric navigation layer (pp. 6-7).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Cloud API access and stop-and-go waiting for VLM outputs limit operation (p. 7).

## Transfer conditions

User-study benefits depend on sketch versus one-shot verbal input; landmark prediction needs geometric checks before motion.

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

- **p. 7, Selected source passage.** "Internet access is also required during operation to access VLM API."
  Extends semantic interfaces to fallible human priors and adds network/latency conditions to transfer.

## Survey-usable statements

### Supported

- Sketch-based topological guidance tolerates imperfect drawing in the evaluated user/task settings. Extends semantic interfaces to fallible human priors and adds network/latency conditions to transfer.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. User-study benefits depend on sketch versus one-shot verbal input; landmark prediction needs geometric checks before motion.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 4, 5, 6, 7; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Hand-drawn maps can be used to convey navigation instructions between humans and robots in a natural and efficient manner. However, these maps can often contain inaccuracies such as scale distortions and missing landmarks which present challenges for mobile robot navigation. This letter introduces a novel Hand-drawn Map Navigation (HAM-Nav) architecture that leverages pre-trained vision language models (VLMs) for robot navigation across diverse environments, hand-drawing styles, and robot embodiments, even in the presence of map inaccuracies. HAM-Nav integrates a unique Selective Visual Association Prompting approach for topological map-based position estimation and navigation planning as well as a Predictive Navigation Plan Parser to infer missing landmarks. Extensive experiments were conducted in photorealistic simulated environments, using both wheeled and legged robots, demonstrating the effectiveness of HAM-Nav in terms of navigation success rates and Success weighted by Path Length. Furthermore, a user study in real-world environments highlighted the practical utility of hand-drawn maps for robot navigation as well as successful navigation outcomes compared against a non-hand-drawn map approach.
