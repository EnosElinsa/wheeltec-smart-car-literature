# Contributing and maintenance

The repository owner maintains the library and the manuscript. To report an error in a review card, a data value or the manuscript, open a GitHub issue that names the paper ID, the file and the physical PDF page of the evidence. This guide records the conventions and procedures that the maintainer follows.

Contributions are accepted under the license of the part they change: MIT for code and CC BY 4.0 for cards, analyses, data and documentation (see the [license table](README.md#license)). The manuscript carries no license before publication.

## Conventions

- **Language.** Research prose and documentation are in English. Review prose uses American English and writes "LiDAR". Excerpts and original abstracts are verbatim. The reading interface, its project JavaScript, generated `INDEX.html` and `06-data/open-source-projects.json` use Chinese labels and project descriptions. These explicitly listed UI files and hash-registered verbatim source transcriptions are exempt from the CJK-text check. All path, credential and source-asset checks still apply. `tools.check_public_tree --cjk strict` rejects CJK text elsewhere.
- **Names.** File and directory names use English ASCII. A paper folder is `<theme>/<year>-<short-name>-<ID>/` and uses the same name in `01-papers/`, `02-fulltext/` and `03-reviews/`. IDs never change once assigned (see the [source policy](06-data/source-policy.md)).
- **Public content.** The owner authorizes publishing admitted reading PDFs, canonical transcriptions and images through Git LFS. Register their exact hashes and sizes in `06-data/reading-assets.json`; preserve original bytes and third-party rights. Keep the historical archive, extraction diagnostics, acquisition state and credentials local. `tools.check_public_tree` permits only registered source assets, while `tools.check_lfs_assets` checks catalog identities, bytes or pointers, and LFS filters.
- **Source bytes.** Publisher BibTeX exports keep their original bytes (`.gitattributes` disables line-ending conversion for `*.bib`). A derived `citation.bib` needs the owner's explicit authorization, keeps the export beside it (for example as `citation-original.bib`) and records the change in the paper's `provenance.json`.
- **Encodings.** The data files do not share one byte layout. For example, `paper-index.csv` and `corpus-comparison.csv` use UTF-8 with a byte-order mark and CRLF line endings, while `library-catalog.csv` and the files in `06-data/evidence-coding/` use UTF-8 without a byte-order mark and LF line endings. Keep each file's encoding and line endings when editing it, preferably with a script.
- **Frozen records.** The codebook text, `primary-codes.csv` and `primary-locators.csv` in `06-data/evidence-coding/` are hash-frozen. A code correction is a new row of `adjudication-log.csv`. A card correction is recorded in `06-data/review-corrections.csv`.
- **Dated records.** Batch records in `06-data/<batch>/`, analyses in `04-analysis/` and revision records in `05-survey/manuscript/revision/` describe their own date. Do not update their counts; add a new record instead. Current totals live in the [README](README.md), the generated indexes and the manuscript's [revision status](05-survey/manuscript/REVISION-REPORT.md).

## Review cards

Write and check a card as described in [03-reviews/WORKFLOW.md](03-reviews/WORKFLOW.md), with the structure of [TEMPLATE.md](03-reviews/TEMPLATE.md) and the values of [vocabulary.md](06-data/vocabulary.md). Record `verification_level: full` only for a whole-paper reading with numbers checked against rendered PDF pages. Every other card is `light` and names the passages that were read.

## Adding a batch of papers

1. Register each paper's PDF and BibTeX under `01-papers/<theme>/<folder>/` and its transcription under `02-fulltext/`. Keep a batch folder `06-data/<batch-name>/` with the manifest (sources, hashes and acquisition status), the reading ledger and a README.
2. Write the review card `03-reviews/<theme>/<folder>/review.md`.
3. Append one row per paper to `06-data/paper-index.csv`, filling the 22 identity and source columns (`code` to `markdown_sha256`, with `source_batch` set to the batch name). Then run `python -m tools.build_tables --strict`, which fills the coding columns from the cards and rewrites `corpus-comparison.csv`.
4. Add the IDs that join the survey to `selected_ids` in `06-data/survey-inclusion.json`. Every indexed paper must be either selected or listed in `internal_reference_ids`.
5. Run `python -m tools.build_indexes --strict` and the checks below.
6. If the manuscript changes, rebuild it as described in the next section.

## Maintaining the project directory

Edit `06-data/open-source-projects.json`, then run `python -m tools.build_indexes --strict` to regenerate `OPEN_SOURCE_PROJECTS.md` and `INDEX.html`. Follow the field rules and browser checks in [the interface guide](06-data/index-interface.md). Resolve each paper link by its exact DOI or official publication URL, retain the textbook source revision and record the date of repository checks. Runtime tags describe available implementations, including separately linked integrations; put the specific ROS distribution and portability limits in the adaptation notes. Keep diffusion policies, self-supervised representations and reinforcement learning distinct. Do not infer licenses, deployment success or journal rankings from project names.

The textbook chapter and README link to the portable directory through public URLs, so either repository can be cloned independently. Changes to the paper collection, review cards or survey selection follow the separate procedures in this guide.

## Manuscript changes

The [manuscript guide](05-survey/manuscript/README.md) gives the commands. In short:

1. Run `python scripts/build_data.py` and, after figure changes, `python scripts/build_figures.py` in `05-survey/manuscript/`.
2. Build `supplement.tex` before `survey.tex`, because the main paper cites supplement labels through `xr`. Use `latexmk -gg` after section or supplement edits, since a plain run can report that the targets are up to date.
3. Run `python scripts/verify_delivery.py`, and add `--sources` when the local sources are present. The verifier asserts label counts, cross-references, equations, numerical cases, page limits and citation coverage. A change to labels or cross-references updates its assertions in the same commit.
4. After any change in text length or references, check the balance of the last page and reset `\IEEEtriggeratref` in `survey.tex` if needed.
5. Record the round in `revision/REVIEW-FIXES-<n>.md` and update the pointers in `REVISION-REPORT.md`, `05-survey/manuscript/README.md` and `revision/README.md`.

## Checks before a commit

```shell
python -m pytest
python -m tools.build_indexes --strict
python -m tools.check_links
python -m tools.check_public_tree --cjk strict
python -m tools.check_lfs_assets
python -m tools.review_check --all --pdf
```

The last command needs the local PDFs and transcriptions. Run `git status` afterwards: a check that regenerates a file should leave no diff. The [Checks workflow](.github/workflows/checks.yml) repeats the first four checks and `python -m tools.build_tables --strict` on GitHub for every push to `main`.

## Commit messages

Start the subject with the area, followed by an imperative summary, for example `Library: add 16 reviewer-named works (K01-K16)`, `Survey: concise review method` or `docs: update batch guide`. Keep a round prefix such as `round5 data:` for the steps of one manuscript revision round.
