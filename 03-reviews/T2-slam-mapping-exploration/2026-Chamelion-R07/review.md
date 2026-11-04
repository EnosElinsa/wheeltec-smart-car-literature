# Chamelion: Reliable Change Detection for Long-Term LiDAR Mapping in Transient Environments

## Metadata

| Field | Value |
|---|---|
| ID | R07 |
| Title | Chamelion: Reliable Change Detection for Long-Term LiDAR Mapping in Transient Environments |
| Authors | Seoyeon Jang, Alex Junho Lee, I Made Aswin Nahrendra, and Hyun Myung |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3665079](https://doi.org/10.1109/lra.2026.3665079) |
| Official URL | https://ieeexplore.ieee.org/document/11397150/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-Chamelion-R07/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-Chamelion-R07/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-Chamelion-R07/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: recorded-robot-data
- evidence_all: recorded-robot-data, dataset-playback
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Custom LiDAR dataset from construction sites and a laboratory (prior map August 2024, scans October 2024) plus public data; carrier not inspected in this reading (p. 5).
- boundary_platform: no
- degradation: scene-change
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: 3D LiDAR
- compute: 14.8 Hz on RTX 3060 and 2.74 Hz on Jetson Orin NX (p. 7).
- compute_location: desktop-offline
- summary_result: Change detection trained on synthesized structural changes updates prior maps online; the network runs at 14.8 Hz on RTX 3060 and 2.74 Hz on Orin NX (p. 7).
- summary_limitation: A fixed learned cross-visibility performs best when registration errors are small and voxel sizes match training (p. 8).
- survey_included: yes
- verification_level: light

## Problem

Occlusion and frequent reconfiguration make LiDAR change detection and long-term map maintenance unreliable.

## Mechanism

Composition-based augmentation imports elements from other scenes to create pseudo change labels; a 4D sparse convolutional dual-head network classifies change and cross-visibility confidence; probabilistic integration updates the prior map (pp. 2-5).

## Baselines and controls

MapMOS and other LiDAR change-detection methods; ablations of map resolution, registration error and dynamic-object removal (pp. 5-7).

## Platform and setup

Real construction-site and office data with a two-month interval between map and scans, plus synthetic datasets (p. 5). Custom LiDAR dataset from construction sites and a laboratory (prior map August 2024, scans October 2024) plus public data; carrier not inspected in this reading (p. 5).

## Evidence type and transfer

Strongest coded setting: `recorded-robot-data`. Offline evaluation of recorded scans against a prior map; map updates are not linked to executed navigation.

## Sensors

3D LiDAR.

## Compute and latency

14.8 Hz on RTX 3060 and 2.74 Hz on Jetson Orin NX (p. 7).

## Key quantitative results

- Runtime is 14.83 Hz on RTX 3060 and 2.74 Hz on Orin NX with similar IoU and F1 (p. 7, Table IV).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- The framework learns a fixed cross-visibility and performs better when registration errors are small or voxel sizes resemble the training data (p. 8).

## Transfer conditions

Depends on accurate map-to-scan registration; embedded throughput is below typical LiDAR rates.

## Code and data

Availability statements and external repositories were not checked in this targeted reading; not verified.

## Version family

Counted once by the registered publication identity; no other version is in the library.

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

- **p. 8, Sec. V.** "As future work, we plan to dynamically compute cross-visibility to enhance robustness under varying registration errors and voxel resolutions."
  Indicates the registration and resolution dependence.
- **p. 7, Sec. IV-E.** "As shown in Table IV, the network runs at 14.8 Hz on the RTX 3060 and 2.74 Hz on the Orin NX."
  Embedded runtime.

## Survey-usable statements

### Supported

- Learned change detection can maintain a prior LiDAR map under construction-site change.

### Not supported

- Map maintenance is not shown to change localization or planning during operation.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 5, 6, 7, 8; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Online change detection is crucial for mobile robots to efficiently navigate through dynamic environments. Detecting changes in transient settings, such as active construction sites or frequently reconfigured indoor spaces, is particularly challenging due to frequent occlusions and spatiotemporal variations. Existing approaches often struggle to detect changes and fail to update the map across different observations. To address these limitations, we propose a dual-head network designed for online change detection and long-term map maintenance. A key difficulty in this task is the collection and alignment of real-world data, as manually registering structural differences over time is both labor-intensive and often impractical. To overcome this, we develop a data augmentation strategy that synthesizes structural changes by importing elements from different scenes, enabling effective model training without the need for extensive ground-truth annotations. Experiments conducted at real-world construction sites and in indoor office environments demonstrate that our approach generalizes well across diverse scenarios, achieving efficient and accurate map updates.
