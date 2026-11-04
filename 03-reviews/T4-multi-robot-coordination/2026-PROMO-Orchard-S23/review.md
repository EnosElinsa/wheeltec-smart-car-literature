# PROMO‐Orchard: A Robust Semantic‐Enhanced Framework for Dual‐Robot Simultaneous Localization and Mapping Merging in Orchard

## Metadata

| Field | Value |
|---|---|
| ID | S23 |
| Title | PROMO‐Orchard: A Robust Semantic‐Enhanced Framework for Dual‐Robot Simultaneous Localization and Mapping Merging in Orchard |
| Authors | Sun, Yefeng and Dai, Jialing and Gong, Liang and Gao, Bishu and Cai, Jinghan and Li, Yanming and Liu, Chengliang |
| Venue | Journal of Field Robotics |
| Year | 2026 |
| Type | journal |
| DOI | [10.1002/rob.70323](https://doi.org/10.1002/rob.70323) |
| Official URL | https://onlinelibrary.wiley.com/doi/10.1002/rob.70323 |
| Theme folder | T4-multi-robot-coordination |
| Batch | survey-200plus-2026-11-03 |
| Local files | `01-papers/T4-multi-robot-coordination/2026-PROMO-Orchard-S23/paper.pdf` and `02-fulltext/T4-multi-robot-coordination/2026-PROMO-Orchard-S23/paper.md` (local only); [citation.bib](../../../01-papers/T4-multi-robot-coordination/2026-PROMO-Orchard-S23/citation.bib) |

## Survey coding

- survey_module: multi-robot
- secondary_modules: localization-mapping
- evidence_type: online-hardware
- evidence_all: online-hardware
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Two agricultural ground robots at one orchard; delayed overlap during simultaneous operation, not seasonal revisits (pp. 10-12).
- boundary_platform: no
- degradation: lidar-degeneracy, data-association-fault
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Ouster OSI-128, Yesense IMU and BeiDou; semantic trunk/row priors
- compute: Onboard Intel i5-1240P/16 GB local mapping; compact summaries precede gated submap exchange (pp. 10-11).
- compute_location: onboard
- summary_result: Orchard-specific structural and semantic gates improve within-study map-merging consistency.
- summary_limitation: One site and two robots; final-map evaluation leaves trigger precision, module latency, CPU and bandwidth unquantified (p. 20).
- survey_included: yes
- verification_level: light

## Problem

Repeated orchard rows can produce geometrically plausible but incorrect inter-robot map alignment.

## Mechanism

Operation-aware submaps, semantic retrieval, orchard-prior initialization, reliability-weighted GICP and posterior merge validation (pp. 4, 20).

## Baselines and controls

Implemented Segregator and internal semantic ablation; no independent fixed-interval scheduling comparison (pp. 12, 20).

## Platform and setup

Two agricultural ground robots at one orchard; delayed overlap during simultaneous operation, not seasonal revisits (pp. 10-12).

## Evidence type and transfer

Strongest coded setting: `online-hardware`. The reference traversal uses the same mapping backbone and is not independent geodetic truth. Online mapping does not demonstrate closed-loop navigation.

## Sensors

Ouster OSI-128, Yesense IMU and BeiDou; semantic trunk/row priors.

## Compute and latency

Onboard Intel i5-1240P/16 GB local mapping; compact summaries precede gated submap exchange (pp. 10-11).

## Key quantitative results

No performance-table numbers are retained in this targeted reading. The qualitative mechanism and evidence conditions above are the basis of survey integration.

## Stated limitations

One site and two robots; final-map evaluation leaves trigger precision, module latency, CPU and bandwidth unquantified (p. 20).

## Transfer conditions

The reference traversal uses the same mapping backbone and is not independent geodetic truth. Online mapping does not demonstrate closed-loop navigation.

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

- **p. 12, Selected source passage.** "rather than an error-free geodetic ground truth"
  Distinguishes orchard prior validity and overlap acceptance from optimizer accuracy or generic team scalability.

## Survey-usable statements

### Supported

- Orchard-specific structural and semantic gates improve within-study map-merging consistency. Distinguishes orchard prior validity and overlap acceptance from optimizer accuracy or generic team scalability.

### Not supported

- Unconditional transfer to another robot, an independent safety guarantee, or whole-paper verification is not established by this targeted reading. The reference traversal uses the same mapping backbone and is not independent geodetic truth. Online mapping does not demonstrate closed-loop navigation.

## Verification log

- 2026-11-03 | host: Codex | scope: targeted source reading of identity/abstract and selected mechanism, setup, evaluation, discussion or limitation passages on physical PDF pp. 1, 4, 10, 11, 12, 14, 20; excerpts checked against Markdown and PDF text; no performance-table numbers retained; not a whole-paper audit | corrections: evidence setting, computation role, reference assumptions and transfer limits recorded explicitly
- Legacy extraction: none; new targeted follow-up reading. The source-reading ledger records the passages used; human final review remains pending.

## Original abstract

Agricultural robots are increasingly used to improve orchard productivity and reduce labor dependence, yet collaborative orchard mapping remains difficult because dense canopy degrades GNSS reliability, repetitive row geometry induces structural aliasing, and long-duration operation over large orchard blocks causes mergeable overlap to emerge only after extended traversal, thereby destabilizing generic registration pipelines. In this work, we formulate orchard map merging as an operation-time progressive submap association and registration problem for a dual-robot field setting and propose PROMO-Orchard, an orchard-aware semantic map-merging framework. The framework integrates four tightly coupled components: class-dependent voxelization with persistent orchard-prior extraction, Orchard-AKS for operation-aware submap scheduling, Sem-OREOS for semantic-enhanced overlap retrieval and merge triggering, and Sem-GICP for class-weighted semantic refinement with orchard structural regularization. Together, these components turn semantic map merging into an operation-time, orchard-aware process rather than a generic post-hoc registration step. Field experiments in three representative orchard settings, namely I-Tunnel, U-Tunnel, and Long-Duration, show that the proposed method consistently suppresses row aliasing and maintains semantically coherent shared maps under in-row overlap, headland U-turning, and delayed-overlap operation. Compared with Segregator and a semantic-ablation variant, the proposed framework reduces ICP error by 78–94% while maintaining FPMR above 91% across all scenarios, and achieves clear improvements in semantic fidelity, boundary continuity, and structural consistency. These results support the conclusion that reliable orchard map merging requires not only semantic cues, but their structured integration with orchard-specific priors, thereby providing a practical basis for collaborative orchard mapping and downstream robotic operations such as navigation, canopy management, harvesting, and logistics. While the present study experimentally validates the dual-robot case, the proposed progressive pairwise merging formulation provides the system-level basis for future extension to larger multi-robot orchard teams.
