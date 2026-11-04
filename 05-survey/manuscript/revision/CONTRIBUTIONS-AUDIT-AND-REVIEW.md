# Contributions, platform coverage, numeric audit, clean build and simulated review - November 4, 2026

This revision follows [ROADMAP-AUDIT-AND-SURVEYS.md](ROADMAP-AUDIT-AND-SURVEYS.md). The selection and the bibliography are unchanged: 229 selected works and 9 background references, 238 references in total, all from 2021-2026.

## Contributions

The contribution list in Section I now states the two results that earlier revisions added.

- The second contribution reports the coded evidence of the 228 technical publications and the finding that only 26% report task outcomes under a designed degradation.
- The third contribution states that each of the four open interfaces comes with a matched comparison (Table V).

## Platform coverage in the evidence map

Table IV gains a row, "Evaluated on a wheeled robot", computed from `boundary_platform` in the corpus coding:

| Section | IV | V | VI | VII | VIII | All |
|---|---:|---:|---:|---:|---:|---:|
| Publications | 66 | 52 | 30 | 40 | 40 | 228 |
| Evaluated on a wheeled robot | 30 | 47 | 25 | 29 | 30 | 161 |

More than half of the localization and mapping studies (36 of 66) evaluate on road vehicles, other embodiments, handheld or mixed rigs, or without a specified physical platform. The synthesis of Section IV and the evidence subsection of Section IX now state this. `build_data.py` asserts both statements ("more than half" for Section IV and "most" for Sections V-VIII), and `verify_delivery.py` recomputes the row.

## Numeric audit

[numeric-audit.json](numeric-audit.json) covers every sentence in Sections IV-X that reports a numerical result. That is 22 sentences:

- 10 belong to the source-checked comparison records in `data/within-study-comparisons.json`.
- For the other 12 (R05, R07, R13, R14, R19, R24, R25, R26, R27, R32, R33 and N20), every number was found in the review card with a page locator. The numbers of each sentence also occur together in one passage of the local full-text transcription.

No mismatch was found. The record lists the manuscript sentences, the numbers and the card locators, and source excerpts remain local.

## Space

Five repeated statements were removed to keep the paper at 24 pages: a benchmark sentence in Section IV that repeats Section II, the resource-accounting sentence of Section IX, which Section X covers, and three sentences in Section X that repeat Sections VIII and IX. Every citation in them remains cited elsewhere. The last page is balanced at 685 and 622 pt with `\IEEEtriggeratref{225}`.

## Clean-checkout build

The repository was cloned fresh from GitHub at `ad8328e`. In the clone, the data were regenerated, both PDFs built, the public verification ran, and the library checks passed: tests, strict table and index rebuilds, links and the public tree. The clone contains no publisher PDFs or transcriptions. One reproducibility defect surfaced and was fixed. `citation_scope_sha256` and `inclusion_sha256` were hashes of raw bytes, so a checkout with different line endings produced different hashes. `build_data.py` and `verify_delivery.py` now hash these two JSON files with CRLF normalized to LF (`text_digest`). The clone and the working copy then agree, and the regenerated files differ from the committed ones only in line endings. [clean-checkout-verification.json](clean-checkout-verification.json) records the run and replaces the earlier two-repository record.

## Verification

`python scripts/verify_delivery.py` and `--sources` pass: 24 pages, 229 corpus citations in prose, 238 resolved references, 27 unique labels, three figures, five tables, six unchanged equations and no unresolved references. The source mode checks 693 local artifacts with no hash mismatch. Sentence rhythm: 543 sentences, mean 21.4 words, 11% under 12 words, 6% over 35 words, with no style flags and a clean house-style scan.

## Simulated review

Two reviewers on different models reviewed commit `5249a0f` independently, and a third step merged their reports. All three reports are kept locally under `99-archive/local/reviews-2026-11-04/` and are not published. This is an internal simulated review, not an editorial decision.

Both reviewers recommend major revision, and neither recommends rejection. Across 24 spot-checked works, no reported number contradicts its source. Both reviewers rate the treatment of denominators, censoring, reference dependence and timing in Section IX as a useful contribution. The merged report lists nine major items:

- Selection reproducibility: the stage counts and the language-model screening appear only in the supplement, and inclusion criteria and an AI-use disclosure are missing.
- Validity of the Table IV coding: there is no codebook and no agreement check. "Degradation testing" mixes manipulated, selected and incidental conditions, and the pooled 26% needs a sample qualifier.
- Derivation of the four interfaces: part of the corpus was selected for them. Rejected candidates and protocol details for Table V are not given.
- The degradation-based organization is claimed but only the function axis is used.
- Wheeled versus non-wheeled evidence: non-wheeled anchors are not flagged, and drivetrain consequences are missing.
- Positioning: Table I has no objective columns, and automated-driving concepts such as minimal risk maneuvers are not discussed.
- Foundational references: these are withheld by the 2021-2026 citation rule.
- Catalogue-style synthesis in Sections IV-VIII.
- Coverage gaps and the 2025-2026 recency skew.

The merged report also lists 21 minor items. They include framing corrections for four studies (the osmAG-LLM end-to-end denominator, the speed-matched MonoMPC comparison, the outdoor baselines of terrain-adaptive MPC, and context for LeLaN, VAMOS, mEclares and Help Me Through), as well as scoring definitions for Fig. 3, Table IV row definitions, index terms and figure type size. Which items to act on is an author decision. Several of them conflict with earlier decisions: the short Section III, the 2021-2026 citation rule, and the 24-page limit.
