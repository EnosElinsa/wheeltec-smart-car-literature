> Stage record before the recent-citation revision and the IEEE refresh: the current manuscript has 229 selected works and 238 references. See the [refresh integration](IEEE-REFRESH-INTEGRATION.md).

# Expansion integration and source audit - November 3, 2026

The working survey incorporates S01-S48 into substantive comparisons in Sections IV-X and updates selection/assessment disclosure in Section III and the supplement. The corpus contains 195 works (192 technical and three context), plus 16 background references, for 211 resolved references. Every corpus key appears in section prose. Five representative tables contain 63 rows, including 15 new works.

## Argument changes

- Localization compares directional feature selection, inertial compensation, preconditioning, calibration, persistent structure and map validity. Reference construction is kept distinct from independent pose truth.
- Motion planning adds angle-dependent terrain risk, visual-geometric cost/speed/novelty maps, parallel homotopy choices and bounded-input/state constraints. Virtual obstacles, external pose, offboard control and numerical-only studies are qualified explicitly.
- Semantic navigation compares multimodal memory, sketch/tour preparation, physical terrain grounding and social scene-understanding counterexamples. Goal reasoning and safe geometric execution remain separate claims.
- Collaboration separates sparse exchange, lossy keyframe selection, lossless coding, planned observations, range geometry and semantic overlap acceptance. Message reduction does not establish reconnection safety.
- Recovery includes planner reinitialization, anti-novelty motion, depth-based corrections, capability reassignment and online adaptation. Goal localization, resets, charging, training servers and escalation are included in deployment cost.
- Evaluation adds survivor-conditioned error, route/reference coverage, virtual hardware hazards, uncertainty events, and preparation/adaptation timing. Challenges now acknowledge implemented mechanisms and focus on their remaining interfaces.

## Evidence scope

All 48 new cards are targeted light assessments with selected physical-page scopes and excerpts matched to the Markdown and exact PDF page text. No new performance-table numbers are introduced. Overall assessment depth is 23 full and 172 light cards: 89 historical conversions and 83 targeted readings. Human final review and whole-paper assessment of the light cards remain incomplete.

The library's `06-data/survey-200plus-2026-11-03/source-reading.json` records the pages, excerpts and judgments; `04-analysis/survey-expansion-integration-2026-11-03.md` maps every addition to its survey consequence. Original PDF, BibTeX and Markdown bytes remain unchanged. S24-S26 derived-citation flags and S41's documented official/PDF title variant survive catalog promotion. The baseline 147 index rows and frozen selection/review-decision hashes are preserved.

## Validation

Both PDFs compile successfully. The main survey is 33 pages with three figures and eight tables; the supplement is three pages with one figure, two tables and ten references. The [delivery audit](delivery-verification.json) confirms all 211 bibliography entries resolve, all 195 corpus works occur in prose, 30 main-document labels are unique, six equations are unchanged, seven checked numerical cases are retained, and all 585 source hashes match. Neither PDF has unresolved references or overfull boxes. The main log retains 12 underfull horizontal boxes; the supplement retains one.

Visual inspection covered the main opening, technical tables, representative body/evaluation pages and final bibliography, plus the supplement. Expanded tables fit their pages; bibliography and supplement columns remain readable. The supplement's balance command was moved to remove a second-column warning.

All 195 review cards pass the PDF-aware checker. The catalog regression suite passes 12 tests, including preservation of derived/title-variant status after assessment. Public links and the strict public-tree scan pass. The public-data verifier also passes locally; a new clean public-clone build was not performed.

The result is a source-checked working draft. Author information and submission declarations remain incomplete. No new robot experiments, publication, push or submission occurred in this integration.
