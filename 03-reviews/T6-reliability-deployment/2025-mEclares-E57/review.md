# Adaptive ergodic search with energy-aware scheduling for persistent multi-robot missions

## Metadata

| Field | Value |
|---|---|
| ID | E57 |
| Title | Adaptive ergodic search with energy-aware scheduling for persistent multi-robot missions |
| Authors | Kaleb Ben Naveed, Devansh R. Agrawal, Rahul Kumar, and Dimitra Panagou |
| Venue | Autonomous Robots, vol. 49, no. 4, article 27 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1007/s10514-025-10215-6](https://doi.org/10.1007/s10514-025-10215-6) |
| Official URL | https://link.springer.com/10.1007/s10514-025-10215-6 |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2025-mEclares-E57/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-mEclares-E57/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-mEclares-E57/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: traversability-planning-control, fault-recovery-deployment
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation, theory-only
- protocol_caveats: motion-capture-pose, scripted-scenario, few-trials
- platform_class: aerial
- platform: Orin DevQuad quadrotor mission agents; ground rover is a supporting mobile charging station
- boundary_platform: yes
- degradation: communication-partition, energy-limit
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: external Vicon pose; EKF prediction of charging-station position
- compute: Orin NX on quadrotors, Raspberry Pi on rover, unspecified central host; 600 +/- 150 ms for three-agent hardware
- compute_location: mixed
- summary_result: In four-quadrotor simulation, RmeSch reports eight returns with zero interval or minimum-energy violations; hardware demonstrations assume instantaneous recharging.
- summary_limitation: Central-node failure recovery supports safe return but cannot ensure task continuity; experiments assume instantaneous recharging.
- survey_included: yes
- verification_level: light

## Problem

Persistent stochastic-field sampling requires revisiting regions as information decays, while energy-limited robots share exclusive access to a mobile charging station and return safely after central-node failure.

## Mechanism

mEclares uses independent-cell Kalman covariances to define clarity/decay and normalizes observation time needed for target clarity into a target information spatial distribution (TISD), guiding multi-agent ergodic paths. RmeSch combines task/back-to-base segments, sorts candidates by shortest remaining flight time, and commits those passing gap-aware and energy-aware checks. After disconnection, agents use the last committed path and stored return rank for delayed return, while the charging rover stops. The farthest point of its 95% covariance ellipsoid estimates landing-energy reserve.

## Baselines and controls

Information planning: lawnmower and uniform-TISD ergodic methods over five synthetic environments, with 20 random feasible initial states for ergodic means. Scheduling Table 2: Fouad and Beltrame 2022, Bentz et al. 2018, Eclares 2024, gap-aware-only meSch, meSch, and RmeSch. The legacy card records a conflict between prose saying all baselines lack mobile charging and Yes entries for meSch/gap-aware meSch; use per-method table distinctions.

## Platform and setup

Simulation: four quadrotors/one rover in 10 × 10 m, plus a 30-quadrotor scaling case. Six hardware demonstrations use one to three Orin DevQuad quadrotors and a ground mobile-charging rover in FlyLab with 15-camera Vicon. The aerial mission agents make this a boundary-platform paper; the rover is supporting infrastructure. Every experiment assumes instantaneous charging T_ch = 0 and a 15 s buffer. Values are inherited, not re-verified.

## Evidence type and transfer

Stochastic-field/battery-model simulation, physical trajectories/return-scheduling demonstrations, and conditional feasibility proofs. Thirty-agent scale is simulation only. Fig. 10 state of charge follows assumed discharge/instantaneous recharge; no real charging current/voltage curves or charging-hardware specification were recorded. Hardware therefore demonstrates return scheduling rather than a validated physical long-term charging process.

## Sensors

External 15-camera Vicon gives hardware pose. An EKF with known process/measurement covariances predicts mobile-station position. Synthetic target/decay fields define clarity cases, rather than real pollutant or temperature measurements.

## Compute and latency

Orin NX on each quadrotor, Raspberry Pi on the rover. The unspecified central host computes TISD, ergodic/nominal rover paths, and scheduling; onboard agents generate candidates. Julia modules and Python-ROS2 wrapper. Legacy values: average back-to-base optimization 150 ms, nonlinear propagation 30 ms, three-agent hardware latency 600 ± 150 ms with T_E = 1.5 s, candidate generation/tracking 1 Hz/50 Hz. They were not re-verified. O(N log N) concerns scheduling/sorting, not all trajectory optimization.

## Key quantitative results

The following legacy values/plot observations were located, not re-verified.

- In five synthetic environments, clarity-TISD mean clarity deficit is lower than lawnmower/uniform-TISD; only Q = 0 can approach zero, without a recorded unified percentage improvement (pp. 16-18).
- Four-agent simulation: RmeSch and meSch each have eight returns, zero gap violations, and zero minimum-energy violations. Gap-aware-only meSch has four returns/four energy violations; Eclares has eight returns/two gap violations (p. 17, Table 2).
- Thirty-agent simulation reports 3 ± 1% remaining state of charge on return, rather than a long-term hardware fault rate (pp. 18-19).
- Hardware Fig. 10 shows the minimum-energy bound (set to zero) and return intervals satisfied, without recorded collisions under instantaneous-recharge assumptions. Central failure is tested by terminating the central node (pp. 19-21).
- Three-agent hardware latency is 600 ± 150 ms with T_E = 1.5 s; this is not a bound for arbitrary team sizes/networks (p. 20).

## Stated limitations

- Recovery after central-node failure cannot ensure task continuity (p. 21, Sec. 9).

## Transfer conditions

Legacy reviewer observations: feasibility requires initial gap/reserve conditions, a team-size bound, solvable return/landing problems, an available landing controller, a correct worst-case discharge model, and a charging station that does not itself need charging. A 95% covariance ellipsoid is probabilistic rather than an absolute bound under unbounded noise. The battery discharge model is control-independent. Instantaneous recharge does not validate physical charging time, docking success, or aging; theory allows nonzero duration only with initially feasible scheduling. Potential-field avoidance is separate from the energy/interval scheduling guarantee. Independent cells omit spatial correlation, and return paths do not optimize information gain. Central failure permits recovery rather than mission continuity. The legacy card records inconsistent reserve-energy signs and return delays ret*T_delta versus (ret-1)*T_delta, not re-verified here. A wheeled mobile-station implementation still needs autonomous localization, physical charging, docking, and timing validation.

## Code and data

The paper reports simulation/experiment code, Julia RmeSch, a Python-ROS2 wrapper, Docker, and Orin DevQuad resources at [the project repository](https://github.com/kalebbennaveed/mEclares-main.git). The data-availability statement says no datasets were generated or analyzed. Deployment/operation was not verified.

## Version family

Autonomous Robots 49:27 (2025), formal 24-page version. It extends Eclares (ICRA 2024, single-to-multi-agent clarity) and meSch (2024 preprint arXiv:2406.04560), adding central-failure fallback, theory, and hardware. Do not count related family versions as independent evidence.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | qualifies | moderate | Sec. 9, Limitations and future directions, p. 21 | "cannot ensure task continuity under such failure." |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 15, Sec. 8, Results and Discussion.** "instantaneous recharging"
  The experiments use this charging assumption, without validating physical charging duration.
- **p. 19, Sec. 8.3.2, Hardware demonstration.** "NVIDIA Orin NX, while the rover uses a  Raspberry Pi."
  Quadrotor/rover compute have different roles; central host specifications were not recorded.
- **p. 21, Sec. 9, Limitations and future directions.** "cannot ensure task continuity under such failure."
  Central-node recovery does not preserve continuous information-gathering service.

## Survey-usable statements

### Supported

- mEclares combines uncertainty-driven ergodic search with energy-aware exclusive return scheduling, with aerial hardware demonstrations, simulated scaling, and conditional feasibility analysis (light boundary review).

### Not supported

- Validated persistent physical charging: experiments assume instantaneous recharge without current/voltage or charge-duration evidence.
- Uninterrupted missions after central failure: task continuity is explicitly excluded.
- Thirty-agent hardware scalability or general collision-free guarantees: 30 agents are simulated, and scheduling feasibility does not prove arbitrary-obstacle avoidance.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format conversion; charging quote shortened; two unverifiable table/math quotes dropped; aerial boundary, instantaneous recharge, and central-failure limits retained
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/cd1414f9dbfb76c705f6b246/
- Legacy provenance: selection_id cd1414f9dbfb76c705f6b246; PDF SHA-256 8abcb0deddf601dc81ce1de584ad1fee02310df3a3ebed1b50e966cf01a8680c (inherited, not re-hashed).

## Original abstract

Autonomous robots are increasingly deployed for long-term information-gathering tasks, which pose two key challenges: planning informative trajectories in environments that evolve across space and time, and ensuring persistent operation under energy constraints. This paper presents a unified framework, mEclares, that addresses both challenges through adaptive ergodic search and energy-aware scheduling in multi-robot systems. Our contributions are two-fold: (1) we model real-world variability using stochastic spatiotemporal environments, where the underlying information evolves continuously over space and time under process noise. To guide exploration, we construct a target information spatial distribution (TISD) based on clarity, a metric that captures the decay of information in the absence of observations and highlights regions of high uncertainty; and (2) we introduce Robust-meSch ( RmeSch ), an online scheduling method that enables persistent operation by coordinating rechargeable robots sharing a single mobile charging station. Unlike prior work, our approach avoids reliance on preplanned schedules, static or dedicated charging stations, and simplified robot dynamics. Instead, the scheduler supports general nonlinear models, accounts for uncertainty in the estimated position of the charging station, and handles central node failures. The proposed framework is validated through real-world hardware experiments, and feasibility guarantees are provided under specific assumptions. [Code: https://github.com/kalebbennaveed/mEclares-m ain.git][Experiment Video: https://www.youtube.com/watch?v=dmaZDvxJgF8]
