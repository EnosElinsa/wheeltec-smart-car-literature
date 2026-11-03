# Real-time kinematics-based sensor-fault detection for autonomous vehicles using single and double transport with adaptive numerical differentiation

## Metadata

| Field | Value |
|---|---|
| ID | E51 |
| Title | Real-time kinematics-based sensor-fault detection for autonomous vehicles using single and double transport with adaptive numerical differentiation |
| Authors | Shashank Verma and Dennis S. Bernstein |
| Venue | Control Engineering Practice, vol. 159, article 106304 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1016/j.conengprac.2025.106304](https://doi.org/10.1016/j.conengprac.2025.106304) |
| Official URL | https://linkinghub.elsevier.com/retrieve/pii/S096706612500067X |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2025-KSFD-E51/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-KSFD-E51/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-KSFD-E51/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, numerical
- protocol_caveats: video-only-hardware, motion-capture-pose, external-pose-source, few-trials
- platform_class: ackermann
- platform: Yahboom aluminum-alloy Ackermann robot car chassis with Holybro Pixhawk 6C and M9N GPS; Readytosky S500 quadcopter with Holybro Pixhawk 4
- boundary_platform: no
- degradation: sensor-fault
- degradation_observed: none
- evaluation_primary: integrity-reliability
- evaluation_all: designed-degradation, integrity-reliability
- sensors: position from the PX4 EKF (GPS, IMU) as a radar substitute, plus motion capture for the quadcopter; rate gyros; accelerometers; magnetometer heading (rover) or IMU attitude (quadcopter)
- compute: computer and runtime not reported; 0.01 s sample time in simulation; 1000-step trailing window
- compute_location: desktop-offline
- summary_result: On recorded Ackermann-rover logs with injected faults, KSFD's six-metric pattern isolated a 1.0 m white-noise position fault and a harmonic z-gyro fault, one run each; no detection rates.
- summary_limitation: Isolation assumes at most one faulty sensor; two simultaneous faults are only flagged, and statistical cutoff thresholds and onboard fault-tolerant integration are left to future work.
- survey_included: yes
- verification_level: full

## Problem

A faulty sensor can corrupt the state used by an autonomous vehicle. The
paper asks how to detect a faulty position, rate-gyro, accelerometer, or
attitude sensor and identify which one failed, without a vehicle dynamics
model, fault training data, or duplicated hardware. It treats ground
vehicles that stay horizontal and aerial vehicles moving in 3D.

## Mechanism

Kinematics-based sensor fault detection (KSFD) evaluates the single and
double transport theorems, which are exact relations between the position of
the vehicle relative to a point with zero inertial acceleration, its body-frame
derivatives, the angular velocity, and the inertial acceleration (pp. 2-3).
Each relation is computed from different sensor subsets: e_s (single
transport) uses attitude or heading, position, and rate gyro; e_d (double
transport) uses position, rate gyro, and accelerometers; e_a uses attitude or
heading, position, and accelerometers (p. 6, Table 3; p. 7, Table 5). The
first and second derivatives of position and the derivative of angular
velocity come from adaptive input and state estimation (AISE): a Kalman filter
for a discrete-time integrator model, an input-estimation subsystem updated by
recursive least squares with F-test variable-rate forgetting and a resetting
matrix, and adaptation of the process and sensor noise covariances (pp. 4-6).
Each error metric is the root-mean-square residual of one relation component
over a trailing window of delta steps (p. 6, Eqs. (66)-(68)) and is compared
with a fixed cutoff. A pattern table maps above-cutoff (AC) and below-cutoff
(BC) states to a faulty sensor: six metrics and six feasible cases (all
sensors healthy or exactly one faulty) out of 64 for ground vehicles (p. 6,
Table 4), nine metrics and nine feasible cases out of 512 for aerial vehicles
(p. 7, Table 6). Any other
pattern means a false positive or negative, or more than one faulty sensor
(p. 7). In the experiments the cutoff is twice the error magnitude at a step
before the fault (k = 1.5 delta for the rover, 3.5 delta for the quadcopter;
pp. 9, 11); in simulation it is twice the RMS error from the sensor noise
floor at k = 2 delta (p. 7). The window is delta = 1000 steps, chosen because
the AISE transient ends within 1000 steps (pp. 7, 9, 11).

## Baselines and controls

There is no baseline. The model-based, knowledge-based, neural, observer, and
hardware-redundancy methods of the introduction (pp. 1-2) are background and
are not run. The control in each example is the set of metrics that stay
below cutoff, which the pattern table uses to separate sensors.

## Platform and setup

- Numerical example (Sec. 6): a figure-8 trajectory x(k) = 2 + sin(2kT_s),
  y(k) = 2 + sin(2kT_s)cos(2kT_s) with T_s = 0.01 s and k from 1 to 6000
  (60 s); white Gaussian noise of 0.001 m on position, 0.0001 rad/s on the
  z gyro, and 0.01 g on the accelerometers (p. 7). Fault: x-accelerometer
  drift of 0.05 g/s from 30 s (p. 8).
- Rover logs (Sec. 7): an off-the-shelf Yahboom aluminum-alloy chassis "with
  Ackerman steering", a Holybro Pixhawk 6C, and an M9N GPS (p. 8; photo in
  Fig. 10(b), p. 9). The rover followed a zigzag of waypoints set in
  QGroundControl under the PX4 default waypoint tracking controller on a
  tennis court at the University of Michigan (pp. 8-9). Position from the PX4
  EKF, which fuses GPS, IMU, and other sensors, replaced the radar (p. 9).
  Faults were added to the logs afterwards: Example 7.1, white noise with
  1.0 m standard deviation on position from 20 s; Example 7.2, harmonic noise
  0.5 sin(0.1kT_s) on the z rate gyro from 30 s, with alpha = 0.05 (p. 9).
- Quadcopter logs (Sec. 8): a Readytosky S500 frame with a Holybro Pixhawk 4
  flew a Hilbert-curve waypoint path in the M-Air facility; position came from
  GPS and motion capture in place of radar (p. 11). Example 8.1: x-accelerometer
  bias of 0.5 g from 40 s (pp. 11-12). Example 8.2: z rate-gyro bias of
  "0.5 g" from 60 s plus x-accelerometer harmonic noise 5 sin(0.01kT_s) from
  80 s (p. 12). The paper gives the gyro bias in g, an acceleration unit.
- Each example is one run with one injected fault scenario. The paper names
  only the sample time of the simulation; the sample time of the logs is not
  stated.

## Evidence type and transfer

The strongest evidence is recorded robot data: the authors logged real rover
and quadcopter runs and injected artificial faults into the logs before
running KSFD (pp. 9, 11). KSFD did not run during the drives, did not drive
the vehicles, and no real sensor failed. All results are time plots of the
residuals and metrics against their cutoffs, with no table of detection
times, false alarms, or missed detections. The "radar" in the experiments is
the PX4 EKF position (rover) or GPS and motion-capture position (quadcopter),
so no real radar was tested. The simulation is a numerical example on an
analytic trajectory with no sensor or vehicle simulation. The authors call
KSFD real time because it uses only data up to the present (p. 7); this is a
causality property, not a measured runtime.

## Sensors

The method needs position relative to a point with zero inertial acceleration,
inertial angular velocity, and inertial acceleration, and is otherwise
"agnostic to specific sensor technologies" (p. 3). The ground case uses
position r_x, r_y, the magnetometer heading, the z rate gyro, and the x and y
accelerometers, assuming zero pitch and roll (p. 3; p. 4, Table 1). The aerial case
uses 3D position, IMU attitude, three rate gyros, and three accelerometers
(p. 4, Table 2). The radar is assumed to give position only (p. 3).

## Compute and latency

The paper reports no processor, per-step computation time, or memory. The
claim that KSFD is "not subject to latency" rests on causality (p. 7), and
the claim of reduced computational burden (p. 14) is not measured. Detection
delay depends on the 1000-step window and the cutoffs and is not reported.
In Example 6.1 the plots show e_d,x and e_a,x crossing their cutoffs only at
about 50 s, some 20 s after the drift begins at 30 s (p. 8, Fig. 5(a), p. 9,
Fig. 9(a), read from the rendered plots).

## Key quantitative results

- Pattern-table size: 6 error metrics and 6 feasible patterns (all sensors healthy or exactly one faulty) out of 64 for ground vehicles, 58 patterns left for multiple faults (p. 6, Table 4); 9 metrics and 9 patterns out of 512 for aerial vehicles, 503 left (p. 7, Table 6).
- Example 6.1, simulated x-accelerometer drift of 0.05 g/s from 30 s: e_d,x and e_a,x exceed their cutoffs while e_s,x, e_s,y, e_d,y, and e_a,y stay below apart from start-up spikes at about 10 s, which Table 4 assigns to the x accelerometer (p. 8, Figs. 5 and 7; p. 9, Fig. 9).
- Example 7.1, rover log with 1.0 m white noise on position from 20 s: all six metrics rise above their cutoffs at 20 s, which Table 4 assigns to the radar (position) sensor (p. 9; p. 10, Figs. 12, 14, 16).
- Example 7.2, rover log with 0.5 sin(0.1kT_s) on the z rate gyro: e_d,x, e_d,y, e_s,x, and e_s,y exceed their cutoffs and e_a,x and e_a,y stay below, which Table 4 assigns to the z rate gyro (p. 9; p. 11, Figs. 18, 20, 22). The setup text puts the fault onset of Examples 7.1 and 7.2 at step 2 delta (p. 9), while Example 7.2 states 30 s, and Figs. 18 and 20 show e_d,x, e_d,y, and e_s,y already above their cutoffs from about 20 s (read from the rendered plot).
- Example 8.1, quadcopter log with 0.5 g x-accelerometer bias from 40 s: e_d,x and e_a,x exceed their cutoffs and the three e_s metrics stay below, identified as the x accelerometer (p. 12; p. 13, Figs. 27 and 29). Fig. 27 also shows all three e_s metrics rising above their cutoffs at about 140-145 s, which the text does not discuss (read from the rendered plot).
- Example 8.2, z-gyro bias from 60 s plus x-accelerometer harmonic noise from 80 s: e_d,x, e_d,y, e_d,z, e_s,x, e_s,y, and e_a,x exceed their cutoffs; KSFD indicates that some sensor is faulty but cannot identify which (p. 12; pp. 13-14, Figs. 31, 33, 35). Fig. 31(c) shows e_d,z above its cutoff at about 15-30 s, before either fault (read from the rendered plot).
- The paper cites Tables 3 and 5 (the sensor tables) for the diagnostic patterns of Tables 4 and 6 (p. 7), and Examples 8.1 and 8.2 cite the ground-vehicle Table 4 for the aerial diagnosis (p. 12). The Section 7 introduction calls Example 7.2 an x-accelerometer harmonic-noise fault, while the example is a z rate-gyro fault (p. 9).

## Stated limitations

- KSFD is validated only with at most one faulty sensor at a time; with several simultaneous faults it indicates that at least one sensor is faulty but does not determine which (p. 2; Example 8.2, p. 12).
- Radar data were unavailable; position from the PX4 EKF (rover) or from GPS and motion capture (quadcopter) was used as a substitute (pp. 9, 11).
- Handling multiple simultaneous sensor failures and integrating KSFD with onboard processing and control systems for real-time fault-tolerant operation are future work (p. 14).
- Statistical techniques for setting the cutoff thresholds are future work (p. 14).
- Multiple sensor faults are described as rare in practice but a potential concern (p. 14).

## Transfer conditions

- Independence of the position source. In the experiments the position came
  from an EKF that also fuses the IMU (p. 9), while e_d and e_a compare that
  position with the same IMU's accelerometers and gyro. A common-cause fault
  could then shift both sides of a relation. A wheeled robot needs a position
  source that does not use the monitored IMU (for example LiDAR localization
  against a fixed frame), and that source must give position relative to a
  point fixed in the world.
- Planar assumption. The ground formulation sets pitch and roll to zero
  (p. 3); ramps, curbs, or rough terrain violate it and would raise the
  metrics without a sensor fault.
- Threshold tuning. Cutoffs are twice a healthy-segment error at one step of
  the same run (pp. 7, 9, 11), so they are fitted per run. False-alarm and
  missed-detection rates are not reported, and the plots show exceedances
  before the injected faults in Examples 7.2 and 8.2 and late exceedances in
  Example 8.1 (see Key quantitative results).
- Latency. With a 1000-step window (10 s at 0.01 s sampling) and a fixed
  cutoff, a slow drift was flagged about 20 s after onset in simulation.
- Rule-free here means that no expert fault knowledge is used; the diagnosis
  still relies on the fixed pattern tables and hand-set cutoffs.
- Faults were injected into logs; behavior under real sensor failure and in a
  closed loop is not shown.

## Code and data

The paper gives no code or data URL and no data-availability statement
(none found in the full text). Not verified elsewhere.

## Version family

A preprint of this work appeared as Verma and Bernstein (2024), arXiv:2309.05158v2
(p. 2; reference list, p. 15). AISE comes from earlier papers of the same
group (Verma, Sanjeevini et al., 2024; Verma, Lai, and Bernstein, 2024)
(p. 2). This library counts only the journal version.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | Sec. 1, p. 2 | "The scope of this paper is limited to single sensor fault scenarios, where KSFD successfully detects and identifies the faulty sensor." |
| C6 | qualifies | moderate | Sec. 7, p. 9 | "was used as a substitute for radar measurements in the analysis" |

## Page-cited excerpts

- **p. 2, Sec. 1.** "In the present paper, KSFD is experimentally validated under the condition that at most one sensor is faulty at any given time."
  The single-fault assumption bounds every isolation result in the paper.
- **p. 7, Sec. 5.2.** "KSFD operates in real time in the sense that it identifies a single faulty sensor during operation using data available up the present time without the need for future data."
  "Real time" means causal; no runtime or detection delay is measured.
- **p. 9, Sec. 7.** "To evaluate the performance of KSFD, artificial faults were introduced into the experimental data."
  The hardware evidence is fault injection into recorded logs, not real sensor failures or an online run.
- **p. 12, Example 8.2.** "However, it is not possible to identify the specific faulty sensors based on Table 4."
  With two faults the method only signals that something is wrong; the text cites Table 4 although the aerial patterns are in Table 6.
- **p. 14, Sec. 9.** "Finally, further research will investigate the development of statistical techniques for determining cutoff thresholds, improving both detection accuracy and robustness."
  The cutoffs used in the paper are heuristic, so detection accuracy is not characterized.

## Survey-usable statements

### Supported

- Exact kinematic relations (single and double transport) combined with causal numerical differentiation give a sensor-fault detector that needs no vehicle dynamics model, but it needs position relative to a world-fixed point, angular velocity, and acceleration.
- On recorded logs of an Ackermann rover with artificially injected faults, the six-metric pattern table identified a 1.0 m white-noise position fault and a harmonic z rate-gyro fault, one run each, shown in plots only.
- On quadcopter logs, an injected x-accelerometer bias was identified, while a combined gyro and accelerometer fault was detected but not attributed.

### Not supported

- KSFD detects faults faster or more reliably than other methods: no baseline is run and no detection time, false-alarm, or missed-detection rate is reported.
- KSFD runs onboard in real time: it was applied to recorded logs, no computer or runtime is reported, and onboard integration is future work (p. 14).
- KSFD has no detection latency: the window and cutoffs delay detection; in Example 6.1 the drift was flagged about 20 s after onset (Figs. 5 and 9).
- KSFD was validated on radar or on real sensor failures: position came from the PX4 EKF or from GPS and motion capture, and all faults were injected into logs.
- KSFD isolates multiple simultaneous faults: Example 8.2 shows that it cannot.
- KSFD reduces computational burden relative to model-based methods: this is stated (p. 14) but not measured.
- The metrics stay below cutoff whenever the sensors are healthy: the plots show exceedances before the injected faults in Examples 7.2 and 8.2 and at about 140-145 s in Example 8.1.

## Verification log

- 2026-10-27 | host: Kiro | scope: full text read (Secs. 1-9); Tables 3-6 read from the rendered p. 6 and p. 7 images; Figs. 3-35 read from rendered images of pp. 7-14 (zoomed crops of Figs. 18, 27, and 31); setup text checked on pp. 2-4 and 7-12 | corrections: rewritten in English to the template; quadcopter controller no longer described as the PX4 default; cutoff rule per experiment stated; pre-onset and late metric exceedances, Table cross-reference errors, and the Example 7.2 onset inconsistency recorded; limitations restricted to author statements (details in tmp/corrections/E51.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/ab14e51d5ec2e4eddac1bc59/

## Original abstract

Sensor-fault detection is crucial for the safe operation of autonomous vehicles. This paper introduces a novel kinematics-based approach for detecting and identifying faulty sensors, which is model-independent, rule-free, and applicable to ground and aerial vehicles. This method, called kinematics-based sensor fault detection (KSFD), relies on kinematic relations, sensor measurements, and real-time single and double numerical differentiation. Using onboard data from radar, rate gyros, magnetometers, and accelerometers, KSFD identifies a single faulty sensor in real time. To achieve this, adaptive input and state estimation (AISE) is used for real-time single and double numerical differentiation of the sensor data, and the kinematically exact single and double transport theorems are used to evaluate the consistency of the data. Unlike model-based and knowledge-based methods, KSFD relies solely on sensor signals, kinematic relations, and AISE for real-time numerical differentiation. For ground vehicles, KSFD requires six kinematics-based error metrics, whereas, for aerial vehicles, nine error metrics are needed. Simulated and experimental examples are provided to evaluate the effectiveness of KSFD.
