# MEF-Explore: Communication-Constrained Multi-Robot Entropy-Field-Based Exploration

## Metadata

| Field | Value |
|---|---|
| ID | R24 |
| Title | MEF-Explore: Communication-Constrained Multi-Robot Entropy-Field-Based Exploration |
| Authors | Khattiya Pongsirijinda, Zhiqiang Cao, Billy Pik Lik Lau, Ran Liu, Chau Yuen, and U-Xuan Tan |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tase.2025.3575237](https://doi.org/10.1109/tase.2025.3575237) |
| Official URL | https://ieeexplore.ieee.org/document/11018365/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2025-MEF-Explore-R24/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2025-MEF-Explore-R24/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2025-MEF-Explore-R24/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: differential-drive
- platform: Gazebo TurtleBots and three physical TurtleBot2 robots on Kobuki bases with Intel NUC i5 and Velodyne LiDAR limited to 7 m (pp. 7, 13).
- boundary_platform: no
- degradation: communication-partition, bandwidth-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: LiDAR occupancy mapping; low-rate position link and range-limited high-rate map link
- compute: Intel NUC i5 on each robot (p. 13).
- compute_location: onboard
- summary_result: Entropy-field exploration with implicit rendezvous gives 21.32% faster exploration and 16.67% higher success than the baseline in real-world experiments (p. 1).
- summary_limitation: Heterogeneous teams and varying communication conditions are left for future evaluation (p. 15).
- survey_included: yes
- verification_level: light

## Problem

Multi-robot exploration usually assumes perfect communication.

## Mechanism

A dynamic graph separates always-available low-speed position sharing from range-limited high-speed map merging; entropies of frontiers and robots guide exploration and trigger rendezvous; a duration-adaptive goal assignment checks goal feasibility (pp. 3-6).

## Baselines and controls

Existing communication-constrained exploration methods including MMPF (pp. 7-13).

## Platform and setup

Two simulated maps with varying team size and range, a no-communication stability test and three-robot hardware runs (pp. 7-14). Gazebo TurtleBots and three physical TurtleBot2 robots on Kobuki bases with Intel NUC i5 and Velodyne LiDAR limited to 7 m (pp. 7, 13).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop hardware with onboard computation; complete partition is evaluated in simulation.

## Sensors

LiDAR occupancy mapping; low-rate position link and range-limited high-rate map link.

## Compute and latency

Intel NUC i5 on each robot (p. 13).

## Key quantitative results

- Without communication, overlapping exploration increases exploration time and failure risk in simulation (p. 13).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The rendezvous proof assumes no error from map merging (p. 15).

## Transfer conditions

Position sharing is assumed always available, which differs from a full partition.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity; no other version is in the library.

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

- **p. 13, Sec. V.** "As shown in Fig. 11(a), we utilize three TurtleBot2 run on a Kobuki base, each equipped with an Intel NUC i5 as the computing unit and a Velodyne LiDAR sensor (scanning range restricted to 7m)."
  Hardware setup.
- **p. 15, Appendix A.** "For mathematical convenience, we assume that there is no error from merging."
  Assumption of the rendezvous analysis.

## Survey-usable statements

### Supported

- Exploration objectives can induce rendezvous for map merging on wheeled hardware.

### Not supported

- Merging is not checked for errors or stale content.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 7, 13, 14, 15; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Collaborative multiple robots for unknown environment exploration have become mainstream due to their remarkable performance and efficiency. However, most existing methods assume perfect robots' communication during exploration, which is unattainable in real-world settings. Though there have been recent works aiming to tackle communication-constrained situations, substantial room for advancement remains for both information-sharing and exploration strategy aspects. In this paper, we propose a Communication-Constrained Multi-Robot Entropy-Field-Based Exploration (MEF-Explore). The first module of the proposed method is the two-layer inter-robot communication-aware information-sharing strategy. A dynamic graph is used to represent a multi-robot network and to determine communication based on whether it is low-speed or high-speed. Specifically, low-speed communication, which is always accessible between every robot, can only be used to share their current positions. If robots are within a certain range, high-speed communication will be available for inter-robot map merging. The second module is the entropy-field-based exploration strategy. Particularly, robots explore the unknown area distributed according to the novel forms constructed to evaluate the entropies of frontiers and robots. These entropies can also trigger implicit robot rendezvous to enhance inter-robot map merging if feasible. In addition, we include the duration-adaptive goal-assigning module to manage robots' goal assignment. The simulation results demonstrate that our MEF-Explore surpasses the existing ones regarding exploration time and success rate in all scenarios. For real-world experiments, our method leads to a 21.32% faster exploration time and a 16.67% higher success rate compared to the baseline.
