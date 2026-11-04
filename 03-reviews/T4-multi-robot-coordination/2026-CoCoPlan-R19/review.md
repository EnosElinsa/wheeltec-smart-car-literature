# CoCoPlan: Adaptive Coordination and Communication for Multi-Robot Systems in Dynamic and Unknown Environments

## Metadata

| Field | Value |
|---|---|
| ID | R19 |
| Title | CoCoPlan: Adaptive Coordination and Communication for Multi-Robot Systems in Dynamic and Unknown Environments |
| Authors | Xintong Zhang, Junfeng Chen, Yuxiao Zhu, Bing Luo, and Meng Guo |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3656769](https://doi.org/10.1109/lra.2026.3656769) |
| Official URL | https://ieeexplore.ieee.org/document/11361077/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-CoCoPlan-R19/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-CoCoPlan-R19/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-CoCoPlan-R19/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware
- platform_class: wheeled-unspecified
- platform: Simulated teams of up to 100 robots; hardware with four UGVs in an office and two UAVs with four UGVs in a disaster-response scene (pp. 2, 8).
- boundary_platform: no
- degradation: communication-partition
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Robot positions and task observations; ad hoc local communication devices (p. 3)
- compute: Python/ROS on an Intel i7 24-core workstation with RTX 4070Ti for simulation (p. 6); hardware placement not inspected.
- compute_location: not-reported
- summary_result: Co-optimizing task assignment with team-wise intermittent communication raises task completion by 22.4% and lowers communication overhead by 58.6% in simulation (p. 1).
- summary_limitation: No limitation is stated in the inspected passages; the optimality argument assumes recurring communication events (p. 6).
- survey_included: yes
- verification_level: light

## Problem

Teams with close-range communication must decide when and where to reconnect while tasks appear online.

## Mechanism

A branch-and-bound search jointly encodes task assignments and communication events; an adaptive objective trades task efficiency against communication latency; an event-optimization module chooses when, where and how global connectivity is re-established using a predicted communication-quality map (pp. 3-5).

## Baselines and controls

All-time connectivity, fixed-schedule and pairwise intermittent-communication protocols (pp. 6-7).

## Platform and setup

Large-scale simulations with dynamic task distributions and hardware demonstrations (pp. 6-8). Simulated teams of up to 100 robots; hardware with four UGVs in an office and two UAVs with four UGVs in a disaster-response scene (pp. 2, 8).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Quantitative results are simulated; the hardware section shows feasibility through snapshots.

## Sensors

Robot positions and task observations; ad hoc local communication devices (p. 3).

## Compute and latency

Python/ROS on an Intel i7 24-core workstation with RTX 4070Ti for simulation (p. 6); hardware placement not inspected.

## Key quantitative results

- Up to 100 robots are supported in dynamic simulated environments (p. 1).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Theorem 2 assumes that communication events recur indefinitely and that the subproblem is solved to optimality at every communication time (p. 6).

## Transfer conditions

Assumes robots reach planned communication positions on time; state consistency after reconnection is not evaluated.

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

- **p. 3, Sec. II-C.** "Agents cannot maintain the continuous real-time communication due to physical limitations."
  States the communication model.
- **p. 6, Sec. III-C.** "Theorem 2: Assume that communication events recur indefinitely and that at every communication time Algorithm 1 is solved to optimality for the adaptive objective (4)."
  Assumption of the convergence result.

## Survey-usable statements

### Supported

- Reconnection can be planned jointly with task allocation rather than imposed as a fixed schedule.

### Not supported

- Validation of exchanged state at reconnection is not studied.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 6, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Multi-robot systems can greatly enhance efficiency through coordination and collaboration, yet in practice, full-time communication is rarely available and interactions are constrained to close-range exchanges. Existing methods either maintain all-time connectivity, rely on fixed schedules, or adopt pairwise protocols, but none adapt effectively to dynamic spatio-temporal task distributions under limited communication, resulting in suboptimal coordination. To address this gap, we propose CoCoPlan, a unified framework that co-optimizes collaborative task planning and team-wise intermittent communication. Our approach integrates a branch-and-bound architecture that jointly encodes task assignments and communication events, an adaptive objective function that balances task efficiency against communication latency, and a communication event optimization module that strategically determines when, where and how the global connectivity should be re-established. Extensive experiments demonstrate that it outperforms state-of-the-art methods by achieving a 22.4% higher task completion rate, reducing communication overhead by 58.6%, and improving the scalability by supporting up to 100 robots in dynamic environments. Hardware experiments include the complex 2D office environment and large-scale 3D disaster-response scenario.
