# Evidence coding of the survey selection

This folder holds the coding layer that the survey uses for its degradation-evidence statistics. It codes the 245 works of the survey selection (244 technical works and one context review) for degradation source, the three degradation-evidence classes, task outcomes in the same experiment, evidence level, response family, platform group and drivetrain. The review cards in `03-reviews/` and the comparison tables of `06-data/` stay unchanged. For manuscript statistics, the codes of this folder replace the card fields `degradation`, `degradation_observed` and `evaluation_all`, and the card-level counts of the previous revision remain one sensitivity row.

| File | Content |
|---|---|
| [codebook.md](codebook.md) | Codebook version 1.0: operational definitions, allowed values, decision rules, locator rules, consistency rules, the coding unit, the attributes marked for double coding, the sampling procedure with its seed, and the interface ranking, sensitivity analyses and robustness findings fixed before coding |
| [codebook.json](codebook.json) | The same codebook in machine-readable form, checked against `codebook.md` by `python scripts/coding.py --check-codebook` (run in `05-survey/manuscript`) |

Files added once they exist:

- `primary-codes.csv` and `primary-locators.csv`: primary codes of all 245 works and a source location for every coded value, frozen before agreement is computed (`freeze.json` holds their SHA-256).
- `sampling.json` and `sample-manifest.csv`: the drawn sample of 40 technical works with seed, attempt index, strata and draw order, published after the independent coding is complete.
- `second-codes.csv`, `second-locators.csv` and `second-coder-record.json`: the independent coding of the sample and its session record.
- `adjudication-log.csv`: every disagreement with its resolution, reason and deciding locator.

Derived products (per-paper final codes, column percentages, the degradation-source by function matrix, the function-pair co-occurrence matrix, interface candidates and sensitivity tables) are written by `05-survey/manuscript/scripts/build_data.py` into `05-survey/manuscript/generated/`.

## Provenance

The codebook was drafted in a language-model agent session on 2026-11-04, before any work was coded. It fixes the seed (20261105) and the stratified draw rule of the sample, and the draw is reproducible with `draw_sample` in `05-survey/manuscript/scripts/coding.py`. Both coding passes are made by language-model sessions: the primary coding of all works, and an independent second coding of the sample in a separate session on a different model without access to the primary codes. Their agreement measures how consistently two language-model coders apply this codebook to shared evidence. It is not human inter-rater reliability. The session records state host and model where the session configuration records them.

All files use UTF-8 without a byte-order mark and LF line endings. They contain no publisher text and no local paths.
