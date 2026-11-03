# OpenIN: Open-Vocabulary Instance-Oriented Navigation in Dynamic Domestic Environments

## Metadata

| Field | Value |
|---|---|
| ID | E44 |
| Title | OpenIN: Open-Vocabulary Instance-Oriented Navigation in Dynamic Domestic Environments |
| Authors | Yujie Tang, Meiling Wang, Yinan Deng, Zibo Zheng, Jingchuan Deng, Sibo Zuo, and Yufeng Yue |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 9, pp. 9256-9263 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3592071](https://doi.org/10.1109/lra.2025.3592071) |
| Official URL | https://ieeexplore.ieee.org/document/11091457/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-OpenIN-E44/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-OpenIN-E44/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2025-OpenIN-E44/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware, cloud-model, scripted-scenario
- platform_class: wheeled-unspecified
- platform: Autolabor robot (model and drive type not stated; four wheels visible in Fig. 6); simulated agent in Habitat on Gibson scenes
- boundary_platform: no
- degradation: scene-change
- degradation_observed: visual-degradation
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: RGB-D camera (Azure Kinect DK on hardware) plus text and optional image instruction; Livox Mid-360 LiDAR for SLAM pose on hardware
- compute: not reported; GPT-4o queried for carrier selection, image comparison, and image-to-text; no timing reported
- compute_location: not-reported
- summary_result: In 20 Habitat five-target tasks, fifth-target SR was 60-100% versus at most 60% for VLFM and OpenFMNav variants; all five targets in sequence succeeded in 0-60% per scene.
- summary_limitation: On the real robot, missing depth on low-reflectivity or small objects and motion blur, which clean simulation avoids, plus occlusions or blind spots, caused CRSG update or recognition failures.
- survey_included: yes
- verification_level: full

## Problem

Frequently used household objects (cups, bottles, boxes) change position, have
several instances of the same category, and change their carriers (the tables
or chairs they stand on). The paper asks how a robot can navigate to one
specific instance named by text, an image, or both, when the instance may have
moved since the scene was mapped, and how the robot can keep its scene memory
up to date during long sequences of such tasks (pp. 1-2). The setting is a
known, pre-mapped home: an initial scene graph must exist before navigation
(p. 4).

## Mechanism

Offline, an instance-level open-vocabulary point-cloud map is built from
pre-collected RGB-D data, in the style of ConceptGraphs, with a caption list
per instance from Tokenize Anything and an SBERT text feature (p. 2). The
Carrier-Relationship Scene Graph (CRSG) has building, room, carrier, and
carried layers (p. 3). Rooms come from a boundary trace along projected wall
and door points. Carrier candidates are objects whose SBERT feature is similar
to "furniture for holding objects"; the k = 3 most frequent captions go to
GPT-4o with a prompt, and size and ground-contact rules give the final carrier
layer (p. 3). An object is carried by a carrier when four geometric rules hold
(bottom below the carrier top plus 0.1 m, XY center within a 0.02 m margin,
footprint at most 1.2 m, and distance to the carrier cloud below 0.3 m; p. 3).
GPT-4o also writes functions that derive spatial relations such as "next to".

Online, CropFormer, Tokenize Anything, and SBERT process each RGB frame
(p. 3). Observed carriers are matched to the graph by size, center distance,
and SBERT similarity; new carriers of known categories are added. Each
carrier has an existence confidence p updated by exponential smoothing with
alpha = 0.5 whenever the carrier should be visible and unoccluded, and it is
removed below a threshold (p. 4). Carried objects are added, removed, or kept
by the same matching; they are not updated when the partial carrier cloud is
too far away (p. 4).

Navigation is a fixed-policy Markov decision process with the actions Explore
(a carrier), Goto (a candidate), and Stop (p. 4). The state holds the robot
position, unexplored carriers, candidates, and a found flag. When candidates
exist, the robot goes to the one with the highest priority, a product of
SBERT similarity and a depth-confidence term divided by one plus the distance,
with omega_1 = 5, omega_2 = 1, d-tilde = 0.3 m, alpha = 10, beta = 0.1, and a
room weight of 1 (same room) or 0.8 (p. 4). Without candidates, GPT-4o picks
the most plausible carrier from the carriers' captions and the target, weighted
by the existence confidence (p. 5). A carried object is accepted as the target
unless SBERT similarity is below 0.5 or RGB-histogram similarity below 0.4,
and when the mean of SBERT and RGB similarity, or of SBERT and the GPT-4o
image-comparison score, exceeds 0.7; the authors set these thresholds from
"empirical findings" (p. 5). The policy is hand-designed, not learned.

## Baselines and controls

- Offline map queries (Table I): VLMaps and ConceptGraphs (p. 5).
- Long-horizon navigation (Table II, Fig. 5): VLFM and OpenFMNav (Ofm) with
  detection thresholds 0.4, 0.55 (the official implementation), and 0.7
  (p. 6). Both are online exploratory methods and use text input only, while
  OpenIN can also use the target image and starts from an initial CRSG
  (p. 6). The comparison therefore differs in inputs and prior map, not only
  in the policy.
- Ours-w/o-u, which uses the initial CRSG for every target without updates,
  is compared in SPL only, in Fig. 5 plots without numbers (p. 6).
- Goal-determination ablation in scene 4 (Table III): without GPT-4o, without
  text features, without RGB histograms (p. 7).
- Navigation-strategy ablation (Table IV): only-carriers_Random (random
  carrier, no candidates) and only-carriers_LLM (MLLM-chosen carrier, no
  candidates), single-instance tasks in three scenes (p. 7).

## Platform and setup

Simulation: Habitat with Gibson scenes. Table I uses 85 queries over 5 Gibson
scenes, 17.65% semantic, 49.41% instance, and 32.94% demand queries (p. 5);
the paper does not say whether the pre-collected RGB-D for these maps was
rendered in Habitat. Table II uses 4 scenes (labeled 2-5), 5 long-horizon
tasks per scene and 20 in total; each task has exactly 5 sequential targets,
each a displaced object or a new object absent from the initial CRSG, with
same-category distractors placed in each scene, and item positions randomly
altered before the runs (p. 6). Table III is scene 4 only, with an unstated
task count; Table IV uses three scenes and an unstated task count (p. 7).

Hardware: an Autolabor robot with a Livox Mid-360 LiDAR for SLAM-based global
pose and an Azure Kinect DK for RGB-D, with path planning and obstacle
avoidance by ROS move_base, in two indoor scenarios with different carrying
surfaces; everyday items were placed on tabletops (p. 8; Fig. 6, p. 7). The
drive type is not stated; Fig. 6 shows a four-wheel robot, so the coding is
wheeled-unspecified. The number of real runs and any success count are not
reported; Fig. 7 shows one successful two-target sequence (p. 7).

SR and SPL are defined (p. 5), but the paper does not state the success
distance threshold or stopping rule that decides whether the robot reached a
target, and gives no step or time budget.

## Evidence type and transfer

The tabulated results (Tables I-IV, Fig. 5) are all simulation or offline map
queries. The real-robot section reports failure modes and one illustrated
success without metrics, so the closed-loop-hardware coding rests on a
qualitative demonstration (video-only-hardware). The displacement of objects
and the new or removed tables are staged by the experimenters in both
settings. GPT-4o is a hosted model, so the method depends on a remote model
query at run time; the paper does not describe the access.

## Sensors

RGB-D input (simulated in Habitat; Azure Kinect DK on hardware) feeds
segmentation, captioning, and the point-cloud graph. The target is given as
text, an image, or both; an image alone is converted to text by GPT-4o
(p. 4). On hardware, a Livox Mid-360 LiDAR provides SLAM-based global pose
(p. 8). No ground-truth sensor is described.

## Compute and latency

The paper reports no processor, GPU, frame rate, per-module runtime, GPT-4o
latency, or query cost, and does not say where perception, graph updates,
and planning run on the hardware. GPT-4o is queried for carrier
identification, spatial-relation functions, carrier selection, image-to-text
conversion, and image comparison (pp. 3-5).

## Key quantitative results

- Offline query success, OpenIN versus ConceptGraphs and VLMaps: 82.4% (70/85) versus 52.9% (45/85) and 43.5% (37/85); OpenIN is highest in each of the 5 scenes, for example 13/14 versus 9/14 and 7/14 in scene 1 and 13/18 versus 8/18 and 6/18 in scene 5. This is retrieval accuracy on a map, not robot arrival (p. 5, Table I).
- Fifth target, OpenIN SR(5) / Tasks_SR(5) in % over 5 tasks per scene: scene 2 100/40, scene 3 80/20, scene 4 80/60, scene 5 60/0 (p. 6, Table II).
- Fifth target, best baseline SR(5): scene 2 Ofm-0.55 40, scene 3 Ofm-0.4 and Ofm-0.7 60, scene 4 Ofm-0.4 and Ofm-0.55 20, scene 5 Ofm-0.4 and Ofm-0.55 40; VLFM is 0 in all four scenes; every baseline Tasks_SR(5) is 0 (p. 6, Table II).
- First target, OpenIN versus best baseline SR(1): scene 2 80 versus 40 (VLFM), scene 3 60 versus 40 (Ofm-0.7), scene 4 100 versus 40 (Ofm-0.7), scene 5 40 versus 40 (Ofm-0.4 and Ofm-0.7, a tie) (p. 6, Table II).
- Goal-determination ablation, scene 4, fifth target SR / Tasks_SR in %: full method 75.0/50.0 versus w/o GPT-4o 50.0/0.0, w/o text 25.0/25.0, and w/o RGB 25.0/25.0. The w/o text and w/o RGB columns are identical in all five rows (p. 7, Table III).
- Table III mixes denominators: 83.3, 66.7, and 50.0 are multiples of 1/6, while 25.0 and 75.0 are multiples of 1/4; the task count is not stated, and the full-method scene 4 values differ from Table II (for example 83.3/83.3 versus 100/100 at the first target), so Table III is a separate run set (p. 7, Table III; p. 6, Table II).
- Navigation-strategy ablation, SPL: full method 0.342 versus only-carriers_LLM 0.309 and only-carriers_Random 0.205, single-instance tasks in three scenes, count not stated (p. 7, Table IV).
- SPL over the five targets (Fig. 5) generally rises for OpenIN in scenes 2-4 and rises then falls in scene 5; Ours-w/o-u stays low. The comparison is a plot without tabulated values (p. 6, Fig. 5).

## Stated limitations

- Low-reflectivity surfaces and small objects often cause missing depth, which leads to update failures on the real robot (p. 8).
- Motion blur in the RGB-D input leads to inconsistent captions and impaired recognition; a GPT-based caption-similarity comparison is planned as a remedy (p. 8).
- The missing-depth and motion-blur issues do not arise in simulation, where depth and RGB data are clean (p. 8).
- Occlusions or blind spots can prevent targets from being added to the CRSG (p. 8).
- In scene 5, observation blind spots and visually ambiguous targets lower SR and therefore SPL (p. 6, Fig. 5 caption; p. 7).

## Transfer conditions

A wheeled robot such as the reference platform needs an initial CRSG built
from pre-collected RGB-D data of the home, a reliable 3D pose (here LiDAR
SLAM), and a calibrated RGB-D camera whose depth survives dark or reflective
surfaces. The thresholds of the target test and the priority function were
set empirically for the Habitat scenes and may need retuning. The method
calls GPT-4o several times per task, so network access, latency, and cost
must be checked; none is reported. Carrier removal relies on a visibility and
occlusion check, so stale entries can persist where the camera cannot see.
The "dynamic" setting means objects moved between tasks and tables added or
removed, not moving people or obstacles during a run; obstacle avoidance is
delegated to move_base. The hardware evidence has no success rate, so the
simulation numbers are the only quantitative basis.

## Code and data

The project page is https://OpenIN-nav.github.io (p. 1). Whether it provides
code, task definitions, or data was not verified.

## Version family

No other version of this work is in the library. HOV-SG, ConceptGraphs, and
GOAT are related work or baselines, not versions. Preprint versions were not
checked.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Sec. V-D, p. 8 | "First, low-reflectivity surfaces and small objects often cause depth missing, leading to update failures." |
| C3 | partial-support | moderate | Sec. V-D, p. 8 | "These issues do not arise in simulation, where the depth and RGB data are clean." |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | Sec. I, p. 2 | "Extensive qualitative and quantitative experiments in the simulation and real world demonstrate that updating the CRSG contributes to efficient navigation in tasks involving long sequences of moved instances." |
| C6 | qualifies | moderate | Sec. IV, p. 4 | "Before navigation begins, we assume that an initial CRSG has been constructed as described in Section III-A, which serves as the initialization for the planner." |

## Page-cited excerpts

- **p. 4, Sec. IV.** "Before navigation begins, we assume that an initial CRSG has been constructed as described in Section III-A, which serves as the initialization for the planner."
  The method starts from an offline scene graph; it is not exploration of an unknown home.
- **p. 6, Sec. V-B.** "In contrast, both Vlfm and Ofm rely solely on text input."
  The baselines receive less input than OpenIN, which can also use the target image.
- **p. 8, Sec. V-D.** "Path planning and obstacle avoidance were handled using the ROS move_base package."
  Motion on the real robot comes from a standard ROS stack; OpenIN chooses the goals.
- **p. 8, Sec. V-D.** "Despite these challenges, our system achieved success in various test cases."
  The hardware result is stated qualitatively; no trial count or success rate is given.
- **p. 8, Sec. V-D.** "Third, occlusions or blind spots can prevent target objects from being updated to the CRSG."
  Graph maintenance depends on what the camera sees; the authors name it as a failure mode.

## Survey-usable statements

### Supported

- In Habitat long-horizon tasks with displaced and new objects (5 tasks of 5 targets in each of 4 Gibson scenes), OpenIN reached the fifth target in 60-100% of tasks per scene, against at most 60% for VLFM and OpenFMNav, which used text only and no prior map.
- Updating a carrier-relationship scene graph during a task sequence generally raised SPL over later targets in three of four scenes, compared with a variant that uses only the initial graph (plots only).
- Instance queries on an offline map succeeded in 82.4% of 85 queries for OpenIN against 52.9% for ConceptGraphs and 43.5% for VLMaps, highest in each scene.
- Real-world failure modes named by the authors are missing depth on low-reflectivity or small objects, motion blur, and occlusions or blind spots.

### Not supported

- OpenIN has the highest SR and Tasks_SR for every target in every scene, as the text says (p. 6): SR is beaten in 2 of 20 scene-target cells (scene 3 target 2, Ofm-0.55 80 versus 60; scene 5 target 2, Ofm-0.7 80 versus 60) and tied for best in scene 5 target 1 (Ofm-0.4 and Ofm-0.7, 40/40); Tasks_SR is never beaten but is tied in scene 3 target 2 (Ofm-0.55, 20), scene 5 target 1 (40), scene 5 target 4 (Ofm-0.7, 20), and scene 5 target 5 (all 0) (p. 6, Table II).
- OpenIN completes long task sequences reliably: all five targets in sequence succeeded in 0 of 5 tasks in scene 5 and in 1 of 5 in scene 3 (p. 6, Table II).
- OpenIN achieves a stated success rate on the real robot: no real trial count, success rate, path length, or time is reported.
- OpenIN runs onboard or in real time: no hardware, runtime, or GPT-4o latency is reported.
- OpenIN navigates unknown homes: it requires an initial CRSG built from pre-collected RGB-D data (p. 4).
- The success rates use a stated arrival threshold: the paper does not define the distance or stopping rule for success.

## Verification log

- 2026-10-30 | host: Kiro | scope: full text read; Tables I and IV and Fig. 5 read from the rendered p. 5-7 images, Table II from a 4x crop of p. 6, Table III from the rendered p. 7 image, Figs. 6-7 and p. 8 checked | corrections: format converted to the English template; Table II counterexamples to the "highest everywhere" claim added; Table III denominator inconsistency recorded; missing success threshold and hardware trial count stated; coding added; deep-review round 1: summary_limitation and Stated limitations scope the "do not arise in simulation" statement to missing depth and motion blur (see tmp/corrections/E44.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/b275f6876be9fde7171b1b22/

## Original abstract

In daily domestic settings, frequently used objects like cups often have unfixed positions and multiple instances within the same category, and their carriers also frequently change. As a result, it becomes challenging for a robot to efficiently navigate to a specific instance. To tackle this challenge, the robot must capture and update scene changes and plans continuously. However, current object-navigation approaches primarily focus on the semantic level and lack the ability to dynamically update the scene representation. In contrast, this paper captures the relationships between frequently used objects and their static carriers. It constructs an open-vocabulary Carrier-Relationship Scene Graph (CRSG) and updates the carrying status during robot navigation to reflect the dynamic changes of the scene. Based on CRSG, we further propose an instance navigation strategy that models the navigation process as a Markov Decision Process. At each step, decisions are informed by the Large Language Model’s commonsense knowledge and visual-language feature similarity. We designed a series of long-horizon navigation tasks for frequently used everyday items in the Habitat simulator. The results demonstrate that by updating the CRSG, the robot can navigate efficiently to moved targets. Additionally, we conducted extensive experiments on a real robot, demonstrating the effectiveness of our method and exploring its limitations.
