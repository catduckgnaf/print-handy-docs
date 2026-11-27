# Print Handy Documentation

The documentation site for [Print Handy](https://github.com/catduckgnaf/print-handy) — design parts with optional AI, prepare and manage 3D prints in the Web UI or chat, and approve each print before it starts. Local first, with no LLM needed for ordinary printing.

**Live site:** https://catduckgnaf.github.io/print-handy-docs/

This repository contains only the documentation site. It is not the Print Handy project itself.

Install via Docker, **Unraid Community Apps**, a [**Home Assistant OS app**](https://github.com/catduckgnaf/print-handy-haos-addon), or the native standalone bot. Native installation and the standalone bot are one path, not two products. The site highlights [model design](https://catduckgnaf.github.io/print-handy-docs/design), Pasta Wrapped, Pasta Cam, Spoolman-backed printer management and guarded beta firmware/component updates.

<!-- Local edits to README.md, BRANDING.md, docs/README.md, Docker and Web UI guides are editorial and intentionally not copied from an unreleased Print Handy ref. Pages navigation and homepage copy live only in this repository. -->

## Source of truth

The content in `docs/` is copied from [`catduckgnaf/print-handy/docs`](https://github.com/catduckgnaf/print-handy/tree/main/docs), which remains the source of truth. Guides that are internal or research-only in that repo are not published here; where a published guide links to one, the link points back to the file on GitHub.

See [catduckgnaf/print-handy#312](https://github.com/catduckgnaf/print-handy/issues/312) for the tracking issue.

Internal file names were lowercased for the site (for example `DISCORD-BOT-SETUP.md` became `discord-bot-setup.md`), and inter-document links were rewritten to site-internal routes or, for targets that are not published here, to absolute GitHub URLs in the Print Handy repo.

## Run locally

Requires Node.js 20 or newer.

```bash
npm ci
npm run docs:dev
```

Then open the local URL VitePress prints.

To produce the production build:

```bash
npm run docs:build
npm run docs:preview
```

## How updates work

Publishing is automatic. When a guide changes on Print Handy `main`, that
repo's `docs-main-dispatch` workflow sends a `print-handy-main`
`repository_dispatch` here, and **Docs auto-sync** (below) copies the
changed guides, verifies them, merges and deploys the site. A daily run and
the daily **Docs sync check** catch anything a dispatch missed.

The manual equivalent, if you ever need it:

1. Run the sync check (below) to see exactly which pages drifted.
2. Copy the changed user-facing guides from `print-handy/docs/` into `docs/` here, lowercasing file names.
3. Rewrite inter-document links the same way as the existing pages (site-internal for published pages, absolute GitHub URLs for anything else in the Print Handy repo).
4. Update the SHA-256 column for each re-synced page in `scripts/sync-manifest.tsv`.
5. Run `scripts/check-sync.sh` (must report no drift) and `npm run docs:build` (fix any dead links it reports).
6. Push to `main`. The Deploy workflow publishes the site to GitHub Pages.

## Keeping the site in sync

### Drift detection

`scripts/sync-manifest.tsv` is the comparison record: for each published
guide it lists the upstream file in `catduckgnaf/print-handy/docs`, the
site file here, and the SHA-256 of the upstream file at the last sync.
The site copies have rewritten file names and links, so the check hashes
the *upstream* files rather than diffing the copies.

- Locally: `scripts/check-sync.sh` — clones upstream `main` (or uses
  `PRINT_HANDY_DIR=/path/to/print-handy` if set), prints every
  CHANGED / ADDED / REMOVED page, then prints the wiki-check prompt.
  Exit 0 means no drift; exit 1 means drift.
- In CI: the **Docs sync check** workflow
  (`.github/workflows/docs-sync-check.yml`) runs the same script daily
  and on `workflow_dispatch`. The drift report goes to the workflow
  summary and an artifact. If there is drift it dispatches Docs auto-sync,
  which publishes the fix.

The version-specific `KLIPPER-014-AUDIT.md`, `OCTOPRINT-2.0.1-AUDIT.md`, and `OPENCREATOR-0.0.7.6-AUDIT.md` are maintainer source audits rather than operating guides. They remain available in the upstream repository with their hardware and version limitations; they are excluded from this user guide site.

Excluded upstream files (internal/research-only or retired walkthroughs, not published here) are
listed in `scripts/check-sync.sh`: `3MF-REMAP-INVENTORY.md` (an
implementation inventory, not a user guide), `BAMBU-CONNECTIVITY.md`,
`DOCKER-117-*.md`, `INTERNAL_RELEASE_NOTES.md`, `ISSUE-126-TIMELAPSE.md`,
`AD5X-WALKTHROUGH.md`, `BAMBU-A1-DOCKER.md`, `LIVE-DEMO.md`, `KICAD-EVALUATION.md`, `MULTI-PRINTER-DESIGN.md` (a design proposal for
unimplemented work; the site publishes shipped guides), `RELEASE-NOTES.md`,
`RENAME-MIGRATION.md`,
`REUSE-MAP.md`, `hardcoded-inventory.md`, `home-assistant-panic.md`
(and `material_temps.yaml`, which is not a guide).

### Auto-sync

The **Docs auto-sync** workflow (`.github/workflows/docs-auto-sync.yml`)
always syncs from upstream `main`. It runs on the `print-handy-main` and
`print-handy-release` dispatches, daily at 07:47 UTC, and by hand from the
Actions tab. Each run:

1. regenerates the site copies with `scripts/sync-docs.py` (no drift means
   a clean no-op);
2. verifies them with `scripts/check-sync.sh` and `npm run docs:build`;
3. opens a `docs-sync/` PR as a record, squash-merges it on that exact
   commit and dispatches the Pages deploy;
4. closes any open **Docs sync needed** issue.

Newly added or removed upstream guides stop the run before any site file
changes, because each one needs a manifest entry (publish or exclude). A
stopped or failed run opens or comments on a single **Docs sync needed**
issue with the run link. That is the only case that needs a human.

The release surfaces gate in Print Handy's `docker-publish` workflow fails
while this site has drift at the release ref; auto-sync clears it on its
own.

### The wiki check

The [Print Handy wiki](https://github.com/catduckgnaf/print-handy/wiki)
(Home, `_Sidebar`, Discord-Bot-Setup and any pages linked from them) is a
separate surface that points readers at these guides. After each
published sync, auto-sync lists the changed guides on one open
**Wiki check after docs sync** issue (label `wiki-check`). Tick the guides
off, update the wiki where needed and close the issue. The wiki check never
blocks publishing.

The site is built with [VitePress](https://vitepress.dev/), modelled on the [openevse documentation site](https://firstof9.github.io/openevse/).

## License

GNU Affero General Public License v3.0 only (AGPL-3.0-only) — see [LICENSE](LICENSE) and [NOTICE](NOTICE). This matches the Print Handy project.
