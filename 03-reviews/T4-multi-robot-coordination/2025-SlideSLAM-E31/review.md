# SlideSLAM: Sparse, Lightweight, Decentralized Metric-Semantic SLAM for Multirobot Navigation

## Metadata

| Field | Value |
|---|---|
| ID | E31 |
| Title | SlideSLAM: Sparse, Lightweight, Decentralized Metric-Semantic SLAM for Multirobot Navigation |
| Authors | Xu Liu, Jiuzhou Lei, Ankit Prabhu, Yuezhan Tao, Igor Spasojevic, Pratik Chaudhari, Nikolay Atanasov, and Vijay Kumar |
| Venue | IEEE Transactions on Robotics, vol. 41, pp. 6529-6548 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tro.2025.3629786](https://doi.org/10.1109/tro.2025.3629786) |
| Official URL | https://ieeexplore.ieee.org/document/11230622/ |
| Theme folder | T4-multi-robot-coordination |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T4-multi-robot-coordination/2025-SlideSLAM-E31/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2025-SlideSLAM-E31/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T4-multi-robot-coordination/2025-SlideSLAM-E31/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, recorded-robot-data, dataset-playback
- protocol_caveats: joystick-driving, pushed-capture, offboard-compute, few-trials
- platform_class: wheeled-unspecified
- platform: three Scarab UGVs (closed-loop runs); Falcon 250 UAV and Falcon 4 UAV (recorded, hand-carried or manually piloted runs); SemanticKITTI
- boundary_platform: no
- degradation: communication-partition
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual
- sensors: RGB-D camera (RealSense D435i or D455) with YOLOv8 or YOLO-World, or 3D LiDAR (Ouster OS1-64) with RangeNet++; VIO or LIO relative odometry; IMU roll and pitch
- compute: onboard Intel i7-10710U (Falcon UAVs) and i7-8700K (Scarab); replay on a laptop i7-10750H without GPU, graph optimization 2.4-4.0 ms indoor and 36.46 ms forest
- compute_location: mixed
- summary_result: SlideMatch versus SlideGraph mean inter-robot position error: 0.28 versus 0.75 m for three indoor Scarab pairs, 0.13 versus 0.24 m for six replayed LiDAR UAV pairs.
- summary_limitation: Objects are modeled by three primitive shapes; one-shot inlier-threshold loop closure can fail in repetitive layouts, and dynamic objects are not modeled and can cause faulty loop closures.
- survey_included: yes
- verification_level: full

## Problem

A heterogeneous team of aerial and ground robots must build a shared
object-level metric-semantic map without infrastructure, while communicating
only opportunistically and running on size-, weight-, and power-constrained
onboard computers. Dense geometric maps are too heavy to store and share, and
existing metric-semantic SLAM is mostly single-robot (pp. 1-2). The paper asks
how to recognize places, merge maps across robots and sensing modalities
(LiDAR and RGB-D), and keep the whole loop real time onboard.

## Mechanism

The front end extracts object instances with RangeNet++ on LiDAR range images
or with YOLOv8 (closed set) or YOLO-World (text prompts) on RGB images
back-projected with depth, tracks them with the Hungarian algorithm, and fits
one of three shapes: cuboids (vehicles), cylinders (tree trunks and light
poles), or simplified ellipsoids with two shape parameters and identity
orientation (pp. 6-8). The back end is a GTSAM factor graph with custom
cuboid and cylinder factors, range-bearing factors for ellipsoids, and
relative-pose odometry factors from VIO or LIO between key poses (pp. 8-9).

Two place-recognition algorithms find inter-robot loop closures from the
object maps. SlideMatch is an anytime exhaustive search over discretized X, Y,
and yaw after zero-centering both maps; SlideGraph matches Delaunay simplices
by sorted vertex-to-centroid distances and class labels and passes the
candidates to CLIPPER for outlier rejection (p. 9). A least-squares fit then
estimates X, Y, Z, and yaw only, because roll and pitch are taken from the IMU
(p. 9).

Communication is modeled as a time-varying undirected graph (p. 4). When a
link exists, each robot sends its object detections per key pose, the
relative odometry between key poses, and its object map; received messages
are buffered until a loop closure gives the frame transform, after which the
other robot's poses and objects are added to the host robot's own factor
graph (p. 10). Robots therefore share raw sparse observations, not
marginalized factor graphs. Each robot shares its whole database at every
exchange; a bookmarking scheme that sends only new information is suggested
but not implemented (p. 15). Loop closure runs on a separate CPU thread
(p. 15).

## Baselines and controls

Inside the system, SlideMatch and SlideGraph are compared on the same object
maps (Table IV). For loop closure alone, SlideGraph is benchmarked against
LCDNet with KITTI-pretrained weights on an RTX 3070 desktop and against the
original CLIPPER on CPU, on SemanticKITTI sequences 05 and 07 and on the
authors' forest data (p. 17, Table VII). On SemanticKITTI, trajectory error is
compared with SuMa++, which also supplies the initial poses (pp. 16-17). The
authors state that benchmarking the entire system against other
metric-semantic SLAM systems is hard, so they benchmark modules only (p. 16).
No baseline is run in the closed-loop exploration experiments.

## Platform and setup

- Robots (p. 11, Table III): Falcon 4 UAV (Ouster OS1-64, VectorNav VN-100
  IMU, i7-10710U, 3-10 m/s), Falcon 250 UAV (RealSense D435i, VOXL VIO,
  i7-10710U, 2-5 m/s), and Scarab UGV (RealSense D455, 2D Hokuyo LiDAR for
  odometry and obstacle avoidance, i7-8700K, 0.5 m/s). The Scarab is
  described only as "a ground wheeled robot" (p. 11); no drive type is given,
  hence wheeled-unspecified.
- Experiment 1.a, recorded data: the Falcon 4 was manually piloted over three
  parking lots and the Falcon 250 hand-carried through four runs in two
  buildings; the data were replayed on a base station (i7-10750H) with one ROS
  node per robot and communication enabled at predetermined intervals, and
  unknown initial poses were created by starting the streams at different
  timestamps (p. 11).
- Experiment 1.b: a hand-carried Falcon 4 and an autonomously navigating
  Scarab mapped the same floor (p. 11). The overview calls the Falcon 4
  "manual piloting" and the Falcon 250 "hand-carrying", while 1.b calls the
  Falcon 4 hand-carried (p. 11); this is the paper's own inconsistency.
- Experiment 2, closed-loop hardware: (2.a) a Falcon 250 and a Scarab explored
  autonomously and merged maps at a base station after the mission; (2.b)
  three Scarabs explored one floor autonomously and shared information over
  Wi-Fi (pp. 11-12). The active SLAM uses the metric-semantic map in real time
  (p. 11). Each setup is one reported run.
- Experiment 3: three Falcon 4 forest flights, manually piloted from the same
  start, replayed from different timestamps to mimic three robots; about 1 km
  per trajectory and 860 mapped trees (pp. 12-13, Fig. 7).
- Experiment 4: SemanticKITTI sequences 05 and 07, each split into three
  overlapping frame intervals, one per virtual robot (p. 16).

## Evidence type and transfer

Only Experiment 2 is closed-loop hardware: SLAM, exploration, planning, and
control ran onboard (p. 11), and the three-Scarab map in Fig. 8 was built in
real time (p. 13). Its quantitative output is the indoor rows of Table IV;
the paper does not say whether both place-recognition algorithms ran live
during that run or were evaluated afterward. Most other tabulated numbers
(outdoor rows of Table IV, Tables V and VI) come from recorded data of
manually piloted or hand-carried robots, replayed on a laptop. Table VII uses
SemanticKITTI with ground-truth segmentation plus the forest data. The paper
does not describe how the ground-truth relative transforms of Table IV were
obtained, except that the forest flights shared a start for ground truthing
(p. 12). No exploration outcome (coverage, time, success) is reported.

Intermittent communication was replicated, not measured on a real network:
every robot published to every other robot every 10 s, all replayed nodes were
within range on one laptop, and no packet loss, delay, or link outage was
injected or measured (p. 15). Table VI therefore reports message size, not
throughput, and its similarity across robots is an artifact of this setup,
as the authors state (p. 15).

## Sensors

Each robot uses either an RGB-D camera or a 3D LiDAR for objects, plus VIO
(VOXL on the Falcon 250) or LIO for relative motion, and the IMU for roll and
pitch. The Scarab also uses a 2D Hokuyo LiDAR for low-level odometry and
obstacle avoidance (p. 11). Object ground truth for Table V came from
surveying the sites and marking object positions by hand (p. 14).

## Compute and latency

- Onboard: i7-10710U on both Falcon UAVs and i7-8700K on the Scarab (p. 11,
  Table III); no onboard timing is reported.
- Laptop replay, Intel i7-10750H without GPU, described as comparable to the
  onboard CPUs (p. 15): RangeNet++ with darknet-13 runs at 1.5 Hz on one
  thread; YOLOv8m runs at 1 Hz per thread and 3 Hz with 4 of 12 threads
  (p. 15).
- Factor adding and graph optimization per robot (p. 15, Table VI): 2.429,
  4.008, and 2.372 ms indoor (68 objects); 9.351, 7.763, and 13.296 ms urban
  (249 objects; 10.14 ms mean); 28.702, 28.638, and 52.046 ms forest (860
  objects; 36.46 ms mean).
- Inter-robot loop closure, SlideGraph versus SlideMatch (p. 15, Table VI):
  22, 24, and 28 ms versus 3638, 1614, and 2252 ms indoor; 95, 86, and 91 ms
  versus 131, 123, and 168 ms urban; 209, 406, and 375 ms versus 1124, 2091,
  and 1836 ms forest. It runs on a separate thread and is not counted in the
  real-time loop.

## Key quantitative results

- Inter-robot localization, six outdoor LiDAR pairs (replayed Falcon 4 data): SlideMatch versus SlideGraph mean position error 0.13 m versus 0.24 m (standard deviations 0.07 m and 0.28 m) and mean yaw error 0.68° versus -0.57° (pp. 12-13, Table IV). Per pair, SlideGraph is better on two of the six (urban #0-#1 0.074 m versus SlideMatch 0.235 m; forest #1-#2 0.049 versus 0.159 m) and much worse on urban #0-#2 (0.848 versus 0.135 m) (p. 13, Table IV).
- Three indoor Scarab pairs (closed-loop exploration): SlideMatch versus SlideGraph mean position error 0.28 m versus 0.75 m, yaw 0.10° versus -2.77° (p. 13); per pair 0.221, 0.165, and 0.460 m versus 0.952, 0.253, and 1.040 m (p. 13, Table IV).
- Aerial-ground RGB-D (Falcon 250 and Scarab, starts up to 6 m and 90° apart): SlideMatch 0.245 m position error; SlideGraph failed (pp. 13-14, Table IV). The yaw error is -2.4° in Table IV but 2.35° in the text (p. 13).
- Cross-modality LiDAR-RGB-D (Experiment 1.b, frames offset 2.51 m, -5.37 m, and 90°): SlideMatch versus SlideGraph 0.542 m versus 0.578 m and -4.0° versus 2.0° (p. 14, Table IV).
- Object mapping with darknet-13: cars precision 0.967, recall 0.881, F1 0.922 over 135 surveyed cars in three lots; tree trunks precision 0.946, recall 0.909, F1 0.927 over 77 surveyed trees (p. 14, Table V).
- Average message size per robot under the 10 s publishing schedule: 0.304 to 0.309 MB indoor, 0.453 to 0.466 MB urban, and 1.702 to 1.742 MB forest; maximal (last) message 0.575 to 0.578, 0.725 to 0.727, and 2.686 to 2.687 MB (p. 15, Table VI). These are message sizes, not data rates.
- Communication per landmark is stated as 3.96 KB indoor, 1.84 KB urban, and 2.03 KB forest, and per meter traveled as 1.65, 1.85, and 5.13 KB (p. 16). The computation is not described; dividing the Table VI averages by the object counts reproduces the urban and forest values but gives about 4.5 KB indoor, and the per-meter values do not follow from Table VI.
- SemanticKITTI, three virtual robots: absolute trajectory error 0.998 m versus SuMa++ 1.154 m (sequence 05, 2.8 km) and 0.962 m versus 1.148 m (sequence 07, 1.2 km), with ground-truth segmentation and SuMa++ initial poses (pp. 16-17).
- Loop-closure benchmark, robot 0 to robot 1, SlideGraph versus CLIPPER and LCDNet (p. 17, Table VII): translation error 0.03 versus 0.04 and 0.09 m (KITTI 05), 0.09 versus 0.06 and 0.05 m (KITTI 07), 0.13 m versus CLIPPER failed and LCDNet 1.10 m (forest); yaw error 0.08° versus 0.04° and 0.22°, 0.09° versus 0.01° and 0.21°, and 2.6° versus failed and 0.1°; CPU runtime 40, 50, and 209 ms versus CLIPPER 152 and 202 ms and LCDNet 1580 ms per scan pair on GPU. Map size is 7.2 KB, 7.3 KB, and 16 KB for SlideGraph and CLIPPER versus 0.84 MB per scan for LCDNet.
- In a forest map pair of about 300 and 800 landmarks, SlideGraph reduces about 240 000 CLIPPER hypotheses to about 3000; the original CLIPPER ran out of memory (p. 17).

## Stated limitations

- The map uses only three simple shapes, which may miss fine details needed
  for manipulation and may lose information, causing inaccurate or missed
  loop closures in ambiguous or repetitive layouts; semantic aliasing raises
  dependence on correct labels, and misclassification can cause errors
  (pp. 17-18).
- Loop closures are accepted one-shot with an inlier threshold, without
  consensus filtering over several candidates, which may fail in scenes with
  repeated objects and similar pairwise distances such as similar conference
  rooms or dense forests (p. 18).
- Dynamic objects are not modeled; they violate the pairwise distance
  consistency assumption and can induce faulty loop closures (p. 18).
- SlideGraph fails between RGB-D aerial and ground robots because noisy RGB-D
  sensing and different viewed object parts reduce pairwise consistency
  (p. 14); noise requires careful selection of the SlideMatch search
  discretization or the SlideGraph matching threshold (p. 14).
- SlideMatch handles these noisy cases at the cost of significant
  computational overhead (p. 16).
- The darknet-13 backbone used for Table V is the smallest and less accurate
  one, chosen for real-time onboard inference (p. 14).

## Transfer conditions

The method needs object classes that are common and static in the target
scene, an RGB-D camera or 3D LiDAR with a working detector, a separate
odometry source (VIO or LIO), and an IMU whose roll and pitch can be trusted,
because only X, Y, Z, and yaw are estimated between robots. With RGB-D
cameras, SlideGraph failed in the aerial-ground case and was less accurate
between the Scarabs, which leaves SlideMatch, the slower algorithm. The communication results
come from replay with a fixed 10 s schedule and full-database messages, so a
real lossy or bandwidth-capped link, and message growth over long missions,
remain untested. The onboard CPUs are desktop-class Intel i7 processors, and
Table VI timings are from a laptop, not from an embedded board. Scarab drive
type and wheel odometry are not described, and the ground robot moves at
0.5 m/s.

## Code and data

The paper links code at https://github.com/KumarRobotics/SLIDE_SLAM and a
project website at https://xurobotics.github.io/slideslam/ (p. 1, footnote).
Release of the recorded robot datasets is not stated. Neither link was
checked.

## Version family

Table I dates SlideSLAM to 2024 (p. 2), which suggests an earlier preprint;
it was not checked. The system builds on the authors' earlier active
metric-semantic SLAM work (references [3], [5], and [8]); none of these is
in the library, and this journal article is counted once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Sec. V-F, p. 14 | "This limitation is caused by reduced pairwise consistency between object positions in the map, which stems from noisy RGB-D sensing combined with the fact that the aerial and ground robots observe different parts of the objects." |
| C3 | unset | n/a | | |
| C4 | partial-support | moderate | Sec. V-I, p. 16 | "This modest communication demand is particularly important when robots operate under intermittent and bandwidth-limited communication conditions." |
| C5 | partial-support | weak | Sec. VI, p. 18 | "Currently, we only use a sufficient inlier threshold to filter out FPs" |
| C6 | qualifies | moderate | Sec. V-F, p. 14 | "In addition, it is important to note that the increased noise levels require a careful selection of parameters, such as the search discretization in SlideMatch or the descriptor matching threshold in SlideGraph." |

## Page-cited excerpts

- **p. 15, Sec. V-I.** "To replicate intermittent communication, each robot publishes ROS messages to each other every 10 seconds."
  The intermittent communication is a fixed publishing schedule in replay, not a measured network condition.
- **p. 15, Sec. V-I.** "we replicate all robots as being within communication range by streaming their data on different ROS nodes running on a laptop."
  The Table VI communication numbers come from one laptop with all robots in range.
- **p. 14, Sec. V-F.** "In contrast, the SlideGraph algorithm fails to perform inter-robot loop closures between RGBD-based aerial and ground robots."
  Cross-platform merging did not succeed with both algorithms.
- **p. 11, Sec. V-A.** "All modules in our software system, including instance segmentation, metric-semantic SLAM, exploration, planning, and control, as shown in Fig. 1, execute in real time onboard the robots."
  The basis for the closed-loop onboard coding; it gives no onboard timing.
- **p. 16, Sec. V-K.** "The framework takes in the point clouds, initial pose estimation from SuMa++ [24], and ground truth segmentation, and estimates the metric-semantic map as well as the robot trajectory."
  The SemanticKITTI accuracy assumes perfect segmentation and SuMa++ initial poses.
- **p. 18, Sec. VI.** "Such objects (e.g., a car changing its parking spot over time) violate the pairwise distance consistency assumption required for robust place recognition and can, therefore, induce faulty loop closures."
  Dynamic objects are a stated failure source that the evaluation does not test.

## Survey-usable statements

### Supported

- Three wheeled robots ran object-level metric-semantic SLAM, exploration, and
  map merging onboard in one indoor closed-loop run; SlideMatch reached a mean
  inter-robot position error of 0.28 m.
- Object-level maps let a LiDAR robot and an RGB-D robot register into one
  frame (0.542 m with SlideMatch, 0.578 m with SlideGraph) in one indoor
  experiment.
- On replayed data, average messages were 0.30 MB indoor to 1.74 MB in a
  forest with 860 objects, under a 10 s full-database publishing schedule.
- SlideGraph loop closure took 22-406 ms on a laptop CPU, against
  123-3638 ms for SlideMatch (Table VI).

### Not supported

- SlideGraph is more accurate than CLIPPER and LCDNet on every benchmark:
  CLIPPER and LCDNet have lower translation error on KITTI 07 (0.06 and
  0.05 m versus 0.09 m), CLIPPER has lower yaw error on KITTI 05 and 07
  (0.04° and 0.01° versus 0.08° and 0.09°), and LCDNet has lower yaw error in
  the forest (0.1° versus 2.6°). SlideGraph is better on all three runtimes
  and on forest translation (Table VII).
- SlideGraph is the more accurate of the two place-recognition algorithms:
  SlideMatch has the lower position error on 8 of the 10 pairs where both
  succeed, and SlideGraph failed the aerial-ground pair (Table IV).
- The system was shown robust to real packet loss, delay, or link outages:
  the schedule was replicated in replay, and no loss or delay was injected
  or measured.
- Communication usage in MB is a data rate: Table VI reports message sizes.
- Decentralized collaboration improved exploration outcomes: no coverage,
  time, or success metric is reported, and no single-robot or centralized
  comparison is run.
- The SemanticKITTI trajectory gain over SuMa++ holds with learned
  segmentation: ground-truth segmentation was used.

## Verification log

- 2026-10-27 | host: Kiro | scope: full text read (Secs. I-VII, reference list skipped); Tables I, III, IV, V, VI, and VII read from rendered page images (pp. 2, 11, 13, 14, 15, 17); all numbers and excerpt pages located with tools.locate | corrections: rebuilt in English in template format with survey coding; legacy reviewer observations moved out of the limitations; Table VII counterexamples, the Table IV versus text yaw inconsistency, the Experiment 1 operation-mode inconsistency, and the unreproducible per-landmark communication ratios added; garbled legacy excerpt dropped; Scarab coded wheeled-unspecified (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/0b84d28b6394d108ab72ae46/

## Original abstract

This article develops a real-time decentralized metricsemantic simultaneous localization and mapping (SLAM) algorithm that enables a heterogeneous robot team to collaboratively construct object-based metric-semantic maps. The proposed framework integrates a data-driven front-end, for instance, segmentation from either RGBD cameras or light detection and ranging (LiDAR) and a custom back-end for optimizing robot trajectories and object landmarks in the map. To allow multiple robots to merge their information, we design semantics-driven place recognition algorithms that leverage the informativeness and viewpoint invariance of the object-level metric-semantic map for inter-robot loop closure detection. A communication module is designed to track each robot’s observations and those of other robots whenever communication links are available. The framework supports real-time, decentralized operation onboard the robots and has been integrated with three types of aerial and ground platforms. We validate its effectiveness through experiments in both indoor and outdoor environments, as well as benchmarks on public datasets and comparisons with existing methods. The framework is opensourced and suitable for both single-agent and multirobot real-time metric-semantic SLAM applications.
