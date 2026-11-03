# Switch-SLAM: Switching-Based LiDAR-Inertial-Visual SLAM for Degenerate Environments

## Metadata

| Field | Value |
|---|---|
| ID | F04 |
| Title | Switch-SLAM: Switching-Based LiDAR-Inertial-Visual SLAM for Degenerate Environments |
| Authors | Junwoon Lee, Ren Komatsu, Mitsuru Shinozaki, Toshihiro Kitajima, Hajime Asama, Qi An, Atsushi Yamashita |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3421792](https://doi.org/10.1109/lra.2024.3421792) |
| Official URL | https://ieeexplore.ieee.org/document/10582434/ |
| Theme folder | T1-perception-localization |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T1-perception-localization/2024-Switch-SLAM-F04/paper.pdf` and `02-fulltext/T1-perception-localization/2024-Switch-SLAM-F04/paper.md` (local only); [BibTeX](../../../01-papers/T1-perception-localization/2024-Switch-SLAM-F04/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: fault-recovery-deployment
- evidence_type: dataset-playback
- evidence_all: dataset-playback, simulation
- protocol_caveats: none
- platform_class: mixed
- platform: public Handheld, CERBERUS ANYmal, and SubT-MRS datasets; simulated Gazebo robot
- boundary_platform: yes
- degradation: visual-degradation, lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation, integrity-reliability
- sensors: 3D LiDAR, monocular camera, IMU; GNSS and loop closure excluded from main trajectory comparisons
- compute: Intel i7-1165G7 CPU with Ubuntu; real-time dataset processing, no end-to-end navigation deadline
- compute_location: desktop-offline
- summary_result: On the selected Handheld degeneracy test, the proposed detector reports 0.96 accuracy and 0.99 recall; evaluation measures estimation rather than navigation recovery.
- summary_limitation: Status changes near the threshold can be nonsmooth; the method uses buffering and interpolation, while broader real-world lighting and motion tests remain future work.
- survey_included: yes
- verification_level: light

## Problem

LiDAR degenerates in poorly structured spaces and visual odometry can fail under aggressive motion or image interruption. A failed estimator can contaminate ordinary multimodal fusion. Switch-SLAM conditions initialization and scan-to-map optimization on degeneracy and visual failure status (pp. 1, 4-5).

## Mechanism

Three normalized small Hessian eigenvalues are compared with thresholds derived from a chi-squared construction. A status buffer and interpolation smooth transitions from LiDAR to visual initialization. When LiDAR degenerates, visual constraints and well-conditioned LiDAR directions support optimization; if vision also fails, the well-conditioned directions remain and IMU preintegration carries the underdetermined directions (pp. 4-5). The threshold construction includes distributional assumptions and a fixed user-chosen significance setting; "non-heuristic" does not mean assumption-free.

## Baselines and controls

The evaluation compares LiDAR, visual, and LiDAR-visual methods, including LIO-SAM, VINS-MONO, and LVI-SAM. GNSS integration and loop closure are disabled in the main comparisons; results average three repeated runs. Detector baselines from references [16] and [17] receive tested thresholds, and the best accuracy/recall settings are reported (pp. 6-7). The complete table rankings were not independently audited.

## Platform and setup

Gazebo Fast Rotate, Plane, and Farm scenarios deliberately separate aggressive motion, structure deficiency, and their combination. Public recorded evidence includes Handheld, four CERBERUS ANYmal sequences, and SubT-MRS Multi Floor/Long Corridor. CERBERUS LiDAR horizontal field of view is restricted to 180 degrees to induce degradation, and only the front-right camera is used (pp. 5-6). This mixed carrier evidence does not validate a particular wheeled drivetrain.

## Evidence type and transfer

Real recordings are dataset playback, complemented by simulation. The paper evaluates trajectory accuracy, mapping/localizability, and degeneracy detection. The selected sections do not show alarms selecting an evaluated navigation stop/replan action, collision outcomes, or mission completion.

## Sensors

The simulated suite uses a Velodyne VLP-16, RGB camera, and IMU. Public datasets have their own LiDAR/camera/IMU suites; CERBERUS uses the front-right image stream and an intentionally restricted LiDAR field of view. GNSS supplies part of detector reference construction but is excluded from the main trajectory fusion comparisons (pp. 6-7).

## Compute and latency

The authors run the comparison methods with Ubuntu on an Intel i7-1165G7 CPU in real-time operation (p. 6). A worst-case deadline, onboard wheel-platform resource budget, detection delay distribution, and task-level fallback latency were not established by this selected reading.

## Key quantitative results

- On the selected Handheld detector test, proposed accuracy is 0.96 and recall 0.99; reference [17] has 0.96 accuracy and 0.96 recall after selecting its tested threshold (p. 7, detector text).
- CERBERUS playback limits LiDAR horizontal field of view to 180 degrees; main comparisons average three repeated runs (p. 6, setup text).

Table II trajectory-error cells were not re-transcribed; the card does not claim the best result on every sequence.

## Stated limitations

- States close to the degeneracy threshold can rapidly change initialization and produce nonsmooth optimization; buffering/interpolation addresses this issue (p. 4).
- Under simultaneous LiDAR degeneracy and visual failure, IMU preintegration significantly affects the undetermined directions (p. 5).
- Wider field tests across structure, aggressive motion, and lighting are future work (p. 8).

## Transfer conditions

For G1, the paper supplies a detector-to-estimator-switch chain and a response to simultaneous sensor weaknesses. A wheeled navigation implementation still needs calibration, a justified status-buffer setting, inertial drift limits, and measured detection-to-action delay with paired safety/task outcomes. Detector accuracy against a constructed GNSS/ICP reference is distinct from calibrated integrity risk. No global absence claim follows from this selective review.

## Code and data

The paper identifies public Handheld/CERBERUS/SubT-MRS data and supplementary material at its IEEE DOI; Gazebo environment assets refer to https://github.com/clearpathrobotics/cpr_gazebo (pp. 1, 6). A Switch-SLAM implementation release and its execution were not verified in the selected pages.

## Version family

Official IEEE Robotics and Automation Letters article, 2024, DOI 10.1109/LRA.2024.3421792. Conference/preprint relatives were not audited; this journal work is counted once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Algorithm discussion, p. 5 | "the optimization process is executed only along the well-conditioned DOFs." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | Sec. V, p. 8 | "a switching structure to effectively prevent failure information from propagating throughout the system" |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 5, Scan-to-map matching.** "the optimization process is executed only along the well-conditioned DOFs."
  The estimator responds to joint weaknesses; task recovery is a separate test.
- **p. 6, Evaluation setup.** "The GNSS integration and loop closure are not used."
  Trajectory comparisons omit these extra corrections.
- **p. 6, Evaluation setup.** "All the experimental results are presented as averages obtained from each set of three repeated tests."
  Repeated playback does not imply independent physical navigation trials.

## Survey-usable statements

### Supported

- Named LiDAR/visual weaknesses can trigger changes to estimator initialization and optimization using a status buffer.
- Accuracy and degeneracy detection are evaluated on deliberately selected or modified datasets under specified sensor conditions.

### Not supported

- Autonomous navigation recovery validated by collision, mission-success, and alert-delay measurements together.
- An assumption-free detector or a formal hazardous-misleading-information guarantee.
- Superior trajectory error on every sequence, since the full table rankings were not audited.

## Verification log

- 2026-11-02 | host: Codex | scope: new targeted light review; read abstract p. 1, switching/assumptions pp. 4-5, evaluation setup/discussion pp. 5-7, conclusion p. 8; table-error cells and detector derivation not fully audited; metadata, abstract, and quoted PDF pages checked; no whole-paper read or complete numeric/table audit | corrections: no legacy extraction; preserve evidence boundaries
- This is a new follow-up card. Source PDF and raw publisher BibTeX were preserved byte-for-byte; any later survey number needs a targeted PDF recheck.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

This letter presents Switch-SLAM, switching-based LiDAR-inertial-visual SLAM for degenerate environments, designed to tackle the challenges in degenerate environments for LiDAR and visual SLAM. Switch-SLAM achieves high robustness and accuracy by utilizing a switching structure that transitions from LiDAR to visual odometry when degeneration of LiDAR odometry is detected. To efﬁciently detect degeneration, SwitchSLAM incorporates a non-heuristic degeneracy detection method that does not require heuristic tuning and demonstrates generalizability across various environments. Switch-SLAM is evaluated on diverse datasets containing both LiDAR and visual odometry degeneracy scenarios. The experimental results highlight the accurate and robust localization by the proposed method in multiple challenging environments with either LiDAR or visual SLAM degeneracy.
