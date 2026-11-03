# Co-NavGPT: Multirobot Cooperative Visual Semantic Navigation Using Vision Language Models

## Metadata

| Field | Value |
|---|---|
| ID | N09 |
| Title | Co-NavGPT: Multirobot Cooperative Visual Semantic Navigation Using Vision Language Models |
| Authors | Bangguo Yu, Qihao Yuan, Kailai Li, Hamidreza Kasaei, Ming Cao |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2025.3645650](https://doi.org/10.1109/lra.2025.3645650) |
| Official URL | https://ieeexplore.ieee.org/document/11302789/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-Co-NavGPT-N09/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-Co-NavGPT-N09/paper.md` (local only); [publisher BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2026-Co-NavGPT-N09/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: multi-robot
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: offboard-compute
- platform_class: legged
- platform: HM3D episodes provide quantitative comparisons; two Go2 quadrupeds provide separate physical demonstrations (pp. 5-7).
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task
- sensors: RGB-D observations, shared map and robot states; hardware localization and initial G-ICP alignment
- compute: Onboard localization; external workstation for perception and planning, not an entirely onboard semantic stack
- compute_location: mixed
- summary_result: Semantic frontier allocation is integrated with geometric execution in simulation and quadruped demonstrations.
- summary_limitation: Failure cases include incomplete reconstruction, multi-floor navigation and object-detection errors (p. 7).
- survey_included: yes
- verification_level: light

## Problem

Multiple robots need semantically informed frontier allocation for target search.

## Mechanism

Co-NavGPT uses a VLM to assign frontiers from a shared map and a Fast Marching Method local policy to execute them (pp. 3, 5).

## Baselines and controls

HM3D comparisons include Cost-Utility, Greedy and Multi-SemExp; comparator identity depends on the metric (p. 6, Table I, rendered).

## Platform and setup

HM3D episodes provide quantitative comparisons; two Go2 quadrupeds provide separate physical demonstrations (pp. 5-7).

## Evidence type and transfer

The strongest inspected setting is `closed-loop-hardware`. Check delayed assignments, map alignment and offboard availability; nominal team operation does not establish communication-loss tolerance.

## Sensors

RGB-D observations, shared map and robot states; hardware localization and initial G-ICP alignment.

## Compute and latency

Onboard localization; external workstation for perception and planning, not an entirely onboard semantic stack.

## Key quantitative results

- In two-agent HM3D episodes, success rate is 0.681 versus 0.625 for Cost-Utility; SPL is 0.369 versus 0.328 for Greedy (p. 6, Table I, rendered PDF checked).
- In one-agent episodes, SPL is 0.236 versus 0.239 for Multi-SemExp (p. 6, Table I); the proposed method does not rank first in every setting.

## Stated limitations

- Failure cases include incomplete reconstruction, multi-floor navigation and object-detection errors (p. 7).

## Transfer conditions

Check delayed assignments, map alignment and offboard availability; nominal team operation does not establish communication-loss tolerance.

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

- **p. 7, Selected source passage.** "are deployed on a workstation equipped with an NVIDIA RTX"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Semantic frontier allocation is integrated with geometric execution in simulation and quadruped demonstrations.
- Check delayed assignments, map alignment and offboard availability; nominal team operation does not establish communication-loss tolerance.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. Failure cases include incomplete reconstruction, multi-floor navigation and object-detection errors (p. 7).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 3, 5, 6, 7, 8; Selected abstract, task/architecture passage, global/local policy, evaluation, deployment and conclusion; Table I visually checked on p. 6. Complete derivation not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—Visual** **target** **navigation** **is** **a** **critical** **capability** **for**
**autonomous** **robots** **operating** **in** **unknown** **environments,** **partic-**
**ularly** **in** **human-robot** **interaction** **scenarios.** **While** **classical** **and**
**learning-based** **methods** **have** **shown** **promise,** **most** **existing** **ap-**
**proaches lack common-sense reasoning and are typically designed**
**for single-robot settings, leading to reduced efficiency and robust-**
**ness** **in** **complex** **environments.** **To** **address** **these** **limitations,** **we**
**introduce Co-NavGPT, a novel framework that integrates a Vision**
**Language** **Model** **(VLM)** **as** **a** **global** **planner** **to** **enable** **common-**
**sense multi-robot visual target navigation. Co-NavGPT aggregates**
**sub-maps** **from** **multiple** **robots** **with** **diverse** **viewpoints** **into** **a**
**unified global map, encoding robot states and frontier regions. The**
**VLM** **uses** **this** **information** **to** **assign** **frontiers** **across** **the** **robots,**
**facilitating coordinated and efficient exploration. Experiments on**
**the Habitat-Matterport 3D (HM3D) demonstrate that Co-NavGPT**
**outperforms** **existing** **baselines** **in** **terms** **of** **success** **rate** **and** **navi-**
**gation efficiency, without requiring task-specific training. Ablation**
**studies** **further** **confirm** **the** **importance** **of** **semantic** **priors** **from**
**the VLM. We also validate the framework in real-world scenarios**
**using quadrupedal robots.**
