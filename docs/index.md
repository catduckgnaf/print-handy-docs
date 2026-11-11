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

This is the example from the GitHub README — the whole flow, as a scroll through one chat conversation. These are mockups built from the bot's real messages and buttons, with placeholder names. Scroll on: the screenshots stay small, the story is on the right.

<div class="story-step">
<div class="story-media">

![Print Handy in Discord: paste a model link, the bot checks the model, then asks which color each part prints in](/screenshots/discord-01-link-and-colors.png)

</div>
<div class="story-text">

**1. Bring a model or design one, then pick your colors.**

Paste a MakerWorld, Printables or Thingiverse link — or just drop an STL or 3MF file into the chat. Print Handy fetches the model, measures it against your printer's bed, and reads the colors the designer used.

Then it asks, part by part, which of *your* loaded filaments each color should print in. Buttons, not commands: if you can tap, you can print. With a configured AI endpoint you can also describe a new part in chat, review its OpenSCAD preview and revise it before Print Handy slices.

</div>
</div>

<div class="story-step">
<div class="story-media">

![Print Handy in Discord: choose the number of copies, then confirm the estimate with Slice and print now, Slice only, Stop with colors saved or Cancel print request](/screenshots/discord-02-copies-and-confirm.png)

</div>
<div class="story-text">

**2. Choose copies, see the estimate, then confirm.**

How many copies? One tap. Print Handy slices the job and shows you the honest numbers first: print time, filament weight, and exactly what will be sent to the printer.

Nothing prints until you approve that exact job — **Slice and print now**, **Slice only** if you are not ready, **Stop with colors saved** to keep your picks for later, or **Cancel**. Your printer never starts on a shrug.

</div>
</div>

<div class="story-step">
<div class="story-media">

![Print Handy in Discord: the print started post, ending with a one-line roast of the model](/screenshots/discord-03-print-start.png)

</div>
<div class="story-text">

**3. The print starts — and yes, it roasts you a little.**

The started post confirms the printer is running and names the spools doing the work, so anyone in the channel can see what is printing and in what.

And because Print Handy has opinions, the post may end with a one-line roast of your model choice — drawn from its built-in corpus, no AI account required. Funny about the model, never about safety: warnings and refusals stay plain and exact.

</div>
</div>

<details>
<summary><b>More of the conversation: fit, spools, the watchdog and the finish</b></summary>

<div class="story-step">
<div class="story-media">

![The fit question and the units question](/screenshots/discord-08-fit-and-geometry.png)

</div>
<div class="story-text">

**If it doesn't fit, you choose how it fits.**

Print Handy measures every model and never silently shrinks one. Too big for the bed? Split it across plates at full size, turn it, shrink it on purpose — or cancel, with the biggest size that *would* fit offered instead of a dead end.

Tiny file with unclear units? You get the millimeters-or-inches question before anything is sliced at the wrong scale.

</div>
</div>

<div class="story-step">
<div class="story-media">

![Print complete post with timelapse](/screenshots/discord-04-print-complete.png)

</div>
<div class="story-text">

**It finishes, with a timelapse.**

The completion post lands in the same chat with a timelapse of the whole print and a final photo of the result — proof, not just a green checkmark.

It mentions the person who started the print, so the right human gets the ping and nobody else's phone buzzes at 2 a.m.

</div>
</div>

<div class="story-step">
<div class="story-media">

![Camera alert with Pause, It's fine and Stop asking for this print](/screenshots/discord-05-camera-watchdog.png)

</div>
<div class="story-text">

**The camera watchdog spots trouble.**

While a print runs, the watchdog keeps an eye on the camera feed for the spaghetti moment. When it sees one, you get the photo and three buttons: **Pause**, **It's fine**, or **Stop asking for this print**.

It can run on a local detector right on your own hardware — no cloud, no AI endpoint, nothing leaving the house.

</div>
</div>

<div class="story-step">
<div class="story-media">

![Paused post and runout spool question](/screenshots/discord-06-pause-and-runout.png)

</div>
<div class="story-text">

**Pause or run out of filament? It asks, properly.**

A paused print and a runout both post to the chat. If a spool ran dry, the spool question walks you through what is loaded now — and answering it settles the spool records honestly, without pretending the print magically resumed.

No silent drops: a print that ends from a pause, by any route, gets named in the chat rather than vanishing.

</div>
</div>

<div class="story-step">
<div class="story-media">

![Changing a spool, guided](/screenshots/discord-09-spool-change.png)

</div>
<div class="story-text">

**Change a spool, guided.**

Swapping filament is a four-tap conversation: pick the slot, pick the new spool, decide what happens to the old one, confirm. Print Handy updates the built-in Spoolman records as part of the same flow.

No spreadsheets, no "which slot was the red one in again" — Print Handy remembers what is loaded where.

</div>
</div>

<div class="story-step">
<div class="story-media">

![New spool prompt and load flow](/screenshots/discord-07-new-spool.png)

</div>
<div class="story-text">

**New spool? It offers it a home.**

Add a spool in Spoolman and Print Handy notices — it offers the new spool for a slot in chat, so the record and the printer agree from the start.

The same works in reverse: what you load through chat is what Spoolman shows. One set of books, kept for you.

</div>
</div>

</details>

## Why this exists

A printer shouldn't require an appointment with a desktop slicer for every job. Describe what you need with optional AI, drop in a model link or upload a file, then let Print Handy prepare the job and ask for approval before it prints.

Get status and printer management in the local Web UI, or use the chat you already have open. Pasta Wrapped remembers the year. Pasta Cam watches for trouble on supported setups. The roasts don't even need an LLM.

*Not affiliated with Bambu Lab. We just liked their app enough to want that convenience on more printers.*

## Start here

- Available in **Unraid Community Apps**. [Installation details](/docker#unraid-dockerman).
- [Docker](/docker): one container with the bot, printer listeners, slicer and bundled Spoolman.
- [Native installation](/install): the same standalone bot installed with Python and systemd, without Docker.
- [Design a model](/design): optional AI design in chat, preview and revise before guided slicing.
- [Web UI](/webui): local chat, status, settings, spool management, print records and Pasta Wrapped.
- [Discord](/discord-bot-setup), [Telegram](/telegram-bot-setup) or [Matrix](/matrix-bot-setup): choose a chat interface, or just use the Web UI.
- [Printer support](/printer-support) · [Printer profiles](/printer-profiles) · [Troubleshooting](/troubleshooting).
- [Community Discord](https://discord.gg/mT2Ht3nqZu): support and discussion.
