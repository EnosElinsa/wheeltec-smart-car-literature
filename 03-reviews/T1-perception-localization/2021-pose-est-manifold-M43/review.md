# Pose Estimation for Ground Robots: On Manifold Representation, Integration, Reparameterization, and Optimization

## Metadata

| Field | Value |
|---|---|
| ID | M43 |
| Title | Pose Estimation for Ground Robots: On Manifold Representation, Integration, Reparameterization, and Optimization |
| Authors | Mingming Zhang, Xingxing Zuo, Yiming Chen, Yong Liu, and Mingyang Li |
| Venue | IEEE Transactions on Robotics, vol. 37, no. 4, pp. 1081-1099 |
| Year | 2021 |
| Type | journal |
| DOI | [10.1109/tro.2020.3043970](https://doi.org/10.1109/tro.2020.3043970) |
| Official URL | https://ieeexplore.ieee.org/document/9325926/ |
| Theme folder | T1-perception-localization |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T1-perception-localization/2021-pose-est-manifold-M43/paper.pdf` and `02-fulltext/T1-perception-localization/2021-pose-est-manifold-M43/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2021-pose-est-manifold-M43/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: customized campus sensor platform (ON AR0144 stereo camera, Bosch BMI 088 IMU, wheel encoders); KAIST Urban vehicles
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: monocular camera (left eye of a stereo pair), wheel encoders, optional IMU
- compute: Intel Core i7-4790 at 2.90 GHz; optimization 9-10 ms versus 8 ms for camera-odometer fusion
- compute_location: desktop-offline
- summary_result: On KAIST city sequences, the second-order manifold with reparameterization and IMU gives the lowest average RMSE, 2.423 m per km, and the lowest drift on five campus sequences.
- summary_limitation: Quadratic manifolds can fail on extremely uneven roads such as farmland, which a quadratic polynomial cannot model.
- survey_included: yes
- verification_level: light

## Problem

Wheel odometers give only 2D velocities, so 6-DoF pose on non-planar ground
is usually either approximated as planar, with an accuracy loss, or
estimated mainly from an IMU, leaving wheel information unused. Ground
robots also meet visual-inertial odometry degeneracies (standing still,
straight motion at constant velocity) more often than handheld or aerial
platforms.

## Mechanism

The local motion manifold is a second-order polynomial. Closed-form 6-DoF
integration uses wheel-odometer measurements on that manifold, and the
manifold is reparameterized periodically so that the representation error
stays statistically characterized. The module sits in an 8-keyframe
sliding-window estimator with a monocular camera and an optional IMU.
Zeroth- and first-order manifolds cannot represent 6-DoF motion and hurt
accuracy when used as constraints.

## Baselines and controls

The comparators are IMU integration, planar odometer integration, MSCKF,
VINS-W, and earlier approximate-manifold IMU fusion. Variants with and
without reparameterization and with and without IMU serve as ablations.

## Platform and setup

Simulation uses piecewise-polynomial and sinusoidal manifolds (camera 10 Hz,
IMU and wheel 100 Hz). Real data: (i) KAIST Urban vehicle sequences (left
PointGrey Flea3 camera, Xsens MTi-300 IMU, RLS LM13 wheel encoders) on
highway and city routes, evaluated as mean RMSE per 1 km; (ii) the authors'
own data on the Zhejiang University Yuquan campus with slopes and terrain
changes: left eye of an ON AR0144 stereo camera (640x400 at 10 Hz), Bosch
BMI 088 IMU (200 Hz), and wheel encoders (100 Hz); positional drift at loop
closure on five sequences.

## Evidence type and transfer

The strongest setting is the authors' own campus data, processed on a
desktop CPU. KAIST errors are open-loop RMSE; the campus ground truth is only
the start-to-end drift. The legacy extraction does not name the robot that
carried the campus sensor suite or its drive type, so the platform is coded
as wheeled-unspecified.

## Sensors

Monocular camera (left eye of a stereo pair), wheel encoders, and an
optional IMU (Xsens MTi-300 on KAIST; Bosch BMI 088 on campus).

## Compute and latency

Runtime was measured on an Intel Core i7-4790 at 2.90 GHz. The added cost
over camera-odometer fusion is small: about 9-10 ms versus 8 ms for the
optimization.

## Key quantitative results

- KAIST city sequences: the second-order manifold with reparameterization and IMU (M2nd+Re+IMU) is best on average, with a mean RMSE of 2.423 m per km; page not located by text search.
- Campus data: the proposed method has the lowest loop-closure drift on five sequences, the IMU further helps, and reparameterization is required; the legacy extraction records no values (pp. 14-15).
- Runtime on an Intel Core i7-4790 (p. 15): optimization takes about 9-10 ms versus 8 ms for camera-odometer fusion; the values were not located by text search.

## Stated limitations

- The manifold representation can fail for robots on an extremely uneven farmland road, which a quadratic polynomial cannot model (pp. 14-15).
- Well-built urban roads are the intended regime (page not located).

## Transfer conditions

The KAIST data come from a road vehicle, and the campus tests use a custom
camera-IMU-encoder payload processed on a desktop-class CPU, not a named
indoor ROS 2 chassis. The method assumes ground that a quadratic manifold
can represent locally.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. VII-B, p. 14 | "We note that, there may be also failure cases for the proposed manifold representation, such as using it for robots on an extremely uneven farmland road, which cannot be properly modeled by a quadratic polynomial." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | weak | Sec. VII-B, p. 13 | "On the other hand, our customized sensor platform consists of a stereo camera system with ON AR0144 imaging sensors, a Bosch BMI 088 IMU, and wheel encoders. For our proposed algorithms, only the left eye of the stereo camera system was used." |

## Page-cited excerpts

- **p. 14, Sec. VII-B.** "We note that, there may be also failure cases for the proposed manifold representation, such as using it for robots on an extremely uneven farmland road, which cannot be properly modeled by a quadratic polynomial."
  The authors' own boundary for the quadratic manifold.
- **p. 13, Sec. VII-B.** "On the other hand, our customized sensor platform consists of a stereo camera system with ON AR0144 imaging sensors, a Bosch BMI 088 IMU, and wheel encoders. For our proposed algorithms, only the left eye of the stereo camera system was used."
  The campus evidence uses a custom low-cost sensor payload with a monocular camera input.

## Survey-usable statements

### Supported

- Integrating wheel-odometer measurements on a second-order motion manifold, with periodic reparameterization, enables 6-DoF pose estimation from wheel odometry and a monocular camera on non-planar ground (numbers from a light review; re-check before citing).
- Reparameterization of the manifold is required for the accuracy gain on the campus data.

### Not supported

- The method works on any terrain: the authors name extremely uneven farmland roads as a failure case.
- The campus results give full-trajectory accuracy: the campus ground truth is only the start-to-end drift.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); no legacy quote dropped; the open-loop RMSE and drift-only ground-truth remark moved from Stated limitations to Evidence type and transfer
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

In this article, we focus on pose estimation dedicated to nonholonomic ground robots with low-cost sensors, by probabilistically fusing measurements from wheel odometers and an exteroceptive sensor. For ground robots, wheel odometers are widely used in pose estimation tasks, especially in applications in planar scenes. However, since wheel odometer only provides two-dimensional (2D) motion measurements, it is extremely challenging to use that for accurate full 6-D pose (3-D position and 3-D orientation) estimation. Traditional methods for 6-D pose estimation with wheel odometers either approximate motion profiles at the cost of accuracy reduction, or rely on other sensors, e.g., inertial measurement unit, to provide complementary measurements. By contrast, we propose a novel motion-manifold-based method for pose estimation of ground robots, which enables to utilize wheel odometers for high-precision 6-D pose estimation. Specifically, the proposed method, first, formulates the motion manifold of ground robots by a parametric representation, second, performs manifold-based 6-D integration with wheel odometer measurements only, and third, reparameterizes manifold representation periodically for error reduction. To demonstrate the effectiveness and applicability of the proposed algorithmic module, we integrate that into a sliding-window pose estimator by using measurements from wheel odometers and a monocular camera. Extensive simulated and real-world experiments are conducted for evaluation, and the proposed algorithm is shown to outperform competing the state-of-the-art algorithms by a significant margin in pose estimation accuracy, especially when deployed in complex, large-scale real-world environments.
