# Print Handy documentation

[Project overview](https://github.com/catduckgnaf/print-handy/blob/main/README.md) · [Contributing](https://github.com/catduckgnaf/print-handy/blob/main/CONTRIBUTING.md)

Pick your problem. Print Handy runs on your hardware with no cloud of its own (your chat app still carries what you send through it), and the core flows need no AI at all.

## Start here

- [Docker](./docker.md): the recommended install, with a copy-paste quickstart from nothing to a first print.
- [Standalone bot](./standalone.md): run without Docker. Choose [Discord](./discord-bot-setup.md), [Telegram](./telegram-bot-setup.md) or [Matrix](./matrix-bot-setup.md).
- [Native installation](./install.md): install Print Handy without Docker (Python + systemd).
- [Web UI](./webui.md): local status, setup and settings interface, on by default. It serves openly on your network until you set a login in its walkthrough.
- [Live demo](https://github.com/catduckgnaf/print-handy/blob/main/docs/LIVE-DEMO.md): static, simulated Discord-style chat demo in the browser. No install, no account, nothing prints.
- [Bambu A1 Docker walkthrough](https://github.com/catduckgnaf/print-handy/blob/main/docs/BAMBU-A1-DOCKER.md): hardware-specific steps and verification limits.

## Everyday printing

- [Project reference](./project-reference.md): commands and everyday workflows.
- [Multi-part projects](./projects.md): upload several STL/3MF files together, trace project/plate JSON IDs and print the next plate.
- [Settings](./settings.md) · [YAML configuration](./configuration-yaml.md): settings, precedence and environment overrides.
- [Slicer warnings](./slicer-warnings.md): OrcaSlicer warnings after slicing.
- [Firmware updates](./firmware-update.md) · [Calibration](./calibration.md) · [Printer macros](./macros.md).
- [Design a part](./design.md): optional AI-assisted OpenSCAD design. Review the result before the usual approval flow.
- [Edit a prepared model](./editing.md): confirmed edit operations and limits. OrcaSlicer warning behavior is covered in [Slicer warnings](./slicer-warnings.md).
- [Printer profiles](./printer-profiles.md): supported delivery methods and verification limits.
- [Status voice](./status-voice.md): the local, no-AI sarcastic quips on intake progress, the copy-count Easter eggs, and how roasts rotate.
- [Printer accessories](./accessories.md): hardware fitted to one printer that did not ship with its model, including the Bondtech INDX tool changer for Klipper printers.
- [More than one printer](./docker.md#more-than-one-printer): one instance serves a whole printer roster, declare every printer in one config file; the full roster reference is the [Printers list](./settings.md#printers-list). Running [separate instances](./multi-instance.md) stays available when you want hard process isolation.

## Printer guides

Start with [Printer support](./printer-support.md) for what support means, connection paths and the hardware checklist. A registered model or passing tests do not prove your physical printer has been verified.

- [ZMod](./zmod.md) · [Stock Flashforge](./flashforge-stock.md) · [AD5X best practices](./device-ad5x.md)
- [Bambu Lab](./bambu-lab.md) · [Bambu connectivity details](https://github.com/catduckgnaf/print-handy/blob/main/docs/BAMBU-CONNECTIVITY.md) · [Prusa](./prusa.md) · [Elegoo](./elegoo.md)
- [Creality](./creality.md) · [Qidi](./qidi.md) · [Sovol](./sovol.md)
- [Anycubic](./anycubic.md) · [Snapmaker](./snapmaker.md) · [OctoPrint and Marlin](./octoprint-marlin.md)
- [Device best practices](./device-best-practices.md)

## Troubleshooting

- Stuck and want a person? Ask in the [Print Handy Discord server](https://discord.gg/mT2Ht3nqZu), in the #support channel, or file an [issue](https://github.com/catduckgnaf/print-handy/issues) when it is a bug that needs tracking.
- [Home Assistant stop button and panic recovery](https://github.com/catduckgnaf/print-handy/blob/main/docs/home-assistant-panic.md) · [Troubleshooting by symptom](./troubleshooting.md) · [Guided setup and debugging](./guided-setup-debugging.md) · [Diagnostics](./diagnostics.md)
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
- [Branding guide](./branding.md) · [Release notes guide](./release-notes-guide.md) · [Release checklist](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/RELEASE-CHECKLIST.md) · [Release notes template](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/RELEASE-NOTES-TEMPLATE.md) · [Internal release history](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/INTERNAL_RELEASE_NOTES.md)
- Historical and internal records, not setup instructions, live in [`history/`](https://github.com/catduckgnaf/print-handy/tree/main/docs/history): [operator live-proof protocol](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/PHASE2-LIVE-PROOFS.md), [rename migration](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/RENAME-MIGRATION.md), [Docker acceptance](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/DOCKER-117-ACCEPTANCE.md), [Docker progress](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/DOCKER-117-PROGRESS.md), [timelapse record](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/ISSUE-126-TIMELAPSE.md), [hardcoded values inventory](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/hardcoded-inventory.md), [CAD evaluation](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/KICAD-EVALUATION.md), [reuse map](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/REUSE-MAP.md), [multi-printer design](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/MULTI-PRINTER-DESIGN.md), the [AD5X implementation contract](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/AD5X-CONTRACT.md) and the [recovered testing lane](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/RECOVERY-TESTING.md).
- [3MF remap inventory](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/3MF-REMAP-INVENTORY.md): which 3MF references a conversion remaps, and where each one lives.
- [3MF conversion evidence matrix](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/3MF-CONVERSION-EVIDENCE.md): the criterion-by-criterion evidence for the foreign 3MF conversion work.
- [Geometry soundness audit](https://github.com/catduckgnaf/print-handy/blob/main/docs/history/GEOMETRY_AUDIT.md): what the sizing, rotation, mirroring, bed fit and support checks cover, and their known limits.

These versioned `docs/` pages are the source of truth. Document features with the code and identify wiki impact in the [contribution checklist](https://github.com/catduckgnaf/print-handy/blob/main/CONTRIBUTING.md#automated-pr-review-support). Use documentation for the checked-out revision; draft work is not shipped capability.
