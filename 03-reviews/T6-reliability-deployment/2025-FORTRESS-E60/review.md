# Real-Time Out-of-Distribution Failure Prevention via Multi-Modal Reasoning

## Metadata

| Field | Value |
|---|---|
| ID | E60 |
| Title | Real-Time Out-of-Distribution Failure Prevention via Multi-Modal Reasoning |
| Authors | Milan Ganai, Rohan Sinha, Christopher Agia, Daniel Morton, Luigi Di Lillo, and Marco Pavone |
| Venue | Proceedings of The 9th Conference on Robot Learning, PMLR 305, pp. 283-308 |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v305/ganai25a.html |
| Theme folder | T6-reliability-deployment |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T6-reliability-deployment/2025-FORTRESS-E60/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-FORTRESS-E60/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-FORTRESS-E60/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: semantic-language-navigation
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, recorded-robot-data, simulation, numerical
- protocol_caveats: video-only-hardware, motion-capture-pose, cloud-model, scripted-scenario, few-trials
- platform_class: aerial
- platform: custom quadrotor with Jetson Nano, Realsense D435, and PX4 (closed loop); ANYmal Generation D quadruped (recorded data); drone agent in CARLA (simulation)
- boundary_platform: yes
- degradation: dynamic-objects, model-error
- degradation_observed: none
- evaluation_primary: integrity-reliability
- evaluation_all: residual, closed-loop-task, integrity-reliability
- sensors: RGBD camera (Realsense D435) with open-vocabulary detection; motion capture for drone pose
- compute: Jetson Nano on the quadrotor; safety inference 0.011 s and reach-avoid planning 1.28 s per fallback; foundation-model queries 3.68-15.65 s run ahead of time
- compute_location: mixed
- summary_result: In CARLA rooftop-landing fallbacks, FORTRESS had 92.2% successful and 7.8% no-plan rates versus 40.0% successful and 60.0% unsafe for AESOP; trial count not stated.
- summary_limitation: The authors write the semantic fallback strategies by hand and map unsafe semantics to static, fixed-radius avoidance regions without dynamic or terrain-specific constraints.
- survey_included: yes
- verification_level: full

## Problem

A robot whose nominal goal becomes unsafe in an out-of-distribution (OOD)
situation, such as a drone whose landing area is on fire, needs a fallback
goal and a path that avoids semantically hazardous regions. Foundation models
can judge semantic hazards but are slow and dynamics-agnostic, and earlier
methods use hard-coded fallback regions or human-specified constraints
(p. 2). The paper asks how to generate semantically safe, dynamically feasible
fallback plans quickly once a runtime monitor raises an alarm.

## Mechanism

FORTRESS splits slow reasoning from fast planning. At a low frequency during
nominal operation or offline, (i) the VLM Molmo turns a hand-written fallback
strategy description (for example "empty, horizontal building roofs") into
pixel goal points, which depth and camera intrinsics convert into cached 3D
goals (p. 4); (ii) an LLM is prompted for a list of high-level failure modes
(for example "Near Human", "High Temperature"), and for each mode a threshold
on the cosine distance between text embeddings is calibrated by a conformal
quantile alpha over embeddings of safe scene descriptions (Eq. 1, p. 5). At
runtime, a semantic cost theta_phi(x) is positive when the embedding of the
description of all concepts within radius l_phi of state x is closer to a
failure mode than the threshold (Eq. 2, p. 5). Planning solves a min-max
reach-avoid problem over all failure modes plus a collision cost (Eq. 3,
p. 5), approximated by RRT with the costs invalidating states and tracked by
LQR or MPC (p. 6). If no plan with nonpositive cost exists, the next strategy
and goal are tried (p. 6).

The appendix theorem (p. 25) states that the tracked trajectory satisfies
the safety and reach constraints of Eq. 3 under these preconditions: known
dynamics (p. 3); a known worst-case tracking error bound eta > 0; avoidance
radii inflated to l_h + eta' with eta' > eta; the planner works in the
inflated free space and returns a trajectory from the start b; the goal ball
B_rho(g) is control invariant with rho > eta; and the planner step satisfies
Delta x < min(rho - eta, min_h 2 sqrt((eta' - eta)^2 + 2(l_h + eta)(eta' - eta))).
The theorem takes the semantic cost functions as given; it says nothing about
detection or classification errors.

## Baselines and controls

- Semantic classification (Table 1): a one-mode ablation that measures
  similarity to a single "Safe" embedding, and on-the-fly prompting of GPT-4o,
  o3-mini, and o4-mini with a yes/no safety question (pp. 6, 19).
- Failure-mode generation (Fig. 5 and Figs. 10-11): failure modes from
  Gemini 2.0 Flash, Claude 3.7 Sonnet, DeepSeek-R1, Llama 4 Scout, GPT-4o,
  Mercury, o1, o3-mini, and o4-mini, compared with the manual modes
  (pp. 7, 20).
- CARLA fallback planning (Fig. 6): AESOP, adapted by the authors with
  Molmo goal generation and 2 m collision avoidance but no semantic safety,
  and Safe-Lang, adapted with Molmo goals and open-vocabulary detection in
  place of human language input with a blanket 4 m avoidance of all detected
  objects (p. 23). All methods share RRT plus LQR (p. 23).
- A Mahalanobis-distance variant is reported as a side ablation; the authors
  find no significant gain over cosine similarity (p. 18).

## Platform and setup

- Synthetic text benchmarks: safe training, safe test, and unsafe test scene
  descriptions for drone, boat, and vehicle domains; eight embedding models
  (MiniLM, Mistral, MPNet, Multilingual-E5, OpenAI Text Embedding Large,
  Qwen2, SFR Embedding Mistral, Voyage AI voyage-3-large) and around 10
  manual failure modes per domain (p. 7). Dataset sizes are not reported.
- Failure-mode sweep: 1 to 50 modes per reasoner, five queries per reasoner,
  2000 calibration experiments per reasoner on the drone synthetic set
  (p. 20).
- ANYmal Generation D in a room under construction: safe data collected
  around boxes, paper scraps, ladders, paint cans, and people detected with
  OWLv2; failure modes from Claude 3.7 Sonnet with an image of the room;
  thresholds calibrated with Qwen2; then a second deployment with placed
  hazards (person on a ladder, cables, caution tape, a blue toxic spill)
  (pp. 7, 24). The number of frames or detections is not reported.
- CARLA: a drone agent above city buildings with people, firetrucks, traffic
  cones, and cars on roofs; goal ball of 1 m, l_c = 2 m, l_phi = 4 m, RRT
  step 0.5 m, LQR tracking, and replanning after at most 15 RRT steps because
  detectors are inaccurate at long range (p. 22). The trial count behind
  Fig. 6 is not stated.
- Dynamic concepts: a 3D double integrator with a skydiving human and a
  falling box, RRT replanning every 10 steps, and MPC with a 2 s (20-step)
  horizon; shown in one example figure (pp. 23-24).
- Quadrotor hardware: an indoor scene of model buildings (Fig. 1) with a
  construction roof (ladder and caution tape), a roof on fire, a rooftop
  parking lot with two vehicles, an empty roof, and a garden roof; goal ball
  0.5 m, l_c = 0.1 m, l_phi = 1.5 m, goal filtering with l_phi inflated by
  0.5 m, RRT step 0.1 m, and interpolated waypoints sent over ROS2 to PX4 at
  100 Hz (pp. 24-25). The drone lands on the garden roof; the number of runs
  is not reported.

## Evidence type and transfer

The strongest setting is the quadrotor run: FORTRESS's plan drives the drone
to a landing, so it is closed-loop hardware, but the outcome is shown only in
Fig. 1 and the only hardware numbers are the component times of Table 2. The
ANYmal results are classification on data the authors recorded with their
robot; the paper does not say the detections changed the robot's motion. The
planning comparison with baselines exists only in CARLA simulation, and the
moving-object case only as a numerical double-integrator example. The
synthetic text benchmarks are not sensor data and fit no evidence category;
they test the embedding classifier alone. No wheeled ground robot is used:
the vehicle domain is synthetic text only.

## Sensors

On the quadrotor, an Intel Realsense D435 streams RGBD data, OWLv2 detects
roof concepts, and Optitrack motion capture provides localization (pp. 24-25).
In CARLA, the simulator's built-in pose, depth view, and camera intrinsics are
used with YOLOv8 and OWLViT (p. 22). On ANYmal, OWLv2 runs on images from the
robot; the camera is not specified (p. 24).

## Compute and latency

Table 2 (p. 8) reports component times "during quadrotor drone hardware
deployment with Jetson Nano". The paper does not say how the proprietary
models in Table 2 (Gemini 2.0 Flash, Claude 3.7 Sonnet, OpenAI and Voyage AI
embeddings) were accessed; because these models are vendor-hosted, the
reviewer codes `mixed` and `cloud-model` (onboard planning, hosted model
queries), which is an inference, not a statement of the paper. Where Molmo
and DeepSeek-R1 ran is also not stated. How the runtime safety inference
embeds descriptions with the OpenAI model in 0.011 s is not explained. The
inference times of on-the-fly prompting (Table 3, p. 19) do not name the
machine.

## Key quantitative results

- Component times on the drone, mean and standard deviation (p. 8, Table 2, rendered image): low-frequency queries, Molmo goal points 5.82 (0.13) s, Gemini 2.0 Flash failure modes 3.68 (0.33) s, Claude 3.7 Sonnet 15.65 (0.51) s, DeepSeek-R1 12.76 (1.22) s, Voyage AI calibration 3.91 (0.08) s, OpenAI calibration 5.43 (0.19) s; at the fallback trigger, safety reasoning inference 0.011 (0.006) s and reach-avoid planning 1.28 (0.55) s.
- CARLA rooftop-landing fallback rates, FORTRESS versus AESOP versus Safe-Lang (p. 8, Fig. 6, rendered image): successful plans 92.2% versus 40.0% versus 67.2%; unsafe plans none shown versus 60.0% versus none shown; no plan 7.8% versus none versus 32.8%. The authors attribute FORTRESS's no-plan cases to all roofs being occupied by unsafe concepts (p. 23); the number of trials is not stated.
- Balanced accuracy of FORTRESS with 10 modes, Voyage AI / Qwen2 / OpenAI embeddings (p. 6, Table 1, rendered image): boat 0.97 / 0.72 / 0.81, vehicle 0.89 / 0.78 / 0.90, ANYmal 0.73 / 0.90 / 0.66.
- Balanced accuracy of on-the-fly prompting, GPT-4o / o3-mini / o4-mini (p. 6, Table 1, rendered image): boat 0.76 / 0.83 / 0.76, vehicle 0.61 / 0.83 / 0.86, ANYmal 0.64 / 0.87 / 0.85. The one-mode "Safe" ablation stays between 0.50 and 0.63.
- ANYmal with Qwen2: TPR 0.82 and TNR 0.98 for FORTRESS versus TPR 1.00 and TNR 0.70 for o4-mini and TPR 0.95 and TNR 0.80 for o3-mini (p. 6, Table 1, rendered image).
- The paper states that FORTRESS reaches a balanced accuracy "higher than 0.90" in each domain (p. 7), but the best Table 1 values for vehicle and ANYmal are 0.90, not higher (p. 6).
- On-the-fly prompting takes 0.49 s (GPT-4o), 3.23 s (o3-mini), and 2.68 s (o4-mini) per query (p. 19, Table 3, rendered image). The text says prompting is more than 50 times slower than FORTRESS (p. 19); against the 0.011 s of Table 2 the GPT-4o ratio is about 45.
- Failure modes generated by reasoners: AUROC on the drone synthetic set generally improves and stabilizes with up to 50 modes; the authors report OpenAI embeddings consistently above 0.95 AUROC and Multilingual-E5 and Voyage AI sometimes above 0.9 (pp. 7, 20, Figs. 5, 10, 11; curves only, no tabulated values).

## Stated limitations

- The semantic fallback strategies are currently written by the authors for each robot and environment (p. 9).
- Fallback goals are static; non-static goals, such as merging into moving traffic, are future work (p. 9).
- Semantically unsafe regions are mapped to static, fixed-radius avoidance regions; dynamic or context-dependent constraints, dynamic obstacles, terrain factors such as surface friction, and disturbances such as wind are not handled (p. 9).
- The framework prevents OOD failures; managing robots that are already experiencing failures is future work (p. 9).
- The method assumes a runtime monitor that raises the alarm; FORTRESS does not provide it (p. 3).

## Transfer conditions

A wheeled robot needs an RGBD camera, an open-vocabulary detector, and a
runtime monitor, plus access to the VLM, LLM, and embedding services ahead
of time. Which embedding model works best changed across domains in Table 1,
so the embedding and threshold must be calibrated on safe descriptions from
the target environment. The theorem needs a known worst-case tracking error
eta; the paper does not report eta for CARLA or the drone, so it cannot be
checked whether the step sizes used there satisfy the bound. Skid-steer or
Ackermann robots would need a tracker with a bounded error under their
kinematics; the paper tests only drone dynamics. Planning took 1.28 s on
average on a Jetson Nano, which sets how early the monitor must trigger.

## Code and data

The paper links a project website, https://milanganai.github.io/fortress
(p. 1). The publisher BibTeX abstract instead says "Website and code" are at
https://submfort.github.io/fortress/; neither site was checked, and the paper
itself does not state a code or data release.

## Version family

CoRL 2025 paper with appendix, counted once. AESOP [13] and Safe-Lang [18]
are separate works adapted as baselines. The publisher BibTeX abstract is a
different text from the abstract printed in the PDF.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | weak | App. D.1, p. 22 | "Because the object detectors are not always accurate from far distances, we perform a cycle of path tracking" |
| C3 | direct-support | moderate | Sec. 1, p. 2 | "renders them unsuitable for real-time querying for granular planning in safety-critical moments" |
| C4 | unset | n/a | | |
| C5 | partial-support | moderate | Sec. 2, p. 3 | "We need systems that adaptively generate real-time fallback strategies, ensuring recoveries are semantically safe in uncertain real-world environments." |
| C6 | qualifies | moderate | Sec. 7, p. 9 | "Although we currently write semantic fallback strategies for robots and environments, extensions could develop methods that automatically extract semantic descriptions, infer the relevant fallback goals, and adapt them across diverse robotic platforms and operation settings." |

## Page-cited excerpts

- **p. 8, Sec. 5.3.** "We measure each component of our approach on Jetson Nano hardware shown in Table 2."
  The source of the onboard attribution; the paper does not say how hosted models were reached.
- **p. 23, App. D.3.** "Our approach can reliably generate safe plans successfully with more than a 90% success rate"
  The success rate is for CARLA simulation and one fallback strategy, not for hardware.
- **p. 24, App. F.2.** "We use the Optitrack motion capture system for localization."
  The hardware run depends on external pose, so it does not test localization under the hazards.
- **p. 9, Sec. 7.** "our mapping of semantically unsafe regions to static, fixed-radius avoidance regions could be extended to handle dynamic or context-dependent constraints"
  The authors' own scope limit on the avoidance model.
- **p. 7, Sec. 5.1.** "The results demonstrate that for each domain, FORTRESS's approach can achieve a balanced accuracy performance higher than 0.90"
  Holds only for the best embedding per domain, and the vehicle and ANYmal bests equal 0.90.

## Survey-usable statements

### Supported

- Splitting foundation-model reasoning (seconds) from runtime semantic cost evaluation (0.011 s) and RRT reach-avoid planning (1.28 s) makes a semantic fallback plan available within about a second on a Jetson Nano, with the slow queries cached beforehand.
- In CARLA simulation with one rooftop-landing strategy, semantic cost functions raised the share of successful fallback plans to 92.2%, against 40.0% for an AESOP adaptation without semantic avoidance and 67.2% for a blanket-avoidance Safe-Lang adaptation.
- Calibrating embedding distances to around 10 failure modes outperformed a single "Safe" mode in every domain of Table 1.
- On a staged indoor scene, a quadrotor using FORTRESS landed on the one roof without hazards, with motion-capture localization.

### Not supported

- FORTRESS beats on-the-fly prompting regardless of the embedding model: 5 of the 9 FORTRESS rows of Table 1 are below the best prompting baseline of the same domain (boat Qwen2 0.72 and OpenAI 0.81 versus o3-mini 0.83; vehicle Qwen2 0.78 versus o4-mini 0.86; ANYmal Voyage AI 0.73 and OpenAI 0.66 versus o3-mini 0.87). The OpenAI embedding used in CARLA and on the drone scored 0.66 on ANYmal.
- FORTRESS detects more hazards than prompting: prompting has the higher TPR on ANYmal (o4-mini 1.00 versus 0.82) and on vehicle (GPT-4o 1.00 versus at most 0.83); FORTRESS wins on TNR and balanced accuracy.
- The hardware landing success rate is known: one landing is shown in Fig. 1 with no trial count.
- The framework replans at 100 Hz: 100 Hz is the waypoint stream to PX4; planning takes 1.28 s on average.
- The whole pipeline runs on a Jetson Nano: the failure-mode and calibration queries use vendor-hosted models whose access is not described.
- The theorem guarantees safety against OOD hazards: it assumes correct semantic costs, a known tracking-error bound, a found plan, and a control-invariant goal region.
- The result transfers to wheeled ground robots: the ground-vehicle domain is synthetic text, and no wheeled robot was run.

## Verification log

- 2026-10-27 | host: Kiro | scope: full text read (Secs. 1-7 and Appendices A-G); Table 1 (p. 6), Fig. 5 (p. 7), Fig. 6 and Table 2 (p. 8), Table 3 (p. 19), Fig. 1 (p. 1), and Fig. 13 (p. 24) read from rendered page images; setup values and excerpts located with --find | corrections: rebuilt in English template format; Fig. 6 rates added; limitations restricted to author statements; paper inconsistencies recorded (balanced accuracy "higher than 0.90", "> 50x" speed ratio); counterexamples to the prompting comparison listed; hosted-model compute flagged as unstated; BibTeX code URL differs from the paper's website (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T3-T6/014467eb387c046567de212e/

## Original abstract

While foundation models offer promise toward improving robot safety in out-of-distribution (OOD) scenarios, how to effectively harness their generalist knowledge for real-time, dynamically feasible response remains a crucial problem. We present FORTRESS, a joint reasoning and planning framework that generates semantically safe fallback strategies to prevent safety-critical, OOD failures. At a low frequency under nominal operation, FORTRESS uses multi-modal foundation models to anticipate possible failure modes and identify safe fallback sets. When a runtime monitor triggers a fallback response, FORTRESS rapidly synthesizes plans to fallback goals while inferring and avoiding semantically unsafe regions in real time. By bridging open-world, multi-modal reasoning with dynamics-aware planning, we eliminate the need for hard-coded fallbacks and human safety interventions. FORTRESS outperforms on-the-fly prompting of slow reasoning models in safety classification accuracy on synthetic benchmarks and real-world ANYmal robot data, and further improves system safety and planning success in simulation and on quadrotor hardware for urban navigation. Website can be found at https://milanganai.github.io/fortress.
