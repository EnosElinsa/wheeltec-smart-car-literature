# Robust Slip-Aware Fusion for Mobile Robots State Estimation

## Metadata

| Field | Value |
|---|---|
| ID | M39 |
| Title | Robust Slip-Aware Fusion for Mobile Robots State Estimation |
| Authors | Ehsan Hashemi, Xingkang He, and Karl H. Johansson |
| Venue | IEEE Robotics and Automation Letters, vol. 7, no. 3, pp. 7896-7903 |
| Year | 2022 |
| Type | journal |
| DOI | [10.1109/lra.2022.3184768](https://doi.org/10.1109/lra.2022.3184768) |
| Official URL | https://ieeexplore.ieee.org/document/9801647/ |
| Theme folder | T1-perception-localization |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T1-perception-localization/2022-slip-aware-fusion-M39/paper.pdf` and `02-fulltext/T1-perception-localization/2022-slip-aware-fusion-M39/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2022-slip-aware-fusion-M39/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: fault-recovery-deployment
- evidence_type: online-hardware
- evidence_all: online-hardware
- protocol_caveats: none
- platform_class: skid-steer
- platform: Clearpath Jackal
- boundary_platform: no
- degradation: wheel-slip, terrain
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: wheel speeds and wheel torque, IMU accelerations and yaw rate
- compute: real-time implementation at 20 ms sampling; computer and runtime not reported
- compute_location: not-reported
- summary_result: Mean longitudinal-speed RMSE of 6.2% (low speed) and 8.8% (high speed) over high-grip, gravel, and slippery surfaces, with 15 tests per scenario.
- summary_limitation: No limitation is stated by the authors; the estimator gives proprioceptive speed and slip only, and coupling with visual-inertial navigation is future work.
- survey_included: yes
- verification_level: full

## Problem

Wheel odometry and inertial speed estimates become unreliable when a mobile
robot experiences large or combined slip, uneven torque distribution (as in
skid steering), or tire-force saturation. GNSS is unavailable indoors and in
urban canyons, so the paper asks how to estimate longitudinal speed and
per-wheel slip from proprioceptive sensors alone, without knowing the road
friction coefficient.

## Mechanism

Each wheel has an observer built on an augmented inertial-tire model: the
states are the lumped LuGre tire deflection and the longitudinal relative
velocity, and the input combines wheel rotational acceleration with the
IMU-derived acceleration of the wheel center. The observer is a Kalman-Bucy
type estimator whose error covariance upper-bounds the mean square error
(Lemma 1) and is uniformly bounded under observability-type assumptions
(Theorem 1). The four wheel-level estimates are transformed to the body frame
and fused by covariance intersection (CI). An adaptive set allocation removes
from the CI set any wheel whose rotational acceleration exceeds a moving mean
over the last four samples. The fused speed re-initializes the wheel
observers. The model uses only tire stiffness and damping parameters and a
load-distribution factor; it does not need the road friction coefficient.
The discrete implementation uses a 20 ms sampling period.

## Baselines and controls

The comparator is a robust linear parameter-varying (LPV) observer with a
switching mechanism from earlier work (reference [22] of the paper), plus the
raw wheel peripheral speed. The comparator appears only in time plots of
individual runs (Figs. 5 and 8); no RMSE is reported for it, so the summary
statistics in Figs. 11 and 12 describe the proposed estimator alone. A
parameter study perturbs the rubber stiffness and damping parameters
sigma_0 and sigma_2 and the load factor kappa by plus or minus 30%.
Rear-wheel-drive and all-wheel-drive configurations are compared.

## Platform and setup

All experiments use a Clearpath Jackal, indoors and outdoors, on high-grip
floors, asphalt, gravel, and wet or mixed-friction surfaces. Scenarios are
mild cornering, obstacle avoidance at the force capacity, obstacle avoidance
with extra traction requests from the motion planner, and cornering with
uneven slip at each wheel. Low-speed tests use at most 0.6 m/s and high-speed
tests 0.6 to 2 m/s; 15 tests were run for each scenario. Some tests reach
slip ratios of at least 80% at individual tires.

## Evidence type and transfer

The estimator runs in real time while the robot drives, so the results are
online hardware evidence; the computer it ran on is not stated. The
estimates are meant for guidance control (p. 3), but no run shows the
controller using them, so the results show estimation accuracy, not a
closed-loop navigation benefit. The text does not describe the sensor that
provides the ground-truth speed labelled "Meas.", and it does not define the
normalization of the percentage RMSE.

## Sensors

Wheel rotational speeds, wheel torque (through the wheel dynamics), and IMU
longitudinal and lateral accelerations and yaw rate. No camera, LiDAR, or
GNSS is used by the estimator.

## Compute and latency

The estimator runs in real time with a 20 ms sampling period. The paper does
not report where it runs (onboard or on a separate computer), the processor,
per-step computation time, or memory use.

## Key quantitative results

- Overall average speed RMSE of 6.2% for all low-speed tests and 8.8% for all high-speed tests, on high-grip, gravel, and slippery surfaces; the normalization of the percentage is not defined (p. 7, Fig. 11).
- RMSE bounded by 17.4% for the hardest case, accelerated high-speed obstacle avoidance with all-wheel actuation, in the parameter study (p. 7, Fig. 12).
- RMSE stays below 18% under plus or minus 30% changes of sigma_0, sigma_2, and kappa for both all- and rear-wheel actuation (p. 7, Fig. 12).
- The LPV comparator shows large errors during long-term large slip between 2.5 s and 4.5 s of one obstacle-avoidance run, while the proposed fusion does not; the comparison is a time plot without a numeric error (p. 5, Fig. 5).
- On gravel, the proposed estimator shows smaller error and faster convergence than the LPV observer without using road-friction information, again in a time plot of one run (p. 6, Fig. 8).

## Stated limitations

- Integration with tightly coupled visual-inertial navigation is named as future work (p. 7).
- The discretization assumes that the model realization does not vary significantly within one sampling interval, which the authors state is valid for the platform at a 0.02 s sampling time (p. 5).

## Transfer conditions

The method needs per-wheel speed and torque signals and an IMU at the center
of gravity, plus tire parameters identified for the target wheels; the paper
identified them by recursive least squares over measured wheel forces, with
an R-squared of 0.9 and 7% RMS error (p. 4). Robots whose motor drivers do
not expose wheel torque, or whose tires differ from the Jackal's, need a new
identification. The method estimates longitudinal speed and slip, not lateral
velocity or a full pose.

## Code and data

The paper does not state that code or data are released.

## Version family

No conference version or extension was found in the library.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. IV-A, p. 5 | "This results in a combined-slip tire force behaviour (during path tracking), which is challenging for existing wheel odometry-based or inertial-based navigation systems" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV, p. 5 | "which is valid for the platform and the estimator with the sampling time" |

## Page-cited excerpts

- **p. 5, Sec. IV-A.** "As a result, the LPV approach has large estimation errors for long-term large slip conditions"
  The comparator fails under persistent slip; the claim is about speed estimation, not navigation.
- **p. 7, Sec. IV-B.** "The overall average of RMSE are 6.2% and 8.8% for all low- and high-speed tests, respectively, on various surfaces."
  The main quantitative result, averaged over all surfaces and scenarios.
- **p. 7, Sec. V.** "the novel proprioceptive observer can also be integrated with existing tightly-coupled visual-inertial navigation systems to address localization and odometry challenges under large-slip conditions."
  Coupling with exteroceptive localization is future work, not an evaluated result.

## Survey-usable statements

### Supported

- A wheel-level observer with covariance-intersection fusion estimates longitudinal speed under combined slip on a skid-steer robot, with 6.2% and 8.8% mean RMSE at low and high speed.
- Excluding wheels with large rotational acceleration from the fusion set is the mechanism used against extreme slip.

### Not supported

- The estimator improves 6-DoF localization or navigation success: no pose or task metric is reported.
- The fusion reduces RMSE versus the LPV observer by a stated amount: the comparator appears only in time plots of single runs.
- The method runs onboard or on low-power hardware: no computer or timing other than the 20 ms sampling period is reported.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read; results text on pp. 4-7 and Figs. 5, 8, 11, 12 captions checked against the PDF; independent fact-check applied | corrections: evidence setting changed to online hardware; compute location set to not reported; lateral-stability statement reworded; comparator shown only in plots; limitations restricted to author statements (see 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

A novel robust and slip-aware speed estimation framework is developed and experimentally verified for mobile robot navigation by designing proprioceptive robust observers at each wheel. The observer for each corner is proved to be consistent, in the sense that it can provide an upper bound of the mean square estimation error (MSE) timely. Under proper conditions, the MSE is proved to be uniformly bounded. A covariance intersection fusion method is used to fuse the wheel-level estimates, such that the updated estimate remains consistent. The estimated slips at each wheel are then used for a robust consensus to improve the reliability of speed estimation in harsh and combined-slip scenarios. As confirmed by indoor and outdoor experiments under different surface conditions, the developed framework addresses state estimation challenges for mobile robots that experience uneven torque distribution or large slip. The novel proprioceptive observer can also be integrated with existing tightly-coupled visual-inertial navigation systems.
