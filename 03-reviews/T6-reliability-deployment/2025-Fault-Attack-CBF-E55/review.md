# Safe Control for Nonlinear Systems Under Faults and Attacks via Control Barrier Functions

## Metadata

| Field | Value |
|---|---|
| ID | E55 |
| Title | Safe Control for Nonlinear Systems Under Faults and Attacks via Control Barrier Functions |
| Authors | Hongchao Zhang, Zhouchi Li, and Andrew Clark |
| Venue | IEEE Transactions on Automatic Control, vol. 70, no. 11, pp. 7334-7349 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tac.2025.3571338](https://doi.org/10.1109/tac.2025.3571338) |
| Official URL | https://ieeexplore.ieee.org/document/11006510/ |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2025-Fault-Attack-CBF-E55/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Fault-Attack-CBF-E55/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-Fault-Attack-CBF-E55/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: numerical
- evidence_all: numerical, theory-only
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: abstract feedback-linearized WMR model; separate Boeing 747 lateral model
- boundary_platform: no
- degradation: actuator-fault, sensor-fault
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: abstract position/velocity channels; trusted noise-free WMR heading
- compute: QP with EKF bank; CPU, solver period, and latency not recorded
- compute_location: not-reported
- summary_result: In illustrated WMR and Boeing numerical cases, the proposed controller preserves safety while residual-triggered reconstruction baselines cross the constraints.
- summary_limitation: Candidate fault sets are known and disjoint; joint sensor-actuator attacks remain future work, and the actuator theorem uses a separate noise-free model.
- survey_included: yes
- verification_level: light

## Problem

With known candidate sensor fault/attack patterns or redundant-actuator failure sets, detection followed by reconstruction can react too late to preserve the safe set. The paper seeks safety and target-set stability under those conditions.

## Mechanism

For sensor faults, each EKF excludes a known disjoint fault set, with auxiliary EKFs excluding pairs of sets. Estimate-difference threshold tests reject inconsistent hypotheses. High-order stochastic CBF/CLF constraints over retained estimates define a control QP. Actuator failures use a separate noise-free model, satisfying HOCBF constraints for all candidate diagonal complete-failure matrices. SOS/Positivstellensatz conditions check feasibility.

## Baselines and controls

WMR: residual-threshold detection plus LQR recomputation from Chapter 7.3 of Blanke et al., Diagnosis and Fault-Tolerant Control [13]. Boeing: the same residual detection, followed by failure identification and a reconstructed CBF-CLF QP with G = G L_i.

## Platform and setup

Both cases are numerical. The WMR is feedback-linearized to a double integrator [x, y, x_dot, y_dot], with six channels: duplicated x, duplicated y, v_x, v_y. The legacy card records σ_w = σ_v = 0.05, an additive attack of 2 on channel four from t ≥ 1, y ≥ -0.1 safety, and an origin goal ball of radius 0.05. The four-state Boeing 747 lateral model has three rudder-servo inputs and two redundant actuators: L_1 = diag(1,0,1) at 2.5-5 s and L_2 = diag(0,1,1) after 5 s, with yaw-rate bounds ±0.025. Setup values were inherited, not re-verified.

## Evidence type and transfer

Conditional finite-horizon probability safety theory, high-order CBF/CLF analysis, SOS feasibility checks, and two abstract-model case studies. These are coded numerical, rather than physical hardware or sensor simulation. The separate aircraft case is a boundary example and supplies no wheeled-actuator hardware evidence.

## Sensors

Abstract position/velocity channels with Gaussian/Brownian noise and linear observation models. WMR heading is explicitly attack-free and noise-free. No physical sensor model was recorded. Candidate fault sets are known and mutually disjoint.

## Compute and latency

Quadratic input cost with linear CBF/CLF constraints; m candidate EKFs plus m choose 2 auxiliary EKFs. CPU, solution period, and latency were not recorded. The legacy extraction restricts SOS feasibility treatment to polynomial/linear constant-gain settings, rather than general automatic deployment.

## Key quantitative results

These legacy trajectory observations were located, not re-verified.

- In the illustrated WMR case, HOSCBF-CLF preserves safety and converges, while the residual baseline with threshold 0.1 detects the fault but crosses the boundary (p. 14, Fig. 2).
- In the illustrated Boeing case, the proposed method preserves yaw-rate bounds and converges to zero under two servo failures; the residual baseline with threshold 0.02 crosses the boundary (p. 14, Fig. 3).
- No Monte Carlo success rate, RMSE, repeat count, or physical hardware data was recorded; trajectory plots cannot establish a universal zero-accident rate (pp. 13-14, Sec. VII).

## Stated limitations

- Joint sensor/actuator attacks remain future work (p. 14, Sec. VIII).
- WMR heading is assumed attack-free and noise-free (p. 13, Sec. VII-A); this setup condition does not guarantee safety for attacks on every channel.

## Transfer conditions

Legacy reviewer observations: sensor safety is finite-horizon and probabilistic, conditional on a tightened initial safe set, EKF error events, detectability after pairwise exclusions, control feasibility, and error/threshold conditions. It is not unconditional permanent safety. Known disjoint sets exclude arbitrary unmodeled or joint sensor/actuator faults. The actuator theorem separately needs noise-free dynamics, sufficient redundancy, and complete zero-output failures. General feasibility uses R^p inputs without establishing physical saturation constraints; Boeing noise does not remove the theorem's noise-free premise. Comparisons use residual/reconstruction baselines, without statistical or hardware comparisons to modern fault-tolerant planners.

## Code and data

No author code/data URL or reproducible experiment repository was found in the legacy extraction; availability was not verified.

## Version family

The TAC journal paper extends Clark, Li, and Zhang's CDC 2020 "Control barrier functions for safe CPS under sensor faults and attacks" [56], pp. 796-803, adding high relative degree, actuator failures, and feasibility verification. Count the journal version once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | Fig. 2, Sensor Fault and Attack, p. 14 | "Baseline entered unsafe region while proposed method remains safe and converge to goal region." |
| C6 | qualifies | moderate | Sec. VIII, Conclusion, p. 14 | "Future work in this area will include attacks that jointly affect sensors and actuators." |

## Page-cited excerpts

- **p. 14, Fig. 2, Sensor Fault and Attack.** "Baseline entered unsafe region while proposed method remains safe and converge to goal region."
  This is a numerical WMR trajectory; actual/real states do not mean physical hardware.
- **p. 14, Sec. VII-B, Actuator Failure.** "three rudder servos, which may fail and output zero when failure happens."
  The actuator model has redundant channels and zero-output failure.
- **p. 14, Sec. VII-B, Simulation result.** "The trajectory of the proposed scheme stays in the safe region and converges to 0"
  This is an illustrated Boeing-model trajectory, without repeated-run statistics.
- **p. 14, Sec. VIII, Conclusion.** "Future work in this area will include attacks that jointly affect sensors and actuators."
  The separate sensor and actuator designs must not be combined into a joint-attack guarantee.
- **p. 13, Sec. VII-A, Sensor Fault and Attack.** "attack-free and noise-free"
  This is the exact prose suffix of the heading assumption; the unmatched equation token was removed.

## Survey-usable statements

### Supported

- CBF/CLF constraints over candidate fault hypotheses avoid the detection/reconstruction delay illustrated in numerical WMR and aircraft cases, subject to model and feasibility conditions (light review).

### Not supported

- Physical robot or flight validation: both case studies are numerical.
- Unconditional permanent safety under arbitrary joint attacks: fault sets, error events, horizon, feasibility, and separate model assumptions constrain the results.
- Saturation-aware safety or universal zero failure probability: physical input bounds and statistical hardware evidence are not established.

## Verification log

- 2026-11-02 | host: Codex | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format conversion; heading quote shortened to exact prose suffix; future-work quote expanded to its located conclusion sentence; separate sensor/actuator assumptions retained
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/c6d834f8e970e5742be664ff/
- Legacy provenance: selection_id c6d834f8e970e5742be664ff; PDF SHA-256 089212793bb7eb4c0d62ab781c2399ee08209f2e4de88330cc4be605ceb32329 (inherited, not re-hashed).

## Original abstract

Safety is one of the most important properties of control systems. Sensor faults and attacks and actuator failures may cause errors in the sensor measurements and system dynamics, which leads to erroneous control inputs and hence safety violations. In this article, we improve the robustness against sensor faults and actuator failures by proposing a class of fault-tolerant control barrier functions (FT-CBFs) for nonlinear systems. Our approach maintains a set of state estimators according to fault patterns and incorporates CBF-based constraints to ensure safety under sensor faults. We then propose a framework for joint safety and stability by integrating FT-CBFs with control Lyapunov functions. By utilizing redundancy, we proposed high order CBF-based approach to ensure safety when actuator failures occur. We propose a sum-of-squares-based approach to verify the feasibility of FT-CBFs for both sensor faults and actuator failures. We evaluate our approach via two case studies, namely, a wheeled mobile robot system in the presence of a sensor attack and a Boeing 747 lateral control system under actuator failures.
