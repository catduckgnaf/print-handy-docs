---
layout: home

hero:
  name: "Print Handy"
  text: "Bambu Handy for every printer"
  tagline: "Paste a MakerWorld or Printables link from your phone. Print Handy slices it, matches your spools, asks before it prints, watches the camera for spaghetti, and roasts your model on the way out. Works from the couch, the office, or the grocery store checkout line. We don't judge. The bot does."
  image:
    src: /logo.png
    alt: Print Handy
  actions:
    - theme: brand
      text: Get Started
      link: /docker
    - theme: alt
      text: View on GitHub
      link: https://github.com/catduckgnaf/print-handy

features:
  - icon: 📱
    title: Print from anywhere
    details: Your slicer lives on a desk. You don't. Drop a link or upload an STL or 3MF in chat, pick colors with buttons, and the job is sliced and waiting for your OK before you're back from the fridge.
  - icon: 🔥
    title: Roasts included
    details: Every print start comes with a one-line roast of your model. Another articulated dragon? Bold choice. Needs an AI endpoint, and you can turn it off if your ego is fragile.
  - icon: 🍝
    title: Spaghetti patrol
    details: The camera watchdog checks frames for spaghetti, detached parts and stalls, then asks with Pause and It's fine buttons. Sometimes it really is fine. Sometimes it's modern art.
  - icon: ✅
    title: Nothing prints behind your back
    details: You check the bed and approve the exact sliced job before anything is sent. Lock approvals to one person if your friends have questionable taste.
  - icon: 🧵
    title: Spoolman, minus the spreadsheet
    details: Spools are matched to slots, runouts ask what you loaded, and filament is charged to the right spool. Bookkeeping you'll actually keep.
  - icon: 🖨️
    title: Every printer, every chat
    details: Klipper, Bambu Lab, Flashforge, Prusa, Elegoo, Creality, Sovol, Snapmaker, Qidi, Anycubic and OctoPrint. Discord, Telegram or Matrix, plus a Web UI for status, settings and spools. One Docker container, no slicer babysitting.
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
