# Multirobot Persistent Monitoring: Minimizing Latency and Number of Robots With Recharging Constraints

## Metadata

| Field | Value |
|---|---|
| ID | R34 |
| Title | Multirobot Persistent Monitoring: Minimizing Latency and Number of Robots With Recharging Constraints |
| Authors | Ahmad Bilal Asghar, Shreyas Sundaram, and Stephen L. Smith |
| Venue | IEEE Transactions on Robotics |
| Year | 2025 (DOI year 2024) |
| Type | journal |
| DOI | [10.1109/tro.2024.3502497](https://doi.org/10.1109/tro.2024.3502497) |
| Official URL | https://ieeexplore.ieee.org/document/10757438/ |
| Theme folder | T6-reliability-deployment |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-Recharge-Monitoring-R34/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Recharge-Monitoring-R34/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-Recharge-Monitoring-R34/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: multi-robot
- evidence_type: numerical
- evidence_all: numerical
- protocol_caveats: none
- platform_class: none
- platform: Graph instances for patrolling, CVRP benchmark instances and a wildfire-monitoring graph built from satellite hotspot data (pp. 12-15).
- boundary_platform: yes
- degradation: energy-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: None; graph-based planning
- compute: Not inspected in this reading.
- compute_location: not-reported
- summary_result: An approximation algorithm and an orienteering heuristic minimize the number of robots that satisfy revisit-latency constraints with periodic depot recharging (pp. 5-16).
- summary_limitation: Battery consumption may be stochastic in practice; multiple depots are future work (p. 16).
- survey_included: yes
- verification_level: light

## Problem

Persistent monitoring must satisfy revisit-latency constraints while robots return to a depot before battery discharge.

## Mechanism

Areas are weighted graph vertices with latency limits; walks are built by an approximation algorithm with a proven ratio and by greedy and orienteering heuristics; a related algorithm minimizes maximum weighted latency for a fixed team (pp. 4-12).

## Baselines and controls

An existing solver and CVRP benchmark instances (pp. 13-15).

## Platform and setup

Simulated patrolling and wildfire monitoring instances (pp. 12-16). Graph instances for patrolling, CVRP benchmark instances and a wildfire-monitoring graph built from satellite hotspot data (pp. 12-15).

## Evidence type and transfer

Strongest coded setting: `numerical`. Numerical evaluation on graphs; no physical robots.

## Sensors

None; graph-based planning.

## Compute and latency

Not inspected in this reading.

## Key quantitative results

- The orienteering heuristic typically gives better solutions than the approximation algorithm on the tested instances (p. 16).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Battery consumption by the robots may be stochastic, requiring risk-averse solutions (p. 16).
- Inspection and recharging times are assumed zero (p. 4).

## Transfer conditions

Deterministic discharge and zero recharge time do not represent docking failures or battery aging.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

The authors state that this article extends their earlier conference work (p. 3); that version is not in the library, and this journal article is counted once.

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

- **p. 4, Sec. III.** "Similarly, the recharging time can also be assumed to be zero."
  Modeling assumption.
- **p. 16, Sec. VIII.** "In practical scenarios, battery consumption by the robots may be stochastic."
  Author-stated limit.

## Survey-usable statements

### Supported

- Recharging constraints can be built into multirobot persistent-monitoring routes with approximation guarantees.

### Not supported

- Physical charging and uncertain discharge are not evaluated.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 3, 4, 12, 15, 16; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

In this article, we study multirobot path planning for persistent monitoring tasks. We consider the case where robots have a limited battery capacity with a discharge time $D$. We represent the areas to be monitored as the vertices of a weighted graph. For each vertex, there is a constraint on the maximum allowable time between robot visits, called the latency. The objective is to find the minimum number of robots that can satisfy these latency constraints while also ensuring that the robots periodically charge at a recharging depot. The decision version of this problem is known to be PSPACE-complete. We present a $O\left(\frac{\log D}{\log\log D}h\log\rho\right)$ approximation algorithm for the problem where $\rho$ is the ratio of the maximum and the minimum latency constraints, and $h$ reflects the ratio of distance of vertices from the depot to their latency constraints. We also present an orienteering-based heuristic to solve the problem and show empirically that it typically provides higher quality solutions than the approximation algorithm. We extend our results to provide an algorithm for the problem of minimizing the maximum weighted latency given a fixed number of robots. We evaluate our algorithms on large problem instances in a patrolling scenario and in a wildfire monitoring application. We also compare the algorithms with an existing solver on benchmark instances.
