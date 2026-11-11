# Print Handy branding kit

One place for the name, the pitch, the voice and the assets. When a page, a
store listing or a link preview describes Print Handy, it copies from here, so
the README, the docs site, the Unraid template, GitHub and anyone else's
listing all say the same thing.

## The pitch

**Local first. Local your way.**

**Design, slice and manage prints without opening a slicer.**

Bambu Handy for every printer.

Bambu owners get a slick phone app: find a model, tap print, check on it from
anywhere. Everyone else gets a slicer chained to a desktop, a USB stick, and a
walk to the garage to see if the first layer stuck. Print Handy is that phone
experience for everybody else, Bambu included. It lives in the chat app you
already have open, so "print this" is one pasted link instead of a sit-down
session with a slicer.

What it is, in facts: describe a model in Discord, Telegram or Matrix with an optional design model endpoint, then review the OpenSCAD preview and changes; or provide a model link, STL or 3MF without any LLM. Print Handy runs the slicer for you and asks for approval before the print starts. The Web UI provides local chat, status, settings, print data, Wrapped and spool management. Camera monitoring (Pasta Cam), timelapses and the local no-LLM roast engine add the fun. Printer care includes calibration and Spoolman-backed spools, with firmware and plugin/component updates only on eligible Moonraker setups (beta, confirmed actions). One Docker container, or the native standalone bot.

Local-first is part of the pitch, not a footnote: Print Handy was made as a
local-only solution that runs on the owner's machine and talks to printers on
the local network, with no Print Handy account and no Print Handy cloud. AI
is optional, and Discord is optional; neither is needed for the core flows.
Say so wherever there is room, in those words or close to them — and never
stretch it into "nothing leaves the house": the chat provider the owner picks
carries the messages, files and photos sent through it, like any other
message on that platform.

Always pair the Bambu comparison with the not-affiliated line wherever there is
room for it:

> Not affiliated with Bambu Lab. We just liked their app enough to want it on
> every other printer.

## Copy by length

Copy these as written. Each one is sized for where it goes. Do not call two native bot guides two install methods. Print Handy is available in Unraid Community Apps.

| Use | Length | Copy |
|---|---|---|
| Tagline | 6 words | Local first. Local your way. |
| Link preview, GitHub repo description | under 160 characters | Design with optional AI, or send a model link. Printing, management, Wrapped and Pasta Cam, on your hardware. LLM optional. |
| Store listing or plugin list, one line | one sentence | Design a part with optional AI or send a model link; Print Handy slices it for you, manages spools and printers, and keeps the fun local. |
| Short paragraph | about 60 words | Print Handy is local first, your way. Describe a part with optional AI or share an STL, 3MF or model link. It handles the slicer and approval, tracks spools with Spoolman, supports printer management and eligible beta firmware updates, and brings Wrapped, Pasta Cam and local roasts. Use the Web UI, Discord, Telegram or Matrix. No LLM required for normal printing. |

## Voice

- **Funny about the model, never about safety.** Keep approval prompts, heat and motion warnings, refusals and errors plain and exact. Put roasts only where they belong: one per print on the completion post, the failure and cancel posts, and a confirmed-spaghetti camera alert, drawn from the local roast corpus (no LLM, no endpoint, #1002); never in safety copy.
- **Short, concrete and task-first.** Say what the reader can do, then link to details. Avoid repetitive reassurance and exhaustive inventories on entry pages.
- **Local-first, stated honestly.** Print Handy itself runs on the owner's machine and has no Print Handy cloud. Chat providers carry messages and files; model downloads and optional hosted AI use the network. Never claim that nothing leaves the house.
- **No manual slicer means no slicer app to operate, not no slicing.** Print Handy still uses OrcaSlicer or the configured slicer in the background. AI design requires a configured endpoint and OpenSCAD; printing existing models does not need an LLM.
- **Beta updates are limited.** Firmware and plugin component updates are guarded and apply only to eligible Moonraker configurations. Other families get information or manual guidance. Print Handy does not update its own container, Spoolman or OrcaSlicer through that command.
- **Mark optional features clearly.** Camera monitoring, AI, live viewing and printer controls are optional or separately enabled. Do not imply camera analysis guarantees safe unattended printing.
- **Describe supported paths, not every printer.** Name connection families in short copy and link to the current support guide. Distinguish code coverage from hardware verification. Never imply certification.
- **Preserve approvals.** State that the exact sliced job needs human approval before printing. Do not suggest a model estimate or bounding box proves a safe physical print.
- **American spelling** (color, behavior, gray) and avoid em dashes.

Approved short copy:

- "Your slicer lives on a desk. You don’t."
- "Another articulated dragon? Bold choice."
- "Sometimes it really is fine. Sometimes it's modern art."
- "Spoolman, minus the spreadsheet."
- "Not affiliated with Bambu Lab. We just liked their app enough to want it on every other printer."

## The mascot

The mascot is the catduck: a yellow, fluffy cat with duck feet and a nozzle
thumbs-up, on a black rounded tile with a green ring. It is named after the
maintainer's handle. Use it as is: no recoloring, no cropping off the feet, no
stretching.

## Colors

| Name | Hex | Where it comes from |
|---|---|---|
| Catduck yellow | `#F5C247` | Mascot fur |
| Duck-foot yellow | `#FED32C` | Mascot feet, highlights |
| Tile black | `#181818` | Icon tile, wordmark |
| Ring green | `#4B985C` | Icon ring, success accents |
| Eye blue | `#1286E3` | Mascot eyes, links |
| Docs orange | `#F97316` | Docs site theme color |

## Assets

All in [`assets/branding/`](https://github.com/catduckgnaf/print-handy/tree/main/assets/branding):

| File | Size | Use it for |
|---|---|---|
| `social-preview.png` | 1280 x 640 | GitHub social preview, link preview cards (`og:image`) |
| `logo-lockup.png` / `logo-lockup-dark.png` | 2240 x 1120 | README header and docs (light and dark backgrounds) |
| `avatar-1024.png` | 1024 x 1024 | Bot avatars (Discord, Telegram, Matrix), Unraid and store icons |
| `icon-master.png`, `icon-16` to `icon-512.png`, `favicon.ico` | various | Favicons, app icons, the Web UI |

## Where the copy lives

Update these together when the pitch changes:

| Surface | Where |
|---|---|
| README | `README.md` (synced to the docs site's Guide page on release) |
| Docs home page and link preview | `print-handy-docs`: `docs/index.md` and `docs/.vitepress/config.mjs` |
| Unraid template | `docker/unraid/print-handy.xml` here and `catduck-unraid-templates/templates/print-handy.xml` |
| GitHub repo description and social preview | Repository settings |
| Third-party listings | ZMod's plugin list (`ghzserg/zmod` `docs/*/Plugin.md`) |
