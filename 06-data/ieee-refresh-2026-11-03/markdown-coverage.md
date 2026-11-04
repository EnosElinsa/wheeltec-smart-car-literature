# OXR Markdown coverage

All 36 new sources were transcribed using SoMarkAI/OXR-1.0 through self-hosted vLLM 0.25.1 and OXR D-FINE layout analysis. The archive contains 36 Markdown files, 482 per-page JSON files and 907 image assets referenced by Markdown or page JSON. The full library has 231 source transcriptions. The 195 earlier transcriptions retain their original bytes.

Every PDF page has one physical-page marker; all output hashes and referenced image paths resolve. Mechanical checks screened short output, low PDF-text word coverage and truncation warnings. No flagged page remains after the recorded checks. This establishes artifact coverage, not exact recognition of every equation, table or reading order. Use the original PDF for numerical claims and formulas.

The pipeline retained 5 warnings: `{"Recognition": 1, "reading_order_invalid": 1, "reading_order_repaired": 2, "reading_order_supplemented": 1}`. The warning log and page JSON preserve them. Reading-order repairs produce a complete unique block order before assembly; configured header/footer removal still applies. The [quality notes](quality-notes.md) record page checks and any recovery. The [extraction ledger](markdown-extraction.json) holds hashes, page counts and image counts.

Both task-owned OXR/vLLM and layout services were stopped after the batch. Port checks confirmed 8080 and 8081 were free. Process identities were recorded before shutdown so unrelated server workloads were preserved.

| ID | PDF pages | Archived images | Warnings | Local Markdown |
|---|---:|---:|---:|---|
| R01 | 8 | 17 | 0 | `02-fulltext/T1-perception-localization/2026-Radar-Uncertainty-R01/paper.md` |
| R02 | 14 | 50 | 0 | `02-fulltext/T1-perception-localization/2026-RaLI-Multi-R02/paper.md` |
| R03 | 12 | 39 | 0 | `02-fulltext/T1-perception-localization/2025-Ground-Constrained-SLAM-R03/paper.md` |
| R04 | 16 | 18 | 0 | `02-fulltext/T1-perception-localization/2025-WING-R04/paper.md` |
| R05 | 20 | 44 | 2 | `02-fulltext/T1-perception-localization/2025-AirSLAM-R05/paper.md` |
| R06 | 19 | 17 | 0 | `02-fulltext/T1-perception-localization/2025-CMRNext-R06/paper.md` |
| R07 | 8 | 21 | 0 | `02-fulltext/T2-slam-mapping-exploration/2026-Chamelion-R07/paper.md` |
| R08 | 8 | 13 | 0 | `02-fulltext/T2-slam-mapping-exploration/2026-E2-BKI-R08/paper.md` |
| R09 | 8 | 7 | 0 | `02-fulltext/T2-slam-mapping-exploration/2026-Radar-Long-Term-R09/paper.md` |
| R10 | 8 | 9 | 0 | `02-fulltext/T2-slam-mapping-exploration/2026-OMCL-R10/paper.md` |
| R11 | 21 | 43 | 1 | `02-fulltext/T2-slam-mapping-exploration/2026-LiDAR-Teach-Radar-Repeat-R11/paper.md` |
| R12 | 21 | 33 | 0 | `02-fulltext/T2-slam-mapping-exploration/2026-Super4DR-R12/paper.md` |
| R13 | 8 | 7 | 0 | `02-fulltext/T3-planning-control/2026-Terrain-Adaptive-MPC-R13/paper.md` |
| R14 | 8 | 9 | 0 | `02-fulltext/T3-planning-control/2026-MonoMPC-R14/paper.md` |
| R15 | 8 | 6 | 0 | `02-fulltext/T3-planning-control/2026-TRAIL-R15/paper.md` |
| R16 | 20 | 55 | 0 | `02-fulltext/T3-planning-control/2026-HEIGHT-R16/paper.md` |
| R17 | 12 | 30 | 1 | `02-fulltext/T3-planning-control/2025-Compensation-MPC-R17/paper.md` |
| R18 | 20 | 53 | 0 | `02-fulltext/T3-planning-control/2025-SCOPE-R18/paper.md` |
| R19 | 8 | 11 | 0 | `02-fulltext/T4-multi-robot-coordination/2026-CoCoPlan-R19/paper.md` |
| R20 | 8 | 8 | 0 | `02-fulltext/T4-multi-robot-coordination/2026-Multi-Proxy-R20/paper.md` |
| R21 | 8 | 16 | 0 | `02-fulltext/T4-multi-robot-coordination/2026-Hierarchical-Transmission-R21/paper.md` |
| R22 | 20 | 46 | 0 | `02-fulltext/T4-multi-robot-coordination/2026-URGE-R22/paper.md` |
| R23 | 20 | 24 | 0 | `02-fulltext/T4-multi-robot-coordination/2026-riMESA-R23/paper.md` |
| R24 | 17 | 39 | 1 | `02-fulltext/T4-multi-robot-coordination/2025-MEF-Explore-R24/paper.md` |
| R25 | 8 | 5 | 0 | `02-fulltext/T5-semantic-embodied-navigation/2026-Sem-NaVAE-R25/paper.md` |
| R26 | 8 | 21 | 0 | `02-fulltext/T5-semantic-embodied-navigation/2026-VAMOS-R26/paper.md` |
| R27 | 8 | 10 | 0 | `02-fulltext/T5-semantic-embodied-navigation/2026-osmAG-LLM-R27/paper.md` |
| R28 | 16 | 33 | 0 | `02-fulltext/T5-semantic-embodied-navigation/2026-VLN-Game-R28/paper.md` |
| R29 | 8 | 6 | 0 | `02-fulltext/T5-semantic-embodied-navigation/2025-OLiVia-Nav-R29/paper.md` |
| R30 | 8 | 8 | 0 | `02-fulltext/T5-semantic-embodied-navigation/2026-NORM-Nav-R30/paper.md` |
| R31 | 21 | 51 | 0 | `02-fulltext/T6-reliability-deployment/2026-Cloud-Edge-System-R31/paper.md` |
| R32 | 17 | 30 | 0 | `02-fulltext/T6-reliability-deployment/2025-Mechanical-Compute-Energy-R32/paper.md` |
| R33 | 17 | 62 | 0 | `02-fulltext/T6-reliability-deployment/2025-Help-Me-Through-R33/paper.md` |
| R34 | 17 | 26 | 0 | `02-fulltext/T6-reliability-deployment/2025-Recharge-Monitoring-R34/paper.md` |
| R35 | 17 | 24 | 0 | `02-fulltext/T6-reliability-deployment/2025-R-FAC-R35/paper.md` |
| R36 | 17 | 16 | 0 | `02-fulltext/T6-reliability-deployment/2025-RADIUM-R36/paper.md` |
