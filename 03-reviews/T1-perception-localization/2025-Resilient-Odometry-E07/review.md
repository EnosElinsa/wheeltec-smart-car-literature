# Resilient odometry via hierarchical adaptation

## Metadata

| Field | Value |
|---|---|
| ID | E07 |
| Title | Resilient odometry via hierarchical adaptation |
| Authors | Shibo Zhao, Sifan Zhou, Yuchen Zhang, Ji Zhang, Chen Wang, Wenshan Wang, and Sebastian Scherer |
| Venue | Science Robotics, vol. 10, no. 109, article eadv1818 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1126/scirobotics.adv1818](https://doi.org/10.1126/scirobotics.adv1818) |
| Official URL | https://www.science.org/doi/10.1126/scirobotics.adv1818 |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2025-Resilient-Odometry-E07/paper.pdf` and `02-fulltext/T1-perception-localization/2025-Resilient-Odometry-E07/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2025-Resilient-Odometry-E07/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: fault-recovery-deployment
- evidence_type: online-hardware
- evidence_all: online-hardware, dataset-playback
- protocol_caveats: joystick-driving, few-trials
- platform_class: wheeled-unspecified
- platform: human-driven TartanDrive vehicle and a corridor vehicle (wheeled); legged robot (single 13-condition run); aerial and handheld platforms in the datasets
- boundary_platform: no
- degradation: visual-degradation, lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: RGB camera, LiDAR, IMU (configuration varies by platform)
- compute: not reported in the main text (no CPU or GPU model, module runtime, memory, or power)
- compute_location: not-reported
- summary_result: On eight SubT-MRS challenge sequences, Super Odometry reports 0.271 average ATE versus 0.588 for the Liu submission; the averaging weights are not stated.
- summary_limitation: The authors state that performance depends heavily on accurate calibration and precise time synchronization, and that few-shot adaptation is not guaranteed for every robot.
- survey_included: yes
- verification_level: light

## Problem

When visual, geometric, or both kinds of sensing degrade, conventional fusion is easily corrupted by bad observations. The paper seeks hierarchical adaptation that balances computational load against continued availability.

## Mechanism

Super Odometry adapts at several levels. KLT tracking and geometric PCA select reliable features. The front end reweights factors by the distribution of observability labels over six directions. A modality whose contribution stays below 10% for 2 to 4 s has its factors removed. When all exteroceptive sensing degrades, a learned IMU model supplies local velocity and covariance as a motion prior, fused with LiDAR and vision per direction. The learned inertial model is a 1D ResNet with an LSTM, with a shared backbone and per-platform heads, pretrained and then adapted online with LoRA on a frozen backbone and self-supervision: the factor graph provides labels while perception is good, and inertial estimates feed back when it is bad. This is not a guarantee of drift-free pure-IMU operation for unlimited time.

## Baselines and controls

Learned inertial baselines AI-IMU, RNIN-VIO, TLIO, and IMO retrained on the same data. For the eight SubT-MRS challenge sequences, submissions by their original authors (Liu, Weitong, Kim, Yibin, Zhong, and Zheng), some of which ran offline and used loop closure. Fully smoke-filled cases are excluded from the averages of Tables 2 and 3 because all other methods failed there.

## Platform and setup

The authors report a cumulative 200 km and 800 h over six years on aerial, wheeled, legged, and handheld platforms in several configurations; this is not 800 h of continuous failure-free operation of one wheeled vehicle. A single run with 13 degradation types (2966 m, 46 min, 0.2 m final drift) used a legged robot. A 668 m corridor run with a vehicle at 4 m/s for 90% of the route and at most 5 m/s. The wheeled smoke and open-field tests use online estimation on data of a human-driven TartanDrive vehicle, with 45 s of adaptation under good perception before entering smoke and a further 60 s cross-platform adaptation test. There is no test on the reference platform and no closed-loop fusion with wheel encoders.

## Evidence type and transfer

Cumulative multi-platform field experience, one integrated legged run, online estimation on wheeled corridor and smoke runs, and evaluation on the public challenge data. Recovery of localization does not show safe navigation control, long autonomous operation of one platform, or recovery from hardware faults.

## Sensors

RGB camera, LiDAR, and IMU, reconfigured according to the available modalities. The training set of more than 100 h comprises SubT-MRS, TartanDrive, IDOL, Blackbird, and UZH data from eight platforms, with IMU axes unified and resampled to 200 Hz. Wheeled platforms do not imply fused wheel encoders. Accurate calibration and time synchronization are an explicit dependency. The main text does not list all LiDAR and IMU models; the supplementary material was not read.

## Compute and latency

The main text reports real-time operation and online adaptation with 45 s and 60 s of data, but no common CPU or GPU model and no per-module runtime, memory, or power. The 200 Hz rate is the resampling rate of data and evaluation trajectories, not a demonstrated rate of the full fusion or of online training. Inference and LoRA update rates would need the supplementary material and cannot be derived from sensor rates.

## Key quantitative results

- SubT-MRS challenge, eight sequences: published average ATE 0.271 for Super Odometry versus 0.588 for Liu; per-sequence values of Super Odometry 0.238, 0.074, 0.396, 0.026, 0.104, 0.204, 0.817, and 0.315 (p. 11, Table 2).
- The legacy reviewer computed an equal-weight mean of 0.438 for Liu's eight values, which does not match the published 0.588, and the weights are not stated; the headline 54% improvement is therefore not adopted (p. 11, Table 2).
- Learned inertial odometry on four platforms: ATE 6.17, 1.46, 4.32, and 3.32 and T-RTE 2.52, 0.79, 1.95, and 1.04 for the proposed model; the improvement percentages (19.63% and so on) are computed mostly against AI-IMU (7.68, 3.23, 8.26, 4.14), not against the column-wise second best (7.68, 3.10, 6.96, 3.72) (p. 9, Table 1).
- Floor01 position robustness: Super Odometry 0.891 versus Liu 0.910 and Weitong 0.909, so it is not best on every metric (p. 11, Table 3).
- A 600 s occlusion test has a maximum APE of 0.184 m (p. 7).
- The single legged run of 2966 m ends with 0.2 m final drift without loop closure; this is an endpoint error, not a full-trajectory ATE (p. 3).

## Stated limitations

- Performance depends heavily on accurate calibration and precise time synchronization (p. 12).
- The adaptation cannot guarantee few-shot capability for every robot or motion pattern (p. 16).
- The modality-removal threshold and time window were chosen empirically and are tunable (p. 5).
- The challenge comparison excludes completely degraded and smoke-related experiments (p. 11).

## Transfer conditions

Legacy reviewer observations: the 200 km and 800 h total is not broken down by platform, failure, or availability, so it is not a lifetime or MTBF figure. Under total degradation the learned IMU prior is still subject to distribution shift and bias accumulation. The smoke segments have no independent quantitative ATE and no distribution of full-failure durations. The supplementary methods, Table S1, and movies were not read. The reference point of the Table 1 percentages and the aggregation of the Table 2 average are unresolved. A wheeled reuse needs calibrated, time-synchronized camera, LiDAR, and IMU and a platform head for the learned inertial model.

## Code and data

Data are archived at https://zenodo.org/records/17569700 (p. 18); the archive was not downloaded or checked. The legacy extraction found no code repository URL in the main text. The supplementary material (methods, Figs. S1 to S7, Table S1, Movies S1 to S6) was not obtained.

## Version family

The current PDF carries a correction dated 2026-01-09 that changes only references 66 and 68 and states that no data or conclusions were affected (p. 18); it is not counted as a 2026 paper. The method extends the IROS 2021 Super Odometry work of the same group; the six years of cumulative validation should not all be credited to the new LoRA module.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Abstract, p. 1 | "Existing odometry systems often struggle with severe sensory degradations and extreme conditions such as smoke, sandstorms, snow, or low-light conditions" |
| C3 | qualifies | moderate | p. 16 | "it cannot guarantee “few-shot” capability for every robot or motion pattern." |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | Abstract, p. 1 | "providing a reliable fallback when exteroceptive sensors fail" |
| C6 | qualifies | moderate | p. 12 | "the performance of our system depends heavily on accurate calibration and precise time synchronization." |

## Page-cited excerpts

- **p. 2, Introduction.** "800 operational hours over 6 years on aerial, wheeled, legged, and handheld robots"
  A cumulative figure over heterogeneous configurations, not continuous autonomy of one vehicle.
- **p. 3, Integrated test.** "we conducted a comprehensive degradation experiment on a legged robot in a single run."
  The 13-condition run is legged evidence, not wheeled.
- **p. 5, Engine selection.** "This threshold and temporal window were empirically chosen and tunable"
  The 10% and 2 to 4 s rule is an empirical threshold without a recovery guarantee.
- **p. 9, Wheeled smoke test.** "evaluated its performance online using data from human-driven vehicles."
  Online estimation on human-driven vehicle data, not autonomous navigation.
- **p. 9, Adaptation.** "This online training process required only 45 s of data collection"
  Adaptation happens under good perception before the smoke.
- **p. 9, Table 1.** "compared with the second-best model across various robotic platforms"
  The stated reference does not match the column-wise second best.
- **p. 11, Table 2.** "ATE performance on SubT-MRS"
  Source of the challenge averages.
- **p. 11, Averages.** "This comparison excludes completely degraded or smoke-related experiments"
  The averages say nothing about smoke conditions.
- **p. 12, Calibration.** "the performance of our system depends heavily on accurate calibration and precise time synchronization."
  Calibration and synchronization are prerequisites.
- **p. 16, Generalization.** "it cannot guarantee “few-shot” capability for every robot or motion pattern."
  No universal guarantee for new platforms.
- **p. 18, Correction.** "No data or conclusions were affected."
  The 2026 correction does not create a new version.

## Survey-usable statements

### Supported

- Hierarchical adaptation (feature selection, direction reweighting, engine removal, learned inertial fallback) keeps odometry running through visual and geometric degradation in the authors' tests, with a reported SubT-MRS average ATE of 0.271 versus 0.588.
- A learned inertial model adapted online with LoRA under good perception serves as the fallback when exteroceptive sensing fails.

### Not supported

- Super Odometry is best on every metric of the challenge: Floor01 position robustness is 0.891 versus 0.910 (Liu) and 0.909 (Weitong).
- The 54% average improvement or the 35.5% improvement over the second best: the aggregation weights and reference columns do not match the tables.
- The system was validated for 800 h on a wheeled robot: the figure is cumulative over six years and many platforms, and the integrated 13-condition run used a legged robot.
- The averages hold in smoke: smoke-related experiments are excluded from them.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; no legacy quote dropped
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/d4c3e6a1c33135f6412afc84/

## Original abstract

Resilient and robust odometry is crucial for autonomous systems operating in complex and dynamic environments. Existing odometry systems often struggle with severe sensory degradations and extreme conditions such as smoke, sandstorms, snow, or low-light conditions, threatening both the safety and functionality of robots. To address these challenges, we present Super Odometry, a sensor fusion framework that dynamically adapts to varying levels of environmental degradation. Super Odometry uses a hierarchical structure to integrate four core modules from lower-level to higher-level adaptability, including adaptive feature selection, adaptive state direction selection, adaptive engine selection, and a learning-based inertial odometry. The inertial odometry, trained on more than 100 hours of heterogeneous robotic platforms, captures comprehensive motion dynamics. Super Odometry elevates the inertial measurement unit to equal importance with camera and light detection and ranging (LiDAR) systems in the sensor fusion framework, providing a reliable fallback when exteroceptive sensors fail. Super Odometry has been validated across 200 kilometers and 800 operational hours on a fleet of aerial, wheeled, and legged robots and under diverse sensor configurations, environmental degradation, and aggressive motion profiles. It marks an important step toward safe and long-term robotic autonomy in all-degraded environments.
