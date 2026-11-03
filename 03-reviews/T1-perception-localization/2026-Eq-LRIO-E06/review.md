# An Equivariant Filter-Based State Estimator for Tightly-Coupled LiDAR–Radar–Inertial Odometry

## Metadata

| Field | Value |
|---|---|
| ID | E06 |
| Title | An Equivariant Filter-Based State Estimator for Tightly-Coupled LiDAR–Radar–Inertial Odometry |
| Authors | Anbo Tao, Yarong Luo, Chi Guo, Chunxi Xia, Mingle Zhao, and Xingxing Li |
| Venue | IEEE Transactions on Automation Science and Engineering, vol. 23, pp. 14926-14940 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tase.2026.3726435](https://doi.org/10.1109/tase.2026.3726435) |
| Official URL | https://ieeexplore.ieee.org/document/11664132/ |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2026-Eq-LRIO-E06/paper.pdf` and `02-fulltext/T1-perception-localization/2026-Eq-LRIO-E06/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2026-Eq-LRIO-E06/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: HeRCULES vehicle sequences (snow); SNAIL handheld, e-bike, and SUV sequences (campus, rain)
- boundary_platform: yes
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: LiDAR, IMU, millimeter-wave radar (ARS548 or Oculii Eagle)
- compute: Intel Core Ultra 9 275HX CPU, no GPU; 7.645 ms (ARS548) and 9.244 ms (Oculii Eagle) total per frame
- compute_location: desktop-offline
- summary_result: On Parking04, Eq-LRIO has 2.190 m position RMSE versus 2.493 m for FAST-LIO2; on Library03 EKF-LRIO is better (4.824 m versus 4.926 m).
- summary_limitation: The authors state that the observability result is conditional on the current map being exact.
- survey_included: yes
- verification_level: light

## Problem

LiDAR-inertial odometry loses accuracy in rain, snow, and weak geometry, and EKF linearization can introduce spurious observable information. The paper also separates the contribution of the added radar from that of the geometric filter.

## Mechanism

An equivariant filter on a semi-direct product group (SD-EqF) jointly estimates the navigation state and IMU biases. LiDAR points are regrouped at the radar timestamps; a point-to-plane update is followed by a Doppler update. Outliers are removed by radar cross section (RCS), RANSAC, residual, and chi-squared tests. The paper analyzes continuous-time and discrete-time observability.

## Baselines and controls

EKF-RIO, FAST-LIO2, EKF-LRIO (the same pipeline with only the filter replaced), and Eq-LIO, with the same map, preprocessing, and noise settings. Initial attitude and velocity perturbations test robustness.

## Platform and setup

Playback of public real-world datasets: HeRCULES vehicle sequences in snow, and SNAIL handheld, e-bike, and SUV sequences on a campus in rain.

## Evidence type and transfer

Real-world dataset playback plus conditional theoretical analysis. There is no new deployment and no closed-loop test on the reference platform.

## Sensors

LiDAR, IMU, and millimeter-wave radar; runtimes are given for the ARS548 and Oculii Eagle radars. Sensor extrinsics are treated as calibrated.

## Compute and latency

An Intel Core Ultra 9 275HX CPU without a GPU; total processing time per frame is 7.645 ms with the ARS548 and 9.244 ms with the Oculii Eagle (pp. 13-14). The timing is on a desktop-class CPU, not an embedded computer.

## Key quantitative results

- Parking04 position RMSE: Eq-LRIO 2.190 m versus FAST-LIO2 2.493 m (legacy location: Table II, page 11; the values were located only in a figure caption of the transcription, not in the PDF text layer).
- Library03 position RMSE: Eq-LRIO 4.926 m versus EKF-LRIO 4.824 m, so EKF-LRIO is better on this sequence (p. 13; the legacy card attributes the values to Table II).
- Sequence 20240113/1: Eq-LRIO 0.055 m versus 0.486 m (legacy location: Table III; comparator not named in the legacy card; not located in the PDF text layer).
- Initial velocity perturbation of -20 m/s on 20231105/5: FAST-LIO2 2.316 m, Eq-LRIO 0.139 m, and EKF-LRIO 0.135 m, so most of the gain comes from the radar (p. 13).
- Total processing time per frame: 7.645 ms (ARS548) and 9.244 ms (Oculii Eagle) (p. 14).

## Stated limitations

- The observability result holds conditional on the current map being exact (p. 8).

## Transfer conditions

Legacy reviewer observations: observability conditional on an exact map is not full observability for general SLAM. Under static conditions gravity and the accelerometer bias are coupled, and radar gives no global position or yaw. Gravity modeling is not ideal, and the EqF is not better than the EKF on every sequence. A reuse needs a calibrated LiDAR-radar-IMU rig and a millimeter-wave radar with Doppler output.

## Code and data

The code is at https://github.com/taoxiom/EQLRIO (p. 2). HeRCULES and SNAIL are public datasets. Running the repository was not checked.

## Version family

Eq-LRIO is one work in this library. The earlier Eq-LIO is a baseline of a different sensor modality and is not counted as an independent replication.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Abstract, p. 1 | "However, LiDAR performance degrades under adverse weather conditions." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Remark 1, p. 8 | "the observability result is obtained conditional on the current map being exact." |

## Page-cited excerpts

- **p. 8, Remark 1.** "the observability result is obtained conditional on the current map being exact."
  The theory assumes an exact map.
- **p. 13, Velocity perturbations.** "the choice of sensing modality plays the dominant role"
  The same sentence calls the filter's effect secondary; the main gain cannot be credited to the EqF alone.
- **p. 14, Computation.** "the total processing time is 7.645 ms per frame when using the ARS548 radar, and 9.244 ms per frame when using the Oculii Eagle radar."
  Timing on a desktop-class CPU, not measured on embedded hardware.

## Survey-usable statements

### Supported

- Tightly coupling Doppler radar with LiDAR-inertial odometry reduces the effect of wrong initial velocity: at -20 m/s, 0.139 m (Eq-LRIO) and 0.135 m (EKF-LRIO) versus 2.316 m for FAST-LIO2 on one sequence.
- The equivariant filter keeps the unobservable directions of the nonlinear system, under the condition of an exact map.

### Not supported

- The equivariant filter beats the EKF on every sequence: EKF-LRIO is better on Library03 and slightly better in the -20 m/s case.
- The accuracy gains come mainly from the filter: the authors attribute the dominant role to the sensing modality.
- The method runs in real time on embedded hardware: timing is only on a Core Ultra 9 CPU.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese free-layout card converted to the English template; p. 13 quote trimmed to its first clause because the transcription drops the "fi" ligature in the rest; the abstract keeps the printed "offers" and "suffers", which the transcription renders without the "ff" ligature (94% match)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/891fe35cea319dfe826a8543/

## Original abstract

Over the past decade, the fusion of light detection and ranging (LiDAR) and inertial navigation systems (INS) has become a reliable solution for environmental perception in intelligent mobile platforms. However, LiDAR performance degrades under adverse weather conditions. Millimeter-wave radar offers complementary benefits: it is robust to environmental disturbances and provides direct Doppler velocity measurements. Moreover, most existing fusion frameworks rely on the extended Kalman filter (EKF), which suffers from linearization errors and inconsistency. To address these limitations, we propose and derive a tightly-coupled LiDAR–radar–inertial odometry framework based on the equivariant filter (EqF). The framework leverages both LiDAR and radar to provide complementary constraints on the 9-dimensional navigation state, significantly improving accuracy and robustness in challenging environments. Furthermore, we conduct an in-depth observability analysis using Lie derivative theory, examining both the nonlinear system and its discrete filter system. We show that the EqF preserves the same unobservable directions as the underlying nonlinear system, thereby ensuring consistent state estimation, a property that standard EKF does not possess. In addition, experiments on real-world datasets demonstrate that our method outperforms the state-of-the-art LiDAR–inertial odometry approach and other EKF-based approaches in terms of localization accuracy, robustness and velocity estimation precision.
