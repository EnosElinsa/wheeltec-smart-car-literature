# Predefined-Time Fault-Tolerant Formation Control for Large-Scale Heterogeneous Wheeled Mobile Robot Swarms

## Metadata

| Field | Value |
|---|---|
| ID | X13 |
| Title | Predefined-Time Fault-Tolerant Formation Control for Large-Scale Heterogeneous Wheeled Mobile Robot Swarms |
| Authors | Shiyu Yin, Chen Chen, and Zhengrong Xiang |
| Venue | IEEE Systems Journal, vol. 20, no. 3, pp. 771-780 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/jsyst.2026.3706478](https://doi.org/10.1109/jsyst.2026.3706478) |
| Official URL | https://doi.org/10.1109/jsyst.2026.3706478 |
| Theme folder | T4-multi-robot-coordination |
| Batch | supplemental |
| Local files | `01-papers/T4-multi-robot-coordination/2026-FT-formation-swarm-X13/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-FT-formation-swarm-X13/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2026-FT-formation-swarm-X13/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: fault-recovery-deployment
- evidence_type: numerical
- evidence_all: numerical
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Six numerical heterogeneous wheeled mobile robots (two-wheeled agents 1-3, three-wheeled agents 4-6) and a virtual leader; drive type not reported
- boundary_platform: no
- degradation: actuator-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: None stated (numerical rigid-body models)
- compute: Not reported
- compute_location: not-reported
- summary_result: In numerical simulation of six faulty heterogeneous robots, tracking errors enter a neighborhood of zero before the predefined time of 25 s, with smaller overshoot than FT-FTFC.
- summary_limitation: The authors leave directed and switching topologies and air-ground swarms to future work; evidence is theory plus numerical simulation on an undirected graph.
- survey_included: yes
- verification_level: light

## Problem

Formation control for heterogeneous wheeled mobile robots must meet a user-specified settling time under actuator faults. Finite-time bounds depend on the initial states, fixed-time maps from gains to settling time are implicit, and prescribed-time scaling can be singular. Single-agent fault-tolerant laws do not capture fault propagation over a communication network.

## Mechanism

A two-layer distributed architecture separates formation among reference generators from tracking by the individual robots. Both layers use predefined-time (PdT) control. An adaptive scheme without fault detection and isolation estimates and compensates actuator effectiveness loss and drift within the predefined time over an undirected graph. Fuzzy logic appears among the stated keywords and design elements.

## Baselines and controls

FT-FTFC [21] is the comparator. Other controls are not recorded in the legacy extraction; not verified.

## Platform and setup

Numerical simulation only: six agents and a virtual leader. Agents 1-3 are two-wheeled and agents 4-6 are three-wheeled, with masses and inertias in Table I. Persistent actuator faults act from t = 0 (effectiveness matrices and drift terms).

## Evidence type and transfer

All results are numerical integration of rigid-body models with injected actuator faults. There is no sensor simulation, no physical robot, and no communication impairment beyond the fixed undirected graph.

## Sensors

None stated; the robots are numerical rigid-body models.

## Compute and latency

Not recorded in the legacy extraction; not verified.

## Key quantitative results

- Tracking errors converge to a small neighborhood of zero before the predefined time of 25 s (p. 9).
- Versus FT-FTFC [21]: smaller overshoot and a user-defined convergence bound without a priori fault matrices (p. 9).

## Stated limitations

- Future research will extend the architecture to directed and switching topologies and to cross-domain heterogeneous swarms such as air-ground formations (p. 9).

## Transfer conditions

Legacy reviewer observations: there is no physical robot trial, the network fault-propagation argument motivates the model but does not quantify real network failure rates, and the evidence for fault tolerance is theory plus simulation. A wheeled robot team reusing the controller needs dynamics models close to the numerical ones and an undirected communication graph.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | strong | Sec. I, p. 2 | "More critically, these works fail to adequately consider the complexities arising from dynamic information interactions in MRSs, meaning their control strategies cannot be directly extended to large-scale swarms where local faults may propagate through the communication network." |
| C5 | direct-support | moderate | Sec. V, p. 9 | "Furthermore, the proposed adaptive fault-tolerant control scheme guarantees that, even in the presence of actuator faults, the system can achieve fault-tolerant formation control within the PdT." |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 2, Introduction.** "More critically, these works fail to adequately consider the complexities arising from dynamic information interactions in MRSs, meaning their control strategies cannot be directly extended to large-scale swarms where local faults may propagate through the communication network."
  Network interaction and fault propagation are treated as multi-robot constraints absent from single-agent control.
- **p. 9, Conclusion.** "Furthermore, the proposed adaptive fault-tolerant control scheme guarantees that, even in the presence of actuator faults, the system can achieve fault-tolerant formation control within the PdT."
  Actuator faults are a first-class control condition; the evidence is theory and simulation, not a physical failure experiment.
- **p. 9, Simulation.** "the tracking errors converge to a small neighborhood of zero well before the PdT"
  The headline simulation result.
- **p. 9, Conclusion.** "Future research will extend the proposed architecture to directed and switching topologies for complex communications"
  The authors' stated scope limit.

## Survey-usable statements

### Supported

- A two-layer predefined-time controller with adaptive fault compensation keeps formation errors near zero before 25 s for six simulated heterogeneous wheeled robots under persistent actuator faults (numbers from a light review; re-check before citing).

### Not supported

- The controller was validated on physical robots: the evidence is numerical simulation only.
- The controller handles directed, switching, or lossy networks: the analysis assumes an undirected graph, and other topologies are future work.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: structured extraction converted to the English template; the 25 s result and the stated limitation were located with sentences from the simulation and conclusion sections (p. 9); legacy reviewer observations moved from Stated limitations to Transfer conditions
- Legacy extraction: automated reviewer (codex), supplemental batch.

## Original abstract

This work addresses the fault-tolerant formation control problem involving heterogeneous wheeled mobile robots (WMRs) under undirected network graphs, with predefined-time (PdT) convergence guaranteed. To tackle the system heterogeneity and reduce the complexity of cooperative control design, a distributed control architecture with an embedded reference signal generator is proposed. By introducing the reference generator layer, the original formation control problem is decoupled into two relatively independent subproblems: 1) formation achievement among reference generators and 2) reference tracking for individual robots. PdT control strategies are developed for both layers. Subsequent stability analysis demonstrates that the entire system achieves the desired formation within a specific, user-defined timeframe. Because this duration is completely unaffected by the agents’ initial states, the convergence process is fully predictable. In addition, an adaptive fault-tolerant control scheme is designed for the purpose of handling actuator degradations. This scheme estimates and compensates for fault effects in PdT, ensuring the system remains robust even under actuator faults. The proposed controller guarantees that fault-tolerant formation control is achieved within a PdTframe, maintaining system stability and performance despite actuator failures. To validate these theoretical contributions, comprehensive numerical simulations are conducted using a coordinated group of six WMRs.
