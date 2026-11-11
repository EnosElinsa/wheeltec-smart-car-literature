# Deep reinforcement learning navigation with public author implementations

Eleven additional conference papers have official PDF/native-BibTeX pairs and OXR-1.0 transcriptions: seven ICRA, two IROS and two CoRL papers, published in 2023-2025. They were deduplicated against 615 catalog identities by DOI, official archive URL and title before selection. The pairs retain their publisher bytes. All 90 physical pages, per-page JSON and 90 referenced images passed artifact checks; the extraction services were stopped.

| Paper | Venue / year | Algorithm | Author implementation |
|---|---|---|---|
| [ARiADNE: A Reinforcement learning approach using Attention-based Deep Networks for Exploration](https://doi.org/10.1109/icra48891.2023.10160565) | ICRA 2023 | SAC; attention graph exploration | [D01](https://github.com/marmotlab/ARiADNE) |
| [Intention Aware Robot Crowd Navigation with Attention-Based Interaction Graph](https://doi.org/10.1109/icra48891.2023.10160660) | ICRA 2023 | PPO; recurrent interaction graph; trajectory prediction | [D02](https://github.com/Shuijing725/CrowdNav_Prediction_AttnGraph) |
| [Occlusion-Aware Crowd Navigation Using People as Sensors](https://doi.org/10.1109/icra48891.2023.10160715) | ICRA 2023 | PPO; variational occlusion inference | [D03](https://github.com/yejimun/PaS_CrowdNav) |
| [RLPP: A Residual Method for Zero-Shot Real-World Autonomous Racing on Scaled Platforms](https://doi.org/10.1109/icra55743.2025.11127278) | ICRA 2025 | SAC residual policy; Pure Pursuit | [D04](https://github.com/ForzaETH/f1tenth_gym/tree/paper/rlpp) |
| [Stranger Danger! Identifying and Avoiding Unpredictable Pedestrians in RL-based Social Robot Navigation](https://doi.org/10.1109/icra57147.2024.10610413) | ICRA 2024 | SARL; unpredictability features and rewards | [D05](https://github.com/sarapohland/stranger-danger) |
| [When to Replan? An Adaptive Replanning Strategy for Autonomous Navigation using Deep Reinforcement Learning](https://doi.org/10.1109/icra57147.2024.10611474) | ICRA 2024 | DQN; global replanning trigger | [D06](https://github.com/omron-sinicx/when2replan) |
| [MAexp: A Generic Platform for RL-based Multi-Agent Exploration](https://doi.org/10.1109/icra57147.2024.10611573) | ICRA 2024 | IPPO, MAPPO and other MARL baselines; continuous exploration | [D07](https://github.com/COAI-Lab/MAexp) |
| [NaviSTAR: Socially Aware Robot Navigation with Hybrid Spatio-Temporal Graph Transformer and Preference Learning](https://doi.org/10.1109/iros55552.2023.10341395) | IROS 2023 | SAC; preference rewards; spatio-temporal graph Transformer | [D08](https://github.com/SMARTlab-Purdue/SAN-NaviSTAR) |
| [Hyp2Nav: Hyperbolic Planning and Curiosity for Crowd Navigation](https://doi.org/10.1109/iros58592.2024.10801513) | IROS 2024 | Hyperbolic value network; tree search; curiosity rewards | [D09](https://github.com/GDam90/hyp2nav) |
| [Context-Aware Deep Reinforcement Learning for Autonomous Robotic Navigation in Unknown Area](https://proceedings.mlr.press/v229/liang23a.html) | CoRL 2023 | SAC; graph attention context; waypoint selection | [D10](https://github.com/marmotlab/Context_Aware_Navigation) |
| [FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](https://proceedings.mlr.press/v229/stachowicz23a.html) | CoRL 2023 | RLPD; visual initialization; autonomous real-world practice | [D11](https://github.com/kylestach/fastrlap-release) |

The catalog now contains 626 records and 455 active transcribed reading sets. The 247 existing assessments and 245 survey selections are unchanged; these eleven sources have no review cards. Their project descriptions appear in [textbook Chapter 54](https://enoselinsa.github.io/wheeltec-ros-textbook/08-advanced-applications/54-open-source-projects/#drl-projects), with exploration and multi-robot methods in the corresponding sections.

## Implementation scope

Pinned author repositories and source hashes are recorded in [code evidence](code-evidence.json). Training and evaluation entry points were inspected, not executed. Ten repositories have an MIT root license; no common root license was located for the ARiADNE training repository, so public source availability alone does not establish reuse permission. RLPP redirects to the author's F1TENTH Gym branch: checkpoints and testing are available, while dedicated training instructions remain unfinished. CrowdNav++ uses a separate GST project to train the pedestrian predictor. ROS versions, perception inputs and vehicle dynamics differ across projects; these sources do not establish deployment on the R680.

## Selection limits

This is a targeted selection, not exhaustive conference coverage. Discovery metadata and author pages nominated papers; the agent checked titles, abstracts, DRL mechanisms, ground-robot tasks and public implementation identity. Diffusion-only or imitation-only methods, aerial/manipulation-only tasks and repositories offering only a simulator without a verified navigation policy were not selected. T-RO DRL-VO and IJRR Bayesian Controller Fusion remain candidates for later acquisition because verifiable JCR edition/category evidence was incomplete; no new journal was acquired in this batch. RA-L, Autonomous Robots and Journal of Field Robotics remain excluded from new downloads under the [current policy](../acquisition-policy.json).

The [manifest](manifest.json) binds registered paths, hashes and fixed selections; original acquisition state, review packets, upstream README copies and rollback plans stay private. See [verification](verification.json). OCR is a reading aid; equations, tables and exact values should be checked in the PDF.
