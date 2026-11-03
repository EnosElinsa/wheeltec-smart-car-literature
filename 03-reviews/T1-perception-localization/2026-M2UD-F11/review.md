# M2UD: A multi-model, multi-scenario, uneven-terrain dataset for ground robot with localization and mapping evaluation

## Metadata

| Field | Value |
|---|---|
| ID | F11 |
| Title | M2UD: A multi-model, multi-scenario, uneven-terrain dataset for ground robot with localization and mapping evaluation |
| Authors | Yanpeng Jia, Shiyi Wang, Shiliang Shao, Yue Wang, Fu Zhang, and Ting Wang |
| Venue | The International Journal of Robotics Research, 45(10), 1457–1477 |
| Year | 2026 (online 2025) |
| Type | journal |
| DOI | [10.1177/02783649251401224](https://doi.org/10.1177/02783649251401224) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649251401224 |
| Theme folder | T1-perception-localization |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T1-perception-localization/2026-M2UD-F11/paper.pdf` and `02-fulltext/T1-perception-localization/2026-M2UD-F11/paper.md` (local only); [BibTeX](../../../01-papers/T1-perception-localization/2026-M2UD-F11/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: fault-recovery-deployment
- evidence_type: dataset-resource
- evidence_all: dataset-resource, recorded-robot-data
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: self-developed six-wheeled outdoor robot and four-wheeled indoor robot; detachable sensor rig also used handheld for detailed mapping captures
- boundary_platform: no
- degradation: visual-degradation, lidar-degeneracy, terrain, dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Velodyne VLP-16, RealSense D455, Xsens MTi300, M68UGI-G GNSS; FARO scanner and limited Leica Laser Tracker checks provide separate references
- compute: onboard ROS bag recording to 4 TB SSD; benchmark CPU/GPU and control-loop latency not reported in selected passages
- compute_location: not-reported
- summary_result: M2UD provides rough-terrain multi-sensor recordings and localization/mapping reference data, with sequence-level SLAM benchmarks rather than a pose-uncertainty-conditioned navigation controller.
- summary_limitation: The authors propose future semantic labels for navigable-area and terrain analysis, more accurate hardware synchronization, and more challenging scenes with map ground truth.
- survey_included: yes
- verification_level: light

## Problem

Ground-robot SLAM datasets often emphasize planar motion and a narrow range of conditions. M2UD supplies aggressive six-degree-of-freedom motion, uneven terrain, and degraded sensing for localization and map benchmarking (pp. 1, 7, 19). For G3, it offers data for studying how localization degrades on terrain; that resource is distinct from a controller that changes terrain cost or speed using pose uncertainty.

## Mechanism

Two sensor-equipped ground robots record ROS bags, with calibration, software timestamp alignment, format conversion, and trajectory evaluation tools (pp. 7–9, 12–13). Outdoor localization references smooth noisy RTK data; indoor references use offline multi-sensor SLAM, and mixed routes add RTK factors when available (pp. 11–12). A static FARO scan supplies reference maps for two scenes, matched offline with dynamic ghosting manually removed; detachable sensor kits are also carried by hand for detailed mapping captures (p. 12). EA-Drift augments trajectory error with per-frame processing time (pp. 13–14). None of these selected mechanisms propagates pose covariance to a closed-loop terrain planner.

## Baselines and controls

The primary localization benchmark compares A-LOAM, KISS-ICP, LIO-SAM, FAST-LIO2, DSO, VINS-Mono, and ORB-SLAM3. The authors retain default method parameters and change sensor intrinsics/extrinsics; the rural sequence has no images, and the plaza sequence is evaluated only before entering a lift because all methods fail afterward (p. 15). Additional methods appear in qualitative map/trajectory examples (p. 16). Mapping comparisons include LIO-SAM, FAST-LIO2, Point-LIO, SLAMesh, and ImMesh (p. 19). Full baseline implementation parity, all plots, and numeric table cells were not audited.

## Platform and setup

A six-wheeled rocker-arm robot primarily records outdoors, and a four-wheeled mobile robot primarily records indoors; steering mechanics are not specified in the selected setup text (p. 7). The resource contains 58 sequences in 12 categories and over 50 km of recordings, including uneven terrain, aggressive motion, dark corridors, open areas, dynamic scenes, and smoke/snow/dust conditions (pp. 1, 7, 11, 19). The primary evaluation selects 12 localization sequences and two mapping scenes (pp. 1, 14, 19). Detailed mapping capture also uses the detachable rig handheld, so the map subset should not all be described as wheeled closed-loop trials (p. 12).

## Evidence type and transfer

The contribution is a dataset resource with SLAM benchmarks on recorded data, not a demonstrated autonomous terrain-navigation controller. Recording with an onboard computer does not establish that any evaluated SLAM algorithm controlled the vehicle. The selected evaluations report trajectory/map error and compute-sensitive estimator scores, rather than collision, intervention, speed-adaptation, or mission-success results for a pose-uncertainty-conditioned planner (pp. 13–16, 19).

## Sensors

Both robots use the same Velodyne VLP-16, RealSense D455, Xsens MTi300, and M68UGI-G GNSS configuration. The selected MTi300 replaces the camera's internal IMU for the supplied inertial measurements. GNSS/RTK is used to build outdoor reference trajectories, not evidence that a benchmark method needs online RTK. Camera/IMU/LiDAR extrinsics and software time alignment are described; the authors use ROS ApproximateTime and estimate/compensate a camera-to-LiDAR offset instead of a shared hardware trigger (pp. 8–9). FARO map scans and Leica Laser Tracker checks have separate reference roles (pp. 11–12).

## Compute and latency

ROS bags are stored on a 4 TB SSD in an onboard computer; processor and GPU specifications were not identified in the selected setup or benchmark passages (p. 7). EA-evo consumes a frame-by-frame timing file and sensor frequency to incorporate estimator processing time into EA-Drift (pp. 13–14). That score is not an end-to-end sensing/planning/actuation delay, an onboard feasibility measurement, or a collision-risk bound. Benchmark compute placement is not established by the recorder's location.

## Key quantitative results

- The resource contains 58 sequences across 12 categories, with a total route length over 50 km; these are dataset scale, not autonomous mission-success statistics (p. 19, Conclusion).
- Twelve selected localization sequences and two map-evaluation scenes support the reported benchmark; table cells and algorithm rankings were not independently checked (pp. 1, 14, 19).
- Independent Laser Tracker validation covers two representative indoor sequences; the authors explicitly say localization accuracy is not verified for every indoor sequence (p. 12).

No Table 5/7/9 numeric effect size is transcribed in this targeted light review.

## Stated limitations

- Data-collection permissions, equipment, and venue restrictions prevent Laser Tracker use in every indoor scene; indoor reference accuracy is validated on two representative sequences instead (pp. 11–12).
- Semantic labels for point clouds/images and navigable-area or terrain analysis remain future work (p. 19).
- The authors plan more accurate hardware time synchronization, more robust outdoor platforms, and additional challenging scenes with accurate reference maps (p. 19).

## Transfer conditions

For G3, use the recordings to compare pose-estimation degradation under matched uneven-terrain and sensing conditions, while retaining reference uncertainty and sensor timing as part of the evaluation. Smoothed RTK can contain model-dependent corrections, and an indoor reference generated by another SLAM system is not uniformly independent metrology; neither the two Laser Tracker checks nor static map scans certify every sequence. The handheld mapping subset differs from the main wheeled localization captures. A new closed-loop experiment must supply terrain labels/costs, a calibrated pose-uncertainty estimate, a policy for speed or path changes, and paired safety/task outcomes. EA-Drift's compute penalty does not supply those control decisions (pp. 11–14, 19).

## Code and data

The paper states that data, videos, calibration sequences, and development kits are available at [the M2UD project page](https://yaepiii.github.io/M2UD/) (pp. 1, 8, 12–13). Tools include RTK smoothing/publishing, bag conversion, trajectory alignment, and EA-evo evaluation. Downloads, licenses, executability, and reproduction were not independently checked in this targeted read.

## Version family

The supplied publisher PDF and raw BibTeX identify the 2026 IJRR volume 45(10), pages 1457–1477. Copyright and the previously verified online publication are in 2025; the download filename does not change the formal year. The title says "multi-model" while the abstract uses "multi-modal"; each source wording is preserved. This DOI is counted once as F11; other version-family relations were not audited.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Conclusion, p. 19 | "including extensive degraded situations, aggressive motion, and uneven terrain" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Future work, p. 19 | "we plan to assign 3D semantic labels to point clouds and images for use in navigable area and terrain analysis." |

## Page-cited excerpts

- **p. 7, Acquisition platform.** "two self-developed ground robots are utilized for data collection, both equipped with identical sensors to ensure data consistency."
  Physical data collection is established; closed-loop use of any benchmark estimator is not.
- **p. 12, Localization ground truth.** "although the localization accuracy is not verified on all indoor sequences"
  Independent validation of representative routes does not cover every indoor reference.
- **p. 19, Conclusion.** "we plan to assign 3D semantic labels to point clouds and images for use in navigable area and terrain analysis."
  The dataset supports a future terrain-analysis study without supplying a tested terrain-control policy.

## Survey-usable statements

### Supported

- M2UD adds wheeled rough-terrain and degraded-sensing recordings with localization/map references and a compute-sensitive SLAM metric (pp. 7–14, 19).
- Its indoor reference pipeline uses offline SLAM, with independent Laser Tracker checks on two representative sequences rather than every indoor route (pp. 11–12).

### Not supported

- Pose covariance changes terrain cost, speed, or recovery in a measured navigation loop; the selected method is a dataset/benchmark pipeline, with terrain-analysis labels left for future work (pp. 13–14, 19).
- Every sequence has an independent millimeter-accuracy localization reference; reference methods differ by environment and only selected routes have external validation (pp. 11–12).
- A compute-weighted error metric demonstrates safe onboard control; the benchmark does not measure the full robot decision/actuation loop (pp. 13–16).

## Verification log

- 2026-11-02 | host: Codex | scope: new targeted light reading of physical PDF p. 1 identity/abstract; pp. 7–9 platform/sensors/calibration; pp. 11–14 reference generation and evaluation; pp. 15–16 selected baseline and failure discussion; p. 19 mapping/conclusion/future work; metadata and selected prose values checked; no whole-paper, proof, or rendered-table audit | corrections: new F11 card; distinguishes recorded data, handheld mapping subset, reference dependencies, and terrain-control evidence; formal 2026 and online 2025 retained.
- Legacy extraction: none; new follow-up reading from the user-supplied publisher PDF and unchanged publisher BibTeX.

## Original abstract

As one of the most widely used types of robots, ground robots play a crucial role in inspection, exploration, rescue, and other applications. In recent years, advancements in light detection and ranging (LiDAR) technology have made sensors more accurate, lightweight, and cost-effective. Therefore, researchers increasingly integrate LiDAR with other sensors, such as inertial measurement units (IMUs) and cameras, for simultaneous localization and mapping (SLAM) studies, providing robust technical support for ground robots and expanding their application domains. Public datasets that incorporate multiple sensors and diverse scenarios are essential for advancing SLAM technology in ground robots. However, existing datasets for ground robots are typically restricted to flat-terrain motion with 3 degrees of freedom (DOF) and cover only a limited range of scenarios. Although handheld devices and unmanned aerial vehicle (UAV) exhibit richer and more aggressive movements, their datasets are predominantly confined to small-scale environments due to endurance limitations. To fill these gaps, we introduce M2UD, a multi-modal, multi-scenario, uneven-terrain SLAM dataset for ground robots. This dataset contains a diverse range of highly challenging environments, including cities, villages, open fields, long corridors, plazas, underground parking, and mixed scenarios. Additionally, it presents extreme weather conditions such as darkness, smoke, snow, and dust. The aggressive motion and degradation characteristics of this dataset not only pose challenges for testing and evaluating existing SLAM methods but also advance the development of more advanced SLAM algorithms. To benchmark SLAM algorithms, M2UD provides smoothed ground truth localization data obtained via real-time kinematics (RTK) and introduces a novel localization evaluation metric that considers both accuracy and efficiency. Additionally, we utilize a high-precision millimeter-level laser scanner to acquire ground truth maps of two representative scenes, facilitating the development and evaluation of mapping algorithms. We select 12 localization sequences and 2 mapping sequences to evaluate several classical LiDAR and visual SLAM algorithms, verifying usability of the dataset. To enhance usability, the dataset is accompanied by a suite of development kits, including data transformation, timestamp alignment, ground truth smoothing. The dataset and related videos are available at https://yaepiii.github.io/M2UD/.
