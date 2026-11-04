# LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments

## Metadata

| Field | Value |
|---|---|
| ID | R11 |
| Title | LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments |
| Authors | Renxiang Xiao, Yichen Chen, Yuanfan Zhang, Qianyi Shao, Yushuai Chen, Yuxuan Han, Yunjiang Lou, and Liang Hu |
| Venue | IEEE Transactions on Robotics |
| Year | 2026 |
| Type | journal |
| DOI | [10.1109/tro.2026.3699433](https://doi.org/10.1109/tro.2026.3699433) |
| Official URL | https://ieeexplore.ieee.org/document/11543515/ |
| Theme folder | T2-slam-mapping-exploration |
| Batch | ieee-refresh-2026-11-03 |
| Local files | `01-papers/T2-slam-mapping-exploration/2026-LiDAR-Teach-Radar-Repeat-R11/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2026-LiDAR-Teach-Radar-Repeat-R11/paper.md` (local only); [citation.bib](../../../01-papers/T2-slam-mapping-exploration/2026-LiDAR-Teach-Radar-Repeat-R11/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: fault-recovery-deployment
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, dataset-playback
- protocol_caveats: none
- platform_class: skid-steer
- platform: AgileX SCOUT 2.0 for closed-loop teach-and-repeat on a university campus; three platforms over 40+ km and six months (pp. 1, 12, 18).
- boundary_platform: no
- degradation: lidar-degeneracy, scene-change, dynamic-objects, visual-degradation
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task, designed-degradation
- sensors: 3D LiDAR for teaching; forward-looking 4D millimeter-wave radar with Doppler for repeating
- compute: Intel NUC primary with an RTX 4060 laptop secondary over ROS (p. 12); laptop mounting not verified in this reading.
- compute_location: onboard
- summary_result: LiDAR teach and 4D-radar repeat maintain closed-loop route repetition with centimeter-level accuracy across weather, smoke and structural change (pp. 1, 14-17).
- summary_limitation: Radar occupancy mapping for planning and obstacle avoidance is future work (p. 19).
- survey_included: yes
- verification_level: light

## Problem

Teach-and-repeat navigation fails under adverse weather, transient dynamics and slow structural change.

## Mechanism

LiDAR keyframes recorded during teaching are matched with forward 4D radar during repeating by a cross-modal registration network using a Doppler motion prior and LiDAR-intensity/radar-power alignment; adaptive node selection controls storage; localization errors drive incremental fine-tuning without ground-truth labels (pp. 3-11).

## Baselines and controls

ADPGICP radar teach-and-repeat, LIO-SAM, CT-ICP cross-modal registration and Regformer LiDAR teach-and-repeat (pp. 15-16).

## Platform and setup

Open-loop dataset tests and closed-loop campus routes including slopes, narrow areas, moving vehicles, pedestrians and smoke (pp. 12-17). AgileX SCOUT 2.0 for closed-loop teach-and-repeat on a university campus; three platforms over 40+ km and six months (pp. 1, 12, 18).

## Evidence type and transfer

Strongest coded setting: `closed-loop-hardware`. Closed-loop hardware repetition with the method driving the robot; methods failing on the first route are excluded from later routes (p. 15).

## Sensors

3D LiDAR for teaching; forward-looking 4D millimeter-wave radar with Doppler for repeating.

## Compute and latency

Intel NUC primary with an RTX 4060 laptop secondary over ROS (p. 12); laptop mounting not verified in this reading.

## Key quantitative results

- All single-modal radar teach-and-repeat baselines fail to maintain stable registration during long-range navigation (p. 15).

Numbers above come from the inspected text passages; table values were not re-read from rendered pages in this targeted reading.

## Stated limitations

- Enhancing 4D radar occupancy mapping to support planning and obstacle avoidance is future work (p. 19).

## Transfer conditions

Requires a prior LiDAR teaching pass on the same route; obstacle avoidance does not yet use the radar.

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

- **p. 15, Sec. V-C.** "As shown in Table VI, all single-modal radar T&R methods fail to maintain stable registration during long-range navigation."
  Baseline failure under the tested conditions.
- **p. 19, Sec. VI.** "Future work will investigate how to enhance 4-D mmWave radar occupancy mapping to support reliable planning and obstacle avoidance, thereby increasing the safety of cross-modal T&R navigation system."
  Author-stated limit on safety functions.

## Survey-usable statements

### Supported

- Cross-modal teach-and-repeat with label-free adaptation sustains closed-loop wheeled navigation over months under sensing degradation.

### Not supported

- The radar repeat phase is not shown to provide obstacle avoidance or safety guarantees.
- Whole-paper verification and unconditional transfer to another wheeled robot are not established by this targeted reading.

## Verification log

- 2026-11-03 | host: Kiro | scope: targeted source reading of identity, abstract and selected method, setup, evaluation and limitation passages on physical PDF pp. 1, 2, 12, 14, 15, 16, 17, 18, 19; excerpts checked against Markdown and PDF text; table values not re-read from rendered pages; not a whole-paper audit | corrections: none (new card)
- Legacy extraction: none; new targeted reading of the 2026-11-03 IEEE refresh batch.

## Original abstract

Long-term autonomy requires robust navigation in environments subject to dynamic and static changes, as well as adverse weather conditions. Teach-and-repeat (T&R) navigation offers a reliable and cost-effective solution by avoiding the need for consistent global mapping; however, existing T&R systems lack a systematic solution to tackle various environmental variations, such as weather degradation, ephemeral dynamics, and structural changes. This work proposes LiDAR teach radar repeat (LTR$^{2}$), the first cross-modal, cross-platform LiDAR-teach-and-radar-repeat system that systematically addresses these challenges. LTR$^{2}$ leverages LiDAR during the teaching phase to capture precise structural information under normal conditions and utilizes 4-D millimeter-wave radar during the repeating phase for robust operation under environmental degradations. To align sparse and noisy forward-looking 4-D radar with dense and accurate omnidirectional 3-D LiDAR data, we introduce a cross-modal registration (CMR) network that jointly exploits Doppler-based motion priors and the physical laws governing LiDAR intensity and radar power density. Furthermore, we propose an adaptive fine-tuning strategy that incrementally updates the CMR network based on localization errors, enabling long-term adaptability to static environmental changes without ground-truth labels. We demonstrate that the proposed CMR network achieves state-of-the-art CMR performance on the open-access dataset. Then, we validate LTR$^{2}$ across three robot platforms over a large-scale, long-term deployment (40+ km over 6 months), including challenging conditions, such as nighttime smoke. Experimental results and ablation studies demonstrate centimeter-level accuracy and strong robustness against diverse environmental disturbances, significantly outperforming existing approaches.
