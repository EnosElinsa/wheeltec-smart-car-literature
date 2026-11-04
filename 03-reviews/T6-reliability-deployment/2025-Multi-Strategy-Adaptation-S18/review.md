# Multi-Strategy Deployment-Time Learning and Adaptation for Navigation under Uncertainty

## Metadata

| Field | Value |
|---|---|
| ID | S18 |
| Title | Multi-Strategy Deployment-Time Learning and Adaptation for Navigation under Uncertainty |
| Authors | Paudel, Abhishek and Xiao, Xuesu and Stein, Gregory J. |
| Venue | Conference on Robot Learning |
| Year | 2025 |
| Type | conference |
| DOI | none (see official URL) |
| Official URL | https://proceedings.mlr.press/v270/paudel25a.html |
| Theme folder | T6-reliability-deployment |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T6-reliability-deployment/2025-Multi-Strategy-Adaptation-S18/paper.pdf` and `02-fulltext/T6-reliability-deployment/2025-Multi-Strategy-Adaptation-S18/paper.md` (local only); [citation.bib](../../../01-papers/T6-reliability-deployment/2025-Multi-Strategy-Adaptation-S18/citation.bib) |

## Survey coding

- survey_module: fault-recovery-deployment
- secondary_modules: traversability-planning-control
- evidence_type: simulation
- evidence_all: simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Simulated visual mazes and point-goal trials; physical drivetrain not specified (p. 7).
- boundary_platform: no
- degradation: visual-degradation, model-error
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, designed-degradation
- sensors: Simulated visual observations and partially revealed maps/subgoals
- compute: Intel i9/RTX A6000; learning/domain adaptation and replay can occur between trials; no live robot timing bound (p. 16).
- compute_location: desktop-offline
- summary_result: Replay-aware selection changes which adaptation strategy is used as policies improve.
- summary_limitation: Requires policies amenable to counterfactual reasoning; multiple learners and replay of old trials impose compute growth (pp. 8, 16).
- survey_included: yes
- verification_level: light

## Problem

Past policy performance becomes stale when several deployment-time learners evolve.

## Mechanism

Counterfactual replay bounds updated policy cost on older trials to select among nonstationary navigation/adaptation strategies (pp. 5-6).

## Baselines and controls

UCBandit and RollingReplay; nonlearned, pretrained, CycleGAN and from-scratch policies (p. 7).

## Platform and setup

Simulated visual mazes and point-goal trials; physical drivetrain not specified (p. 7).

## Evidence type and transfer

Strongest coded setting: `simulation`. Selection cost, training cost and between-trial idle time must be reported separately; simulation does not establish physical recovery.

## Sensors

Simulated visual observations and partially revealed maps/subgoals.

## Compute and latency

Intel i9/RTX A6000; learning/domain adaptation and replay can occur between trials; no live robot timing bound (p. 16).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

Requires policies amenable to counterfactual reasoning; multiple learners and replay of old trials impose compute growth (pp. 8, 16).

## Transfer conditions

Selection cost, training cost and between-trial idle time must be reported separately; simulation does not establish physical recovery.

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

- **p. 8, Selected source passage.** "may not be directly applicable for selection between model-free navigation methods"
  Adds adaptation-strategy selection to runtime supervision while exposing a representational prerequisite.

## Survey-usable statements

### Supported

- Replay-aware selection changes which adaptation strategy is used as policies improve. Adds adaptation-strategy selection to runtime supervision while exposing a representational prerequisite.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. Selection cost, training cost and between-trial idle time must be reported separately; simulation does not establish physical recovery.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 5, 6, 7, 8, 16; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

We present an approach for performant point-goal navigation in unfamiliar partially-mapped environments. When deployed, our robot runs multiple strategies for deployment-time learning and visual domain adaptation in parallel and quickly selects the best-performing among them. Choosing between policies as they are learned or adapted between navigation trials requires continually updating estimates of their performance as they evolve. Leveraging recent work in model-based learning-informed planning under uncertainty, we determine lower bounds on the would-be performance of newly-updated policies on old trials without needing to re-deploy them. This information constrains and accelerates bandit-like policy selection, affording quick selection of the best-performing strategy shortly after it would start to yield good performance. We validate the effectiveness of our approach in simulated maze-like environments, showing improved navigation cost and cumulative regret versus existing baselines.
