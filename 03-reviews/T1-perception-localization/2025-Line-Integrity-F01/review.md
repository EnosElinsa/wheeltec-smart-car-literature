# Safety-Quantifiable Line Feature-Based Monocular Visual Localization With 3D Prior Map

## Metadata

| Field | Value |
|---|---|
| ID | F01 |
| Title | Safety-Quantifiable Line Feature-Based Monocular Visual Localization With 3D Prior Map |
| Authors | Xi Zheng, Weisong Wen, Li-Ta Hsu |
| Venue | IEEE Transactions on Intelligent Transportation Systems |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tits.2025.3572620](https://doi.org/10.1109/tits.2025.3572620) |
| Official URL | https://ieeexplore.ieee.org/document/11021529/ |
| Theme folder | T1-perception-localization |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T1-perception-localization/2025-Line-Integrity-F01/paper.pdf` and `02-fulltext/T1-perception-localization/2025-Line-Integrity-F01/paper.md` (local only); [BibTeX](../../../01-papers/T1-perception-localization/2025-Line-Integrity-F01/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: localization-mapping
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: campus UGV (drive type unspecified); EuRoC aerial and CARLA vehicle data are additional settings
- boundary_platform: no
- degradation: data-association-fault
- degradation_observed: none
- evaluation_primary: integrity-reliability
- evaluation_all: residual, integrity-reliability
- sensors: monocular images and IMU; prior 3D line map; HDL-32E LiDAR plus IMU construct campus reference/map
- compute: Intel Core i9-12900K desktop, Ubuntu 20.04, ROS/C++; feature matching depends on prior-map size
- compute_location: desktop-offline
- summary_result: Recorded ground-robot and aerial-data experiments compare localization errors and empirical protection-level coverage; the computed protection level is not used to drive recovery.
- summary_limitation: Protection-level coverage depends on measurement covariance and feature geometry; the study predicts estimation errors while planning and operational alert thresholds remain future work.
- survey_included: yes
- verification_level: light

## Problem

Monocular visual-inertial odometry drifts, and low residual error alone does not quantify hazardous localization error. The paper adds prior-map localization and a RAIM-inspired protection level (PL) for position and rotation (pp. 1, 6-7).

## Mechanism

Visual-inertial odometry initializes matching between image lines and 3D lines extracted from a prior point-cloud map. Foot-point constraints support pose optimization, while a weighted residual chi-squared test greedily rejects outliers. The PL combines bias-induced and noise-induced error under a linearized observation model, known Gaussian covariance, and a chosen number of residual outliers (pp. 1, 6-7). The method assumes negligible linearization error; it does not calibrate a downstream navigation controller.

## Baselines and controls

VINS, a prior line-to-line localization benchmark, proposed PPL without rejection, and PPL-OR with rejection compare localization accuracy. The PL is compared with a 3-sigma uncertainty envelope; covariance and remaining-outlier assumptions are varied. No recovery-controller ablation was established in the selected sections (pp. 7-8, 11-12).

## Platform and setup

EuRoC indoor aerial data, self-collected campus UGV data, and CARLA driving data are distinct settings. The campus UGV travels a square route; drive type is not stated in the selected text. LiDAR/IMU LIO-SAM constructs the campus prior map and reference trajectory, so the reference is an estimator rather than independent motion capture (pp. 7, 10-11).

## Evidence type and transfer

The headline evidence is estimation on recorded data, not an estimator demonstrated to drive a physical navigation or recovery loop. Ground, aerial, and simulated-vehicle results support a transferable monitoring mechanism. Shared dependence of the campus reference and map on LiDAR/IMU should remain visible (p. 11).

## Sensors

The evaluated localization consumes monocular images, IMU, and a prior line map. Campus equipment includes RealSense D435i, Xsens MTi-10, and Velodyne HDL-32E. LiDAR and IMU produce the prior map/reference through LIO-SAM; their role differs from the online visual localization input (pp. 10-11).

## Compute and latency

All experiments use an Intel Core i9-12900K desktop with Ubuntu 20.04, ROS, and C++. The authors distinguish feature-processing and optimization threads, and explain that large prior maps increase matching cost (pp. 7, 12). Table VI numeric timings were not read from a rendered image, so no timing value is transcribed here. A robot-level worst-case deadline and fallback were not established.

## Key quantitative results

- The ground-data PL discussion selects measurement covariance 13.1 pixel-squared after a covariance sweep with two residual outliers. This is a setting-dependent tuning choice, not a universal coverage guarantee (p. 12, text around Fig. 14).
- The campus recorded route is 295.5 m; CARLA routes are 1, 2, and 3 km. These describe evaluation scale, not autonomous mission success (p. 11, setup text).

Table error and bound-rate cells were not re-transcribed in this targeted review.

## Stated limitations

- With severe VINS initial-state drift, the loosely coupled localization can have difficulty converging (p. 12).
- Map density/precision and IMU/line geometry impair PL performance, especially yaw (p. 13).
- Larger prior maps increase computation, while prior-map updates and broader PL use in operational decisions, mapping, and planning are future work (p. 13).

## Transfer conditions

G1 is narrowed by a concrete integrity-monitoring mechanism. To transfer it into navigation, one must validate map quality, line geometry, noise/outlier assumptions, initial-state convergence, and an alert threshold tied to a tested stop/relocalization/recovery behavior. Empirical PL error coverage alone does not establish controlled integrity risk or paired safety/task outcomes. The paper explicitly reserves operational thresholds and planning use for future work (p. 13).

## Code and data

The paper identifies https://github.com/ZHENGXi-git/SafetyQuantifiable-PLVINS (p. 1). Repository availability, execution, and released campus data were not verified in this targeted read.

## Version family

Official IEEE journal article, 2025, DOI 10.1109/TITS.2025.3572620; one work is counted. Other conference/preprint versions were not audited.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | qualifies | strong | Sec. VI, p. 13 | "In this study, the computed PL is used solely to predict state estimation errors." |
| C6 | qualifies | moderate | Sec. V-B, p. 12 | "maintaining the size of the loaded prior map within a rational range is vital to the real-time performance of the method." |

## Page-cited excerpts

- **p. 13, Conclusion and Future Work.** "In this study, the computed PL is used solely to predict state estimation errors."
  PL is evaluated as an estimation-error monitor; a recovery policy is not established.
- **p. 7, Experiment Results and Discussions.** "All experiments are implemented on a desktop with Intel Core i9-12900K and Ubuntu 20.04."
  Desktop processing does not establish embedded deployment.
- **p. 12, System Evaluation.** "maintaining the size of the loaded prior map within a rational range is vital to the real-time performance of the method."
  The timing claim depends on map size.

## Survey-usable statements

### Supported

- Prior-map visual localization can be accompanied by a multiple-outlier PL whose empirical coverage is evaluated on recorded aerial/ground data.
- The authors explicitly separate state-error prediction from prospective operational alerting and planning use.

### Not supported

- A demonstrated monitor-to-recovery navigation chain with paired collision/task metrics.
- A universal calibrated safety guarantee independent of covariance, geometry, map quality, or VINS initialization.
- Independent physical ground truth for the campus evaluation.

## Verification log

- 2026-11-02 | host: Codex | scope: new targeted light review; read abstract p. 1, observation/PL premises pp. 6-7, evaluation setup and selected discussion pp. 7-13; numerical table cells and proof appendices not audited; metadata, abstract, and quoted PDF pages checked; no whole-paper read or complete numeric/table audit | corrections: no legacy extraction; preserve evidence boundaries
- This is a new follow-up card. Source PDF and raw publisher BibTeX were preserved byte-for-byte; any later survey number needs a targeted PDF recheck.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

Accurate and safety-quantifiable localization is of great significance for safety-critical autonomous systems, such as Autonomous ground vehicles (AGVs) and autonomous aerial vehicles (AAVs). The visual odometry-based method can provide accurate positioning in a short period but is subject to drift over time. Moreover, the quantification of the safety of the localization solution (the error is bounded by a certain value) is still a challenge. To fill the gaps, this paper proposes a safety-quantifiable line feature-based visual localization method with a prior map. The visual-inertial odometry provides a high-frequency local pose estimation, which serves as the initial guess for the visual localization. By obtaining a visual line feature pair association, a foot point-based constraint is proposed to construct the cost function between the 2D lines extracted from the real-time image and the 3D lines extracted from the high-precision prior 3D point cloud map. Moreover, a global navigation satellite system (GNSS) receiver autonomous integrity monitoring (RAIM) inspired method is employed to quantify the safety of the derived localization solution. Among that, an outlier rejection (also well-known as fault detection and exclusion) strategy is employed via the weighted sum of squares residual with a Chi-squared probability distribution. A protection level (PL) scheme considering multiple outliers is derived and utilized to quantify the potential error bound of the localization solution in both position and rotation domains. The effectiveness of the proposed safety-quantifiable localization system is verified using the datasets collected by AAV and AGV in indoor and outdoor environments, respectively. The open-source code is available at https://github.com/ZHENGXi-git/SafetyQuantifiable-PLVINS
