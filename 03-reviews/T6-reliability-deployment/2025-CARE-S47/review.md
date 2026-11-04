# CARE: Enhancing Safety of Visual Navigation through Collision Avoidance via Repulsive Estimation

## Metadata

| Field | Value |
|---|---|
| ID | S47 |
| Title | CARE: Enhancing Safety of Visual Navigation through Collision Avoidance via Repulsive Estimation |
| Authors | Kim, Joonkyung and Sim, Joonyeol and Kim, Woojun and Sycara, Katia P. and Nam, Changjoo |
| Venue | Conference on Robot Learning |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v305/kim25c.html |
| Theme folder | T6-reliability-deployment |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-CARE-S47/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-CARE-S47/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-CARE-S47/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: speed-capped, scripted-scenario
- platform_class: differential-drive
- platform: LoCoBot on TurtleBot4 base, TurtleBot4 and RoboMaster S1 with per-platform parameters and low-speed constraints (pp. 6, 14).
- boundary_platform: no
- degradation: model-error, dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Monocular RGB, UniDepthV2 estimated depth; no additional physical range sensor
- compute: Depth estimation plus base navigation inference; complete physical compute placement not retained in selected passages.
- compute_location: not-reported
- summary_result: Trajectory correction improves collision-avoidance behavior within the evaluated speed/scenario conditions.
- summary_limitation: Monocular depth errors, restricted range/FOV and an unsafe base trajectory can defeat correction (p. 9).
- survey_included: yes
- verification_level: light

## Problem

RGB navigation foundation policies may output colliding trajectories under scene/camera distribution changes.

## Mechanism

Estimated top-down ranges produce repulsive vectors that adjust base-policy local trajectories (pp. 3-5).

## Baselines and controls

NoMaD/ViNT with and without CARE under exploration and image-goal tasks; platform-specific tuning (p. 6).

## Platform and setup

LoCoBot on TurtleBot4 base, TurtleBot4 and RoboMaster S1 with per-platform parameters and low-speed constraints (pp. 6, 14).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. A postprocessor is not a formal safety shield; reflective/transparent obstacles and occluded motion remain perception failures.

## Sensors

Monocular RGB, UniDepthV2 estimated depth; no additional physical range sensor.

## Compute and latency

Depth estimation plus base navigation inference; complete physical compute placement not retained in selected passages.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Monocular depth errors, restricted range/FOV and an unsafe base trajectory can defeat correction (p. 9).

## Transfer conditions

A postprocessor is not a formal safety shield; reflective/transparent obstacles and occluded motion remain perception failures.

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

- **p. 9, Selected source passage.** "CARE adjusts but does not generate trajectories."
  Adds a lightweight correction mechanism while exposing the perception assumptions a safety claim would need.

## Survey-usable statements

### Supported

- Trajectory correction improves collision-avoidance behavior within the evaluated speed/scenario conditions. Adds a lightweight correction mechanism while exposing the perception assumptions a safety claim would need.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. A postprocessor is not a formal safety shield; reflective/transparent obstacles and occluded motion remain perception failures.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 4, 5, 6, 9, 14; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

We propose CARE (Collision Avoidance via Repulsive Estimation) to improve the robustness of learning-based visual navigation methods. Recently, visual navigation models, particularly foundation models, have demonstrated promising performance by generating viable trajectories using only RGB images. However, these policies can generalize poorly to environments containing out-of-distribution (OOD) scenes characterized by unseen objects or different camera setups (e.g., variations in field of view, camera pose, or focal length). Without fine-tuning, such models could produce trajectories that lead to collisions, necessitating substantial efforts in data collection and additional training. To address this limitation, we introduce CARE, an attachable module that enhances the safety of visual navigation without requiring additional range sensors or fine-tuning of pretrained models. CARE can be integrated seamlessly into any RGB-based navigation model that generates local robot trajectories. It dynamically adjusts trajectories produced by a pretrained model using repulsive force vectors computed from depth images estimated directly from RGB inputs. We evaluate CARE by integrating it with state-of-the-art visual navigation models across diverse robot platforms. Real-world experiments show that CARE significantly reduces collisions (up to 100%) without compromising navigation performance in goal-conditioned navigation, and further improves collision-free travel distance (up to 10.7×) in exploration tasks. Project page: https://airlab-sogang.github.io/CARE/
