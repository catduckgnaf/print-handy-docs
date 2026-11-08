---
layout: home

hero:
  name: "Print Handy"
  text: "Your slicer lives on a desk. You don’t."
  tagline: "Share a model link or file. Choose filament, review the estimate, and approve the exact job before it reaches your printer."
  image:
    src: /logo-dark.png
    alt: Print Handy catduck mascot
  actions:
    - theme: brand
      text: Get Started
      link: /docker
    - theme: alt
      text: View on GitHub
      link: https://github.com/catduckgnaf/print-handy
    - theme: alt
      text: Join the Discord
      link: https://discord.gg/mT2Ht3nqZu

features:
  - icon: 📱
    title: A shorter trip to print
    details: Send a model link or file from Discord, Telegram or Matrix. Print Handy slices it and waits for your approval.
  - icon: ✅
    title: You approve the job
    details: Review the sliced job and estimate before a print is sent. Keep the human in the loop, where the hot equipment is.
  - icon: 🧵
    title: Filament in view
    details: Track spools with the bundled Spoolman API and match them to printer slots.
  - icon: 🖨️
    title: Several connection paths
    details: Works across supported Klipper, Bambu Lab, Flashforge, Prusa, Elegoo, Creality, Sovol, Snapmaker, Qidi, Anycubic and OctoPrint paths. See printer guides for limits and hardware verification status.
  - icon: 🏠
    title: Local-first
    details: Runs on your hardware without a Print Handy cloud. Chat providers carry what you send; model downloads and optional hosted AI use the network.
  - icon: 🍝
    title: Optional camera checks
    details: Configure a camera watchdog and a vision endpoint or local detector. Alerts are not a promise of safe unattended printing.
---

[![CI](https://github.com/catduckgnaf/print-handy/actions/workflows/ci.yml/badge.svg)](https://github.com/catduckgnaf/print-handy/actions/workflows/ci.yml)
[![GitHub releases](https://img.shields.io/github/v/release/catduckgnaf/print-handy)](https://github.com/catduckgnaf/print-handy/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/catduckgnaf/print-handy/blob/main/LICENSE)

## Why this exists

Bambu owners get a slick phone app: find a model, tap print, check on it from anywhere. Everyone else gets a slicer chained to a desktop, a USB stick, and a walk to the garage to see if the first layer stuck.

Print Handy is that phone experience for everybody else, Bambu included. It lives in the chat app you already have open, so "print this" is one pasted link instead of a sit-down session with a slicer. It is also a little mean about your model choices, which is a feature.

*Not affiliated with Bambu Lab. We just liked their app enough to want it on every other printer.*

## Start here

- [Introduction](/guide) — the documentation index and how to find the right guide.
- [Docker](/docker) — the single-container install: bot, listener and bundled Spoolman in one image.
- [Web UI](/webui) — optional local status, settings, designs, and a read-only sliced-layer view. It is off by default, and it does not start a print.
- [Discord bot setup](/discord-bot-setup) — create your Discord application and bot, and hand Print Handy the token and IDs safely.
- [Printer profiles](/printer-profiles) — supported printers, delivery methods and verification limits.
- [Troubleshooting](/troubleshooting) — troubleshoot by symptom.
- [Print Handy Discord server](https://discord.gg/mT2Ht3nqZu) — support, chat and the live demo server; ask in #support when you are stuck.
