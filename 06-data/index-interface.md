# Paper and open-source project interface

The [online catalog](https://enoselinsa.github.io/wheeltec-smart-car-literature/) and versioned `INDEX.html` share a Chinese interface with separate paper and project tabs. The paper tab is generated from admitted papers in the shared catalog (`main` and `surveys`). Excluded/background identities and pending acquisition records stay in the administrative CSV and do not inflate the displayed paper count. Styles, scripts and data are embedded; no server, CDN, textbook checkout or network request is required to browse. GitHub's file view does not execute HTML; use the online catalog or [OPEN_SOURCE_PROJECTS.md](../OPEN_SOURCE_PROJECTS.md) for a readable GitHub directory.

The page uses a compact catalog layout: paper and project tabs, a left sidebar for classification, and a searchable list on the right. Tab and sidebar counts describe the full collection, independently of list filters; the list heading shows the matched count. Annual ICRA/IROS/RSS/CoRL editions are grouped into conference families. The year chart shows the latest six bibliographic years with nonempty earlier years grouped into an earlier bin. Selecting a chart bar, source or research direction opens its matching papers with a fresh filter state. Source tabs separate journals and conferences; expanding the source list reveals every nonempty source. Venue counts describe holdings, not journal rankings.

The paper list supports inclusive start/end years, research direction, publication type and publication source. Filter options and their counts respect the other filters; zero-count alternatives are omitted. An applied filter that becomes empty remains selected without a zero-count option, and its removable chip permits recovery. Search matches all words across titles, identifiers, DOI, full and short venue names, research directions and scope notes. Sorting, pagination, result totals and CSV export use exactly the same matched set. CSV export includes all matches, not just the visible page, with Chinese column labels and UTF-8 BOM for spreadsheet use.

The interface uses plain-language labels, a restrained white/gray palette, blue text links and consistent sans-serif typography. Classification rows and thin dividers replace decorative cards, icons and oversized statistics. Paper titles, venue names and years are prominent; internal identifiers, source notes and derived-citation notices are in expandable paper details. PDF, full text, citation, publisher and reading-note links appear only when recorded and use a new tab. On mobile, the sidebar becomes a compact classification area and paper rows stack with thin separators. The URL fragment stores list filters and pagination for bookmarking; `/` focuses search outside form fields. Reduced-motion preferences and keyboard focus are supported. No journal quartile or implementation availability is inferred from venue names.

Counts appear next to tabs, classification items and result headings, without standalone statistics blocks or enlarged figures. DRL is a normal method filter. Do not add explanatory subtitles, reading-availability claims, association totals, category totals, repository-check dates, a global R680 hardware block or instructions describing obvious controls. Year bars carry their own labels. Repository verification dates and year-selection rules belong in this maintenance guide and the source data. Result summaries show only the visible item range.

Run `python -m tools.build_indexes --strict` after catalog changes. The renderer is `tools/local_index.py`, its template is `tools/local_index.html`, and `tools/build_indexes.py` invokes it. The Chinese UI files, localized project JSON and registered verbatim full texts have scoped language exceptions in the public-tree checker; source-file, credential and absolute-path checks remain enforced. Public research prose and documentation stay English. Preserve JSON escaping and text-only rendering of catalog data. The generated HTML, its generator and template are versioned. PDF, full-text Markdown and image payloads are delivered through Git LFS; clone with LFS and run `git lfs pull` before opening the page.

Validate data totals against the catalog, positive filter options, combined year/source selections, exact matched identifiers, chart navigation, bookmark restoration, sorting, pagination, empty states, CSV export, keyboard access and responsive layouts in a real browser. Interface checks do not change source bytes, assessments or survey membership.

## Open-source projects

The project tab contains 66 implementations and tools in six application areas, including 17 projects with DRL methods. It links 52 distinct publications to local reading files. Project and paper counts are separate: a project can cite several papers, and several projects can cite the same paper. Tools without an associated paper have no invented publication metadata.

Search covers project names, algorithms, inputs and outputs, runtime notes, adaptation limits and publication titles. Direction, method, environment and publication-year filters can be combined. Facet options show positive project counts under the remaining filters. Method tags overlap and their counts must not be added together. Publication-year filtering uses the linked catalog's bibliographic year where available, otherwise the cited year. Projects with no known publication year do not match a selected year. Sorting, pagination and UTF-8 CSV export use all matched projects.

Rows show purpose, method, input/output, runtime, code and README links. Expand a row for its full explanation, specific vehicle requirements under usage conditions, publications, existing PDF/full-text/citation links and additional implementation resources. The comparison table retains these vehicle requirements. A paper entry also links back to its project details. Unspecified licenses are omitted. Runtime tags identify an implementation or a linked integration; the adaptation text identifies specific ROS versions and portability limits. A ROS 2 tag does not establish Humble compatibility or demonstrated R680 deployment. Diffusion policies and self-supervised representations remain separate from DRL. CASH's description identifies both the QMIX/MAPPO and DAgger options.

Select up to four projects for comparison of algorithms, observations, outputs, runtime, R680 requirements and papers. Selection survives filtering and pagination, and can be bookmarked. At four selected projects, unselected checkboxes are disabled until one is removed. Comparison and list filters are cleared separately. Both tabs support keyboard navigation and `/` for the active search. URL fragments store the active tab, filters, page and comparison. The comparison region has its own horizontal scroll on small screens.

## Project data and maintenance

| File | Purpose |
|---|---|
| [open-source-projects.json](open-source-projects.json) | Maintained project descriptions, facets, publication identities and dated public GitHub metadata |
| `tools/project_catalog.py` | Schema checks, exact publication association checks and portable Markdown generation |
| `tools/project_index.css` / `tools/project_index.js` | Project styles, filters, comparison and navigation, embedded into generated HTML |
| `OPEN_SOURCE_PROJECTS.md` | Generated portable directory for GitHub and offline Markdown reading |

The project descriptions were adapted from [textbook chapter 54](https://enoselinsa.github.io/wheeltec-ros-textbook/08-advanced-applications/54-open-source-projects/). The JSON records its repository, revision, path and per-project anchors. All 66 repository links and READMEs were checked on November 12, 2026. A dated repository check does not establish continuing maintenance. The directory includes historical and infrastructure projects; journal-acquisition Q1 requirements do not reclassify their associated publications or trigger downloads.

Edit the JSON, verify claims against the README and paper, then run `python -m tools.build_indexes --strict`. Resolve `paper_codes` by exact DOI or official publication URL; the generator rejects missing, excluded or unrelated associations. Do not associate papers by approximate title. Regeneration updates the HTML and portable directory together, without requiring a sibling checkout or network access. Third-party code retains its own license. Keep paper source bytes, assessment status and survey membership unchanged.

Browser validation should cover combined project filters, empty states, exact paper/project links in both directions, bookmark reload, comparison limits and removal, CSV row counts, pagination, keyboard access, desktop/mobile layouts and console errors. Unit tests cover unsafe URLs, invalid facets, duplicate projects, publication identity errors and safe standalone JSON embedding.

## GitHub Pages

[Deploy Pages](../.github/workflows/pages.yml) builds and deploys the site on every push to `main`, with a manual dispatch option. Pages uses the GitHub Actions build type. The deployment environment is `github-pages`; concurrent releases are serialized.

The builder `tools/build_site.py` reads the committed `INDEX.html` and produces a separate, ignored `_site/` artifact with `index.html` and an identical `INDEX.html` alias. The offline interface and catalog are unchanged. Both views, comparison, bookmarks and CSV export use the deployed resource URLs. Documentation and review links point to GitHub at the deployed commit. PDF and figure links point to the existing Git LFS media at the same commit.

Only canonical full-text Markdown is fetched through LFS during deployment. Its size and SHA-256 must match the reading-asset manifest before rendering. Full texts become static HTML pages under `fulltext/`, and the original citation bytes are copied under `citations/`. The Markdown renderer permits tables and code blocks, strips unsafe HTML and rewrites relative figure links to LFS media. Mathematical expressions are preserved and typeset with MathJax 3.2.2 from jsDelivr; wide expressions scroll within the text column. PDF and figure payloads are not duplicated into the Pages artifact. Source transcriptions and original PDFs retain their existing status and bytes.

Install `requirements-pages.txt` to build or test the site tools. For a local preview, use a new or empty output directory:

```shell
git lfs pull --include="02-fulltext/**/paper.md" --exclude=""
python -m tools.build_site --out _site --revision <full-commit-sha>
python -m http.server 8080 --directory _site
```

Before announcing a deployment, verify the live URL, both catalog tabs, combined filters, project comparison, a full-text page and figure, a PDF payload and an exact-byte citation download.
