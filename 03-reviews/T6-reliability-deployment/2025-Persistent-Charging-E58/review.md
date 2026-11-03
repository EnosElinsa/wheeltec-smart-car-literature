# The Persistent Robot Charging Problem for Long-Duration Autonomy

## Metadata

| Field | Value |
|---|---|
| ID | E58 |
| Title | The Persistent Robot Charging Problem for Long-Duration Autonomy |
| Authors | Nitesh Kumar, Jaekyung Jackie Lee, Sivakumar Rathinam, Swaroop Darbha, P. B. Sujit, and Rajiv Raman |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 3, pp. 2191-2198 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2024.3524897](https://doi.org/10.1109/lra.2024.3524897) |
| Official URL | https://ieeexplore.ieee.org/document/10819616/ |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2025-Persistent-Charging-E58/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Persistent-Charging-E58/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-Persistent-Charging-E58/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: multi-robot
- evidence_type: numerical
- evidence_all: numerical
- protocol_caveats: none
- platform_class: aerial
- platform: Simulated heterogeneous UAV fleet
- boundary_platform: yes
- degradation: energy-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: No sensor model; known charging and operating durations
- compute: Ubuntu 20.04 NUC, Intel i7-6770HQ, 32 GB RAM; Gurobi; TPWS under 0.01 s on evaluated instances
- compute_location: desktop-offline
- summary_result: In a two-station simulation, selecting UAVs 1, 2, and 7 yielded 58 aggregate flying minutes per 36-minute cycle.
- summary_limitation: Known integer charging and operating times, full-charge cycles, and a common charging depot constrain the scheduling model.
- survey_included: yes
- verification_level: light

## Problem

Schedule periodic recharging for heterogeneous robots while minimizing the number of charging stations. With a fixed station budget, select a subset of robots to maximize aggregate operating time.

## Mechanism

Known integer charging and operating periods define a finite scheduling horizon through their least common multiple (LCM). A one-hot cyclic-state integer linear program (ILP) optimizes initial charge or phase and the maximum concurrent charging demand, with an extension for robot selection. Shortening operating periods creates charge reserves and may reduce the LCM. A delayed robot searches for the earliest feasible phase while the other schedules remain fixed.

## Baselines and controls

Thrift Price Window Scheduling (TPWS), described as an 8-approximation, is the named comparator. The legacy extraction also contrasts original periods with periods shortened by a safety margin of up to 10%.

## Platform and setup

The evidence is numerical scheduling and task simulation: a ten-robot example, ten randomized period instances, and a mission example with seven candidate UAVs, two charging stations, and 30 task locations. The mission uses a simulated speed of 16 m/s, 4000 mAh/22.2 V batteries, and one-minute slots. No physical autonomous docking or multiday hardware operation is reported in the legacy extraction.

## Evidence type and transfer

The scheduling examples evaluate ILP resource allocation and delayed arrivals in simulated UAV missions. They do not demonstrate physical charging reliability, docking, or long-duration operation on wheeled robots. The aerial platform is a boundary case for transferring the charging-resource mechanism.

## Sensors

Sensors are not modeled. Charging and operating durations are known inputs; the routing layer is separated through a given operating-time budget.

## Compute and latency

The simulations use an Ubuntu 20.04 NUC with an Intel i7-6770HQ and 32 GB RAM, using Gurobi. TPWS takes less than 0.01 s on the evaluated instances; ILP computation grows with the LCM. The legacy extraction records the trend in Fig. 5, without a general real-time guarantee for optimal ILP solutions.

## Key quantitative results

- With a 10% safety margin, the modified versus original scheduling horizons were 504 versus 11592 slots in instance 1 and 540 versus 1287 slots in instance 3; these are legacy values, obtained by sacrificing operating time (p. 7, Table I; caption located, table values not re-verified).
- Selecting three of seven UAVs (1, 2, and 7) on two stations yielded 58 aggregate flying minutes in a 36-minute cycle, with individual reserves of 1, 2, and 4 minutes (p. 7).
- When UAV 2 arrived two minutes late, rescheduling allowed charging at minute 3 versus minute 10 under the original schedule (p. 8).
- For power-of-two charging and cycle periods, the legacy extraction records equal station counts for ILPS and TPWS; in the evaluated perturbed instances ILPS needed fewer stations, with no uniform percentage improvement extracted (p. 6, Fig. 4).

## Stated limitations

- Charging and operating durations are known integer inputs; stations are colocated, and partial charging or operation is disallowed except at initial deployment (p. 2).
- The scheduling problem is NP-hard and a large LCM increases the scheduling horizon and computational burden (pp. 1, 4).

## Transfer conditions

Transfer to wheeled robots requires measured route-energy budgets, return-to-station reserves, and reliable charging contact. The legacy extraction flags battery aging, nonlinear charging, docking failure, and random consumption as outside the model. It also cautions that finding a later feasible slot does not establish sufficient remaining charge to wait, and that the LCM-reduction search should not be treated as an independently audited global-optimality guarantee.

## Code and data

The legacy extraction records simulation data at https://github.com/Nitesh-mk/Persistent-Scheduling-Problem-Data-Set.git, a commercial Gurobi solver, and IEEE supplementary material; availability was not verified.

## Version family

Counted as the RA-L 2025 article. The PDF gives January 1, 2025 as the publication date (p. 1); the 2024 digits in the DOI do not establish a 2024 online year. The legacy extraction distinguishes this work from the authors' 2024 routing metaheuristic.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | Sec. VI, p. 7 | "This selection provided a total ﬂying time of 58 minutes within a cycle time of 36 minutes and effectively scheduled the robots on 2 charging stations." |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 7, Sec. VI.** "This selection provided a total ﬂying time of 58 minutes within a cycle time of 36 minutes and effectively scheduled the robots on 2 charging stations."
  This is aggregate flying time across selected UAVs in a simulation, not single-robot endurance or physical charging validation.
- **p. 6, Sec. V.** "The simulations were executed on a computational platform comprising an Ubuntu 20.04 NUC computer, equipped with an Intel i7-6770HQ processor and 32 GB of RAM."
  The reported compute platform is for the scheduling simulations.

## Survey-usable statements

### Supported

- Periodic charging schedules can be optimized for station use and robot selection under known integer-duration assumptions.
- The legacy mission example demonstrates aggregate service-time allocation and delayed-arrival rescheduling in UAV simulation; any numerical citation requires rechecking the PDF.

### Not supported

- The paper validates multiday physical autonomy or autonomous docking on a wheeled robot; the legacy evidence is simulation.
- Reducing the scheduling horizon preserves full operating time; the safety margin shortens the operating period.
- The sum of 58 flying minutes is the endurance of one UAV; it is aggregate time within a 36-minute cycle.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: English template conversion; both legacy quotes retained after exact matching; online-year inference corrected; legacy values located without table or number re-verification
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/6bb20b53f363d3f6154d5eef/.

## Original abstract

This paper introduces a novel formulation for finding the recharging schedule for a fleet of n heterogeneous robots that minimizes utilization of recharging resources. This study provides a foundational framework applicable to Multi-Robot Mission Planning, particularly in scenarios demanding Long-Duration Autonomy (LDA) or other contexts that necessitate periodic recharging of multiple robots. A novel Integer Linear Programming (ILP) model is proposed to calculate the optimal initial conditions (partial charge) for individual robots, leading to minimal utilization of charging stations. This formulation was further generalized to maximize the servicing time for robots when charging stations are limited. The efficacy of the proposed formulation is evaluated through a comparative analysis, measuring its performance against the thrift price scheduling algorithm documented in the existing literature. The findings not only corroborate the effectiveness of the proposed approach but also underscore its potential as a valuable tool in optimizing resource allocation for a range of robotic and engineering applications.
