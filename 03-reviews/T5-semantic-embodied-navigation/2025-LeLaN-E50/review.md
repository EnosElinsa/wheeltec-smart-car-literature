# LeLaN: Learning A Language-Conditioned Navigation Policy from In-the-Wild Video

## Metadata

| Field | Value |
|---|---|
| ID | E50 |
| Title | LeLaN: Learning A Language-Conditioned Navigation Policy from In-the-Wild Video |
| Authors | Noriaki Hirose, Catherine Glossop, Ajay Sridhar, Oier Mees, and Sergey Levine |
| Venue | Proceedings of The 8th Conference on Robot Learning, PMLR 270, pp. 666-688 |
| Year | 2025 (conference 2024) |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v270/hirose25b.html |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-LeLaN-E50/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-LeLaN-E50/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2025-LeLaN-E50/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, dataset-playback
- protocol_caveats: scripted-scenario, few-trials
- platform_class: differential-drive
- platform: prototype mobile robot on an iRobot Roomba base (Fig. 9); Unitree Go1 quadruped in qualitative cross-embodiment tests only
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: compute-limit
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: single RGB image from the front fisheye lens of a Ricoh Theta S, plus a text instruction
- compute: Nvidia Jetson Orin AGX onboard; 0.054 s to generate one action
- compute_location: onboard
- summary_result: With targets visible at the start, LeLaN reached within 0.2 m in 89% of 150 real-robot trials versus 67% for the strongest baseline, at 0.054 s per action onboard.
- summary_limitation: The policy confuses identical objects under spatial instructions, and the authors call its reaching rate with obstacles (0.60 in 15 experiments, with J_col) insufficient for practical use.
- survey_included: yes
- verification_level: full

## Problem

LeLaN targets language-conditioned object navigation in the "last-mile"
setting: the target object is visible from the robot's start pose, and the
robot must reach it precisely while following instructions that may be simple,
noisy, or describe the object through nearby objects (pp. 2-3). The authors
argue that navigation lacks datasets with both language and action labels,
and that zero-shot use of large foundation models is often too expensive for
edge compute (p. 2). The paper asks whether unlabeled, action-free egocentric
video (robot logs, YouTube tours, and human walking video) can be labeled
automatically with foundation models and used to train a small policy that
runs onboard. Searching for objects that are not in view is outside the main
task; the authors state that the policy could be paired with a learned or
classical search system (p. 2).

## Mechanism

Labeling runs offline (Sec. 3.1, Fig. 2, Appendix A). Segment Anything
produces masks and bounding boxes for each frame. Each crop goes to an
open-source VLM (reference [53], CogVLM) for a description, and GPT-3.5-turbo
decides whether the VLM confidently detected an object and writes several
instructions of the form "Go to X" (p. 3). The authors chose this split
because, at submission time, closed-source VLMs were costly and slow and
open-source VLMs gave poor prompts (p. 3). The 3D object position is the
median of a point cloud from monocular depth (Metric3D for narrow-FOV images,
Depth360 for wide-FOV images), masked by the Segment Anything mask, an
approach similar to CoW (p. 3). Collision-avoiding action labels come from the
navigation foundation model NoMaD, fine-tuned so that a crop of the current
image can serve as its goal image; a crop replaces the goal image for fifty
percent of each batch (p. 14).

The policy (Sec. 3.2, Appendix F) encodes the instruction with a frozen CLIP
ViT-B32 text encoder, conditions a ResNet-FiLM visual encoder (trained from
scratch) on it, adds EfficientNet-B0 features of the current and previous
observations, and passes them through a Transformer and an MLP that output 24
pairs of linear and angular velocity (p. 18, Fig. 8). A differentiable
kinematic model integrates the velocities into 2D virtual poses. The loss is
J_pose, the squared error between the final pose and the object position
projected to the horizontal plane, plus J_col, the squared error to the NoMaD
trajectory, plus J_smooth, the squared change between consecutive velocity
commands (p. 4, Eq. 1). J_col is masked out near the target; Sec. 3.2 writes
the condition as the projected object position being below 1.0, with no unit
(p. 5), and Appendix G.1 calls it a certain distance threshold (p. 18). When
J_col is used, the policy is pre-trained without it, fine-tuned with it, and
given an image history; training uses L = 1, that is, one previous
observation (pp. 14, 18). Training draws 256 observations per batch and uses
Adam with a learning rate of 0.0001 (p. 18). At run time the instruction is
encoded once at the start, the policy is recomputed at the best frame rate,
and only the first velocity command of each predicted sequence is executed,
as in receding-horizon control (p. 19).

## Baselines and controls

All four baselines were re-implemented by the authors and restricted to the
last-mile task (Appendix H, pp. 19-20):

- CoW with the OWL-ViT B/32 detector, Depth360 monocular depth, and a state lattice planner; the exploration part of CoW is not implemented (p. 19).
- OWL-v2 + ZoeDepth with the same state lattice planner; the larger patch size of OWL-v2 makes it slower than CoW (p. 20).
- OWL-ViT + ViNT, where the crop from the OWL-ViT box is the ViNT goal image (p. 20).
- OpenFMNav modified for last-mile navigation: GPT-4o lists candidate objects, a VLM identifies objects in the observation, Grounded-SAM segments them, and Depth360 with the same lattice planner drives the robot. Of two versions, the authors use the one in which inference runs only on the initial observation and the planner then takes over, because the per-observation version was very slow and performed worse (p. 20). The paper does not say how GPT-4o was accessed; GPT-4o is a closed model, so this step cannot have run on the robot's Orin.

The state lattice planner uses 15 motion primitives of constant linear and
angular commands over 8 steps (2.664 s), a goal-distance cost, and a penalty
of 1000.0 for primitives that come closer to the estimated obstacle point
cloud than the robot radius; the obstacle points come from monocular depth of
the same RGB image (p. 23). Internal controls are three data mixtures of
LeLaN in Tables 2 and 4 (YT 0.0% and HW 0.0%, YT 20.0% and HW 43.5%, YT 100.0%
and HW 100.0%), the J_col ablation in Table 3, the encoder ablation in Table 5,
and the data-volume ablation in Fig. 5. The policies in Tables 2 and 4 are the
simplest version, without J_col and without image history (L = 0) (p. 5).

## Platform and setup

Training data (Table 1, p. 5): the Indoor Navigation Dataset has 31.0 h of
autonomous and teleoperated robot trajectories from GS2 (17.6 h), GS4
(10.5 h), and SACSoN/HuRoN (2.9 h), with 111570 images; the YouTube Tour
Dataset has 82.5 h (593727 images) from 32 countries; the Human-walking
Dataset has 15.7 h (113277 images) recorded by walking with a handheld fisheye
camera in 11 cities in 3 countries. YouTube and walking data are sampled at
2 FPS. The data volume is stated differently across the paper: "over 130
hours" in the abstract (p. 1), "over 120 hours" released in the contribution
list (p. 2), and "over 100 hours" in the conclusion (p. 8); the Table 1 rows
add up to slightly less than 130 h. Training ran on a workstation with an
Intel i9 CPU, 96GB RAM, and an NVIDIA RTX 4090 GPU (p. 18).

Robot (Appendix G.2, p. 19): a prototype mobile robot. The labels in the
Fig. 9 image name an iRobot Roomba mobile base, an Nvidia Orin AGX robot
controller, a Ricoh Theta S omnidirectional camera, and a Krisdonia NJF-5X
power bank; these labels were read from the figure image, not from the text
layer. Only the front fisheye lens of the Theta S is used. Robot speed limits
are not reported.

Main evaluation (Sec. 4.1, Table 2, p. 6): 28 objects or structures, with 5
or 6 instructions per object, of which two are simple and the rest noisy
(wrong adjectives, long prompts, or no object noun) (p. 16). Each method has
150 trials, and a trial succeeds when the robot reaches within a 0.2 m radius
of the target; the seven rows of Table 2 make up the "over 1050 evaluations"
(p. 6). When identical objects cannot be told apart by the prompt, reaching
any matching object counts as success (p. 16). The environment description is
inconsistent: Sec. 4.1 names five environments, 3 indoor floors and 2 outdoor
spaces (p. 6), while Appendix E places 18 objects on a university campus and
10 in a home environment (p. 16), and Table 4 splits the results into office
floor, entrance hall, home environment, and outside (p. 15).

Additional settings (Sec. 4.2, p. 7): six dynamic objects that are moved after
the robot starts, reported as a column of Table 2; 15 navigation experiments
with obstacles between robot and target (Table 3); and long-distance
navigation with a topological memory recorded beforehand by teleoperation,
OWL-v2 node scoring, ViNT, and a switch to LeLaN at the selected node (p. 22).
Cross-embodiment tests (Sec. 4.3, Fig. 4, pp. 7-8) use a Unitree Go1
quadruped with a different fisheye camera and the same wheeled robot with a
PCB-mounted fisheye camera, a narrow-FOV Intel D435i, or a spherical camera
mounted higher. The Fig. 4 caption speaks of three types of experiments but
lists four setups. Long-distance and cross-embodiment results are shown only
in supplemental videos.

## Evidence type and transfer

Tables 2 to 4 are closed-loop hardware results: the policy drives the robot,
and no prior map is used. They show last-mile reaching of a visible target on
one Roomba-based robot with one camera, in campus and home scenes, with 150
trials per method and no confidence intervals or significance tests. Two
tabulated settings are staged and small. The six dynamic objects are moved
after the robot starts navigating (p. 7); the column values (0.83, 0.33, 0.17,
and 0.00) fit one trial per object (5/6, 2/6, 1/6, 0/6), but the trial count
is not stated. In Table 3 the 15 experiments belong to the with-obstacle
column, whose values fit 15 runs (9/15, 2/15, 6/15). The trial count of the
without-obstacle column is not stated: 0.77 is not a multiple of 1/15, and
the values for OWL-v2 + ZoeDepth (0.67) and for LeLaN without J_col (0.89)
equal the Table 2 totals, with no statement on whether those trials were
reused. These two settings are the basis of the scripted-scenario and
few-trials codes. Table 3 does not restate the success radius or how
collisions are scored.

All methods run on the same onboard computer, which is fixed, not varied, so
limited onboard compute is coded as observed rather than designed. The paper
reports its effects: the OWL-v2 + ZoeDepth baseline often fails in the
obstacle runs because of its slow inference (p. 7), and a larger text encoder
lowered the frame rate on the robot (pp. 15-16).

Fig. 5 and Table 5 are offline evaluations on a held-out test dataset of the
labeled data, measured as mean square error between the generated pose and
the target; the composition of that split is not described. Long-distance
navigation, which uses a topological memory recorded by teleoperation
(p. 22), and cross-embodiment transfer are side demonstrations shown only in
supplemental videos, with no tabulated metrics. They show feasibility only
and are not coded as protocol caveats. The baselines are reduced versions of
their original systems, so the comparison ranks last-mile pipelines, not the
full CoW or OpenFMNav systems.

## Sensors

The policy uses one RGB image from the front fisheye lens of a Ricoh Theta S
and the text instruction; it uses no depth camera, LiDAR, or odometry
(p. 19). Monocular depth (Metric3D, Depth360) appears only in labeling, and
the baselines estimate depth from the same RGB image (Depth360 or ZoeDepth)
for a fair comparison (pp. 3, 19). Cross-embodiment tests swap in a
PCB-mounted fisheye camera, an Intel D435i used as a narrow-FOV camera, and a
spherical camera at a greater height (p. 19). How success within 0.2 m was
measured is not described.

## Compute and latency

The policy runs on the robot's Nvidia Orin AGX (Appendix G.2; the Table 2
caption says Nvidia Jetson Orin). The inference time in Table 2 is the time to
generate an action given the current observation: 0.054 s for LeLaN, 0.22 s
for CoW, 0.33 s for OWL-ViT + ViNT, 2.82 s for OWL-v2 + ZoeDepth, and 22.0 s
for OpenFMNav, which runs inference only on the initial observation (p. 6).
The OpenFMNav pipeline queries GPT-4o (p. 20), a closed model that cannot run
on the Orin; the paper does not say how it was accessed, so the 22.0 s is not
a purely onboard time. This concerns a baseline: compute_location codes
LeLaN's own setting, which is onboard. The paper describes LeLaN as 4 times
faster than the fastest baseline, CoW (p. 7). The timing excludes camera
capture, actuation, and end-to-end loop latency, and no control rate is
reported. A larger CLIP text encoder increased the computational load,
reduced the frame rate, and increased battery consumption on the robot, so
the ViT-B32 text encoder was kept (pp. 15-16). Labeling with CogVLM and
GPT-3.5-turbo happens before training and is not part of the evaluated loop.
Parameter count, training time, and the cost and time of labeling are not
reported.

## Key quantitative results

- Success within 0.2 m over 150 trials with 28 objects: LeLaN trained on all data 0.89 versus OWL-v2 + ZoeDepth 0.67, CoW 0.58, OWL-ViT + ViNT 0.47, and OpenFMNav 0.43 (p. 6, Table 2).
- Noisy prompts 0.88 versus 0.63 for OWL-v2 + ZoeDepth; simple prompts 0.91 versus 0.73 for CoW and OWL-v2 + ZoeDepth; multiple-object prompts 0.81 versus 0.62 (p. 6, Table 2).
- Dynamic objects moved after the start (six objects; trial count not stated): 0.83 versus 0.33 for OWL-ViT + ViNT, 0.17 for CoW, and 0.00 for OpenFMNav and OWL-v2 + ZoeDepth (p. 6, Table 2; p. 7).
- Trained on indoor robot data only, LeLaN reaches 0.65 overall, below OWL-v2 + ZoeDepth at 0.67; adding YT 20.0% and HW 43.5% raises it to 0.85 (p. 6, Table 2).
- Time to generate one action on Jetson Orin: 0.054 s for LeLaN versus 0.22 s for CoW, 0.33 s for OWL-ViT + ViNT, 2.82 s for OWL-v2 + ZoeDepth, and 22.0 s for OpenFMNav on the initial observation only; the OpenFMNav pipeline includes a GPT-4o query whose access is not described (p. 6, Table 2; p. 20).
- With obstacles, in 15 experiments: arrival rate 0.60 for LeLaN with J_col versus 0.13 for LeLaN without J_col and 0.40 for OWL-v2 + ZoeDepth with its collision-aware planner. Without obstacles: 0.77 versus 0.89 and 0.67, with no stated trial count; 0.89 and 0.67 equal the Table 2 totals (p. 7, Table 3).
- Per environment, full-data LeLaN versus OWL-v2 + ZoeDepth: office floor 0.96 versus 0.65, entrance hall 0.85 versus 0.57, home environment 0.87 versus 0.77, and outside 0.87 versus 0.67 (p. 15, Table 4).
- Trained on indoor robot data only, LeLaN reaches 0.53 in the home environment versus 0.77 for OWL-v2 + ZoeDepth (p. 15, Table 4).
- On the offline test set, the two ResNet-FiLM configurations give mean square errors of 1.291 and 1.202, against 1.690 and 1.673 with pre-trained CLIP visual encoders; the text attributes the small gain to the larger text encoder (p. 16, Table 5).
- Test-set pose error stops improving around 100K frames of Indoor Navigation or Human-walking data, while YouTube data keep improving it beyond 100K frames, with the best policy at over 500K frames; values are only plotted (p. 8, Fig. 5).

## Stated limitations

- The policy has trouble telling multiple copies of the same object apart by spatial reasoning alone; with two doors and an instruction to go to the leftmost door, it often gets confused (p. 8).
- Collision avoidance remains a challenging task for language-conditioned navigation policies (p. 8); the target reaching rate is not sufficient for practical use, and reliable collision avoidance with precise language-conditioned navigation remains a challenge (p. 19).
- Weighting goal reaching against collision avoidance needed trial and error; a much larger J_col weight degrades goal reaching (p. 18).
- Near the target, NoMaD pushes the robot away from the object and can prevent it from being reached, so J_col is masked close to the goal (p. 14).
- LeLaN is designed for last-mile navigation and assumes that the target is seen at the initial position; long-distance navigation needs an added topological memory (p. 7).
- A wide-FOV camera is generally better for reducing blind spots and easing object detection (p. 19).

## Transfer conditions

A wheeled robot that reuses LeLaN needs a base that accepts linear and angular
velocity commands, a camera with a field of view close to the training data
(the authors favor wide FOV), and an onboard GPU in the Jetson Orin class to
reach the reported 0.054 s per action. The speed range, camera height, and
camera calibration of the evaluated robot are not reported, so the velocity
scaling of the policy has to be checked on the target platform. The target
must be visible from the start; objects out of view need a separate search or
a teleoperated topological map. With J_col the arrival rate in the 15 obstacle
experiments is 0.60, so a separate safety layer is needed. The robot training
data come from office buildings (GS2, GS4, SACSoN), and home and outdoor
coverage comes from YouTube and walking video. Cross-embodiment transfer is
shown only qualitatively.

## Code and data

The project page is https://learning-language-navigation.github.io/ (p. 1).
The paper states that the models and datasets are open-sourced and lists the
YouTube source URLs in Appendix I. The PDF names no code repository.
Repository contents, licenses, and data availability were not verified.

## Version family

The PMLR record and the BibTeX title end in "In-the-Wild Video", while the
PDF title ends in "In-the-Wild Videos". The abstract in the BibTeX export
differs from the PDF abstract and gives a smaller data volume and no trial
count. The PDF footer names the 8th Conference on Robot Learning (CoRL 2024),
Munich, Germany. An arXiv version was not checked. NoMaD, ViNT, SACSoN, and
ExAug, by overlapping authors, are separate works used here as components,
data sources, or references. The library counts this PMLR paper once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Sec. 4.2, p. 7 | "Due to its robust performance and fast inference speed, our method significantly outperforms the baselines as shown in Table 2." |
| C3 | direct-support | strong | Appendix G.1, p. 19 | "reliable collision avoidance with precise language-conditioned navigation is a remaining challenge for our method." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Appendix G.2, p. 19 | "a wide FOV camera is generally better for reducing blind spots and making object detection easier." |

## Page-cited excerpts

- **p. 2, Sec. 2.** "we focus on the case where the object is within the line of sight of the robot"
  The task excludes search; the results do not cover finding objects out of view.
- **p. 3, Sec. 3.1.** "while the open-source VLMs resulted in poor quality prompts"
  The split between VLM description and LLM prompting was a cost and quality choice at submission time, not a tested design.
- **p. 6, Table 2.** "Success is determined by the robot reaching within a 0.2 [m] radius of the target object."
  All success rates in Tables 2 and 4 use this radius; Table 3 does not restate it.
- **p. 6, Sec. 4.1.** "Our method achieves an average success rate of 89% compared to 67%, the performance of the strongest baseline."
  The headline result is for the model without J_col and without image history, on targets visible from the start.
- **p. 7, Sec. 4.2.** "We conduct 15 navigation experiments for different target"
  The 15 experiments are the with-obstacle column of Table 3; the trial count of the without-obstacle column is not stated.
- **p. 7, Sec. 4.2.** "This baseline often fails navigation due to its slow inference speed."
  The obstacle comparison partly reflects the 2.82 s per action of OWL-v2 + ZoeDepth, not only the quality of its planner.
- **p. 7, Sec. 4.2.** "The LeLaN is designed for last-mile navigation, which assumes that the target object is seen at the initial robot position."
  Long-distance use depends on an added topological memory and has no reported metrics.
- **p. 7, Sec. 4.2.** "We evaluate our method and the baselines on object navigation with six dynamic objects."
  The dynamic-object column of Table 2 rests on six objects; the number of trials per object is not stated.
- **p. 7, Sec. 4.2.** "The relatively small network size allows us to implement our policy at a higher frame rate onboard (4 times faster than the fastest baseline, CoW)"
  The speed claim compares per-action computation on the same onboard computer, not end-to-end latency.
- **p. 8, Sec. 5.** "our policy has trouble distinguishing between multiple copies of the same object using spatial reasoning alone."
  Spatial-relation instructions among identical objects are a stated failure case.
- **p. 14, Appendix A.** "As the robot approaches the object, the NoMaD policy will more strongly push the robot to avoid the object to avoid collision, sometimes preventing the object from being reached."
  The distilled collision-avoidance teacher conflicts with goal reaching near the target, which explains the masking of J_col.
- **p. 15, Appendix B.** "even with just the Indoor Navigation dataset, which does not include at-home and outdoor data, our method still exhibits a clear performance gap between the baselines."
  Table 2 gives 0.65 for this model against 0.67 for OWL-v2 + ZoeDepth, so the statement holds only against the three weaker baselines overall and on the office floor.
- **p. 19, Appendix G.2.** "We calculate the control policy on the edge robot controller, Nvidia Orin AGX, with the best frame rate for each method."
  LeLaN and the detector-based baselines run on the onboard Orin; the GPT-4o step of OpenFMNav cannot run there, and the paper does not say how it was accessed.
- **p. 19, Appendix G.2.** "Our policy works well across these various camera configurations, but a wide FOV camera is generally better for reducing blind spots and making object detection easier."
  The camera swaps are reported without metrics, and the authors attach a preference for wide-FOV cameras to transfer.
- **p. 19, Fig. 9.** "Note that we only use the front side camera of the omnidirectional camera, Ricoh Theta S, to navigate the robot."
  The policy input is one fisheye RGB view; no depth or range sensor is used.
- **p. 20, Appendix H.** "the language instruction is fed into a VLM, in this case GPT-4o, to generate a list of potential objects to look for in the scene"
  The OpenFMNav baseline depends on GPT-4o, so its 22.0 s inference time is not a purely onboard figure.
- **p. 22, Appendix J.** "we collect the topological memory (a sequence of images) by teleoperating through the environment."
  Long-distance navigation needs a teleoperated prior traversal of the environment.

## Survey-usable statements

### Supported

- Automatic labeling of action-free video with Segment Anything, a VLM, an LLM, monocular depth, and NoMaD trained a language-conditioned last-mile policy that reached visible targets within 0.2 m in 89% of 150 real-robot trials, against 67% for the strongest re-implemented baseline.
- A small RGB-only policy needed 0.054 s per action on a Jetson Orin, against 0.22 s to 2.82 s for detector pipelines on the same computer, and 22.0 s for a GPT-4o-based pipeline whose model access is not described.
- Adding YouTube and walking video to indoor robot data raised real-robot success from 0.65 to 0.89 in Table 2.
- Distilling NoMaD collision avoidance raised the arrival rate in 15 obstacle experiments from 0.13 to 0.60; without obstacles the rate was 0.77 versus 0.89 without distillation (trial count not stated).

### Not supported

- LeLaN solves object search or long-distance navigation in unseen environments: long-distance runs need a teleoperated topological memory and have no metrics.
- LeLaN transfers across embodiments with measured success: the Go1 and camera-swap tests are qualitative only.
- LeLaN navigates safely among obstacles: the arrival rate in 15 obstacle experiments is 0.60, and the authors call the reaching rate insufficient for practical use.
- Indoor robot data alone already beat the strongest baseline: Table 2 gives 0.65 against 0.67, despite the claim in Appendix B.
- The 89% result was achieved together with collision avoidance: the Table 2 model has no J_col.
- LeLaN outperforms the full CoW or OpenFMNav systems: both were re-implemented without their exploration parts.
- Every pipeline in the Table 2 timing comparison ran entirely on the Jetson: the OpenFMNav pipeline queries GPT-4o, and the paper does not say how it was accessed.
- LeLaN follows moving targets reliably: the dynamic-object result rests on six objects with no stated trial count.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read (Secs. 1-5 and Appendices A-K); Tables 1-5 and captions of Figs. 4, 5, and 9 checked against the PDF; Fig. 9 labels read from the figure image; independent fact-check applied | corrections: rebuilt in English template format; unsupported GitHub link and arXiv identifier removed; computed data total replaced by the paper's own totals; mask unit and trial wording corrected; environment inconsistency recorded; Table 3 trial count limited to the with-obstacle column; GPT-4o pipeline no longer described as onboard; protocol caveats limited to the tabulated settings; compute-limit moved to observed conditions; C6 excerpt replaced; Year in conference format (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/a9047efc33b88dcd9909fc6b/

## Original abstract

The world is filled with a wide variety of objects. For robots to be useful, they need the ability to find arbitrary objects described by people. In this paper, we present LeLaN (Learning Language-conditioned Navigation policy), a novel approach that consumes unlabeled, action-free egocentric data to learn scalable, language-conditioned object navigation. Our framework, LeLaN leverages the semantic knowledge of large vision-language models, as well as robotic foundation models, to label in-the-wild data from a variety of indoor and outdoor environments. We label over 130 hours of data collected in real-world indoor and outdoor environments, including robot observations, YouTube video tours, and human walking data. Extensive experiments with over 1000 real-world trials show that our approach enables training a policy from unlabeled action-free videos that outperforms state-of-the-art robot navigation methods, while being capable of inference at 4 times their speed on edge compute. We open-source our models, datasets and provide supplementary videos on our project page.
