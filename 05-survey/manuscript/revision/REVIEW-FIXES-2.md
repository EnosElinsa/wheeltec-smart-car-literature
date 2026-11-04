# Review fixes, round 2: foundational references and selection detail - November 4, 2026

This revision follows [REVIEW-FIXES-1.md](REVIEW-FIXES-1.md). It applies two author decisions that respond to the simulated review. The selected corpus is unchanged at 229 works from 2021-2026.

## Foundational references (author decision)

Both reviewers asked for the original sources of the definitions and equations in Section II. The author decided on 2026-11-04 to cite foundational pre-2021 sources as background references for attribution, outside the coded corpus and its counts. This replaces the 2026-11-03 rule that admitted no pre-2021 citation. `data/citation-scope.json` records the decision (`foundational_policy_2026_11_04`) and gives a reason for each exception. `citation_scope.py` still requires every pre-2021 background reference to be listed there.

| Key | Source | Attributes |
|---|---|---|
| `B_Campion1996` | Campion et al., kinematic and dynamic models of wheeled robots, IEEE T-RA 1996 | Wheeled kinematic classes, Eqs. (1)-(3) |
| `B_DWA1997` | Fox et al., the dynamic window approach, IEEE RAM 1997 | DWA in Sections I-II |
| `B_TEB2013` | Rösmann et al., timed-elastic-band trajectory optimization, ECMR 2013 | TEB in Sections I-II |
| `B_CBF2017` | Ames et al., control barrier function quadratic programs, IEEE TAC 2017 | CBF condition, Eq. (5) |
| `B_Cadena2016` | Cadena et al., past, present, and future of SLAM, IEEE T-RO 2016 | Estimation posterior, Eq. (4) |
| `B_Nav22020` | Macenski et al., The Marathon 2: a navigation system, IROS 2020 | Nav2 stack, Section II-B |
| `B_GNSSIntegrity2018` | Zhu et al., GNSS position integrity in urban environments, IEEE T-ITS 2018 | Integrity risk, alert limit and protection level, Eq. (6) |

The Nav2 maintainers' survey (Macenski et al., Robotics and Autonomous Systems 168, 2023, `B_Nav2Survey2023`) was added beside the Nav2 system paper. It falls within the 2021-2026 window. The two new records (`B_GNSSIntegrity2018`, `B_Nav2Survey2023`) were verified from opened Crossref DOI records, with the cited-reference lists omitted. The other six were already in `background-sources/` and had been excluded on 2026-11-03.

The supplement no longer says that foundational sources are kept in an "internal library" and not cited. It now lists the background references by role. The bibliography grows from 238 to 246 references: 229 corpus works and 17 background references, seven of them from before 2021.

## Selection detail in Section III (author decision)

The selection-stage table moved from the supplement into Section III (now Table III; the later main-text tables are renumbered IV-VI). Section III now states:

- the journal search (17 journals, 102 journal-year combinations, 58,583 merged records, 43,086 with complete metadata);
- the language-model-assisted screening under preset topic allocations, which stopped after 45 acceptances and left 43,041 records unassessed, and the unavailability of its order and rejection history;
- the six purposive stages, including the stage acquired for the four integration questions and the IEEE-only stages;
- that every included work was read and coded (23 by full reading, the others by targeted or extract-based reading);
- the November 3, 2026 cut-off;
- that stage quotas and publisher restrictions shape the counts of Section IX.

A preprint and its published version count once. Section III states the role of the foundational background references. The supplement keeps the detailed narrative and points to the table in the main paper.

The model, version and prompts of the language-model screening are not recorded in the repository. They are not stated in the manuscript and remain for the authors to supply.

## Length

Twelve sentences that repeated Table V, Section II, Section IX or a neighbouring sentence were removed to keep the paper at 24 pages. Every corpus citation remains in prose. The last page balances at 739 and 712 pt without a forced break.

## Verification

`verify_delivery.py` now expects 28 main labels (with `tab:selection`) and 12 supplement labels. Both modes pass:

- 24 pages, 229 corpus citations in prose and 246 resolved references, with 7 foundational exceptions;
- 28 labels, three figures, six tables and six unchanged equations;
- an 8-page supplement with six tables;
- 693 local artifacts checked with no hash mismatch.

[numeric-audit.json](numeric-audit.json) covers the same 23 numerical sentences with no mismatch. Sentence rhythm: 526 sentences, mean 21.7 words, 12% under 12 words, 8% over 35 words, with no style flags and a clean house-style scan.
