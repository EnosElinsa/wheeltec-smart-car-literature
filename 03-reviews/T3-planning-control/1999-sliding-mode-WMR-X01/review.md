# Sliding mode control for trajectory tracking of nonholonomic wheeled mobile robots

## Metadata

| Field | Value |
|---|---|
| ID | X01 |
| Title | Sliding mode control for trajectory tracking of nonholonomic wheeled mobile robots |
| Authors | Jong-Min Yang and Jong-Hwan Kim |
| Venue | IEEE Transactions on Robotics and Automation, vol. 15, no. 3, pp. 578-587 |
| Year | 1999 |
| Type | journal |
| DOI | [10.1109/70.768190](https://doi.org/10.1109/70.768190) |
| Official URL | https://doi.org/10.1109/70.768190 |
| Theme folder | T3-planning-control |
| Batch | supplemental |
| Local files | `01-papers/T3-planning-control/1999-sliding-mode-WMR-X01/paper.pdf` and `02-fulltext/T3-planning-control/1999-sliding-mode-WMR-X01/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/1999-sliding-mode-WMR-X01/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: external-pose-source, offboard-compute
- platform_class: differential-drive
- platform: MIRO robot-soccer robot, 7.5 cm cube (text: "two driving wheels and one passive centered orientable wheel", p. 7)
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: overhead TMC-7 CCD camera (320x240, 30 Hz) for pose
- compute: Pentium-133 host sends RF commands at 9600 bps; 33 ms sampling period
- compute_location: offboard-local
- summary_result: On a MiroSot pitch, the sliding-mode tracker followed straight and curved references from small and large initial errors, while Bloch-Drakunov tracking failed to converge in Y.
- summary_limitation: The robot heading must not be tangent to any circle around the world origin, which restricts feasible paths; robust control under model uncertainty remains open.
- survey_included: context
- verification_level: light

## Problem

Trajectory tracking for nonholonomic wheeled mobile robots is hard because of
Brockett's obstruction, model mismatch, actuator limits, and localization
error. Earlier sliding-mode trackers often used chained-form kinematics or
incomplete posture outputs rather than torque-level dynamics with an explicit
3D polar posture.

## Mechanism

The posture in polar coordinates is feedback-linearized by the computed-torque
method. A sliding-mode law then tracks a reference trajectory asymptotically
and rejects bounded disturbances (integration error, RF command noise, vision
localization error). On the MIRO hardware the control is realized as
integrated velocity commands to LM629 motor chips, because torque is not
directly accessible.

## Baselines and controls

The comparator is the Bloch-Drakunov sliding-mode tracking scheme, run under
the same disturbances.

## Platform and setup

Real-time trials on the MIRO robot-soccer platform (7.5 cm cube, two driving
wheels and a rolling ball, AT89C52, LM629 velocity loops) on a 130 cm x 90 cm
MiroSot pitch. An overhead TMC-7 CCD camera (320x240, 30 Hz) provides the
pose. A Pentium-133 host sends RF commands at 9600 bps, and the sampling
period is 33 ms. Straight-line and curved references are tracked from small
and large initial errors.

## Evidence type and transfer

The controller drives the physical robot, so the evidence is closed-loop
hardware. Pose comes from overhead vision and the control law runs on the
host PC, coded as external pose source and offboard compute. This is a 1999
classic, coded as context for lineage.

## Sensors

Overhead TMC-7 CCD camera for pose; no dead reckoning.

## Compute and latency

A Pentium-133 host computes the control and sends RF commands at 9600 bps,
with a 33 ms sampling period.

## Key quantitative results

- Vision measurement error is about 2.40 cm in position and 4.83° in orientation (p. 8).
- Sampling period 33 ms; RF link at 9600 bps (p. 8).
- The Bloch-Drakunov scheme failed to converge in Y under the same disturbances; the legacy extraction records no values.

## Stated limitations

- The robot must not have a posture whose heading is tangent to any circle around the world origin, which restricts feasible paths in some environments (p. 10).
- Robust control of nonholonomic systems with model uncertainty remains a challenge because the number of control inputs is less than the number of state variables (p. 10).
- Pose is estimated only visually without dead reckoning, so the posture data carry measurement errors (p. 8).

## Transfer conditions

The evidence is a 1999 overhead-vision soccer robot on a small pitch with an
off-board host. Modern LiDAR or GNSS outages are not quantified. A reader
must replace the overhead pose source and check the polar heading constraint
for the intended paths.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. VI, p. 10 | "It was shown that, by applying the sliding mode control, the controlled behavior of a mobile robot is robust against initial condition errors and external disturbances such as integration error, noise in control signal, localization errors, etc." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI, p. 10 | "This constraint causes restriction in planning feasible paths for the robot in some environments." |

## Page-cited excerpts

- **p. 10, Sec. VI.** "It was shown that, by applying the sliding mode control, the controlled behavior of a mobile robot is robust against initial condition errors and external disturbances such as integration error, noise in control signal, localization errors, etc."
  Localization error is treated as a bounded tracking disturbance.
- **p. 10, Sec. VI.** "The proposed algorithm was implemented on a vision-based mobile robot system. The experimental comparative results with a previous scheme shows the superiority of our approach in tracking capability and robustness in the presence of such uncertainties as mentioned above."
  The authors' hardware claim against one earlier scheme.
- **p. 8, experimental setup.** "Indeed, the vision system in the experimental setup has measurement errors of about 2.40 cm for position and 4.83 degree for orientation."
  Sets the disturbance bound used in the experiments.

## Survey-usable statements

### Supported

- Sliding-mode tracking on computed-torque-linearized polar dynamics tolerated bounded localization error on a real small robot where an earlier sliding-mode scheme did not converge (1999 classic; context only).

### Not supported

- Robustness to modern sensing failures such as LiDAR or GNSS outages: not tested.
- Unrestricted path tracking: the heading constraint restricts feasible paths.

## Verification log

- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); legacy quotes found and kept; legacy C6 claim-row excerpt replaced by the authors' path-restriction sentence so that the row shows the qualification; underactuation limitation located on p. 10; the remark about LiDAR and GNSS outages moved to Transfer conditions
- Legacy extraction: automated reviewer (codex), supplemental batch.

## Original abstract

Nonholonomic mobile robots have constraints imposed on the motion that are not integrable, i.e., the constraints cannot be written as time derivatives of some function of the generalized coordinates. The position control of nonholonomic mobile robots has been an important class of control problems. In this paper, we propose a robust tracking control of nonholonomic wheeled mobile robots using sliding mode. The posture of a mobile robot is represented by polar coordinates and the dynamic equation of the robot is feedback-linearized by the computed-torque method. A novel sliding mode control law is proposed for asymptotically stabilizing the mobile robot to a desired trajectory. It is shown that the proposed scheme is robust to bounded external disturbances. Experimental results demonstrate the effectiveness of accurate tracking capability and the robust performance of the proposed scheme.
