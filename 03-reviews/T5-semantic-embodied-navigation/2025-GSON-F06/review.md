# GSON: A Group-Based Social Navigation Framework With Large Multimodal Model

## Metadata

| Field | Value |
|---|---|
| ID | F06 |
| Title | GSON: A Group-Based Social Navigation Framework With Large Multimodal Model |
| Authors | Shangyi Luo, Peng Sun, Ji Zhu, Yuhong Deng, Cunjun Yu, Anxing Xiao, and Xueqian Wang |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 10, pp. 9646-9653 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1109/lra.2025.3595038](https://doi.org/10.1109/lra.2025.3595038) |
| Official URL | https://ieeexplore.ieee.org/document/11106758/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-GSON-F06/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-GSON-F06/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2025-GSON-F06/citation.bib) |

## Survey coding

- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, dataset-playback
- protocol_caveats: scripted-scenario, few-trials
- platform_class: differential-drive
- platform: two-wheeled nonholonomic mobile robot (p. 5)
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: 2D LiDAR and two RGB cameras
- compute: processor/location not established in selected sections; dense-crowd LMM inference typically 1.5-2 s
- compute_location: not-reported
- summary_result: GPT-4o achieves 86.6% acceptable grouping on 100 scenes; hardware comparisons report lower social disturbance with modest navigation-time and jerk tradeoffs.
- summary_limitation: Dense-crowd inference delay and occlusions reduce responsiveness and grouping accuracy; binary social-group avoidance lacks context-dependent flexibility.
- survey_included: yes
- verification_level: light

## Problem

Collision avoidance and goal reaching do not ensure respect for social interactions such as queues, conversations, or photography. GSON extracts semantic group relationships to guide navigation without calling an LMM at every local planning step (pp. 1, 4-5).

## Mechanism

LiDAR/RGB pedestrian detection, projection-based image filtering, Hungarian association, and constant-velocity Kalman tracking provide people states. Marked images with IDs go to an LMM, and parsed group labels attach to tracks. A keyframe stores the most informative scene within a one-second window, preferring more visible people, and updates when a more representative frame is found or it expires. Global A*/JPS feeds a mid-level planner that fits social-group spaces and replans affected path segments using BIT*. Local NMPC-CBF constrains motion using tracked positions and constant-velocity pedestrian predictions (pp. 3-5).

## Baselines and controls

Grouping: Gemini 2.0 Flash, Gemini 2.5 Pro, Claude 3.7 Sonnet, GPT-4o, Qwen2.5-VL 32B/7B, plus DBSCAN on 2D/3D coordinates. Navigation: TEB, TEB with group estimates, SACSON, GMPC, RLCA. Several other LMM navigation systems were excluded because they were not open source and the authors' implementations were unreliable in pilot tests; this is not an exhaustive LMM-planner comparison (p. 5).

## Platform and setup

Grouping uses 100 image scenarios from SCAND, SiT, and city-walk videos, human-consensus labels, and 10 queries per scenario/model. Hardware is a two-wheeled nonholonomic robot with 2D LiDAR and two RGB cameras. Short-range queuing, photography, talking, and walking scenarios repeat three times with participant position/path/speed variation. A separate long-range demonstration combines four scenarios. Additional dense-crowd cases use a canteen, elevator entrance, and campus gate (pp. 5-7).

## Evidence type and transfer

Group classification is dataset/video evaluation; navigation is closed-loop hardware. Short-range tests involve few staged social interactions. Long-range/dense-crowd demonstrations do not establish a broad failure rate. For G2, group semantics change mid-level routes while local CBF constraints use tracked pedestrians; model latency and semantic errors remain implementation limits.

## Sensors

2D LiDAR and two RGB cameras. A LiDAR person detector is filtered against YOLOv5 image detections, associated, and Kalman-tracked. RGB prompts support grouping; pedestrian position/velocity drives the local planner (pp. 3, 5). Localization and ground-truth arrangements were not established in the selected sections.

## Compute and latency

Selected prose reports about 4 s for GPT-4o/Gemini 2.0 Flash, 2 s for Qwen2.5-VL-32B, 1 s for its 7B variant, and 8 s for Gemini 2.5 Pro/Claude 3.7 Sonnet (p. 5). Dense-crowd tests report typical Qwen2.5-VL-32B inference of 1.5-2 s and occasional responsiveness loss (p. 7). A one-second keyframe rule is a query-update policy rather than an inference deadline. Processor specifications, model locations, end-to-end worst-case timing, and an explicit timeout/fallback policy were not established in the selected sections.

## Key quantitative results

Only selected prose values are retained; no plot values were extracted.

- On 100 grouping scenes with 10 trials per scenario/model, GPT-4o achieves 86.6% acceptable groupings: 77.8% Accurate and 8.8% Miss under the authors' taxonomy (p. 5).
- Short-range hardware scenarios repeat three times. Text reports lowest individual/group disturbance and highest comfort distance, with slightly increased jerk/runtime; numeric plot values were not audited (pp. 5-6, Fig. 8 discussion).
- Dense-crowd Qwen2.5-VL-32B inference typically takes 1.5-2 s and sometimes reduces planner responsiveness (p. 7).
- Calling the LMM adds at least 1 s of response time in the reported navigation comparison, separate from local NMPC/CBF solve timing (p. 6).

## Stated limitations

- LMM inference latency can reduce responsiveness to rapidly changing dense-crowd contexts (p. 7).
- Egocentric occlusions cause incomplete or inaccurate group detection (p. 7).
- Binary labels and avoidance of all detected groups cannot adapt to nuanced social contexts such as crossing a queue versus a conversation (p. 7).

## Transfer conditions

Reviewer conditions: verify camera/LiDAR calibration, track continuity, group-label age, and constant-velocity prediction validity. A CBF on tracked/predicted pedestrians does not establish unconditional safety under missed detections, occlusion, incorrect labels, or solver infeasibility. The selected pages specify keyframe updates and separate planning levels, but do not establish a tested fallback for late/unavailable model results. G2 is narrowed by this semantic-to-route-and-constraint interface and its measured limits; this paper does not settle a global gap claim.

## Code and data

The article states that supplementary material is available through [the DOI](https://doi.org/10.1109/LRA.2025.3595038) (p. 1). No code/data-release URL was located in the selected sections; availability and execution were not verified.

## Version family

RA-L 2025 formal journal article. No conference-extension or related-version statement was located in the selected sections. Count this DOI once. Registration includes small-caps markup around GSON; this title follows the printed PDF and unchanged publisher BibTeX.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | partial-support | moderate | Sec. V-D, LMM inference latency, p. 7 | "sometimes reduced planner responsiveness to rapidly changing social contexts." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V-D, Complex and adaptive group behavior, p. 7 | "this approach lacks flexibility to adapt to nuanced social contexts" |

## Page-cited excerpts

- **p. 4, Sec. IV-B, keyframe policy.** "The LMM is only queried when this keyframe is updated"
  The update rule reduces model-query frequency without imposing a response deadline.
- **p. 7, Sec. V-D, LMM inference latency.** "sometimes reduced planner responsiveness to rapidly changing social contexts."
  The authors observe an operational cost of model latency.
- **p. 7, Sec. V-D, Complex and adaptive group behavior.** "this approach lacks flexibility to adapt to nuanced social contexts"
  Binary grouping and conservative avoidance restrict semantic behavior.
- **p. 5, Sec. V-B1, Experimental Setup.** "using a two-wheeled nonholonomic mobile robot equipped with a 2D LiDAR and two RGB cameras."
  This is wheeled-hardware navigation evidence.

## Survey-usable statements

### Supported

- LMM-derived groups guide mid-level route changes while NMPC-CBF uses tracked pedestrian states, with small staged wheeled-robot experiments.
- G2 is informed by an explicit keyframe query rule and observed latency/occlusion limits; semantic guidance and local constraints occupy distinct planning levels.

### Not supported

- Unconditional collision freedom under arbitrary perception/model errors: CBF constraints depend on tracked/predicted pedestrians, and occlusion errors are observed.
- A bounded model deadline or evaluated timeout fallback: the keyframe rule establishes neither.
- Superiority to every LMM navigation system or large-sample dense-crowd reliability: several systems are excluded and the hardware scope is limited.

## Verification log

- 2026-11-02 | host: Codex | scope: targeted new-paper light review of physical PDF p. 1 (including rendered abstract), selected mechanism pp. 3-5, evaluation/limitations pp. 5-7, and last-page identity context; excerpts matched on exact cited pages; selected prose values checked; no whole-paper or plot/table-value audit; transcription was pending at drafting | corrections: new English follow-up card; printed/BibTeX title used; retained model-specific inference times, local CBF conditioning, small hardware protocol, and unestablished timeout fallback
- Source provenance: newly acquired official publisher PDF and unchanged raw publisher BibTeX, followup-2026-11-02; no legacy extraction was used. Identity: https://ieeexplore.ieee.org/document/11106758/. PDF SHA-256: b24d2e64583fb4e9f0ac014b8a28f3da903703779c0ffb2ca0d74cf540519fed.
- Verification level: light is used here for the user-authorized targeted follow-up read, not a full-paper audit; unreviewed sections, proofs, tables, and numerical claims remain unchecked.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

With the increasing presence of service robots and autonomous vehicles in human environments, navigation systems need to evolve beyond simple destination reach to incorporate social awareness. This letter introduces GSON, a novel group-based social navigation framework that leverages Large Multimodal Models (LMMs) to enhance robots’ social perception capabilities. Our approach uses visual prompting to enable zero-shot extraction of social relationships among pedestrians and integrates these results with robust pedestrian detection and tracking pipelines to overcome the inherent inference speed limitations of LMMs. The planning system incorporates a mid-level planner that sits between global path planning and local motion planning, effectively preserving both global context and reactive responsiveness while avoiding disruption of the predicted social group. We validate GSON through extensive real-world mobile robot navigation experiments involving complex social scenarios such as queuing, conversations, and photo sessions. Comparative results show that our system significantly outperforms existing navigation approaches in minimizing social perturbations while maintaining comparable performance on traditional navigation metrics.
