# How reviews are written and verified

Every `review.md` in this folder follows [`TEMPLATE.md`](TEMPLATE.md) and the
controlled vocabulary in [`../06-data/vocabulary.md`](../06-data/vocabulary.md).
A worked example is
[`T1-perception-localization/2022-slip-aware-fusion-M39/review.md`](T1-perception-localization/2022-slip-aware-fusion-M39/review.md).

## Sources and their roles

| Source | Role |
|---|---|
| `01-papers/<theme>/<folder>/paper.pdf` | Publisher PDF. Authority for numbers, tables, figures, and page numbers. Local only. |
| `02-fulltext/<theme>/<folder>/paper.md` | Source transcription of the PDF; extraction mode is recorded in provenance. Used for reading and excerpt matching. Local only. |
| `01-papers/<theme>/<folder>/citation.bib` | Publisher BibTeX export. Authority for authors, venue, volume, and pages. |
| Earlier review text (Git history, and the archive `99-archive/history-2026-10-25.zip`) | Legacy extraction by an automated reviewer. Treated as a set of claims to check, never as evidence. |

PDFs, transcriptions, and the archive are excluded from the public repository
for copyright reasons. Reviews therefore name them as code-formatted paths
instead of links.

## Procedure for one paper

1. Run `python -m tools.locate <ID> --info` to get the paths, DOI, URL, and
   page count.
2. Read the template, the vocabulary, the worked example, the earlier review,
   and `citation.bib`.
3. Read the whole `paper.md`, including appendices; the reference list can be
   skipped.
4. Check every statement of the earlier review against the full text. Keep
   what is correct, correct what is wrong, and drop what the paper does not
   support. Record each correction (see below).
5. Find the physical PDF page of each number and excerpt with
   `python -m tools.locate <ID> --find "<phrase>"`. Read raw page text with
   `--page N`. Tables are often images without a text layer, and MinerU can
   move, merge, or drop table cells. Before using any number from a table or
   figure, render the page with `python -m tools.locate <ID> --render N`
   (written to `tmp/render/<ID>-p<N>.png`), open the image, and read the
   values from it. Name the tables read this way in the verification log.
6. Write the review in English. Excerpts are verbatim and contiguous (no
   ellipses). The original abstract is the authors' abstract as printed in
   the paper; journal highlights are not an abstract.
7. Run `python -m tools.review_check <path-to-review.md> --pdf` and fix every
   error. Warnings about approximate matches are acceptable when the excerpt
   was checked by eye against the PDF.
8. Record corrections in `06-data/review-corrections.csv` with the columns
   `id, section, issue, old_summary, corrected, pdf_page, evidence`.

The procedure above produces `verification_level: full`. It is used for the
key papers of `READING_GUIDE.md`.

## Light conversion

Papers outside the key set get `verification_level: light`. A light
conversion does not read the whole paper.

1. Run `python -m tools.locate <ID> --info`; read the earlier review and
   `citation.bib`.
2. Translate and restructure the earlier review into the template (all
   sections, American English, "LiDAR"). Keep only what the earlier review
   states and add no new claims. Where it has nothing for a section, write
   "Not recorded in the legacy extraction; not verified." Metadata comes from
   `06-data/paper-index.csv` and `citation.bib`.
3. Code the review from the vocabulary with the information of the earlier
   review, following the coding rules below.
4. Keep an earlier verbatim quote only if `python -m tools.locate <ID> --find
   "<quote>"` finds it, and take its page from that result; drop the quote
   otherwise. When fewer than two quotes remain, or a claim row lacks a found
   excerpt, take short verbatim sentences from the abstract or conclusion,
   located with `--find`.
5. Key quantitative results are the numbers of the earlier review. Give each
   the page that `--find` returns for a phrase containing the number when
   possible; a result without a page is a warning for light reviews, not an
   error.
6. Copy the original abstract verbatim (`python -m tools.locate <ID>
   --abstract`).
7. Write the verification log line with the scope "light conversion of the
   legacy extraction; metadata, abstract, and excerpts checked mechanically;
   numbers not re-verified", plus the legacy line.
8. Run `python -m tools.review_check <path-to-review.md> --pdf`; it must pass
   (warnings are allowed). Record the format change and every dropped quote
   as corrections.

Numbers in a light review are not re-verified. The survey must re-check any
number it cites from a light review against the paper.

## New targeted light reviews

New follow-up papers can have a light review without an earlier extraction.
Read the publisher identity and abstract, then selected method, setup,
evaluation, and limitation passages that answer the recorded follow-up
question. Log the actual sections and physical PDF pages read. Do not claim
whole-paper verification or a legacy conversion when neither occurred.

Use the same template and vocabulary. Mark uninspected details as unknown
or not verified. Check each retained excerpt on its physical PDF page and
against the bound source transcription (MinerU or the explicitly recorded local extraction). Check any retained numeric claim in
the selected source passage; table/figure values require a rendered-page
check. A number omitted from this limited reading stays unverified. Keep
author-stated limitations separate from reviewer transfer conditions.

Record `verification_level: light` and complete the ordinary `review_check
--pdf` validation after the transcription exists. A drafted card with a
pending transcription is not a completed review. Later survey citations
still require a targeted numeric recheck. The historical conversion logs
retain their original, narrower scope.

## Scanned PDFs

`tools.locate` and `tools.review_check --pdf` use embedded PDF text first.
For image-only pages they can use PyMuPDF's Tesseract OCR with an English
`eng.traineddata` model supplied through `TESSDATA_PREFIX`, a system
tessdata directory, or the local `.local/ocr/tessdata/` folder. The November 2
run used the model from the official `tesseract-ocr/tessdata_fast` repository.
The model and OCR output stay local. The original PDF is never rewritten.
OCR cache identities include the PDF hash, model hash, and PyMuPDF version;
changing the source invalidates the cache. Without a model, blank pages
cannot pass excerpt checks. Inspect cited scanned pages visually as well:
OCR can interleave columns or misread symbols. Record that scope in the log.

## Coding rules that need judgment

- `evidence_type` is the strongest setting in the paper. A real-time
  estimator that runs on a moving robot without driving it is
  `online-hardware`; an estimator run later on the authors' recorded data is
  `recorded-robot-data`; public datasets only is `dataset-playback`.
- `platform_class` follows the strongest setting. A wheeled ground robot
  takes precedence when several platforms appear in that setting.
- `survey_module` is the module that the paper's main contribution belongs
  to, regardless of the theme folder.
- `evaluation_all` includes `designed-degradation` only when results are
  reported per named condition (for example per surface, map age, or
  communication cutoff).
- `summary_result` and `summary_limitation` are single sentences of at most
  30 words, with the condition attached to every number.
- `degradation` holds the conditions that the evaluation deliberately
  includes; conditions met in a field study go to `degradation_observed`;
  conditions mentioned only as motivation are not coded.
- `platform_class` needs a source for the drive type (text, cited source, or
  a named figure). Without one, use `wheeled-unspecified`.
- `protocol_caveats` describe the setting behind the tabulated headline
  results. Side demonstrations without metrics are described in prose.
- `compute_location` is `desktop-offline` for a server that processes
  recorded data while no robot is live.

## Writing rules

- Stated limitations contain only what the authors state, each with a page.
  Reviewer observations go to Transfer conditions.
- In comparisons, the method comes first and the comparator second, in the
  label and in the values.
- Say when a comparator appears only in plots, so that a reader does not
  assume a numeric comparison.
- A "best on every sequence" statement in Not supported lists every
  counterexample or gives the count.
- Record inconsistencies inside the paper (for example a count that does not
  match a range) once, where the number is first used.
- Use American English and "LiDAR" in review prose; keep excerpts verbatim.

## Verification log

Each review ends its verification log with a dated line by the host that
performed the check, in the form

```
- YYYY-MM-DD | host: Kiro | scope: <what was read and checked> | corrections: <summary>
```

Use `host: Codex` for checks performed in Codex. Keep historical host entries
unchanged; accepting a platform name does not establish the logged checks.

and keeps one line that names the legacy extraction and, for the expansion
batch, the archived evidence files as
`99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/<group>/<selection-id>/`.
