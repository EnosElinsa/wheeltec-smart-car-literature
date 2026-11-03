# Socially compliant mobile robot navigation via inverse reinforcement learning
## Metadata
| Field | Value |
|---|---|
| ID | X15 |
| Title | Socially compliant mobile robot navigation via inverse reinforcement learning |
| Authors | Henrik Kretzschmar, Markus Spies, Christoph Sprunk, and Wolfram Burgard |
| Venue | The International Journal of Robotics Research, vol. 35, no. 11, pp. 1289-1307 |
| Year | 2016 (online 2015) |
| Type | journal |
| DOI | [10.1177/0278364915619772](https://doi.org/10.1177/0278364915619772) |
| Official URL | https://doi.org/10.1177/0278364915619772 |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | supplemental |
| Local files | `01-papers/T5-semantic-embodied-navigation/2016-IRL-social-nav-X15/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2016-IRL-social-nav-X15/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2016-IRL-social-nav-X15/citation.bib) |
## Survey coding
- survey_module: traversability-planning-control
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, dataset-playback, simulation
- protocol_caveats: video-only-hardware
- platform_class: wheeled-unspecified
- platform: autonomous robotic wheelchair with onboard laser range finders (no drive type in the legacy extraction)
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: residual
- evaluation_all: residual, closed-loop-task
- sensors: laser range finders (Monte Carlo localization and a laser-based people tracker)
- compute: not reported
- compute_location: not-reported
- summary_result: In simulation over ten hallway scenarios, the learned policy keeps 0.34 m minimum clearance, while time-configuration A* with a 0.8 m minimum distance is blocked 60% of the time.
- summary_limitation: The authors assume cooperative agents and state that settings such as evacuations would need game-theoretic modeling.
- survey_included: context
- verification_level: light
## Problem
Robots that treat nearby humans as static obstacles freeze or find no feasible path in hallways. Cooperative pedestrian behavior mixes discrete homotopy choices (passing left or right) with stochastic continuous trajectories, which deterministic social-force or RVO models miss.
## Mechanism
Maximum-entropy inverse reinforcement learning fits a mixture distribution over composite trajectories: discrete homotopy classes plus continuous dynamics. Feature expectations are computed with Hamiltonian Markov chain Monte Carlo sampling, and a Voronoi graph enumerates the homotopy classes. The robot jointly samples its own path and the predicted pedestrian paths, or it can be taught a behavior by teleoperation. Laser Monte Carlo localization runs in a static map, and a laser people tracker supplies pedestrian states. Shared autonomy adds a joystick-direction feature.
## Baselines and controls
Pedestrian modeling is compared with Kuderer et al., social forces, and RVO. Navigation is compared in simulation with a time-configuration A* planner that assumes constant-velocity humans.
## Platform and setup
- Pedestrian modeling: a one-hour motion-capture set (81 composite trajectories) and the Pellegrini et al. hotel set (71 trajectories), with five-fold cross-validation, plus a Turing test with 10 subjects.
- Real robot: office-hallway trials on a robotic wheelchair with laser range finders, covering static clutter, oncoming pedestrians, and two pedestrians blocking the corridor.
- Simulation: comparison with time-configuration A* on recorded pedestrian evasion tracks.
## Evidence type and transfer
The numeric comparisons come from dataset cross-validation and from simulation. The real wheelchair runs show the behavior qualitatively in an office hallway; trial counts and metrics are not recorded in the legacy extraction.
## Sensors
Laser range finders for Monte Carlo localization and people tracking.
## Compute and latency
Not recorded in the legacy extraction; not verified.
## Key quantitative results
- Simulation, ten scenarios: the learned policy keeps a minimum clearance of 0.34 m (p. 16, Table 1).
- Simulation: mean speed of the learned policy 0.56 m/s (Table 1).
- Simulation: time-configuration A* with r_min = 0.8 m is blocked 60% of the time (freezing-robot problem) (p. 16, Table 1).
- Pedestrian data: 81 composite trajectories in the motion-capture set and 71 in the hotel set, with five-fold cross-validation (p. 13).
## Stated limitations
- The approach assumes cooperative agents; modeling evacuation scenarios would require game-theoretic aspects (p. 2).
## Transfer conditions
Legacy reviewer observations (not located as author limitations): pedestrian goals are assumed known in the robot experiments; teleoperation teaching is an alternative to imitating pedestrians; the platform is a wheelchair in an office hallway, not a general outdoor crowd study. A wheeled robot reusing the method needs a reliable people tracker and its own validation of the cooperative-agent assumption.
## Code and data
Not recorded in the legacy extraction; not verified.
## Version family
Not recorded in the legacy extraction; not verified.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | strong | Sec. 5.2.3, p. 16 | "since there is no valid path if the humans are considered as static obstacles" |
| C3 | unset | n/a | | |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. 1, p. 2 | "Our approach assumes cooperative agents" |
## Page-cited excerpts
- **p. 16, Cooperative navigation in an office environment.** "since there is no valid path if the humans are considered as static obstacles"
  Dynamic pedestrians can block conventional planners unless cooperative interaction is modeled.
- **p. 17, Conclusion.** "A set of experiments with a real robot illustrates the applicability of our approach to socially compliant mobile robot navigation."
  Hardware evidence is an illustration on a wheelchair, not a statistical campaign.
- **p. 2, Introduction.** "Our approach assumes cooperative agents"
  The cooperative-agent assumption limits transfer to noncooperative crowds.
- **p. 2, Introduction.** "it would be necessary to introduce game-theoretic aspects"
  The authors' stated extension for evacuation-style settings.
## Survey-usable statements
### Supported
- As background, maximum-entropy IRL over homotopy-class mixtures models cooperative pedestrian avoidance and avoids the freezing of A* with constant-velocity predictions in simulation (light review; context paper).
### Not supported
- The method is validated in dense outdoor crowds: the real tests are office hallways with a wheelchair.
- The method handles noncooperative agents: the authors assume cooperative agents.
## Verification log
- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Full-text structured extraction, Claim summary) converted to the English template; C2 quote trimmed to the part found on the PDF page (the legacy sentence spans pp. 15-16 and continues past "obstacles"); the legacy C6 sentence kept as a plain excerpt and the claim row given the cooperative-agent sentence, which states a limit; known pedestrian goals, teleoperation teaching, and the wheelchair scope moved from limitations to Transfer conditions because they were not located as author limitations
- Legacy extraction: automated reviewer (codex), supplemental batch.
## Original abstract
Mobile robots are increasingly populating our human environments. To interact with humans in a socially compliant way, these robots need to understand and comply with mutually accepted rules. In this paper, we present a novel approach to model the cooperative navigation behavior of humans. We model their behavior in terms of a mixture distribution that captures both the discrete navigation decisions, such as going left or going right, as well as the natural variance of human trajectories. Our approach learns the model parameters of this distribution that match, in expectation, the observed behavior in terms of user-defined features. To compute the feature expectations over the resulting high-dimensional continuous distributions, we use Hamiltonian Markov chain Monte Carlo sampling. Furthermore, we rely on a Voronoi graph of the environment to efficiently explore the space of trajectories from the robot’s current position to its target position. Using the proposed model, our method is able to imitate the behavior of pedestrians or, alternatively, to replicate a specific behavior that was taught by tele-operation in the target environment of the robot. We implemented our approach on a real mobile robot and demonstrated that it is able to successfully navigate in an office environment in the presence of humans. An extensive set of experiments suggests that our technique outperforms state-of-the-art methods to model the behavior of pedestrians, which also makes it applicable to fields such as behavioral science or computer graphics.
