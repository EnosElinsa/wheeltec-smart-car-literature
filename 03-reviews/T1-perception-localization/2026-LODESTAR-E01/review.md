# LODESTAR: Degeneracy-Aware LiDAR-Inertial Odometry With Adaptive Schmidt-Kalman Filter and Data Exploitation

## Metadata

| Field | Value |
|---|---|
| ID | E01 |
| Title | LODESTAR: Degeneracy-Aware LiDAR-Inertial Odometry With Adaptive Schmidt-Kalman Filter and Data Exploitation |
| Authors | Eungchang Mason Lee, Kevin Christiansen Marsim, and Hyun Myung |
| Venue | IEEE Robotics and Automation Letters, vol. 11, no. 1, pp. 922-929 |
| Year | 2026 (online 2025) |
| Type | journal |
| DOI | [10.1109/lra.2025.3634906](https://doi.org/10.1109/lra.2025.3634906) |
| Official URL | https://ieeexplore.ieee.org/document/11260635/ |
| Theme folder | T1-perception-localization |
| Batch | expansion-2026-10-24 |
| Local files | `01-papers/T1-perception-localization/2026-LODESTAR-E01/paper.pdf` and `02-fulltext/T1-perception-localization/2026-LODESTAR-E01/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T1-perception-localization/2026-LODESTAR-E01/citation.bib) |

## Survey coding

- survey_module: localization-mapping
- secondary_modules: none
- evidence_type: dataset-playback
- evidence_all: dataset-playback
- protocol_caveats: none
- platform_class: mixed
- platform: public datasets only, 14 sequences: 2021 HILTI (5), 2022 HILTI (1), SubT-MRS (2), NTU-VIRAL (3, aerial), Newer College (3, handheld); Cavern Handheld is handheld; carriers of the HILTI and SubT-MRS Long Corridor sequences not stated
- boundary_platform: yes
- degradation: lidar-degeneracy
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, designed-degradation
- sensors: one 3D LiDAR per dataset (Livox Mid-70, PandarXT-32, VLP-16, OS1-16, or OS1-64) and IMU, with known LiDAR-IMU extrinsics
- compute: Intel Core i9-13900K CPU with 32 GB RAM; 28.69 ms average computation time versus 21.04 ms for the FAST-LIO2 baseline
- compute_location: desktop-offline
- summary_result: LODESTAR has the lowest APE on 8 of 13 public sequences in Table V, including 1.386 m versus 3.113 m for its FAST-LIO2 baseline on SubT-MRS Long Corridor.
- summary_limitation: The method handles short-term degeneracy with non-zero returns only; it fails when LiDAR returns are absent, and prolonged zero-return intervals cause IMU dead-reckoning drift.
- survey_included: yes
- verification_level: full

## Problem

LiDAR-inertial odometry (LIO) degrades in degenerate environments such as
long corridors, unstructured caverns, and high-altitude flights, where the
scanned points are unevenly distributed across directions (imbalance) or too
few (sparsity). The Jacobian of the registration problem then becomes nearly
singular, and the estimate drifts or diverges (pp. 1-2). The authors group
earlier remedies into degeneracy-aware constrained optimization,
imbalance-aware weight adjustment, and sparsity-aware data augmentation, and
argue that each addresses only one aspect of degeneracy (p. 2). The paper
targets short-term low-information intervals in which the LiDAR still returns
points; prolonged zero-return intervals are outside its scope (p. 2).

## Mechanism

LODESTAR extends the error-state iterated Kalman filter (ESIKF) of FAST-LIO2.
The state holds the current IMU state (rotation, position, velocity,
gyroscope and accelerometer biases, and gravity) plus s_a active and s_f
fixed past poses in a sliding window of size s_w = s_a + s_f (p. 3). A change
term between adjacent states, inspired by SW-LIO, couples the past poses to
the current one, so point-to-plane residuals of past scans have non-zero
Jacobians with respect to the current state and add constraints against
sparsity (p. 4).

DA-ASKF (degeneracy-aware adaptive Schmidt-Kalman filter) sets the Kalman
gain of the fixed states to zero, which treats them as nuisance parameters.
Their covariances stay unchanged but still shape the gain of the current and
active states, so the fixed states act as reference anchors. The covariance
update uses the Joseph form because the gain is altered (p. 4). Degeneracy is
measured by the condition number χ(H), the ratio of the largest to the
smallest singular value of the stacked Jacobian. At each update the window
slides by one frame. The last active state moves to the fixed set when its
condition number is below the threshold T_χ (full sliding) and is dropped
otherwise (partial sliding), so only non-degenerate states become anchors
(p. 4).

DA-DE (degeneracy-aware data exploitation) splits the Jacobian into rotation
and position blocks, takes their SVDs, and projects each point's Jacobian
onto the right singular vectors to obtain a localizability contribution,
similar to X-ICP (p. 5). It prunes current- and active-state points whose
largest contribution does not exceed T_loc, recomputes the condition number
on the pruned set, and then adds fixed-state points, sorted by their
contribution along the degenerate directions, until the condition number
falls below T_χ (p. 5). In the authors' summary, DA-ASKF provides
degeneracy-aware constrained optimization and mitigates sparsity, and DA-DE
addresses imbalance (p. 1). All datasets use T_χ = 1.5, T_loc = cos 35°,
s_a = 2, and s_f = 2 (p. 6), with a voxel resolution of 0.3 m on the
degenerate datasets and 0.5 m on Newer College (p. 5).

## Baselines and controls

The ablation integrates existing degeneracy-aware modules into a common
FAST-LIO2 baseline: NA-LOAM (imbalance-aware weight adjustment), GenZ-ICP and
AdaLIO (sparsity-aware data augmentation), and the method of Hinduja et al.
(degeneracy-aware constrained optimization). Two naive variants complete it:
Vanilla SW, which updates all window states, and Vanilla Schmidt, which fixes
all past states; both use all measurements without selection. DA-ASKF and
DA-DE are also tested alone (p. 5, Tables III and IV). The integrated modules
are the authors' own implementations, described as self-implemented
degeneracy-aware modules (p. 6). The state-of-the-art comparison uses the
LiDAR-only methods KISS-ICP, GenZ-ICP, and DLO, and the LiDAR-inertial methods
LIO-SAM, DLIO, iG-LIO, and AdaLIO (p. 5). The voxel resolution is held equal
across methods, other parameters are the public defaults with no
sequence-specific tuning, and the authors note that results may therefore
differ from the original papers (p. 5). A small grid search over T_χ and
T_loc on two sequences is reported (p. 6, Table II). No repeated runs and no
statistics on pose error are reported.

## Platform and setup

All experiments replay five public datasets (p. 5): 2021 HILTI (Basement 1,
Basement 4, and Drone Arena indoors; Campus 2 and Construction 2 outdoors),
2022 HILTI (Long Corridor), NTU-VIRAL (SPMS sequences, high-altitude outdoor),
SubT-MRS (Long Corridor, highly imbalanced; Cavern Handheld, unstructured),
and Newer College as the non-degenerate control in open campus areas. One
LiDAR is used per dataset: Livox Mid-70 (2021 HILTI), horizontal OS1-16
(NTU-VIRAL), VLP-16 (SubT-MRS), PandarXT-32 (2022 HILTI), and OS1-64 (Newer
College) (p. 5). Table V covers 13 sequences, with SPMS 01 to SPMS 03 for
NTU-VIRAL and Short exp, Long exp, and Quad dynamics for Newer College, and
Table VI covers 2022 HILTI Long Corridor, so 14 sequences are used in total
(p. 7). LIO-SAM has no Table V entries for 2021 HILTI because it does not
support the sensor (p. 7). The metric is the absolute pose error (APE) computed with EVO; 2022 HILTI and
NTU-VIRAL use their official evaluation tools, and 2022 HILTI is reported as
a score (pp. 5-7, Tables IV and VI). Mapping results are compared only
qualitatively (p. 7, Fig. 4). The paper does not describe the carrier
platforms, speeds, durations, or ground-truth sources of the sequences. Only
sequence and reference names indicate the carriers: the Cavern Handheld
sequence, the Newer College reference titled as a handheld dataset, and the
NTU-VIRAL reference titled as an aerial-vehicle viewpoint (p. 8). No robot of
the authors and no closed loop are involved.

## Evidence type and transfer

All results come from offline playback of public datasets on a desktop CPU,
so the evidence type is dataset-playback. Of the 14 sequences used, four
have carriers identified as handheld (Cavern Handheld and the three Newer
College sequences, from the sequence name and the reference title), three as
aerial (NTU-VIRAL SPMS 01 to 03, from the reference title), and seven have no
carrier stated (the six HILTI sequences and SubT-MRS Long Corridor)
(pp. 5, 8). No class carries a majority and the carriers are only partly
identified, so the platform class is coded as mixed and the paper is a
boundary case. The degenerate sequences were selected for their property
(imbalanced corridor, unstructured cavern, sparse high-altitude flight) and
are reported per sequence beside a non-degenerate control dataset (p. 5), so
lidar-degeneracy is coded as a deliberately selected condition and
designed-degradation appears in evaluation_all. The degeneracy is not varied
within a sequence. The results show odometry accuracy and filter conditioning, not navigation
performance, and the timing applies to a desktop CPU.

## Sensors

The method uses one 3D LiDAR and the IMU of each dataset, with the LiDAR-IMU
extrinsic transformation assumed known and the global frame aligned with the
first IMU frame (p. 3). Multi-LiDAR datasets are reduced to one LiDAR (p. 5).
No camera, wheel odometry, or GNSS is used. Ground truth comes from the
datasets and their official evaluation tools; its source is not described.

## Compute and latency

All tests ran on an Intel Core i9-13900K CPU with 32 GB RAM (p. 7). Table V
reports an average computation time of 28.69 ms for LODESTAR, 21.04 ms for
the FAST-LIO2 baseline, and 9.96 ms for iG-LIO, the lowest in the table, with
DLO second at 13.16 ms (p. 7). The paper does not state whether the average is
per scan, and it does not give the LiDAR rate. Fig. 5 breaks the time into
components: propagation and update times rise slightly because of the extra
window states, DA-DE shortens the mapping time by using fewer points, and
DA-ASKF adds negligible overhead (p. 8). The authors describe the overhead
as minimal. No embedded or onboard processor, memory use, or worst-case
latency is reported.

## Key quantitative results

- APE of 1.386 m on SubT-MRS Long Corridor, 0.671 m on SubT-MRS Cavern Handheld, and 0.089 m on 2021 HILTI Basement 4, versus 3.113 m, 3.521 m, and 0.503 m for the FAST-LIO2 baseline (p. 6, Table III).
- Each module alone helps less: DA-ASKF alone gives 1.833 m, 1.774 m, and 0.192 m, and DA-DE alone 2.082 m, 3.899 m, and 0.332 m on the same three sequences; DA-DE alone is worse than the baseline on Cavern Handheld (p. 6, Table III).
- Fixing all past states (Vanilla Schmidt, 4.283 m) or updating all of them (Vanilla SW, 3.962 m) is worse than the baseline on SubT-MRS Long Corridor; Vanilla Schmidt diverges on Cavern Handheld, where Vanilla SW reaches 1.460 m (p. 6, Table III).
- The integrated NA-LOAM and AdaLIO modules diverge on Cavern Handheld, and the integrated GenZ-ICP module diverges on both SubT-MRS sequences and gives 6.365 m on Basement 4 (p. 6, Table III).
- In the threshold grid (T_χ of 1.5, 2.0, and 3.0; T_loc of cos 30°, cos 35°, and cos 45°), APE is lowest at T_χ = 1.5 and T_loc = cos 35° on both sequences and reaches up to 2.486 m on SubT-MRS Long Corridor and 0.293 m on Basement 4 (p. 6, Table II).
- On 2022 HILTI Long Corridor, LODESTAR scores 33.33 versus 28.33 for the baseline, 16.67 for DA-ASKF alone, 13.33 for DA-DE alone, and 0.00 for Vanilla SW and Vanilla Schmidt (p. 6, Table IV).
- Against state-of-the-art methods on 2022 HILTI Long Corridor, LODESTAR scores 33.33 versus 35.00 for iG-LIO, the highest score, and 28.33 for the baseline; KISS-ICP, GenZ-ICP, and LIO-SAM score 0.00 (p. 7, Table VI).
- LODESTAR has the lowest APE on 8 of the 13 sequences in Table V: SubT-MRS Long Corridor, Basement 4, Campus 2, Drone Arena, SPMS 02, SPMS 03, Long exp, and Quad dynamics (p. 7, Table V).
- LODESTAR is second on Cavern Handheld (0.671 m versus DLIO 0.585 m), Basement 1 (0.174 m versus AdaLIO 0.168 m), and Construction 2 (0.078 m versus iG-LIO 0.064 m), and fourth on SPMS 01 (1.582 m versus iG-LIO 0.237 m, DLIO 1.105 m, and LIO-SAM 1.296 m) and Newer College Short exp (0.429 m versus DLO 0.368 m, iG-LIO 0.369 m, and the FAST-LIO2 baseline 0.412 m) (p. 7, Table V).
- Against its FAST-LIO2 baseline, LODESTAR has lower APE on 12 of the 13 Table V sequences, for example 0.610 m versus 2.973 m on SPMS 02 and 0.582 m versus 0.839 m on SPMS 03; the exception is Short exp (0.429 m versus 0.412 m) (p. 7, Table V).
- For condition numbers, LODESTAR has the narrowest interquartile range on Basement 4, the lowest medians on the two Long Corridor sequences, and the lowest maxima of all modules except DA-ASKF alone; paired t-tests give p-values below 10^-4 and 10^-2 for the marked pairs (p. 6, Fig. 3).
- Average computation time is 28.69 ms for LODESTAR versus 21.04 ms for the baseline on the same desktop CPU; iG-LIO is fastest at 9.96 ms (p. 7, Table V).

## Stated limitations

- LODESTAR handles short-term geometric degeneracy but fails when LiDAR returns are absent; LiDAR-radar fusion with Doppler velocity is future work (p. 8).
- Prolonged zero-return intervals still cause IMU dead-reckoning drift, as in most LIO systems (p. 2).
- The condition number is a practical indicator, not a certificate of solvability: a high condition number does not always imply failure, and low condition numbers do not guarantee better accuracy (pp. 2, 6-7).
- T_χ = 1.5 is described as neither universal nor optimal, and both thresholds come from a small grid search on two sequences (p. 6).
- DA-ASKF alone over-constrains the estimate with the densely scanning LiDAR of 2022 HILTI, and DA-DE alone does not fully resolve imbalance (p. 6).
- Because one voxel resolution is used for all methods, comparator results may differ from their original papers (p. 5).

## Transfer conditions

The method needs a 3D LiDAR and an IMU with known extrinsics, and a
FAST-LIO2-style ESIKF with point-to-plane residuals. The evaluated LiDARs
include 16-channel units (VLP-16, OS1-16) and a Livox Mid-70, which resemble
the sensors of small wheeled robots, but no sequence is identified as coming
from a wheeled ground robot. Planar motion, chassis vibration, and fusion
with wheel odometry were therefore not examined. The thresholds T_χ and
T_loc and the window sizes were fixed after tuning on two sequences and need
checking for a new sensor and environment. Timing comes from a desktop i9
CPU; the cost on an embedded ARM computer is unknown. Scenes where returns
vanish, such as glass corridors or open areas beyond LiDAR range, are outside
the method's scope.

## Code and data

The paper lists an open-source release of the full source code, experimental
configurations, and the self-implemented baselines among its contributions
(p. 2), and states that all configurations and self-implemented
degeneracy-aware modules are in the supplementary material at the DOI
(pp. 1, 6). No repository URL is printed. The repository and the
supplementary material were not verified. All datasets are public.

## Version family

The paper cites no conference or preprint version, and the library holds one
entry for this work. Whether a preprint exists was not verified. AdaLIO
(reference [15]), which shares the last author, is a separate method used as
a comparator, not a version of LODESTAR.

## Claim relations

| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. I, p. 2 | "These conditions result in ill-posed estimation, causing odometry drift or divergence, which can lead to mission failure" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | partial-support | weak | Sec. II, p. 2 | "We detect degeneracy early and adapt updates to keep the filter stable during short-term low-information intervals with non-zero returns" |
| C6 | qualifies | moderate | Sec. IV-B, p. 6 | "a value of 1.5 serves as a practical threshold–neither universal nor optimal–conservatively storing states as fixed." |

## Page-cited excerpts

- **p. 2, Sec. II.** "We detect degeneracy early and adapt updates to keep the filter stable during short-term low-information intervals with non-zero returns, acknowledging that prolonged zero-return intervals still cause IMU dead-reckoning drift as in most LIO systems."
  The scope is short-term low-information degeneracy; LiDAR blackout is excluded by design.
- **p. 5, Sec. IV-A.** "Consequently, all datasets except Newer College exhibit substantial measurement imbalance and sparsity, due to both the small number of LiDAR channels and geometric degeneracy in the environments."
  Degeneracy in the test set comes partly from low-channel LiDARs, not only from scene geometry.
- **p. 5, Sec. IV-A.** "Other parameters follow publicly released default values of each method (no sequence-specific tuning)."
  Comparators run with default parameters and a common voxel size, so their numbers may not match their own papers.
- **p. 6, Sec. IV-B.** "a value of 1.5 serves as a practical threshold–neither universal nor optimal–conservatively storing states as fixed."
  The condition-number threshold is an empirical choice from two sequences.
- **p. 6, Sec. IV-B.** "Vanilla Schmidt treats all past states as fixed references, which caused divergence in Cavern Handheld."
  Fixing past states without a degeneracy test can make the estimate diverge; this motivates the adaptive sliding modes.
- **p. 6, Sec. IV-B.** "For 2022 HILTI (see Table 4), applying DA-ASKF alone over-constrained the estimation due to abundant measurements from the densely scanning LiDAR."
  The window constraint can hurt with dense LiDAR data, so the combination with DA-DE is needed.
- **p. 7, Sec. IV-B.** "While low condition numbers do not optimally guarantee superior accuracy, the lower medians of LODESTAR align with the improved localization metrics in Table 3 and Table 4"
  The condition-number analysis is supporting evidence, not proof that better conditioning causes the accuracy gain.
- **p. 7, Sec. IV-D.** "All tests were run on an Intel Core i9-13900K CPU with 32 GB RAM."
  All timing comes from a desktop CPU without a robot in the loop.
- **p. 7, Sec. IV-D.** "LODESTAR achieved real-time performance on par with other methods, while introducing minimal overhead compared with the baseline."
  This is the authors' wording; Table V gives 28.69 ms versus 21.04 ms for the baseline on the same CPU.
- **p. 8, Sec. V.** "While LODESTAR handles short-term geometric degeneracy, it fails when LiDAR returns are absent."
  The stated failure mode; radar fusion is proposed as future work.

## Survey-usable statements

### Supported

- On public degenerate sequences (SubT-MRS Long Corridor and Cavern Handheld, 2021 HILTI Basement 4), an adaptive Schmidt-Kalman sliding window combined with localizability-based point selection reduced APE versus FAST-LIO2, for example from 3.113 m to 1.386 m on SubT-MRS Long Corridor.
- LODESTAR had the lowest APE on 8 of the 13 Table V sequences and lower APE than its FAST-LIO2 baseline on 12 of them; the exception is Newer College Short exp (0.429 m versus 0.412 m).
- On SubT-MRS Cavern Handheld, LODESTAR reached 0.671 m versus 3.521 m for its baseline, but DLIO was more accurate at 0.585 m.
- Choosing which past states to fix by their condition number matters: fixing all past states or updating all of them was worse than the baseline on SubT-MRS Long Corridor, and fixing all of them diverged on Cavern Handheld.
- Each module alone can hurt: DA-DE alone was worse than the baseline on Cavern Handheld, and DA-ASKF alone scored below the baseline on 2022 HILTI Long Corridor.
- The method runs at a 28.69 ms average on a desktop i9-13900K CPU, against 21.04 ms for FAST-LIO2.

### Not supported

- LODESTAR is the most accurate method on every sequence: it is beaten on 5 of the 13 Table V sequences and on the Table VI score, namely Cavern Handheld (0.671 m versus DLIO 0.585 m), Basement 1 (0.174 m versus AdaLIO 0.168 m), Construction 2 (0.078 m versus iG-LIO 0.064 m), SPMS 01 (1.582 m versus iG-LIO 0.237 m, DLIO 1.105 m, and LIO-SAM 1.296 m), Short exp (0.429 m versus DLO 0.368 m, iG-LIO 0.369 m, and the baseline 0.412 m), and 2022 HILTI Long Corridor (33.33 versus 35.00 for iG-LIO).
- LODESTAR always improves on its own FAST-LIO2 baseline: on Newer College Short exp it has 0.429 m versus 0.412 m for the baseline.
- The method was validated on a wheeled ground robot: only public datasets are used, the identified carriers are handheld and aerial, and the others are not stated.
- The method runs in real time on embedded onboard hardware: timing is reported only for a desktop CPU.
- The method copes with LiDAR blackout or zero returns: the authors state that it fails in that case.
- The APE gains are statistically tested: no repeated runs are reported, and the paired t-tests concern condition numbers only.

## Verification log

- 2026-10-26 | host: Kiro | scope: full text read (Secs. I-V); raw PDF text of pp. 1-8 checked for excerpts and captions; Tables II-VI read from rendered page images of pp. 6-7, not from the MinerU transcription, which shifts the Cavern Handheld cells of Table V into the Long Corridor row, merges the Basement 1 and Basement 4 cells, and groups Short exp under NTU-VIRAL; Fig. 1 image viewed; independent fact-check applied | corrections: rebuilt in English template format; unsupported ground-robot platform claim removed; roles of DA-ASKF and DA-DE corrected; ablation module list completed; code-availability statement corrected; excerpt section label corrected; Table V comparison rewritten with every counterexample; platform_class changed to mixed; C6 excerpt replaced (details in 06-data/review-corrections.csv)
- Legacy extraction: automated reviewer (codex), expansion batch 2026-10-24. Legacy evidence files: 99-archive/history-2026-10-25.zip::expansions/2026-10-24/evidence/T1-T2/08654bae72c2e10675156377/

## Original abstract

LiDAR-inertial odometry (LIO) has been widely used in robotics due to its high accuracy. However, its performance degrades in degenerate environments, such as long corridors and high-altitude flights, where LiDAR measurements are imbalanced or sparse, leading to ill-posed state estimation. In this letter, we present LODESTAR, a novel LIO method that addresses these degeneracies through two key modules: degeneracy-aware adaptive Schmidt-Kalman filter (DA-ASKF) and degeneracy-aware data exploitation (DA-DE). DA-ASKF employs a sliding window to utilize past states and measurements as additional constraints. Specifically, it introduces degeneracy-aware sliding modes that adaptively classify states as active or fixed based on their degeneracy level. Using Schmidt-Kalman update, it partially optimizes active states while preserving fixed states. These fixed states influence the update of active states via their covariances, serving as reference anchors–akin to a lodestar. Additionally, DA-DE prunes less-informative measurements from active states and selectively exploits measurements from fixed states, based on their localizability contribution and the condition number of the Jacobian matrix. Consequently, DA-ASKF enables degeneracy-aware constrained optimization and mitigates measurement sparsity, while DA-DE addresses measurement imbalance. Experimental results show that LODESTAR outperforms existing LiDAR-based odometry methods and degeneracy-aware modules in terms of accuracy and robustness under various degenerate conditions.
