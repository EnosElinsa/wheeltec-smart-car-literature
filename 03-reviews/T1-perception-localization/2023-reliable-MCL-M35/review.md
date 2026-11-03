# Reliable Monte Carlo localization for mobile robots

## Metadata

| Field | Value |
|---|---|
| ID | M35 |
| Title | Reliable Monte Carlo localization for mobile robots |
| Authors | Naoki Akai |
| Venue | Journal of Field Robotics, vol. 40, no. 3, pp. 595-613 |
| Year | 2023 |
| Type | journal |
| DOI | [10.1002/rob.22149](https://doi.org/10.1002/rob.22149) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.22149 |
| Theme folder | T1-perception-localization |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T1-perception-localization/2023-reliable-MCL-M35/paper.pdf` and `02-fulltext/T1-perception-localization/2023-reliable-MCL-M35/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2023-reliable-MCL-M35/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: localization-mapping
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Whill Model CR with Hokuyo UTM-30LX-EW
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: integrity-reliability
- evaluation_all: residual, integrity-reliability
- sensors: 2D LiDAR (Hokuyo UTM-30LX-EW), INS or odometry
- compute: not recorded in the legacy extraction
- compute_location: not-reported
- summary_result: From wrong initial poses, reliable MCL relocalized faster than ROS amcl on two 2D-laser datasets and in a long-corridor building, where amcl was slow or never recovered.
- summary_limitation: Failure detection follows a noisy residual classifier and cannot certify closeness to ground truth; free-space global localization is sensitive to map shape change.
- survey_included: yes
- verification_level: light

## Problem

Standard 2D-LiDAR Monte Carlo localization (MCL) can be made more robust to
unmapped obstacles, but robustness alone does not guarantee safety: there is
no reliability score, no failure detection, and no fast recovery when the
estimate is wrong.

## Mechanism

A Rao-Blackwellized particle filter jointly estimates the 2D pose, a
known-or-unknown class for each beam, and a binary localization state
(success or failure). A class-conditional measurement model improves
tracking among moving obstacles. Reliability is the filtered probability of
success, driven by a classifier on the mean absolute error (MAE) of the
residuals. Free-space features support global pose sampling, and importance
sampling fuses those samples with pose tracking, so relocalization runs
continuously instead of as a hard switch. The implementation uses a 2D LiDAR
plus INS or odometry. The author notes that the graphical model could extend
to 3D LiDAR, but only 2D is implemented.

## Baselines and controls

The comparators are traditional MCL variants in simulation and the ROS
`amcl` package (augmented MCL with random-sampling recovery) on datasets and
on the author's platform.

## Platform and setup

(i) Simulation with moving obstacles. (ii) Pre-2014 2D-laser datasets (MIT
CSAIL and Intel Research Lab) in ROS, started with a wrong heading or a fully
wrong initial pose. (iii) The author's platform, a Whill Model CR with a
Hokuyo UTM-30LX-EW (30 m range, 270 degrees, 0.25 degree resolution), in an
indoor building with long corridors.

## Evidence type and transfer

The strongest setting is the author's own wheeled platform. The legacy
extraction does not record whether the method ran online during those runs;
they are coded as recorded robot data, which was not verified. The drive
type of the Whill Model CR is not recorded; the released software supports
differential-drive and omnidirectional models, so the platform is coded as
wheeled-unspecified.

## Sensors

2D LiDAR (Hokuyo UTM-30LX-EW on the author's platform) and INS or odometry.

## Compute and latency

Not recorded in the legacy extraction; not verified.

## Key quantitative results

- On the MIT CSAIL and Intel Research Lab datasets with wrong initial poses, the proposed method relocalizes faster and keeps tracking, while `amcl` is slow or, on Intel, never recovers; the legacy extraction records no values (pp. 14-15).
- On the author's platform in a long-corridor building, the proposed method relocalizes from wrong starts where `amcl` latches onto the wrong corridor; no values recorded (p. 15).
- In simulation, the class-conditional model labels hits on unknown obstacles, and robustness, reliability, and global-localization fusion are shown against traditional MCL variants; no values and no page recorded.

## Stated limitations

- Environment changes cannot be perfectly modeled, so robustness without reliability estimation is insufficient (p. 17).
- Class-conditional models, like M-estimation, need a decent initial guess (p. 17).
- MAE-threshold classification is noisy; Bayesian filtering stabilizes it but cannot say that the pose is close to ground truth, and a better classifier was too expensive to include in this graphical model (p. 17).
- Free-space global localization is sensitive to changes of the map shape, and the uniform importance term can jump even when tracking is fine (p. 18).

## Transfer conditions

The tests on the author's platform are indoor 2D LiDAR on a Whill Model CR
against ROS `amcl`, not a 3D outdoor localization stack. A robot that reuses
the method needs a 2D occupancy map whose shape stays close to the
environment, because free-space global localization depends on it.

## Code and data

The legacy extraction records that the ROS source code is released; the
URL is not recorded; not verified.

## Version family

Not recorded in the legacy extraction; not verified.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. 7, p. 18 | "This paper has presented reliable MCL that can (1) robustly work in dynamic environments, (2) immediately detect localization failure by estimating reliability, and (3) quickly relocalize if estimate has failed." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | direct-support | strong | Sec. 6.3.1, p. 17 | "However, this model cannot contribute to realizing guarantee of localization performance since environment changes cannot be perfectly modeled even if the model is used. Hence, the presented method includes the reliability estimation function. We strongly note that reliable localization that we consider in this study cannot be realized with only robustness improvement." |
| C6 | qualifies | weak | Sec. 7, p. 18 | "In the remaining two experiments, we compared the presented method with amcl that is a popular localization package in ROS. The comparison results showed that the presented method achives fast relocalization more than amcl." |

## Page-cited excerpts

- **p. 18, Sec. 7.** "This paper has presented reliable MCL that can (1) robustly work in dynamic environments, (2) immediately detect localization failure by estimating reliability, and (3) quickly relocalize if estimate has failed."
  The three functions of the method; the summary is the author's own.
- **p. 17, Sec. 6.3.1.** "However, this model cannot contribute to realizing guarantee of localization performance since environment changes cannot be perfectly modeled even if the model is used. Hence, the presented method includes the reliability estimation function. We strongly note that reliable localization that we consider in this study cannot be realized with only robustness improvement."
  Robustness alone does not give reliability; failure detection is needed.
- **p. 18, Sec. 7.** "In the remaining two experiments, we compared the presented method with amcl that is a popular localization package in ROS. The comparison results showed that the presented method achives fast relocalization more than amcl."
  The comparison is against one ROS baseline, `amcl`.

## Survey-usable statements

### Supported

- Estimating a binary localization-success state alongside the pose gives 2D-LiDAR MCL a failure-detection signal, and fusing free-space global localization by importance sampling enables relocalization.
- The author states that robustness to environment change alone cannot make localization reliable.

### Not supported

- The reliability estimate certifies that the pose is close to ground truth: the author states that it cannot.
- The method has been shown with 3D LiDAR: only a 2D implementation exists.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: format (English template); no legacy quote dropped
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

Reliability is a key factor for realizing safety guarantee of fully autonomous robot systems. In this paper, we focus on reliability in mobile robot localization. Monte Carlo localization (MCL) is widely used for mobile robot localization. However, it is still difficult to guarantee its safety because there are no methods determining reliability for MCL estimate. This paper presents a novel localization framework that enables robust localization, reliability estimation, and quick relocalization, simultaneously. The presented method can be implemented using a similar estimation manner to that of MCL. The method can increase localization robustness to environment changes by estimating known and unknown obstacles while performing localization; however, localization failure of course occurs by unanticipated errors. The method also includes a reliability estimation function that enables a robot to know whether localization has failed. Additionally, the method can seamlessly integrate a global localization method via importance sampling. Consequently, quick relocalization from a failure state can be realized while mitigating noisy influence of global localization. We conduct three types of experiments using wheeled mobile robots equipped with a two‐dimensional LiDAR. Results show that reliable MCL that performs robust localization, self‐failure detection, and quick failure recovery can be realized.
