# Print Handy documentation

[Project overview](https://github.com/catduckgnaf/print-handy/blob/main/README.md) · [Contributing](https://github.com/catduckgnaf/print-handy/blob/main/CONTRIBUTING.md)

Find the task you came to do. Print Handy runs locally, with no Print Handy cloud. Chat providers carry messages and files you send; model downloads and optional hosted AI use the network too. Core print flows do not require an AI model endpoint.

## Start here

- [Docker](./docker.md): recommended install. Follow the quick start, configure a printer and chat platform, then check setup.
- [Standalone bot](./standalone.md): run without Docker. Choose [Discord](./discord-bot-setup.md), [Telegram](./telegram-bot-setup.md) or [Matrix](./matrix-bot-setup.md).
- [Hermes installation](./install.md): add Print Handy to an existing Hermes installation.
- [Web UI](./webui.md): optional local status, setup and settings interface. Set access before exposing it on a network.
- [Bambu A1 Docker walkthrough](./bambu-a1-docker.md): hardware-specific steps and verification limits.

## Everyday printing

- [Project reference](./project-reference.md): commands and everyday workflows.
- [Multi-part projects](./projects.md): upload several STL/3MF files together, trace project/plate JSON IDs and print the next plate.
- [Settings](./settings.md) · [YAML configuration](./configuration-yaml.md): settings, precedence and environment overrides.
- [Slicer warnings](./slicer-warnings.md): OrcaSlicer warnings after slicing.
- [Firmware updates](./firmware-update.md) · [Calibration](./calibration.md) · [Printer macros](./macros.md).
- [Design a part](./design.md): optional AI-assisted OpenSCAD design. Review the result before the usual approval flow.
- [Edit a prepared model](./editing.md): confirmed edit operations and limits. OrcaSlicer warning behavior is covered in [Slicer warnings](./slicer-warnings.md).
- [Printer profiles](./printer-profiles.md): supported delivery methods and verification limits.
- [More than one printer](./docker.md#more-than-one-printer): one instance serves a whole printer roster — declare every printer in one config file; the full roster reference is the [Printers list](./settings.md#printers-list). Running [separate instances](./multi-instance.md) stays available when you want hard process isolation.

## Printer guides

Start with [Printer support](./printer-support.md) for what support means, connection paths and the hardware checklist. A registered model or passing tests do not prove your physical printer has been verified.

- [ZMod](./zmod.md) · [Stock Flashforge](./flashforge-stock.md) · [AD5X best practices](./device-ad5x.md)
- [Bambu Lab](./bambu-lab.md) · [Bambu connectivity details](https://github.com/catduckgnaf/print-handy/blob/main/docs/BAMBU-CONNECTIVITY.md) · [Prusa](./prusa.md) · [Elegoo](./elegoo.md)
- [Creality](./creality.md) · [Qidi](./qidi.md) · [Sovol](./sovol.md)
- [Anycubic](./anycubic.md) · [Snapmaker](./snapmaker.md) · [OctoPrint and Marlin](./octoprint-marlin.md)
- [Device best practices](./device-best-practices.md) · [AD5X integration contract](./ad5x-contract.md)

## Troubleshooting

- [Home Assistant panic recovery](https://github.com/catduckgnaf/print-handy/blob/main/docs/home-assistant-panic.md) · [Troubleshooting by symptom](./troubleshooting.md) · [Guided setup and debugging](./guided-setup-debugging.md) · [Diagnostics](./diagnostics.md)
- [Intake limits](./intake-limits.md) · [Mesh audit](./mesh-audit.md)
- The `doctor` checks configuration and configured services. It may contact Moonraker or Spoolman; run it only where authorized. A clean check does not prove physical readiness.

## Advanced setup

- [Docker details](./docker.md): image pinning, storage, optional camera features, timelapses, upgrades and rollback.
- [Web UI details](./webui.md): access, settings behavior, optional controls and limitations.
- [Multi-instance setup](./multi-instance.md) · [Listeners](./listeners.md) · [Component provenance](./components.md)
- [Cloudflare examples](./cloudflare.md): optional hosted endpoints and network use. Examples are not proof of a live deployment.
- [Flash Studio](./flash-studio.md): optional user-installed slicer.
- [Geometry layout](./geometry-layout.md) · [CAD split plans](./cad-split-plans.md)

## Contributors and history

- [Contribution workflow](https://github.com/catduckgnaf/print-handy/blob/main/CONTRIBUTING.md) · [Pull request template](https://github.com/catduckgnaf/print-handy/blob/main/.github/PULL_REQUEST_TEMPLATE.md)
- [Branding guide](./branding.md) · [Release notes](https://github.com/catduckgnaf/print-handy/blob/main/docs/RELEASE-NOTES.md) · [Release checklist](./release-checklist.md) · [Release notes template](./release-notes-template.md) · [Internal release history](https://github.com/catduckgnaf/print-handy/blob/main/docs/INTERNAL_RELEASE_NOTES.md)
- [Rename migration](https://github.com/catduckgnaf/print-handy/blob/main/docs/RENAME-MIGRATION.md)
- Historical or internal records, not setup instructions: [Docker #117 acceptance](https://github.com/catduckgnaf/print-handy/blob/main/docs/DOCKER-117-ACCEPTANCE.md), [Docker #117 progress](https://github.com/catduckgnaf/print-handy/blob/main/docs/DOCKER-117-PROGRESS.md), [timelapse issue #126](https://github.com/catduckgnaf/print-handy/blob/main/docs/ISSUE-126-TIMELAPSE.md), [hardcoded values inventory](https://github.com/catduckgnaf/print-handy/blob/main/docs/hardcoded-inventory.md), [CAD evaluation](https://github.com/catduckgnaf/print-handy/blob/main/docs/KICAD-EVALUATION.md), [reuse map](https://github.com/catduckgnaf/print-handy/blob/main/docs/REUSE-MAP.md), [multi-printer design](https://github.com/catduckgnaf/print-handy/blob/main/docs/MULTI-PRINTER-DESIGN.md), [recovered testing lane](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/RECOVERY-TESTING.md).

These versioned `docs/` pages are the source of truth. Document features with the code and identify wiki impact in the [contribution checklist](https://github.com/catduckgnaf/print-handy/blob/main/CONTRIBUTING.md#automated-pr-review-support). Use documentation for the checked-out revision; draft work is not shipped capability.
