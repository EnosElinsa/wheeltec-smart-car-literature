# FIT-SLAM 2: Efficient 3D exploration with Fisher information and traversability-based adaptive roadmap

## Metadata

| Field | Value |
|---|---|
| ID | E13 |
| Title | FIT-SLAM 2: Efficient 3D exploration with Fisher information and traversability-based adaptive roadmap |
| Authors | Suchetan Saravanan, Anais Bains, Caroline P.C. Chanel, and Damien Vivet |
| Venue | Robotics and Autonomous Systems, vol. 194, article 105188 |
| Year | 2025 |
| Type | journal |
| DOI | [10.1016/j.robot.2025.105188](https://doi.org/10.1016/j.robot.2025.105188) |
| Official URL | https://linkinghub.elsevier.com/retrieve/pii/S0921889025002854 |
| Theme folder | T2-slam-mapping-exploration |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T2-slam-mapping-exploration/2025-FIT-SLAM2-E13/paper.pdf` and `02-fulltext/T2-slam-mapping-exploration/2025-FIT-SLAM2-E13/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T2-slam-mapping-exploration/2025-FIT-SLAM2-E13/citation.bib) |

## Survey coding

- survey_module: traversability-planning-control
- secondary_modules: localization-mapping
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: external-pose-source, video-only-hardware, few-trials
- platform_class: skid-steer
- platform: simulated skid-steer differential-drive vehicle in Gazebo; four-wheel differential-drive rover in the field run (Fig. 17(a))
- boundary_platform: no
- degradation: terrain
- degradation_observed: visual-degradation
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task, residual, designed-degradation
- sensors: RGB-D camera with ORB-SLAM3 and VLP-16 LiDAR for traversability (simulation); ZED 2i stereo camera with ORB-SLAM3 and stereo point cloud (field)
- compute: Intel i5-13420H at 3.4 GHz, ROS 2 Humble in Docker; mean planning time 20.8 ms without and 63.0 ms with Fisher information
- compute_location: not-reported
- summary_result: With simulator ground-truth poses, exploration took 880 s versus 1118 s (FAEL) in Cave and 342 s versus 479 s (GB-Planner 2) in Marsyard; tuned FAEL was faster in Corridor.
- summary_limitation: The authors state that ground-truth-pose benchmarking ignores localization drift and perception errors, and that the field run was a proof of concept without benchmarking.
- survey_included: yes
- verification_level: full

## Problem

Exploration planners for ground robots in unstructured, GNSS-denied terrain
are usually decoupled from SLAM, so they ignore localization uncertainty and
can drive the robot into feature-poor areas where visual tracking fails and
the robot falls into dead reckoning (pp. 1-2). The paper extends the authors'
FIT-SLAM into an active SLAM framework for unmanned ground vehicles that
couples a traversability map and a planning roadmap to the SLAM pose graph,
orders frontiers with an open-path TSP, and prunes path segments with low
expected Fisher information.

## Mechanism

- Traversability (pp. 5-6): each cell of a local 2D grid gets step height,
  slope, and roughness from the points in the cell and its 8 neighbors,
  normalized by the robot's ground clearance and maximum slope; the cell
  risk is the maximum of these metrics. Local maps registered at SLAM
  keyframes are fused into a global map with log-odds updates, and the
  global map is recomputed when keyframe poses change. Table 1 (p. 11) uses
  0.25 m cells, 40° maximum slope, and 0.2 m ground clearance.
- Frontiers (p. 6): known traversable cells next to unknown cells, found by
  BFS, clustered with minimum and maximum cluster sizes and a risk
  threshold; the utility is the Shannon-entropy reduction for the best
  camera orientation, as in FIT-SLAM.
- Roadmap (pp. 6-8): an undirected graph of frontier nodes and the keyframes
  from which they were observed. A frontier-to-keyframe edge is taken as
  collision-free; other edges are checked on the traversability map, with
  edge cost equal to the summed traversability of the crossed cells. Nodes
  are found with a hash grid. Each frontier keeps a fixed transform to its
  keyframe, so a loop closure moves the nodes with the optimized keyframes,
  after which edges are re-checked.
- Goal ordering (pp. 8-9): frontiers inside a radius around the robot are
  local; the route from the robot through all local frontiers to the
  nearest global frontier is an open-path TSP, solved by brute force with
  cached bidirectional edge costs; replanning starts after the first
  frontier is observed.
- Localizability (pp. 9-10): the Fisher information matrix of unit-bearing
  landmark observations is precomputed per voxel of the camera field of
  view and scalarized with the A-optimality criterion; repeated landmarks in
  one voxel are down-weighted with an exponential decay. Information is
  summed at roadmap nodes within a look-ahead distance; an edge whose pose
  falls below a threshold is removed from the roadmap and replanning is
  triggered (Algorithm 4).

## Baselines and controls

The exploration comparators are NBVP, FIT-SLAM 1, GB-Planner 2, and FAEL
(p. 11). All share the vehicle, localization, start position, and a
pure-pursuit controller at 1.0 m/s (p. 11). FAEL's default 1.0 m sampling
interval left the Corridor run at 36% coverage, so the authors reduced the
sampling interval and viewpoint spacing to 0.35 m and kept these values for
all worlds (pp. 13-14). Runs stop when the world is explored or after a
fixed duration, defined as the time at which at least 4 of the 5 methods had
fully explored it, and runs that largely exceeded the others were aborted
manually (p. 12). By this review's count, only 3 of 5 methods completed
Marsyard (FAEL and NBVP are marked as terminated), so the stated rule does
not match that world. The localization ablation compares FIT-SLAM 2 with and
without Fisher information in Marsyard with all other parameters identical
(p. 14); no baseline planner is run with SLAM.

## Platform and setup

- Simulation (Gazebo): a skid-steer differential-drive vehicle with an RGB-D
  camera and a VLP-16 LiDAR (p. 11). Worlds: Corridors (3520 m²), Cave
  (2425 m², moderately uneven terrain), and Marsyard (1100 m², craters,
  mounds, rocky surfaces) (p. 11). The exploration-time and planner-runtime
  comparisons use ground-truth poses from the simulator (pp. 12, 15). Each
  method appears with one value per world; repeated runs are not reported.
- Localization ablation: Marsyard with ORB-SLAM3; Fig. 14 shows one run with
  and one without Fisher information. Runs without it often aborted; their
  number is not given (p. 14).
- Field run: one outdoor exploration with a differential-drive rover, a ZED
  2i stereo camera, ORB-SLAM3, and a stereo point cloud for traversability
  (pp. 17-18). Fig. 17(a) shows a four-wheel rover; with the text's
  "differential-drive", this review codes skid-steer. Only the trajectory
  and reconstruction are shown (Fig. 17(b)).

## Evidence type and transfer

The method drives a physical rover in the field run, so the strongest
setting is closed-loop hardware, but that run has no metric, no comparator,
and no ground truth (p. 19). Every number comes from simulation. Exploration
times and the planner comparison isolate the planner from SLAM error by
using simulator poses; only the Fisher-information ablation runs with a
SLAM back-end, and it compares the method with itself. The headline 33% is
therefore a simulated planning result, not a field result.

## Sensors

Simulation: RGB-D camera for ORB-SLAM3 and a VLP-16 LiDAR for
traversability (p. 11). Field: ZED 2i stereo camera for ORB-SLAM3 and for
the traversability point cloud (p. 18); the LiDAR visible on the rover in
Fig. 17(a) is not named as an input. The Fisher-information model in Fig. 6
assumes a 70° camera field of view and σ² = 0.001 I₃ (p. 10). Simulator
poses serve as ground truth for the localization errors of Fig. 14.

## Compute and latency

All experiments ran on an Intel i5-13420H CPU at 3.4 GHz in Docker with ROS
2 Humble on Ubuntu 22.04 (pp. 11, 15). Modules were compiled in Release
mode and ran in a separate container from Gazebo and visualization; CPU and
memory were sampled at 1 Hz from Docker container statistics (p. 15). Fig.
16 covers the Corridor run. The paper does not say which computer ran the
field rover's software or whether it was onboard.

## Key quantitative results

Tables 1-4 and Figs. 14 and 16 were read from the rendered page images.

- Exploration time with simulator poses, FIT-SLAM 2 versus FIT-SLAM 1, FAEL, GB-Planner 2, NBVP: Corridor 1809 s versus 2883, 1706, 2421, and 2895 s (NBVP terminated); Cave 880 s versus 1384, 1118, 1133, and 1449 s (NBVP terminated); Marsyard 342 s versus 544, 443 (FAEL terminated), 479, and 689 s (NBVP terminated) (p. 12, Table 2).
- The "% Incr. exploration" row gives 27.04% for Cave (against FAEL) and 40% for Marsyard (against GB-Planner 2), and "–" for Corridor, where FAEL was 103 s (5.69%) faster (pp. 12, 14, Table 2). The text's 33% for unstructured worlds and 20.47% over all worlds match the mean of 27.04% and 40.06%, and that mean with -5.69% included, by this review's arithmetic (p. 12).
- Mean planning time per iteration with simulator poses: FIT-SLAM 2 without Fisher information 20.80 ms versus FIT-SLAM 1 620.58 ms, GB-Planner 2 431.26 ms, FAEL 207.86 ms, and NBVP 2762.11 ms (p. 16, Table 3). The worlds included in this aggregate are not stated. The text calls this 100 times faster than NBVP and FIT-SLAM 1 (p. 16); the table gives factors of about 133 for NBVP and 30 for FIT-SLAM 1.
- Module times in active SLAM mode: frontier search 3.4 ms, roadmap update 3.2 ms, full path optimization 14.2 ms, Fisher-information evaluation 42.2 ms; overall 20.8 ms without and 63.0 ms with Fisher information (p. 17, Table 4). The text says that Fisher information takes nearly half of the planning time (p. 17), while 42.2 of 63.0 ms is about two thirds.
- CPU and memory, Corridor run: FIT-SLAM 2 has the lowest CPU use throughout, roughly 10-25% against about 30-250% for the others, where GB-Planner 2 and FIT-SLAM 1 start near 30-50% (container percentages, read from the plot); its memory is above FIT-SLAM 1 and below FAEL and NBVP, and below GB-Planner 2 only after roughly 1,000 s, before which GB-Planner 2 uses less (pp. 16, 18, Fig. 16). No numeric values are tabulated.
- Localization ablation, one Marsyard run each: without Fisher information the translational error peaks near 3.9 m and the rotational error leaves the 15° scale, while with it the translational error stays below about 1.5 m; the run with Fisher information lasts about 575 s against about 495 s (p. 17, Fig. 14, read from the plot; the paper gives no numbers).

## Stated limitations

- Benchmarking with simulator ground-truth poses does not account for localization drift and perception errors, which can significantly affect real deployments (p. 12).
- Using Fisher information reduces localization error but with a small increase in exploration time, because safer paths are longer (p. 14).
- Several challenges remain for safe yet efficient exploration with a visual SLAM back-end (p. 14).
- The Fisher-information evaluation does not directly reduce localization uncertainty, and the system does not explicitly seek loop closures (pp. 14-15).
- The field experiment was not used to benchmark against other methods; it is a proof of concept (p. 19).
- In highly dynamic environments or with moving obstacles, the roadmap may become partially disconnected or outdated; this is beyond the scope of the work (p. 19).
- Future work: perception models that address sensor uncertainty and occlusion, and multi-robot exploration with roadmap fusion (p. 19).

## Transfer conditions

The traversability thresholds (0.2 m clearance, 40° slope, 0.25 m cells)
are set for the simulated vehicle and must be re-identified for another
robot. The localizability check needs a feature-based visual SLAM that
exposes its landmark map and keyframes (ORB-SLAM3 here), a calibrated camera
field of view, and a threshold whose value the paper does not report. The
roadmap's collision-free guarantee for frontier-to-keyframe edges holds only
for the static map at the time of observation, which is the dynamic-scene
limitation the authors name. The speed advantage over baselines was shown
only with perfect poses at 1.0 m/s in simulation; with SLAM, only the
self-ablation exists. A wheeled robot with a 2D LiDAR and no camera cannot
use the Fisher-information module as described.

## Code and data

The authors release the implementation at https://github.com/suchetanrs/FIT-SLAM
(p. 1); the data availability statement says only that a GitHub link is
given (p. 19). The Cave world comes from
https://github.com/LTU-RAI/darpa_subt_worlds and Marsyard from
https://github.com/LeoRover/leo_simulator (p. 11). The repository content
and any field data were not verified.

## Version family

This journal paper extends FIT-SLAM (ICARA 2024,
[10.1109/ICARA60736.2024.10553174](https://doi.org/10.1109/ICARA60736.2024.10553174)),
which is the FIT-SLAM 1 baseline (pp. 2, 11). The conference paper is not in
the library; the work is counted once, by this article.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | partial-support | moderate | Sec. 4.3, p. 14 | "It is important to notice that without the assistance of Fisher Information, the robot often lost it is tracking, leading to dead-reckoning." |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | weak | Sec. 4.3, p. 14 | "In the other cases, the exploration was aborted due to a large accumulation of localization error without Fisher Information." |
| C6 | qualifies | moderate | Sec. 4.5, p. 19 | "While this experiment was not used to benchmark against other methods, it serves as a proof of concept, demonstrating that the proposed approach is viable for deployment in real-world conditions." |

## Page-cited excerpts

- **p. 12, Sec. 4.2.** "However, we acknowledge that this approach does not account for real-world challenges such as localization drift and perception errors, which can significantly impact exploration performance in practical deployments."
  The exploration-time comparison of Table 2 uses simulator poses and says nothing about end-to-end performance with SLAM.
- **p. 12, Sec. 4.2.** "The manual aborts were done when the exploration largely exceeded the other approaches in the same setting."
  Terminated entries in Table 2 are lower bounds, not completion times.
- **p. 14, Sec. 4.2.** "FAEL marginally outperformed our method in one scenario by 103 s (5.69%)."
  The authors' own counterexample in the structured Corridor world.
- **p. 14, Sec. 4.3.** "The exploration run used for comparison in Fig. 14 was one of the rare cases where the robot completed it is exploration without Fisher Information."
  Fig. 14 compares against a surviving run; no failure rate is given.
- **p. 14, Sec. 4.3.** "Note that, the proposed FIM-based evaluation does not directly reduce localization uncertainty; rather, it helps limit its increase by guiding the robot through areas with higher expected information gain"
  The module avoids low-observability paths; it is not an active loop-closure planner.
- **p. 16, Sec. 4.4.** "In summary, FIT-SLAM 2 planning time was 100 times faster than NBVP and FIT-SLAM 1, 20 times faster than GB-Planner 2 and 10 times faster than FAEL."
  Table 3 supports about 133x, 30x, 21x, and 10x; the 100x figure does not hold for FIT-SLAM 1.
- **p. 19, Sec. 5.** "First, note that in highly dynamic environments or in the presence of moving obstacles, the roadmap may become partially disconnected or outdated, which can impair the planner’s effectiveness."
  The roadmap assumes a static scene.

## Survey-usable statements

### Supported

- In Gazebo with simulator poses, a SLAM-keyframe-and-frontier roadmap with open-path TSP ordering explored Cave in 880 s versus 1118 s and Marsyard in 342 s versus 479 s for the next-best completed planner.
- Removing roadmap edges with low precomputed Fisher information kept visual SLAM tracking in a simulated Marsyard run where runs without it often aborted, at the cost of a longer exploration.
- Planning without Fisher information took 20.8 ms per iteration on an Intel i5-13420H CPU, and the Fisher-information check added 42.2 ms.

### Not supported

- FIT-SLAM 2 explores fastest in every world: tuned FAEL was 103 s faster in Corridor (1706 s versus 1809 s).
- The 33% gain holds on a real robot or with SLAM: it comes from two simulated worlds with ground-truth poses, and the field run has no comparator.
- FIT-SLAM 2 improves localization accuracy over state-of-the-art planners, as the abstract implies: localization error is compared only with the method's own variant without Fisher information, in single runs.
- Planning is 100 times faster than FIT-SLAM 1: Table 3 gives about 30 times.
- FIT-SLAM 2 uses the least resources on every metric: its memory use is above FIT-SLAM 1 throughout and above GB-Planner 2 for roughly the first 1,000 s (Fig. 16(b)), and the Fisher-information check triples planning time.
- The Fisher-information module raises the exploration success rate by a stated amount: no number of runs or failure rate is reported.
- The method runs onboard a small rover: the field run's computer is not stated.

## Verification log

- 2026-10-27 | host: Kiro | scope: full text read; Tables 1-4 and Figs. 14, 16, and 17 read from rendered page images (pp. 11, 12, 16, 17, 18); setup, protocol, and limitation statements checked on pp. 1, 2, 5-19 | corrections: field run recoded as closed-loop hardware without metrics; platform class from the text and Fig. 17(a); stopping-rule mismatch in Marsyard, 100x and nearly-half inconsistencies recorded; localization claim limited to self-ablation; unsupported "Pi" timing statement dropped (see tmp/corrections/E13.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/54ed476388933cf5dc761f22/

## Original abstract

This paper presents FIT-SLAM 2, an enhanced framework for autonomous 3D exploration, integrating Fisher Information and a traversability-aware adaptive roadmap. Building on FIT-SLAM, our approach introduces frontier classification into local and global categories, a scheduling strategy for exploration path computation, and optimized real-time Fisher Information computation using pre-computed lookup tables to assess localization confidence and ensure safe exploration. FIT-SLAM 2 seamlessly integrates with the SLAM backend while iteratively constructing and updating an adaptive roadmap that optimizes both navigation efficiency and safety. This enables the robot to efficiently explore complex environments – including rocky terrains, caves, and mazes – while maintaining robust localization. Extensive experiments demonstrate that FIT-SLAM 2 achieves a 33% increase in exploration rate in unstructured environments along with a notable improvement in localization accuracy and computational efficiency over state-of-the-art methods. For reproducibility and future enhancements, we release our implementation at https://github.com/suchetanrs/FIT-SLAM.
