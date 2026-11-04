# Multi-Session Mapping and Long-Term Localization for Autonomous Vehicles Using Radar

## Metadata

| Field | Value |
|---|---|
| ID | R09 |
| Title | Multi-Session Mapping and Long-Term Localization for Autonomous Vehicles Using Radar |
| Authors | Daniel Casado Herraez, Matthias Zeller, Dong Wang, Jens Behley, Michael Heidingsfeld, and Cyrill Stachniss |
| Venue | IEEE Robotics and Automation Letters |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/lra.2026.3653332](https://doi.org/10.1109/lra.2026.3653332) |
| Official URL | https://ieeexplore.ieee.org/document/11346986/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-Radar-Long-Term-R09/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-Radar-Long-Term-R09/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-Radar-Long-Term-R09/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: road-vehicle
- platform: SNAIL-Radar and HeRCULES automotive-radar sequences with the ARS548 radar (p. 5).
- boundary_platform: yes
- degradation: scene-change
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: Automotive 4D radar with Doppler velocities
- compute: Processor not inspected in this reading.
- compute_location: desktop-offline
- summary_result: Multi-session radar loop verification and temporal map maintenance preserve persistent points and support localization in maintained maps (pp. 6-7).
- summary_limitation: Map generation assumes a planar vehicle trajectory (p. 5).
- survey_included: yes
- verification_level: light

## Problem

LiDAR-oriented multi-session mapping fails on sparse automotive radar data, and maps degrade with change.

## Mechanism

Per-session radar SLAM maps are aligned by place recognition with multi-sequence loop detection and verification; a temporal occupancy grid filters noise and movable objects; localization combines odometry, scan-to-map matching and Doppler velocity (pp. 3-5).

## Baselines and controls

LiDAR-derived alignment methods and RaI-SLAM or RIV-SLAM back ends; maintained versus non-maintained maps (pp. 5-7).

## Platform and setup

Public multi-session radar datasets; failed baseline runs are marked N/A and omitted from averages (p. 6). SNAIL-Radar and HeRCULES automotive-radar sequences with the ARS548 radar (p. 5).

## Evidence type and transfer

Strongest coded setting: `dataset-playback`. Dataset replay on road vehicles.

## Sensors

Automotive 4D radar with Doppler velocities.

## Compute and latency

Processor not inspected in this reading.

## Key quantitative results

- Localization in a non-maintained map can fail at low compression and recover after heavy downsampling removes wrong correspondences (p. 7).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- A planar vehicle trajectory is assumed during map generation (p. 5).

## Transfer conditions

Road-vehicle radar geometry and planar motion differ from small indoor robots; failed baseline runs are excluded from averages.

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

- **p. 5, Sec. IV-A.** "During map generation, we assume a planar vehicle trajectory."
  Stated modeling assumption.
- **p. 6, Sec. IV-C.** "In our evaluation, we omit the results of methods with failed runs."
  Failure censoring in the averages.

## Survey-usable statements

### Supported

- Radar maps can be aligned across sessions and maintained for long-term localization on public vehicle data.

### Not supported

- The approach is not evaluated on a robot whose navigation depends on the maintained map.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 3, 5, 6, 7; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Localization of autonomous vehicles in existing maps is crucial for reliable navigation. Using previously constructed maps allows vehicles to estimate their pose without the inherent odometry drift. Building such maps involves aligning data recorded at different times and maintaining the map over time. While LiDAR sensors are commonly used for mapping due to their high accuracy, they are sensitive to adverse weather and involve high production costs. In this letter, we address the problem of long-term mapping and localization leveraging automotive radars, which are robust to weather conditions and offer a cost-effective alternative to LiDARs. In our approach, we construct maps of coinciding areas and align them by performing place recognition between them. Additionally, our multi-sequence loop detection and verification strategy for radar sensors is able to filter incorrect loop matches, enhancing trajectory alignment. Then, our novel map maintenance module handles radar noise and preserves persistent map points that remain reliable for localization. Subsequently, we estimate the robot poses in the resulting map by combining local odometry with scan-to-map matching, overcoming the complexities of sparse automotive radar data. We evaluate our method on public automotive radar datasets. The results show that our approach achieves state-of-the-art trajectory alignment, preserves persistent map points for localization, and reliably localizes within the constructed maps.
