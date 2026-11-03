# Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks

## Metadata

| Field | Value |
|---|---|
| ID | E49 |
| Title | Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks |
| Authors | Jiazhao Zhang, Kunyu Wang, Shaoan Wang, Minghan Li, Haoran Liu, Songlin Wei, Zhongyuan Wang, Zhizheng Zhang, and He Wang |
| Venue | Proceedings of Robotics: Science and Systems (RSS 2025) |
| Year | 2025 |
| Type | conference |
| DOI | [10.15607/rss.2025.xxi.013](https://doi.org/10.15607/rss.2025.xxi.013) |
| Official URL | https://roboticsconference.org/2025/program/papers/13/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-Uni-NaVid-E49/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-Uni-NaVid-E49/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2025-Uni-NaVid-E49/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: video-only-hardware, offboard-compute
- platform_class: legged
- platform: quadruped robot in the real-world demonstrations (model not reported); simulated agents in the benchmarks
- boundary_platform: yes
- degradation: none
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: monocular RGB video
- compute: remote server with an NVIDIA A100 GPU; about 0.2 s to generate the next four actions
- compute_location: offboard-local
- summary_result: R2R Val-Unseen in simulation: SR 47.0% and SPL 42.7 versus NaVid 37.4% and 35.9, with RGB-only input.
- summary_limitation: The authors state that the model covers four fixed tasks and predicts only short-horizon discrete actions; smooth continuous motion is future work.
- survey_included: yes
- verification_level: light

## Problem

The paper asks whether a single video vision-language-action model can unify instruction following, object navigation, embodied question answering, and person following, while keeping the cost of the video history low.

## Mechanism

EVA-CLIP extracts 256 visual tokens per frame. Tokens are pooled by group to 64 (current), 4 (short-term), and 1 (long-term) per frame; the short-term buffer holds 64 frames, and adjacent long-term tokens merge when their cosine similarity exceeds 0.95. A two-layer MLP projects visual tokens into Vicuna-7B, and a navigation token separates action generation from answering. Each prediction outputs four discrete primitives: forward 25 cm, turn left or right 30 degrees, or stop (p. 4-5 per the legacy card). Control is discrete in continuous scenes, not a smooth velocity policy.

## Baselines and controls

Named baselines include NaVid, ETPNav, HAMT, PIRLNav-IL-RL, OVRL-v2, VLFM, DAgRL+OD, NavILLM, and an IBVS person follower with ground-truth bounding boxes; video question-answering baselines include BridgeQA, LLaMA-VID, and ST-LLM. Ablations cover multi-task training and the history memory.

## Platform and setup

- Training: 3.6M multi-task navigation samples from 861 synthetic scenes plus 3.2M public video question-answering samples; 40 H800 GPUs for about 35 hours (1400 GPU hours), one epoch, video sampled at 1 FPS (pp. 5, 7). The 3.2M value was checked visually on p. 7; other numbers retain light-review status.
- Benchmarks in simulation: R2R and RxR (VLN-CE), HM3D ObjectNav, HM3D-OVON, MP3D-EQA, and a self-built language person-following benchmark.
- Real world: demonstrations on a quadruped robot (Fig. 5-7); robot model, camera model, and onboard compute are not reported in the main text. Trial counts and success statistics point to the supplementary material, which is not part of the 17-page main PDF and was not checked.

## Evidence type and transfer

The quantitative evidence is simulation. The real-world evidence is qualitative trajectories on a quadruped with remote inference. There is no wheeled-robot or onboard Jetson validation.

## Sensors

Online input is monocular RGB video and language, without depth or explicit odometry (p. 7).

## Compute and latency

A remote server with an NVIDIA A100 GPU runs Uni-NaVid and sends commands to the robot; it needs about 0.2 s to generate the next four actions (p. 7 per the legacy card). The robot uploads compressed observations asynchronously and executes pending actions. A100 memory, network bandwidth, end-to-end latency, and Jetson performance are not reported.

## Key quantitative results

- R2R Val-Unseen (SR % / SPL): Uni-NaVid 47.0 / 42.7 versus NaVid 37.4 / 35.9, a 9.6-point SR gain; ETPNav 57.0 / 49.0 and HAMT 55.0 / 51.0, which use panorama, depth, odometry, and high-level actions, are higher (Table II; no located page, the PDF has no text layer).
- RxR: 48.7 / 40.9 versus NaVid 23.8 / 21.2; the NaVid row is trained on R2R only, while Uni-NaVid's training data include RxR (Table III; no located page).
- HM3D ObjectNav: 73.7 / 37.1 versus PIRLNav-IL-RL 70.4 / 34.1 and OVRL-v2 64.7 / 28.1; the baselines mostly use odometry, Uni-NaVid only RGB (Table IV; no located page).
- HM3D-OVON zero-shot Val-Unseen: 39.5 / 19.8 versus zero-shot VLFM 35.2 / 19.6 and fine-tuned DAgRL+OD 37.1 / 19.8; on Val-Seen 41.3 / 21.1, with SPL slightly below DAgRL+OD 21.2 (Table V; no located page).
- MP3D-EQA: 47.3% accuracy in continuous environments versus NavILLM 44.5% in discrete environments, so the settings differ; with ground-truth trajectories 54.4 versus 47.4 (Table VI; no located page).
- Person following: SR 61.21, following rate 71.93, collision rate 2.07% versus IBVS with ground-truth boxes 50.58, 68.89, 0.80%; higher success and following rate but a higher collision rate (Table VII; no located page).
- History ablation: VLN SR 9.61 with the current frame only versus 48.7 with the full history (Table X; no located page).

## Stated limitations

- The model covers four fixed tasks and assumes a standard-size robot (p. 11 per the legacy card).
- It is limited to predicting simple trajectories composed of a short horizon of low-level discrete actions; smooth continuous motion and long cross-building tasks are future work (p. 11).

## Transfer conditions

Legacy reviewer observations:
- The video memory and a ROS action adapter are reusable, but the 25 cm / 30-degree primitives need wheeled closed-loop control and independent obstacle avoidance.
- Network latency, robot size, camera height, emergency stop, and compressed Jetson inference must be re-validated.
- Real-world quantitative results, confidence intervals, A100 memory, bandwidth, and end-to-end latency are not reported in the main text.
- The PDF has no text layer; the legacy card used OCR and read the table values from the page images.

## Code and data

Project page https://pku-epic.github.io/Uni-NaVid/. Repository availability, weight license, complete data download, and reproducibility were not verified.

## Version family

The RSS 2025 paper and the preprint of the same title are one version family. The predecessor NaVid is a separate work used as a baseline.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | qualifies | moderate | Sec. VII, p. 11 | "is currently limited to predicting simple trajectories composed of a short horizon of future low-level discrete actions." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. VI-A, p. 7 | "utilize a remote server with an NVIDIA A100 GPU to run Uni-NaVid" |

## Page-cited excerpts

- **p. 5, Sec. IV-C Action Planning.** "The action tokens belong to the discrete action set"
  Each step predicts discrete primitives (forward 25 cm, turn 30 degrees, stop).
- **p. 7, Sec. VI-A Deployment Details.** "utilize a remote server with an NVIDIA A100 GPU to run Uni-NaVid"
  Inference runs on a remote A100, not onboard.
- **p. 7, Sec. VI-A Deployment Details.** "All tasks take an online captured RGB video"
  RGB video and language are the only inputs.
- **p. 11, Sec. VII Limitations.** "is currently limited to predicting simple trajectories composed"
  The authors acknowledge short-horizon discrete actions only.

## Survey-usable statements

### Supported

- A single RGB-only video VLA trained on 3.6M multi-task samples improves on NaVid in simulated VLN (R2R SR 47.0% versus 37.4%) and is competitive on ObjectNav, OVON, EQA, and person following.
- Real-world use relied on remote A100 inference at about 0.2 s per four actions.

### Not supported

- Uni-NaVid beats all VLN methods: ETPNav and HAMT are higher on R2R with richer inputs.
- Uni-NaVid is safer at person following: its collision rate is higher than IBVS.
- The real-world results are quantified: the main text shows only qualitative trajectories.
- The model runs onboard at 5 Hz on embedded hardware: inference ran on a remote A100.

## Verification log

- 2026-10-27 | host: Kiro | scope: light conversion of the legacy extraction; metadata and abstract checked; numeric results retained from the legacy card | corrections: translated to the English template; automated PDF excerpt checks remained unresolved because the PDF has no text layer
- 2026-11-02 | host: Codex | scope: light review repair; OCR page matching plus visual inspection of PDF pp. 5, 7, 11; table results not re-verified | corrections: shortened two page excerpts to contiguous source text; confirmed the remote A100 and discrete-action limitations visually; corrected public video question-answering samples from 2.3M to 3.2M on p. 7
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T4-T5/0aea41b5e50203d87a8d1952/

## Original abstract

Embodied Navigation is a fundamental capability for intelligent robots, requiring robots to follow human commands and move autonomously within physical environments. Despite significant advancements, most existing navigation approaches are tailored to specific navigation tasks, such as instruction following, searching objects, answering questions, tracking people, and more. However, the increasing demands on advanced embodied navigation pose the challenge of designing a practical navigation agent that can incorporate multiple navigation tasks naturally and benefits from the synergy between these tasks. To this end, we present Uni-NaVid, a video-based vision-language-action (VLA) model to unify different paradigms of navigation tasks and improve navigation performance by encouraging the synergy among different navigation sub-tasks. This VLA model can directly take natural language instructions and RGB video streams as inputs and output low-level robotic actions in an end-to-end manner. To efficiently process extensive RGB video streams, we propose an online token merge strategy that spatially and temporally consolidates similar visual information which improves the inference speed to 5 Hz. For training Uni-NaVid, we collect 3.6 million navigation data samples across different navigation tasks. Extensive experiments on diverse navigation benchmarks demonstrate that Uni-NaVid achieves state-of-the-art performance within a unified framework by using only ego-centric RGB video as inputs. Additionally, real-world experiments confirm the model's effectiveness and efficiency, shedding light on its strong generalizability
