# Markdown extraction coverage

> **Stage record, November 3, 2026.** Its counts and statuses describe that date and are not updated. Current totals are in the [repository README](../../README.md).

**195 of 195 registered papers now have archived Markdown**, with file hashes verified. This includes all 147 baseline papers and all 48 additions.

The 48 additions were re-extracted using **SoMark OXR-1.0 through self-hosted vLLM 0.25.1**, with its D-FINE layout model. Their **802 physical PDF pages** are represented by sequential `<!-- PDF page: N -->` markers. OXR Markdown, per-page structured JSON and 996 referenced figure/image assets are retained under the matching `02-fulltext/<theme>/<folder>/` directories. Referenced files resolve locally. The earlier PyMuPDF4LLM exports remain private comparison backups; they are not the active transcriptions.

MinerU precision was attempted on S03 twice, but upload connections timed out before parsing. The user then requested this OXR service. Outputs are labeled OXR; no MinerU results are claimed. The original 147 MD files retain their existing extraction modes and bytes: the first 127 include 62 precision, 52 original-export and 13 precision-direct-official-api records; the supplementary 20 use local PyMuPDF4LLM.

Extraction and whole-paper review are separate. All additions now have targeted method/setup/evaluation/limitation readings and light evidence cards, recorded in the [reading ledger](source-reading.json). This is not a whole-paper or complete numerical audit. Formulas, table cells and numerical claims must be checked against the PDF before citation. Automatic reading-order repairs and targeted page retries are recorded in provenance. See the [extraction manifest](markdown-extraction.json), [coverage CSV](markdown-coverage.csv), and [next survey steps](survey-integration-next-steps.md).

The mechanical screen covered all 802 pages and flagged five figure/table pages (S19 pp. 14/16, S22 p. 16, S23 p. 17, S24 p. 12). Their figures/captions or tables were retained; excluded publisher headers, license and footer text explain the low lexical overlap. Three pages were reprocessed at higher resolution (S07 p. 16, S20 p. 11, S31 p. 10). Six successful reading-order repairs and one automatic recognition retry remain recorded as diagnostics. No unresolved output truncation remains. These checks do not verify scientific equations or numerical claims.

| ID | Pages | Mode | Markdown path | Images |
|---|---:|---|---|---:|
| S01 | 12 | OXR-1.0 / vLLM | `02-fulltext/T2-slam-mapping-exploration/2026-NVMS-SLAM-S01/paper.md` | 17 |
| S02 | 8 | OXR-1.0 / vLLM | `02-fulltext/T2-slam-mapping-exploration/2026-Active-Visual-MPC-S02/paper.md` | 28 |
| S03 | 8 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2024-AGLoc-S03/paper.md` | 10 |
| S04 | 10 | OXR-1.0 / vLLM | `02-fulltext/T4-multi-robot-coordination/2026-Set-Theoretic-Platoon-S04/paper.md` | 14 |
| S05 | 11 | OXR-1.0 / vLLM | `02-fulltext/T3-planning-control/2026-Risk-Zone-CBF-S05/paper.md` | 12 |
| S06 | 8 | OXR-1.0 / vLLM | `02-fulltext/T4-multi-robot-coordination/2026-Fixed-Time-Deadlock-S06/paper.md` | 11 |
| S07 | 20 | OXR-1.0 / vLLM | `02-fulltext/T3-planning-control/2026-Curvature-Vector-Field-S07/paper.md` | 55 |
| S08 | 11 | OXR-1.0 / vLLM | `02-fulltext/T3-planning-control/2025-Low-Complexity-Tracking-S08/paper.md` | 33 |
| S09 | 17 | OXR-1.0 / vLLM | `02-fulltext/T3-planning-control/2025-Topology-Trajectory-S09/paper.md` | 33 |
| S10 | 8 | OXR-1.0 / vLLM | `02-fulltext/T4-multi-robot-coordination/2024-Swarm-SLAM-S10/paper.md` | 21 |
| S11 | 8 | OXR-1.0 / vLLM | `02-fulltext/T4-multi-robot-coordination/2025-Foundation-Loop-Closing-S11/paper.md` | 9 |
| S12 | 26 | OXR-1.0 / vLLM | `02-fulltext/T5-semantic-embodied-navigation/2025-Multimodal-Language-Maps-S12/paper.md` | 15 |
| S13 | 8 | OXR-1.0 / vLLM | `02-fulltext/T5-semantic-embodied-navigation/2025-Temporal-Scene-Graph-S13/paper.md` | 16 |
| S14 | 20 | OXR-1.0 / vLLM | `02-fulltext/T6-reliability-deployment/2025-SELFI-S14/paper.md` | 13 |
| S15 | 9 | OXR-1.0 / vLLM | `02-fulltext/T6-reliability-deployment/2026-Fixed-Time-FTC-S15/paper.md` | 10 |
| S16 | 16 | OXR-1.0 / vLLM | `02-fulltext/T6-reliability-deployment/2025-Resilient-TEB-S16/paper.md` | 10 |
| S17 | 21 | OXR-1.0 / vLLM | `02-fulltext/T6-reliability-deployment/2022-Resilient-Energy-Tasks-S17/paper.md` | 35 |
| S18 | 16 | OXR-1.0 / vLLM | `02-fulltext/T6-reliability-deployment/2025-Multi-Strategy-Adaptation-S18/paper.md` | 14 |
| S19 | 22 | OXR-1.0 / vLLM | `02-fulltext/T6-reliability-deployment/2025-SLAM-Loop-Costs-S19/paper.md` | 13 |
| S20 | 24 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2025-Low-Light-SLAM-S20/paper.md` | 47 |
| S21 | 24 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2026-HK-MEMS-S21/paper.md` | 23 |
| S22 | 22 | OXR-1.0 / vLLM | `02-fulltext/T2-slam-mapping-exploration/2026-Season-Robust-Orchard-S22/paper.md` | 26 |
| S23 | 24 | OXR-1.0 / vLLM | `02-fulltext/T4-multi-robot-coordination/2026-PROMO-Orchard-S23/paper.md` | 16 |
| S24 | 16 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2026-DR-ICP-S24/paper.md` | 54 |
| S25 | 24 | OXR-1.0 / vLLM | `02-fulltext/T4-multi-robot-coordination/2026-Planned-Synchronization-S25/paper.md` | 46 |
| S26 | 21 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2026-Map-Representation-Loc-S26/paper.md` | 22 |
| S27 | 15 | OXR-1.0 / vLLM | `02-fulltext/T4-multi-robot-coordination/2026-Range-Only-SLAM-S27/paper.md` | 26 |
| S28 | 13 | OXR-1.0 / vLLM | `02-fulltext/T4-multi-robot-coordination/2026-Mobile-UWB-Anchors-S28/paper.md` | 23 |
| S29 | 12 | OXR-1.0 / vLLM | `02-fulltext/T4-multi-robot-coordination/2026-Bandwidth-SLAM-S29/paper.md` | 15 |
| S30 | 14 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2026-Implicit-Voxel-SLAM-S30/paper.md` | 24 |
| S31 | 12 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2025-Degeneracy-Compensation-S31/paper.md` | 48 |
| S32 | 14 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2026-IMU-Odometer-Calibration-S32/paper.md` | 20 |
| S33 | 17 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2026-GEODE-S33/paper.md` | 16 |
| S34 | 31 | OXR-1.0 / vLLM | `02-fulltext/T2-slam-mapping-exploration/2026-NeuSE-S34/paper.md` | 33 |
| S35 | 31 | OXR-1.0 / vLLM | `02-fulltext/T2-slam-mapping-exploration/2026-Density-Map-Loops-S35/paper.md` | 21 |
| S36 | 28 | OXR-1.0 / vLLM | `02-fulltext/T2-slam-mapping-exploration/2026-BIM-Loc-S36/paper.md` | 21 |
| S37 | 32 | OXR-1.0 / vLLM | `02-fulltext/T1-perception-localization/2026-DCReg-S37/paper.md` | 19 |
| S38 | 7 | OXR-1.0 / vLLM | `02-fulltext/T6-reliability-deployment/2024-SCALE-S38/paper.md` | 12 |
| S39 | 8 | OXR-1.0 / vLLM | `02-fulltext/T5-semantic-embodied-navigation/2025-HAM-Nav-S39/paper.md` | 19 |
| S40 | 8 | OXR-1.0 / vLLM | `02-fulltext/T5-semantic-embodied-navigation/2025-VLM-GroNav-S40/paper.md` | 3 |
| S41 | 13 | OXR-1.0 / vLLM | `02-fulltext/T6-reliability-deployment/2025-LiReN-S41/paper.md` | 8 |
| S42 | 12 | OXR-1.0 / vLLM | `02-fulltext/T3-planning-control/2025-Velociraptor-S42/paper.md` | 8 |
| S43 | 22 | OXR-1.0 / vLLM | `02-fulltext/T5-semantic-embodied-navigation/2025-Mobility-VLA-S43/paper.md` | 18 |
| S44 | 24 | OXR-1.0 / vLLM | `02-fulltext/T5-semantic-embodied-navigation/2025-SocialNav-SUB-S44/paper.md` | 10 |
| S45 | 18 | OXR-1.0 / vLLM | `02-fulltext/T3-planning-control/2025-SPARTA-S45/paper.md` | 19 |
| S46 | 21 | OXR-1.0 / vLLM | `02-fulltext/T2-slam-mapping-exploration/2025-NP-Elevation-S46/paper.md` | 10 |
| S47 | 16 | OXR-1.0 / vLLM | `02-fulltext/T6-reliability-deployment/2025-CARE-S47/paper.md` | 13 |
| S48 | 20 | OXR-1.0 / vLLM | `02-fulltext/T3-planning-control/2025-Conformal-Crowd-S48/paper.md` | 7 |
