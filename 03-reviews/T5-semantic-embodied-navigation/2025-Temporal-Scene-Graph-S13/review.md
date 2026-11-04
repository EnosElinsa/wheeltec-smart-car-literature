# Temporal Scene-Object Graph Learning for Object Navigation

## Metadata

| Field | Value |
|---|---|
| ID | S13 |
| Title | Temporal Scene-Object Graph Learning for Object Navigation |
| Authors | Chen, Lu and He, Zongtao and Wang, Liuyi and Liu, Chengju and Chen, Qijun |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3553055](https://doi.org/10.1109/lra.2025.3553055) |
| Official URL | https://ieeexplore.ieee.org/document/10933547/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-Temporal-Scene-Graph-S13/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-Temporal-Scene-Graph-S13/paper.md` (local only); [citation.bib](../../../01-papers/T5-semantic-embodied-navigation/2025-Temporal-Scene-Graph-S13/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: offboard-compute
- platform_class: wheeled-unspecified
- platform: Self-developed wheeled service robot plus AI2THOR/Gibson object-navigation tests (pp. 4, 7-8).
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Monocular camera with DETR object detections; no depth input
- compute: Nearby laptop i5-11400H/RTX3050Ti executes the algorithms; no audited end-to-end actuator-latency bound (p. 7).
- compute_location: offboard-local
- summary_result: Temporal object/scene relations guide search in unseen scenes and a physical demonstration.
- summary_limitation: Sensitive to missed/false detections; missing depth causes corner trapping and a target may remain out of view at termination (p. 7).
- survey_included: yes
- verification_level: light

## Problem

Limited egocentric visibility and forgotten history hinder object-goal search.

## Mechanism

Holistic object features, local/global scene-object graph and temporal aggregation provide a recurrent navigation representation (pp. 3-4).

## Baselines and controls

End-to-end ObjectNav methods and representation/temporal ablations (p. 4).

## Platform and setup

Self-developed wheeled service robot plus AI2THOR/Gibson object-navigation tests (pp. 4, 7-8).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Simulation action choices and laptop execution do not provide onboard real-time obstacle-clearance guarantees.

## Sensors

Monocular camera with DETR object detections; no depth input.

## Compute and latency

Nearby laptop i5-11400H/RTX3050Ti executes the algorithms; no audited end-to-end actuator-latency bound (p. 7).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Sensitive to missed/false detections; missing depth causes corner trapping and a target may remain out of view at termination (p. 7).

## Transfer conditions

Simulation action choices and laptop execution do not provide onboard real-time obstacle-clearance guarantees.

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

- **p. 7, Selected source passage.** "the model lacks depth perception in the environment"
  Supplies a failure-specific counterexample to equating semantic search success with geometric feasibility.

## Survey-usable statements

### Supported

- Temporal object/scene relations guide search in unseen scenes and a physical demonstration. Supplies a failure-specific counterexample to equating semantic search success with geometric feasibility.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Simulation action choices and laptop execution do not provide onboard real-time obstacle-clearance guarantees.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 4, 7, 8; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Object navigation tasks require agents to locate target objects within unfamiliar indoor environments. However, the first-person perspective inherently imposes limited visibility, complicating global planning. Hence, it becomes imperative for the agent to cultivate an efficient visual representation from this restricted viewpoint. To address this, we introduce a temporal scene-object graph (TSOG) to construct an informative and efficient ego-centric visual representation. Firstly, we develop a holistic object feature descriptor (HOFD) to fully describe object features from different aspects, facilitating the learning of relationships between observed and unseen objects. Next, we propose a scene-object graph (SOG) to simultaneously learn local and global correlations between objects and agent observations, granting the agent a more comprehensive and flexible scene understanding ability. This facilitates the agent to perform target association and search more efficiently. Finally, we introduce a temporal graph aggregation (TGA) module to dynamically aggregate memory information across consecutive time steps. TGA offers the agent a dynamic perspective on historical steps, aiding in navigation towards the target in longer trajectories. Extensive experiments in AI2THOR and Gibson datasets demonstrate our method’s effectiveness and efficiency for ObjectNav tasks in unseen environments.
