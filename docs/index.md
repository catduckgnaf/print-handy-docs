---
layout: home

hero:
  name: "Print Handy"
  text: "Your slicer lives on a desk. You don’t."
  tagline: "Drop a model link in chat, pick your colors, approve the slice — then go live your life while it prints. Bambu Handy energy, for every printer. Even Bambu."
  image:
    src: /logo-dark.png
    alt: Print Handy catduck mascot
  actions:
    - theme: brand
      text: Get Started
      link: /docker
    - theme: alt
      text: Try the live demo
      link: /live-demo
    - theme: alt
      text: Join the Discord
      link: https://discord.gg/mT2Ht3nqZu

features:
  - icon: 📱
    title: A shorter trip to print
    details: Send a model link or file from Discord, Telegram or Matrix. Print Handy slices it, shows you the estimate, and waits for your say-so.
  - icon: 🖨️
    title: Bambu Handy for everyone — even Bambu
    details: The find-it, tap-print, check-from-the-sofa phone experience Bambu owners love, brought to Klipper, Flashforge, Prusa, Elegoo, Creality, Sovol, Snapmaker, Qidi, Anycubic and OctoPrint printers — and yes, Bambu too.
  - icon: 🎉
    title: Fun features!
    details: A gentle roast when your print starts, timelapses that land in the chat when it finishes, a camera watchdog that watches for spaghetti, and spools that practically manage themselves.
  - icon: 🧵
    title: Spoolman built in
    details: Filament tracking rides along in the same install — no second service to set up. Print Handy matches spools to printer slots and knows what is loaded where.
  - icon: 🏠
    title: Local-first
    details: Runs on your hardware, in your house, with no Print Handy cloud. AI and chat platforms are optional extras, never a requirement.
---

[![CI](https://github.com/catduckgnaf/print-handy/actions/workflows/ci.yml/badge.svg)](https://github.com/catduckgnaf/print-handy/actions/workflows/ci.yml)
[![GitHub releases](https://img.shields.io/github/v/release/catduckgnaf/print-handy)](https://github.com/catduckgnaf/print-handy/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/catduckgnaf/print-handy/blob/main/LICENSE)

## See it in action

This is the example from the GitHub README — the whole flow, as a scroll through one chat conversation. These are mockups built from the bot's real messages and buttons, with placeholder names.

<div class="story-step">

**1. Drop a link, pick your colors.**

![Print Handy in Discord: paste a model link, the bot checks the model, then asks which color each part prints in](/screenshots/discord-01-link-and-colors.png)

</div>

<div class="story-step">

**2. Choose how many copies, then confirm — nothing prints until you do.**

![Print Handy in Discord: choose the number of copies, then confirm the estimate with Slice and print now, Slice only, Stop with colors saved or Cancel print request](/screenshots/discord-02-copies-and-confirm.png)

</div>

<div class="story-step">

**3. The print starts — and yes, it roasts you a little.**

![Print Handy in Discord: the print started post, ending with a one-line roast of the model](/screenshots/discord-03-print-start.png)

</div>

<details>
<summary><b>More of the conversation: fit, spools, the watchdog and the finish</b></summary>

<div class="story-step">

**If it doesn't fit, choose how it fits.** The model is measured, never silently shrunk: split it across plates at full size, turn it, shrink it — or cancel.

![The fit question and the units question](/screenshots/discord-08-fit-and-geometry.png)

</div>

<div class="story-step">

**It finishes, with a timelapse.**

![Print complete post with timelapse](/screenshots/discord-04-print-complete.png)

</div>

<div class="story-step">

**The camera watchdog spots trouble.**

![Camera alert with Pause, It's fine and Stop asking for this print](/screenshots/discord-05-camera-watchdog.png)

</div>

<div class="story-step">

**Pause, runout and the spool question.**

![Paused post and runout spool question](/screenshots/discord-06-pause-and-runout.png)

</div>

<div class="story-step">

**Change a spool, guided.** Pick the slot, pick the new spool, decide what happens to the old one, confirm.

![Changing a spool, guided](/screenshots/discord-09-spool-change.png)

</div>

<div class="story-step">

**A spool added in Spoolman gets offered for a slot.**

![New spool prompt and load flow](/screenshots/discord-07-new-spool.png)

</div>

</details>

## Why this exists

Bambu owners get a slick phone app: find a model, tap print, check on it from anywhere. Everyone else gets a slicer chained to a desktop, a USB stick, and a walk to the garage to see if the first layer stuck.

Print Handy is that phone experience for everybody else. It lives in the chat app you already have open, so "print this" is one pasted link instead of a sit-down session with a slicer. It is also a little mean about your model choices, which is a feature.

*Not affiliated with Bambu Lab. We just liked their app enough to want it on every other printer.*

## Start here

- [Live demo](/live-demo) — try the conversation in your browser. Nothing installs, nothing prints.
- [Docker](/docker) — the single-container install: bot, listener and bundled Spoolman in one image.
- [Introduction](/guide) — the documentation index and how to find the right guide.
- [Discord bot setup](/discord-bot-setup) — create your Discord application and bot, and hand Print Handy the token and IDs safely.
- [Printer profiles](/printer-profiles) — find your printer and see what it can do.
- [AD5X walkthrough](/ad5x-walkthrough) — the Flashforge AD5X with ZMod, end to end.
- [Web UI](/webui) — a local status and settings page for your own network.
- [Troubleshooting](/troubleshooting) — troubleshoot by symptom.
- [Print Handy Discord server](https://discord.gg/mT2Ht3nqZu) — support, chat and the live demo server; ask in #support when you are stuck.
