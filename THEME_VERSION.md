# al-folio foundation

- Starter: [al-folio v1.2](https://github.com/alshedivat/al-folio/releases/tag/v1.2), released 2026-08-09.
- Commit: `b95d6d61a1b0663529094b1b5f4fbe8aa41f8a04`.
- Runtime: `al_folio_core` **1.0.15**, upgrade tooling: `al_folio_upgrade` **1.0.3** (the v1.2 release pins).
- Workflow: the release's [bootstrap skill](https://github.com/alshedivat/al-folio/blob/v1.2/.agents/skills/al-folio-bootstrap/SKILL.md), not the pre-v1 fork migration workflow. The source website was plain HTML.
- Read upstream `AGENTS.md`, `docs/BOUNDARIES.md`, `docs/ARCHITECTURE.md`, `docs/INSTALL.md`, and `docs/CUSTOMIZE.md` at that tag.
- All dependency resolutions are recorded in `Gemfile.lock`. Optional demo plugins are omitted in both `Gemfile` and `_config.yml`.
- `LICENSE` preserves the upstream MIT notice. The footer retains Jekyll / al-folio attribution.

Intentional local customization:

- `assets/css/main.scss`: the released Sass entry point, with one final `@use "site"` for additive typography, spacing, color, and responsive styles in `_sass/_site.scss`.
- `_layouts/bib.liquid`: a compact bibliography view to show full authors, descriptions, contributions, clear statuses, and text links from one BibTeX source. Optional preview fields support existing local research assets.
- `_includes/header.liquid`: the released header with the theme control moved outside the collapsed menu, using inline sun/moon SVGs so it remains visible on phones without an icon-font dependency.
- `assets/js/theme.js`: a small two-state theme runtime, using the core's `initTheme()` entry point and `data-theme` attributes. Defaults to dark, persists an explicit visitor choice, updates syntax-highlighting styles and the accessible button state, and handles unavailable local storage.
- `.al-folio-overrides.yml`: generated drift manifest for shadowed runtime files. Audit and review it when updating the theme gems.

The theme gem supplies the remaining layouts, navigation runtime, compiled utilities, and scripts. No Tailwind compiler or third-party JavaScript library is vendored in this repository.
