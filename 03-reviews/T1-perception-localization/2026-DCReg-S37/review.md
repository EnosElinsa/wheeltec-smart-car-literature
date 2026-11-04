# DCReg: Decoupled characterization for efficient degenerate LiDAR registration

## Metadata

| Field | Value |
|---|---|
| ID | S37 |
| Title | DCReg: Decoupled characterization for efficient degenerate LiDAR registration |
| Authors | Xiangcheng Hu and Xieyuanli Chen and Mingkai Jia and Jin Wu and Ping Tan and Steven L. Waslander |
| Venue | The International Journal of Robotics Research |
| Year | 2026 |
| Type | journal |
| DOI | [10.1177/02783649261465040](https://doi.org/10.1177/02783649261465040) |
| Official URL | https://journals.sagepub.com/doi/10.1177/02783649261465040 |
| Theme folder | T1-perception-localization |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T1-perception-localization/2026-DCReg-S37/paper.pdf` and `02-fulltext/T1-perception-localization/2026-DCReg-S37/paper.md` (local only); [citation.bib](../../../01-papers/T1-perception-localization/2026-DCReg-S37/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback, numerical
- protocol_caveats: none
- platform_class: mixed
- platform: Self-collected Pandar XT-32/RTK-INS sequences, public multi-carrier benchmarks and controlled synthetic registration; own carrier not established in the selected passages (p. 15).
- boundary_platform: yes
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: LiDAR point clouds; RTK/INS used as reference in own sequences
- compute: Preconditioned conjugate-gradient registration is evaluated; exact benchmark processor was not retained.
- compute_location: desktop-offline
- summary_result: Directional preconditioning stabilizes ill-conditioned registration without adding an independent measurement source.
- summary_limitation: Completely missing geometric information and initialization outside the convergence basin remain fundamental limitations (p. 27).
- survey_included: yes
- verification_level: light

## Problem

Full-Hessian analysis can mix translational and rotational conditioning, obscuring weak physical motion directions.

## Mechanism

Uses Schur-complement subspace separation, aligns eigen-directions, and applies targeted spectral shaping in a preconditioner while preserving the original least-squares objective (pp. 1, 7, 12-14).

## Baselines and controls

Controlled cylinder perturbations and public/own degenerate sequences, including deliberately range-limited scans and mitigation ablations (pp. 15, 26).

## Platform and setup

Self-collected Pandar XT-32/RTK-INS sequences, public multi-carrier benchmarks and controlled synthetic registration; own carrier not established in the selected passages (p. 15).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Distinguish improved numerical conditioning from restored observability; check whether nonzero information and reasonable initialization remain.

## Sensors

LiDAR point clouds; RTK/INS used as reference in own sequences.

## Compute and latency

Preconditioned conjugate-gradient registration is evaluated; exact benchmark processor was not retained.

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Completely missing geometric information and initialization outside the convergence basin remain fundamental limitations (p. 27).

## Transfer conditions

Distinguish improved numerical conditioning from restored observability; check whether nonzero information and reasonable initialization remain.

## Code and data

Availability statements and external repositories were not independently checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity. No separate preprint or conference version is added to the corpus.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | unset | n/a | | |

## Page-cited excerpts

- **p. 27, Selected source passage.** "the values remain non-zero given reasonable initial poses."
  Sharpens the survey distinction among stabilization, selective observations and genuinely complementary constraints.

## Survey-usable statements

### Supported

- Directional preconditioning stabilizes ill-conditioned registration without adding an independent measurement source. Sharpens the survey distinction among stabilization, selective observations and genuinely complementary constraints.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Distinguish improved numerical conditioning from restored observability; check whether nonzero information and reasonable initialization remain.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 7, 12, 14, 15, 26, 27; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

LiDAR point cloud registration is fundamental to robotic perception and navigation. However, in geometrically degenerate or narrow environments (e.g., corridors), registration problems become ill-conditioned: certain motion directions are weakly constrained, leading to unstable solutions and degraded accuracy. Existing methods adopt a detect-then-mitigate paradigm but fail to reliably detect, physically interpret, and stabilize such ill-conditioning without corrupting the optimization problem. In this study, we introduce DCReg (Decoupled Characterization for Ill-conditioned Registration), which establishes a principled detect–characterize–mitigate paradigm that systematically addresses ill-conditioned registration through three integrated innovations. First, DCReg achieves reliable ill-conditioning detection by employing a Schur complement decomposition to the hessian matrix. This structure-aware technique decouples the 6-DoF registration problem into 3-DoF clean rotational and translational subspaces, eliminating coupling effects that mask degeneracy patterns in conventional full-Hessian analyses. Second, within these decoupled subspaces, we develop physically interpretable characterization techniques that resolve eigenbasis ambiguities through principled basis alignment. This establishes stable and quantitative mappings between mathematical eigenspaces and physical motion directions, providing actionable insights about which specific motions lack constraints and to what extent. Third, leveraging this directional spectral information, we design a targeted mitigation strategy via a structured preconditioner. While guided by MAP regularization principles for spectral shaping, our approach implements eigenvalue clamping exclusively within the preconditioner rather than modifying the origin problem. This preserves the original least-squares objective and its minimizer while enabling efficient and stable optimization via Pre-conditioned Conjugate Gradient with a single physically interpretable parameter. Extensive experiments demonstrate DCReg achieves at least 20%–50% improvement in long-duration localization accuracy and typical speedups of $5-30\times$ (up to $116\times$ in certain scenarios) over comparable degeneracy-aware baseline methods across diverse environments. Our implementation will be available at https://github.com/JokerJohn/DCReg.
