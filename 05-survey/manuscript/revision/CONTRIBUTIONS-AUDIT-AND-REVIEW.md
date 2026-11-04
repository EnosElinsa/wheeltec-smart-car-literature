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

The simulated two-reviewer T-IV review of this version is reported below once it completes.
