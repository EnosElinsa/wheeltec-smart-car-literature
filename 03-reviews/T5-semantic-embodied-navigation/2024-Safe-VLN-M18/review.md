# Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments
## Metadata
| Field | Value |
|---|---|
| ID | M18 |
| Title | Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments |
| Authors | Lu Yue, Dongliang Zhou, Liang Xie, Feitian Zhang, Ye Yan, and Erwei Yin |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 6, pp. 4918-4925 |
| Year | 2024 |
| Type | journal |
| DOI | [10.1109/lra.2024.3387171](https://doi.org/10.1109/lra.2024.3387171) |
| Official URL | https://ieeexplore.ieee.org/document/10496163/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2024-Safe-VLN-M18/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2024-Safe-VLN-M18/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2024-Safe-VLN-M18/citation.bib) |
## Survey coding
- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: simulation
- evidence_all: simulation
- protocol_caveats: none
- platform_class: wheeled-unspecified
- platform: Habitat VLN-CE agent modeled as a 1.5 m mobile robot with simulated panoramic RGB-D; no drive type and no physical chassis
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: simulated panoramic RGB-D (12 RGB and 12 depth cameras); depth-derived 2D LiDAR occupancy mask
- compute: not reported; the JPS-based navigator takes eight times longer than Safe-VLN on val-unseen
- compute_location: not-reported
- summary_result: On R2R-CE in Habitat, Safe-VLN raises SR and SPL over ETPNav and reduces navigation collisions; a JPS-based navigator takes eight times longer on val-unseen.
- summary_limitation: The authors leave real-robot deployment, sim-to-real transfer, and training with real observations to future work; all results come from Habitat.
- survey_included: yes
- verification_level: light
## Problem
Vision-and-language navigation in continuous environments (VLN-CE, in Habitat) drops the discrete navigation-graph assumption and uses low-level actions in continuous 3D indoor meshes. Discrete VLN methods transferred to this setting often ignore collisions: predicted waypoints can lie inside obstacles, the agent can hit furniture on the way to a waypoint, or it can deadlock. The authors argue that this is an obstacle to sim-to-real transfer, because discrete graphs assume perfect node-to-node travel.
## Mechanism
The paper defines three collision types: a waypoint collision (the predicted candidate lies inside an obstacle), a navigation collision (a hit while moving to the next waypoint), and a dynamic collision (a waypoint becomes non-navigable over time; injected synthetically because VLN-CE has no dynamic agents). Safe-VLN adds two modules to ETPNav:
1. Waypoint predictor: the ETPNav heatmap is masked by a simulated 2D LiDAR occupancy mask built from depth, with 2D and 3D LiDAR ablations at 1.0 m and 1.5 m height.
2. Navigator: "re-selection after collision" picks another candidate instead of looping into the same obstacle.
The simulated agent is a 1.5 m mobile robot with 12 RGB and 12 depth cameras at 1.25 m height (30° spacing) and the actions forward 0.25 m, turn ±15°, and stop. The 2D LiDAR occupancy is a 3 m radial map with 12 range bins and 120 heading bins.
## Baselines and controls
ETPNav and an ETPNav variant with a JPS grid planner. Ablations: the occupancy mask (M-Use) and re-selection (R-Use) in training and evaluation, and the LiDAR type and height (2D, 3D, fused).
## Platform and setup
Simulation only: R2R-CE in Habitat on Matterport3D meshes, val-seen and val-unseen splits. Dynamic-collision episodes are synthetic. No physical robot trial is reported.
## Evidence type and transfer
All results come from Habitat. The LiDAR and the panoramic RGB-D are simulator constructs, and the occupancy mask comes from simulated depth, so the results do not show how the method behaves with real LiDAR noise or a real chassis.
## Sensors
Simulated panoramic RGB-D (12 RGB and 12 depth cameras) and an occupancy mask from a constructed 2D or 3D LiDAR derived from depth (3 m range).
## Compute and latency
Not recorded in the legacy extraction beyond the relative timing: on val-unseen, the JPS-based navigator takes eight times longer than Safe-VLN (p. 6).
## Key quantitative results
- Full Safe-VLN reports higher SR and SPL than ETPNav and fewer navigation collisions, with the navigation-collision rate down to a few percent in several rows (Table V).
- Runtime: the JPS-based navigator takes eight times longer than Safe-VLN on val-unseen (p. 6, Table III).
- LiDAR ablation: a reconstructed 3D LiDAR at 1.0 m or fused 2D and 3D LiDAR degrades navigation performance relative to the 2D LiDAR (p. 7, Table IV).
## Stated limitations
- Deploying Safe-VLN on a real robot, studying sim-to-real transfer, and augmenting training data with real observations are future work (p. 8).
- Discrete-graph VLN models trained in simulation are hard to apply to real systems (p. 1).
- A reconstructed 3D LiDAR at 1.0 m degrades performance, which the authors attribute to reconstruction errors on low furniture from occlusion and insufficient lighting (p. 7).
- Grid-based JPS suffers from projection errors, and a finer grid would make the computation cost unaffordable (p. 6).
## Transfer conditions
Legacy reviewer observation: dynamic collisions are not in the VLN-CE dataset and must be injected (not located). The occupancy mask is built from simulated depth, not from a hardware LiDAR. A wheeled robot reusing Safe-VLN needs a real 2D LiDAR or depth-based occupancy at a comparable height and range, and its own check of the re-selection behavior on a physical chassis.
## Code and data
Not recorded in the legacy extraction; not verified.
## Version family
Not recorded in the legacy extraction; not verified.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. I, p. 2 | "First, in comparison to those in discrete environments, the waypoints generated by the waypoint predictor in continuous environments may not be navigable due to the incorrect perception of surrounding environments." |
| C3 | direct-support | moderate | Sec. I, p. 1 | "This leads to a significant challenge when attempting to apply VLN models trained in simulations to real-world systems." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V, p. 8 | "We plan to deploy the proposed Safe-VLN to a real-world robot and conduct collision avoidance evaluation and analysis." |
## Page-cited excerpts
- **p. 2, Introduction.** "First, in comparison to those in discrete environments, the waypoints generated by the waypoint predictor in continuous environments may not be navigable due to the incorrect perception of surrounding environments."
  Perception error is a stated cause of VLN-CE collisions.
- **p. 1, Introduction.** "This leads to a significant challenge when attempting to apply VLN models trained in simulations to real-world systems."
  Sim-to-real is named as a barrier; the letter does not measure a failed physical transfer.
- **p. 8, Conclusion.** "We plan to deploy the proposed Safe-VLN to a real-world robot and conduct collision avoidance evaluation and analysis."
  There is no real-robot evaluation.
- **p. 8, Conclusion.** "To achieve this, we will investigate the sim-to-real transfer of Safe-VLN and explore various methods to enhance the real-world environmental perception such as augmenting the training data with real-world observations."
  Sim-to-real transfer is future work.
- **p. 6, Comparison with JPS.** "the time spent using the JPS-based navigator is eight times longer than that using Safe-VLN"
  The runtime comparison is relative and measured in simulation.
## Survey-usable statements
### Supported
- In Habitat VLN-CE, masking waypoints with a depth-derived 2D LiDAR occupancy and re-selecting after collisions raises SR and SPL over ETPNav and reduces navigation collisions (light review; re-check before citing).
### Not supported
- Safe-VLN has been validated on a robot: the authors defer real-robot evaluation.
- More LiDAR information always helps: the 3D LiDAR at 1.0 m and the fused LiDAR degrade performance.
## Verification log
- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Claim summary, Hardware caveat) converted to the English template; the legacy "~8x" runtime ratio replaced by the paper's "eight times longer" wording; the note that dynamic collisions must be injected moved from limitations to Transfer conditions because it was not located as an author limitation; the two-sentence legacy C6 quote split, with the first sentence in the claim row
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.
## Original abstract
The task of vision-and-language navigation in continuous environments (VLN-CE) aims at training an autonomous agent to perform low-level actions to navigate through 3D continuous surroundings using visual observations and language instructions. The significant potential of VLN-CE for mobile robots has been demonstrated across a large number of studies. However, most existing works in VLN-CE focus primarily on transferring the standard discrete vision-and-language navigation (VLN) methods to continuous environments, overlooking the problem of collisions. Such oversight often results in the agent deviating from the planned path or, in severe instances, the agent being trapped in obstacle areas and failing the navigational task. To address the above-mentioned issues, this letter investigates various collision scenarios within VLN-CE and proposes a classification method to predicate the underlying causes of collisions. Furthermore, a new VLN-CE algorithm, named Safe-VLN, is proposed to bolster collision avoidance capabilities including two key components, i.e., a waypoint predictor and a navigator. In particular, the waypoint predictor leverages a simulated 2D LiDAR occupancy mask to prevent the predicted waypoints from being situated in obstacle-ridden areas. The navigator, on the other hand, employs the strategy of ‘re-selection after collision’ to prevent the robot agent from becoming ensnared in a cycle of perpetual collisions. The proposed Safe-VLN is evaluated on the R2R-CE, the results of which demonstrate an enhanced navigational performance and a statistically significant reduction in collision incidences.
