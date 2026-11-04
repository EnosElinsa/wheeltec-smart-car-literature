# Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs

## Metadata

| Field | Value |
|---|---|
| ID | S43 |
| Title | Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs |
| Authors | Xu, Zhuo and Chiang, Hao-Tien Lewis and Fu, Zipeng and Jacob, Mithun George and Zhang, Tingnan and Lee, Tsang-Wei Edward and Yu, Wenhao and Schenck, Connor and Rendleman, David and Shah, Dhruv and Xia, Fei and Hsu, Jasmine and Hoech, Jonathan and Florence, Pete and Kirmani, Sean and Singh, Sumeet and Sindhwani, Vikas and Parada, Carolina and Finn, Chelsea and Xu, Peng and Levine, Sergey and Tan, Jie |
| Venue | Conference on Robot Learning |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v270/xu25b.html |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-Mobility-VLA-S43/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-Mobility-VLA-S43/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2025-Mobility-VLA-S43/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: teleoperated-mapping, cloud-model
- platform_class: wheeled-unspecified
- platform: Wheel-based mobile manipulator with MPC obstacle avoidance and a teleoperated demonstration tour (pp. 5-6).
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Tour/current images, multimodal instructions and low-level navigation sensing
- compute: Long-context VLM high-level frame retrieval with offline topological graph and local waypoint policy; complete placement not retained (pp. 4, 8).
- compute_location: mixed
- summary_result: Hierarchical goal retrieval plus a prepared graph enables multimodal instruction execution.
- summary_limitation: No autonomous exploration; long high-level inference impedes interaction (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Multimodal instructions require destination reasoning beyond a named object category.

## Mechanism

Long-context VLM retrieves a goal frame from a demonstration tour; topological routing and visual goal reaching issue low-level waypoints (pp. 3-5).

## Baselines and controls

High-level model alternatives, direct waypoint output and graph-removal ablations (pp. 6, 8).

## Platform and setup

Wheel-based mobile manipulator with MPC obstacle avoidance and a teleoperated demonstration tour (pp. 5-6).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Coverage of the demonstration tour is part of deployment cost; reasoning latency and low-level obstacle avoidance have separate scopes.

## Sensors

Tour/current images, multimodal instructions and low-level navigation sensing.

## Compute and latency

Long-context VLM high-level frame retrieval with offline topological graph and local waypoint policy; complete placement not retained (pp. 4, 8).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

No autonomous exploration; long high-level inference impedes interaction (p. 8).

## Transfer conditions

Coverage of the demonstration tour is part of deployment cost; reasoning latency and low-level obstacle avoidance have separate scopes.

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

- **p. 8, Selected source passage.** "The current version of Mobility VLA relies on a demonstration tour, and does not explore the environment automatically."
  Makes environment preparation and the semantic-to-geometric interface explicit in the navigation comparison.

## Survey-usable statements

### Supported

- Hierarchical goal retrieval plus a prepared graph enables multimodal instruction execution. Makes environment preparation and the semantic-to-geometric interface explicit in the navigation comparison.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Coverage of the demonstration tour is part of deployment cost; reasoning latency and low-level obstacle avoidance have separate scopes.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 4, 5, 6, 8; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

An elusive goal in navigation research is to build an intelligent agent that can understand multimodal instructions including natural language and image, and perform useful navigation. To achieve this, we study a widely useful category of navigation tasks we call Multimodal Instruction Navigation with demonstration Tours (MINT), in which the environment prior is provided through a previously recorded demonstration video. Recent advances in Vision Language Models (VLMs) have shown a promising path in achieving this goal as it demonstrates capabilities in perceiving and reasoning about multimodal inputs. To solve MINT, we present Mobility VLA, a hierarchical Vision-Language-Action (VLA) navigation policy that combines the environment understanding and common sense reasoning power of long-context VLMs and a robust low-level navigation policy based on topological graphs. The high-level policy consists of a long-context VLM that takes the demonstration tour video and the multimodal user instruction as input to find the goal frame in the tour video. Next, a low-level policy uses the goal frame and an offline constructed topological graph to generate robot actions at every timestep. We evaluated Mobility VLA in a 836m² real world environment and show that Mobility VLA has a high end-to-end success rates on previously unsolved multimodal instructions such as “Where should I return this?” while holding a plastic bin. A video demonstrating Mobility VLA can be found here: [youtu.be/-Tof__Q8_5s
