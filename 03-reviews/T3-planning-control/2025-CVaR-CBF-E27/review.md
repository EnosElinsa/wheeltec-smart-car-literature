# Safe Navigation in Uncertain Crowded Environments Using Risk Adaptive CVaR Barrier Functions

## Metadata

| Field | Value |
|---|---|
| ID | E27 |
| Title | Safe Navigation in Uncertain Crowded Environments Using Risk Adaptive CVaR Barrier Functions |
| Authors | Xinyi Wang, Taekyung Kim, Bardh Hoxha, Georgios Fainekos, and Dimitra Panagou |
| Venue | 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 7669-7676 |
| Year | 2025 |
| Type | conference |
| DOI | [10.1109/iros60139.2025.11246134](https://doi.org/10.1109/iros60139.2025.11246134) |
| Official URL | https://ieeexplore.ieee.org/document/11246134/ |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2025-CVaR-CBF-E27/paper.pdf` and `02-fulltext/T3-planning-control/2025-CVaR-CBF-E27/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-CVaR-CBF-E27/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: simulation
- evidence_all: simulation, theory-only
- protocol_caveats: none
- platform_class: none
- platform: simulated double-integrator robot in a 12 m by 12 m crowd simulator (no wheeled model; p. 6)
- boundary_platform: yes
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: simulated 5 m sensing range; no physical sensor
- compute: not reported; Delta t = 0.1 s is the simulation step
- compute_location: not-reported
- summary_result: With 5 obstacles and sigma 0.05 in simulation, the risk-adaptive CVaR-BF reaches success 0.917 and collision 0.058 versus CrowdNav++ 0.833 and 0.167.
- summary_limitation: The authors note that no solution may exist under the maximum risk level in dynamic scenes, and leave prediction-error quantification and realistic validation to future work.
- survey_included: yes
- verification_level: light

## Problem

When the motion of crowd obstacles is uncertain, a fixed CVaR risk level is either too conservative, making the optimization infeasible, or too permissive, causing collisions.

## Mechanism

At each step, discrete risk candidates are checked in parallel, and the smallest feasible beta below an upper bound is chosen. A dynamic safety zone expands with the relative position and velocity, and sampled CVaR constraints minimally correct a go-to-goal input. The guarantee depends on the predicted distribution and on a feasible solution existing; Remark 1 states that a solution may still not exist.

## Baselines and controls

- CVaR(Dist) with beta = 0.01 and beta = 0.99.
- RCBF(Cone).
- CBF(Cone).
- ORCA.
- CrowdNav.
- CrowdNav++.
- Ablations without the dynamic zone and without risk adaptation.

## Platform and setup

All tests run in a 12 m by 12 m crowd simulator. The robot is a double integrator with Delta t = 0.1 s, a 5 m sensing range, per-axis acceleration below 3 m/s^2, and speed below 2 m/s. Non-cooperative obstacles follow a social force model with speeds 0.3, 0.6, 0.9, and 1.2 m/s and radii 0.3, 0.4, and 0.5 m; each setting uses 120 configurations. Prediction is constant velocity with L = 20 Gaussian position samples (truncated at ±3 sigma), with sigma from 0 to 0.15.

## Evidence type and transfer

The legacy card lists conditional CVaR safety theory and a crowd-simulation benchmark with ablations. There is no hardware experiment.

## Sensors

A simulated 5 m measurement range; no LiDAR or camera fusion system is implemented.

## Compute and latency

Risk candidates are processed in parallel. No CPU, solve time, or hardware control rate is reported; Delta t = 0.1 s is the simulation step.

## Key quantitative results

- 5 obstacles, sigma = 0.05: proposed SR 0.917, FR 1.000, CR 0.058, ATL 13.036 m, ATT 13.092 s; versus CrowdNav++ SR 0.833 and CR 0.167, and ORCA SR 0.417 and CR 0.583 (p. 7, Table I).
- Ablation: without the dynamic zone (distance-based), SR 0.859 and CR 0.133; with fixed beta = 0.01, SR 0.681, FR 0.689, CR 0.007 (p. 8, Table II).
- In the deterministic case (sigma = 0), CrowdNav++ has the highest success rate, so the method is not better than the baselines under every condition (p. 7, Fig. 4a).

## Stated limitations

- Under the maximum allowable risk level, there may still be cases with no solution, particularly in dynamic obstacle environments (p. 4, Remark 1).
- Quantifying the estimation error of human trajectory prediction models, continuous-time formulations, and validation in more realistic scenarios are left to future work (p. 8).

## Transfer conditions

Legacy reviewer observations: a 5.8% collision rate shows that the conditional probabilistic theory is not a zero-collision guarantee. ORCA and the RL baselines use a simpler holonomic model, so the dynamics are not identical across methods. Prediction is constant velocity with a set Gaussian noise and only 20 samples; mismatch with real crowd distributions and solver real-time performance are not tested.

## Code and data

The first page has Paper Page, Video, and Code hyperlink labels; the local text does not expand the URLs. The repository address was not checked and is not guessed.

## Version family

Official IROS 2025 paper. No journal extension or overlap with other papers in this batch is declared.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | weak | Remark 1, p. 4 | "there may still be cases where no solution exists for (18), particularly in dynamic obstacle environments." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Conclusion, p. 8 | "and validating our method in more realistic navigation scenarios." |

## Page-cited excerpts

- **p. 7, VI-B Benchmark Comparisons, Table I.** "Proposed 0.917 1.000 0.058 13.036 13.092"
  The Table I row for 5 obstacles and sigma = 0.05 (SR, FR, CR, ATL, ATT); a 5.8% collision rate remains.
- **p. 4, Remark 1.** "there may still be cases where no solution exists for (18), particularly in dynamic obstacle environments."
  Feasibility is not guaranteed by the adaptive risk level.
- **p. 7, Baselines.** "Note that both ORCA and the RL methods assume a holonomic model, resulting in a simpler problem setup compared to the other methods."
  The baseline dynamics differ from those of the proposed method.
- **p. 7, Results.** "CrowdNav++ achieves the highest success rate since it is trained in the same deterministic environment."
  A counterexample to "best in every condition".
- **p. 8, Conclusion.** "and validating our method in more realistic navigation scenarios."
  Realistic validation is future work.

## Survey-usable statements

### Supported

- Adapting the CVaR risk level per step with a dynamic safety zone raises the simulated success rate over fixed-risk CVaR-BF, CBF, ORCA, and RL baselines at 5 obstacles and sigma = 0.05 (0.917 versus 0.833 for CrowdNav++; number from a light review, re-check before citing).
- Fixed low risk levels are safe but often infeasible (fixed beta = 0.01: CR 0.007 with SR 0.681).

### Not supported

- The method beats every baseline in every setting: CrowdNav++ has the highest success rate in the deterministic case (sigma = 0).
- The method guarantees zero collisions: CR is 0.058 in Table I, and Remark 1 admits infeasible cases.
- Hardware or real-crowd validation: all results are simulation.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; the legacy Table I quote was found and kept; excerpts added from Remark 1, the baseline note, the Fig. 4 discussion, and the conclusion; platform_class none because the simulated robot is a double integrator without a wheeled model
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/783ab7520ca2fd40ce7e0ea3/

## Original abstract

Robot navigation in dynamic, crowded environments poses a significant challenge due to the inherent uncertainties in the obstacle model. In this work, we propose a risk-adaptive approach based on the Conditional Value-at-Risk Barrier Function (CVaR-BF), where the risk level is automatically adjusted to accept the minimum necessary risk, achieving a good performance in terms of safety and optimization feasibility under uncertainty. Additionally, we introduce a dynamic zone-based barrier function which characterizes the collision likelihood by evaluating the relative state between the robot and the obstacle. By integrating risk adaptation with this new function, our approach adaptively expands the safety margin, enabling the robot to proactively avoid obstacles in highly dynamic environments. Comparisons and ablation studies demonstrate that our method outperforms existing social navigation approaches, and validate the effectiveness of our proposed framework. [Paper Page] [Video] [Code].
