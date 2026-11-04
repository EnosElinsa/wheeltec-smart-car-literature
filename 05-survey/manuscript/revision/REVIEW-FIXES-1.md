# Review fixes, round 1 - November 4, 2026

This revision applies the low-cost items of the simulated review recorded in [CONTRIBUTIONS-AUDIT-AND-REVIEW.md](CONTRIBUTIONS-AUDIT-AND-REVIEW.md). None of these items conflicts with an earlier author decision. Items that do conflict are left for an author decision: foundational pre-2021 references, selection detail in Section III, missing 2021-2024 works and the major restructuring. The selection and the bibliography are unchanged at 229 works and 238 references.

## Study descriptions corrected against the sources

Each change was checked against the local transcription.

- osmAG-LLM: 21 of 30 building trials succeed end to end and 27 reach a correct position. The failure analysis reports 9 failures, of which 6 reached a position with the target visible.
- MonoMPC: the collision rate is 6.6% against 25% for the navigation stack at a similar mean speed and 48.3% for its faster setting. This replaces "up to seven times fewer collisions".
- Terrain-adaptive MPC: outdoors it still exceeds MPPI (67%) and GAKD (73%) after falling from 94% to 80%. Table III now reads "Few quantified simulation-to-hardware comparisons".
- LeLaN: collision training raises arrival with obstacles from 0.13 to 0.60 but lowers success without obstacles from 0.89 to 0.77.
- VAMOS: the gain is from 6 to 9 of 10 runs.
- Help Me Through: the text adds the 20 h variant with online fine-tuning.
- mEclares: the text states that it was evaluated with quadrotor agents and a ground charging rover.
- Correlation-aware map repair (F03) is described consistently as an estimator-level candidate mechanism evaluated on recorded road-vehicle data, not as a validated reconnection protocol.

## Claims and terms

- The 26% figure is qualified as a property of the purposively selected sample in the abstract, the contribution list and the conclusion. The abstract gives the count (59 of 228) and the period (January 2021 to November 2026).
- "Designed degradation" in the prose is now "a named degradation condition". This matches the coding, which also counts deliberately selected difficult sequences. Section IX states that a publication counts when it names the condition and reports results for it, without a matched nominal control.
- The contribution list says that the survey proposes the four interfaces and outlines a matched comparison for each. Section X states that the interfaces are an agenda proposed by this survey, not a ranking derived from the coding, and that part of the corpus was acquired for them. Table V now reads "would test" and "Primary outcomes".
- Two unconditioned superlatives now carry their conditions: "least invasive" in Section IV and "most conservative" in Section VI.
- The conclusion no longer claims that no response can substitute for another.

## Non-wheeled evidence

- Fig. 1 marks with a dagger the 20 named examples that were not evaluated on a wheeled robot or its data. The marks are computed from `boundary_platform` in the corpus coding (`build_figures.py`).
- The caption states that the named methods are examples.
- Sections VII and X now state the platform of the non-wheeled anchors: perception calibration on a legged robot, FORTRESS on a quadrotor, aerial target tracking, and road-vehicle data for map repair.

## Table IV and Fig. 3

- Table IV rows are renamed "Integrity or failure-risk assessment" and "Wheeled-robot platform or data".
- The "All" column gives percentages.
- A table note states that counts are per publication, that the two attributes of a combined row need not come from the same experiment, and that Fig. S1 also counts the context review of Section V (52 versus 53).
- The Fig. 3 caption defines a false alarm by the pose error relative to the alert limit and defines a missed detection.
- Section IX defines the alarm time as the first detector decision that the supervisor receives and the action time as the onset of the commanded response.

## Front and back matter

- Index terms now include localization, motion planning, fault tolerance and performance evaluation.
- An Acknowledgment discloses the use of large language model tools for screening, drafting and language editing, following the IEEE policy on AI-generated content. The authors should name the specific tools before submission.

## Length

Ten sentences that repeated Table II, Table IV or other sections were removed. Every citation in them remains cited elsewhere. The main paper stays at 24 pages. The last page balances without a forced break (739 and 676 pt; the trigger is set to an unused value), and almost no slack remains.

## Verification

[numeric-audit.json](numeric-audit.json) now covers 23 numerical sentences. The new numbers for MonoMPC, terrain-adaptive MPC, LeLaN and VAMOS are found together in the transcriptions. R27's 21 of 30 is recorded as derived from the 9 reported failures. `verify_delivery.py` passes in both modes: 24 pages, 238 references, 27 labels, and 693 source artifacts with no hash mismatch. Sentence rhythm: mean 21.6 words, 11% under 12 words, 7% over 35 words, with no style flags and a clean house-style scan.
