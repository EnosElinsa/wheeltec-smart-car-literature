# Anisotropic Terrain-Aware Autonomous Exploration via Image-Domain Perception and Sparse Routing

## Metadata

| Field | Value |
|---|---|
| ID | N08 |
| Title | Anisotropic Terrain-Aware Autonomous Exploration via Image-Domain Perception and Sparse Routing |
| Authors | Yang Zhao, Lelai Zhou, Chen Zhang, Yibin Li |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3723311](https://doi.org/10.1109/lra.2026.3723311) |
| Official URL | https://ieeexplore.ieee.org/document/11652930/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-Anisotropic-Exploration-N08/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-Anisotropic-Exploration-N08/paper.md` (local only); [publisher BibTeX](../../../01-papers/T2-slam-mapping-exploration/2026-Anisotropic-Exploration-N08/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: differential-drive
- platform: FW-001 four-wheel differential-drive and Jueying Lite3 quadruped demonstrations cover terrain exploration.
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Robosense LiDAR with FAST-LIO; field of view differs between embodiments
- compute: Onboard computer; complete deadline and actuator-response distributions not assessed
- compute_location: onboard
- summary_result: Anisotropic terrain costs couple slope and travel direction in autonomous exploration.
- summary_limitation: The authors describe the cost as a heuristic rather than a full dynamics model (p. 4).
- survey_included: yes
- verification_level: light

## Problem

Terrain traversal cost depends on travel direction relative to slope.

## Mechanism

Euler Cost assigns direction-dependent quasi-static traversal costs to a sparse graph; it omits nonlinear slip and suspension transients (p. 4).

## Baselines and controls

Wheeled and quadruped demonstrations use different sensing fields of view; platform differences are not a planner-only ablation (pp. 5, 7).

## Platform and setup

FW-001 four-wheel differential-drive and Jueying Lite3 quadruped demonstrations cover terrain exploration.

## Evidence type and transfer

The strongest inspected setting is `closed-loop-hardware`. A cross-slope geometric proxy and a measured roll angle are distinct from a calibrated rollover probability; verify traction and dynamics on the target chassis.

## Sensors

Robosense LiDAR with FAST-LIO; field of view differs between embodiments.

## Compute and latency

Onboard computer; complete deadline and actuator-response distributions not assessed.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- The authors describe the cost as a heuristic rather than a full dynamics model (p. 4).

## Transfer conditions

A cross-slope geometric proxy and a measured roll angle are distinct from a calibrated rollover probability; verify traction and dynamics on the target chassis.

## Code and data

Availability and links beyond the publisher artifacts were not independently verified in this targeted reading.

## Version family

One publisher DOI is counted. A comprehensive preprint/extension-family search was not performed in this targeted reading.

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

- **p. 4, Selected source passage.** "not a full robot dynamics model"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Anisotropic terrain costs couple slope and travel direction in autonomous exploration.
- A cross-slope geometric proxy and a measured roll angle are distinct from a calibrated rollover probability; verify traction and dynamics on the target chassis.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. The authors describe the cost as a heuristic rather than a full dynamics model (p. 4).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 4, 5, 7, 8; Selected cost-model scope, evaluation setup, deployment/platform discussion and conclusion. Complete derivation and numerical result tables not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—Autonomous** **exploration** **on** **uneven** **terrain** **remains**
**challenging,** **as** **rugged** **terrain** **structures** **not** **only** **reduce** **explo-**
**ration** **performance** **and** **increase** **computational** **burden** **during**
**perception, but also threaten the navigation safety of robots. This**
**article** **proposes** **an** **anisotropic** **terrain-aware** **autonomous** **explo-**
**ration** **framework** **based** **on** **image-domain** **perception** **and** **sparse**
**routing.** **To** **reduce** **the** **computational** **burden,** **we** **convert** **the** **3D**
**point** **cloud** **into** **a** **2.5D** **elevation** **map,** **and** **use** **image** **domain**
**operator convolution combined with hysteresis classifier to extract**
**stable** **and** **sparse** **topological** **navigation** **maps.** **In** **order** **to** **fully**
**consider** **the** **traversal** **cost** **on** **uneven** **terrain,** **we** **designed** **the**
**anisotropic cost model Euler Cost to decouple path direction and**
**terrain** **gradient.** **Rather** **than** **serving** **as** **a** **full** **robot** **dynamics**
**model,** **the** **Euler** **Cost** **is** **formulated** **as** **a** **lightweight** **anisotropic**
**quasi-static** **traversal-cost** **heuristic.** **This** **not** **only** **punishes** **high-**
**risk actions such as cross-slope driving, but also calculates the cost**
**on irregular terrain more realistically. A kinematically consistent**
**frontier strategy was designed to generate smooth and safe explo-**
**ration sequences. We validated our method in various challenging**
**simulation** **scenarios** **and** **real** **uneven** **terrain** **in** **the** **wild,** **and**
**compared it with advanced methods. The results indicate that our**
**method reduces the maximum chassis roll angle by 20%** _**∼**_ **30%**
**while maintaining exploration efficiency similar to state-of-the-art**
**methods.**
