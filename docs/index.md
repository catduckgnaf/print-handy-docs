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

## See it in action

This is the example from the GitHub README — the whole flow, as a scroll through one chat conversation. These are mockups built from the bot's real messages and buttons, with placeholder names. Scroll on: the screenshots stay small, the story is on the right.

<div class="story-step">
<div class="story-media">

![Print Handy in Discord: paste a model link, the bot checks the model, then asks which color each part prints in](/screenshots/discord-01-link-and-colors.png)

</div>
<div class="story-text">

**1. Drop a link, pick your colors.**

Paste a MakerWorld, Printables or Thingiverse link — or just drop an STL or 3MF file into the chat. Print Handy fetches the model, measures it against your printer's bed, and reads the colors the designer used.

Then it asks, part by part, which of *your* loaded filaments each color should print in. Buttons, not commands: if you can tap, you can print.

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
