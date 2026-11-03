# <Full paper title, exactly as published>

<!--
Review template for 03-reviews. Copy this file to
03-reviews/<theme>/<year-short-name-ID>/review.md and replace every <...>.
Keep the section headings and their order: tools/review_check.py checks them.
Write in American English ("localization", "behavior") and write "LiDAR" in
review prose; excerpts keep the paper's original spelling. Page numbers are
physical PDF pages ("p. 7"), not the printed page numbers of the journal.
Comments like this one are removed in real reviews.
-->

## Metadata

| Field | Value |
|---|---|
| ID | <M39> |
| Title | <Full title> |
| Authors | <First Author, Second Author, and Last Author> |
| Venue | <Journal or proceedings name> |
| Year | <journal: bibliographic year, plus "(online YYYY)" when the article appeared online in an earlier year; conference: proceedings year, plus "(conference YYYY)" when the meeting year differs> |
| Type | <journal or conference> |
| DOI | <[10.xxxx/yyyy](https://doi.org/10.xxxx/yyyy) or "none (see official URL)"> |
| Official URL | <publisher landing page> |
| Theme folder | <T1-perception-localization> |
| Batch | <baseline-2026-09-18, supplemental, expansion-2026-10-24, or followup-2026-11-02> |
| Local files | `<01-papers/.../paper.pdf>` and `<02-fulltext/.../paper.md>` (local only, not in the public repository); add a relative link to the paper's `citation.bib` |

## Survey coding

<!-- Values must come from 06-data/vocabulary.md. Keep one "- key: value" line per field. -->

- survey_module: <localization-mapping>
- secondary_modules: <none>
- evidence_type: <closed-loop-hardware>
- evidence_all: <closed-loop-hardware, dataset-playback>
- protocol_caveats: <none>
- platform_class: <skid-steer>
- platform: <Clearpath Jackal>
- boundary_platform: <no>
- degradation: <wheel-slip, terrain>
- degradation_observed: <none>
- evaluation_primary: <residual>
- evaluation_all: <residual, designed-degradation>
- sensors: <wheel encoders, IMU>
- compute: <Intel NUC onboard; 0.02 s sampling period>
- compute_location: <onboard>
- summary_result: <One sentence with the main number and its condition.>
- summary_limitation: <One sentence with the main stated limitation.>
- survey_included: <yes>
- verification_level: <full or light; see 06-data/vocabulary.md>

## Problem

<What problem the paper solves and under which operating condition. Two to four sentences.>

## Mechanism

<How the method works: model, estimator or planner structure, key design choices. Name parameters that matter for transfer.>

## Baselines and controls

<Named baselines, ablations, and what is held fixed. State when a baseline was re-implemented or modified by the authors.>

## Platform and setup

<Robots, scenes, datasets, trial counts, speeds, durations. Separate simulation, recorded data, and closed-loop hardware.>

## Evidence type and transfer

<Which results come from which evidence setting, and what that setting can and cannot show.>

## Sensors

<Sensors used by the method, and sensors used only for ground truth.>

## Compute and latency

<Processor, where it runs, timing numbers with their scope (per frame, per module, end to end), and what is not reported.>

## Key quantitative results

<!--
Every bullet carries a physical PDF page and, when applicable, a table or
figure number. In "A versus B" bullets, values follow the order of the label
(method first, comparator second). Say when a comparator appears only in
plots without numbers. Read tables and figures from a rendered page image
(python -m tools.locate <ID> --render N) when the PDF has no text layer or the
transcription has empty, merged, or shifted cells.
-->

- <Metric: method value versus comparator value, condition> (p. <6>, Table <III>).

## Stated limitations

<!-- Only statements made by the authors, each with a page. Reviewer observations go to Transfer conditions. If the authors state no limitation, write "The authors state no limitation." -->

- <Limitation stated by the authors> (p. <8>).

## Transfer conditions

<Conditions that a reader must check before reusing the result on another wheeled robot: sensors, calibration, kinematics, compute, environment.>

## Code and data

<Code and data availability as stated in the paper, with URLs. Say "not verified" for anything that was not checked.>

## Version family

<Related conference, journal, or preprint versions and how this library counts them.>

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | <direct-support> | <strong> | <Sec. IV-A, p. 6> | "<verbatim excerpt from the full text>" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | <qualifies> | <moderate> | <Sec. IV, p. 5> | "<verbatim excerpt>" |

## Page-cited excerpts

<!-- Verbatim, contiguous text from the paper (no ellipses). One line per excerpt, then one line of interpretation. -->

- **p. <8>, <Section name>.** "<verbatim excerpt>"
  <What the excerpt shows and what it does not show.>

## Survey-usable statements

### Supported

- <A statement the survey may make, with its condition.>

### Not supported

<!-- When the tempting statement is "best on every sequence", list every counterexample or give the count ("beaten on 5 of 13 sequences"). -->

- <A tempting statement that the full text does not support, and why.>

## Verification log

- <2026-10-26> | host: Kiro | scope: <full text read; Tables I-III and Fig. 7 checked against the PDF> | corrections: <none, or a short list; details in 06-data/review-corrections.csv>
- Legacy extraction: <automated reviewer (codex), batch name; or "none; new targeted follow-up reading">. Legacy evidence files: <99-archive/history-2026-10-25.zip::path>, if any.

## Original abstract

<The authors' abstract, copied verbatim from the paper.>
