# OPEN: Lightweight Map-Based Semantic Navigation for GPS-Free Last-Mile Delivery
## Metadata
| Field | Value |
|---|---|
| ID | M10 |
| Title | OPEN: Lightweight Map-Based Semantic Navigation for GPS-Free Last-Mile Delivery |
| Authors | Junhui Wang, Dongjie Huo, Yongliang Shi, Chao Gao, Yan Qiao, and Guyue Zhou |
| Venue | IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 20713-20725 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/tase.2025.3605356](https://doi.org/10.1109/tase.2025.3605356) |
| Official URL | https://ieeexplore.ieee.org/document/11146857/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-OPEN-M10/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-OPEN-M10/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2025-OPEN-M10/citation.bib) |
## Survey coding
- survey_module: semantic-language-navigation
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware
- platform_class: wheeled-unspecified
- platform: unnamed wheeled campus robot with Logitech RGB camera, Livox MID-360, and GPS for ground-truth logging (Fig. 8); simulated differential-drive four-wheel robot in Gazebo
- boundary_platform: no
- degradation: gnss-denial, scene-change
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: monocular RGB camera (Logitech); Livox MID-360 LiDAR
- compute: AMD R9-7945HX with RTX 4060 for the benchmark; edge-side large model on an RTX 4090D (24 GB)
- compute_location: not-reported
- summary_result: In Gazebo residential scenes, OPEN reaches 100% success in small and medium scenes and 80% in the large scene, versus 40%, 20%, and 0% for ViNT and NoMaD.
- summary_limitation: The authors state that OSM geometry can deviate from the road network, that LLM task planning fails through hallucination and output-format violations, and that indoor scenes are out of scope.
- survey_included: yes
- verification_level: light
## Problem
Last-mile outdoor delivery needs scalable maps, localization without GPS (GPS is often occluded on campuses and in residential areas), and natural-language addresses. High-precision semantic maps are expensive, and learning-only navigators such as ViNT and NoMaD generalize poorly and do not consume structured addresses. Crowdsourced OpenStreetMap (OSM) is cheap but geometrically wrong, which can lead a robot off the road. Cloud VLMs add latency, connectivity, and privacy costs on edge robots.
## Mechanism
OPEN (OpenStreetMap-enhanced oPen-air sEmantic Navigation) couples foundation models with classical navigation on off-the-shelf OSM:
- An LLM parses delivery instructions into structured destinations (JSON). A fine-tuned MiniCPM-V-2.6 is compared with cloud LLMs such as GPT-4o-mini.
- A VLM with MobileSAM and CLIP matches image instances to OSM element types, projects LiDAR to a bird's-eye view, and registers it in 2D for a global pose without GPS; the same stack writes discovered entrance IDs back into OSM.
- Fast-LIO2 local LiDAR odometry is fused with the VLM global priors in a factor graph.
- A* and TEB provide planning, with a multi-source local replanner (traversability from open-world segmentation and inverse perspective mapping, LiDAR obstacle cost, OSM road-direction cost) for wrong OSM geometry.
- An exploration-exploitation-verification routine finds entrances around buildings.
GPS, when present, is used only for logging and is disabled during navigation.
## Baselines and controls
ViNT and NoMaD with goal-image inputs; replanning on and off under injected OSM deviations; cloud LLMs and VLMs versus on-device MiniCPM models for task planning and entrance recognition; a human teleoperation baseline in the real test. Other controls are not recorded in the legacy extraction; not verified.
## Platform and setup
- Simulation: ROS 2 and Gazebo with three residential scales; a simulated differential-drive four-wheel robot with a monocular camera and a Livox MID-360.
- Real robot: an unnamed wheeled campus platform with a Logitech RGB camera, a Livox MID-360, and GPS for ground-truth logging only (Fig. 8). On the university campus, GPS degrades between buildings and under trees, and GPS is disabled during navigation. The task is a sequential delivery to two buildings.
- Success means reaching within 10 m of the destination.
## Evidence type and transfer
The tabulated success rates and the OSM-deviation study come from Gazebo. The real campus test is a sequential delivery compared by trajectories with ViNT, NoMaD, and human teleoperation; the number of real runs is not recorded in the legacy extraction. The LLM and VLM accuracies are offline component evaluations.
## Sensors
Logitech RGB camera and Livox MID-360 LiDAR. GPS is present on the real robot but used only for ground-truth logging.
## Compute and latency
The benchmark ran on an AMD R9-7945HX with an RTX 4060; the edge-side large model was checked on an RTX 4090D with 24 GB (p. 9). Whether either ran onboard during the real test, and latency figures, are not recorded in the legacy extraction; not verified.
## Key quantitative results
- Gazebo success rate: OPEN 100% (small), 100% (medium), and 80% (large) versus 40%, 20%, and 0% for both ViNT and NoMaD (p. 10).
- OSM deviation of (1 m, 1 m): success rate with replanning 80% versus 20% without (p. 10, Table III).
- OSM deviation of (3 m, 1 m): success rate with replanning 60% versus 0% without (Table III).
- Map storage: OSM needs about 1% of a voxel point-cloud map and 0.01% of a NoMaD topological map (p. 11, Table VI).
- Task planning success rate: GPT-4o-mini 1.00; fine-tuned MiniCPM-V-2.6 0.97 after distillation; base MiniCPM models about 0.22-0.23 (p. 9, Table I).
- Entrance-number accuracy: GPT-4o 99% overall; MiniCPM-o-2.6 91% (p. 11, Table IV).
- Real campus delivery: ViNT and NoMaD collide before the first building, OPEN completes the sequence, and human teleoperation reaches 96.1% SPL (p. 11).
## Stated limitations
- Navigating directly along inaccurate OSM paths can cause robots to leave safe regions or collide with curbs and obstacles (p. 2).
- Cloud VLMs require stable connectivity, add latency, and raise privacy concerns, so reliable offline operation is needed (p. 2).
- LLM task planning fails through hallucinated details and through violations of the required output format (p. 9).
- Indoor environments lack OSM coverage and are not suitable for the system (p. 9).
- Future work covers dynamic environments and agents and learning-based navigation for residential generalization (p. 12).
## Transfer conditions
Success is defined within 10 m of the destination (p. 9), which is loose for door-to-door delivery. Legacy reviewer observations: the edge VLM check used an RTX 4090D, and cloud models give the strongest planners; MiniCPM entrance recognition (91%) is below the cloud VLMs. A wheeled robot reusing OPEN needs an outdoor area with OSM coverage, a 3D LiDAR for Fast-LIO2 and BEV registration, and GPU compute for the VLM.
## Code and data
The abstract states that code and benchmark are public at https://github.com/EI-Nav/light-map-navigation.git; not verified.
## Version family
Not recorded in the legacy extraction; not verified.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. VI, p. 12 | "By leveraging OSM as a lightweight map representation, OPEN eliminates the need for costly pre-mapping while ensuring adaptive navigation without relying on GPS, which is crucial for environments where GPS is degraded, unavailable, or intentionally avoided." |
| C3 | direct-support | moderate | Sec. I, p. 2 | "Deploying the OPEN system on resource-constrained edge devices introduces multiple challenges." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Experimental setup, p. 9 | "Indoor environments typically lack OSM coverage" |
## Page-cited excerpts
- **p. 12, Conclusion.** "By leveraging OSM as a lightweight map representation, OPEN eliminates the need for costly pre-mapping while ensuring adaptive navigation without relying on GPS, which is crucial for environments where GPS is degraded, unavailable, or intentionally avoided."
  GPS-degraded last-mile delivery is the operating condition; OSM error is a map-error mode, not a LiDAR or vision outage study.
- **p. 2, Introduction.** "Deploying the OPEN system on resource-constrained edge devices introduces multiple challenges."
  LLM and VLM navigation is constrained by edge compute, connectivity, and latency.
- **p. 12, Conclusion.** "Furthermore, its feasibility is validated on resource-constrained edge devices, ensuring practicality for real-world deployment."
  The authors claim edge feasibility; the edge check used an RTX 4090D.
- **p. 8, Real-world environment.** "The GPS is used solely for logging the ground truth trajectory and is disabled during navigation."
  The real test is GPS-free by design.
- **p. 9, Real-world environment.** "Indoor environments typically lack OSM coverage"
  The method does not apply indoors.
- **p. 11, Real-world results.** "ViNT and NoMaD both encounter collisions while navigating to the first building and are unable to complete the task."
  The real comparison is a single delivery sequence described by outcome.
## Survey-usable statements
### Supported
- OPEN navigates outdoor residential scenes on OSM without GPS and reaches 100%/100%/80% success in Gazebo, versus 40%/20%/0% for ViNT and NoMaD (numbers from a light review; re-check before citing).
- Local replanning recovers success under injected OSM deviations (80% versus 20% at (1 m, 1 m)).
### Not supported
- OPEN runs fully on a small onboard computer: the reported compute is a laptop-class R9-7945HX with RTX 4060 and an RTX 4090D for the edge model.
- OPEN is validated statistically on the real robot: the real test is a sequential delivery described by trajectories and outcomes.
- OPEN works indoors: the authors exclude indoor scenes for lack of OSM coverage.
## Verification log
- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Claim summary, Hardware caveat) converted to the English template; the 10 m success radius moved from limitations to Transfer conditions because it is a metric definition, and the MiniCPM accuracy gap moved there because it is a reviewer comparison; C6 excerpt replaced by the p. 9 indoor-scope sentence because the legacy C6 sentence reads as support and is kept as a plain excerpt; the code URL added from the abstract
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.
## Original abstract
The growing demand for efficient last-mile delivery highlights the need for autonomous robots to improve operational efficiency and reduce costs. Traditional navigation methods rely on high-precision maps, which are expensive to produce and maintain, while learning-based approaches often struggle to adapt to diverse real-world environments. To address these challenges, this paper presents OpenStreetMap-enhanced oPen-air sEmantic Navigation (OPEN), a system that combines foundation models with classic navigation algorithms to enable scalable outdoor navigation. By leveraging off-the-shelf OpenStreetMap (OSM), OPEN eliminates the need for extensive pre-mapping and provides a lightweight, readily available map representation. The system uses Large Language Models (LLMs) to interpret delivery instructions and Vision Language Models (VLMs) for global localization without relying on GPS, real-time map updates, and entrance recognition, ensuring robust navigation in complex environments. To further enhance adaptability, OPEN incorporates a local replanning method that dynamically adjusts waypoints in response to environmental changes and OSM inaccuracies. Since existing benchmarks do not adequately reflect the challenges of last-mile delivery, this work introduces a new benchmark designed for residential navigation. Experiments conducted in both simulated and real-world settings demonstrate that OPEN improves navigation accuracy, efficiency, and reliability, outperforming existing semantic navigation methods. To facilitate further research, the code and benchmark are publicly available at https://github.com/EI-Nav/light-map-navigation.git
