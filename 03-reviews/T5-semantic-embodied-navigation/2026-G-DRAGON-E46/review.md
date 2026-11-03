# G-DRAGON: Geospatial Reasoning and Dynamic Planning for Retrieval-Augmented Outdoor Navigation

## Metadata

| Field | Value |
|---|---|
| ID | E46 |
| Title | G-DRAGON: Geospatial Reasoning and Dynamic Planning for Retrieval-Augmented Outdoor Navigation |
| Authors | Dongzhihan Wang, Yi Du, Jianan Sun, Yuan Xue, Yingchen Zhang, Bing Xiao, Chen Wang, and Liang Xu |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 7, pp. 8768-8775 |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3699135](https://doi.org/10.1109/lra.2026.3699135) |
| Official URL | https://ieeexplore.ieee.org/document/11543204/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2026-G-DRAGON-E46/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2026-G-DRAGON-E46/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2026-G-DRAGON-E46/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: few-trials
- platform_class: wheeled-unspecified
- platform: Agilex Scout Mini UGV (drive type not recorded in the legacy card); NVIDIA Nova Carter UGV in Isaac Sim
- boundary_platform: no
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual
- sensors: RoboSense Helios16P 16-beam LiDAR, Intel RealSense D455F RGB-D camera, IMU, WheelTec G70 GPS
- compute: NVIDIA Jetson AGX Orin 64GB onboard; Qwen2.5-14B on a local edge server for the initial behavior tree; latency not reported
- compute_location: mixed
- summary_result: Isaac Sim Task 1 (building, 5 m): SR 100% / 95.56% at 300 / 800 m versus OPEN 77.78% / 26.67%; NoMaD fails at long range.
- summary_limitation: The authors state that the system still needs a local network link to an edge server to obtain the initial behavior tree.
- survey_included: yes
- verification_level: light

## Problem

Natural-language commands must be grounded in local OpenStreetMap (OSM) entities to complete outdoor routes of several hundred meters and then hand over to an open-vocabulary "last-mile" search around the target building.

## Mechanism

GeoQA assigns OSM entities category-name IDs; a single pretrained LLM first extracts semantic cues and then decodes with Trie-constrained beam search, so it outputs only existing IDs. RAPPER uses Qwen2.5-14B to generate, in one pass, an XML behavior tree from a predefined library of actions and conditions; GeoQA and a local OSRM instance generate the road route, and the goal is the nearest point on the building outline. NæVIS combines LIO with a RayFronts open-semantic voxel map. After the GPS signal stabilizes, the robot drives straight for 5 m to calibrate the local-to-ENU heading; waypoints are sampled every 20 m on straight roads and every 3 m on curves. Near the goal, the robot scans 360 degrees, searches the nearest frontier inside the OSM building polygon, clusters thresholded voxels with DBSCAN, and projects the cluster centroid as the navigation goal. The behavior tree restarts route search on stagnation or planning failure.

## Baselines and controls

GeoQA is compared with BM25, DPR, vanilla Qwen2.5-14B, and GPT-4o. In navigation, NoMaD receives goal images and OPEN receives exact coordinates, while G-DRAGON receives semantic instructions and OSM, so inputs differ (p. 6). The real-world RAPPER ablation gives the ENU goal directly without intermediate topological waypoints.

## Platform and setup

- Simulation: two Isaac Sim campus digital twins with an NVIDIA Nova Carter UGV; GNSS is ground truth converted to WGS84 with added Gaussian noise. 45 episodes per range (300 and 800 m): 5 buildings x 3 positions x 3 headings. Task 1 reaches a building (5 m success threshold); Task 2 then searches for an object (2 m threshold) (p. 7).
- Retrieval: 5000 queries synthesized by an external LLM from about 300 building nodes in a 1 x 1 km region of one campus, Easy:Hard 7:3 (p. 5).
- Real world: Agilex Scout Mini on a university campus, four scenarios of 200-500 m (p. 7). Fig. 4 labels only the GPS receiver as WheelTec G70; the chassis is not a WHEELTEC robot.
- Mission start needs a network link to the local edge server; execution can then run offline (p. 8).

## Evidence type and transfer

Quantitative navigation and retrieval results come from simulation and synthetic queries; hardware evidence is four closed-loop runs on a wheeled robot. No multi-day operation, repeated real statistics, or fully offline start-up.

## Sensors

The real robot carries a 16-beam LiDAR, an RGB-D camera, an IMU, and GNSS; Fig. 4 labels them RoboSense Helios16P, Intel RealSense D455F, and WheelTec G70 GPS. LIO and the RayFronts semantic voxel map use these sensors. The 5 m heading initialization depends on stable GNSS (p. 5), so it is not evidence of GNSS-denied robustness.

## Compute and latency

The real robot carries an NVIDIA Jetson AGX Orin, 64GB in Fig. 4 (p. 6). Qwen2.5-14B runs on a local edge server to provide the initial behavior tree; the server CPU and GPU, inference latency, memory, and end-to-end rate are not reported. The RTX 5090 is used for simulation rendering and is not evidence of onboard Orin inference time (p. 6).

## Key quantitative results

- Navigation (Table I), G-DRAGON at 300 / 800 m: Task 1 SR 100 / 95.56%, SPL 85.25 / 81.45%; Task 2 SR 80 / 62.22%, SPL 38.52 / 35.67% (p. 7, Table I).
- OPEN: Task 1 SR 77.78 / 26.67%, Task 2 SR 20 / 17.78%; NoMaD reaches 0 on both long-range tasks (Table I, image; no located page).
- Retrieval (Table II): GeoQA Easy R@1 / R@5 97.6 / 99.6%, Hard 74.8 / 81.8%; GPT-4o Hard 87.4 / 88.1% is higher than GeoQA, so GeoQA is not best at every difficulty (Table II, image; no located page).
- Real-world RAPPER ablation (Table III): SPL with RAPPER 87.27 / 83.32 / 86.25 / 84.28% in the four scenarios, without RAPPER 0 / 0 / 21.64 / 0% (Table III, image; no located page). Completing all four runs is not a stable success-rate statistic.
- The legacy card notes that the general claim of exceeding baselines by 50% has no single metric definition; the per-task table values are used instead.

## Stated limitations

- The current system still requires a local network link to the edge server to obtain the initial behavior tree (p. 8).
- Onboard LLM deployment to remove this start-up dependency is future work (p. 8).

## Transfer conditions

Legacy reviewer observations:
- Local OSM entities, road network, and GNSS are required; exploration of a fully unknown map is not the goal.
- The Trie guarantees only that the ID exists, not that retrieval is correct; Hard R@1 is still 74.8%.
- The behavior tree is drawn from a fixed skill library and is not a proof that arbitrary instructions are executable or safe.
- Generalization to other regions is not tested; the retrieval set is one campus with LLM-synthesized queries, and cross-domain or human-query bias is not addressed.
- The four real runs have no repetitions or variance, and the edge link only decouples execution after start-up.

## Code and data

The full text gives no repository URL for the method source code, the 5000 queries, or the simulation data. The code and supplementary material were not checked. Cited OSM, OSRM, and open-source baselines do not mean the full implementation is open.

## Version family

The RA-L 2026 paper is counted once; it does not claim to extend a conference version. OPEN and OpenBench are earlier comparison works and are not merged with this one; the GeoQA, RAPPER, and NæVIS modules are not counted separately.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | qualifies | moderate | Sec. V, p. 8 | "the current system still requires a local network link to the edge server to obtain the initial Behavior Tree." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV-D, p. 6 | "we provide OPEN with exact coordinates and NoMaD with target images" |

## Page-cited excerpts

- **p. 4, Sec. III-A GeoQA Module.** "This mechanism effectively eliminates semantic hallucination by ensuring that every generated token sequence corresponds to an extant entity in the OSM database"
  The constraint ensures a valid entity; Table II Hard R@1 of 74.8% shows that it does not ensure the right one.
- **p. 4, Sec. III-B Rapper.** "it utilizes a locally deployed LLM to parse instructions into a Behavior Tree, decomposing tasks and selecting skills from the predefined pool."
  The behavior tree selects from predefined skills.
- **p. 5, Sec. III-C NæVIS.** "Once the GPS signal stabilizes, the robot traverses a straight-line trajectory of length"
  Heading initialization (5 m in the same passage) needs stable GNSS and room to drive straight.
- **p. 5, Sec. IV-A Experiment Setup.** "These queries were synthesized using an external LLM based on approximately 300 building nodes"
  The 5000 queries are LLM-synthesized from one campus.
- **p. 6, Sec. IV-A Experiment Setup.** "We evaluate our system on an Agilex Scout Mini UGV shown in Fig. 4(a), equipped with an NVIDIA Jetson AGX Orin."
  The chassis is a Scout Mini; the LLM start-up runs on the edge server.
- **p. 6, Sec. IV-D Quantitative Results on Simulation Environments.** "we provide OPEN with exact coordinates and NoMaD with target images"
  Baseline inputs differ from the semantic instruction and OSM input.
- **p. 7, Sec. IV-D Quantitative Results on Simulation Environments.** "requiring subsequent exploration around the building polygon to locate a specific object"
  Task 2 adds object search with a stricter 2 m threshold.
- **p. 7, Sec. IV-E Real-World Deployment.** "We deployed the system at a large-scale university campus to evaluate real-world performance across four 200m–500 m scenarios."
  Only four real scenarios, without repetitions.
- **p. 8, Sec. V Limitations and Future Work.** "the current system still requires a local network link to the edge server to obtain the initial Behavior Tree."
  Start-up depends on the edge server.
- **p. 8, Sec. V Limitations and Future Work.** "Future work will explore deploying onboard LLMs to eliminate this start-up dependency and enable truly standalone task initialization."
  An onboard LLM is future work.

## Survey-usable statements

### Supported

- In Isaac Sim campus twins, OSM-grounded generative retrieval with a behavior-tree planner reaches the target building in 100% and 95.56% of episodes at 300 and 800 m, where OPEN reaches 77.78% and 26.67%.
- On a wheeled UGV with a Jetson AGX Orin, the system completed four 200-500 m campus missions after an edge-server start-up.

### Not supported

- Trie-constrained retrieval removes retrieval errors: Hard R@1 is 74.8%, and GPT-4o is better on Hard queries.
- The system runs fully standalone: the initial behavior tree needs an edge-server link.
- The real-world results are a success-rate statistic: four single runs.
- The system works without GNSS: heading initialization needs a stable GPS signal.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: Chinese card converted to the English template; the legacy synthetic-query quote was cut before "extracted from a 1×1 km2 region" and the Task 2 quote was cut to "requiring subsequent exploration around the building polygon to locate a specific object", because the full strings do not match paper.md exactly; the three table-caption pseudo-quotes and the duplicate Fig. 4 quote were dropped; most table values have no located page
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/4a70a81eb3a3642e8c840ae2/

## Original abstract

Autonomous ground robots operating in large-scale outdoor environments require both robust long-range navigation and fine-grained “last-mile” exploration. Current advances in visual-language navigation (VLN) work well at short-range tasks, lacking geospatial grounding for long-distance missions. Some OpenStreetMap (OSM)-based methods relying on cloud-based Large Language Models (LLMs) are prone to factual hallucination and cannot conduct “last-mile” exploration based on human instruction. To address these challenges, we present G-DRAGON, a retrieval-augmented framework for outdoor, open-world navigation. This framework maps natural-language commands to versioned, local OSM entities via generative retrieval based on lightweight LLM, yielding accurate coordinates for global route planning. A high-level planning module bridges global topological routes with the SLAM system, projecting geospatial waypoints into the robot’s navigable frame. For the “last mile,” the framework transitions to frontier-based exploration and open-set semantic voxel mapping to localize open-vocabulary targets. Experimental results in simulation demonstrate our framework outperforms state-of-the-art baselines. Furthermore, we validate the system in unseen real-world urban environments on an Unmanned Ground Vehicle (UGV), successfully completing person-search missions with trajectories of up to 500 m.
