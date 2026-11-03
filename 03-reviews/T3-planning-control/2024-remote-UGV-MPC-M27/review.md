# Remote UGV Control via Practical Wireless Channels: A Model Predictive Control Approach

## Metadata

| Field | Value |
|---|---|
| ID | M27 |
| Title | Remote UGV Control via Practical Wireless Channels: A Model Predictive Control Approach |
| Authors | Jinghao Cao, Subhan Khan, Wanchun Liu, Yonghui Li, and Branka Vucetic |
| Venue | IEEE Transactions on Intelligent Vehicles, early-access article, pp. 1-13 (accepted version; no volume or issue in the BibTeX export) |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/tiv.2024.3471990](https://doi.org/10.1109/tiv.2024.3471990) |
| Official URL | https://ieeexplore.ieee.org/document/10702475/ |
| Theme folder | T3-planning-control |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T3-planning-control/2024-remote-UGV-MPC-M27/paper.pdf` and `02-fulltext/T3-planning-control/2024-remote-UGV-MPC-M27/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T3-planning-control/2024-remote-UGV-MPC-M27/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: numerical
- evidence_all: numerical
- protocol_caveats: none
- platform_class: differential-drive
- platform: simulated UGV modeled as unicycle kinematics (radius 0.34 m, 1 m/s, 140 deg/s); no physical robot
- boundary_platform: no
- degradation: dynamic-objects, communication-delay-loss
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: simulated range-bearing beacon at the origin (Gaussian noise); no onboard sensor
- compute: multi-core MPC time per step 32.47 ms (Exp. 1) and 33.92 ms (Exp. 2) at a 10 ms sampling time; processor and solver not reported
- compute_location: not-reported
- summary_result: In numerical circle and eight-curve tracking with packet loss and delay, Euclidean error averaged 22.38 and 13.48 cm, versus at least 24.54 and 22.99 cm for three baselines.
- summary_limitation: The authors model only quasi-static Rayleigh fading and note the UGV may not keep the safety margin from all obstacles once localization accuracy degrades.
- survey_included: yes
- verification_level: full

## Problem

A remote controller drives a ground vehicle over wireless links that delay
and drop packets in both directions (sensor to controller and controller to
actuator), while the vehicle is subject to process noise and noisy position
measurements and must avoid static and moving obstacles. The paper asks how
to keep reference tracking and obstacle avoidance working under these
combined imperfections.

## Mechanism

The vehicle is a unicycle kinematic model with inputs v and omega, taken from
reference [31] of the paper (Wang and Low, skidding and slipping in wheeled
mobile robots) and discretized by first-order Euler integration (pp. 2-3).
Process disturbances are additive Gaussian noise on v and omega; the authors
motivate them by skidding or slippage (p. 2). A single beacon at the origin
measures range and bearing with Gaussian noise (p. 3).

The channel model draws delays from a discrete uniform distribution up to a
maximum latency and packet errors from a quasi-static Rayleigh fading model
with a short-blocklength error formula (p. 3). A "smart receiver" keeps the
packet with the smallest age of information. A compensator predicts the
current measurement from a delayed one using the control sequences stored in
a buffer, feeds the prediction into an EKF, and uses the EKF estimate as the
initial state of a direct multiple-shooting MPC (p. 4; Algorithm 1, p. 5). The MPC
cost is quadratic in state and input error, with velocity and angular-rate
bounds and circular obstacle constraints (Eqs. 14-16). The full predicted
input sequence is sent to the actuator buffer so that the actuator can apply
a stored input when a packet is late or lost. Instead of the 0.34 m robot
radius, the MPC uses a 0.54 m safety radius to absorb noise (p. 5).

## Baselines and controls

Experiments 1 and 2 compare the method with one representative controller
from each of three families: a predictive PID for packet dropouts
(reference [18]), an LQR with packet-loss compensation ([20]), and a robust
economic MPC with delay handling ([16]) (p. 6). The paper does not describe
how these comparators were implemented or tuned. PID and LQR have no obstacle
avoidance mechanism (marked NA in Tables III and IV), and the MPC of [16]
does not handle packet loss or measurement noise (p. 6). All comparisons use
the nominal channel conditions only. Experiment 3 (point stabilization)
varies the prediction horizon (Table V) and the channel conditions
(Table VI) for the proposed method alone; no comparator appears there.

## Platform and setup

All results come from the authors' own numerical simulation. Nominal
settings (p. 5): Q = diag([0.005, 0.0349])^2, R = diag([0.1, 0.0349])^2,
prediction horizon N = 100, sampling time 10 ms; sensor-to-controller SNR
15 dB with 50 ms maximum delay, controller-to-actuator SNR 20 dB with 10 ms
maximum delay, code rate 1, block length 100 bits. Vehicle limits (p. 6):
radius 34 cm, safety margin 54 cm, 1 m/s forward or backward, 140 deg/s.

- Experiment 1 (pp. 6-7): circle of radius 5 m, 50 s, four static obstacles
  (radii 0.15 to 0.5 m) and four moving obstacles (0.2 to 0.5 m/s).
- Experiment 2 (p. 8): eight-curve x = 5 sin(theta), y = 5 sin(theta)
  cos(theta), again with four static and four moving obstacles.
- Experiment 3 (p. 9): point stabilization from [0, 0, 0] to [1.5, 1.5, 0]
  past a 0.3 m diameter obstacle at (0.5, 0.5).

The paper does not state the number of runs or random seeds per setting; the
tables appear to report one run each, and Fig. 10 shows per-step error and
time distributions for Experiments 1 and 2.

## Evidence type and transfer

The authors describe a "simulated UGV" (p. 1). The simulation integrates an
abstract unicycle model with additive noise and an analytic range-bearing
measurement; no physics engine, sensor simulator, robot software stack, or
hardware is used. The evidence is therefore coded numerical. The conclusion's
phrase "when implemented on a UGV" (p. 11) refers to this simulated agent.
The results show tracking error, obstacle clearance, and per-step solve time
of the scheme within its own channel and noise model. They cannot show
behavior under real Wi-Fi traffic, real localization error, vehicle dynamics,
or actuator limits beyond the two rate bounds.

## Sensors

One simulated beacon at the origin returns the range and bearing of the
vehicle with Gaussian noise (sigma_r = 0.1, sigma_alpha = 0.0349 rad). The
problem formulation attributes measurement noise to "imperfect radar
readings" (p. 2). Ground truth is the simulated true state.

## Compute and latency

Tables III and IV report a "multi-core process time" per step: 32.47 ms
(Exp. 1) and 33.92 ms (Exp. 2) for the method (pp. 8-9). Table V reports
single-core and multi-core MPC times of 10.6 to 14.4 ms and 8.4 to 11.6 ms
for horizons 10 to 100 in point stabilization (p. 9). The processor, number
of cores, programming environment, and optimization solver are not reported.

## Key quantitative results

- Experiment 1, circle with obstacles, nominal channel: average Euclidean distance error of the method 22.38 cm versus 24.54 cm (LQR), 42.41 cm (MPC [16]), and 80.97 cm (PID) (p. 8, Table III).
- Experiment 1 step heading error: method 2.214 deg versus 1.499 deg (LQR), 2.170 deg (MPC [16]), and 4.671 deg (PID); LQR and the MPC of [16] are lower (p. 8, Table III).
- Experiment 1 multi-core process time: method 32.47 ms versus 0.025 ms (PID), 42.80 ms (MPC [16]), and 76.88 ms (LQR) (p. 8, Table III).
- Experiment 2, eight-curve with obstacles: average Euclidean error 13.48 cm versus 22.99 cm (MPC [16]), 25.42 cm (LQR), and 81.37 cm (PID); step heading error 0.405 deg versus 2.714 deg (LQR), 2.796 deg (MPC [16]), and 4.776 deg (PID); process time 33.92 ms versus 0.026 ms (PID), 41.04 ms (MPC [16]), and 89.30 ms (LQR) (p. 9, Table IV).
- Collision avoidance is marked achieved for the method and failed for the MPC of [16] in both experiments; PID and LQR are NA because they have no avoidance mechanism (pp. 8-9, Tables III and IV).
- Point stabilization over the horizon: N = 10, 15, 20, 50, 100 give steady-state position errors of 29.37, 5.33, 16.4, 16.5, and 14.7 cm, heading errors of 35.02, 21.45, 7.341, 0.5910, and 0.3617 deg, and multi-core times of 9.7, 9.2, 8.4, 8.7, and 11.6 ms (p. 9, Table V).
- Point stabilization over 15 channel settings (SNR 5, 10, 15, 20, 100 dB with packet error rates 0.696, 0.312, 0.112, 0.037, 0; sensor-to-controller maximum latency 10, 30, 50 ms): steady-state position error 1.09 to 1.89 cm, heading error 0.0411 to 0.8037 deg, and collision avoidance in every setting, with no monotone trend in SNR or latency (p. 10, Table VI).
- Internal inconsistencies: the Experiment 1 text cites Table IV for its results, which are in Table III (p. 7); the text calls the 0.0475 heading error "radians" while Table VI lists it in degrees (pp. 9-10); at the nominal N = 100, Table V gives 14.7 cm steady-state position error, but the text and Table VI give 1.82 cm (pp. 9-10); and the text says longer horizons lower the steady-state position error although Table V is lowest at N = 15 (p. 9).
- The Fig. 10 box plots do not match the tables: read from the plots, the mean errors are about 0.13 m (method) and 0.22 m (MPC [16]) for the circle and about 0.12 m and 0.42 m for the eight-curve, against 22.38 and 42.41 cm (Table III) and 13.48 and 22.99 cm (Table IV) (p. 11, Fig. 10).

## Stated limitations

- Only quasi-static Rayleigh fading channels are studied; channel-model variations are not considered (p. 6).
- In the eight-curve run, localization accuracy diminishes toward the end, and the vehicle may not keep a safe distance from all obstacles within the safety margin (p. 9).
- A localization error of 15 cm makes the MPC control more difficult in the circle run (p. 7).
- A longer horizon does not necessarily improve performance, because the MPC processing time grows with the horizon (p. 9).
- Integration with pathfinding algorithms in environments that more closely simulate real-world conditions is left for future work (p. 11).

## Transfer conditions

The per-step solve times in Tables III and IV (32.47 and 33.92 ms) exceed
the 10 ms sampling time, and the paper does not explain how the simulation
handles a solve that takes longer than one step; a real-time deployment would
need a longer period or a faster solver. Safety rests on a fixed 0.2 m
inflation of the robot radius, not on an uncertainty-dependent bound or a
monitor. Slip is represented only by zero-mean Gaussian noise on v and omega
(sigma_v = 0.005), so the results say nothing about systematic slip. The
range-bearing beacon at the origin and the obstacle positions known to the
MPC replace any onboard perception. Channel parameters (SNR, block length,
delay bounds) are configured, not measured on a network. A wheeled robot that
reuses the scheme needs a measured channel model, a localization source, and
a solver that fits its control period.

## Code and data

The paper does not state that code or data are released.

## Version family

No conference version or extension was found in the library.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | weak | Sec. V-B, p. 7 | "the accuracy of the localisation does make the MPC control more difficult" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | weak | Sec. V-A, p. 5 | "Given the presence of process noise and measurement noise, an additional safety margin is necessary to ensure the robot’s safe task completion." |
| C6 | qualifies | moderate | Sec. V-A, p. 5 | "In this section, a series of simulation experiments have been conducted to evaluate the applicability of the aforementioned method across a range of tasks." |

## Page-cited excerpts

- **p. 6, Sec. V-A.** "Notably, we only focus on Quasi-Static Rayleigh Fading channels, thus the channel model variations are not considered in this study."
  The channel model is fixed; robustness to other fading or interference models is not tested.
- **p. 9, Sec. V-C.** "However, it may not be able to maintain a safe distance from all obstacles within the safety margin."
  The authors concede that the fixed margin can be violated once localization error grows.
- **p. 9, Sec. V-D.** "The steady-state error is 1.82 centimeters, and the heading error is 0.0475 in radians."
  The nominal point-stabilization result; Table VI lists the same heading value in degrees, and Table V reports 14.7 cm at the same horizon.
- **p. 11, Sec. VII.** "we aim to integrate this method with pathfinding algorithms to tackle more intricate tasks within environments that closely simulate real-world conditions."
  Planning and more realistic environments are future work.

## Survey-usable statements

### Supported

- In numerical simulation with configured packet loss and delay, an MPC with buffered-input compensation and an EKF had lower average Euclidean tracking error than PID, LQR, and a delay-only MPC on circle and eight-curve references (22.38 and 13.48 cm).
- In simulated point stabilization, the scheme kept steady-state position error between 1.09 and 1.89 cm over packet error rates from 0 to 0.696 and sensor-to-controller latencies up to 50 ms.

### Not supported

- The method is best on every metric: in Experiment 1 its heading error (2.214 deg) is higher than that of LQR (1.499 deg) and the MPC of [16] (2.170 deg), and PID has the lowest process time in both experiments.
- The scheme was validated on a physical UGV or a real wireless network: all results are numerical simulation with configured channel parameters.
- The scheme runs in real time: the per-step solve times exceed the 10 ms sampling time, and no processor is reported.
- Tracking error falls monotonically with the horizon or degrades with worse channels: Table V is lowest at N = 15, and Table VI shows no monotone trend.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read (Secs. I-VII); Tables III, IV, V, and VI and Fig. 10 read from rendered page images of pp. 8-11; excerpts and pages checked against the PDF | corrections: rebuilt in template format; evidence setting coded numerical; comparator scope limited to Experiments 1 and 2 under nominal channels; reviewer observations moved out of stated limitations and author limitations added; horizon trade-off statement corrected against Table V; table and figure inconsistencies recorded; C2 and C5 recoded (details in tmp/corrections/M27.csv)
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.

## Original abstract

In addressing wireless networked control systems (WNCS) subject to unexpected packet loss and uncertainties, this paper presents a practical Model Predictive Control (MPC) based control scheme with considerations of of packet dropouts, latency, process noise and measurement noise. A discussion of the quasi-static Rayleigh fading channel is presented herein to enhance the realism of the underlying assumption in a real-world context. To achieve a desirable performance, the proposed control scheme leverages the predictive capabilities of a direct multiple shooting MPC, employs a compensation strategy to mitigate the impact of wireless channel imperfections. Instead of feeding noisy measurements into the MPC, we employ an Extended Kalman Filter (EKF) to mitigate the influence of measurement noise and process disturbances. Finally, we implement the proposed MPC algorithm on a simulated Unmanned Ground Vehicle (UGV) and conduct a series of experiments to evaluate the performance of our control scheme across various scenarios. Through our simulation results and comparative analyses, we have substantiated the effectiveness and improvements brought about by our approach through the utilization of multiple metrics.
