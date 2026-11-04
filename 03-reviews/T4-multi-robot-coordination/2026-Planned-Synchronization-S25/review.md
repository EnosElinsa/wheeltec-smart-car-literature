# Planned synchronization for multi-robot systems with active observations

## Metadata

| Field | Value |
|---|---|
| ID | S25 |
| Title | Planned synchronization for multi-robot systems with active observations |
| Authors | Zhong, Patrick and Rossi, Federico and Shell, Dylan A. |
| Venue | Autonomous Robots |
| Year | 2026 |
| Type | journal |
| DOI | [10.1007/s10514-025-10225-4](https://doi.org/10.1007/s10514-025-10225-4) |
| Official URL | https://link.springer.com/10.1007/s10514-025-10225-4 |
| Theme folder | T4-multi-robot-coordination |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Planned-Synchronization-S25/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Planned-Synchronization-S25/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Planned-Synchronization-S25/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, numerical
- protocol_caveats: none
- platform_class: differential-drive
- platform: Two TurtleBot3 Burger robots stop and pan to obtain relative marker observations before executing formation macro-actions (p. 14).
- boundary_platform: no
- degradation: communication-delay-loss, sensor-fault
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: IMU and ZED Mini/ArUco observations; no global localization
- compute: Centralized policy solution with decentralized projected execution on onboard single-board computers; planning hardware not retained (pp. 3, 14).
- compute_location: onboard
- summary_result: Planned check-ins trade observation cost against uncertainty during formation execution.
- summary_limitation: Inconsistent observations can produce mismatched actions and check-in times; observation-delay treatment requires a delay model (pp. 18, 21).
- survey_included: yes
- verification_level: light

## Problem

Observations and synchronization consume time and energy while uncertain actions increase formation-state uncertainty.

## Mechanism

Macro-action MDP jointly optimizes motion, check-in timing and rescheduling; finite observation delay enters the discount model (pp. 3, 21).

## Baselines and controls

Fixed-stride check-in policies; numerical unicycle models qualitatively matched to hardware uncertainty and observation-cost sweeps (pp. 15-16).

## Platform and setup

Two TurtleBot3 Burger robots stop and pan to obtain relative marker observations before executing formation macro-actions (p. 14).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Designed synchronization and quantified non-idealities do not establish safe reconnection after arbitrary network partitions.

## Sensors

IMU and ZED Mini/ArUco observations; no global localization.

## Compute and latency

Centralized policy solution with decentralized projected execution on onboard single-board computers; planning hardware not retained (pp. 3, 14).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Inconsistent observations can produce mismatched actions and check-in times; observation-delay treatment requires a delay model (pp. 18, 21).

## Transfer conditions

Designed synchronization and quantified non-idealities do not establish safe reconnection after arbitrary network partitions.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Citation is explicitly derived from publisher RIS/metadata and checked against Crossref; formal issue year 2026. Article identifiers remain in the citation record. Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

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

- **p. 21, Selected source passage.** "In practice, measuring the joint state takes a finite amount of time that can depend on the system state and can differ for each agent."
  Adds active observation scheduling to the team-information budget and qualifies an always-connected coordination model.

## Survey-usable statements

### Supported

- Planned check-ins trade observation cost against uncertainty during formation execution. Adds active observation scheduling to the team-information budget and qualifies an always-connected coordination model.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Designed synchronization and quantified non-idealities do not establish safe reconnection after arbitrary network partitions.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 14, 15, 16, 18, 21, 22; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

An important class of robotic applications involves multiple agents cooperating to provide state observations to plan joint actions. We study planning under uncertainty when more than one participant must proactively plan perception and/or communication acts, and decide whether the cost to obtain a state estimate is justified by the benefits accrued by the information thus obtained. The approach we introduce is suitable for settings where observations are of high quality and they—either alone or along with communication—recover the system’s joint state, but the costs incurred mean this happens only infrequently. We formulate the problem as a type of Markov decision process (MDP) to be solved over macro-actions, sidestepping the construction of the full joint belief space, a well-known source of intractability. We then give a suitable Bellman-like recurrence that immediately suggests a means of solution. In their most general form, policies for these problems simultaneously describe (1) low-level actions to be taken, (2) stages when system-wide state is recovered, and (3) commitments to future rescheduling acts. The formulation expresses multi-agency in a variety of distinct practical forms, including: one party assisting by providing observations of, or reference points for, another; several agents communicating sensor information to fuse data and recover joint state; multiple agents coordinating activities to arrive at states that make joint state simultaneously observable to all individuals. Though solved in centralized form over joint states, the MDP is structured to allow decentralized execution, under some assumptions of synchrony in activities. After providing small-scale simulation studies of the general formulation, we discuss a specific scenario motivated by underwater gliders. We report on a physical robot implementation mocked-up to respect these same constraints, showing that joint plans are found and executed effectively by individual robots after appropriate projection. On the basis of our experience with hardware, we examine enhancements to the model that address nonidealities we have identified in practice, including the assumptions regarding synchrony.
