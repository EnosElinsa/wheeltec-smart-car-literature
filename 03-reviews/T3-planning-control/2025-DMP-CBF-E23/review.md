# Dynamic Movement Primitives With Control Barrier Functions for Constrained Trajectory Planning

## Metadata

| Field | Value |
|---|---|
| ID | E23 |
| Title | Dynamic Movement Primitives With Control Barrier Functions for Constrained Trajectory Planning |
| Authors | Federico Vesentini, Daniele Meli, Nicola Sansonetto, Luca Di Persio, and Riccardo Muradore |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 9, pp. 9416-9421 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3594987](https://doi.org/10.1109/lra.2025.3594987) |
| Official URL | https://ieeexplore.ieee.org/document/11112576/ |
| Theme folder | T3-planning-control |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T3-planning-control/2025-DMP-CBF-E23/paper.pdf` and `02-fulltext/T3-planning-control/2025-DMP-CBF-E23/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2025-DMP-CBF-E23/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation, theory-only
- protocol_caveats: video-only-hardware, few-trials
- platform_class: wheeled-unspecified
- platform: custom-built mobile robot with a ROS2 interface (drive type not recorded in the legacy extraction)
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: not reported (the legacy card found no localization or obstacle sensor model)
- compute: closed-form CBF correction; no processor or solve time reported
- compute_location: not-reported
- summary_result: In a narrow-corridor simulation with two moving obstacles, CMP stays at 0.015 m RMSE from the reference versus 1.304 m for a potential-field DMP.
- summary_limitation: The closed-form safe input holds for a single CBF; combining CBFs, uncertainty, unpredictable dynamic obstacles, and 3D motion are left to future research.
- survey_included: yes
- verification_level: light

## Problem

Standard DMPs cannot guarantee nonlinear motion constraints after the trajectory is generalized. The paper aims to keep the demonstrated shape as closely as possible without slowing down the whole trajectory.

## Mechanism

The DMP is written as a control-affine system, and the closed-form safe input of a single CBF corrects the forcing term, giving Constrained Movement Primitives (CMPs). Separate constraints are built for maximum velocity, obstacle avoidance with a dynamic potential field, and maximum centrifugal acceleration.

## Baselines and controls

- The original DMP.
- A time-rescaled DMP (tau = 1.10).
- A DMP with the dynamic artificial potential field forcing term of Duhé et al. (reference [26]).

## Platform and setup

Simulation: training on a 1000-point elliptical demonstration; a narrow corridor with static point obstacles and two obstacles moving back and forth. Hardware: a custom-built mobile robot with ROS2; a static obstacle of radius about 0.08 m, enlarged by the robot half-width to about 0.15 m; alpha swept from 10 to 50.

## Evidence type and transfer

The legacy card lists theoretical safety and convergence propositions, dynamic-obstacle simulation, and hardware validation on the custom mobile robot with a static circular obstacle. Dynamic obstacles appear only in simulation.

## Sensors

The text does not name the localization or obstacle sensors for the hardware test; LiDAR use cannot be inferred.

## Compute and latency

The CBF correction is closed-form. No CPU or GPU model or measured solve time is reported.

## Key quantitative results

- Reference-trajectory RMSE in the narrow-corridor simulation: CMP 0.015 ± 0.013 m versus potential-field DMP 1.304 ± 0.737 m (p. 5).
- Velocity limit 2.50 m/s: uniform time scaling raises execution time from 3.14 s to 3.50 s, while the CBF slows the trajectory only where needed (p. 4).
- Centrifugal acceleration limited to 12 m/s^2 (p. 5). On hardware, Fig. 4 shows the effect of alpha on smoothness and obstacle distance, without confidence intervals over repeated trials.

## Stated limitations

- The safe control action of Theorem 3 holds only for a single CBF; multiple CBFs are possible only in specific cases such as obstacle avoidance (p. 3).
- Three-dimensional motion with dynamic and unpredictable obstacles, combining different CBFs in one DMP, and uncertainty are left to future research (p. 6).

## Transfer conditions

Legacy reviewer observations: the demonstration is an analytic ellipse, not multi-scene human driving data, so the results do not imply a generalization guarantee for end-to-end learning. The authors' safety and convergence propositions were recorded but not independently checked, including their applicability to complex disconnected safe sets. The hardware obstacle is static.

## Code and data

Code: https://github.com/Vese91/DD-Robot-DMPs (footnote, p. 3); IEEE supplementary video. No dataset is reported. Not run.

## Version family

The text does not claim to extend a conference paper; the method builds on the DMP library of Ginesi et al. and on existing CBF theory. The library counts this DOI once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | weak | Real robot experiments, p. 5 | "we consider a volumetric static circular obstacle" |

## Page-cited excerpts

- **p. 5, IV-C Obstacle Avoidance.** "CMPs (continuous red curve) avoid obstacles by staying closer to the reference trajectory (dashed green curve) than the original DMPs."
  Supports the simulated RMSE comparison against the potential-field DMP.
- **p. 5, Real robot experiments.** "We test our methodology on a custom-built mobile robot controlled via a ROS2 interface."
  The hardware platform is a custom robot; no drive type is recorded.
- **p. 5, Real robot experiments.** "we consider a volumetric static circular obstacle"
  The hardware obstacle is static.
- **p. 3, Remark 1.** "Theorem 3 yields the safe control action (8) only in the case of"
  The closed-form result covers one CBF.
- **p. 6, Conclusion.** "In future research, we will extend the framework to threedimensional motion in presence of dynamic and impredictable obstacles"
  Unpredictable dynamic obstacles are outside the evaluated scope.

## Survey-usable statements

### Supported

- A closed-form CBF correction of the DMP forcing term enforces velocity, obstacle, and centrifugal-acceleration constraints while staying close to the demonstration in the authors' simulation (RMSE 0.015 m versus 1.304 m; number from a light review, re-check before citing).
- A CBF velocity limit slows the trajectory only where needed, whereas uniform time scaling lengthens the whole execution.

### Not supported

- The method is validated on hardware with dynamic obstacles: the hardware obstacle is static.
- The safety result covers arbitrary combinations of constraints: the closed form holds for a single CBF.
- Hardware RMSE or safety rates: the hardware results are plots without repeated-trial statistics.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; legacy RMSE quote dropped because the transcription loses its decimal points; excerpts taken from the obstacle, hardware, Remark 1, and conclusion text
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/3e3715b9853d8a36df7f5f85/

## Original abstract

Dynamic Movement Primitives (DMPs) form a robust framework for trajectory generation based on imitation learning, aiming to replicate the shape of reference trajectories from demonstrations closely. DMPs have been extensively employed for trajectory planning in robotic systems. However, they cannot safely guarantee complex nonlinear constraints, which is essential at the control level. On the other hand, Control Barrier Functions (CBFs) are used to modulate the input of control-affine dynamic systems subject to state-dependent constraints, guaranteeing that the system remains within predefined safe sets while converging towards target states. This letter proposes Constrained Movement Primitives (CMPs), a novel framework that integrates DMPs with CBFs to generate safe-by-construction trajectories subject to nonlinear constraints. We represent DMPs in control-affine form and combine them with the closed-form input provided by CBFs, overcoming the limitations ofexisting iterative optimisation methods for constrained DMPs. We demonstrate that CBFs preserve the goal convergence guarantees of DMPs. Moreover, we validate our approach in simulation and on a real mobile robot subject to nonlinear kinodynamic constraints, concerning maximum Cartesian velocity, obstacle avoidance, and maximum centrifugal acceleration to avoid slippery over curved trajectories.
