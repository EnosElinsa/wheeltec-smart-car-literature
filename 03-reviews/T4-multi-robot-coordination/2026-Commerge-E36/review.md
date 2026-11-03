# Commerge: Communication-efficient, robust, and fast LiDAR map merging framework for multi-robot coordination in resource-constrained scenarios

## Metadata

| Field | Value |
|---|---|
| ID | E36 |
| Title | Commerge: Communication-efficient, robust, and fast LiDAR map merging framework for multi-robot coordination in resource-constrained scenarios |
| Authors | Hogyun Kim, Jiwon Choi, Juwon Kim, Geonmo Yang, Seokhwan Jeong, Hyungtae Lim, and Younggun Cho |
| Venue | The International Journal of Robotics Research, online first (vol. 0, no. 0, article 02783649261464202, 36 pages) |
| Year | 2026 |
| Type | journal |
| DOI | [10.1177/02783649261464202](https://doi.org/10.1177/02783649261464202) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649261464202 |
| Theme folder | T4-multi-robot-coordination |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-Commerge-E36/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-Commerge-E36/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2026-Commerge-E36/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: offboard-compute, few-trials
- platform_class: wheeled-unspecified
- platform: unnamed four-wheel robots (INHA-Indoor, INHA-Outdoor), custom rover (INHA-Cave), legged robot (INHA-Planetary); public HeLiPR, Kimera-Multi, WildPlaces, MCD, and Botanic Garden data
- boundary_platform: no
- degradation: scene-change, communication-delay-loss, bandwidth-limit, compute-limit
- degradation_observed: lidar-degeneracy, dynamic-objects, communication-partition
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: 3D LiDAR (spinning Ouster and Velodyne, non-repetitive Livox) with FAST-LIO2 LiDAR-inertial odometry; robots send SOLiD descriptors and keyframe poses
- compute: central server on Intel i7-12700KF (32 GB), IPC-6000 with i5-8265U (8 GB), or Jetson Nano (4 GB); 17.122 s communication time on Town 01-03 (IPC-6000)
- compute_location: desktop-offline
- summary_result: On HeLiPR Town pairs, Commerge exchanged 13.7 MB on average versus 14.8 GB for full-scan baselines and 43.3 MB for KISS-Matcher, with 5.619 m versus 6.412 m merging RMSE.
- summary_limitation: A central server is required; on large HeLiPR sequences real-time merging remains challenging on IPC-6000 and Jetson Nano, and decentralization is future work.
- survey_included: yes
- verification_level: full

## Problem

Multi-robot 3D LiDAR map merging needs inter-robot loop closures. Centralized
frameworks stream scans or descriptors from every robot to a server, and
distributed frameworks send whole data backlogs when robots meet, so traffic
grows with mission length and arrives in bursts (p. 2). Downsampling,
keyframing, and compression reduce data volume but do not decide which
inter-robot loops are worth sending (p. 2). The paper asks which keyframe scans
two robots must send to a server so that the server can still estimate their
relative transform, under limited bandwidth, packet loss, non-line-of-sight
(NLOS) links, and limited server memory and compute.

## Mechanism

Each robot runs LiDAR SLAM with a GTSAM pose graph (p. 15), FAST-LIO2 odometry
in the experiments (p. 23), and intra-robot loop closures found with the SOLiD
global descriptor and checked by point-to-point ICP (p. 8). During the mission
each robot sends only its SOLiD descriptors and keyframe poses to a central
server (p. 9). The server computes a dense descriptor-distance affinity matrix
between two robots by brute force, because Kd-tree retrieval would break the
diagonal patterns that sequential matching needs (p. 9). Loop selection then
runs as a three-stage cascade:

- Stage A, sequential matching: the affinity matrix is thresholded, connected
  clusters are labelled, and the cluster with the lowest mean distance among
  those whose span exceeds a minimum area is kept (pp. 9-10).
- Stage B, balanced vertex cover (BVC): on the bipartite exchange graph of the
  kept cluster, the server selects a minimum set of scans that covers every
  candidate loop. All scans get the same cost because CPU time and wireless
  bandwidth fluctuate, and entropy-derived minimum-share constraints prevent a
  "monologue" solution in which one robot sends almost everything. In the
  experiments the shares are p_alpha = p_beta = 1/2, and the authors state that
  the share is not an online estimate of link capacity (p. 11).
- Stage C, maximum edge-weighted clique: the remaining loops form a
  compatibility graph. Pairwise positional consistency compares translation
  distances only, because SOLiD is rotation invariant (p. 13), a threshold
  masks infeasible pairs, and edge weights combine positional consistency with
  SOLiD similarity (pp. 12-13).

The server sends an exchange policy back, each robot sends only the endpoint
scans of the selected loops, and the server builds one submap per robot and
aligns them once with KISS-Matcher (coarse) followed by small-GICP (fine)
(p. 14). The result is a single inter-robot transform per robot pair. BVC is
solved as a mixed-integer linear program and the clique as a mixed-integer
quadratic program with Gurobi; each returns the optimal solution if it
finishes within the solver time limit and a near-optimal solution otherwise
(p. 16). The time limit is not reported. The authors state that the cascade
does not form a single globally optimal end-to-end objective (p. 2). Table 1
lists a 1.0 m voxel size, 1.0 m keyframe spacing, an ICP fitness threshold of
0.3 m or 2.0 m depending on the scan pattern, a temporal window of 100
keyframes, SOLiD thresholds of 0.05/0.01 (intra-robot) and 0.10/0.05
(inter-robot), a minimum cluster area of 10,000, and a 5 m positional
consistency threshold (p. 16, Table 1).

## Baselines and controls

The map merging baselines are LT-Mapper, ELite, Uni-Mapper, and LAMM, which
transmit scan data at each communication step, and KISS-Matcher, which sends
voxelized map segments when robots are in proximity and assumes that
proximity can be detected through signal strength (p. 23). All methods use
FAST-LIO2 odometry with 1.0 m keyframe spacing and 1.0 m voxelization, and
descriptors come from single scans; KISS-Matcher additionally voxelizes its
accumulated map at 1.0 m before sending (p. 23). Table 4 groups the four
scan-streaming methods in one "Baselines" row. All five baselines are
centralized. Under NetEm emulation the comparator is the distributed
Multi-Proxy, because centralized systems often fail to provide fair
comparisons in real deployments due to system-level failures (p. 26). Stage A is compared with the SeqSLAM-based pipeline of AutoMerge on
HeLiPR (pp. 28-29). Ablations add stage B, stage C, or both to stage A on NTU
01-10 and Town 01-03 (p. 28, Table 8), replace SOLiD with Scan Context
(Fig. 30), and vary the mission stage (Table 9). Module checks compare SOLiD
with eight other place recognition descriptors (Table 10) and KISS-Matcher
with scan-level registration methods (Table 11). The paper does not say
whether the baselines were re-implemented or run from released code. Other
exchange-graph methods cited in Sec. 2.5 are not compared.

## Platform and setup

Public data (Sec. 6.3): HeLiPR Roundabout and Town (Ouster OS2-128, three
robots), Kimera-Multi Outdoor and Tunnel (five robots in the Fig. 20 example),
WildPlaces (sequences V02, V03, and V04 with gaps of 6 to 14 months), MCD NTU
(Livox Mid-70), and Botanic Garden (Livox Avia). The public sequences were
recorded one robot at a time and are time-shifted to a central sequence to
form synchronized multi-robot runs (p. 18). Botanic Garden lacks ground-truth
alignment between robots and is assessed qualitatively; WildPlaces and
Kimera-Multi Tunnel, where LiDAR odometry drifts, use ground-truth trajectories
with arbitrary rotations (p. 18), described for Tunnel as a deliberately
injected yaw bias (p. 21, Fig. 15).

In-house data (Fig. 8, p. 17): INHA-Cave (lava cave, custom rover),
INHA-Planetary (planetary-analog terrain, legged robot), INHA-Indoor
(corridor, wheeled robot), and INHA-Outdoor (nighttime campus with many
pedestrians, wheeled robot). The text names no robot model, drive type, or
in-house LiDAR. The Fig. 8 (c) and (d) photos show small wheeled robots, but
their drive type cannot be read from the images, so the platform class is
coded as wheeled-unspecified; the caption calls the cave robot only a custom
rover. Table 7 lists
three robots indoors and two outdoors (p. 27). Cave and Planetary data were
run under NetEm-emulated delay, bandwidth limits, and packet loss (p. 20).
Indoor and Outdoor data were sent over a real WLAN built from two TP-Link
Omada EAP245 access points, with ROS/ZeroMQ messaging and the IPC-6000 as
server (pp. 18, 21). Robot speeds, in-house run durations, and the number of
repetitions are not reported; each network condition appears once. Fig. 28
reports RMSE box plots with paired t-tests (p-value below 10^-4) across
pipeline configurations, but the paper does not say what the samples are
(p. 28).

## Evidence type and transfer

The strongest setting is the in-house data, recorded on the authors' robots,
sent over the real WLAN for Indoor and Outdoor. It is coded as recorded robot
data because Fig. 8 describes the deployments as dataset acquisition, Sec. 6.4
calls the runs datasets, the paper never states that the robots were driving
and running SLAM while they transmitted, and the same WLAN and IPC-6000 setup
also measured payload and communication time for the public datasets
(p. 17), which can only be replays. If the WLAN runs were live, they would be
online hardware evidence. In neither case does the merged map drive a robot,
so the paper shows no closed loop. The WLAN runs give qualitative merged maps
(Figs. 25 and 26) and delivery counts (Table 7), but no merging error. Merging
accuracy (Table 3) comes from public data on the Intel-i7, and payload and
communication time (Table 4) from public data streamed over the WLAN to the
IPC-6000 (p. 17).

Three distinctions matter for reuse. First, the payload metric d_exch sums
message payload bytes (p. 17); it is neither throughput nor link-layer
traffic, and protocol overhead and retransmissions are not counted. The
communication time t_comm runs from the first to the last transmission,
summed over robots (p. 16); Table 8 calls it computation time, and its
283,637.921 s entry shows that it includes the server's selection time before
scans are requested. Second, the Table 6 drop ratio is the share of
descriptors not delivered under a configured NetEm condition, and the Table 7
dropout ratio is the measured share of transmissions not received over the
real WLAN; neither is a configured packet-loss rate, and the 73.3% figure is
not a loss rate that was set. Third, the architecture is a central
map-merging server. NLOS disconnection reduces what reaches the server, but
the paper has no exploration, task allocation, or robot-to-robot merging
while robots are cut off from the server; a decentralized version is future
work (p. 32).

## Sensors

The method uses 3D LiDAR scans and the poses of LiDAR-inertial odometry
(FAST-LIO2 in all experiments, p. 23), so each robot needs a 3D LiDAR and an
IMU. The public data use the Ouster OS2-128 (HeLiPR), Velodyne VLP-16
(Kimera-Multi, per Fig. 21 on p. 24), Livox Mid-70 (MCD), and Livox Avia
(Botanic Garden); WildPlaces is used as submaps. The Fig. 13 caption names an
Ouster OS1-64 for Kimera-Multi Outdoor (p. 19), which conflicts with the VLP-16
named in Fig. 21 and Table 2. The in-house LiDARs are not named. Merging error
is computed against dataset ground-truth trajectories after Umeyama alignment
with the EVO toolkit (p. 16). No camera, GNSS, or wheel odometry is used.

## Compute and latency

Three server tiers were tested: an Intel Core i7-12700KF desktop with 32 GB
RAM, an IPC-6000 industrial mini PC with an Intel Core i5-8265U and 8 GB RAM,
and a Jetson Nano with a quad-core ARM Cortex-A57 and 4 GB RAM; each is
assumed to be the central server (p. 16). Merging error was evaluated on the
Intel-i7 and communication on the IPC-6000 (p. 17). Because the paper does
not state that any robot was live during these runs, the server computation
is coded as desktop-offline. The runtime breakdown is
given only as a figure: on NTU 01-10 the pipeline is real-time feasible on all
three tiers, while on Town 01-03 execution time rises sharply on weaker
hardware and real-time execution remains challenging on the IPC-6000 and the
Jetson Nano (p. 32, Fig. 32). Sequential matching dominates the computational
cost (p. 32). Stage A takes 1.070 s versus 1943.714 s for the AutoMerge
pipeline on HeLiPR (p. 29). Peak RAM is shown only in Figs. 21 and 22. The
paper reports no robot-side compute, descriptor generation time, solver time
limit, end-to-end latency from scan capture to merged map, or energy use.

## Key quantitative results

- Merging RMSE on the Intel-i7, averaged over robot pairs: 2.825 m on HeLiPR Roundabout versus 17.740 m for KISS-Matcher and 9.739 m for LT-Mapper, and 5.619 m on Town versus 6.412 m and 9.503 m; ELite, LAMM, and Uni-Mapper exhausted the 32 GB RAM on both (p. 19, Table 3).
- On Kimera-Multi Outdoor (partial overlap) the average RMSE is 15.640 m versus 22.926 m for KISS-Matcher; on MCD NTU it is 2.189 m, worse than KISS-Matcher at 1.248 m and better than LT-Mapper at 3.510 m (p. 19, Table 3).
- Cumulative message payload over the real WLAN with the IPC-6000 server: Town average 13.7 MB versus 43.3 MB for KISS-Matcher and 14.8 GB for the scan-streaming baselines; Roundabout 16.8 MB versus 72.4 MB and 14.7 GB; NTU 3.4 MB versus 6.5 MB and 292.2 MB (p. 23, Table 4).
- Communication time is 17.122 s on Town 01-03 versus 42.113 s for KISS-Matcher, and 4.042 s on average for NTU versus 9.682 s and 6.588 min; the scan-streaming baselines exceed 1 h (T/O) on every Roundabout and Town pair (p. 23, Table 4).
- In the illustrated HeLiPR selection, scan data per robot fall from approximately 7000 MB to 60.0 MB and 50.1 MB after sequential matching, 25.9 MB and 26.5 MB after the balanced vertex cover, and 1.3 MB per robot after clique selection, stated as a 99.98% reduction (p. 6, Fig. 2).
- A second illustrated selection goes from 100 MB to 200 MB per robot to 0.4 MB per robot, stated as a 99.6% reduction (p. 29, Fig. 29).
- In the Fig. 5 example, standard minimum vertex cover sends less in total than the balanced cover (2.2 + 47.9 = 50.1 MB versus 25.9 + 26.9 = 52.8 MB) but yields submaps with less overlap; the balanced value for robot beta is 26.9 MB here and 26.5 MB in Fig. 2 (p. 12, Fig. 5).
- On Town 01-02, Commerge ran without OOM on the Jetson Nano, IPC-6000, and Intel-i7; KISS-Matcher failed only on the Jetson Nano, LT-Mapper ran only on the Intel-i7, and ELite, Uni-Mapper, and LAMM failed on all three; the check marks are blank in the transcription and were read from the x marks and Sec. 7.4 (p. 24, Table 5).
- With five robots on Kimera-Multi Outdoor, the scan-streaming baselines accumulate approximately 800 MB, while Commerge sends 448-byte SOLiD descriptors per robot per keyframe plus four discrete scan transmissions (p. 24, Fig. 20).
- NetEm on INHA-Planetary: average descriptor size 448 B versus 1,585 B for Multi-Proxy; descriptor drop ratio 0 for both under 2 ms delay, ≤20 Mbit/s, and 10% packet loss; 0.31% versus 2.54% under 2,000 ms delay; 62.64% versus 92.52% under ≤2 Mbit/s; 75.91% versus 99.43% under a configured 50% packet loss (p. 26, Table 6).
- The mild delay condition is 2 ms in Table 6 and Sec. 8.1 but 10 ms in the Fig. 23 caption; Fig. 24 shows Commerge merged maps on the cave data under 2000 ms delay, a 2 Mbit/s limit, and 50% packet loss (p. 25, Fig. 23).
- Real WLAN: received over sent was 2326/3265, 1876/2050, and 1234/1346 indoors (dropout 28.8%, 8.5%, and 8.3%) and 2029/7204 and 1541/5773 outdoors (71.8% and 73.3%); the caption calls these descriptor dropouts while the rows count scans, and merging is reported as successful in both environments (p. 27, Table 7).
- Stage A versus AutoMerge on HeLiPR: exchange data 232.9 MB versus 934.1 MB, runtime 1.070 s versus 1943.714 s, and RMSE 2.988 m versus 5.727 m (p. 29, Fig. 27).
- Stage ablation on Town 01-03 (RMSE, t_comm, payload): stage A alone 2.988 m, 276.932 s, 232.9 MB; with BVC 3.464 m, 140.190 s, 117.9 MB; with the clique only 2.887 m, 283,637.921 s, 209.8 MB; full pipeline 3.005 m, 17.122 s, 14.4 MB (p. 28, Table 8).
- Stage ablation on NTU 01-10: stage A alone 1.826 m, 24.137 s, 20.3 MB; full pipeline 1.792 m, 4.637 s, 3.9 MB; the clique without BVC gives the same RMSE and payload but takes 131.141 s (p. 28, Table 8).
- The full-pipeline RMSE differs between tables without explanation: 3.005 m on Town 01-03 in Tables 8 and 9 but 8.580 m in Table 3, and 1.792 m on NTU 01-10 in Table 8 but 2.594 m in Table 3, while payload and communication time match Table 4 (p. 19, Table 3).
- Over mission stages on Town 01-03, RMSE is 3.867 m with 11.4 MB at the first quarter (10 min) without intra-robot loops, 3.653 m with 21.7 MB at one third (15 min), and 3.005 m with 14.4 MB when both missions are complete (p. 29, Table 9).
- Place recognition: SOLiD (448 B) reaches Recall@1 0.587, AUC 0.587, and F1 max 0.608 on NTU 01-02, where RING++ (345,728 B) has the higher Recall@1 of 0.787; on NTU 01-10 SOLiD (0.351, 0.740, 0.689) is below RING++ (0.471, 0.801, 0.712) on all three metrics (p. 31, Table 10).
- Scan-level registration on Kimera-Multi Tunnel: KISS-Matcher with PLANE-ICP has the highest success rate on three of four sequences, for example 89.056% on A01-A02 versus 47.590% for KISS-Matcher alone (p. 31, Table 11).

## Stated limitations

- Execution time on resource-constrained systems remains a practical limitation for large-scale scenarios; sequential matching dominates the computational cost and is the target of future optimization (p. 32).
- The framework relies on a central server; a fully decentralized system for communication-restricted environments is future work (p. 32). For centralized frameworks in general, the authors name the single server as a bottleneck and potential single point of failure (p. 5).
- Transmission costs cannot be assigned reliably because CPU time and wireless bandwidth fluctuate, so every scan gets the same weight and the vertex count is used as a proxy for communication cost (p. 11).
- The experiments use the two-robot equal-share balance; extension to larger teams and asymmetric participation rests on the entropy formulation only (p. 11).
- Public data with truly simultaneous multi-robot acquisition are scarce, so single-robot sequences are time-shifted; quantitative evaluation is limited for Botanic Garden, WildPlaces, and Kimera-Multi Tunnel (p. 18).
- The cave and planetary environments did not permit a real wireless infrastructure, so network degradation there was emulated (p. 20).
- BVC and clique selection are NP-hard and may return near-optimal solutions at the solver time limit (p. 16), and the cascade is not a single globally optimal objective (p. 2).

## Transfer conditions

The method needs a 3D LiDAR and LiDAR-inertial odometry on every robot, since
SOLiD descriptors, ICP verification, and KISS-Matcher registration all work on
3D point clouds; a robot with only a 2D scanner cannot reuse it as published.
A server must be reachable over a shared network and run Gurobi, a commercial
solver whose licensing the paper does not discuss. The tested team merges are
pairwise with equal shares. The thresholds in Table 1 (1.0 m keyframes and
voxels, a minimum cluster area of 10,000, a 5 m consistency threshold, and an
ICP threshold that depends on the scan pattern) were set for campus- and
city-scale runs; short indoor trajectories of a small robot may not form a
cluster above the minimum area, which the paper does not test. The output is
one rigid transform per robot pair from a one-shot submap registration; the
paper does not describe sending the merged map back to robots or using it for
navigation. Real-time operation on a Jetson-class server holds for the
small-scale NTU run, not for city-scale HeLiPR runs. The WLAN results come
from one indoor and one outdoor run with two access points; dropout depends
on the building layout and server position.

## Code and data

The paper mentions an open-source release with further implementation details
but gives no repository URL (p. 16). The author note points to supplementary
materials at https://sparolab.github.io/research/commerge (p. 33). Release of
the INHA in-house datasets is not stated. The project page, code, and data
were not verified.

## Version family

The paper builds on the authors' earlier "Kim et al., 2025" work on fast
descriptor exchange and robust registration (p. 3). The reference list has
two Kim et al. (2025) entries, SKiD-SLAM (arXiv:2505.08230) and the DiTer++
dataset paper (p. 34); the description matches SKiD-SLAM, but the in-text
citation does not disambiguate. SOLiD (Kim et al., 2024) and KISS-Matcher
(Lim et al., 2024) are earlier component papers of the same groups. None of
these is in the library. The library counts this IJRR article once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | weak | Sec. 6.3, p. 18 | "present geometrically degenerate environments where LiDAR odometry exhibits substantial drift, preventing reliable assessment" |
| C3 | unset | n/a | | |
| C4 | direct-support | strong | Sec. 1, p. 2 | "the server must exchange and process massive amounts of global descriptors or sensor data, which quickly exhausts bandwidth and drains battery power" |
| C5 | partial-support | weak | Sec. 2.3, p. 5 | "reliance on a single server introduces bottlenecks and potential single points of failure, limiting scalability in real-world deployments where stable network links are rarely guaranteed" |
| C6 | qualifies | moderate | Sec. 10, p. 32 | "indicating that real-time execution remains challenging on IPC-6000 and Jet-Nano platforms" |

## Page-cited excerpts

- **p. 2, Sec. 1.** "the server must exchange and process massive amounts of global descriptors or sensor data, which quickly exhausts bandwidth and drains battery power"
  The communication and resource constraint is the paper's premise; battery drain is asserted, not measured.
- **p. 3, Sec. 1.** "the overall volume of exchanged descriptors and scans is effectively the same as in centralized systems that ship all data"
  The authors' earlier work sped up merging but did not reduce traffic, which motivates the selection cascade.
- **p. 5, Sec. 2.3.** "reliance on a single server introduces bottlenecks and potential single points of failure, limiting scalability in real-world deployments where stable network links are rarely guaranteed"
  Commerge keeps a central server, so this risk applies to it; server failure is not tested.
- **p. 6, Fig. 2.** "reduces the exchanged data to just 1.3 MB per robot"
  The 1.3 MB figure is the scan data of one illustrated selection, not the cumulative payload of a mission; the caption does not say whether descriptor traffic is included.
- **p. 11, Sec. 4.4.** "making the vertex count a robust proxy for communication cost"
  Scans have uniform cost, so the cover minimizes scan count, not bytes or link time.
- **p. 11, Sec. 4.4.** "Since our objective is scan cardinality rather than bandwidth"
  The balance shares are fixed design values, not adapted to measured link quality.
- **p. 12, Fig. 5.** "it produces submaps with reduced overlap despite being taken from the same location, increasing the likelihood of failure in the submap merging stage"
  Balancing can cost slightly more data than a plain minimum vertex cover; the gain is overlap for registration.
- **p. 16, Sec. 6.1.** "Note that we assume each platform serves as the central server"
  All three hardware tiers are server hardware; no tier is evaluated as robot-side compute.
- **p. 17, Sec. 6.2.** "which measures the cumulative payload size of all transmitted messages"
  d_exch is a byte count of message payloads, not throughput and not link-layer traffic.
- **p. 18, Sec. 6.3.** "all robot sequences are time-shifted to align with a designated central sequence, creating synchronized multi-robot trajectories"
  The public-data results are replays of single-robot recordings, not simultaneous team runs.
- **p. 20, Sec. 6.4.** "do not permit real wireless infrastructure due to the harshness of the environments, so we emulate delay, bandwidth limitation, and packet loss using NetEm"
  The cave and planetary network results are emulated on recorded data.
- **p. 23, Sec. 7.** "KISS-Matcher assumes robots can detect proximity through signal strength indicators"
  The strongest baseline sends map segments at encounters, so its traffic pattern differs from the scan-streaming baselines.
- **p. 26, Table 6.** "Drop ratio is defined as the percentage of descriptors that fail to be successfully delivered."
  The drop ratio is an outcome measured under a configured NetEm setting; 75.91% under 50% configured loss is not the configured loss.
- **p. 27, Table 7.** "Descriptor dropout statistics under real communication conditions on the INHA dataset."
  The caption speaks of descriptors while the rows count scans; the 73.3% value is one robot in one outdoor run.
- **p. 27, Sec. 8.2.** "our Commerge still achieves successful map merging in both environments"
  Success on the real WLAN is shown by merged-map figures, without an error metric or repeated runs.
- **p. 32, Sec. 10.** "indicating that real-time execution remains challenging on IPC-6000 and Jet-Nano platforms"
  Running on the Jetson Nano shows memory feasibility, not real-time operation at city scale.
- **p. 32, Sec. 11.** "In addition, we plan to extend Commerge toward a fully decentralized system that removes the reliance on a central server in communication-restricted environments."
  Operation without a reachable server is future work.

## Survey-usable statements

### Supported

- A server-side cascade of sequential matching, balanced vertex cover, and edge-weighted clique selection on descriptors and poses lets robots send only scans incident to selected loops; on HeLiPR Town pairs the cumulative payload was 13.7 MB versus 43.3 MB for KISS-Matcher and 14.8 GB for full-scan streaming, with 5.619 m versus 6.412 m merging RMSE.
- Commerge ran on a 4 GB Jetson Nano server for Town 01-02, where all compared methods ran out of memory; real-time operation on such hardware holds only for small-scale runs.
- With 448 B descriptors, Commerge lost fewer descriptors than Multi-Proxy (1,585 B) under NetEm, for example 75.91% versus 99.43% under a configured 50% packet loss on INHA-Planetary, and still produced merged maps.
- Over a real WLAN with NLOS links, merged maps were reported for indoor and outdoor runs in which up to 73.3% of one robot's transmissions did not reach the server.
- Balancing scan selection across two robots can cost more data than a plain minimum vertex cover (52.8 MB versus 50.1 MB in one example) in exchange for overlap that registration needs.

### Not supported

- Commerge cuts whole-mission communication 5000-fold in general: that figure comes from one illustrated selection (7000 MB to 1.3 MB per robot), and the Table 4 mission payload ratios are smaller.
- The payload numbers are bandwidth or throughput: d_exch counts message payload bytes, and t_comm is elapsed time from first to last transmission that includes server selection time.
- Commerge tolerates 73.3% configured packet loss: 73.3% is a measured non-delivery ratio in one real outdoor run; the largest configured NetEm loss is 50%.
- Robots keep exploring or merging maps while partitioned from the server: the architecture is centralized, and decentralization is future work.
- Commerge has the lowest merging error on every dataset: on MCD NTU it is worse than KISS-Matcher, and its Town and NTU errors differ between Table 3 and Table 8.
- The balanced cover adapts to link bandwidth: the shares are fixed at one half for two robots and are not link-capacity estimates.
- The method has been shown on a closed-loop multi-robot mission: the merged map does not drive the robots, and the paper does not state that the WLAN runs were live.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read (Secs. 1-11, author note, and the Kim et al. 2025 reference entries); raw PDF text of pp. 2, 3, 17, 19, 24, 26-29 checked, including Table 7 and the captions of Figs. 2, 5, 8, 13, 20, 21, 23, 24, 26, 29; Tables 1-6 and 8-11 have no PDF text layer, so their values were read from the transcription (Table 2 and Fig. 8 from the transcription image) and cross-checked with the body text | corrections: rebuilt in English in template format; evidence coded as recorded robot data instead of a real wireless closed loop; GPU-training statement removed; Fig. 2 descriptor-exclusion claim reworded; cave platform wording corrected; Kim et al. (2025) attribution qualified; Table 3 versus Table 8 RMSE discrepancy and other internal inconsistencies added; after the independent fact-check, the AutoMerge comparison order was fixed, platform recoded as wheeled-unspecified from the Fig. 8 photos, compute location set to desktop-offline, and degradation split into designed and observed conditions (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/38792d787ac192a8487d6295/

## Original abstract

By maintaining global consistency across robot teams, multi-robot light detection and ranging (LiDAR) map merging enables faster exploration and efficient area coverage. However, map merging requires exchanging massive sensor data between the server and robots, making communication the bottleneck, especially in communication-constrained environments. Therefore, we present Commerge, a communication-efficient map merging framework that achieves bandwidth reduction through graph-theoretic selective data exchange. By doing so, our Commerge reduces inter-robot communication by up to 5000× while maintaining alignment accuracy. Our key insight is that only a small subset of carefully selected scans is sufficient for robust map merging. We formulate this as a three-stage cascaded optimization problem on an exchange graph, where vertices represent robot keyframes and edges denote candidate inter-robot loops. Through three cascade stages, we select a sequentially overlapped, balanced-transmission-cost, and geometrically-perceptually optimal scan subset that preserves alignment quality while reducing communication. Unlike existing approaches that either transmit whole scans, which require GB-scale data exchange, or employ naïve downsampling, our approach exchanges only MB-scale data while achieving comparable alignment accuracy. Extensive evaluation on five public datasets and four in-house datasets covering cave, planetary-analog, indoor, and outdoor campus environments shows up to 99.98% reduction in data exchange (e.g., from 7000 MB to 1.3 MB on the HeLiPR dataset), while maintaining alignment performance across embedded to desktop platforms. Furthermore, we demonstrate that our proposed framework operates on resource-constrained hardware where existing methods fail, enabling real-world multi-robot deployment in bandwidth-limited field operations. Finally, we validate system robustness under a real-world non-line-of-sight (NLOS) communication environment with up to 73.3% dropout rate, as well as under emulated network degradation scenarios including delay, bandwidth limitation, and packet loss, confirming reliable map merging even under severely degraded connectivity.
