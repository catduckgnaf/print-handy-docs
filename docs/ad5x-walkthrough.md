# AD5X walkthrough: from printer to printing from chat

The Flashforge Adventurer 5X (AD5X) is the printer Print Handy was
raised on. This walkthrough takes you from a stock AD5X to dropping a
model link in chat and watching the print start — the whole path, in
order. It favors the ZMod setup most AD5X owners run with Print Handy;
a stock-firmware path exists too and is covered at the fork below.

## What you need

- An AD5X on your network, with its four-slot IFS loaded or ready to load.
- A machine to run Print Handy on (a small server, NAS or Raspberry Pi
  class board is plenty) with Docker.
- A chat account on Discord, Telegram or Matrix. Discord is the path
  most people take first: [Discord bot setup](./discord-bot-setup.md).

## Step 1 — Pick your firmware path

**ZMod (recommended).** ZMod turns the AD5X into a full Klipper /
Moonraker printer, which is where Print Handy can do the most: read
spool slots from Klipper, calibrate from chat, and start prints the
same way ZMod's own macros do. Your printer model key is
`flashforge.ad5x`. Background and details: [ZMod printers](./zmod.md).

**Stock Flashforge firmware.** No ZMod, no Moonraker: Print Handy
talks to the printer's LAN interface instead. Your model key is
`flashforge_stock.ad5x`. What works and what does not is in
[Stock Flashforge](./flashforge-stock.md).

The rest of this walkthrough follows the ZMod path.

## Step 2 — The ZMod setup that works best

The tested baseline is ZMod running **screenless** (`display_off=1`)
with HelixScreen, Fluidd or Mainsail as the local interface. Screenless
is not a downgrade: it is what lets Print Handy read and verify the
values the stock screen would otherwise own.

- Z offset and bed mesh live in Klipper, where Print Handy can read,
  calibrate and verify them.
- IFS slot presence comes from Klipper, so insertion prompts, runout
  evidence and refill events all work.
- Cancels are plain Klipper cancels, handled the same from every
  interface.

Two one-time jobs when you switch from the stock screen:

1. Copy the stock screen's Z offset into the screenless store once
   with ZMod's `LOAD_ZOFFSET_NATIVE`, and keep `load_zoffset=1` set.
2. Build a fresh bed mesh with `/print-calibration` from chat — it
   measures into a scratch profile first and only saves after you
   accept.

The full settings table, purge and mesh choices, and what has been
verified on real hardware: [AD5X best practices](./device-ad5x.md).

## Step 3 — Install Print Handy

Follow the [Docker guide](./docker.md): one container carries the bot,
the printer listener, OrcaSlicer and the bundled Spoolman. The two
things to set for an AD5X are the model and the printer's address:

```ini
PRINT_HANDY__PRINTER__MODEL=flashforge.ad5x
PRINT_HANDY__SERVICES__MOONRAKER_URL=http://<your-ad5x-address>:7125
```

Set the model explicitly — the shipped Docker default is a generic
Klipper printer, and an AD5X left on the default will not see its four
IFS slots.

## Step 4 — Check the setup before the first print

Run the setup checks from the Docker guide and confirm the bot answers
in your channel. Two AD5X-specific checks are worth the minute:

- `/print-firmware` shows the ZMod version Print Handy can read. Check
  it again after any ZMod update.
- Ask the bot what is loaded. It should name the spools in your IFS
  slots — that answer comes from Klipper, so it proves the whole chain
  (bot, Moonraker, ZMod) in one question.

## Step 5 — Your first print

1. Drop a model link (MakerWorld, Printables, Thingiverse and friends)
   or an STL/3MF file into the chat.
2. Answer the color questions: each part maps to one of your four IFS
   slots, and Print Handy checks the loaded spools match.
3. Pick how many copies, review the sliced estimate, and approve it.
   Nothing reaches the printer before that approval — that is the
   whole design.
4. Follow along in the same chat: progress posts, a timelapse when it
   finishes, and a mention for whoever started the print.

## Step 6 — Spools and the IFS

Spoolman is built into the install, so there is nothing extra to run:
Print Handy keeps the spool records and matches them to the four IFS
slots. Assign a spool to a slot once and Print Handy remembers what is
loaded where, asks when a job wants a color that is not loaded, and
walks you through a spool change when you ask.

One AD5X nicety worth setting up: load two slots with the same color
and material and ZMod's native infinite-spool handling switches to the
backup automatically when the first spool runs out — Print Handy
verifies the backup really is the same color, material and profile
before it counts as a candidate.

## Where to go next

- [AD5X best practices](./device-ad5x.md) — the settings and habits
  that work well, in the order to change them.
- [ZMod printers](./zmod.md) — delivery formats, versions and the
  ZMod-specific behavior in depth.
- [Printer calibration](./calibration.md) — Z offset, mesh and the
  supervised calibration flows.
- [Troubleshooting](./troubleshooting.md) — by symptom, when something
  does not behave.
