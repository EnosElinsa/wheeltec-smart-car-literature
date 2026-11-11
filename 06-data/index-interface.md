# Local reading interface

The local `INDEX.html` is generated from the same catalog as the public Markdown indexes. It is an offline HTML file with embedded data, styles and JavaScript; no CDN, web server or build runtime is required for reading.

The interface includes an inclusive year range, journal/conference family, publication type, theme, collection, assessment and reading-file filters. Search matches all entered words across title, ID, DOI, venue and scope notes. Sorting, pagination, empty states and a reset action apply to the same result set. Theme and venue option counts respect the other filters. Header totals describe the full catalog; result counts describe the current filters. Annual ICRA/IROS/RSS/CoRL editions are grouped into conference families.

The URL fragment stores filters and pagination for bookmarking. Press `/` outside a form field to focus search. Export results downloads the entire filtered result set as CSV, including rows beyond the visible page. Mobile layouts display paper cards. PDF, Markdown, native citation, review and publisher links appear only when recorded in the catalog. Assessment and derived-citation labels remain explicit. Venue names do not certify current journal rankings.

Run `python -m tools.build_indexes --strict` from the library root after catalog changes. The renderer is `tools/local_index.py`, its self-contained template is `tools/local_index.html`, and `tools/build_indexes.py` invokes it. Preserve the embedded JSON escaping and text-only DOM rendering when changing the interface. The generated local HTML remains excluded from the public repository; the generator and template are versioned.

Validation covered real Chromium interactions at desktop and mobile widths: inclusive year/venue combinations, exact matched IDs, totals, pagination, search, assessment, empty and reversed-year states, CSV row counts and bookmark restoration. Source-pair integrity and review status remain separate from interface validation. Current downloads follow [the acquisition policy](acquisition-policy.json) and [current work](current-work.md).
