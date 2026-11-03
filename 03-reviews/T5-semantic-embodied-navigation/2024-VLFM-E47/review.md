# VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation

## Metadata

| Field | Value |
|---|---|
| ID | E47 |
| Title | VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation |
| Authors | Naoki Yokoyama, Sehoon Ha, Dhruv Batra, Jiuguang Wang, and Bernadette Bucher |
| Venue | 2024 IEEE International Conference on Robotics and Automation (ICRA), pp. 42-48 |
| Year | 2024 |
| Type | conference |
| DOI | [10.1109/icra57147.2024.10610712](https://doi.org/10.1109/icra57147.2024.10610712) |
| Official URL | https://doi.org/10.1109/icra57147.2024.10610712 |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2024-VLFM-E47/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2024-VLFM-E47/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2024-VLFM-E47/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware
- platform_class: legged
- platform: Boston Dynamics Spot with arm (real world); Habitat simulated agent (benchmarks)
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: RGB-D camera and planar odometry (simulation); Spot gripper RGB camera, Spot body depth cameras, and ZoeDepth monocular depth (real world)
- compute: real-world models on a laptop RTX 4090 MaxQ Mobile GPU with 16 GB VRAM, "real-time"; no per-frame timing; simulation hardware not reported
- compute_location: not-reported
- summary_result: Habitat ObjectNav SPL/SR, success = STOP within 1 m in 500 steps: 52.2/84.0 Gibson, 30.4/52.5 HM3D, 17.5/36.4 MP3D versus SemUtil 40.5/69.3, ESC 22.3/39.2 (HM3D), 14.2/28.7 (MP3D).
- summary_limitation: The authors assume targets are visible from the default camera height and the value map is task-specific; single-floor support fails 14.6% (HM3D) and 9.6% (MP3D) of episodes.
- survey_included: yes
- verification_level: full

## Problem

Object Goal Navigation (ObjectNav): a robot must find any instance of a named
object category (for example "bed") in a previously unseen environment,
without a pre-built map, using only an egocentric RGB-D camera and odometry
relative to its start pose (p. 2). The paper asks how a pre-trained
vision-language model can rank exploration frontiers by semantic relevance
without task-specific training, instead of exploring the nearest frontier or
first converting detections into text for a language model (p. 2).

## Mechanism

An episode has three phases: the robot first rotates in place for a full turn
to initialize its maps, then explores, then navigates to a detected target
(p. 2). Depth and odometry build a top-down 2D obstacle map; depth points
that are too short or too tall to be obstacles are filtered out, and the
midpoint of each explored/unexplored boundary is a frontier waypoint (p. 3).
If no frontier remains and no target was detected, the robot calls STOP,
which counts as a failure (p. 3).

A second top-down grid, the value map, has a semantic-value channel and a
confidence channel. BLIP-2 computes a cosine similarity between the current
RGB image and the prompt "Seems like there is a <target object> ahead.", and
the score is projected into the camera's field-of-view cone, masked by depth
occlusions (p. 3). The confidence of a pixel is cos^2 of its normalized angle
from the optical axis (1 on the axis, 0 at the image edges). When a region is
seen again, its value becomes the confidence-weighted average of the previous
and current values, and the confidence is updated with a weighted average
biased toward the higher confidence (p. 3). The frontier with the highest
value is explored next.

Targets are detected with YOLOv7 for COCO categories and Grounding-DINO for
other categories; MobileSAM extracts the object contour, and depth gives the
closest object point as the goal waypoint (p. 4). In simulation, waypoints
are followed by a PointNav policy trained with Variable Experience Rollout
(VER) on HM3D training scenes, using depth and goal distance and heading but
no RGB (pp. 4-5). On the real robot, the Boston Dynamics (BD) API replaces
the PointNav policy (p. 6).

## Baselines and controls

Zero-shot comparators are CLIP on Wheels (CoW, nearest-frontier exploration
until detection), ESC and SemUtil (frontiers scored from nearby detections
converted to text and evaluated by an LLM or BERT), and ZSON (trained on
ImageNav and applied to ObjectNav with text embeddings) (p. 5). Supervised
comparators trained on ObjectNav are PONI, SemExp, PIRLNav (behavioral
cloning on 77k human demonstrations plus reinforcement-learning fine-tuning)
and RegQLearn (reinforcement learning only) (p. 5). Table I leaves cells
empty where "the cited work did not evaluate their approach on the
corresponding dataset" (p. 5), so the baseline values appear to come from the
cited works; the paper does not state that the baselines were re-run under
the same settings. SemExp was evaluated only on a subset of MP3D episodes with
COCO classes, so its MP3D cells are empty (p. 5).

The ablation (Table II, p. 6) holds the full system fixed and varies only the
value-update rule: Replacement (new value overwrites the old), Unweighted
average, and the proposed confidence-weighted average.

## Platform and setup

Simulation: Habitat on validation splits of three sets of 3D scans of real
environments (p. 5). Gibson uses the SemExp ObjectNav split with 1000
episodes in 5 scenes; HM3D has 2000 episodes in 20 scenes with 6 object
categories; MP3D has 2195 episodes in 11 scenes with 21 categories (p. 5).
Actions are MOVE FORWARD 0.25 m, TURN LEFT/RIGHT 30 degrees, LOOK UP/DOWN 30
degrees, and STOP. An episode succeeds if STOP is called within 1 m of any
instance of the target category in at most 500 steps (p. 2). Metrics are
success rate (SR) and success weighted by inverse path length (SPL),
reported in percent (p. 5).

Real world: a Boston Dynamics Spot (called a "Spot Arm platform" in the
conclusion) navigates to objects in an office building without a prior map
(pp. 1, 6). The paper reports no trial count, success rate, path length,
collision count, or list of target objects for these runs, and refers to
videos at naoki.io/vlfm (p. 6). Spot is legged; the paper does not describe
its locomotion, so the class comes from the manufacturer's public description
of Spot as a quadruped; the acknowledgment cites funding for "autonomous
navigation of legged robots" (p. 6).

## Evidence type and transfer

All quantitative results (Tables I and II) come from Habitat simulation. The
Spot deployment is closed-loop hardware, because VLFM selects the waypoints
that the BD API drives to, but it is reported only as a description and
videos, without metrics; hence `video-only-hardware`. The real-world setup
also differs from the simulated one: waypoint following uses the BD API, not
the evaluated PointNav policy, target depth comes from ZoeDepth, and
obstacles come from Spot's body depth cameras (p. 6). The simulation results
therefore show semantic search efficiency in static, single-floor scanned
homes; they say nothing about collision rates, dynamic obstacles, or the
real-world success rate.

## Sensors

Simulation: an egocentric RGB-D camera and an odometry sensor giving forward
and horizontal distance and heading relative to the start pose (p. 2). The
odometry has no z coordinate (p. 6). The PointNav policy uses depth only
(p. 5). Real world: the gripper camera feeds BLIP-2 and the detectors;
because of the gripper camera's limited depth range, ZoeDepth estimates a
depth image to place the target waypoint; Spot's body depth cameras provide
obstacles for frontier generation (p. 6).

## Compute and latency

On Spot, BLIP-2, GroundingDINO, MobileSAM, and ZoeDepth "were loaded and
executed in real-time" on a laptop with an RTX 4090 MaxQ Mobile GPU and 16 GB
of VRAM (p. 6). The paper does not say whether the laptop was carried by the
robot or connected remotely, and gives no frame rate, per-module latency, or
CPU and memory use. The PointNav policy was trained on 4 GPUs with 64 workers
each for 2.5 billion steps, about 7 days (p. 4). The hardware used for the
simulation benchmarks is not reported. The introduction claims that the
joint vision-language scoring "increases computational inference speed"
(p. 2), but no timing comparison is given.

## Key quantitative results

All values are SPL/SR in percent on the Habitat validation splits, with the
success rule of p. 2 (STOP within 1 m in at most 500 steps).

- VLFM: Gibson 52.2/84.0, HM3D 30.4/52.5, MP3D 17.5/36.4 (p. 5, Table I).
- VLFM versus the best zero-shot comparator per dataset: Gibson 52.2/84.0 versus SemUtil 40.5/69.3; HM3D 30.4/52.5 versus ESC 22.3/39.2; MP3D 17.5/36.4 versus ESC 14.2/28.7, the differences of +11.7/+14.7, +8.1/+13.3, and +3.3/+7.7 points that the text reports (p. 5, Table I). Other zero-shot rows: ZSON HM3D 12.6/25.5 and MP3D 4.8/15.3; CoW MP3D 3.7/7.4 (p. 5, Table I).
- VLFM versus supervised ObjectNav methods: Gibson 52.2/84.0 versus PONI 41.0/73.6, SemExp 33.9/65.7, and RegQLearn 31.3/63.7; MP3D 17.5/36.4 versus PONI 12.1/31.8 (+5.4/+4.6, as stated); HM3D 30.4/52.5 versus PIRLNav 27.1/64.1 (+3.3 SPL, -11.6 SR, as stated) (p. 5, Table I). The text states +19.2% SPL and +19.0% SR over SemExp on Gibson, but the Table I values give +18.3 for both; the introduction's "12% on Gibson, 5% on MP3D and 3% on HM3D" SPL gains over prior state of the art (p. 2) do not match Table I for MP3D, where the best prior SPL is ESC 14.2 (+3.3).
- Stairs: 14.6% of HM3D and 9.6% of MP3D episodes fail because they require traversing stairs, which the single-floor maps cannot handle (p. 6).
- Value-update ablation, weighted average versus unweighted average versus replacement: Gibson 52.2/84.0 versus 50.9/83.0 versus 48.0/76.1; HM3D 30.4/52.5 versus 30.0/51.8 versus 26.5/44.5; MP3D 17.5/36.4 versus 17.1/35.0 versus 16.6/31.7 (p. 6, Table II).
- Real-world Spot runs: no quantitative result is reported (p. 6).

## Stated limitations

- VLFM supports only single-floor episodes, because the simulator's odometry has no z coordinate, which complicates resetting the top-down maps when the floor changes (p. 6).
- Target objects are assumed to be easily visible from the default camera height; actively directing the camera and searching by manipulation, such as looking inside closed drawers, are future work (p. 6).
- The value map holds only task-specific semantic information, so it cannot be reused for sequential navigation to different objects or for other language-specified tasks such as vision-language navigation (p. 6).
- On Spot, the BD API guides the robot to a waypoint only if the path is relatively free of obstacles, and the gripper camera's limited depth range required ZoeDepth (p. 6).

## Transfer conditions

VLFM's semantic layer is zero-shot, but the full stack is not training-free:
the simulated PointNav policy was trained for about 7 days on 4 GPUs (p. 4),
and the detectors and BLIP-2 are pre-trained. A wheeled robot needs an RGB-D
camera with enough depth range for frontier mapping and target placement, a
reliable planar odometry source, a waypoint follower that handles obstacles
(the BD API was used on Spot only for relatively obstacle-free paths), and a
GPU comparable to a laptop RTX 4090 with 16 GB VRAM to run BLIP-2,
GroundingDINO, MobileSAM, and ZoeDepth; no onboard embedded deployment was
tested. Results come from static scanned homes; dynamic obstacles and
multi-floor search were not evaluated. Spot's camera height and gripper
camera viewpoint differ from a small wheeled robot's, which matters because
the authors assume targets are visible from the default camera height.

## Code and data

The paper gives the project page naoki.io/vlfm for videos (pp. 1, 6). It
does not state a code repository or released weights; any code release was
not verified. Gibson, HM3D, MP3D, and Habitat are public benchmarks and
simulator.

## Version family

ICRA 2024 paper, DOI 10.1109/ICRA57147.2024.10610712. No journal extension or
other version is in the library; preprint versions were not checked.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | weak | Sec. VI-A, p. 6 | "We also attribute the higher performance on the Gibson and HM3D datasets compared to the MP3D dataset to the quality of the 3D scans." |
| C3 | partial-support | moderate | Sec. II, p. 2 | "are often trained exclusively on simulated data, which can impede deployment of these policies onto realworld platforms" |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI-C, p. 6 | "For waypoint navigation, we utilize the BD API instead of a PointNav policy, which can guide the robot towards a specified waypoint, provided the path is relatively free of obstacles." |

## Page-cited excerpts

- **p. 2, Sec. III.** "An episode is defined as successfully completed if STOP is called within 1 m of any instance of the target object in 500 or fewer steps."
  The success threshold behind every SR and SPL value in Tables I and II.
- **p. 5, Sec. VI-A.** "VLFM significantly outperforms all zero-shot methods across all benchmarks"
  Supported by Table I against the zero-shot rows; it does not cover the supervised PIRLNav SR on HM3D.
- **p. 5, Sec. VI-A.** "In the HM3D dataset, VLFM only falls short of PIRLNav in terms of success"
  The one Table I cell in which a comparator beats VLFM.
- **p. 6, Sec. VI-A.** "VLFM currently only supports single-floor episodes due to the lack of a z coordinate in the odometry observation provided by the simulator"
  The cause of the stairs failures on HM3D and MP3D.
- **p. 6, Sec. VI-C.** "loaded and executed in real-time on a laptop equipped with an RTX 4090 MaxQ Mobile GPU with 16 GB of VRAM"
  The only compute statement for the real-world runs; no latency is given and the laptop's location is not stated.
- **p. 6, Sec. VII.** "we assume target objects will be easily visible in the scene from the default height of the robot camera"
  An author-stated limitation of the search strategy.

## Survey-usable statements

### Supported

- Scoring frontiers with a vision-language similarity map, without converting detections to text, gave higher Habitat ObjectNav SPL and SR than the zero-shot baselines on Gibson, HM3D, and MP3D (success = STOP within 1 m in 500 steps).
- Confidence-weighted fusion of repeated observations raised SPL and SR on all three datasets over replacement and unweighted averaging, by up to 8.0 SR points (HM3D, over replacement).
- A frontier-plus-VLM pipeline was run on a Spot robot in an office with models on a laptop GPU, as a demonstration without metrics.

### Not supported

- VLFM beats every method on every metric: PIRLNav has the higher HM3D SR (64.1 versus 52.5); VLFM is best in the other 5 of 6 Table I columns, and many comparator cells are empty.
- VLFM has a measured real-world success rate or collision rate: the Spot runs have no metrics.
- VLFM is faster than LLM-based frontier scoring: the speed claim on p. 2 has no timing data.
- The whole system needs no training: the PointNav policy was trained for 2.5 billion steps.
- VLFM is shown to work on a wheeled robot or onboard embedded compute: the only hardware is Spot with a laptop GPU.
- VLFM handles multi-floor search: it fails all episodes that need stairs.
- VLFM beats SemExp on Gibson by 19.2 SPL points: Table I gives 18.3.

## Verification log

- 2026-10-27 | host: Kiro | scope: full text read; Table I (p. 5) and Table II (p. 6) read from rendered page images; Fig. 1 page checked; every number and excerpt located with tools.locate | corrections: rebuilt in English template; success threshold page and setting separation added; reviewer observations moved out of limitations; SemExp and introduction inconsistencies recorded; ZSON MP3D SR 15.3 restored from the image (dropped in the transcription); compute location set to not reported (see tmp/corrections/E47.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/e8d511f8c08fa827b9924392/

## Original abstract

Understanding how humans leverage semantic knowledge to navigate unfamiliar environments and decide where to explore next is pivotal for developing robots capable of human-like search behaviors. We introduce a zero-shot navigation approach, Vision-Language Frontier Maps (VLFM), which is inspired by human reasoning and designed to navigate towards unseen semantic objects in novel environments. VLFM builds occupancy maps from depth observations to identify frontiers, and leverages RGB observations and a pre-trained vision-language model to generate a language-grounded value map. VLFM then uses this map to identify the most promising frontier to explore for finding an instance of a given target object category. We evaluate VLFM in photo-realistic environments from the Gibson, Habitat-Matterport 3D (HM3D), and Matterport 3D (MP3D) datasets within the Habitat simulator. Remarkably, VLFM achieves state-of-the-art results on all three datasets as measured by success weighted by path length (SPL) for the Object Goal Navigation task. Furthermore, we show that VLFM’s zero-shot nature enables it to be readily deployed on real-world robots such as the Boston Dynamics Spot mobile manipulation platform. We deploy VLFM on Spot and demonstrate its capability to efficiently navigate to target objects within an office building in the real world, without any prior knowledge of the environment. The accomplishments of VLFM underscore the promising potential of vision-language models in advancing the field of semantic navigation. Videos of real world deployment can be viewed at naoki.io/vlfm.
