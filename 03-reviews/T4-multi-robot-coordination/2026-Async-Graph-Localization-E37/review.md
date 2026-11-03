# Parallel Graph Inference for Decentralized and Asynchronous Multi-Robot Cooperative Localization Under Limited Connectivity
## Metadata
| Field | Value |
|---|---|
| ID | E37 |
| Title | Parallel Graph Inference for Decentralized and Asynchronous Multi-Robot Cooperative Localization Under Limited Connectivity |
| Authors | Qirong Tang, Haoyu Liu, Min Yu, and Yuanxiang Wang |
| Venue | IEEE Robotics and Automation Letters, vol. 11, pp. 12120-12127 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3729488](https://doi.org/10.1109/lra.2026.3729488) |
| Official URL | https://ieeexplore.ieee.org/document/11673300/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Async-Graph-Localization-E37/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Async-Graph-Localization-E37/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2026-Async-Graph-Localization-E37/citation.bib) |
## Survey coding
- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: dataset-playback
- evidence_all: dataset-playback, simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: five ground robots of the public UTIAS dataset (three beacons, two clients); simulated underwater robots in Webots
- boundary_platform: no
- degradation: communication-delay-loss
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: UTIAS: odometry (forward speed, yaw rate) and camera range and bearing; simulation: IMU, compass, depth, forward-looking sonar, USBL on 10% of robots
- compute: i7-10750H offline; one-step inference 11.5 ms (simulation) and 6.9 ms (UTIAS)
- compute_location: desktop-offline
- summary_result: One-step inference takes 11.5 ms (simulation) and 6.9 ms (UTIAS) versus 81.1 and 46.9 ms for windowed GBP with window 10, on an i7-10750H offline.
- summary_limitation: The authors note that outdated mutual measurements contribute negligibly at long delays; at 8 s delay, accuracy approaches dead reckoning.
- survey_included: yes
- verification_level: light
## Problem
Under limited connectivity, relative measurements between robots arrive late and out of order. Single-step filters struggle to align this historical information, and large-window optimization can block control-rate state feedback.
## Mechanism
Each robot keeps a sparse local factor graph. A main thread performs real-time one-step inference, while a communication thread inserts historical relative measurements and neighbor priors and runs Gaussian belief propagation (GBP). When it finishes, a callback propagates the historical correction to the latest state. Non-keyframes are discarded, but their one-step posteriors with the fused relative-to-reference information accumulate into a composite odometry. Messages on the composite manifold SO(3) x R6 are transformed to a common tangent space before fusion.
## Baselines and controls
- Dead reckoning (no inter-robot relative measurements).
- F-ESKF (later called F-CI in the paper; the naming is inconsistent).
- F-DMV (discorrelated minimum variance).
- F-DCU (decentralized covariance union).
- O-WGBP (Robot Web windowed GBP with windows 5 and 10, enlarged adaptively under long delays).
- Centralized Gauss-Newton (CGN) and decentralized batch Gauss-Newton (DGN) for approximation-error comparisons.
## Platform and setup
- Webots underwater-robot simulation with 12, 25, 50, and 100 robots, 100 s each; 10% of the robots have 2 Hz USBL absolute positions, and the others rely on cooperation.
- Playback of nine sequences of the public UTIAS dataset with five ground robots: three beacons observe known landmarks and two clients do not. The authors recorded no new hardware data and ran no online navigation.
- Approximation-error analysis: 12 robots, 20 s, five delay levels, 10 random initial states per condition.
- Each robot exchanges with only one peer at a time; f_d = 1/T_d measures the frequency and delay of exchanging one pair of relative measurements. The UTIAS example uses T_d = 3.2 s, and the underwater simulation goes up to 8 s.
## Evidence type and transfer
Derivation of Gaussian GBP on manifolds, underwater acoustic-network simulation, playback of a public ground-robot dataset, and offline timing and empirical convergence and error analysis. Acoustic communication is simulated and UTIAS is playback, so real network dropouts, thread congestion, long-term memory growth, and onboard resources are not validated.
## Sensors
Simulation: IMU, compass, and depth at 100 Hz, forward-looking sonar at 10 Hz, simulated acoustic modem delay, USBL global position at 2 Hz on 10% of the robots, and fairly accurate initial-state priors for all robots. UTIAS: odometry from forward speed and yaw rate, and camera-based relative range and bearing; the three beacons observe known landmarks. No real underwater sensor hardware is reported.
## Compute and latency
Offline on an i7-10750H at 2.6 GHz over 2000 one-step inferences: O-PGI 11.5 ms (simulation) and 6.9 ms (UTIAS); O-WGBP with window 5 takes 38.4 and 21.9 ms and with window 10 81.1 and 46.9 ms; the filters take about 0.5 ms (p. 7). The metric is one-step inference; background historical inference, total CPU, memory, and network bytes per second are not fully reported.
## Key quantitative results
- One-step inference: O-PGI 11.5/6.9 ms versus O-WGBP (window 10) 81.1/46.9 ms, about 7.1 and 6.8 times faster; this is the single-step latency of the parallel architecture, not a total compute reduction (p. 7).
- Approximation error against CGN, 12 robots, 20 s, 10 runs, 5 delays: DGN 0.146 m, O-WGBP 0.116 m, O-PGI 0.171 m; O-PGI is slightly less accurate than windowed GBP, which the authors attribute to callback delay (p. 8).
- At T_d = 8 s, O-PGI and O-WGBP accuracy approaches pure dead reckoning (p. 6).
- In the UTIAS example with three beacons, two clients, and 3.2 s delay, delayed corrections still improve the clients (p. 7).
- Scaling to 100 robots is supported mainly by the error curves of Fig. 6; no 100-robot hardware or full-stack measurement is given.
## Stated limitations
- At long delays, outdated mutual measurements make a negligible contribution to real-time cooperative localization (p. 6).
## Transfer conditions
Legacy reviewer observations:
- Continuous real-time state output differs from timely historical correction: background updates have visible delay, so fusing arbitrarily old measurements is not free.
- Known absolute references or landmarks and fairly accurate initial priors support observability; fully anchorless teams with severe drift are not tested.
- GBP convergence and "global optimality" are shown only by limited simulation comparisons, without a general nonlinear GBP convergence result or a Gauss-Newton global-optimality certificate.
- The method relies on late data eventually being exchanged with timestamped neighbor priors and measurements; permanent partitions, retransmission protocols, and global consistency after disconnection are not addressed.
## Code and data
The public UTIAS dataset [20] is the benchmark source. The legacy extraction found no author code repository or new data URL in the paper; the implementation was not run.
## Version family
RA-L 2026, DOI 10.1109/LRA.2026.3729488. It builds on Robot Web, GBP, and composite-manifold modeling, and the paper does not state that it extends an earlier conference paper. Counted as one work.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | direct-support | moderate | Sec. VI-B, p. 6 | "outdated mutual measurements make a negligible contribution to real-time cooperative localization." |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI-D, p. 7 | "One-step inference time is evaluated offline on an i7-10750H" |
## Page-cited excerpts
- **p. 7, Sec. VI-D Scalability and Computational Analysis.** "One-step inference time is evaluated offline on an i7-10750H"
  Timing is offline on a laptop CPU, not onboard and not including network delay.
- **p. 7, Sec. VI-D Scalability and Computational Analysis.** "11.5 ms (6.9 ms) in simulation (UTIAS dataset)."
  Mean one-step inference; excludes background historical inference; filters take about 0.5 ms.
- **p. 6, Sec. VI-B Simulation Study.** "outdated mutual measurements make a negligible contribution to real-time cooperative localization."
  At T_d = 8 s, old relative measurements add little; asynchronous fusion does not keep a benefit under extreme delay.
- **p. 8, Sec. VI-E Convergence and Approximation Error Analysis.** "0.146 m, 0.116 m, and 0.171 m, respectively, representing approximation errors."
  DGN, O-WGBP, and O-PGI deviations from CGN in a limited 20 s simulation; not a general error bound.
- **p. 7, Sec. VI-C Experiment on the UTIAS Dataset.** "three beacon robots obtain landmark measurements and achieve high accuracy"
  UTIAS accuracy depends on three landmark-observing beacons helping two clients.
## Survey-usable statements
### Supported
- Decoupling real-time one-step inference from background GBP fusion of delayed relative measurements keeps one-step latency at 11.5 ms (simulation) and 6.9 ms (UTIAS) on an i7-10750H, versus 81.1 and 46.9 ms for windowed GBP.
- Delayed relative measurements still improve client robots in UTIAS playback at 3.2 s delay when beacons observe landmarks.
### Not supported
- The method keeps a cooperative benefit at any delay: at 8 s, accuracy approaches dead reckoning.
- The method is the most accurate approximation of the centralized solution: its deviation (0.171 m) exceeds O-WGBP (0.116 m) and DGN (0.146 m).
- The method is validated onboard under real network dropouts: acoustic links are simulated and UTIAS is replayed offline.
## Verification log
- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; legacy quote with the fl ligature in "offline" normalized to "offline" as found in the text; no legacy quote dropped
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/d9dfc3bf6871f0e81d1141fc/
## Original abstract
Limited connectivity poses a critical challenge for multi-robot cooperative localization, as delayed or out-of-order measurements often cause conventional algorithms to misalign and diverge. Existing methods typically struggle to balance real-time constraints with the computational cost of retrospectively fusing latent data. To address this, a parallel graph inference framework is proposed for decentralized and asynchronous cooperative localization. Each robot constructs a local sparse factor graph to uniformly represent state variables and measurements. Crucially, a multi-thread architecture is introduced to decouple high-frequency real-time estimation from the latency-prone fusion of inter-robot measurements. This allows the system to maintain control-rate state feedback while asynchronously integrating historical relative measurements via Gaussian belief propagation. Extensive evaluations on simulated and real-world datasets validate the system across varying sensor configurations, scales, and connectivity conditions. The results demonstrate that the proposed method remains robust under significant communication delays, achieving the accuracy of optimization-based approaches with the runtime efficiency of filter-based methods.
