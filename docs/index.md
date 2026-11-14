---
layout: home

hero:
  name: "Print Handy"
  text: "Design it. Print it. Skip opening a slicer."
  tagline: "Describe a part with optional AI, or send a model link or file. Print Handy handles the slicing and asks before printing. Local first. Local your way: Web UI, Discord, Telegram or Matrix. LLM or no LLM."
  image:
    src: /logo-dark.png
    alt: Print Handy catduck mascot
  actions:
    - theme: brand
      text: Get Started
      link: /guide
    - theme: alt
      text: Design a model
      link: /design
    - theme: alt
      text: Unraid Community Apps
      link: /docker#unraid-dockerman

features:
  - icon: 🧩
    title: Design a model. No slicer app required.
    details: Describe a part, preview it and request changes with optional AI and OpenSCAD. Or bring your own STL, 3MF or model link. Print Handy slices in the background and asks you to approve the actual job.
  - icon: 🎉
    title: Pasta Wrapped, Pasta Cam and a little attitude
    details: Pasta Wrapped recaps your printing year, with optional local video and sharing. Pasta Cam watches for print failures where supported; timelapses and a built-in, no-LLM roast engine make the rest more fun.
  - icon: 🛠️
    title: Complete printer management
    details: Manage prints, printers, calibration and filament with bundled Spoolman. Check firmware and supported plugin updates where available. In beta, updates are limited by printer family and require confirmation.
  - icon: 🏠
    title: Local first. Local your way.
    details: Runs on your hardware with no Print Handy cloud. Use the local Web UI, Discord, Telegram or Matrix. Ordinary printing and roasts need no LLM; AI design is optional. External chat services carry what you send through them.
---

## From idea to printed part

Ask **"design a wall hook with two screw holes"** in chat, review the preview and request changes, then approve the prepared print. AI design needs a configured model endpoint; Print Handy runs OpenSCAD and the slicer for you. **You do not have to open or operate a slicer yourself.**

Prefer no AI? Send an STL, 3MF or model link instead. The same guided slicing, filament choices, checks and final approval work without an LLM. [How design works](/design) · [Printing without an LLM](/standalone) · [Supported printers](/printer-profiles)

## See it in action

This is the example from the GitHub README — the whole flow, through one chat conversation. These are mockups built from the bot's real messages and buttons, with placeholder names. Flip through the conversation with the Next and Previous buttons: each photo comes with its part of the story.

<ScreenshotGallery />

## Why this exists

A printer shouldn't require an appointment with a desktop slicer for every job. Describe what you need with optional AI, drop in a model link or upload a file, then let Print Handy prepare the job and ask for approval before it prints.

Get status and printer management in the local Web UI, or use the chat you already have open. Pasta Wrapped remembers the year. Pasta Cam watches for trouble on supported setups. The roasts don't even need an LLM.

*Not affiliated with Bambu Lab. We just liked their app enough to want that convenience on more printers.*

## Start here

- Available in **Unraid Community Apps**. [Installation details](/docker#unraid-dockerman).
- Available as a **Home Assistant OS app**: add `https://github.com/catduckgnaf/print-handy-haos-addon` under **Settings > Apps > App store > Repositories** and install **Print Handy**. It runs the same image and updates itself with each release. [Installation details](/home-assistant-os).
- [Docker](/docker): one container with the bot, printer listeners, slicer and bundled Spoolman.
- [Native installation](/install): the same standalone bot installed with Python and systemd, without Docker.
- [Design a model](/design): optional AI design in chat, preview and revise before guided slicing.
- [Web UI](/webui): local chat, status, settings, spool management, print records and Pasta Wrapped.
- [Discord](/discord-bot-setup), [Telegram](/telegram-bot-setup) or [Matrix](/matrix-bot-setup): choose a chat interface, or just use the Web UI.
- [Printer support](/printer-support) · [Printer profiles](/printer-profiles) · [Troubleshooting](/troubleshooting).
- [Community Discord](https://discord.gg/mT2Ht3nqZu): support and discussion.
