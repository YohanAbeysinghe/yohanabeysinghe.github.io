# Yohan Abeysinghe's academic website

An al-folio v1.2 site for **https://yohanabeysinghe.github.io/**. Runtime and navigation come from the pinned `al_folio_core` gem. See [THEME_VERSION.md](THEME_VERSION.md) for provenance and [the migration review](docs/MIGRATION.md) for sources, discrepancies, and verification.

## Run locally

Use Ruby **3.3.13** (`.ruby-version`) and Bundler. On this Mac, Ruby 3.3 was installed with Homebrew; the preview script selects it automatically.

```bash
# macOS, when Homebrew Ruby is needed:
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"

# Keep gems outside this checkout: its parent directory contains colons,
# which Bundler does not support in gem paths.
bundle config set --local path "$HOME/.cache/yohan-site/bundle"
bundle install
bash scripts/preview.sh
```

Open **http://127.0.0.1:4000/**. Jekyll watches content changes. Restart it after changing `_config.yml` or `_data` if a change is not reflected. Stop with Ctrl-C. The public VEGA project is hosted separately; its absolute links open the existing live project.

```bash
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/verify_site.py
bundle exec al-folio upgrade audit --no-fail
bundle exec al-folio upgrade overrides audit
```

Generated files live in ignored `_site/`; dependencies and caches are ignored. Node is only needed for the optional formatter: `npm ci`, then `npm run lint:prettier`. No npm build or Tailwind compilation is required.

## Update content

- **Homepage:** `_pages/about.md` contains the biography, Interests, and Contact sections. Keep the current-student wording independent of academic year. The displayed email and social icon links are derived from `_data/socials.yml`.
- **Internship notice:** edit `_data/availability.yml`; set `enabled: false` to hide it.
- **Social links:** `_data/socials.yml`. The Scholar ID is preserved from the original public site.
- **Publications:** add a verified record to `_bibliography/papers.bib`. Include full authors, title, year, official journal or proceedings, and a verified `paper` URL. `venue` is the short display label; `status` distinguishes a published work from a preprint. Use `summary` for a short description and `contribution` only when supported. Avoid placeholders for unreleased code.
- **Publication ordering:** `selected_order` controls the order within each year on Publications. The About page is a short biography and links to the full publication list rather than rendering a second bibliography.
- **Research figures:** the four papers use local figures in `images/publications/`; see `docs/publication-figures.md` for sources. Set `preview`, `preview_alt`, `preview_width`, and `preview_height` in the BibTeX entry. `abbr` supplies the venue badge. Images retain their original aspect ratios and open at a larger size when clicked.
- **Experience / education:** `_pages/experience.md`.
- **Honors:** `_data/honors.yml`, rendered on `_pages/honors.md`. Group entries under Mathematics, Physics, or Programming. Each competition year appears as a separate bullet, newest first, with the recorded host location where available. Medals, honorable mentions, rankings, and participation remain distinct.
- **Courses:** `_data/courses.yml`, rendered on `_pages/courses.md`, lists PhD coursework, current enrollment, and TA courses with instructors. Do not infer semesters or publish grades.
- **CV:** the navigation tab opens the PDF directly (`nav_cv_pdf: true` on `_pages/cv.md`). The download remains `/data/Yohan_Abeysinghe_CV.pdf`. Navigation and download links automatically append a content-based version using the theme's cache filter so browsers fetch a fresh PDF when it changes. Replace that file deliberately with the intended public version to retain existing links. `src/` is private, ignored, and explicitly excluded from Jekyll; never copy it into public assets automatically.

Custom styling is additive in `_sass/_site.scss`. `_layouts/bib.liquid` is a compact, intentional view override. The rest of the theme comes from gems. After a gem update, inspect override drift, rebuild, and review before accepting new checksums:

```bash
bundle exec al-folio upgrade overrides audit
bundle exec al-folio upgrade overrides diff _layouts/bib.liquid
bundle exec al-folio upgrade overrides diff assets/css/main.scss
```

Dark mode is enabled by default. The sun/moon button at the top right switches between dark and light, including when the mobile menu is closed, and remembers the visitor's choice. `enable_darkmode` in `_config.yml` controls whether the switch is enabled. The two-state preference behavior is a small local override in `assets/js/theme.js`; `_includes/header.liquid` keeps the control outside the collapsed menu and uses inline SVG icons. Both palettes are defined with CSS variables in `_sass/_site.scss`. These overrides are tracked in `.al-folio-overrides.yml` alongside the bibliography and Sass entry point.

## Publishing updates

The user has approved publishing this migration. The source is maintained in the existing repository, and `master` is the production branch. Push future work to a branch and open a pull request to **master**. The pull-request job builds and checks the site without deploying. Pushes to `migration/al-folio` also run a build for migration verification; deployment is restricted to `master`.

The repository's **Settings → Pages → Build and deployment → Source** is set to **GitHub Actions**. Keep the `github-pages` environment restricted to `master`. Merge a reviewed pull request to publish. `.github/workflows/pages.yml` builds with the locked gems and uploads only `_site/`; the deployment job has `pages: write` and `id-token: write`. No default GitHub Pages Jekyll build or credentials for third-party services are required. The workflow can also be dispatched on `master`.

Check the latest **Build and publish academic site** run in Actions to verify publication. Failed **pages build and deployment** runs from before the source change are historical legacy builds; they do not describe the current deployment.

The user-site configuration is `url: https://yohanabeysinghe.github.io` and `baseurl: ""`. Keep the repository identity and origin unchanged. Leave the separate `YohanAbeysinghe/vega_website` repository and its Pages settings intact.

## Revert

Before publishing, retain the migration branch and switch to `master` only after committing or stashing your work. The original site is in Git at **4a4ee47**; there is no backup inside the published site.

After publication, revert migration commit `2feca57` through a new pull request rather than rewriting history. Restoring the old plain HTML also restores its old workflow state, so restore the previous Pages publishing source (the `master` branch, root directory) or add a static-artifact workflow for that old HTML. Keep the current `.gitignore` user change and the separate VEGA project untouched.

The footer is fixed to the bottom edge, with muted theme-aware credits and no copyright sentence. Edit `footer_text` in `_config.yml` for its wording; `_includes/footer.liquid` renders the credits and `_sass/_site.scss` reserves space beneath the content.

The browser tab icon is `assets/img/favicon.svg`, a minimal teal “YA” monogram on a white rounded square. The initials use vector paths in the site's light-mode accent color (`#006e83`). `_config.yml` selects it through `icon: favicon.svg`; the theme automatically versions the asset URL when its contents change.
