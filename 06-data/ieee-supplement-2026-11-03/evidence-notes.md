# Selected-source reading notes — supplementary IEEE batch

These are targeted readings, separate from the 127 completed review cards. They do not establish whole-paper verification or add papers to the manuscript statistics. Page numbers are physical PDF pages. Source paths and hashes are in [manifest.json](manifest.json).

## N01 — Adaptive error-state fusion for ground-vehicle LIO

Read: abstract; adaptive weighting and experimental setup on p. 5; runtime discussion and conclusion on p. 8. The complete derivation, ablations, and numerical tables were not audited; no numerical performance results are retained.

AESF-LIO separates ground and non-ground point-to-plane residuals and fuses the resulting error-state corrections. Its adaptive roll/pitch weighting is selected from the residuals of the two groups (p. 5). It addresses the influence of imbalanced geometric constraints using LiDAR and IMU information; it does not introduce a wheel measurement or a new independent sensing channel.

The evaluation compares trajectory errors in simulation, public sequences, and data from a vehicle equipped with LiDAR/IMU. The conclusion states that the method was “mainly validated in relatively flat urban environments” (p. 8), leaving more difficult non-flat settings for future investigation. These estimator results should not be presented as proof of improved closed-loop navigation on uneven terrain.

Survey use: compare geometry-aware weighting with degeneracy-aware updates and additional sensing modalities. Distinguish poor weighting of available constraints from a genuinely missing observable direction; redistributing existing measurements alone does not supply independent information in an unconstrained direction.

## N05 — Graph-based SLAM-aware exploration

Read: abstract; comparison protocols on pp. 6–7; Pioneer3AT deployment and conclusion on pp. 7–8. The complete pruning proof and result tables were not audited; no numerical performance values are retained.

This planner deliberately schedules informative loop closures over a supplied topo-metric graph and combines the plan with online graph updating and replanning. The comparison uses the same Karto SLAM system across planners (p. 7). The authors also distinguish the prior-aware methods from baselines that do not require the same prior information (p. 6); this input difference matters when interpreting comparative performance.

The hardware demonstration explores a campus corridor using a Pioneer3AT, wheel encoders, and a planar laser. Its camera is used for visualization, and the initial topo-metric information comes from a satellite map (pp. 7–8). The conclusion specifically targets environments with rich topology information and leaves an online construction of the prior graph and a multirobot extension to future work (p. 8).

Survey use: include a prior-aware, localization-aware planning comparator alongside frontier exploration and traversability/localizability methods. It supplies an existing integration, with concrete requirements on prior information and useful loop-closure opportunities. A graph-reliability objective and a calibrated probability of unsafe localization remain different quantities.

## N06 — Predictive data acquisition for visual teach, repeat and learn

Read: abstract; dataset and comparison protocol on p. 5; deployment discussion and conclusion on pp. 7–8. No performance-table values or significance-test results were retained; the complete model-training pipeline was not audited.

The method uses ambiguity of visual matching to influence which locations supply additional training examples. The evaluation uses Witham Wharf and Cestlice recorded datasets (p. 5). The conclusion explicitly says that the pipeline is presented using datasets collected by real robots (p. 8). Evaluation data include revisits at later dates, rather than evidence of uninterrupted autonomous service over the interval between sessions.

The discussion links useful acquisition to accessible locations, task constraints, and exploration time. It also identifies blind spots when a location is never revisited and leaves scheduling both where and when to acquire observations to future work (pp. 7–8).

Survey use: compare representation maintenance through selective data acquisition with map updates and resource scheduling. Keep model/matching improvement on recorded data separate from deployment availability, task completion, and maintenance cost on a robot executing a long-term mission.

## N07 — Multi-robot active graph exploration

Read: abstract; relation to earlier work on p. 2; simulation setup on p. 6; conclusion on p. 8. Complete approximation proofs and numerical tables were not audited; no numerical performance values are retained.

The method combines coverage planning with informative loop-edge selection, formulated as non-monotone submodular maximization. The authors explicitly extend their previous single-robot SLAM-aware exploration work (N05, cited as [22]) to the multi-robot problem (p. 2). These are distinct publications and problems within a related method family.

The evaluation uses simulated two-dimensional graph environments (p. 6). The conclusion states that prior topo-metric information is required and identifies incorporation of the planner into a multi-robot SLAM system as future work (p. 8). The graph experiments therefore do not establish operation of an integrated physical robot team, performance under communication outages, or recovery from localization failures.

Survey use: compare how loop opportunities and path length enter single-robot and team objectives. Present the approximation guarantee with its graph objective and assumptions; keep it separate from closed-loop localization reliability and physical deployment evidence.

## N08 — Anisotropic terrain-aware autonomous exploration

Read: cost-model scope on p. 4; evaluation setup on p. 5; deployment and platform discussion on p. 7; conclusion on p. 8. Numerical result tables and complete derivations were not audited; no numerical performance improvements are retained.

Euler Cost couples travel direction with terrain slope in a sparse navigation graph. The authors explicitly describe it as a lightweight anisotropic quasi-static traversal-cost heuristic, rather than a full robot dynamics model (p. 4). Nonlinear wheel slip, suspension transients, and actuator-level force interactions are omitted. The cross-slope term is a geometric proxy for rollover risk, rather than a calibrated failure probability.

Hardware demonstrations use an FW-001 four-wheel differential-drive robot and a DeepRobotics Jueying Lite3 quadruped, with robosense LiDAR, FAST-LIO, and an onboard computer (pp. 5, 7). The cross-platform discussion also identifies a change in LiDAR field of view (p. 7). Result differences between these platforms cannot be attributed to the planner alone.

Survey use: add a direction-dependent traversability comparator. Distinguish the computationally efficient geometric cost, the measured maximum-roll metric, and any stronger claim of dynamic safety. Preserve sensing and embodiment differences when discussing transfer between wheeled and legged robots.

## N09 — Co-NavGPT

Read: abstract; task definition and architecture on p. 3; global/local policy on p. 5; evaluation and deployment on pp. 5–7; conclusion on pp. 7–8. Table I was checked in the rendered PDF on p. 6. The remaining mathematical and implementation details were not comprehensively audited.

The VLM assigns frontiers from a shared map and robot states. A Fast Marching Method local policy executes the assigned goals and updates them from observations (p. 5). The hardware demonstration uses quadrupedal robots, initial Generalized-ICP alignment, onboard localization, and a workstation for perception and planning (p. 7). This is a useful existing integration of semantic reasoning, team allocation, and geometric navigation. It does not establish performance on wheeled platforms or robustness to communication loss.

Table I reports two-agent success rate 0.681 for Co-NavGPT versus 0.625 for Cost-Utility, and SPL 0.369 versus 0.328 for Greedy (p. 6). These comparators differ by metric and should be named separately. Co-NavGPT does not have the highest SPL in every setting: with one agent it scores 0.236 versus 0.239 for Multi-SemExp. The quantitative evidence comes from HM3D episodes; the hardware examples are separate demonstrations.

The stated failure cases include incomplete reconstructed regions, multi-floor navigation, and object-detection errors (p. 7). The reported system frequency should not be interpreted as a measurement of each VLM API call's latency or onboard execution of the entire stack. The paper explicitly places perception and planning on an external workstation (p. 7).

Survey use: compare with GSON and other semantic/geometric architectures in the semantic and multi-robot chapters. Qualify claims about missing integration. Investigate delayed or stale assignments separately from nominal coordination success.

## N10 — NMPC-augmented visual navigation and safe learning control

Read: abstract; safety supervisor and system configuration on p. 5; recovery handling and experimental comparisons on pp. 6–7; conclusion on p. 8. The configuration and recovery passage were also checked on rendered pp. 5–6. Numerical performance cells in Table I were not transcribed or used.

This system combines stereo ORB-SLAM3, NMPC wheel-reference updates, learned actuator control with adaptation, and a separate safety supervisor. The hardware is a 6,000 kg skid-steering vehicle with electro-hydrostatic drives (p. 5). INS-RTK supplies the experimental reference; it should not be silently attributed to the vision-only navigation estimate.

The paper states that “any tracking loss triggered a safety stop and relocalization attempt” (p. 6). If relocalization failed, SLAM was restarted and the trial repeated. The evaluation therefore contains an implemented localization-loss response, while trial repetition must remain distinct from successful autonomous continuation of the same mission.

The safety analysis concerns the paper's defined pose-error bound and controller assumptions (p. 5). It is not evidence that arbitrary, undetected localization bias is safely handled. The ground-surface and trajectory comparisons on pp. 6–7 also separate the high-level vision/NMPC effect from low-level actuation comparisons.

Survey use: add an existing estimation/control/recovery comparator to the planning, reliability, and localization-triggered recovery discussions. Focus the remaining question on trustworthy triggers and the measured outcome of recovery, rather than on a general absence of integration. The actuator design and vehicle scale are transfer conditions.

## N11 — Range-based multi-robot integrity monitoring

Read: abstract and contribution scope on pp. 1–2; validation and sensor emulation on p. 6; hardware implementation on p. 7. The p. 6 layout was inspected. The complete derivation and convergence proof were not audited; no performance numbers are retained here.

The proposed monitor uses inter-robot ranges to detect affected agents and reconstruct localization errors. The abstract describes a distributed formulation using sequential convex programming and ADMM. Its hardware demonstration has a narrower implementation: the monitor is centralized at a ground station (p. 7).

The mixed-reality experiment combines real Crazyflie UAVs and virtual PX4 agents. Inter-robot range measurements are emulated from motion-capture and simulator poses (pp. 6–7). These are important qualifications: the experiment does not establish robustness of physical UWB ranging or a fully distributed implementation on a moving wheeled team.

Survey use: compare shared-state error diagnosis with correlation-aware map repair and collaborative localization. Preserve the distinction between a distributed algorithm, the implementation actually evaluated, and the sensing channel actually measured. The source qualifies broad claims that shared-state fault reconstruction has not been studied.

## N13 — Predictive fault tolerance in robot swarms

Read: abstract; simulation and robot setup on p. 2; selected fault-model, detection, and resolution passages on pp. 3–5; experimental discussion on pp. 6–7; conclusion on pp. 7–8. Complete model equations and numerical result tables were not audited; no performance percentages are retained.

The study models gradual motor and sensing degradation and compares shutdown after fault detection with withdrawal to a maintenance base while the affected robot can still travel. All experiments use ROS 2 and Gazebo Classic, with homogeneous simulated TurtleBot3 differential-drive robots (p. 2). Foraging resource collection is the task outcome. Separate experiments use an idealized detection trigger and the proposed behavioral detector; these should not be conflated.

In the predictive resolution, robots that reach the base are assumed to receive maintenance before redeployment or replacement (p. 5). If they fail to return, they remain stranded. This is an explicit maintenance assumption in simulation, rather than a physical repair demonstration. The conclusion identifies intelligent online path planning within fault resolution as future work (p. 8).

Survey use: include an existing detection-to-response mechanism and a task-level comparison. Analyze when to withdraw, whether the robot can still reach safety, and the consequences of a stranded teammate. Preserve the simulated degradation model, assumed maintenance service, and absence of physical swarm deployment when assessing applicability.

## N15 — Resilient planning with minimal STL relaxation

Read: abstract; runtime correction/replanning and case-study setup on p. 6; selected comparison/scalability passages on p. 7; discussion and conclusion on p. 8. Complete formal proofs and numerical tables were not audited; no performance numbers are retained.

The framework monitors a trajectory against Signal Temporal Logic requirements, attempts a local control-barrier-function correction, and invokes global mixed-integer replanning when local correction is infeasible or unsuitable. It permits changes to task time windows and task removal within the specified allowance (pp. 1, 6–7). Completing a relaxed mission therefore differs from satisfying every original requirement.

The case studies are numerical simulations using MATLAB optimization tools and Robotarium (p. 6). Their dynamic-obstacle scenarios do not establish physical recovery after a localization or actuator fault. The scalability discussion also distinguishes relatively small local quadratic programs from the computational burden of global mixed-integer planning as mission size grows (p. 7).

Survey use: compare recovery policies by what is preserved, relaxed, or abandoned after disruption. Include the allowed mission changes and solver burden as explicit conditions; keep trajectory repair and task relaxation separate from sensor-fault diagnosis and physical repair.

## N16 — Set-based LPV fault diagnosis for ground vehicles

Read: abstract; selected model and bounded-uncertainty passages on pp. 2–4; validation setup on p. 8; fault-injection and runtime discussion on p. 9; detection/isolation discussion on pp. 10–11; conclusion on pp. 11–12. Complete derivations and numerical result tables were not audited; no fault-magnitude or runtime values are retained.

The method combines online zonotopic set-membership estimation with invariant-set analysis of minimum detectable and isolable faults. Observer gains are computed offline. Its lateral vehicle model and uncertainty bounds define the domain of these guarantees (pp. 2–4). Detectability and isolability are different conditions; a fault that separates from the healthy set may still overlap another fault class (pp. 10–11).

The validation uses real measurements acquired from a prototype vehicle on a test track, including IMU yaw rate, odometry speed, Correvit sideslip, and a steering-angle encoder (p. 8). The diagnostic study then considers injected actuator and sensor fault signals, with the computation comparison performed in MATLAB on a workstation (p. 9). This establishes a data-backed diagnosis case, rather than an onboard fault-tolerant controller evaluated during physical failures.

The conclusion leaves fault estimation and fault-tolerant control for future work (p. 12). Survey use: strengthen the comparison between residual-based alarms, explicit fault-separation conditions, and recovery actions. Preserve the model/noise bounds, measurement availability, and separation between collected vehicle data and the evaluated diagnostic computation.

## N18 — Proactive anomaly detection with multisensor fusion

Read: abstract; method, data collection, and model input on pp. 3–4; experimental setup on p. 5; real-time test on p. 7, including its footnote; limitations and conclusion on p. 8. The p. 7 footnote was verified in the rendered PDF. No numerical table results were retained.

PAAD predicts future failure from current RGB/LiDAR observations and an image representation of the controller's planned path (p. 3). The data come from a skid-steering TerraSentia ground robot. Failure labels are tied to states requiring human intervention; during collection an operator disengages autonomy, repositions the robot, and restarts it (p. 3). The paper therefore supplies a useful proactive-monitoring comparator with an explicit failure definition.

The real-time test requires a precise qualification: footnote 3 states that it “was performed on streaming data from rosbags” (p. 7). It measures the detector's behavior on replayed field observations. The inspected evaluation does not establish that PAAD's alerts caused an autonomous recovery or reduced failures in closed-loop deployment. The conclusion also notes unavoidable false detections when both sensing modalities are blocked (p. 8).

Survey use: compare proactive detection with localization-integrity alarms and implemented recovery supervisors. Keep prediction quality, streaming execution, and the effectiveness of an executed response as separate evidence claims.

## N19 — Active collision-based navigation for wheeled robots

Read: abstract; active collision planning on p. 4; implementation and hardware protocol on p. 5; hardware localization results, simulation planning test, and conclusion on p. 6. The complete filter derivation was not audited. No numerical table cells were retained.

The method turns detected contact into a map-conditioned observation, incorporated into particle-filter and EKF localization. Its planner inserts contact events when propagated position uncertainty would exceed a threshold (p. 4). This is a concrete existing mechanism linking an action to future localization information.

The experimental settings must remain distinct. In the hardware localization experiment the operator remotely drives the robot into obstacles and returns it to its starting position (p. 5). The prior map is built with LiDAR; online localization uses IMU and wheel odometry, with motion capture for reference. The active bounce planner is evaluated separately in simulation (p. 6, Sec. V-D). These results do not establish autonomous contact-planned recovery on physical hardware after an actual sensor failure.

Survey use: include a contact-based information-gathering alternative alongside modality switching and geometry-seeking exploration. Preserve the known-map requirement, contact/detection assumptions, and the separation between a teleoperated hardware localization experiment and simulated active planning. A covariance threshold is not itself a calibrated integrity guarantee.

## N02 — SE(2)-constrained LiDAR-inertial odometry

Read: abstract on p. 1; selected IMU/model passages on pp. 3–4; experimental protocol and conclusion on pp. 6–8. Numerical result tables and the full derivation were not audited; no comparative accuracy values are retained.

The estimator parameterizes the ground-vehicle pose on SE(2) and incorporates departures in height, roll and pitch as stochastic perturbations of the LiDAR residuals (p. 4). This is a motion-prior/noise-model response, rather than an independently observed correction for arbitrary nonplanar motion. The indoor AGV uses a VLP-16 and Intel NUC i5-10210U; Vicon provides the reference, and the robot is remotely controlled (p. 6). Outdoor sequences use an IMU and GPS reference (p. 7).

The conclusion explicitly states that the method may fail when ground slope varies significantly (p. 8). Thus the model is a useful comparator for wheel/contact priors and local ground manifolds, with a stated boundary on terrain variation. The reviewed experiments establish estimation behavior, not improved closed-loop mission completion.

Survey use: Section IV, motion priors/contact/adaptation, alongside M24, M43 and M39. Compare fixed planar reduction, stochastic departures, locally estimated terrain and slip-dependent wheel information. Check result cells and reference quality before adding numerical comparisons.

## N03 — Trace-imprint estimation of wheel slip and sideslip

Read: abstract and scope on p. 1; selected trace-formation model on p. 3; image processing/testbed on p. 6; operating limits and conclusion on pp. 7–8. Numerical result tables and the full lug/soil derivation were not audited.

The method estimates longitudinal slip and lateral sideslip from the geometry of lug imprints in deformable soil. The rover testbed uses rigid lugged wheels, a camera/IMU and laptop processing; the image scale assumes that trace width matches wheel width during straight travel, an approximation the authors acknowledge (p. 6).

The method relies on distinct, preserved imprints. The experimental discussion reports failure above slip ratio 0.6 on sand when the required feature becomes indistinguishable (p. 7). The applicability discussion excludes crushed-stone floors and muddy terrain (p. 8). Integration with visual/inertial navigation and vehicle motion control is future work. Estimating slip is consequently separate from correcting odometry or demonstrating slip-aware control.

Survey use: Section IV, motion priors/contact/adaptation, and terrain transfer in Section X. Compare this contact/terrain observation with M39's wheel/IMU fusion and learned wheel models. Retain soil and wheel requirements; do not generalize it to ordinary wheels on warehouse floors.

## N04 — Non-reproducibility in LiDAR-inertial odometry

Read: abstract on p. 1; protocol on p. 5; implementation ablations and arithmetic-order experiment on pp. 6–7; conclusion on p. 8. Code changes were not executed independently and numerical table cells were not audited.

The study separates nondeterministic implementations from changing experimental conditions. Its protocol initializes subscribers before playback, buffers data to control frame loss and repeats each system/sequence experiment 30 times; parameters are empirically tuned rather than left at defaults (p. 5). It compares original implementations with deterministic variants. The observed variability becomes more pronounced on low-channel LiDAR recordings or geometrically degenerate scenes (p. 6).

The arithmetic experiment changes matrix-addition order while preserving the exact-arithmetic expression; observed pose results still vary (pp. 6–8). The authors leave a rigorous mathematical explanation and additional nondeterministic mechanisms for future work. The result does not show that all apparent LIO improvements are invalid, nor that deterministic execution guarantees greater accuracy.

Survey use: Section IX, timing/placement/comparisons and trial-unit interpretation, with M2UD (F11) and existing estimator comparisons. Repeated runs of one recording assess implementation variability; they are not independent physical missions. Record configurations, frame handling, numerical libraries and execution variability before interpreting a small single-run improvement.

## N12 — Real-time spatiotemporal tubes

Read: system and task assumptions on pp. 2–3; case studies and comparison protocol on p. 6; discussion and conclusion on pp. 7–8. Complete proofs and numerical result tables were not audited.

The controller adapts a spherical tube's center and radius from current obstacle information for a prescribed-time reach/avoid task. The considered pure-feedback system assumes locally Lipschitz dynamics, known sign-definite input coupling and bounded disturbances (p. 2). Assumption 3 requires separation between the unsafe set and tube center at the target time (p. 3); feasibility cannot be inferred solely from online obstacle sensing.

Case studies distinguish an omnidirectional mobile-robot hardware example from the quadrotor simulation (p. 6). Baseline comparisons and scalability experiments are separate randomized computational studies. The discussion says paths need not be shortest and identifies global planning as future work (p. 7). Explicit input constraints are also listed as future work (p. 8).

Survey use: Section V, safety filters/explicit risk conditions, and Section IX, guarantees/empirical rates. Compare with E25/E26/E55, retaining their different assumptions and guaranteed events. Transfer to nonholonomic or saturated wheeled systems requires a compatible model and feasible inputs; this source does not establish arbitrary-embodiment safety.

## N14 — Resilient memory-event-triggered MPC

Read: abstract and vehicle assumptions on pp. 1–2; event-update discussion/HIL setup on p. 7; platform and sampling configuration on p. 8; experimental discussion and conclusion on p. 9. Full proofs and numerical performance plots were not audited.

The controller uses historical triggering information and a maximum interval without an update to reduce repeated MPC solves while retaining the specified tracking properties. Its low-speed Ackermann model assumes no wheel slip and ignores height/tilt effects (p. 2). These conditions matter when comparing resilience to sensing, terrain or actuator degradation.

The validation is explicitly described as hardware-in-the-loop. An industrial Intel i7 computer hosts the control algorithms; Jetson Nano/STM32 components belong to the vehicle/low-level architecture (pp. 7–8). The HIL sampling period is one second (p. 8). Experimental differences with and without triggering are discussed on p. 9; an upper bound on silent events is interpreted as protection against event-generator faults/attacks, but the inspected protocol does not establish performance over a separately specified set of physical cyberattack trials.

Survey use: Section V, tracking/mission costs/network support, and Section VIII, resources. Compare with F02's observer/tolerant tracking architecture. Separate trigger frequency, actual computation time, control-loop age and bounded-silence protection. Do not attribute all control computation to the Jetson Nano or equate fewer solves with the same percentage of energy savings.

## N17 — Behavior-tree navigation and recovery on a wheeled-legged robot

Read: architecture/planner roles on pp. 2–3; recovery triggers/actions on pp. 4–5; simulation selection and real-robot protocol on pp. 5–7. Numerical result tables were not audited.

CENTAURO combines global/local elevation maps, hierarchical planning, a plan evaluator and behavior-tree supervision. Four failures trigger distinct actions: invalid wheel contact, local-plan failure, being stuck and stepping failure. Actions include stopping, moving wheel contacts, replanning, reversing the last action and reshaping the support polygon (pp. 4–5). Thus integrated monitoring and executed recovery already exist, with motion primitives tied to the hybrid embodiment.

The simulation study excludes infeasible obstacle arrangements and generated scenarios where the global planner fails or takes too long (pp. 5–6). Reported retained-scenario results therefore do not estimate success over all generated requests. Persistent local/global planning failures can still require human intervention (p. 5). Physical CENTAURO trials use slower motion and a lower local-map update rate than simulation (p. 7).

Survey use: Section VIII, diagnosis-to-response, alongside E59 and N10, plus Section IX's treatment of excluded/no-plan requests. Compare failure definitions, available trustworthy state, recovery actions and continuation of the original task. Wheel repositioning and stepping cannot be assumed available on a conventional differential-drive or Ackermann chassis.

## N20 — Dense multi-scan adjustment

Read: abstract/registration mechanism on p. 1; sensor-platform description on p. 2; benchmark/reference setup on p. 5; comparison configuration, speed and conclusion on p. 6. Full optimization derivations and numerical error-table cells were not audited.

DMSA models points from multiple scans jointly using grid-cell distributions, with iterative reduction of their scatter. It supports continuous-trajectory optimization with IMU data and keyframe optimization (p. 1). Its own Bicycle Street recording uses a sensor platform on a bicycle trailer (p. 2); other evaluated recordings include construction and campus environments.

Comparison sequences use aligned absolute pose errors, with dataset references for public sequences and GNSS/inertial reference for the authors' recording (p. 5). Baselines use default functional settings, with a preprocessing modification for LiLi-OM; failure to adapt its sensor setup is marked N/A, distinct from a run that starts and then fails (p. 6).

Reported processing time is 1.5–4 times sequence recording duration on an Intel i9-12900K, with numerical Jacobians identified as the bottleneck (p. 6). This implementation does not establish real-time closed-loop deployment. No individual error-table values are retained here.

Survey use: Section IV, dynamic geometry/persistent maps, and Section IX, timing and comparable inputs. Compare dense multi-scan estimation with feature selection and selective updates (E01/E08/E15). Distinguish estimation continuity, error, failure/N/A and compute budget; do not collapse them into a single real-time robustness ranking.
