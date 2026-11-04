# Figures, condensation and repository merge - November 4, 2026

This revision follows the [IEEE refresh integration](IEEE-REFRESH-INTEGRATION.md). It redraws the figures as SVG, condenses the text, shortens Section III, corrects the reference formatting and moves the manuscript into the evidence-library repository. The selection is unchanged: 229 selected works and 5 background references, 234 references in total, all from 2021-2026.

## Figures

All figures are drawn by `scripts/build_figures.py` with the helpers in `scripts/svgkit.py`. Each figure is written as an editable SVG and converted to a vector PDF with PyMuPDF. The TikZ sources `fig-stack.tex`, `fig-degradation.tex` and `fig-eval-objects.tex` and the generated `fig-corpus-stats.tex` were removed, and `survey-format.tex` loads `graphicx` instead of TikZ and pgfplots.

| Figure | Content | Change |
|---|---|---|
| Fig. 1 `fig-taxonomy` (Introduction) | Five functional sections, their response families with representative methods, the three evaluation axes of Section IX and the four numbered open interfaces of Section X | New |
| Fig. 2 `fig-stack` (Section II) | Navigation functions colored by reviewing section, degradation entry points and the numbered open interfaces | Merges the former stack and degradation figures |
| Fig. 3 `fig-evaluation` (Section IX) | One episode on synchronized lanes: operating condition, internal signals with a false alarm, executed response and task outcome, with detection delay, response delay and recovery time | Redrawn |
| Fig. S1 `fig-corpus` (supplement) | Selected publications by year and principal function | Redrawn from `generated/corpus-year-module.json` |

The main paper keeps three figures and 30 labels, since `fig:taxonomy` replaces the former `fig:degradation`.

## Condensed text

Sections were rewritten with grouped citations and merged comparisons. Every selected work is still cited in substantive prose, the six displayed equations match their hash baseline, and the tables are unchanged. Approximate source word counts:

| Section | Before | After |
|---|---:|---:|
| I Introduction | 734 | 652 |
| II Background | 1,761 | 1,382 |
| III Scope and literature selection | 339 | 225 |
| IV Localization and mapping | 3,573 | 1,804 |
| V Traversability, planning and control | 3,299 | 1,631 |
| VI Semantic navigation | 2,175 | 1,158 |
| VII Multi-robot coordination | 2,413 | 1,181 |
| VIII Fault tolerance and recovery | 2,796 | 1,173 |
| IX Evaluation practice | 1,997 | 1,256 |
| X Open challenges | 2,090 | 1,793 |
| XI Conclusion | 228 | 241 |
| Total | 21,405 | 12,496 |

Section III now states scope, eligibility, sources, the purposive and language-model-assisted selection, incomplete 2026 and proceedings coverage, and the comparison principle. Stage counts, the acceptance cap, unassessed records, assessment depth and the PDF rechecks are reported in Supplement Sections S1-S3, which already held them. The supplement's own semicolons and ", but" clauses were also removed.

The abstract (216 words) names the corpus size and the organizing principle and uses the interface names of Section X. Section X opens with the numbering shared by Figs. 1 and 2.

## Style measurements

The house-style scan finds no "so", "because", semicolon, ", but", "e.g.", "we", "our" or "Hence" in the main text or supplement prose. Table cells keep commas instead of semicolons. Sentence statistics of the body (`rhythm.py`, sentences of four or more words): before, mean 16.1 words with 24% under 12 words; after, mean 23.0, median 22, 13% under 12 words and 11% over 35 words, within the team band of 21.4-23.8 words and 9-14% short sentences. The `style_fingerprint.py` count, which also counts short headings and fragments, gives a body mean of 22.9 words and 16% under 12 words.

## Bibliography formatting

`scripts/bib_case.py` brace-protects title words whose case carries meaning (acronyms, mixed-case method names, digit-letter tokens and listed proper names such as Gaussian or Voronoi) before IEEEtran applies sentence case. It also unwraps titles that a publisher export braced as a whole, so they follow the same rule. Earlier builds printed, for example, "Care", "Selfi", "slam" and "rl". `ieee-bst-control.bib` lists the first author followed by "et al." for the 39 entries with more than six authors, following the IEEE reference style. Publisher files in the library are unchanged.

## Length

The main paper fell from 36 to 26 pages: text on pages 1-20 and references on pages 20-26. The T-IV maximum is 24 pages (18 plus 6 paid). The reference list alone takes about six and a half pages, and the five module tables (Tables III-VII) take about one column each. The remaining options are to move the module tables to the supplement (about 2.5 pages), to shorten each table to fewer representative rows, or to cut further prose. Each option changes content, so it is left to the authors.

## Repository merge

The manuscript was a separate Git repository (`EnosElinsa/wheeltec-navigation-survey`, last commit `8800270`). It is now ordinary tracked content of this repository at `05-survey/manuscript/`. Its history is preserved in a local bundle under `99-archive/local/`, which is excluded from the public tree. `scripts/project_paths.py` now resolves the library as the repository root (or `WHEELTEC_LITERATURE_ROOT`), and `verify_delivery.py` records one `base_commit` instead of two source commits.

## Verification

`python scripts/verify_delivery.py` and `python scripts/verify_delivery.py --sources` pass: 229 corpus citations in prose, 234 resolved references, 30 unique labels, three figures, eight tables, six unchanged equations, no unresolved references, no overfull boxes and no LaTeX warnings. The source mode checks 693 local PDF/BibTeX/Markdown artifacts with no hash mismatch. The supplement has three pages, seven labels, one figure and two tables. The figures and the last reference page were checked visually, and `\IEEEtriggeratref{220}` balances the last page.
