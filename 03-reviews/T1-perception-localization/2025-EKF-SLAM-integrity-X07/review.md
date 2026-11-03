# Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach

## Metadata

| Field | Value |
|---|---|
| ID | X07 |
| Title | Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach |
| Authors | Osama Abdul Hafez, Mathieu Joerger, and Matthew Spenko |
| Venue | The International Journal of Robotics Research, vol. 44, no. 6, pp. 972-988 |
| Year | 2025 (online 2024) |
| Type | journal |
| DOI | [10.1177/02783649241287797](https://doi.org/10.1177/02783649241287797) |
| Official URL | https://doi.org/10.1177/02783649241287797 |
| Theme folder | T1-perception-localization |
| Batch | supplemental |
| Local files | `01-papers/T1-perception-localization/2025-EKF-SLAM-integrity-X07/paper.pdf` and `02-fulltext/T1-perception-localization/2025-EKF-SLAM-integrity-X07/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2025-EKF-SLAM-integrity-X07/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: localization-mapping
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, simulation
- protocol_caveats: video-only-hardware, few-trials
- platform_class: road-vehicle
- platform: instrumented vehicle with a roof-rack sensor suite (Ouster-64 LiDAR and STIM-300 IMU used); simulated kinematic bicycle model
- boundary_platform: yes
- degradation: data-association-fault
- degradation_observed: none
- evaluation_primary: integrity-reliability
- evaluation_all: residual, designed-degradation, integrity-reliability
- sensors: LiDAR range and bearing to landmarks and STIM-300 IMU (experiment); rear-wheel velocity, steering angle, and range and bearing to landmarks (simulation)
- compute: processor and runtime not reported; truncating fault hypotheses at n_max simultaneous faults makes the cost polynomial
- compute_location: not-reported
- summary_result: In simulation, integrity risk approaches one at x = 20 m as poorly spaced landmarks enter view, while the 2σ envelope and chi-squared detector miss the association error.
- summary_limitation: The method is tailored to EKF-SLAM, a chi-squared detector, and local nearest neighbors; truncating hypotheses at n_max simultaneous faults trades a looser bound for tractable computation.
- survey_included: yes
- verification_level: full

## Problem

Feature-based SLAM can fail when an extracted feature is associated with the
wrong landmark or when a new landmark is created from a feature of an existing
landmark or a moving object. The authors argue that sigma covariance bounds,
the usual safety measure in mobile robotics, give no guarantee because they
ignore such measurement faults, which are rare deterministic errors that
zero-mean Gaussian noise cannot model (p. 2). The paper asks how to upper-bound
the integrity risk, the probability of a large error in a state of interest
without an alarm, for EKF-SLAM, where the landmark map is not known a priori
and every estimated landmark can itself be faulted. EKF-SLAM is chosen because
the authors consider state-of-the-art SLAM techniques too complicated for
rigorous integrity analysis (p. 1).

## Mechanism

The estimator is EKF-SLAM with local nearest-neighbor data association: a
feature is associated with the closest estimated landmark in Mahalanobis
distance when that distance is below a threshold T_a, and a non-associated
feature that is farther than T_n from all landmarks becomes a new landmark,
with T_a no larger than T_n (p. 4). The fault detector is the squared norm of
the standardized innovation; under faults it follows a non-central
chi-squared distribution, and its threshold is set from a false-alarm budget
I_FA (pp. 5-7). Hazardous misleading information is the event that the error
in the state of interest exceeds the alert limit while the detector stays
below its threshold.

The integrity risk is summed over mutually exclusive fault hypotheses. For
each hypothesis, the conditional risk is upper-bounded by the worst-case fault
vector, with an analytic worst-case direction and a line search over its
magnitude (pp. 7-8). The hypothesis probability is bounded by a product of
feature and landmark failure probabilities under an independence assumption,
and the prior robot state estimate is always treated as faulted (p. 8). Feature
failure is mis-association plus unmapped-association; the mis-association
probability is bounded by a sum over the landmarks in the field of view that
uses the landmark separation metric and the non-central chi-squared CDF, and
the unmapped-association probability is an empirical constant (p. 9). Landmark
failure risk is accumulated recursively: the risk of mis-addition or
dynamic-addition when the landmark is created, plus the failure risk of every
feature associated with it later (p. 10). The unknown effect of past faults
is bounded through the fact that the detector did not alarm at the previous
epoch, with an extra risk I_NC (p. 11). Only hypotheses with at most n_max
simultaneous faults are evaluated, and the probability of more faults is
added as a bound; this reduces the cost from O(n^n) to O(n^n_max) in the
number of feature measurements (p. 8). Algorithm 1 lists the steps (p. 12).
In the experiment, landmarks with a failure risk above 1% are excluded from
data association and from the fault hypotheses (pp. 14-15).

## Baselines and controls

The comparators for the integrity risk are the covariance envelope of the
lateral error and the chi-squared detector of the same EKF-SLAM run. No other
integrity monitor, SLAM estimator, or data association method is compared.
The simulation contrasts a map with properly separated landmarks and a map
with two close landmarks at x = 40 m; in the second map the following
landmarks were shifted so that association errors at x = 40 m are not
reflected in later innovations (p. 13). The text calls the envelope 2σ, while
the Fig. 3 caption names 3σ bounds (p. 13). A second simulation varies the
landmark spacing between maps. The experiment uses NDT scan matching-based
batch estimation as ground truth (p. 14) and has no baseline monitor. No
ablation of the 1% isolation step or of n_max is reported.

## Platform and setup

Simulation: a constant-speed kinematic bicycle model follows predefined
way-points in a landmark-rich environment; rear-wheel velocity and steering
angle are the relative measurements, and range and bearing to landmarks are
the absolute measurements (p. 12). Table 1 lists a speed of 25 km/h, a time
step of 0.1 s, a sensor range of 25 m, an alert limit of 1.5 m, velocity and
steering-angle noise standard deviations of 0.1 m/s and 0.4°, a LiDAR noise
standard deviation of 0.2 m, I_FA of 10^-5, P_UA and P_Da of 10^-15, and a
wheelbase of 1.0 m (p. 13). The availability study varies the landmark
spacing from 8 m to 23 m in 1 m increments under a safety requirement of 1e-5;
the paper states 15 maps, although 8-23 m in 1 m steps gives 16 (p. 13).

Experiment: one run on S. Federal Street from 31st to 33rd St. in Chicago,
where, as the authors state with a citation to Nagai et al. (2024), dense tree
clusters degrade or deny GPS coverage (p. 14). The roof rack carries two
Velodyne VLP-16 LiDARs, one Ouster-64 LiDAR, a STIM-300 IMU, and a Novatel
SPAN-CPT DGPS; only the Ouster LiDAR and the STIM-300 were used, with lamp
posts, columns, and tree trunks as landmarks (p. 14, Fig. 9). The state has 15
variables: three for position, three for attitude, three for linear velocity,
and six for gyroscope and accelerometer biases (p. 14). Table 2 lists a LiDAR
rate of 10 Hz, an IMU rate of 125 Hz, a LiDAR noise standard deviation of
0.25 m, an alert limit of 1.5 m, I_FA of 10^-5, and P_UA of 10^-10 (p. 15).
The state of interest is the vehicle lateral offset (p. 15). The scenario was
selected so that EKF-SLAM would fail because of data association errors
(p. 14). Speed, route length, duration, n_max, and who drove the vehicle are
not reported.

## Evidence type and transfer

The strongest evidence is the vehicle run. The paper does not state that the
monitor ran online during driving, the ground truth is a batch estimate, and
the monitor output does not drive the vehicle, so the run is coded as
recorded vehicle data. It is a single run selected to fail, shown only in
Figs. 10 and 11 without tabulated metrics; the only number given for it is
the failure position at 60 m. It is therefore coded with the caveats
video-only-hardware (figure-only results) and few-trials. In that run the
integrity risk crosses the safety threshold after the localization failure,
so it shows the monitor flagging a failure, not warning ahead of it, although
the authors describe it as predicting the failure (p. 15). The simulation
evidence comes from maps designed to produce one association failure.

Data association faults are designed into the simulation and deliberately
selected in the vehicle run, so they are coded as degradation. GNSS denial is
not coded in either degradation field: GPS was not used at all (p. 14), so
the GPS degradation of the street is a property of the site that the
evaluated estimator never encountered, and no result speaks to it. Neither
setting uses a wheeled ground robot: the simulated model is car-like (1.0 m
wheelbase, 25 km/h), and the sensors ride on a passenger vehicle.

## Sensors

The method uses landmark range and bearing from the Ouster LiDAR and the
STIM-300 IMU in the experiment, and rear-wheel velocity, steering angle, and
landmark range and bearing in simulation. GPS was not used because multipath
errors are prevalent even with coverage (p. 14). The VLP-16 LiDARs and the
DGPS were mounted but unused. Ground truth comes from NDT scan matching-based
batch estimation; the paper does not say which sensor data it used.

## Compute and latency

The paper reports no processor, runtime per epoch, or memory use. The only
cost statement is complexity: evaluating all fault hypotheses is exponential,
O(n^n), and truncation at n_max simultaneous faults makes it polynomial,
O(n^n_max), at the price of a looser bound (p. 8).

## Key quantitative results

- In the poorly spaced simulated map, the lateral error grows without being reflected in the 2σ covariance envelope, and the integrity risk peaks at x = 20 m when the two close landmarks enter the field of view (p. 13, Figs. 3 and 5).
- In the same map, the chi-squared detector fails to detect the data association error (p. 13, Fig. 4).
- Near x = 20 m the failure probability of landmark ID-2 jumps up to one in the poorly spaced map, unlike landmark ID-1, and the integrity risk approaches one (p. 13, Fig. 6).
- With landmark spacing varied from 8 m to 23 m and a 1e-5 safety requirement, availability increases as spacing decreases, then drops drastically at high density; the text gives no availability values (p. 14, Fig. 7).
- In the vehicle run, EKF-SLAM fails at 60 m in the x-direction, attributed to few extracted features and close landmarks in Mahalanobis distance (p. 15, Fig. 10).
- The integrity risk rises above the predefined safety threshold after the localization failure in the vehicle run (p. 15, Fig. 11).

## Stated limitations

- The analysis is restricted to EKF-SLAM because state-of-the-art SLAM techniques are considered too complicated for rigorous integrity analysis; the authors argue that EKF-SLAM should be tackled first, before adapting the approach to such estimators (p. 1).
- Evaluating every fault hypothesis is exponential in the number of feature measurements; limiting the hypotheses to n_max simultaneous faults loosens the upper bound, a trade-off between computing time and overconfidence of the bound (p. 8).
- The unmapped-association probability is a constant bounded empirically by parameter identification (p. 9), and the dynamic-addition probability is a constant bounded experimentally (p. 10).
- The derivation assumes that linearization errors can be bounded by a biased Gaussian with inflated covariance and that sensor faults are a single lumped additive and multiplicative quantity (p. 3), and it assumes independence among feature and landmark failure events (p. 8).

## Transfer conditions

The method needs a feature-based map of distinguishable point landmarks
(poles, columns, trunks) measured by range and bearing, EKF-SLAM with local
nearest-neighbor association, and a chi-squared innovation detector. A
different estimator, such as a factor graph, needs a new derivation. The
unmapped-association and dynamic-addition probabilities are not derived and
must be identified for the target environment. The 1.5 m alert limit fits a
car's lateral offset; a small indoor wheeled robot needs its own alert limit
and landmark layout. The cost of enumerating fault hypotheses on embedded
hardware is unknown because no runtime is reported. The 1% landmark isolation
threshold is a design value without a reported sensitivity study. The vehicle
evidence comes from one street in Chicago, recorded with a roof-rack sensor
suite and without GPS, not from a wheeled robot.

## Code and data

The paper does not state that code or data are released. Not verified
elsewhere.

## Version family

The method extends the authors' integrity monitoring for localization with a
known landmark map (Arana et al., 2018, 2019a, 2019b, 2020a) and for
fixed-lag smoothing (Hafez et al., 2020a, 2020b), all cited in Sec. 1. The
paper also cites the first author's PhD thesis, Hafez (2023), on localization
safety for state-of-the-art estimators, and a companion particle-filter
integrity paper (Hafez et al., 2024, IEEE Transactions on Robotics). Whether
the thesis contains this EKF-SLAM method was not verified. The library counts
this IJRR article once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "The results show that data association errors can cause significant positioning performance degradation that can only be predicted using the proposed integrity risk metric." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | direct-support | moderate | Sec. 9.1, p. 13 | "Thus, unlike the 2σ covariance envelope bound, the proposed integrity risk metric succeeds in predicting mobile robot localization failure." |
| C6 | qualifies | moderate | Sec. 9.2, p. 14 | "The sensor suite mounted on a vehicle’s roof rack (see Figure 9) is comprised of a STIM-300 tactical inertial measurement’s unit for relative measurements" |

## Page-cited excerpts

- **p. 1, Sec. 1.** "This paper focuses on EKF-based SLAM because most, if not all, state-of-the-art localization and mapping techniques are currently too complicated to be utilized in rigorous safety analyses via the integrity risk."
  The scope is limited to EKF-SLAM by the authors' choice; no claim is made for graph-based or learned SLAM.
- **p. 2, Sec. 1.** "Integrity risk is the probability of having large positioning errors without triggering an alarm."
  The metric is a probability of undetected hazardous error, distinct from a covariance envelope.
- **p. 8, Sec. 6.** "At the expense of loosening the integrity risk’s upper bound, this bound reduces the time complexity to become polynomial with the number of feature measurements"
  Tractability depends on truncating the fault hypotheses; the paper gives no runtime.
- **p. 13, Sec. 9.1.** "Thus, unlike the 2σ covariance envelope bound, the proposed integrity risk metric succeeds in predicting mobile robot localization failure."
  The result comes from a simulated map designed so that the association error is not visible in later innovations.
- **p. 13, Fig. 3.** "Lateral robot estimate error (blue) with its 3σ bounds (dashed red) for the properly-spaced landmark map"
  The caption names 3σ bounds while the text names a 2σ envelope; the figure itself was not checked.
- **p. 14, Sec. 9.1.** "if the map’s landmark density becomes relatively high, then the localization’s availability drastically drops because the risk of data association errors dominates over the increase in the number of measurements."
  Supports a non-monotonic effect of landmark density on availability, in simulation only.
- **p. 14, Sec. 9.2.** "In this experiment, GPS receiver measurements have not been utilized because even when there is coverage, multi-pathing errors are prevalent."
  GPS plays no part in the evaluated estimator, so the run says nothing about GNSS denial.
- **p. 14, Sec. 9.2.** "the test scenario has been selected such that EKF-based SLAM would fail during the experiment, due to data association errors."
  The vehicle run was chosen to contain a failure; it does not estimate how often failures occur.
- **p. 14, Fig. 9.** "In this experiment, only the ouster lidar and STIM-300 were utilized."
  The method was run with one 3D LiDAR and one tactical-grade IMU; the other mounted sensors were unused.
- **p. 15, Sec. 9.2.** "Note that the localization integrity risk becomes above the predefined safety threshold after the event of robot localization failure"
  On hardware the risk crosses the threshold after the failure, so the run does not show advance warning.

## Survey-usable statements

### Supported

- For EKF-SLAM with local nearest-neighbor association, an integrity risk bound that accounts for mis-association, unmapped-association, mis-addition, and dynamic-addition flagged a designed simulated association failure that the 2σ covariance envelope and the chi-squared detector missed.
- In simulation with landmark spacing varied from 8 m to 23 m, localization availability rises with landmark density until landmarks become too close to distinguish, and then drops.
- Per-landmark failure risk can be used to exclude high-risk landmarks (above 1%) from data association, as done in the vehicle experiment.

### Not supported

- The monitor warns before a failure on hardware: in the single vehicle run the integrity risk exceeds the threshold after the failure.
- The monitor runs in real time onboard: no processor or runtime is reported.
- The bound applies to graph-based or particle-filter SLAM: the derivation is specific to EKF-SLAM.
- The 1% landmark isolation improves accuracy or integrity: no comparison with and without isolation is reported.
- The method has been validated on a wheeled ground robot: the platforms are a car roof rack and a simulated bicycle model.
- The method has been evaluated under GNSS denial: GPS was not used, and the GPS degradation of the test street is only a property of the site.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read (Secs. 1-10 and Algorithm 1); Tables 1-2, Figs. 3-11 captions, and results text on pp. 12-15 checked against the PDF; revised after an independent fact-check against the updated template and vocabulary | corrections: rebuilt in template format; platform recoded as road vehicle (boundary); evidence setting set to recorded vehicle data with caveats video-only-hardware and few-trials; gnss-denial dropped (GPS unused); map-count inconsistency noted; Year set to 2025 (online 2024); unsupported particle-filter limitation removed; reviewer observations moved out of stated limitations; C2 and C5 strength lowered and C5 excerpt replaced (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer, supplemental batch (selection ID a19fe3ac54f6b6e3a7184ad8). No legacy evidence files are named.

## Original abstract

The safety of SLAM-based estimation for mobile robots is a challenging research problem, particularly for life- or mission-critical exploratory applications. To address this problem, this work proposes a method to utilize integrity risk, a widely used performance metric in aviation, to quantify SLAM-based mobile robot’s localization safety. More importantly, the approach accounts for sensor measurement faults, unknown deterministic errors that cannot be modeled via Gaussian white noise. The method is tailored for an EKF-based SLAM estimator, a chi-squared failure detector, and a local nearest neighbors data association criterion. The results show that data association errors can cause significant positioning performance degradation that can only be predicted using the proposed integrity risk metric. Furthermore, the study demonstrates that as the map’s landmark density increases, mobile robot localization safety improves, except when the landmark map’s density is too high to make the features indistinguishable, which leads to positioning safety degradation.
