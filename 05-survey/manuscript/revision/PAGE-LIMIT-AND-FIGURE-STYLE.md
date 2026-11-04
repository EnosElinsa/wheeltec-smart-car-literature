# Page limit, synthesis table and figure style - November 4, 2026

This record describes the state after this revision. [EVIDENCE-MAP-AND-PROSE.md](EVIDENCE-MAP-AND-PROSE.md) supersedes its page count (now 24), Table IV description, word counts and style measurements.

This revision follows [FIGURES-AND-CONDENSATION.md](FIGURES-AND-CONDENSATION.md). It brings the main paper within the 24-page maximum of IEEE T-IV surveys, adds a cross-function synthesis table, revises the prose of Sections I-IX, and redraws the figures in a grayscale journal style. The selection is unchanged: 229 selected works and 5 background references, 234 references in total, all from 2021-2026.

## Length

The main paper fell from 26 to 23 pages. The five module tables, formerly Tables III-VII, moved to a new final supplement section, S5 "Representative Implementations by Navigation Function", as Tables S3-S7. Their content is unchanged. The main text cites them through the `xr` package (`\externaldocument[S-]{supplement}` in `survey.tex`, references written as `\ref{S-tab:localization}`), so the supplement must be compiled before the main paper. The supplement grew from three to eight pages and from 8 to 65 references, since the moved tables cite their implementations. The `balance` package was removed from the supplement. `\IEEEtriggeratref{220}` balances the last reference page of the main paper (left column 685 pt, right column 676 pt).

Shortening the tables to fewer rows and cutting more prose were the alternatives. Both would have removed comparisons, while the move keeps every row and every prose citation.

## Synthesis table

Table III (`tab:synthesis`, end of Section VIII) replaces the moved tables in the main text. For each of the five navigation functions it lists the main responses to degradation, the conditions under which they help and the main evidence gaps in the reviewed studies. It closes Sections IV-VIII and opens Section IX, whose first paragraph now argues from its last column that most open questions concern evaluation. Fig. 3 now follows the first subsection of Section IX.

## Prose

Sections IV and V were rewritten in full, and Sections I-III and VI-IX were revised sentence by sentence. The revision splits ", and" joins of two independent claims, gives each subsection a clear topic sentence, keeps short topic and transition sentences, and merges short fragments whose referent was unclear. Section titles use title case. Approximate source word counts, before the November 4 condensation and now:

| Section | Before | Now |
|---|---:|---:|
| I Introduction | 734 | 659 |
| II Background | 1,761 | 1,409 |
| III Scope and literature selection | 339 | 227 |
| IV Localization and mapping | 3,573 | 1,856 |
| V Traversability, planning and control | 3,299 | 1,654 |
| VI Semantic navigation | 2,175 | 1,182 |
| VII Multi-robot coordination | 2,413 | 1,208 |
| VIII Fault tolerance and recovery (with Table III) | 2,796 | 1,535 |
| IX Evaluation practice | 1,997 | 1,346 |
| X Open challenges | 2,090 | 1,793 |
| XI Conclusion | 228 | 241 |
| Total | 21,405 | 13,110 |

Style measurements: `rhythm.py` gives 508 sentences with mean 22.0 words, median 20, 9% under 12 words and 9% over 35 words, within the team band of 21.4-23.8 words and 9-14% short sentences. `style_fingerprint.py` gives a body mean of 21.8 words with 11% under 12 words, sentence-initial "However" at 1.4 per 100 sentences and no flags against the house-style band. The house-style scan finds no "so", "because", semicolon, ", but", "e.g.", "we", "our", "Hence" or "which means" in the main text or supplement.

## Figure style

`scripts/svgkit.py` and `scripts/build_figures.py` were rewritten for a print journal style:

- Text is set in Times, matching the IEEEtran body font.
- Graphics are grayscale: near-black ink, two gray rules, a light fill for emphasis and a gray ramp for the corpus bars. No figure depends on color.
- Boxes have thin rules and square corners, arrows have slim heads, degradation sources use dashed boxes, and the four open interfaces are circled numerals 1-4 in Figs. 1 and 2 and Section X.
- Dashes are drawn as separate segments with a consistent phase, since PyMuPDF ignores SVG dash arrays.

The captions of Figs. 2 and 3 no longer refer to colors. Fig. 3 shades the degraded interval and defines a false alarm as a threshold crossing outside it.

## Repository

The former manuscript repository `EnosElinsa/wheeltec-navigation-survey` was deleted on GitHub with the owner's authorization, after checking that its branch heads matched the local backup bundle and that it had no issues or releases. Its history remains in the bundle under `99-archive/local/`, which is excluded from the public tree. This repository is the only public repository of the project.

## Verification

`python scripts/verify_delivery.py` and `python scripts/verify_delivery.py --sources` pass. The verifier now asserts at most 24 main-paper pages, 26 unique main labels, 13 supplement labels disjoint from the main labels, and that the main text's `S-` references are exactly the five supplement tables. It reports them separately as `supplement_references`. Results: 23 pages, 229 corpus citations in prose, 234 resolved references, three figures, four tables, six unchanged equations, no unresolved references, no overfull boxes and no LaTeX warnings. The supplement has eight pages, 65 resolved references, one figure and seven tables. The source mode checks 693 local PDF/BibTeX/Markdown artifacts with no hash mismatch. All pages were checked visually on a contact sheet.
