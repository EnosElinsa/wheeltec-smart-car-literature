# Graph-Based SLAM-Aware Exploration With Prior Topo-Metric Information

## Metadata

| Field | Value |
|---|---|
| ID | N05 |
| Title | Graph-Based SLAM-Aware Exploration With Prior Topo-Metric Information |
| Authors | Ruofei Bai, Hongliang Guo, Wei-Yun Yau, Lihua Xie |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3420817](https://doi.org/10.1109/lra.2024.3420817) |
| Official URL | https://ieeexplore.ieee.org/document/10577228/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | ieee-supplement-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2024-SLAM-Aware-Exploration-N05/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2024-SLAM-Aware-Exploration-N05/paper.md` (local only); [publisher BibTeX](../../../01-papers/T2-slam-mapping-exploration/2024-SLAM-Aware-Exploration-N05/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: none
- platform_class: skid-steer
- platform: A Pioneer3AT explores campus corridors using wheel/laser estimation and a satellite-derived prior; simulation evaluates graph-based exploration.
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: Planar laser and wheel encoders; satellite-derived topo-metric prior; camera for visualization
- compute: Complete hardware computation placement and control-loop latency not established by this reading
- compute_location: not-reported
- summary_result: Prior-aware exploration explicitly schedules loop closures while retaining a common SLAM back-end.
- summary_limitation: The conclusion targets environments with rich topological prior information; online construction of that prior and a multirobot extension are future work (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Coverage alone can produce exploration routes with weak loop-closure geometry.

## Mechanism

The planner inserts informative loop closures into exploration routes over a supplied topo-metric graph and updates the plan online (pp. 1, 6-8).

## Baselines and controls

All compared planners use Karto SLAM, but some baselines do not require the same prior graph; prior availability must accompany the comparison (pp. 6-7).

## Platform and setup

A Pioneer3AT explores campus corridors using wheel/laser estimation and a satellite-derived prior; simulation evaluates graph-based exploration.

## Evidence type and transfer

The strongest inspected setting is `closed-loop-hardware`. Useful loop opportunities and a compatible prior graph are required; a graph reliability objective is distinct from a calibrated hazardous-pose probability.

## Sensors

Planar laser and wheel encoders; satellite-derived topo-metric prior; camera for visualization.

## Compute and latency

Complete hardware computation placement and control-loop latency not established by this reading.

## Key quantitative results

- No numerical performance-table values were retained in this targeted reading (p. 8).

## Stated limitations

- The conclusion targets environments with rich topological prior information; online construction of that prior and a multirobot extension are future work (p. 8).

## Transfer conditions

Useful loop opportunities and a compatible prior graph are required; a graph reliability objective is distinct from a calibrated hazardous-pose probability.

## Code and data

Availability and links beyond the publisher artifacts were not independently verified in this targeted reading.

## Version family

N07 explicitly extends this single-robot method to team graph exploration; the distinct problems and publisher DOIs are counted separately.

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

- **p. 7, Selected source passage.** "All methods run the same SLAM method called"
  Interpret within the experimental setting and transfer conditions above.

## Survey-usable statements

### Supported

- Prior-aware exploration explicitly schedules loop closures while retaining a common SLAM back-end.
- Useful loop opportunities and a compatible prior graph are required; a graph reliability objective is distinct from a calibrated hazardous-pose probability.

### Not supported

- Unconditional safety, uniform superiority, or successful same-mission recovery beyond the inspected protocol. The conclusion targets environments with rich topological prior information; online construction of that prior and a multirobot extension are future work (p. 8).

## Verification log

- 2026-11-03 | host: Codex | scope: targeted light reading of physical PDF pages 1, 6, 7, 8; Selected abstract, comparison protocol, exploration evaluation discussion, hardware demonstration and conclusion; complete pruning proof and result tables not audited. Abstract and retained excerpts checked against the publisher PDF and local PyMuPDF4LLM transcription; whole paper not verified. | corrections: new targeted review; no legacy claims imported.
- Legacy extraction: none; new targeted follow-up reading. Source identity, page scope and hashes: [source-reading.json](../../../06-data/ieee-supplement-2026-11-03/source-reading.json).

## Original abstract

_**Abstract**_ **—Autonomous** **exploration** **requires** **a** **robot** **to** **explore**
**an unknown environment while constructing an accurate map us-**
**ing Simultaneous Localization and Mapping (SLAM) techniques.**
**Without prior information, the exploration performance is usually**
**conservative** **due** **to** **the** **limited** **planning** **horizon.** **This** **letter** **ex-**
**ploits** **prior** **information** **about** **the** **environment,** **represented** **as** **a**
**topo-metric graph, to benefit both the exploration efficiency and the**
**pose graph reliability in SLAM. Based on the relationship between**
**pose graph reliability and graph topology, we formulate a SLAM-**
**aware path planning problem over the prior graph, which finds a**
**fast exploration path enhanced with the globally informative loop-**
**closing** **actions** **to** **stabilize** **the** **SLAM** **pose** **graph.** **A** **greedy** **algo-**
**rithmisproposedtosolvetheproblem,wheretheoreticalthresholds**
**are derived to significantly prune non-optimal loop-closing actions,**
**without affecting the potential informative ones. Furthermore, we**
**incorporate** **the** **proposed** **planner** **into** **a** **hierarchical** **exploration**
**framework,** **with** **flexible** **features** **including** **path** **replanning,** **and**
**online prior graph update that adds additional information to the**
**prior graph. Simulation and real-world experiments indicate that**
**the proposed method can reliably achieve higher mapping accuracy**
**than** **compared** **methods** **when** **exploring** **environments** **with** **rich**
**topologies,** **while** **maintaining** **comparable** **exploration** **efficiency.**
**Our method has been open-sourced on GitHub.**
