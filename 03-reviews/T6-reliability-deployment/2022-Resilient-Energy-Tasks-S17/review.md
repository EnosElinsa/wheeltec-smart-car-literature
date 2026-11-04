# A Resilient and Energy-Aware Task Allocation Framework for Heterogeneous Multirobot Systems

## Metadata

| Field | Value |
|---|---|
| ID | S17 |
| Title | A Resilient and Energy-Aware Task Allocation Framework for Heterogeneous Multirobot Systems |
| Authors | Notomista, Gennaro and Mayya, Siddharth and Emam, Yousef and Kroninger, Christopher and Bohannon, Addison and Hutchinson, Seth and Egerstedt, Magnus |
| Venue | IEEE Transactions on Robotics |
| Year | 2022 |
| Type | journal |
| DOI | [10.1109/tro.2021.3102379](https://doi.org/10.1109/tro.2021.3102379) |
| Official URL | https://ieeexplore.ieee.org/document/9531464/ |
| Theme folder | T6-reliability-deployment |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2022-Resilient-Energy-Tasks-S17/paper.pdf` and `02-fulltext/T6-reliability-deployment/2022-Resilient-Energy-Tasks-S17/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2022-Resilient-Energy-Tasks-S17/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: multi-robot
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, numerical
- protocol_caveats: simulated-agents-on-hardware, scripted-scenario
- platform_class: differential-drive
- platform: Robotarium physical differential-drive robots with simulated cameras, projected aerial capability and simulated low-friction region (pp. 15-17).
- boundary_platform: no
- degradation: sensor-fault, wheel-slip
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Testbed states and modeled camera capabilities; not a hardware camera-failure diagnosis experiment
- compute: Mixed centralized MIQP task allocation and decentralized QP execution architecture; physical compute placement not retained (pp. 14, 17).
- compute_location: not-reported
- summary_result: Capability-aware reassignment maintains team tasks during staged feature loss and blocked-motion scenarios.
- summary_limitation: The authors emphasize that realistic realization requires mixed centralized/decentralized implementation (p. 17).
- survey_included: yes
- verification_level: light

## Problem

Task assignments must change when capabilities fail or environmental interactions reduce robot effectiveness.

## Mechanism

Maps features to capabilities and tasks, encodes priorities with barrier constraints, and updates specialization to reallocate tasks (pp. 3, 7, 14).

## Baselines and controls

Allocation/execution behavior before and after programmed capability loss; current versus outdated allocation numerical comparison (pp. 16-17).

## Platform and setup

Robotarium physical differential-drive robots with simulated cameras, projected aerial capability and simulated low-friction region (pp. 15-17).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Physical motion with virtual cameras/friction does not demonstrate actual sensor fault detection, measured traction recovery or battery endurance.

## Sensors

Testbed states and modeled camera capabilities; not a hardware camera-failure diagnosis experiment.

## Compute and latency

Mixed centralized MIQP task allocation and decentralized QP execution architecture; physical compute placement not retained (pp. 14, 17).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

The authors emphasize that realistic realization requires mixed centralized/decentralized implementation (p. 17).

## Transfer conditions

Physical motion with virtual cameras/friction does not demonstrate actual sensor fault detection, measured traction recovery or battery endurance.

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

- **p. 17, Selected source passage.** "simulated low-friction zone"
  Connects single-robot failure to task-level substitution while distinguishing modeled energy objectives from measured energy autonomy.

## Survey-usable statements

### Supported

- Capability-aware reassignment maintains team tasks during staged feature loss and blocked-motion scenarios. Connects single-robot failure to task-level substitution while distinguishing modeled energy objectives from measured energy autonomy.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Physical motion with virtual cameras/friction does not demonstrate actual sensor fault detection, measured traction recovery or battery endurance.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 3, 7, 14, 15, 16, 17, 18; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

In the context of heterogeneous multirobot teams deployed for executing multiple tasks, this article develops an energy-aware framework for allocating tasks to robots in an online fashion. With a primary focus on long-duration autonomy applications, we opt for a survivability-focused approach. Toward this end, the task prioritization and execution—through which the allocation of tasks to robots is effectively realized—are encoded as constraints within an optimization problem aimed at minimizing the energy consumed by the robots at each point in time. In this context, an allocation is interpreted as a prioritization of a task over all others by each of the robots. Furthermore, we present a novel framework to represent the heterogeneous capabilities of the robots, by distinguishing between the features available on the robots and the capabilities enabled by these features. By embedding these descriptions within the optimization problem, we make the framework resilient to situations, where environmental conditions make certain features unsuitable to support a capability and when component failures on

the robots occur. We demonstrate the efficacy and resilience of the proposed approach in a variety of use-case scenarios, consisting of simulations and real robot experiments.
