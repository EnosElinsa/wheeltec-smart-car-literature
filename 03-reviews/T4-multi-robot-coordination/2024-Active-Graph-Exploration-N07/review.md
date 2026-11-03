# Multi-Robot Active Graph Exploration with Reduced Pose-SLAM Uncertainty via Submodular Optimization

## Metadata

| Field | Value |
|---|---|
| ID | N07 |
| Title | Multi-Robot Active Graph Exploration with Reduced Pose-SLAM Uncertainty via Submodular Optimization |
| Authors | Ruofei Bai, Shenghai Yuan, Hongliang Guo, Pengyu Yin, Wei-Yun Yau, Lihua Xie |
| Venue | 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/iros58592.2024.10802691](https://doi.org/10.1109/iros58592.2024.10802691) |
| Official URL | https://ieeexplore.ieee.org/document/10802691/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2024-Active-Graph-Exploration-N07/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2024-Active-Graph-Exploration-N07/paper.md` (local only); [publisher BibTeX](../../../01-papers/T4-multi-robot-coordination/2024-Active-Graph-Exploration-N07/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: simulation
- evidence_all: simulation
- protocol_caveats: none
- platform_class: none
- platform: The evaluated environments are simulated two-dimensional graphs, rather than an integrated physical SLAM team.
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: Simulated 2D pose graphs and prior topo-metric information
- compute: Desktop graph optimization; physical distributed placement not evaluated
- compute_location: desktop-offline
- summary_result: Submodular loop selection couples simulated team coverage to a pose-graph objective.
- summary_limitation: The conclusion requires prior topo-metric information and leaves incorporation into a multirobot SLAM system for future work (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Team exploration must balance coverage with loop opportunities for pose estimation.

## Mechanism

After generating coverage paths, the algorithm adds loop edges through non-monotone submodular maximization with approximation bounds for its graph objective (pp. 1-2).

## Baselines and controls

Graph simulation compares approximation algorithms and a greedy loop-selection algorithm; numerical results and complete proofs were not audited (pp. 6, 8).

## Platform and setup

The evaluated environments are simulated two-dimensional graphs, rather than an integrated physical SLAM team.

## Evidence type and transfer

The strongest inspected setting is `simulation`. Graph-objective bounds do not establish communication resilience or closed-loop pose reliability of a physical team.

## Sensors

Simulated 2D pose graphs and prior topo-metric information.

## Compute and latency

Desktop graph optimization; physical distributed placement not evaluated.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- The conclusion requires prior topo-metric information and leaves incorporation into a multirobot SLAM system for future work (p. 8).

## Transfer conditions

Graph-objective bounds do not establish communication resilience or closed-loop pose reliability of a physical team.

## Code and data

Availability and links beyond the publisher artifacts were not independently verified in this targeted reading.

## Version family

The paper explicitly extends N05 (p. 2). It is a distinct team-graph publication, not an additional version of the same evaluated problem.

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

- **p. 8, Selected source passage.** "with simulated graph exploration experiments"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Submodular loop selection couples simulated team coverage to a pose-graph objective.
- Graph-objective bounds do not establish communication resilience or closed-loop pose reliability of a physical team.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. The conclusion requires prior topo-metric information and leaves incorporation into a multirobot SLAM system for future work (p. 8).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 2, 6, 8; Selected abstract, relationship to previous work, simulation setup and conclusion. Complete approximation proofs and numerical tables not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **— This** **paper** **considers** **the** **multi-robot** **active** **graph**
**exploration problem, where robots need to collaboratively cover**
**a** **graph** **environment** **while** **maintaining** **reliable** **pose** **estima-**
**tion** **in** **collaborative** **Simultaneous** **Localization** **and** **Mapping**
**(SLAM).** **Considering** **both** **objectives** **presents** **challenges** **for**
**multi-robot** **pathfinding,** **as** **it** **involves** **the** **expensive** **covariance**
**propagation** **for** **SLAM** **uncertainty** **evaluation,** **especially** **when**
**considering** **various** **combinations** **of** **robots’** **paths.** **To** **reduce**
**the** **computational** **complexity,** **we** **propose** **an** **efficient** **two-**
**stage** **strategy** **where** **exploration** **paths** **are** **first** **generated** **for**
**quick coverage, and then enhanced by adding informative loop-**
**closing** **actions** **along** **the** **paths** **for** **reliable** **pose** **estimation.** **We**
**formulate** **the** **latter** **problem** **as** **a** **non-monotone** **submodular**
**maximization problem by relating SLAM uncertainty with pose**
**graph** **topology,** **which** **(1)** **facilitates** **a** **more** **efficient** **evaluation**
**of** **SLAM** **uncertainty** **than** **covariance** **inference,** **and** **(2)** **allows**
**the** **employment** **of** **approximation** **algorithms** **in** **submodular**
**optimization** **to** **provide** **suboptimality** **guarantees.** **We** **further**
**introduce** **ordering** **heuristics** **to** **improve** **the** **objective** **values**
**while** **preserving** **the** **optimality** **bound.** **Simulation** **experiments**
**over** **randomly** **generated** **graph** **environments** **verify** **the** **effec-**
**tiveness of our methods to achieve quick coverage and enhanced**
**pose** **graph** **reliability,** **and** **benchmark** **the** **performance** **of** **the**
**approximation** **algorithms** **and** **the** **greedy-based** **algorithm** **in**
**the** **loop** **edge** **selection** **problem.** **Our** **implementations** **will** **be**
**open-source** **at** **https://github.com/bairuofei/CGE.**
