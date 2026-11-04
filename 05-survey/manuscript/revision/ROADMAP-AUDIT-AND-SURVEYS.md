# Research roadmap, claim audit and related surveys - November 4, 2026

This record describes the state after this revision. [CONTRIBUTIONS-AUDIT-AND-REVIEW.md](CONTRIBUTIONS-AUDIT-AND-REVIEW.md) supersedes its Table IV, page-balance and style measurements.

This revision follows [EVIDENCE-MAP-AND-PROSE.md](EVIDENCE-MAP-AND-PROSE.md). It completes the remaining items of the content and prose plan: a research roadmap for Section X, condition-based guidance in the section syntheses, a tighter abstract, a check of critical characterizations against the sources, four additional related surveys, and acronym and terminology consistency. The selected corpus is unchanged at 229 works. The bibliography grows from 234 to 238 references, all from 2021-2026, because four related surveys join the background references.

## Section X and Table V

Table V (`tab:roadmap`) states, for each of the four open interfaces, the unresolved dependency, a matched comparison (what is held fixed and what is varied) and the decisive outcomes. The experiment-design paragraphs that previously followed each interface subsection were folded into the table. Each subsection now keeps the existing mechanisms, the open question and the prerequisites that a trial should violate. The six "Broader Challenges" subsections were merged into five. Transfer from simulation now sits with multifactor benchmarks, and continual learning sits with long-term maintenance. Every citation of the previous Section X is retained.

## Section syntheses and abstract

The syntheses of Sections IV-VIII now say when each response family applies, not only what it does:

- IV: selective updates when weak constraints remain, independent sensing when a modality fails, and relocalization or map revision for accumulated inconsistency.
- V: support and stability models for physical failure modes, and stated-risk constraints for moving obstacles.
- VI: candidate selection as the most conservative coupling.
- VII: asynchronous estimation for unpredictable links, and rendezvous for plannable connectivity.
- VIII: tolerant control, matched monitors and trustworthy local state as the respective conditions.

Each synthesis keeps its evidence statement from the evidence map.

The abstract fell from 243 to 228 words and from 9 to 10 sentences, with no sentence over 35 words. Its mean sentence length is 22.3 words, down from 26.4.

## Claim audit

The audit covered every sentence in Sections IV-X that carries a limiting marker (such as assumes, requires, only, without, offline, simulated, external, fails) and cites exactly one corpus work: 73 sentences at audit time. It also covered 65 limiting clauses that end in a single citation inside multi-citation sentences. Each claim was matched against its review card and its local full-text transcription. The 35 clauses without a strong match, and 25 sentences whose card did not state the limitation directly, were checked with targeted phrase searches. Five wordings were corrected (S13, E42, R10, M05, M32), and the remaining claims are supported by the card or the transcription. [claim-audit.json](claim-audit.json) lists the audited sentence claims in their current manuscript wording and each correction with its reason. Source excerpts used during the audit remain local and are not published.

The audit checks characterizations against the review evidence. It is not a re-reading of every paper. Claims in tables and in sentences that cite several works within one clause were not part of it.

## Related surveys

Four surveys were added to Table I and to the related-survey sentence of the Introduction. They are cited as background references, with identity and metadata verified from the opened Crossref DOI records stored in `background-sources/`. Their Table I scopes come from their abstracts.

| Key | Survey | Venue |
|---|---|---|
| `B_SubTSLAM2024` | Ebadi et al., Present and Future of SLAM in Extreme Environments: The DARPA SubT Challenge | IEEE T-RO 40, 2024 |
| `B_GlobalLiDARLoc2024` | Yin et al., A Survey on Global LiDAR Localization: Challenges, Advances and Open Problems | IJCV 132, 2024 |
| `B_SocialNav2023` | Mavrogiannis et al., Core Challenges of Social Robot Navigation: A Survey | ACM THRI 12, 2023 |
| `B_VLNSurvey2022` | Gu et al., Vision-and-Language Navigation: A Survey of Tasks, Methods, and Future Directions | ACL 2022 |

Table I now orders its eight surveys by the section they relate to (IV-VII). No survey on fault tolerance for wheeled robots from 2021-2026 in a peer-reviewed venue was found in this search.

## Terminology and acronyms

A scan of spelling variants (fallback, relocalization, closed-loop, real time, onboard, dataset, multi-robot, LiDAR) found consistent usage. Ten acronyms were used without a definition. GP, NDT, MPPI, LQR, VAE, ADMM, LPV, EKF and NMPC are now defined at first use, and "RL" in Section VIII is written out.

## Length and verification

The main paper stays at 24 pages, the T-IV maximum. The Section X restructuring offsets Table V and the four new Table I rows. The last page is balanced at 721 and 676 pt by `\IEEEtriggeratref{224}`. Little page slack remains.

Sentence rhythm (`rhythm.py`): 544 sentences, mean 21.4 words, 11% under 12 words and 6% over 35 words. `style_fingerprint.py` reports no flags. The house-style scan is clean.

`python scripts/verify_delivery.py` and `--sources` pass: 24 pages, 229 corpus citations in prose, 238 resolved references, 27 unique labels (Table V adds `tab:roadmap`), three figures, five tables, six unchanged equations, no unresolved references and no LaTeX warnings. The source mode checks 693 local artifacts with no hash mismatch.
