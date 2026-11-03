# How Safe Is Particle Filtering-Based Localization for Mobile Robots? An Integrity Monitoring Approach

## Metadata

| Field | Value |
|---|---|
| ID | M28 |
| Title | How Safe Is Particle Filtering-Based Localization for Mobile Robots? An Integrity Monitoring Approach |
| Authors | Osama Abdul Hafez, Mathieu Joerger, and Matthew Spenko |
| Venue | IEEE Transactions on Robotics, vol. 40, pp. 3372-3387 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/tro.2024.3420798](https://doi.org/10.1109/tro.2024.3420798) |
| Official URL | https://ieeexplore.ieee.org/document/10577499/ |
| Theme folder | T1-perception-localization |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T1-perception-localization/2024-PF-integrity-M28/paper.pdf` and `02-fulltext/T1-perception-localization/2024-PF-integrity-M28/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2024-PF-integrity-M28/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: localization-mapping
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, simulation
- protocol_caveats: none
- platform_class: road-vehicle
- platform: vehicle roof rack with Ouster 64-beam LiDAR and STIM-300 IMU; bicycle-model simulation
- boundary_platform: yes
- degradation: data-association-fault, gnss-denial
- degradation_observed: none
- evaluation_primary: integrity-reliability
- evaluation_all: integrity-reliability, residual, designed-degradation
- sensors: 64-beam Ouster LiDAR (range and bearing to landmarks), STIM-300 IMU
- compute: not recorded in the legacy extraction
- compute_location: not-reported
- summary_result: In simulation, safety improves with landmark density until landmarks become indistinguishable; the particle filter is safer than the EKF when landmarks are poorly separated.
- summary_limitation: Integrity availability is limited when the alert limit is very tight, and too-dense landmark maps raise the misassociation risk.
- survey_included: yes
- verification_level: light

## Problem

Accident-free kilometers, particle spread, and covariance are not safety
proofs for landmark-based particle-filter localization, because they ignore
measurement faults such as local-nearest-neighbor misassociation (MA) and
association with unmapped objects (UA).

## Mechanism

A particle-filter fault detector is paired with a bound on integrity risk,
the probability of a hazardous lateral error without an alarm, under
local-nearest-neighbor association. The bound accounts for the predicted
particle-error distribution, the MA and UA hypothesis probabilities, and the
detector statistic. Association requires a feature to fall in the validation
region of the same landmark for every predicted particle, which targets
tunnel-like association failures.

## Baselines and controls

In simulation, the particle-filter (PF) integrity monitor is compared with an
extended Kalman filter (EKF) integrity monitor under well-separated and
poorly separated landmarks and three map densities. In the field test, 150
and 300 particles are compared.

## Platform and setup

Simulation uses a bicycle model with range and bearing landmarks, an alert
limit of 10 cm, and map densities of 0.003, 0.006, and 0.009 landmarks per
square meter. The field test uses a vehicle roof rack on S. State Street
(31st to 33rd St.) in Chicago, where GPS is denied or degraded by trees and
buildings. The landmark map was built by SLAM beforehand. The lateral alert
limit is 1.5 m.

## Evidence type and transfer

The integrity numbers come from simulation and from a car-mounted sensor
suite in an urban canyon, not from a small indoor wheeled platform. The
legacy extraction does not record whether the field data were processed
online; they are coded as recorded data from the authors' vehicle, which was
not verified. Because the platform is a road vehicle, this is a boundary
paper for the survey.

## Sensors

A STIM-300 IMU provides relative measurements, and a 64-beam Ouster LiDAR
provides range and bearing to lamp posts, columns, and tree trunks. GPS is
not used because of multipath. A Velodyne VLP-16 and a NovAtel SPAN-CPT are
present on the rack but not used here.

## Compute and latency

Not recorded in the legacy extraction; not verified.

## Key quantitative results

- Simulation: safety improves as map density increases from 0.003 to 0.009 landmarks per square meter, until landmarks become indistinguishable (pp. 10-11).
- Simulation: the PF is safer than the EKF when landmarks are poorly separated, and often but not always safer when they are well separated (p. 10).
- Field test with a 1.5 m lateral alert limit: 300 particles give a smaller detector statistic and integrity risk than 150 particles (p. 12).

## Stated limitations

- Localization availability is limited when the alert limit is set very tight (p. 11).
- Too-dense maps produce indistinguishable landmarks and raise the misassociation risk (p. 11).
- Relative measurements are assumed fault-free in simulation (page not located).

## Transfer conditions

The experimental landmarks are urban poles and trees, not a 2D indoor
occupancy map, and the sensor suite is car-mounted (Ouster-64 and a tactical
STIM-300 IMU), not a small indoor wheeled platform. The simulation results
depend on well-separated landmarks and a sufficient number of particles.

## Code and data

Not recorded in the legacy extraction; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | weak | Sec. XI-B, p. 11 | "The proposed robot localization safety method is tested in an urban environment (S. State Street from 31st to 33rd St.) in Chicago, IL, USA, where GPS signals are denied or degraded due to dense tree coverage and tall buildings lining the street (see Fig. 12)." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | direct-support | strong | Sec. I, p. 1 | "However, the number of successfully driven kilometers alone is inadequate to establish navigation safety; a recent study [2] revealed that autonomous vehicles must cover billions of kilometers under all potential weather conditions to provide a conservative navigation safety proof." |
| C6 | qualifies | weak | Sec. XI-B, p. 11 | "The proposed robot localization safety method is tested in an urban environment (S. State Street from 31st to 33rd St.) in Chicago, IL, USA, where GPS signals are denied or degraded due to dense tree coverage and tall buildings lining the street (see Fig. 12)." |

## Page-cited excerpts

- **p. 11, Sec. XI-B.** "The proposed robot localization safety method is tested in an urban environment (S. State Street from 31st to 33rd St.) in Chicago, IL, USA, where GPS signals are denied or degraded due to dense tree coverage and tall buildings lining the street (see Fig. 12)."
  The field test is a GPS-degraded urban street, with a vehicle-mounted suite rather than a small robot.
- **p. 1, Sec. I.** "However, the number of successfully driven kilometers alone is inadequate to establish navigation safety; a recent study [2] revealed that autonomous vehicles must cover billions of kilometers under all potential weather conditions to provide a conservative navigation safety proof."
  The motivation for an integrity metric instead of driven distance.

## Survey-usable statements

### Supported

- Integrity risk under data-association faults can be bounded for particle-filter localization, and in simulation the PF is safer than the EKF when landmarks are poorly separated.
- Denser landmark maps improve safety only until landmarks become indistinguishable.

### Not supported

- The PF is always safer than the EKF: the authors state it is often, not always, safer when landmarks are well separated.
- The bound has been shown on a small wheeled robot or an indoor occupancy map: the field test uses a car roof rack and urban landmarks.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); no legacy quote dropped; the landmark-type remark moved from Stated limitations to Transfer conditions as a reviewer observation
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Deriving safe bounds on particle filter estimate is a research problem that, if solved, could greatly benefit robots in life-critical applications, a field that is facing increasing interest as more robots are being deployed near humans. In response, this article introduces a new fault detector and derives a performance measure for particle filter: integrity risk. Integrity risk is defined as the probability of having large estimate errors without triggering an alarm, all while considering measurement faults, unknown deterministic errors that cannot be modeled via normal white noise. In this work, the faults come in the form of incorrectly associated features when using the local nearest neighbors. Simulations and experiments assess the efficiency of the introduced safety metric. The results show that safety improves as map density increases as long as the number of particles is sufficient to shape the error distribution and the landmarks are well separated. Also, the results indicate that, when landmarks are poorly separated, particle filter is safer than Kalman filter, whereas, when landmarks are well separated, particle filter is often, but not always, safer than Kalman filter.
