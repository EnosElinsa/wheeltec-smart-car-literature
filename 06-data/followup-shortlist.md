# Confirmed follow-up reading: 15 papers

> **Stage record, November 2, 2026.** Its counts and statuses describe that date and are not updated. Current totals are in the [repository README](../README.md).

Prepared and confirmed by the user on 2026-11-02. The fixed selection is F01-F15; acquisition difficulties do not change it. Completed papers retain these IDs in the library. See the [acquisition/review ledger](followup-status.csv) and [full-text assessment](followup-assessment.md) for actual completion and remaining access requirements.

All 79 source titles and archived abstracts were read. Canonical DOI/URL matching removes three repeated records (rows 32 -> 3, 46 -> 34, 59 -> 23). Two more records already belong to the library (row 30 = E50, LeLaN; row 41 = E60, FORTRESS). This leaves 74 distinct candidates outside the historical corpus: 15 confirmed here and 59 deferred. Deferral is a bounded reading decision, not a rejection of scientific quality.

The [screening ledger](candidate-screening.csv) preserves all 79 rows, decisions, source paths, and SHA-256 hashes of the exact archived abstract strings. Its proposed decisions are the historical screening stage; the separate status ledger records user confirmation and subsequent acquisition. The [original queue](followup-candidates.csv) keeps its 79-row order. The abstracts came from the existing local historical archive, not a new exhaustive search. The title/abstract boundaries below remain the original screening rationale; later publisher and selected-full-text findings are recorded separately.

The four questions below come from the existing corpus-scoped evaluation agenda. These candidates may narrow or overturn that agenda; title/abstract screening cannot establish that any gap is filled or remains globally absent.

| Gap | Question |
|---|---|
| G1 | Does degraded localization or an integrity monitor trigger recovery, with both safety and navigation outcomes measured? |
| G2 | How are language/model reasoning, collision constraints, query cost, and fallback coupled? |
| G3 | Does pose uncertainty change traversability costs, speed, or closed-loop terrain decisions? |
| G4 | What happens during communication loss, after reconnection, and when local faults can spread? |

## F01. Safety-Quantifiable visual localization (G1)

[Safety-Quantifiable Line Feature-Based Monocular Visual Localization With 3D Prior Map](https://doi.org/10.1109/tits.2025.3572620) — original queue row 70.

Why read: RAIM-inspired fault exclusion and position/rotation protection levels connect localization errors to a safety quantity.

Known boundary from the abstract: AGV/AAV dataset evaluation; a protection level is not yet an integrity-conditioned navigation action.

Full-text check: Does a protection-level alarm trigger an autonomous recovery or speed change, with paired task and safety metrics?

## F02. Event-triggered fault-tolerant tracking (G1)

[Event-Triggered Fault-Tolerant Tracking Control for Autonomous Ground Vehicle via Descriptor Reduced-Order Observer](https://doi.org/10.1109/tits.2025.3548150) — original queue row 36.

Why read: A descriptor observer reconstructs physical faults and tracking errors for event-triggered fault-tolerant control.

Known boundary from the abstract: The abstract reports AGV setpoint tracking; perception degradation and integrity-risk calibration remain unconfirmed.

Full-text check: Are localization or sensor errors included in the controller assumptions and experimental fault-to-action chain?

## F03. Fault-tolerant decentralized map update (G1, G4)

[Fault tolerant decentralized collaboration for simultaneous localization and prior map update with stable 2D features](https://doi.org/10.1016/j.robot.2026.105402) — original queue row 63.

Why read: Collaborative localization and map update include fault detection, isolation, recovery, and robot correlation handling.

Known boundary from the abstract: Simulation and experimental data are reported; closed-loop navigation and partition/reconnect tests are not established.

Full-text check: Does collaborative fault recovery change robot navigation, and are shared map faults or disconnections evaluated?

## F04. Switch-SLAM (G1)

[Switch-SLAM: Switching-Based LiDAR-Inertial-Visual SLAM for Degenerate Environments](https://doi.org/10.1109/lra.2024.3421792) — original queue row 1.

Why read: A degeneracy detector switches between LiDAR and visual odometry, directly testing the sensing-to-recovery interface.

Known boundary from the abstract: The abstract describes dataset localization; switching estimators alone is not task-level navigation recovery.

Full-text check: What triggers switching, and are recovery latency, alarm errors, and task outcomes measured together?

## F05. VL-TGS (G2, G3)

[VL-TGS: Trajectory Generation and Selection Using Vision Language Models in Mapless Outdoor Environments](https://doi.org/10.1109/lra.2025.3559822) — original queue row 25.

Why read: Traversability-constrained candidate generation is combined with VLM trajectory selection on wheeled robots outdoors.

Known boundary from the abstract: Traversability and human-like path metrics do not by themselves establish certified collision safety or bounded latency.

Full-text check: Are hard constraints checked after VLM selection, and what happens when the model is delayed or chooses badly?

## F06. GSON (G2)

[GSON: A Group-Based Social Navigation Framework With Large Multimodal Model](https://doi.org/10.1109/lra.2025.3595038) — original queue row 26.

Why read: A mid-level planner combines slower multimodal social reasoning with pedestrian detection and tracking.

Known boundary from the abstract: Real-world social navigation is reported; an explicit query schedule, safety certificate, and fallback need full-text checks.

Full-text check: How are model latency and missed social predictions handled without interrupting the local collision-avoidance loop?

## F07. Sentinel (G2)

[Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress](https://proceedings.mlr.press/v270/agia25a.html) — original queue row 42.

Why read: Fast statistical action-consistency detection is separated from less time-sensitive VLM progress monitoring.

Known boundary from the abstract: Evidence is mobile manipulation; failure detection is not automatically an autonomous navigation fallback policy.

Full-text check: Does the runtime monitor trigger safe recovery, and how are query rate, detection delay, and task completion coupled?

## F08. Perceive With Confidence (G2)

[Perceive With Confidence: Statistical Safety Assurances for Navigation with Learning-Based Perception](https://proceedings.mlr.press/v270/dixit25a.html) — original queue row 16.

Why read: Conformal calibration links learned perception uncertainty and planning to statistical safety under state-distribution shifts.

Known boundary from the abstract: Hardware is a quadruped in static indoor scenes; the abstract does not establish a language-model fallback.

Full-text check: Which exchangeability or shift assumptions support the assurance, and how do latency and dynamic obstacles affect it?

## F09. Terrain-aware Voronoi collaboration (G3, G4)

[Multi‐Robot Collaborative Navigation Framework Based on 3D Voronoi Partitioning in Uneven and Unstructured Environments](https://doi.org/10.1002/rob.70260) — original queue row 53.

Why read: Terrain-aware partitioning and subgoal selection combine traversability with multi-robot navigation on uneven terrain.

Known boundary from the abstract: The abstract reports simulation and hardware, but drive type and propagation of pose uncertainty require confirmation.

Full-text check: Does localization uncertainty enter terrain costs or speed control, and are uncertainty and navigation outcomes paired?

## F10. Multi-fidelity GP exploration (G3)

[Adaptive exploration under localization uncertainty using multi-fidelity Gaussian processes](https://doi.org/10.1007/s10514-025-10235-2) — original queue row 60.

Why read: Localization uncertainty changes the environmental-field model and the exploration trajectory objective.

Known boundary from the abstract: Hardware is an underwater gliding robotic fish; this is a transferable uncertainty mechanism, not wheeled terrain evidence.

Full-text check: How is pose uncertainty propagated into planning, and what additional model is needed for terrain collision risk?

## F11. M2UD (G3)

[M2UD: A multi-model, multi-scenario, uneven-terrain dataset for ground robot with localization and mapping evaluation](https://doi.org/10.1177/02783649251401224) — original queue row 76.

Why read: Ground-robot sequences combine uneven terrain and sensing degradation with localization/mapping ground truth.

Known boundary from the abstract: This is a benchmark resource, not a planner or proof of uncertainty-aware closed-loop navigation.

Full-text check: Which sequences and metrics can support a paired pose-error and terrain-navigation evaluation?

## F12. Failure-aware target tracking (G4)

[Failure-Aware Multi-Robot Coordination for Resilient and Adaptive Target Tracking](https://doi.org/10.1109/tase.2025.3647786) — original queue row 38.

Why read: The framework distinguishes temporary and permanent sensing/communication failures and adapts connected and disconnected agents.

Known boundary from the abstract: The abstract reports failure scenarios without fixing platform, reconnect-map consistency, or communication assumptions.

Full-text check: Are actual disconnections/reconnections and local fault propagation measured alongside task performance?

## F13. C-CBF (G4)

[C-CBF: Communication-Aware Control Barrier Functions for Resilient Multi-Robot Connectivity](https://doi.org/10.1109/tase.2026.3667964) — original queue row 24.

Why read: Reception-aware communication constraints and collision avoidance are solved jointly in local control programs.

Known boundary from the abstract: Evidence in the abstract is simulation under a Rician channel model; partition/reconnect map consistency is unconfirmed.

Full-text check: What is guaranteed under model mismatch, and do slack variables permit loss of safety or connectivity?

## F14. Cross-rank exploration (G4)

[Decentralized multi-robot exploration under low-bandwidth communications](https://doi.org/10.1007/s10514-025-10234-3) — original queue row 23.

Why read: Position-only sharing coordinates decentralized exploration with explicit bandwidth and coverage objectives.

Known boundary from the abstract: Real deployment uses three quadrupeds; sparse messages do not prove operation through complete partitions.

Full-text check: Does evaluation include full outages and reconnection, and how are coverage redundancy and inconsistent state handled?

## F15. CoVOR-SLAM (G4)

[CoVOR-SLAM: Cooperative SLAM Using Visual Odometry and Ranges for Multi-Robot Systems](https://doi.org/10.1109/tits.2025.3566633) — original queue row 69.

Why read: Pose, covariance, and range sharing offers a low-communication alternative to exchanging shared map features.

Known boundary from the abstract: Two-rover images and UWB data are reported; autonomous outage recovery and map consistency are not established.

Full-text check: Which communication and shared-prior assumptions remain, and what fails during a partition or faulty range input?

## Confirmed acquisition scope

Check current publisher identity and version family, then acquire the official PDF/raw BibTeX pair with arp. Export full-text Markdown with MinerU into the corresponding local full-text folder and write a light review with the same evidence boundaries used in the current library. Re-check any specific numeric result before using it in the survey. Acquisition difficulties stay recorded rather than silently changing the selection.

All fifteen papers, F01–F15, now have verified official PDF/raw BibTeX pairs, original MinerU precision Markdown, and checked targeted light cards. They join the historical 112, giving 127 review cards at completion of that selection (23 full and 104 light, including 89 historical conversions and 15 targeted readings). The PDF-inclusive checker passes all 127; a light review still does not establish whole-paper or comprehensive numerical verification.

F03 (Elsevier), F09 (Wiley), and F11 (Sage) initially required manual PDF access. The user supplied all three official publisher PDFs; their identities, authors, DOIs, and volume/issue details were checked against the retained raw publisher BibTeX before import. Their transcriptions and targeted reviews are complete, and no fixed ID was replaced. See the [status ledger](followup-status.csv) for separate acquisition/review states and the [assessment](followup-assessment.md) for the resulting G1/G3/G4 revisions. The title/abstract screening notes above remain the rationale and questions used when selecting the papers, rather than the final full-text findings.

The subsequent N01–N20 assessment brings the current selection to 147 publications (23 full and 124 light cards). The [selection record](survey-inclusion.json) preserves the historical baseline and current membership.
