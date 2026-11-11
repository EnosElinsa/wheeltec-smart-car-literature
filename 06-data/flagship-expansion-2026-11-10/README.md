# Flagship robotics expansion

Historical acquisition snapshot. Later manual completion and OXR extraction resolved all but H05; use [current work](../current-work.md) for present actions. Original selection and delivery counts below remain historical evidence.

Sixty additional works were screened against titles and abstracts, deduplicated against all 534 baseline catalog records, and frozen for acquisition on November 11, 2026. The batch excludes IEEE Robotics and Automation Letters and all venues outside T-RO, IJRR, Science Robotics, ICRA, IROS, RSS and CoRL. The directory date retains the batch's original discovery label.

46 official PDF/raw-BibTeX pairs are registered in the shared six-theme layout. 14 selections remain unresolved; their reserved H-series IDs are retained in [selection.csv](selection.csv) and the [manifest](manifest.json). Acquisition does not create transcriptions, review cards, evidence coding or survey membership.

| Venue | Selected | Delivered pairs |
|---|---:|---:|
| IEEE Transactions on Robotics | 25 | 25 |
| IEEE International Conference on Robotics and Automation | 10 | 10 |
| IEEE/RSJ International Conference on Intelligent Robots and Systems | 10 | 10 |
| Conference on Robot Learning | 6 | 1 |
| Robotics: Science and Systems | 5 | 0 |
| The International Journal of Robotics Research | 3 | 0 |
| Science Robotics | 1 | 0 |

Native BibTeX bytes are unchanged. The manifest records official URLs and source hashes; the original delivery state, institution/browser state, selection files, import plans and rollback backups stay private. The catalog and local reading view expose each delivered PDF and citation. Missing transcriptions are represented by empty Markdown paths.

RSS, SAGE and AAAS selections require official manual downloads because the installed acquisition runtime has no adapter. Five CoRL 2025 pages point to the venue's GitHub archive rather than the path accepted by the PMLR adapter; these remain explicit contract errors and were not silently substituted. The successful CoRL 2023 pair uses the existing PMLR contract. A local manual-download checklist contains links and reserved filenames for the nine manual selections.

Coverage is partial: OpenAlex has not indexed IROS 2026, the CoRL 2024 directory parser failed, and CoRL 2026 proceedings were unavailable. The selection is purposive and does not claim exhaustive venue coverage.

See [venue assessment](venue-assessment.md) for the baseline venue mix and the limits of venue-level judgments. Each delivered paper retains a title/abstract screening rationale in the manifest; hardware or full-paper quality claims require later assessment.

## Starting points for the WHEELTEC project

These priorities follow title/abstract relevance, not full-paper assessment. H15 (CPBA-LIWO) and H08 (Semantic-LiDAR-Inertial-Wheel fusion) directly match wheel/IMU/LiDAR localization. H12 (FineNav) addresses wheeled navigation with a modular mapping stack. H40 (TOPP-DWR) treats differential-drive speed and angular constraints. H34 addresses fault-tolerant cooperative localization, and H20 (MobileROS) addresses wireless reliability in ROS deployments. H43 (FAST-LIVO2), H48 (NeuPAN), H53 (BEVPlace++) and H57 (OKVIS2-X) provide additional localization, navigation and mapping references; their platform assumptions must be checked before implementation.
