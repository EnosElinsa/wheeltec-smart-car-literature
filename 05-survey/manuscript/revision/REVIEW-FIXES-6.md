# Review fixes, round 6: concise method section, acknowledgment and figures - November 5, 2026

This revision follows [REVIEW-FIXES-5.md](REVIEW-FIXES-5.md). It answers the author's requests of 2026-11-05: a shorter Section III without the batch-by-batch account, a short AI-use acknowledgment, and clearer figures. It also closes the two findings left open by the last check of round 5.

## Section III
- The section is now titled "Review Method" and has three short paragraphs: scope and eligibility, corpus selection, and coding.
- The selection table moved to supplement S1 (Table S1, `tab:selection`, unchanged rows). The main paper no longer lists the selection stages, the screening archive counts, the venue mix or the stage dates. Supplement S1 keeps all of them.
- The selection paragraph states that the corpus was built in purposive stages, from a language-model-assisted journal screening extended by theme-balanced and targeted searches and by works named in an internal review of an earlier draft. It keeps the IEEE share (`\IEEEShare`) and the 2025-2026 share (`\RecentShare`), and it states that the counts describe the selected literature.
- The coding paragraph keeps the three evidence classes, the same-experiment rule, the second coding of the sampled works with the median kappa (`\KappaMedian`), and the statement that this agreement is between two language-model coding passes and not human inter-rater reliability. The kappa range stays in supplement S7.
- `verify_delivery.py` now expects 29 main labels and 23 supplement labels, with `tab:selection` in the supplement. The main paper refers to S1 instead of the venue-mix table.
- [claim-audit.json](claim-audit.json) records the two moved Section III claims under `round6_moved_or_shortened`.

## Acknowledgment
The acknowledgment is now three sentences. It names the language-model agents Codex and Kiro and the tasks they assisted with: literature screening, reading notes, the evidence coding of Section III, and drafting and revision. It names MinerU and the OXR-1.0 model for the PDF transcriptions and keeps the authors' responsibility statement. The configured coding models and the note on unrecorded executed models stay in the public coding record (`06-data/evidence-coding/second-coder-record.json` and its README) and in [REVIEW-FIXES-4.md](REVIEW-FIXES-4.md). The IEEE policy requires the disclosure itself, so it is kept in short form.

## Open findings of round 5
- **S7 headline sentence.** It had read "Adjudication changed the headline count from 81 to 81" after the third commit of round 5. It now reads "The headline count is 81 in the frozen primary codes and 81 after adjudication and the later rechecks", which states the net result without claiming a change.
- **Counts table of round 5.** The table in [REVIEW-FIXES-5.md](REVIEW-FIXES-5.md) now lists the Table VI and S8 rows, the sensitivity, co-occurrence and candidate-table changes, and the four IX-B shares moved by the third commit. Each value was compared between commits 6333140 and e460b88.

## Figures
- **Fig. 2.** Each degradation group now sits directly above the function box it enters, with one short arrow. Sensing and estimation enters Measurements and State estimation. Environment and map change runs down the lane between State estimation and Representation. Communication and computation enters Teammates, learned and semantic inference enters Task interpretation, and terrain and mobility enters Control. No entry arrow crosses a box, another arrow or the main information flow. The long cross-figure line from the communication group and the second branch of the learned-inference group into Planning were removed. The supervision links and the interface numerals keep their meaning. The caption is unchanged.
- **Fig. 1.** The four evidence shades are evenly spaced (white, #EFEFEF, #D3D3D3, #B4B4B4). The platform line in the darkest cells is set in black.
- Fig. 3 and Fig. S1 are unchanged.

## Length and verification
- The main paper has 24 pages. The shorter Section III moved the last references into the left column, and `\IEEEtriggeratref{264}` now balances the last page: references 258-263 end at 317 pt and 264-270 at 353 pt. The supplement keeps 17 pages.
- `build_data.py`, `build_figures.py`, `latexmk -gg` of the supplement and the main paper, `verify_delivery.py` and `--sources` pass. Neither log has an Overfull, undefined or LaTeX Warning line.
- All corpus and background keys are cited in prose. Sentence rhythm: mean 23.3 words, 12% under 12 words. The house-style scan of the new text is clean, and its ", and" joins are list joins.
- Library checks pass: pytest, `build_tables --strict`, `build_indexes --strict`, `check_links` and `check_public_tree --cjk strict`.
