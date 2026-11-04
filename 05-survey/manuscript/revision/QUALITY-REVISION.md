# Content and language revision — 2026-11-02

Historical report for the 127-publication revision. The subsequent 147-publication synthesis and current checks are recorded in [IEEE-INTEGRATION.md](IEEE-INTEGRATION.md).

The authorized revision implements the eight findings in CONTENT-AND-LANGUAGE-REVIEW.md. The main change is comparative synthesis: paragraphs explain a shared navigation problem, alternatives, surviving information, observed trade-offs, and applicability. The revision adds seven source-checked numerical examples without pooling their results or asserting cross-study performance rankings. No unresolved Blocker or High finding remains within this revision's scope. Field-wide novelty has not been certified; research directions are explicitly limited to the reviewed mechanisms and evaluations.

The artifact boundary includes the abstract, all eleven IEEEtran sections, the supplement, all included tables and figures, the data generator, and the delivery verifier. Native LaTeX conventions and the established engineering register were retained. No highlights, graphical abstract, cover letter, or response letter is present. Internal records, source hashes, and development scripts remain outside the manuscript's scholarly argument. This report applies latex-prose-audit; the prior reference-prose calibration and PDF inspection workflow remain applicable.

## Findings and disposition

| Priority | Location | Finding / check | Applied correction |
|---|---|---|---|
| High | Evaluation table and generator | A4/C11: counting unit included a review with original task evidence | Count the 124 technical publications, explicitly excluding all three background publications. The unchanged index yields 86 component, 72 task, 49 degradation, and 13 integrity/reliability attributes; attributes overlap. |
| Medium | Abstract, I–III, IX, evaluation figure | A2/B9: mixed organizing categories | Functional chapters provide coverage; the comparison follows affected assumption, response, required information, and evidence. Evaluation separates measurement level, test conditions, and risk/diagnostic interpretation. |
| Medium | IV–VIII and chapter syntheses | B9/A4: method inventories outweighed comparison | Compare selection, sensor substitution, reinitialization, dynamic exclusion/estimation, learned planning roles, semantic interfaces, information sharing, and fault responses through their requirements and trade-offs. |
| Medium | Five technical tables and supplement Table S2 | C11/A4: outcome categories omitted measured quantities | Replace 52 broad outcome labels with evaluated quantities. Add seven numerical cases with baselines, experimental units, source tables/plots, and interpretation. |
| Medium | X and related-review positioning | A4: gap statements exceeded the checked evidence | Recognize existing estimation/planning, semantic/control, recovery, and fusion integrations. Specify the remaining degraded-information interface and a discriminating experiment; scope conclusions to reviewed systems. |
| Medium | IV–VIII, X | A2/A4: generic embodiment caveats | State which information mechanism transfers and which wheel-contact, curvature, footprint, traction, stopping, or tracking assumptions need modification. |
| Low | Repeated F03/F09/F11 discussion | B9: repetition | Keep full diagnosis/reset limits in VIII and reference-system dependencies in IX. Other mentions retain only the fact needed for their local argument. |
| Low | X–XI and technical syntheses | B5/B9: abstract integration wording and repeated protocols | Replace repeated metric inventories with specific response choices and matched comparisons. Centralize the common protocol in IX; conclude with conditional technical findings. |

Disposition: 1 High, 5 Medium, and 2 Low findings addressed. The novelty-related finding is addressed by narrowing claims and acknowledging contrary integrated examples, not by inferring absence from retrieval results.

## Vocabulary ledger

| Term | Meaning / use |
|---|---|
| Degradation | Operating change affecting required information, models, resources, or physical capability |
| Response | Change to estimator information, model, map/state hypothesis, or executed action |
| Functional area | Navigation function used for chapter coverage, not a mutually exclusive mechanism taxonomy |
| Technical publications | The 124 selected technical studies/resources; the three background publications remain cited but are excluded from evaluation counts |
| Component / task measures | Measurement level; runtime and classification scores are component measures rather than errors |
| Degradation test | Experimental condition with source, onset, severity, and duration |
| Risk / diagnostic claim | A claim tied to its particular failure event, assumptions, calibration, and unit |
| APE | Absolute pose error, introduced at the first numerical LODESTAR comparison; ATE and RPE definitions remain unchanged |

## Notation and artifact ledgers

All six displayed equations are exactly unchanged from the baseline and immediate pre-revision snapshot. No mathematical model, symbol, algorithm, or label was redefined. The measurement-level terminology is aligned across the abstract, IX, evaluation table, evaluation figure, and supplement. Full-width comparison tables retain 8 pt text, paired setting/quantity cells, platform notes, and their existing row order. The supplementary results table is new; its independent metrics and protocols are retained row by row.

The main document contains 3 figures, 8 tables, and 30 unique labels. The supplement contains 1 figure, 2 tables, and 7 unique labels. Source-table numbers in Table S2 refer to the cited papers, not to this manuscript. All 127 selected works remain cited in substantive main-text prose. The main bibliography resolves 143 entries and the supplement resolves 10.

## Claim ledger and original-source checks

| Case | Original artifact / physical PDF page | Checked claim and boundary |
|---|---|---|
| E01 LODESTAR | Tables III and V / 6–7 | Long Corridor APE 1.386 versus 3.113 m; benchmark-average desktop time 28.69 versus 21.04 ms. Short exp reverses ordering, 0.429 versus 0.412 m. Surviving LiDAR returns are required. |
| E13 FIT-SLAM 2 | Tables 2 and 4 / 12, 17 | Cave 880 versus 1118 s and Corridor 1809 versus 1706 s for FAEL. Planning 20.8 versus 63.0 ms without/with Fisher information. Simulator-pose benchmarks and SLAM ablation are separate evaluations. |
| E25 Safe Horizon MPC | Table 2 / 11 | 100 Gaussian eight-pedestrian simulations, common solver/cost, matched joint-risk specification 0.05: duration 16.0 (1.9) versus 18.4 (2.4) s. Maximum estimated plan collision probability 0.0092 versus 0.0019. This is planned risk under a known motion distribution. |
| E50 LeLaN | Tables 2 and 3 / 6–7 | 150 visible-target trials, 28 objects, 0.2 m threshold: 0.89 versus 0.67. Separate 15-trial obstacle ablation: arrival 0.60 with versus 0.13 without collision training. No open-world search or collision-risk inference. |
| F09 TAPM-IVP | Table 2 / 12 | Scene 1, ten trials/method, two robots: success 90% each versus 40%/30% after removing partitioning and greedy subgoal selection together. Per-robot simulation rates, not hardware team completion. |
| E59 GP recovery | Fig. 6 / 6 | Ten simulated runs/goal/world: dense 1 m doorway goal 0 gives 8/10 versus 3/10; sparse 2 m goal 0 gives 10/10 for both. Counts read from plotted rates; hardware provides staged demonstrations. |
| M37 home deployment | Table 3 / 10 | 1539 requests, 1130 successes, 177 failures, 232 unperformed. Reported 86.46% uses 1307 attempts, not all requests. Assistance, selected homes, and availability limit interpretation. |

The relevant original method/evaluation passages and rendered source tables or plots were inspected. Source PDF hashes and page locators are retained in data/within-study-comparisons.json; no raw PDF, publisher BibTeX, or transcription was modified. Seven checks do not constitute new whole-paper verification of all 127 publications. The 23 full / 104 light assessment distinction, including 89 earlier extracts and 15 targeted readings, is retained.

A bounded independent Crossref check used five broader queries; three returned metadata candidates and two were rate-limited. These metadata results were not treated as full-paper evidence or proof of a literature gap, and no new reference was added. The raw search diagnostics are retained in the local archive. Wider coverage and exhaustive novelty assessment remain beyond the conclusions of this revision.

## Verification

Both commands completed successfully:

```text
latexmk -pdf -quiet -interaction=nonstopmode -halt-on-error -file-line-error survey.tex
latexmk -pdf -quiet -interaction=nonstopmode -halt-on-error -file-line-error supplement.tex
```

The main PDF has 24 pages and the supplement 3. All 381 source-artifact hashes match the index; the seven quantitative source hashes and the six unchanged equations are also checked by scripts/verify_delivery.py. Both PDFs have no undefined citations/references, LaTeX warnings, overfull boxes, or underfull vertical boxes. Five underfull horizontal notices remain in the main document and one in the supplement; the rendered lines were checked. All pages were rendered and inspected, with enlarged inspection of the changed evaluation diagram, table headers, and supplementary results. No clipping or overlap was found. Table S2 now appears at the top of S2; its explanation and balanced bibliography begin on S3.

The exact ten-word screen found one matching numeric comparison phrase in 11,469 windows against 141 project documents. It is the independently checked Short exp result, “0.429 m versus 0.412 m for the baseline”; this is retained as a numerical comparison. This lexical screen is not an originality determination. Delivery verification, git diff whitespace checking, and reverse application checking of the cumulative source patch passed.

Positive patterns retained: explicit technical subjects and mechanism descriptions; within-study comparisons with relevant counterexamples; separate meanings for estimation uncertainty, plan risk, diagnostics, and task outcomes. Historical change maps, patches and rendered checks are retained in the local archive; current changes are recorded in Git. Current PDF hashes and build diagnostics are in delivery-verification.json.
