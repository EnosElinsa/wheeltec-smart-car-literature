# Learning‐based model predictive control for improved mobile robot path following using Gaussian processes and feedback linearization

## Metadata

| Field | Value |
|---|---|
| ID | M33 |
| Title | Learning‐based model predictive control for improved mobile robot path following using Gaussian processes and feedback linearization |
| Authors | Jie Wang, Michael T. H. Fader, and Joshua A. Marshall |
| Venue | Journal of Field Robotics, vol. 40, no. 5, pp. 1014-1033 |
| Year | 2023 |
| Type | journal |
| DOI | [10.1002/rob.22165](https://doi.org/10.1002/rob.22165) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.22165 |
| Theme folder | T3-planning-control |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T3-planning-control/2023-LB-MPC-path-M33/paper.pdf` and `02-fulltext/T3-planning-control/2023-LB-MPC-path-M33/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2023-LB-MPC-path-M33/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: external-pose-source
- platform_class: skid-steer
- platform: Clearpath Husky A200 (text: "skid-steer mobile robot", p. 3)
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Swift Navigation Duro RTK GPS, LORD 3DM-GX5-25 IMU; wheel speeds used in analysis
- compute: Dell XPS 15 laptop (i7-7700HQ, 12 GB), ROS Kinetic, Python 2.7; 10 Hz control
- compute_location: not-reported
- summary_result: On an infinite-shaped sand path, GP-FBLMPC reduced lateral and heading path-following errors by 85.31% and 59.2% versus FBLMPC, matching GP-NMPC at lower compute.
- summary_limitation: Offline GP estimation on a full disturbance data set limits use in new unknown environments, and GP uncertainty is not propagated, so predictions can be overconfident.
- survey_included: yes
- verification_level: light

## Problem

High-accuracy path following for skid-steer wheeled robots on off-road sand
and grass. Unmodeled dynamics and wheel-terrain interaction make a nominal
unicycle model insufficient.

## Mechanism

GP-FBLMPC applies feedback-linearized MPC to a fixed unicycle kinematic model
and adds Gaussian-process disturbance models trained on field residuals. Only
the GP mean predictions are used, with no uncertainty propagation. Linear MPC
after feedback linearization avoids iterative nonlinear optimization, and the
steering rate is saturated after the QP.

## Baselines and controls

FBLMPC without GP models, and GP-NMPC (Ostafew et al., 2016).

## Platform and setup

Five outdoor experiment series on a Clearpath Husky A200 on sand and grass,
with scripted infinite, track, and infinite3 paths. The control laptop is a
Dell XPS 15 (i7-7700HQ, 12 GB) with ROS Kinetic on Ubuntu 16.04 and Python
2.7, controlling at 10 Hz. Localization fuses a LORD 3DM-GX5-25 IMU and a
Swift Navigation Duro RTK GPS in a `robot_localization` EKF (about ±1 cm,
30 Hz). The commanded speed was 0.9 m/s; the actual speed was about
0.70-0.75 m/s, near the mechanical limit.

## Evidence type and transfer

All results come from closed-loop field runs. The pose used by the controller
comes from RTK GPS and IMU fusion, coded as an external pose source. The
legacy extraction does not say whether the laptop rode on the robot, so
compute_location is not-reported.

## Sensors

RTK GPS and IMU (gyroscope) for localization; wheel speeds are used in the
analysis.

## Compute and latency

Dell XPS 15 laptop (i7-7700HQ, 12 GB), ROS Kinetic, Python 2.7, 10 Hz
control. The legacy extraction states that GP-FBLMPC needs less computation
than GP-NMPC because it does not iterate and needs fewer GP models; no
timing values are recorded.

## Key quantitative results

- Experiment 1 (infinite path on sand): GP-FBLMPC versus FBLMPC reduced lateral and heading path-following errors by 85.31% and 59.2% (p. 10).
- GP-FBLMPC matched the path-following error of GP-NMPC at lower computational cost and transferred to untrained paths on the same terrain; the legacy extraction records no values (p. 18).
- Commanded speed 0.9 m/s; actual speed about 0.70-0.75 m/s (p. 11).

## Stated limitations

- Offline GP model estimation on a full disturbance data set can limit application in new unknown environments (p. 18).
- Only the GP mean predictions are used, without uncertainty propagation, so multi-step predictions can be overconfident and MPC solutions overoptimistic (p. 18).
- Closed-loop feasibility and stability guarantees for learning-based MPC under probabilistic constraints are left open (p. 18).
- The Husky could not hold 0.9 m/s while turning (p. 11).

## Transfer conditions

The gains rely on centimeter-level RTK GPS and a laptop-class controller.
The GP models are terrain-specific and trained offline. Husky, laptop, and
RTK do not form a tightly resource-constrained stack, and closed-loop
guarantees remain unproven.

## Code and data

A video is given at https://youtu.be/tC09jJQ0OXM. Code and data release are
not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | direct-support | strong | Sec. 6.2, p. 18 | "In the current work, the requirement of offline GP model estimation due to the usage of a full disturbance data set can limit the application of the proposed approach in new unknown environments." |
| C4 | unset | n/a | | |
| C5 | direct-support | strong | Sec. 6.2, p. 18 | "Moreover, the current implementation only used the predicted mean values of the GP models, and we did not consider uncertainty propagation in the GP model approximations." |
| C6 | qualifies | strong | Sec. 3, p. 3 | "Clearpath Husky A200 skid-steer mobile robot" |

## Page-cited excerpts

- **p. 18, Sec. 6.2.** "In the current work, the requirement of offline GP model estimation due to the usage of a full disturbance data set can limit the application of the proposed approach in new unknown environments."
  The learned model does not adapt online to new terrain.
- **p. 18, Sec. 6.2.** "Moreover, the current implementation only used the predicted mean values of the GP models, and we did not consider uncertainty propagation in the GP model approximations."
  GP uncertainty is unused in the controller.
- **p. 18, Sec. 6.1.** "Extensive outdoor tests of five experiments on the Husky A200 mobile robot demonstrate the GP-FBLMPC algorithm is able to reduce the path following errors effectively compared with controllers that do not use GP modeling."
  The authors' summary of the field evidence on one platform.

## Survey-usable statements

### Supported

- GP-learned disturbance models with feedback-linearized MPC reduced lateral path-following error by 85.31% against the same MPC without GP on a sand path (Husky A200, RTK GPS; numbers from a light review; re-check before citing).
- The method reached GP-NMPC accuracy without iterative nonlinear optimization.

### Not supported

- Adaptation to new, unknown terrain without retraining: the GP models are estimated offline.
- Uncertainty-aware or certified control: GP uncertainty is not propagated, and guarantees are open.
- Accuracy without RTK-grade localization: all runs used RTK GPS fused with an IMU.

## Verification log

- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); legacy C3 and C5 quotes found and kept; legacy C6 claim-row excerpt replaced by the platform phrase so that the row shows the qualification, with the original sentence kept as a page-cited excerpt
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

This paper proposes a high-performance path following algorithm that combines Gaussian processes (GP) based learning and feedback linearization (FBL) with model predictive control (MPC) for ground mobile robots operating in off-road terrains, referred to as GP-FBLMPC. The algorithm uses a nominal kinematic model and learns unmodeled dynamics as GP models by using observation data collected during field experiments. Extensive outdoor experiments using a Clearpath Husky A200 mobile robot show that the proposed GP-FBLMPC algorithm's performance is comparable to existing GP learning-based nonlinear MPC (GP-NMPC) methods with respect to the path following errors. The advantage of GP-FBLMPC is that it is generalizable in reducing path following errors for different paths that are not included in the GP models training process, while GP-NMPC methods only work well on exactly the same path on which GP models are trained. GP-FBLMPC is also computationally more efficient than the GP-NMPC because it does not conduct iterative optimization and requires fewer GP models to make predictions over the MPC prediction horizon loop at every time step. Field tests show the effectiveness and generalization of reducing path following errors of the GP-FBLMPC algorithm. It requires little training data to perform GP modeling before it can be used to reduce path-following errors for new, more complex paths on the same terrain (see video at https://youtu.be/tC09jJQ0OXM).
