# Distributed Safe Navigation for Multi-Robot Systems With Fixed-Time Convergence and Deadlock Resolution

## Metadata

| Field | Value |
|---|---|
| ID | S06 |
| Title | Distributed Safe Navigation for Multi-Robot Systems With Fixed-Time Convergence and Deadlock Resolution |
| Authors | Yin, Jia-Yuan and Yang, Guang-Hong and Wang, Huimin and Wang, Jun-Sheng |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3671566](https://doi.org/10.1109/lra.2026.3671566) |
| Official URL | https://ieeexplore.ieee.org/document/11425779/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Fixed-Time-Deadlock-S06/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Fixed-Time-Deadlock-S06/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Fixed-Time-Deadlock-S06/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, numerical
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: AGILEX mobile-vehicle team with onboard mapping/localization, local-network coordination and staged formation/deadlock cases (p. 7).
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: LiDAR, IMU and inter-robot optimization messages
- compute: Distributed local QPs and fixed-time auxiliary updates over a LAN; exact processor not retained (p. 7).
- compute_location: not-reported
- summary_result: Distributed safety-responsibility updates and deadlock resolution are executed on mobile vehicles.
- summary_limitation: Highly constrained feasibility and robustness under more complex network conditions are identified as future work (p. 7).
- survey_included: yes
- verification_level: light

## Problem

Distributed safety filters can allocate avoidance responsibility conservatively and become trapped in deadlock.

## Mechanism

Decouples inter-agent barrier constraints by regularized primal decomposition, updates local safety responsibility in fixed time and coordinates auxiliary-variable deadlock perturbations (pp. 1, 3-5).

## Baselines and controls

Standard barrier control and deadlock/update ablations in model simulations; physical formation navigation among obstacles (pp. 6-7).

## Platform and setup

AGILEX mobile-vehicle team with onboard mapping/localization, local-network coordination and staged formation/deadlock cases (p. 7).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. A convergence bound is conditional on the modeled coordination process; a low-latency LAN test does not validate partition tolerance.

## Sensors

LiDAR, IMU and inter-robot optimization messages.

## Compute and latency

Distributed local QPs and fixed-time auxiliary updates over a LAN; exact processor not retained (p. 7).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Highly constrained feasibility and robustness under more complex network conditions are identified as future work (p. 7).

## Transfer conditions

A convergence bound is conditional on the modeled coordination process; a low-latency LAN test does not validate partition tolerance.

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

- **p. 7, Selected source passage.** "enhancing the robustness of the algorithm under more complex network conditions."
  Acknowledges implemented distributed deadlock response while narrowing the remaining question to feasibility and degraded-network operation.

## Survey-usable statements

### Supported

- Distributed safety-responsibility updates and deadlock resolution are executed on mobile vehicles. Acknowledges implemented distributed deadlock response while narrowing the remaining question to feasibility and degraded-network operation.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. A convergence bound is conditional on the modeled coordination process; a low-latency LAN test does not validate partition tolerance.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 2, 3, 4, 5, 6, 7; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

This letter addresses the problem of distributed safe navigation for multi-robot systems (MRSs), proposing a comprehensive framework that unifies safety-critical control, real-time navigation, and deadlock resolution. To enable a fully distributed implementation of control barrier function (CBF)-based safety, this work employs a regularized primal decomposition to decouple inter-agent safety constraints. A novel distributed Fixed-Time Stable Gradient Flow (FxTS-GF) algorithm is then designed, which enables each robot to complete the optimal safety responsibility allocation and efficiently solve its local quadratic program (QP) for collision avoidance within each control cycle. Furthermore, the framework incorporates a distributed deadlock resolution mechanism that breaks undesired equilibria through coordination among neighboring robots. Theoretical guarantees are provided for the framework’s anytime-safety, optimality, and fixed-time stability. Finally, the effectiveness and practical applicability of the proposed method are validated through both simulations and hardware experiments on a team of mobile vehicles.
