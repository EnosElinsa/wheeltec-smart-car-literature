# VLM-Social-Nav: Socially Aware Robot Navigation Through Scoring Using Vision-Language Models
## Metadata
| Field | Value |
|---|---|
| ID | M07 |
| Title | VLM-Social-Nav: Socially Aware Robot Navigation Through Scoring Using Vision-Language Models |
| Authors | Daeun Song, Jing Liang, Amirreza Payandeh, Amir Hossain Raj, Xuesu Xiao, and Dinesh Manocha |
| Venue | IEEE Robotics and Automation Letters, vol. 10, no. 1, pp. 508-515 |
| Year | 2025 (online 2024) |
| Type | journal |
| DOI | [10.1109/lra.2024.3511409](https://doi.org/10.1109/lra.2024.3511409) |
| Official URL | https://ieeexplore.ieee.org/document/10777573/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2025-VLM-Social-Nav-M07/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2025-VLM-Social-Nav-M07/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2025-VLM-Social-Nav-M07/citation.bib) |
## Survey coding
- survey_module: semantic-language-navigation
- secondary_modules: traversability-planning-control
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware
- protocol_caveats: cloud-model, scripted-scenario
- platform_class: differential-drive
- platform: Turtlebot 2 (TurtleBot is differential-drive by the vocabulary definition) with Velodyne VLP-16, Zed 2i, and a laptop
- boundary_platform: no
- degradation: dynamic-objects
- degradation_observed: none
- evaluation_primary: closed-loop-task
- evaluation_all: closed-loop-task
- sensors: Zed 2i RGB camera; Velodyne VLP-16 LiDAR
- compute: laptop with Intel i7 CPU and RTX 2080 GPU; GPT-4V queries with 2-3 s average response time
- compute_location: mixed
- summary_result: Over four indoor social scenarios with 21 runs each, VLM-Social-Nav improves average success by at least 27.38% and average collision rate by 19.05% over DWA and behavior cloning.
- summary_limitation: The authors state that GPT-4V responses take 2-3 s, which can be problematic in more dynamic scenarios, and that robot experiments were conducted only indoors.
- survey_included: yes
- verification_level: light
## Problem
Socially compliant motion in human-centered indoor spaces is hard to encode with fixed rules or large demonstration datasets. Imitation-learning and reinforcement-learning social navigators need substantial data or reward engineering and generalize poorly. Geometric planners such as DWA avoid LiDAR obstacles but ignore etiquette such as yielding, keeping right, reacting to gestures, and doorway precedence.
## Mechanism
YOLO detects social entities (humans, doors, gestures) in RGB images. When a cue is present, GPT-4V is prompted with the image, the current action, and etiquette text, and returns a preferred heading and speed. This output becomes a social cost added to a DWA planner, which still uses LiDAR for collision geometry. The VLM is not queried every control cycle: formatted prompts with predefined choices and cue-gated queries bring GPT-4V response time to about 2-3 s. The authors use the VLM output as a cost term rather than as the sole action source, because VLMs still make mistakes.
## Baselines and controls
DWA without the social cost, and behavior cloning trained on SCAND. Other controls are not recorded in the legacy extraction; not verified.
## Platform and setup
All reported robot trials are real indoor tests on a Turtlebot 2 with a Velodyne VLP-16, a Zed 2i, and a laptop (Intel i7, RTX 2080). There are four scenarios (frontal approach, frontal approach with a stop gesture, intersection, narrow doorway), each with 21 runs per method. A user study with seven participants rates the behavior on a Likert scale. No physics-simulator campaign is reported; images from SCAND and MuSoHu appear only as prompting examples.
## Evidence type and transfer
The success and collision rates come from closed-loop runs on the real Turtlebot 2 in four staged indoor encounters. They do not cover outdoor sidewalks, crossings, or scenes with several groups of people. The social cost depends on a cloud-hosted GPT-4V.
## Sensors
Zed 2i RGB camera for YOLO and the VLM; Velodyne VLP-16 LiDAR for the DWA collision geometry.
## Compute and latency
A laptop with an Intel i7 CPU and an Nvidia RTX 2080 GPU runs the robot side; GPT-4V is a remote model. Average VLM response time is 2-3 s after prompt formatting and cue gating (p. 7). Planner cycle times are not recorded in the legacy extraction; not verified.
## Key quantitative results
- Success rate: VLM-Social-Nav reaches 100% in all four scenarios (Table I).
- Average success rate: at least 27.38% improvement, and average collision rate 19.05% improvement, over the compared methods in the four scenarios (p. 1).
- Results are averaged over 21 runs per method and scenario (p. 5, Table I).
- User study with seven participants: VLM-Social-Nav is rated most socially compliant (p. 6).
## Stated limitations
- Interpreting social rules and deriving actions from raw robot perception remains complex (p. 8).
- GPT-4V-class models need several seconds to respond; the 2-3 s average is sufficient for the tested interactions but can be problematic in more dynamic scenarios with frequent interactions (p. 7).
- VLMs can still make mistakes, so relying solely on them for navigation decisions is not safe (p. 7).
- Robot experiments were conducted only indoors; outdoor navigation and scenes with multiple groups, where simple left or right directions may not suffice, are future work (p. 7).
- Open-source VLMs such as LLaVA and visual prompting are named as next steps for hallucination detection and spatial reasoning (p. 8).
## Transfer conditions
The social cost needs a cloud VLM with connectivity and multi-second latency; the robot-side computer is a laptop with an RTX 2080. The LiDAR-based DWA remains the safety layer. Encounters were staged with one or two people in corridors and doorways. A wheeled robot reusing the method must budget for VLM latency at its own speed.
## Code and data
Not recorded in the legacy extraction; not verified.
## Version family
Not recorded in the legacy extraction; not verified.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | direct-support | moderate | Sec. V, p. 7 | "We propose a novel social navigation approach based on VLMs, focusing on real-time, socially compliant decisionmaking in human-centric environments." |
| C3 | direct-support | moderate | Sec. V, p. 8 | "However, interpreting social rules and deriving appropriate actions from them based on raw robot perception remains complex." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Discussion, p. 7 | "Although our robot experiments were conducted only indoors" |
## Page-cited excerpts
- **p. 7, Conclusion.** "We propose a novel social navigation approach based on VLMs, focusing on real-time, socially compliant decisionmaking in human-centric environments."
  Human-centric, socially constrained motion is the operating setting, not static obstacle avoidance.
- **p. 8, Conclusion.** "However, interpreting social rules and deriving appropriate actions from them based on raw robot perception remains complex."
  The residual problem is rule interpretation from perception; success gains are still reported.
- **p. 8, Conclusion.** "We demonstrate and evaluate our system in four different real-world social navigation scenarios with a Turtlebot robot."
  The evidence is real-robot, in four scenarios.
- **p. 7, Discussion.** "Although our robot experiments were conducted only indoors"
  The hardware scope is indoor only.
- **p. 7, Discussion.** "require several seconds to respond to prompts"
  VLM latency is the stated real-time constraint.
## Survey-usable statements
### Supported
- A GPT-4V social cost added to DWA on a Turtlebot 2 reached 100% success in four staged indoor social scenarios with 21 runs each (numbers from a light review; re-check before citing).
- VLM response time of 2-3 s was acceptable for the tested encounters, according to the authors.
### Not supported
- The method works in outdoor crowds: all robot experiments were indoors with staged encounters.
- The VLM alone can drive the robot safely: the authors state that relying solely on VLMs is not safe.
- The method runs fully onboard: it queries GPT-4V.
## Verification log
- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Claim summary, Hardware caveat) converted to the English template; C6 excerpt replaced by the p. 7 indoor-only sentence, because the legacy C6 sentence ("We demonstrate ...") reads as support rather than a limit and is kept as a plain excerpt; the abstract states "at least" 27.38%, which the review follows
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.
## Original abstract
We propose VLM-Social-Nav, a novel Vision-Language Model (VLM) based navigation approach to compute a robot’s motion in human-centered environments. Our goal is to make real-time decisions on robot actions that are socially compliant with human expectations. We utilize a perception model to detect important social entities and prompt a VLM to generate guidance for socially compliant robot behavior. VLM-Social-Nav uses a VLM-based scoring module that computes a cost term that ensures socially appropriate and effective robot actions generated by the underlying planner. Our overall approach reduces reliance on large training datasets and enhances adaptability in decision-making. In practice, it results in improved socially compliant navigation in human-shared environments. We demonstrate and evaluate our system in four different real-world social navigation scenarios with a Turtlebot robot. We observe at least 27.38% improvement in the average success rate and 19.05% improvement in the average collision rate in the four social navigation scenarios. Our user study score shows that VLM-Social-Nav generates the most socially compliant navigation behavior.
