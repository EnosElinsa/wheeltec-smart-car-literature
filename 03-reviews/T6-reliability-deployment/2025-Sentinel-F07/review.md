# Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress

## Metadata

| Field | Value |
|---|---|
| ID | F07 |
| Title | Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress |
| Authors | Christopher Agia, Rohan Sinha, Jingyun Yang, Ziang Cao, Rika Antonova, Marco Pavone, and Jeannette Bohg |
| Venue | Proceedings of The 8th Conference on Robot Learning, Proceedings of Machine Learning Research, vol. 270, pp. 689-723 |
| Year | 2025 (conference 2024) |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v270/agia25a.html |
| Theme folder | T6-reliability-deployment |
| Batch | followup-2026-11-02 |
| Local files | `01-papers/T6-reliability-deployment/2025-Sentinel-F07/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Sentinel-F07/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T6-reliability-deployment/2025-Sentinel-F07/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: none
- evidence_type: online-hardware
- evidence_all: online-hardware, simulation
- protocol_caveats: motion-capture-pose, cloud-model, few-trials
- platform_class: omnidirectional
- platform: holonomic mobile base with Kinova Gen3 7-DoF arm (p. 23)
- boundary_platform: no
- degradation: model-error
- degradation_observed: none
- evaluation_primary: integrity-reliability
- evaluation_all: integrity-reliability, designed-degradation
- sensors: fixed external ZED 2; motion capture for mobile-base pose
- compute: local policy/STAC hardware unspecified in selected sections; cloud VLM mean response 14.0 s
- compute_location: mixed
- summary_result: Sentinel achieves 95% detection accuracy on 10 successful and 10 failed real-world chair-tucking rollouts; recovery outcomes are not evaluated.
- summary_limitation: The method has no formal guarantee on detecting failures, and the STAC false-positive guarantee does not certify the VLM ensemble.
- survey_included: yes
- verification_level: light

## Problem

Generative imitation policies can fail when object geometry or initial pose differs from their demonstrations. Erratic action changes and temporally consistent lack of task progress require different runtime detectors. The contribution is detection of failing episodes, rather than a learned replacement controller (pp. 1, 6, 8).

## Mechanism

Sentinel combines statistical temporal action consistency (STAC) and VLM video question answering. STAC compares overlapping action-chunk distributions at adjacent policy-inference steps using a statistical distance, accumulates the scores, and thresholds them using successful calibration rollouts. The VLM receives the task, image history, elapsed time, and task horizon, then labels progress ok/failure. Their predictions are combined by union; fast erratic-failure detection and slower progress reasoning can run at different timescales (pp. 6, 19, 34-35).

## Baselines and controls

Score-based comparisons include state-embedding similarity, diffusion-action reconstruction, output variance, and DDPM loss; temporal variants ablate consistency measurement. VLM ablations compare image versus video QA and multiple models. Detection thresholds share the 95th-quantile successful-rollout protocol: 50 calibration rollouts per simulated task and 10 for hardware (p. 6). Detailed baseline implementation and every comparison cell were not audited.

## Platform and setup

Three simulated tasks are PushT, Close Box, and Cover Object, with object scale/dimension or pose shifts beyond demonstrations. Hardware uses a holonomic mobile base with a Kinova Gen3 arm to tuck a chair under a table. A fixed ZED 2 observes the workspace and motion capture tracks the base. The hardware policy uses EquiBot, predicts 16 actions, executes four, and moves the base if the end effector leaves a predefined workspace. Evaluation has 10 successful and 10 failed hardware rollouts after calibration on 10 nominal successful rollouts (pp. 6, 8, 23-24).

## Evidence type and transfer

Hardware supports online failure monitoring of a mobile-manipulation policy; the selected experiment evaluates detector accuracy and detection time. It does not show an alarm-triggered recovery controller or a resulting navigation/collision outcome, so the monitor is coded online-hardware. Simulation stresses different failure modes. For G2, the transferable contribution is assigning fast and slow failure categories to different monitors; mobile manipulation is not a direct wheeled-navigation recovery benchmark.

## Sensors

One fixed external ZED 2 produces point clouds; Grounded Segment Anything extracts task-relevant objects from language descriptions. Motion capture supplies mobile-base pose. The VLM receives camera history, while the policy uses point clouds and proprioception (pp. 19, 23-24). Sensor placement and external pose requirements matter for deployment transfer.

## Compute and latency

The VLM is queried in the cloud; the reported mean GPT-4o video-QA response time is 14.0 s at writing. The authors treat that delay as acceptable for the slower task-progression category while assigning erratic behavior to STAC (p. 6). Image frequency relative to policy execution is a tunable parameter, with nu in {1,2} used in experiments (p. 19). Local STAC/policy processor specifications, monetary query cost, a worst-case latency bound, and a model-timeout fallback were not established in the selected sections. Compute is coded mixed for local policy/consistency processing plus cloud VLM; the local hardware is unspecified.

## Key quantitative results

Only values stated in the selected prose are recorded; table/plot cells were not independently read.

- On the hardware chair-tucking task, Sentinel reports 95% detection accuracy over 10 successful and 10 failed policy rollouts (p. 8, results text accompanying Table 2).
- With the same hardware setting and 10 successful calibration rollouts, STAC detects 80% of policy failures with 90% true-negative rate; the VLM reports 90% true-positive and 100% true-negative rates (p. 8, results prose).
- Mean cloud GPT-4o video-QA response time is reported as 14.0 s; this is an inference-response mean, not a worst-case navigation-loop bound (p. 6).

## Stated limitations

- The erratic/progression taxonomy may not exhaust possible failures (p. 8).
- There is no formal guarantee of detecting failures; combining detectors by union can increase false alarms, and the method detects failures as they occur rather than predicting them (p. 8).
- The formal false-positive bound applies only to STAC under nominal successful-trajectory assumptions; it neither certifies the VLM ensemble nor guarantees detection or false alarms on arbitrary OOD successes. The conformal guarantee is marginal over calibration datasets (pp. 34-35).

## Transfer conditions

Reviewer conditions: reproduce successful-rollout calibration for the new robot, policy, horizon, and sensors, and check that STAC action coordinates and multimodality assumptions remain meaningful. The STAC proposition uses i.i.d. full nominal trajectories, not independent time steps. OOD behavior and cloud reasoning remain empirical. A navigation deployment would need an explicit alarm-to-action contract, collision constraints, handling of model/network delays, and paired safety/task metrics; the selected detection experiments do not supply those components. These are corpus-scoped G2 checks, not an assertion that no other work addresses them.

## Code and data

The paper links [qualitative results](https://sites.google.com/stanford.edu/sentinel) on p. 1. Code/data availability and deployment were not independently verified.

## Version family

Formal CoRL 2024 proceedings paper published in PMLR 270 in 2025. PDF uses Zi-ang Cao while publisher citation uses Ziang Cao; identity/order agree. No DOI is exposed in the official citation. Preprint/later-version relationships were not audited; this review counts the proceedings work once.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | partial-support | moderate | Sec. 4.2, task-progress monitoring, p. 6 | "At the time of writing, cloud-querying a state-of-the-art VLM for video QA incurs significant latency" |
| C4 | unset | n/a | | |
| C5 | qualifies | moderate | Conformal guarantee remarks, p. 35 | "We make no claims on combined performance of STAC and the VLM, as VLM represents a black-box classifier." |
| C6 | qualifies | moderate | Limitations, p. 8 | "our approach does not provide formal guarantees on detecting failures." |

## Page-cited excerpts

- **p. 23, B.1.2, Mobile Robot Setup.** "We use a holonomic mobile base equipped with a Kinova Gen3 7-DoF arm."
  The physical embodiment is mobile manipulation.
- **p. 6, Sec. 4.2, task-progress monitoring.** "At the time of writing, cloud-querying a state-of-the-art VLM for video QA incurs significant latency"
  This motivates different monitoring timescales, without a deadline guarantee.
- **p. 8, Limitations.** "our approach does not provide formal guarantees on detecting failures."
  Detection accuracy is not a formal safety or recovery guarantee.
- **p. 35, Conformal guarantee remarks.** "We make no claims on combined performance of STAC and the VLM, as VLM represents a black-box classifier."
  The nominal STAC FPR result does not certify the ensemble.

## Survey-usable statements

### Supported

- Sentinel combines statistical action consistency with slower VLM progress monitoring for simulated and physical mobile-manipulation failure detection.
- For G2, the paper motivates separate monitoring timescales and evaluates detection, while leaving a navigation alarm-to-recovery contract outside the selected evidence.

### Not supported

- Formally guaranteed detection or an ensemble-wide safety guarantee: the authors explicitly limit their formal result to STAC's nominal false-positive rate.
- Autonomous recovery improves navigation success: the selected hardware experiment measures detector performance on chair-tucking rollouts.
- Guaranteed low-latency semantic intervention: the reported VLM time is a mean, and no timeout fallback or worst-case deadline is established.

## Verification log

- 2026-11-02 | host: Codex | scope: targeted new-paper light review of physical PDF pp. 1, 6-8, 19, 23-24, 28, 34-35; metadata and original abstract checked; short excerpts matched on exact cited PDF pages; selected prose numbers read; no whole-paper, proof, or table-cell audit; transcription was pending at drafting | corrections: new English follow-up card; preserved formal FPR assumptions, external-pose and cloud-latency boundaries; no legacy claims or synthetic evidence added
- Source provenance: newly acquired official publisher PDF and unchanged raw publisher BibTeX, followup-2026-11-02; no legacy extraction was used. Identity: https://proceedings.mlr.press/v270/agia25a.html. PDF SHA-256: 10ffa23d7c24d220ac16b0c7c5bcfe55e634936b5a04e01942e5ac01500bfb1a.
- Verification level: light is used here for the user-authorized targeted follow-up read, not a full-paper audit; unreviewed sections, proofs, tables, and numerical claims remain unchecked.

- 2026-11-02 | host: Codex | scope: final transcription-bound validation; metadata, original abstract and retained excerpts checked with the PDF-inclusive review checker; original source bytes preserved; targeted light scope retained | corrections: parsing completed; selected excerpts shortened where OCR spacing or mathematical markup prevented matching; no whole-paper or full numeric verification

## Original abstract

Robot behavior policies trained via imitation learning are prone to failure under conditions that deviate from their training data. Thus, algorithms that monitor learned policies at test time and provide early warnings of failure are necessary to facilitate scalable deployment. We propose Sentinel, a runtime monitoring framework that splits the detection of failures into two complementary categories: 1) Erratic failures, which we detect using statistical measures of temporal action consistency, and 2) task progression failures, where we use Vision Language Models (VLMs) to detect when the policy confidently and consistently takes actions that do not solve the task. Our approach has two key strengths. First, because learned policies exhibit diverse failure modes, combining complementary detectors leads to significantly higher accuracy at failure detection. Second, using a statistical temporal action consistency measure ensures that we quickly detect when multimodal, generative policies exhibit erratic behavior at negligible computational cost. In contrast, we only use VLMs to detect failure modes that are less time-sensitive. We demonstrate our approach in the context of diffusion policies trained on robotic mobile manipulation domains in both simulation and the real world. By unifying temporal consistency detection and VLM runtime monitoring, Sentinel detects 18% more failures than using either of the two detectors alone and significantly outperforms baselines, thus highlighting the importance of assigning specialized detectors to complementary categories of failure. Qualitative results are made available at sites.google.com/stanford.edu/sentinel.
