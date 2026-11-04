# URGE: Efficient Decentralized Multirobot Exploration Guided by Unknown Regions Under Limited Communication

## Metadata

| Field | Value |
|---|---|
| ID | R22 |
| Title | URGE: Efficient Decentralized Multirobot Exploration Guided by Unknown Regions Under Limited Communication |
| Authors | Qingchen Bi, Xuebo Zhang, Shiyong Zhang, Qianli Dong, and Jing Yuan |
| Venue | IEEE Transactions on Robotics |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tro.2026.3714659](https://doi.org/10.1109/tro.2026.3714659) |
| Official URL | https://ieeexplore.ieee.org/document/11613101/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-URGE-R22/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-URGE-R22/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-URGE-R22/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: wheeled-unspecified
- platform: Simulated Scout 2.0 robots with VLP-16; three real robots with Livox MID360 and Intel NUC in forest, parking-lot and tunnel scenes (pp. 11, 15).
- boundary_platform: no
- degradation: bandwidth-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: 3D LiDAR; SLAM and traversability mapping
- compute: Intel NUC i7-1165G7 on each robot (p. 15).
- compute_location: onboard
- summary_result: Subregion map sharing with cost and load-balanced allocation improves exploration efficiency by 13.3-45.6% and reduces redundant exploration by 22.5-51.5% over the second-best method (p. 2).
- summary_limitation: Assumes reliable SLAM, accurate traversability and a homogeneous team; intermittent links leave regional maps temporarily inconsistent (p. 18).
- survey_included: yes
- verification_level: light

## Problem

Multirobot exploration wastes effort on redundant coverage and consumes bandwidth for map exchange.

## Mechanism

A regionalized exploration information map abstracts subregions by state; robots exchange explored subregions; allocation minimizes total path cost while balancing load; unknown-region guidance adds global geometric cues to route planning (pp. 4-10).

## Baselines and controls

M-TARE, MGGP and other decentralized exploration methods, with allocation and balance ablations (pp. 12-14).

## Platform and setup

Simulations with ideal communication and real-world tests over an ad hoc multihop mesh network (pp. 11, 15). Simulated Scout 2.0 robots with VLP-16; three real robots with Livox MID360 and Intel NUC in forest, parking-lot and tunnel scenes (pp. 11, 15).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop hardware in three scenes; quantitative comparisons with baselines are simulated under ideal communication.

## Sensors

3D LiDAR; SLAM and traversability mapping.

## Compute and latency

Intel NUC i7-1165G7 on each robot (p. 15).

## Key quantitative results

- Removing the joint allocation increases exploration time by 27.2% and team trajectory length by 20.4% in simulation (p. 14).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- URGE assumes reliable SLAM and accurate traversability estimation (p. 18).
- Intermittent connectivity can leave regional maps temporarily inconsistent (p. 18).
- A homogeneous team is assumed (p. 18).

## Transfer conditions

Eventual consistency relies on full-set exchange and a rule that explored overrides unexplored; corrupted or misregistered shared states are not considered.

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

- **p. 11, Sec. VII-B.** "In the simulation, the inter-robot communication is assumed to be ideally connected at all times."
  Communication assumption of the baseline comparisons.
- **p. 4, Sec. III.** "At the start of exploration, the relative positions of all robots are assumed to be known."
  Initialization assumption of the shared frame.

## Survey-usable statements

### Supported

- Compact regional abstractions with a deterministic merge rule support decentralized exploration on hardware.

### Not supported

- Comparative gains are not measured under limited communication.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 4, 11, 14, 15, 18; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Multirobot autonomous exploration often suffers from low efficiency and high communication overhead. To address this, we propose an unknown-region-guided autonomous exploration framework (URGE), which introduces a lightweight, subregion-based environmental representation and information sharing scheme to enable a task allocation strategy that jointly optimizes cost and task load, ultimately achieving spatially dispersed exploration. To capture sufficient spatial information while significantly reducing inter-robot communication volume, the framework incorporates a novel regionalized exploration information map (REIM) that abstracts the environment into subregions with different states. Based on the REIM, a task allocation strategy formulated as a joint optimization problem is proposed. It minimizes the total path cost while balancing the task load across robots, encouraging spatially dispersed exploration and fully leveraging each robot’s exploration capability. Furthermore, we extend prior route planning strategies by introducing global geometric cues. This enables more globally informed exploration routes and promotes the exploration of distant, unknown regions. The proposed framework is comprehensively evaluated using five metrics through extensive comparisons with existing methods, ablation studies, and real-world experiments. Compared with the state-of-the-art methods, URGE improves exploration efficiency by 13.3%–45.6% and reduces redundant exploration by 22.5%–51.5%. The evaluation results also demonstrate that URGE achieves superior cooperative performance and strong practical applicability, while maintaining low communication overhead.
