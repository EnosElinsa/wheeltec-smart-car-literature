# VL-TGS: Trajectory Generation and Selection Using Vision Language Models in Mapless Outdoor Environments

## Metadata

| Field | Value |
|---|---|
| ID | F05 |
| Title | VL-TGS: Trajectory Generation and Selection Using Vision Language Models in Mapless Outdoor Environments |
| Authors | Daeun Song, Jing Liang, Xuesu Xiao, and Dinesh Manocha |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 6, pp. 5791-5798 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3559822](https://doi.org/10.1109/lra.2025.3559822) |
| Official URL | https://ieeexplore.ieee.org/document/10960724/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-VL-TGS-F05/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-VL-TGS-F05/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2025-VL-TGS-F05/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, recorded-robot-data
- protocol_caveats: cloud-model, few-trials
- platform_class: wheeled-unspecified
- platform: Clearpath Husky; drive mechanics not independently checked in this targeted read
- boundary_platform: no
- degradation: terrain
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: Velodyne VLP16, RealSense D435i, odometry velocity, and GPS current/target position
- compute: laptop Intel i7 and NVIDIA GeForce RTX 2080; online GPT-4V selection takes 2-4 s
- compute_location: mixed
- summary_result: GPT-4V responses take 2-4 s while DWA follows a previously selected approximately 10 m trajectory in the single-run-per-method outdoor experiment.
- summary_limitation: The learned generator does not guarantee traversable candidates, and performance depends on VLM robustness.
- survey_included: yes
- verification_level: light

## Problem

Mapless outdoor navigation must respect geometric traversability and context such as sidewalks, curbs, flower beds, and zebra crossings. LiDAR geometry alone can miss color-semantic differences, while unconstrained visual reasoning can select physically unsuitable paths. VL-TGS generates geometric candidate trajectories and asks a VLM to choose among marked candidates (pp. 1, 3-4).

## Mechanism

An attention-based CVAE uses successive LiDAR observations and robot velocities to generate diverse candidate trajectories. Training combines traversability, CVAE, and diversity losses. Candidates from two successive time steps provide redundancy; Hausdorff-distance filtering removes near-duplicates. Camera/LiDAR transforms project numbered candidates into RGB, ordered by endpoint distance to a GPS goal. GPT-4V receives the marked image and a wheeled-robot/contextual-rules prompt, then selects a trajectory. DWA executes and locally adjusts the selected path while later VLM decisions are pending (pp. 3-4, 7).

## Baselines and controls

Trajectory comparisons include MTG, ViNT, NoMaD, PIVOT, and CoNVOI. Ablations contrast generative candidates with random candidate generation and compare VLM selection with MTG's goal-distance heuristic. The hardware run compares MTG, NoMaD, and CoNVOI. Each method has one hardware run, and human intervention counts as a failure (pp. 4, 6-7). Full parameter parity and every metric cell were not audited.

## Platform and setup

A Clearpath Husky carries VLP16 LiDAR, D435i camera, and a laptop. Its generator training/evaluation data include LiDAR/velocity, binary traversability maps, and diverse targets with ground-truth trajectories. The binary map is not used at inference. Four benchmark contexts are flower bed, curb, crosswalk, and a goal behind an obstruction. The outdoor hardware goal lies approximately 100 m away behind a building, and the planner recursively generates approximately 10 m paths. Each method is evaluated once in the combined real-world route (pp. 4-5, 7). Drive mechanics were not independently checked.

## Evidence type and transfer

Benchmark trajectory evidence concerns traversability against labeled maps and similarity to human-operated paths; hardware demonstrates mapless closed-loop execution with GPS goal direction and DWA. The single hardware run per method supplies no statistical failure rate. The benchmark deliberately emphasizes settings difficult for LiDAR and is primarily stationary; dynamic-obstacle handling is discussed rather than quantified as a dedicated stress test (pp. 6-7). For G2, semantic selection is separated from local motion response; for G3, traversability is conditioned on geometry and scene semantics rather than a propagated pose covariance.

## Sensors

Velodyne VLP16, RealSense D435i RGB, odometry-derived velocity, and GPS for robot/goal relative position. LiDAR-to-camera projection calibration is required for trajectory overlays. Labeled traversability maps are training/evaluation resources, not online inputs (pp. 3-4, 7). No explicit pose-uncertainty distribution or integrity monitor was established in the selected mechanism.

## Compute and latency

The robot uses a laptop with Intel i7 CPU and NVIDIA GeForce RTX 2080 GPU for the local pipeline, with online GPT-4V semantic selection (p. 4). VLM responses typically take 2-4 s; a new query is issued on response, and the local motion planner continues along the selected approximately 10 m trajectory while waiting (pp. 4, 7). Compute is coded mixed for the laptop pipeline and hosted model dependency. Model-server specifications, monetary query cost, worst-case response time, network-loss handling, and a timeout-triggered stop/recovery policy were not established in the selected sections.

## Key quantitative results

Only selected prose values are included; table cells and headline percentage improvements were not independently audited.

- VLM trajectory selection operates every 2-4 s, with approximately 10 m candidates; the authors state that this latency is unsuitable for high-frequency decision-making (pp. 4, 7).
- The real-world goal is approximately 100 m away, with one run per method; intervention to recover the robot defines failure (p. 7).
- Text reports the fewest interventions and shortest distance/time for VL-TGS in that route; exact Table II values were not read from an image and are omitted (p. 7).

## Stated limitations

- The deep generative model cannot guarantee consistently traversable candidates; sampling two successive time steps increases the chance of a traversable option without supplying a guarantee (p. 4).
- Online VLM output latency of 2-4 s makes it unsuitable for high-frequency real-time decisions (p. 7).
- Performance depends on VLM robustness, and the trajectory generator is a candidate for future improvement (p. 8).

## Transfer conditions

Reviewer conditions: validate geometric candidates, LiDAR/camera calibration, GPS goal estimates, robot footprint, curb/terrain constraints, and DWA collision response on the target platform. Continuing the previous path while waiting is the documented delay behavior; it is not a demonstrated timeout/failure fallback. The selected algorithm sends a chosen candidate to DWA, but does not establish a new certified collision test after VLM selection or arbitrary-model-error safety. Traversability loss and semantic context are not pose-uncertainty propagation. Wheeled transfer must separately check how localization errors alter overlays, costs, speed, and stopping. These observations narrow G2/G3 within this corpus; they do not establish a global absence of such methods.

## Code and data

The paper states that supplementary material is available through [the DOI](https://doi.org/10.1109/LRA.2025.3559822) (p. 1). Code/data-release URLs and executable availability were not verified in this targeted read.

## Version family

RA-L 2025 formal journal article. The CVAE generator follows MTG and the paper compares related navigation methods; no same-work conference-extension statement was located in the selected sections. Count this DOI once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | partial-support | moderate | Sec. IV-F, Low Frequency of Online Large VLMs, p. 7 | "This latency makes them unsuitable for high-frequency real-time decision-making." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. IV-E, Real Robot Experiment, p. 7 | "Each method was evaluated in a single run, and failures were counted whenever human intervention was required to recover the robot." |

## Page-cited excerpts

- **p. 4, Sec. III-C, VLM-Based Trajectory Selection.** "the deep-learning-based generative model cannot guarantee the consistent generation of traversable trajectories."
  Candidate generation is learned and does not itself certify traversability.
- **p. 7, Sec. IV-F, Low Frequency of Online Large VLMs.** "This latency makes them unsuitable for high-frequency real-time decision-making."
  Semantic-model timing cannot replace a fast local response loop.
- **p. 7, Sec. IV-F, Low Frequency of Online Large VLMs.** "the motion planner ensures the robot continues to follow the selected trajectory while waiting for the VLM’s decision."
  The documented delay behavior is continued execution, not an evaluated timeout recovery.
- **p. 7, Sec. IV-E, Real Robot Experiment.** "Each method was evaluated in a single run, and failures were counted whenever human intervention was required to recover the robot."
  The hardware comparison is bounded and does not establish a general failure probability.

## Survey-usable statements

### Supported

- VL-TGS overlays learned geometric candidates on camera images for VLM semantic selection, while DWA follows/adjusts the selected trajectory in a bounded outdoor wheeled-robot demonstration.
- G2 is narrowed by explicit continued-path behavior during slow model responses; G3 remains a transfer question because semantic/geometric traversability does not establish pose-uncertainty-aware decisions.

### Not supported

- Guaranteed traversable generation or certified post-VLM collision safety: the generator limitation is explicit, and the selected method relies on a local planner.
- A tested timeout, network-failure, or bad-model recovery policy: following the previous path while waiting does not establish these.
- Pose uncertainty directly alters terrain costs or speed, or statistically reliable dynamic-crowd performance: those mechanisms/evaluations were not established in the selected sections.

## Verification log

- 2026-11-02 | host: Codex | scope: targeted new-paper light review of physical PDF pp. 1, 3-4, selected scenario/benchmark discussion pp. 5-6, hardware/discussion p. 7, and limitations p. 8; metadata/abstract checked; short excerpts matched on cited PDF pages; selected prose numbers checked; no whole-paper or rendered-table audit; excerpts checked mechanically against the MinerU transcription | corrections: new English follow-up card; omitted unverified percentage/table values; retained learned-candidate limitation, single-run evidence, continued-path delay behavior, and distinction between semantic traversability and pose uncertainty; abstract retains the published spacing in of human-like, where MinerU merges ofhuman-like (96% mechanical match)
- Source provenance: newly acquired official publisher PDF and unchanged raw publisher BibTeX, followup-2026-11-02; no legacy extraction was used. Identity: https://ieeexplore.ieee.org/document/10960724/. PDF SHA-256: e49cdb8ed19a6913e9216517587035091d07b2d2b34f0e79caa1fc7705679901.
- Verification level: light is used here for the user-authorized targeted follow-up read, not a full-paper audit; unreviewed sections, proofs, tables, and numerical claims remain unchecked.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

We present a multi-modal trajectory generation and selection algorithm for real-world mapless outdoor navigation in human-centered environments. Such environments contain rich features like crosswalks, grass, and curbs, which are easily interpretable by humans, but not by mobile robots. We aim to compute suitable trajectories that (1) satisfy the environment-specific traversability constraints and (2) generate human-like paths while navigating on crosswalks, sidewalks, etc. Our formulation uses a Conditional Variational Autoencoder (CVAE) generative model enhanced with traversability constraints to generate multiple candidate trajectories for global navigation. We develop a visual prompting approach and leverage the Visual Language Model’s (VLM) zero-shot ability of semantic understanding and logical reasoning to choose the best trajectory given the contextual information about the task. We evaluate our method in various outdoor scenes with wheeled robots and compare the performance with other global navigation algorithms. In practice, we observe an average improvement of 20.81% in satisfying traversability constraints and 28.51% in terms of human-like navigation in four different outdoor navigation scenarios.
