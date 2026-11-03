# Fault tolerant decentralized collaboration for simultaneous localization and prior map update with stable 2D features

## Metadata

| Field | Value |
|---|---|
| ID | F03 |
| Title | Fault tolerant decentralized collaboration for simultaneous localization and prior map update with stable 2D features |
| Authors | Maxime Escourrou, Joelle Al Hage, and Philippe Bonnifait |
| Venue | Robotics and Autonomous Systems, 200, 105402 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1016/j.robot.2026.105402](https://doi.org/10.1016/j.robot.2026.105402) |
| Official URL | https://www.sciencedirect.com/science/article/pii/S0921889026000758 |
| Theme folder | T4-multi-robot-coordination |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Fault-Map-Update-F03/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Fault-Map-Update-F03/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-Fault-Map-Update-F03/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: multi-robot, fault-recovery-deployment
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, simulation
- protocol_caveats: none
- platform_class: road-vehicle
- platform: three experimental passenger vehicles (Fig. 11, p. 12); simulated planar robots
- boundary_platform: yes
- degradation: sensor-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation, integrity-reliability
- sensors: 32-layer Velodyne LiDAR and wheel odometry; GNSS for initialization; post-processed RTK IMU SPAN-CPT for ground truth
- compute: ROS simulation; evaluated real-data processor, compute placement, and per-update latency not reported in selected passages
- compute_location: not-reported
- summary_result: On recorded three-vehicle data with injected observation and map faults, collaborative FDIR reportedly improves localization and covariance consistency; rendered-table numbers were not audited.
- summary_limitation: Isolation needs redundant common-landmark observations and at most two simultaneous faults; missing or new landmarks are outside the study.
- survey_included: yes
- verification_level: light

## Problem

Faulty perception observations and incorrectly located prior-map landmarks can corrupt decentralized collaborative localization, including the estimates exchanged between robots (pp. 1–3, 6). The paper jointly updates poses and stable 2D map features while distinguishing observation, map, and odometry faults. For G1/G4 it supplies a monitor-to-estimator/map-repair chain; its selected evaluation does not show that a detected fault drives a navigation stop, replan, or task recovery.

## Mechanism

Robots begin with the same globally referenced prior map and unique landmark IDs. They broadcast observed IDs and exchange state, maps, covariances/cross-covariances, and relative landmark observations when they simultaneously observe a common feature (pp. 1, 3). A Schmidt–Kalman filter (SKF) updates collaborating robots and the map while retaining covariance relationships to non-collaborating robots. Since other robots' odometry is unavailable, their predicted poses stay static while process uncertainty is inflated; Kullback–Leibler averaging (KLA) fuses full-state estimates before collaborative updates (pp. 5–6).

Fault detection compares squared Mahalanobis innovation residuals with chi-squared thresholds. Observation-space and map-independent landmark-space residual signatures distinguish observation from map faults under redundancy assumptions (pp. 7–8). Recovery excludes faulty observations, or increases a faulty landmark's covariance so available observations correct its pose in the next update. For odometry divergence, the specified action is a filter-reinitialization signal or a warning that localization is unusable (p. 8). These are state-estimation responses, not a demonstrated motion policy.

## Baselines and controls

The paper compares collaborative with standalone estimation, then FDIR with observation-only fault detection/exclusion (FDE) and no diagnosis under injected observation/map faults (pp. 9–11, 13–14). The map-fault example explains why exclusion alone can leave a bad landmark uncorrected and eventually allow estimator divergence. A centralized EKF comparison is cited from the authors' previous work [49], rather than presented as a new matched benchmark here (p. 10). Channel Filter communication/computation comparisons are analytical, and the broader comparison with iMESA and other C-SLAM methods is a feature/assumption discussion rather than an executed common-data benchmark (pp. 6, 14–16). Table rankings and error cells were not independently audited.

## Platform and setup

ROS simulation uses three robots, four prior-map landmarks, odometry, and simulated LiDAR. The collaboration-only simulation averages 100 noise realizations; the fault examples inject observations and incorrect landmark poses/covariances (pp. 8–11). Real data were acquired on 90-second campus routes by three experimental cars visible in Fig. 11, not small wheeled robots. Each carried 32-layer Velodyne LiDAR, odometry, GNSS for initialization, and post-processed RTK IMU SPAN-CPT ground truth (p. 12; rendered setup inspected). OSM facade landmarks and the cars' recorded observations create changing collaboration groups (pp. 12–13).

For the real-data fault comparison, observations receive injected biases and two map landmarks receive incorrect initial poses/covariances (p. 13). This is a controlled estimator evaluation on acquired vehicle data; the selected experiment does not establish that the method's output controlled vehicle motion.

## Evidence type and transfer

The strongest supported setting is recorded-robot-data, plus simulation. The authors describe an online recursive method, but the empirical section explicitly describes data acquisition and evaluation with real data; it does not report a live estimate-to-control connection (pp. 1, 11–14). Localization/map errors, uncertainty coverage, residual detection, and correction are evaluated. Navigation success, collision risk, recovery maneuver completion, and a filter-reset execution trial are not established.

For G4, changing common-landmark collaboration windows and KLA correction of differing map estimates are shown (pp. 9–13). Bidirectional messages, common timestamps, and buffering are part of the architecture (p. 3). Message-loss tolerance is claimed for SKF operation, but the selected experiment does not inject a measured packet-loss, complete-partition, delayed-reunion, or stale-message protocol. Do not promote the estimator's covariance consistency to universal partition/reconnection map agreement.

## Sensors

The real pipeline uses 32-layer Velodyne LiDAR and wheel odometry. Cylinder3D extracts building points; NDT aligns them with OSM facade grids; clustering and RANSAC yield relative 2D facade poses. GNSS initializes pose and post-processed RTK IMU SPAN-CPT supplies ground truth, not continuous GNSS localization input (p. 12). Features must be associated with the same prior-map landmark IDs. Missing/new landmarks are not handled in this study (p. 6).

## Compute and latency

ROS is named for simulation, but the selected setup/evaluation does not identify a processor, compute location, measured per-update runtime, or a detection-to-repair deadline (pp. 8, 12–15). The bandwidth analysis assumes 32-bit floats and 10 Hz LiDAR; it is a payload calculation rather than a measured delivered network rate or an end-to-end timing experiment (pp. 14–16). KLA's full covariance inversion can dominate SKF's lower-order computation, and lower-frequency KLA/map exchange is proposed as an optimization (pp. 6, 15–16).

## Key quantitative results

- The fault-isolation construction assumes at most two simultaneous faults; isolating a map fault requires at least two robots observing the landmark, and isolating odometry divergence requires at least three observed landmarks (pp. 7–8).
- Collaboration-only simulation results average 100 noise realizations; the real-data scenario consists of three vehicles on 90-second routes (pp. 9, 12).
- The real-data fault setup injects observation biases between 2 and 15 s with mean 1 m at 1% occurrence, and map position biases of 5 m and 2.6 m; these are evaluation conditions, not performance gains (p. 13).
- The authors report improved real-data localization/covariance coverage with FDIR and describe prevention of Green/Orange divergence, but Table 7 cells and plotted values were not independently verified for this light review (pp. 13–14, Table 7 and Fig. 15).

## Stated limitations

- Missing and new map landmarks are not considered (p. 6).
- A simultaneous landmark fault and observation fault on that landmark cannot be isolated. When redundancy assumptions fail or too many faults occur, threshold-exceeding observations are excluded and the map cannot be repaired at that time (p. 8).
- KLA requires consistent incoming state estimates; insufficient covariance inflation for non-collaborating robots can make fusion inconsistent (pp. 6, 9).
- Real LiDAR observation errors do not follow the assumed zero-mean Gaussian model closely, so the false-alarm parameter is manually adjusted using empirical data (p. 13).
- More robust feature extraction, adding/removing map elements, and optimized KLA use remain future work (p. 15).

## Transfer conditions

Verify the common prior map/frame and unique IDs, stable 2D landmark geometry, sufficient simultaneous observations, uncertainty calibration, odometry model, sensor/map alignment, bidirectional radio availability, common timestamps, and buffer behavior. A covariance repair may restore usable estimation without proving an operational integrity-risk bound; the real-data coverage remains below its nominal confidence level in some cars (pp. 13–14). A navigation deployment additionally needs a defined response to unusable localization, independent safety/task metrics, measured detection-to-action latency, and tested recovery execution.

A network study should separately test prolonged partitions, asymmetric loss, stale state, and reconnection; the availability of standalone SKF updates and KLA fusion is a mechanism for such a test, not evidence that the test occurred. Corrupted external observations are considered within the fault model, but arbitrary Byzantine or correlated multi-robot faults exceed the isolation assumptions. Road-car data do not validate the R680 drivetrain, terrain, or onboard implementation.

## Code and data

The targeted text names ROS and OSM and cites the facade-extraction method [50] (pp. 8, 12). A source-code or recorded-data release URL was not established in the selected reading; availability and execution are not verified.

## Version family

This is the 2026 Robotics and Autonomous Systems article, available online February 28, 2026 (p. 1). It cites the authors' 2022 FUSION paper, “Decentralized Collaborative Localization with Map Update using Schmidt-Kalman Filter,” for a previous centralized/decentralized comparison (pp. 10, 18). That relation is recorded as prior related work; this light review does not establish an exact extension/version family. Count the present DOI once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Sec. 5, p. 6 | "These faults have a direct effect on the accuracy and integrity of state estimation." |
| C3 | unset | n/a | | |
| C4 | direct-support | strong | Sec. 4.2, p. 6 | "This leads to differences in map estimates as well as in the cross-covariance with the robots." |
| C5 | partial-support | strong | Sec. 5.3, p. 8 | "Different actions are carried out depending on the type of fault, namely, the exclusion of erroneous observations or the correction of the landmark pose." |
| C6 | qualifies | moderate | Sec. 7.4, p. 13 | "The false alarm probability has been manually adjusted based on empirical data analysis." |

## Page-cited excerpts

- **p. 8, Sec. 5.3, Fault recovery.** "Different actions are carried out depending on the type of fault, namely, the exclusion of erroneous observations or the correction of the landmark pose."
  Recovery here repairs estimator input/state, rather than executing a navigation maneuver.
- **p. 8, Sec. 5.3, Filter reset.** "In the case of odometry fault, a signal must be sent to reinitialize the filter, or to warn the user that the localization is unusable."
  A reset/warning is specified, but a closed-loop reset-to-navigation recovery test is not established.
- **p. 6, Sec. 4.2.** "In order to fuse the information from the different robots in collaboration, the KLA is used before each SKF update step."
  KLA addresses differing estimates and correlations within the stated fusion assumptions.
- **p. 12, Sec. 7.2.** "A data acquisition was conducted with three experimental vehicles"
  The physical evidence is acquired vehicle observations; the phrase does not establish an autonomous control loop.

## Survey-usable statements

### Supported

- F03 narrows G1 with an explicit residual-diagnosis-to-observation-exclusion/map-repair chain, plus a specified odometry reset/warning response; tests measure localization and map quality (pp. 7–14).
- For G4, common-landmark collaboration, cross-covariance handling, KLA, and fault isolation address incorrect information and differing map estimates; simulation and recorded vehicle data compare FDIR with exclusion/no diagnosis (pp. 3, 5–14).

### Not supported

- A navigation maneuver or autonomous task recovery improves safety/completion after a localization alarm: those downstream outcomes are not evaluated in the selected evidence.
- A controlled complete-partition/reconnection experiment proves map agreement under arbitrary loss, timing, or corruption: the reported collaboration windows and covariance results do not establish that protocol.
- Arbitrary simultaneous faults, changing/new landmarks, calibrated operational integrity risk, or measured R680 real-time deployment are not established.

## Verification log

- 2026-11-02 | host: Codex | scope: new targeted light review of physical PDF p. 1 identity/abstract, p. 3 architecture/assumptions, pp. 5–8 SKF/KLA/FDIR selected passages, pp. 9–11 simulation comparisons, pp. 12–14 acquired-data setup/results, p. 15 conclusion, p. 16 selected communication/complexity discussion, and p. 18 prior-work reference; p. 12 rendered setup inspected; abstract and excerpts checked against PDF and MinerU transcription; review_check --pdf passed; table cells, proofs, and complete numeric results not audited | corrections: no legacy extraction; estimator/map repair, recorded-data evidence, redundancy/correlation premises, and untested network-loss protocol kept distinct.
- Legacy extraction: none; new targeted follow-up reading from the user-supplied official publisher PDF and retained unchanged publisher BibTeX.

## Original abstract

Accurate and reliable localization is crucial for safe navigation of autonomous robots. In environments where GNSS performs poorly, robots can rely on stable 2D features stored on prior vector maps, such as OpenStreetMap, which are detected by on-board sensors. This paper proposes a fault tolerant decentralized collaborative method for online localization and map update. We focus on the case of indirect collaboration, where robots only collaborate through the observation of common landmarks. The method relies on the Schmidt–Kalman filter, which handles correlations between robots while minimizing the number of communications. A Kullback–Leibler Average data fusion is also employed. To ensure the integrity of the state estimation, a fault detection, isolation, and recovery approach is proposed, enabling the detection of sensor faults and the correction of map faults through collaboration. The method is evaluated using both simulation and experimental data. Results show that collaboration improves accuracy and consistency of localization and mapping, and improves the ability to detect faults.
