# Review additions: registered and assessed sources

**16 verified official PDF/BibTeX pairs, 16 local PyMuPDF4LLM Markdown files and 16 targeted light review cards.** All 16 are survey selection members. The library now has 247 acquired and assessed publications, and the survey selection has 245 works.

An internal simulated two-reviewer review of an earlier draft named these works as missing from the corpus. The user confirmed the selection of 16 formally published works from 2021–2024. They were not found by a systematic search, and this stage did not apply the earlier screening. By bibliographic year there are three works from 2021, six from 2022, three from 2023 and four from 2024. Six are journal articles and ten are conference papers. Their survey modules are localization and mapping (1), traversability, planning and control (4), multi-robot systems (5), and semantic and language navigation (6).

## Acquisition

Thirteen pairs came from automated publisher retrieval. The user downloaded the STEP (K03), CERBERUS (K10) and HM3D (K11) pairs by hand. The automated identity check rejected these three pairs, so their identities were matched by hand, as recorded in their provenance files. Every PDF and native BibTeX matches the SHA-256 recorded at delivery, and the BibTeX bytes are unchanged except for K11. The K11 export has a citation key with spaces, so its registered citation is a derived citation that replaces only that key; the user authorized this exception. The [evidence notes](evidence-notes.md) record each identity check.

## Transcription

All 16 PDFs (262 physical pages) were transcribed locally with PyMuPDF4LLM 0.2.9 on PyMuPDF 1.27.2.3, with physical-page markers and 470 extracted images. This mode differs from the MinerU and OXR transcriptions of earlier batches. The transcription of K01 contained 32 lone UTF-16 surrogates from broken math glyphs, which were replaced with U+FFFD. Two-column layouts are sometimes interleaved in the Markdown, so excerpts were also checked against the PDF text layer. The [extraction ledger](markdown-extraction.json) lists every file and hash.

## Assessment

On November 4, 2026, each paper received a targeted reading of identity, abstract and selected method, setup, evaluation and limitation passages. The [reading ledger](source-reading.json) records the physical pages and retained excerpts. Every card passes `tools.review_check --pdf`; K03 and K10 record abstract waivers because their abstracts were checked against the PDF text layer. Table values were not re-read from rendered pages, and the readings do not establish whole-paper verification.

Use the [source catalog](../library-catalog.csv), [selection and artifact paths](selection.csv) and [source manifest](manifest.json). PDFs, transcriptions, page JSON and figures remain local; public indexes show their paths as code.

| ID | Theme | Year | Paper | Survey use |
|---|---|---:|---|---|
| K01 | T1 | 2024 | [SubT-MRS Dataset: Pushing SLAM Towards All-weather Environments](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_SubT-MRS_Dataset_Pushing_SLAM_Towards_All-weather_Environments_CVPR_2024_paper.html) | Source of the degraded sequences behind the LODESTAR result (Section IV-A), its fusion-challenge outcome (Section IV-B) and a degraded-SLAM benchmark (Table II). |
| K02 | T2 | 2021 | [RELLIS-3D Dataset: Data, Benchmarks and Analysis](https://ieeexplore.ieee.org/document/9561251/) | Off-road terrain-segmentation data beside GA-Nav (Section V-A, Table II). |
| K03 | T3 | 2021 | [STEP: Stochastic Traversability Evaluation and Planning for Risk-Aware Off-road Navigation](https://www.roboticsproceedings.org/rss17/p021.html) | Uncertainty-aware terrain risk that accounts for localization error (Section V-A); qualifies the pose-uncertainty gap claim (Section X-C, Table IV). |
| K04 | T3 | 2022 | [TartanDrive: A Large-Scale Dataset for Learning Off-Road Dynamics Models](https://ieeexplore.ieee.org/document/9811648/) | Off-road dynamics data beside the learned-dynamics discussion (Section V-A, Table II). |
| K05 | T3 | 2024 | [EVORA: Deep Evidential Traversability Learning for Risk-Aware Off-Road Autonomy](https://ieeexplore.ieee.org/document/10606099/) | Uncertainty-aware terrain risk with OOD avoidance (Sections V-A and X-C). |
| K06 | T4 | 2022 | [Kimera-Multi: Robust, Distributed, Dense Metric-Semantic SLAM for Multi-Robot Systems](https://ieeexplore.ieee.org/document/9686955/) | Outlier-robust distributed multi-robot SLAM (Sections VII-B and X-D). |
| K07 | T4 | 2022 | [LAMP 2.0: A Robust Multi-Robot SLAM System for Operation in Challenging Large-Scale Underground Environments](https://ieeexplore.ieee.org/document/9830862/) | Outlier-resilient centralized multi-robot SLAM with batched data after link loss (Sections VII-B and X-D). |
| K08 | T4 | 2022 | [Heterogeneous Ground and Air Platforms, Homogeneous Sensing: Team CSIRO Data61's Approach to the DARPA Subterranean Challenge](https://ieeexplore.ieee.org/document/10876055/) | Communication-limited SubT team system on tracked, legged and aerial robots (Sections VII-C and X-D). |
| K09 | T4 | 2022 | [Resilient and Modular Subterranean Exploration with a Team of Roving and Flying Robots](https://ieeexplore.ieee.org/document/10876072/) | Communication-limited SubT team system with wheeled robots and drones (Sections VII-C and X-D). |
| K10 | T4 | 2022 | [CERBERUS in the DARPA Subterranean Challenge](https://www.science.org/doi/10.1126/scirobotics.abp9742) | Winning SubT team system of legged and aerial robots (Sections VII-C and X-D). |
| K11 | T5 | 2021 | [Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/34173cb38f07f89ddbebc2ac9128303f-Abstract-round2.html) | Scene source of the Habitat benchmarks used by semantic-navigation studies (Section VI-A, Table II). |
| K12 | T5 | 2023 | [LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action](https://proceedings.mlr.press/v205/shah23b.html) | Foundation-model navigation lineage before LeLaN (Section VI-B). |
| K13 | T5 | 2023 | [GNM: A General Navigation Model to Drive Any Robot](https://ieeexplore.ieee.org/document/10161227/) | Foundation-model navigation lineage (Section VI-B). |
| K14 | T5 | 2023 | [ViNT: A Foundation Model for Visual Navigation](https://proceedings.mlr.press/v229/shah23a.html) | Foundation-model navigation lineage (Section VI-B). |
| K15 | T5 | 2024 | [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://ieeexplore.ieee.org/document/10610243/) | Open-vocabulary scene graphs beside HOV-SG (Section VI-A). |
| K16 | T5 | 2024 | [NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://ieeexplore.ieee.org/document/10610665/) | Foundation-model navigation lineage (Section VI-B). |

## Named works that were not added

The same review named further works that this stage did not add:

- VLMaps, whose 2025 journal extension is already in the corpus as S12;
- NeBula, the Team CoSTAR system paper, which exists only as an arXiv preprint;
- learned risk-aware costmaps and learned speed-distribution maps, which the review named without a specific identity;
- the ROS 2 and Nav2 survey and a review of traversability risk assessment, which are surveys rather than corpus works;
- surveys on millimeter-wave radar, safe learning and adverse-weather perception, which are also surveys rather than corpus works and are cited as background references in Table I of the survey.
