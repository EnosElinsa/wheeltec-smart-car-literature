# Targeted extraction-quality checks

All 482 pages passed the final page-count, marker, file-hash and image-reference checks. The mechanical screen initially flagged two formula-heavy appendix pages; they were inspected against rendered PDFs. These checks do not certify exact equation or numerical recognition.

| Paper / physical page | Trigger | Check and disposition |
|---|---|---|
| R04 / 13 | PDF-word overlap 0.5811 | Formula-heavy appendix B; prose, headings and equation groups 48-57f retained. Fragmented PDF math tokens differ from LaTeX. Coverage flag resolved by rendered-page inspection. |
| R04 / 14 | PDF-word overlap 0.4386 | Formula-heavy appendices C/D retained through the final continuation. Coverage flag resolved. Known recognition error: equation label 57i appears as 571. Consult PDF before using formulas. |
| R05 / 12 | Duplicate reading-order ID 22 | Pipeline kept first occurrence; final block IDs unique. Figures 9/10, Table IV and mapping discussion present against rendered page. |
| R11 / 1 | Text recognition reached token limit | Automatic retry with repetition penalty 1.1 completed; abstract, introduction and DOI retained, without final truncation warning. |
| R17 / 5 | Reading-order ID 43 omitted | Pipeline inserted formula block 43 / equation 27; final JSON and Markdown retain it once. Rendered page checked. |
| R24 / 12 | Reading-order ID 14 omitted | Pipeline inserted caption block 14, panel (a) T-bar; figure panels and text retained against rendered page. |
| R32 / 10 | Algorithm code block truncated | Re-extracted this page through OXR at 200 DPI and repetition penalty 1.1. No retry warning; numbered algorithm lines 1-51 retained, including final ApplyConfig, Wait and end while. Compared with rendered Algorithm 1. Original output and recovery receipts preserved privately. |

Five nonfatal pipeline warnings remain in the registered final receipts; the original R32 truncation warning belongs to the preserved superseded page. The final outputs have no unresolved truncation warning. Formula/notation and figure-caption recognition can still contain errors. No new review card, scientific conclusion or numerical manuscript claim was produced.
