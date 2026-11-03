# Robust Control Barrier Functions Using Uncertainty Estimation With Application to Mobile Robots

## Metadata

| Field | Value |
|---|---|
| ID | E29 |
| Title | Robust Control Barrier Functions Using Uncertainty Estimation With Application to Mobile Robots |
| Authors | Ersin Daş and Joel W. Burdick |
| Venue | IEEE Transactions on Automatic Control, vol. 70, no. 7, pp. 4766-4773 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tac.2025.3538742](https://doi.org/10.1109/tac.2025.3538742) |
| Official URL | https://ieeexplore.ieee.org/document/10872802/ |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2025-Robust-CBF-Uncertainty-E29/paper.pdf` and `02-fulltext/T3-planning-control/2025-Robust-CBF-Uncertainty-E29/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-Robust-CBF-Uncertainty-E29/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation, theory-only
- protocol_caveats: video-only-hardware, few-trials
- platform_class: tracked
- platform: tracked mobile robot on a 25-degree slope with carpet patches (text and Fig. 3, p. 7); simulated elastic actuator
- boundary_platform: yes
- degradation: terrain, wheel-slip
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: full-state measurement or estimate assumed; hardware sensing described in reference [31], not in this paper
- compute: 50 Hz control loop on the robot; onboard computer described in reference [31]; QP solve time not reported
- compute_location: onboard
- summary_result: On a 25-degree slope with slip, the uncertainty-estimating CBF-QP keeps the tracked robot inside the safe set, whereas the nominal CBF-QP leaves it.
- summary_limitation: The bound delta_L is set beforehand; the authors leave its data-driven estimation and state estimation errors to future work.
- survey_included: yes
- verification_level: light

## Problem

Matched and unmatched uncertainties that depend on state and input break the safety of nominal CBF and HOCBF controllers.

## Mechanism

A linear-gain auxiliary-state estimator estimates the total uncertainty, and the paper derives an ultimate bound on the estimation error. The matched component is compensated by feedforward, and the error bound with an augmented Lyapunov term robustifies the CBF-QP. For HOCBFs with a relative-degree difference of one between input and disturbance, the problem generally becomes an SOCP.

## Baselines and controls

- Nominal CBF-QP (tracked robot hardware).
- HOCBF-QP (elastic actuator simulation).
- Robustified HOCBF [22], which assumes matched disturbances only (simulation comparison).

## Platform and setup

Elastic-joint simulation at 100 Hz. A tracked mobile robot on a 25-degree slope with high-friction carpet patches that induce slip; linear and angular speed limited to ±0.5; safety parameter tau = 1 m for the wall or slope edge; 50 Hz hardware control.

## Evidence type and transfer

The legacy card lists conditional robust-safety theory, an elastic-actuator simulation, and a slope experiment with the tracked robot. The hardware test uses a first-order CBF, not the HOCBF-SOCP.

## Sensors

The estimator requires full-state measurement or estimation and known control inputs. Hardware sensing is described in reference [31] and not in this paper; sensor models are not given here.

## Compute and latency

The hardware control loop runs at 50 Hz (p. 8). The test vehicle and its onboard computation are described in reference [31] (p. 7). Mean or maximum QP solve times are not reported.

## Key quantitative results

- 25-degree slope experiment: the nominal CBF-QP leaves the safe set, while the UE-CBF-QP trajectory keeps h ≥ 0, at a 50 Hz loop rate (p. 8).
- Simulation: UE-HOCBF-QP stays safe with the estimation error inside its bound, while R-HOCBF, which ignores unmatched disturbances, fails (p. 7). No success rates, trial counts, or tables of mean errors are reported.

## Stated limitations

- Future work will estimate the bound delta_L with data-driven techniques and consider state estimation errors (p. 8).
- The theory assumes that the disturbance relative degree is lower than the input relative degree by at most one (p. 3).

## Transfer conditions

Legacy reviewer observations: the theory requires bounded total disturbance and derivative, a full-column-rank input matrix, full state, and known inputs; delta_L currently comes from pre-trials or simulation. The initial condition for the augmented safe set is stricter than h(x0) ≥ 0, and the estimator must be faster than the CBF rate. The hardware tests a first-order CBF, so it does not validate the general HOCBF-SOCP. The proofs were not independently checked, and a few examples give no statistical guarantee over arbitrary terrain.

## Code and data

The legacy card found no code or data link; hardware details are in reference [31]. Not verified.

## Version family

TAC 2025 technical note. No extension of another paper in this batch is declared.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | weak | Fig. 3 caption, p. 7 | "The higher friction carpet patches on the slope result in slip uncertainty when only one track lies on a patch" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | IV-B Experimental Validation, p. 7 | "The test vehicle and its onboard computation are described in Section IV of [31]." |

## Page-cited excerpts

- **p. 8, IV-B Experimental Validation on a Mobile Robot.** "The control loops operated at a 50 Hz rate."
  The hardware control frequency; this is not a single-QP latency.
- **p. 7, IV-B Experimental Validation on a Mobile Robot.** "The test vehicle and its onboard computation are described in Section IV of [31]."
  Hardware details are outside this paper.
- **p. 7, Fig. 3 caption.** "The higher friction carpet patches on the slope result in slip uncertainty when only one track lies on a patch"
  The slip uncertainty is designed into the test.
- **p. 7, IV-A Simulation.** "In addition, the robustified HOCBF method [22] does not guarantee safety, as it only considers matched uncertainty."
  The counterexample for matched-only robustification is from simulation.

## Survey-usable statements

### Supported

- Estimating total uncertainty with an error bound and robustifying the CBF-QP keeps a tracked robot safe on a 25-degree slope with slip, where the nominal CBF-QP fails, in the shown run.
- Matched-only robustification fails under unmatched uncertainty in the authors' elastic-actuator simulation.

### Not supported

- The HOCBF-SOCP is validated on hardware: the hardware uses a first-order CBF.
- Statistical safety over terrain: no repeated-trial rates are reported.
- The result applies directly to wheeled robots: the hardware platform is tracked.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; the legacy 50 Hz quote was found and kept; excerpts added from the experiment text, Fig. 3 caption, and simulation text; compute_location onboard from the located sentence on onboard computation
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/a83235d63c2803874fd99441/

## Original abstract

This article proposes a safety-critical control design approach for nonlinear control affine systems in the presence of matched and unmatched uncertainties. Our constructive framework couples control barrier function (CBF) theory with a new uncertainty estimator to ensure robust safety. We use the estimated uncertainty, along with a derived upper bound on the estimation error, for synthesizing CBFs and safety-critical controllers via a quadratic program-based feedback control law that rigorously ensures robust safety while improving disturbance rejection performance. We extend the method to higher order CBFs (HOCBFs) to achieve safety under unmatched uncertainty, which may cause relative degree differences with respect to control input and disturbances. We assume the relative degree difference is at most one, resulting in a second-order cone constraint. We demonstrate the proposed robust HOCBF method through a simulation of an uncertain elastic actuator control problem and experimentally validate the efficacy of our robust CBF framework on a tracked robot with slope-induced matched and unmatched perturbations.
