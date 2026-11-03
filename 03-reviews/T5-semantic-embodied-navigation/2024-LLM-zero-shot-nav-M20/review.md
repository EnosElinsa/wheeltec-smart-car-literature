# Can an Embodied Agent Find Your “Cat-shaped Mug”? LLM-Based Zero-Shot Object Navigation
## Metadata
| Field | Value |
|---|---|
| ID | M20 |
| Title | Can an Embodied Agent Find Your “Cat-shaped Mug”? LLM-Based Zero-Shot Object Navigation |
| Authors | Vishnu Sashank Dorbala, James F. Mullen, and Dinesh Manocha |
| Venue | IEEE Robotics and Automation Letters, vol. 9, no. 5, pp. 4083-4090 |
| Year | 2024 (online 2023) |
| Type | journal |
| DOI | [10.1109/lra.2023.3346800](https://doi.org/10.1109/lra.2023.3346800) |
| Official URL | https://ieeexplore.ieee.org/document/10373065/ |
| Theme folder | T5-semantic-embodied-navigation |
| Batch | baseline-2026-09-18 |
| Local files | `01-papers/T5-semantic-embodied-navigation/2024-LLM-zero-shot-nav-M20/paper.pdf` and `02-fulltext/T5-semantic-embodied-navigation/2024-LLM-zero-shot-nav-M20/paper.md` (local only, not in the public repository); [BibTeX](../../../01-papers/T5-semantic-embodied-navigation/2024-LLM-zero-shot-nav-M20/citation.bib) |
## Survey coding
- survey_module: semantic-language-navigation
- secondary_modules: none
- evidence_type: closed-loop-hardware
- evidence_all: closed-loop-hardware, simulation
- protocol_caveats: cloud-model
- platform_class: differential-drive
- platform: TurtleBot 2 (TurtleBot is differential-drive by the vocabulary definition); RoboTHOR agent in simulation
- boundary_platform: no
- degradation: none
- degradation_observed: model-error
- evaluation_primary: closed-loop-task
- evaluation_all: residual, closed-loop-task
- sensors: RGB-D camera (model not named); depth costmap via RTAB-Map and costmap_2d
- compute: not reported; GPT-3 queried through prompts
- compute_location: mixed
- summary_result: On a real TurtleBot 2, LGX reaches 54.2% success versus 27.8% for GLIP-on-Wheels and 6.9% for random exploration; on RoboTHOR, 35.0% versus 27.5% for OWL-CoW.
- summary_limitation: The authors state that failure cases remain, especially when the LLM incorrectly localizes the target object, and that SR and SPL are weakly informative for zero-shot navigation.
- survey_included: yes
- verification_level: light
## Problem
Language-driven zero-shot object-goal navigation (L-ZSON) asks an agent to find a uniquely described object in an unseen environment without task-specific training. Supervised object navigation does not cover free-form labels, and simulators such as RoboTHOR and Habitat mostly contain common class names ("mug") rather than descriptions such as "cat-shaped mug". The paper treats real homes with free-form language and partial observability as a necessary evaluation.
## Mechanism
Language-guided exploration (LGX):
1. The robot rotates 360° and collects RGB and depth.
2. Depth is turned into a 2D costmap with RTAB-Map and ROS `costmap_2d`.
3. RGB is turned into a YOLO object list or BLIP captions, which are prompted into GPT-3; GPT-3 picks a sub-goal object or a cardinal direction. Invalid LLM replies fall back to a random direction.
4. In parallel, GLIP grounds the free-form target; when its confidence reaches the threshold G_th (0.85 on RoboTHOR), the robot stops and goes to the box.
The best simulated variant is YOLO to GPT-3 with GLIP. Seven prompt templates are compared (perspective, order of the object set, "ONE word").
## Baselines and controls
OWL-CoW and CoW on RoboTHOR; GLIP-on-Wheels (frontier-based exploration with GLIP and no LLM) in simulation and on the robot; random exploration with GLIP on the robot; BLIP-caption prompts versus object-list prompts; seven prompt templates.
## Platform and setup
- Simulation: RoboTHOR validation, 1800 episodes in 15 scenes with 12 classes; n_r = 5 and an exploration distance of 5 m.
- Real robot: TurtleBot 2 with a two-phase room-hallway-room protocol and unique household objects (Table II).
## Evidence type and transfer
The success rates come from RoboTHOR and from closed-loop runs of the real TurtleBot 2. The real protocol covers two rooms and a hallway, not long-horizon search of a whole home. Exploration decisions come from the cloud model GPT-3.
## Sensors
RGB and depth camera (model not named); the depth stream feeds RTAB-Map and `costmap_2d`.
## Compute and latency
Not recorded in the legacy extraction; not verified. GPT-3 is used through prompts, not as an onboard model.
## Key quantitative results
- RoboTHOR SR/SPL: LGX (YOLO to LLM with GLIP) 35.0%/21.9% versus OWL-CoW 27.5%/17.2% and CoW 15.2%/9.7%.
- RoboTHOR: GLIP-on-Wheels (frontier exploration with GLIP, no LLM) 33.2%/20.3%.
- BLIP prompts underperform object-list prompts, and putting "ONE word" first lowers PSR and SR.
- Real TurtleBot 2 success: LGX 54.2% versus GLIP-on-Wheels 27.8% and random with GLIP 6.9% (p. 7).
- Real Phase-2 failure (wrong room): 20.8% of runs (p. 7).
- GLIP on the robot: 87.5% true positives when the object is visible and 8.3% false positives when it is absent (p. 7, Fig. 6).
## Stated limitations
- The method still has failure cases, especially when the LLM incorrectly localizes the target object (p. 8).
- SR and SPL should be improved to be more informative for zero-shot navigation tasks (p. 8).
- When the LLM gives no valid response, the agent moves in a random direction (p. 4).
- RoboTHOR provides a skewed basis for context-dependent exploration: SR barely changes despite large changes in PSR (p. 7).
## Transfer conditions
Legacy reviewer observations: GLIP false negatives and false positives reduce real-world success, and some unique objects (for example "stevia sugar packets") were never localized; robot-perspective prompts more often answer "no" or "nothing" (not located as author limitations). GPT-3 is queried offboard. A wheeled robot reusing LGX needs connectivity to the language model and an RGB-D costmap stack.
## Code and data
Not recorded in the legacy extraction; not verified.
## Version family
Not recorded in the legacy extraction; not verified.
## Claim relations
| Claim | Relation | Strength | Location | Excerpt |
|---|---|---|---|---|
| C1 | unset | n/a | | |
| C2 | unset | n/a | | |
| C3 | direct-support | moderate | Sec. VI, p. 8 | "Our method still includes a number of failure cases, especially when the LLM incorrectly localizes the target object." |
| C4 | unset | n/a | | |
| C5 | unset | n/a | | |
| C6 | qualifies | moderate | Sec. V-A, p. 5 | "We conduct experiments with a Turtle-Bot 2 to validate two facets of LGX in the real world" |
## Page-cited excerpts
- **p. 8, Limitations, conclusions, and future work.** "Our method still includes a number of failure cases, especially when the LLM incorrectly localizes the target object."
  LLM error is a first-class failure mode.
- **p. 5, Experiment setup.** "We conduct experiments with a Turtle-Bot 2 to validate two facets of LGX in the real world"
  The real-robot study validates exploration and grounding, in a two-phase room and hallway protocol.
- **p. 7, Real-world results.** "The success case occurs 54.2% of the time"
  The real success rate.
- **p. 7, Real-world results.** "When the goal object was present in the scene, GLIP accurately detected it 87.5% of the time."
  Grounding errors remain when the object is visible.
- **p. 4, Prompting.** "Should the LLM not provide us with a valid response, the agent moves in a random direction."
  Invalid LLM outputs fall back to random motion.
## Survey-usable statements
### Supported
- GPT-3-guided exploration with GLIP grounding reached 54.2% success on a real TurtleBot 2 for uniquely described objects, versus 27.8% for GLIP-on-Wheels (numbers from a light review; re-check before citing).
- LLM mislocalization of the target is the authors' main named failure mode.
### Not supported
- LGX runs onboard without connectivity: it prompts GPT-3.
- LGX is validated on long-horizon search of whole homes: the real protocol is two rooms and a hallway.
## Verification log
- 2026-11-02 | host: Kiro | scope: light conversion of the legacy extraction; metadata, abstract, and excerpts checked mechanically; numbers not re-verified | corrections: free-form card (Validation, Tags, Claim summary, Hardware caveat) converted to the English template; C6 quote trimmed to the part found in the text; the GLIP false-detection and robot-perspective prompt notes, and the offboard-GPT-3 note, moved from limitations to Transfer conditions because they were not located as author statements
- Legacy extraction: automated reviewer (codex), baseline batch 2026-09-18.
## Original abstract
We present language-guided exploration (LGX), a novel algorithm for Language-Driven Zero-Shot Object Goal Navigation (L-ZSON), where an embodied agent navigates to an uniquely described target object in a previously unseen environment. Our approach makes use of large language models (LLMs) for this task by leveraging the LLM’s commonsense-reasoning capabilities for making sequential navigational decisions. Simultaneously, we perform generalized target object detection using a pre-trained Vision-Language grounding model. We achieve state-of-the-art zero-shot object navigation results on RoboTHOR with a success rate (SR) improvement of over 27% over the current baseline of the OWL-ViT CLIP on Wheels (OWL CoW). Furthermore, we study the usage of LLMs for robot navigation and present an analysis of various prompting strategies affecting the model output. Finally, we showcase the benefits of our approach via real-world experiments that indicate the superior performance of LGX in detecting and navigating to visually unique objects.
