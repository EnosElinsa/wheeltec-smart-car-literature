# A Set-Theoretic Control Strategy for a Platoon of Constrained Differential-Drive Robots With Inter-Vehicle Collision Avoidance

## Metadata

| Field | Value |
|---|---|
| ID | S04 |
| Title | A Set-Theoretic Control Strategy for a Platoon of Constrained Differential-Drive Robots With Inter-Vehicle Collision Avoidance |
| Authors | Rajkumar, Suryaprakash and Tiriolo, Cristian and Lucia, Walter |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2026.3656805](https://doi.org/10.1109/tase.2026.3656805) |
| Official URL | https://ieeexplore.ieee.org/document/11359586/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Set-Theoretic-Platoon-S04/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Set-Theoretic-Platoon-S04/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Set-Theoretic-Platoon-S04/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: none
- platform_class: differential-drive
- platform: Quanser QBOT differential-drive platoon with constrained actuators (p. 8).
- boundary_platform: no
- degradation: actuator-fault
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Leader/follower pose and control messages; QBOT LiDAR, IMU, depth cameras and wheel encoders are listed
- compute: QBOT includes Jetson Orin Nano; exact computation placement/complete latency was not independently established in the selected passages (p. 8).
- compute_location: not-reported
- summary_result: Reachability-based reference delays coordinate constrained platoon tracking and inter-vehicle separation.
- summary_limitation: No extra author-stated limitation retained; reliable inter-agent communication and feasible leader motion are explicit assumptions (p. 3).
- survey_included: yes
- verification_level: light

## Problem

Leader-follower tracking with bounded wheel inputs can produce inter-vehicle collisions without coordinated reference timing.

## Mechanism

Feedback linearizes kinematics, applies set-theoretic MPC to tracking, and adapts follower reference delays using worst-case reachable-set overlap (pp. 3-7).

## Baselines and controls

Physical platoon comparison with a competitor controller; proof conditions include feasible initial placement and a feasible leader path (pp. 7-9).

## Platform and setup

Quanser QBOT differential-drive platoon with constrained actuators (p. 8).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. The adaptive delay is a designed trajectory-reference offset, not evidence of tolerance to packet delay or loss.

## Sensors

Leader/follower pose and control messages; QBOT LiDAR, IMU, depth cameras and wheel encoders are listed.

## Compute and latency

QBOT includes Jetson Orin Nano; exact computation placement/complete latency was not independently established in the selected passages (p. 8).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

No extra author-stated limitation retained; reliable inter-agent communication and feasible leader motion are explicit assumptions (p. 3).

## Transfer conditions

The adaptive delay is a designed trajectory-reference offset, not evidence of tolerance to packet delay or loss.

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

- **p. 3, Selected source passage.** "there exists an inter-agent reliable communication network"
  Separates formation timing from communication degradation in the coordination comparison.

## Survey-usable statements

### Supported

- Reachability-based reference delays coordinate constrained platoon tracking and inter-vehicle separation. Separates formation timing from communication degradation in the coordination comparison.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. The adaptive delay is a designed trajectory-reference offset, not evidence of tolerance to packet delay or loss.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 4, 7, 8, 9; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

In this paper, a novel control strategy is proposed to perform inter-vehicle collision-free platooning of actuator-constrained differential-drive mobile robots. In particular, we consider a Leader-Follower formation scheme where the leader tracks a given trajectory and the follower tracks the leader’s pose with a controlled inter-agent delay to avoid collisions. First, an input-output feedback linearization is applied to the vehicles’ kinematic model. Then, the linearized error dynamics and input constraints are characterized, and a set-theoretic model predictive controller is designed for trajectory tracking purposes. To ensure the absence of inter-vehicle collisions, we resort to worst-case reachability arguments to define an ad hoc collision avoidance policy that adjusts the inter-vehicle delays accordingly. From a theoretical perspective, it is formally proven that the proposed solution guarantees string stability. Moreover, from a practical point of view, the proposed control scheme is validated and contrasted with a competitor scheme using a lab experiment conducted on a formation of Quanser QBOT platform robots.
