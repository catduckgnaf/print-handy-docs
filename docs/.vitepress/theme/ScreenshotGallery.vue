<script setup>
import { computed, onMounted, ref } from 'vue'
import { withBase } from 'vitepress'

// The "See it in action" story from the homepage, one example at a time.
// Slides keep the page's original order, alt text and story copy; flipping
// is manual only (Previous / Next buttons, dots, or arrow keys) and wraps
// around at both ends. Without JavaScript every slide stays listed, the
// way the page read before the gallery.
const slides = [
  {
    src: '/screenshots/discord-01-link-and-colors.png',
    alt: 'Print Handy in Discord: paste a model link, the bot checks the model, then asks which color each part prints in',
    title: '1. Bring a model or design one, then pick your colors.',
    body: [
      'Paste a MakerWorld, Printables or Thingiverse link — or just drop an STL or 3MF file into the chat. Print Handy fetches the model, measures it against your printer\'s bed, and reads the colors the designer used.',
      'Then it asks, part by part, which of <em>your</em> loaded filaments each color should print in. Buttons, not commands: if you can tap, you can print. With a configured AI endpoint you can also describe a new part in chat, review its OpenSCAD preview and revise it before Print Handy slices.',
    ],
  },
  {
    src: '/screenshots/discord-02-copies-and-confirm.png',
    alt: 'Print Handy in Discord: choose the number of copies, then confirm the estimate with Slice and print now, Slice only, Stop with colors saved or Cancel print request',
    title: '2. Choose copies, see the estimate, then confirm.',
    body: [
      'How many copies? One tap. Print Handy slices the job and shows you the honest numbers first: print time, filament weight, and exactly what will be sent to the printer.',
      'Nothing prints until you approve that exact job — <strong>Slice and print now</strong>, <strong>Slice only</strong> if you are not ready, <strong>Stop with colors saved</strong> to keep your picks for later, or <strong>Cancel</strong>. Your printer never starts on a shrug.',
    ],
  },
  {
    src: '/screenshots/discord-03-print-start.png',
    alt: 'Print Handy in Discord: the print started post, ending with a one-line roast of the model',
    title: '3. The print starts — and yes, it roasts you a little.',
    body: [
      'The started post confirms the printer is running and names the spools doing the work, so anyone in the channel can see what is printing and in what.',
      'And because Print Handy has opinions, the post may end with a one-line roast of your model choice — drawn from its built-in corpus, no AI account required. Funny about the model, never about safety: warnings and refusals stay plain and exact.',
    ],
  },
  {
    src: '/screenshots/discord-08-fit-and-geometry.png',
    alt: 'The fit question and the units question',
    title: 'If it doesn\'t fit, you choose how it fits.',
    body: [
      'Print Handy measures every model and never silently shrinks one. Too big for the bed? Split it across plates at full size, turn it, shrink it on purpose — or cancel, with the biggest size that <em>would</em> fit offered instead of a dead end.',
      'Tiny file with unclear units? You get the millimeters-or-inches question before anything is sliced at the wrong scale.',
    ],
  },
  {
    src: '/screenshots/discord-04-print-complete.png',
    alt: 'Print complete post with timelapse',
    title: 'It finishes, with a timelapse.',
    body: [
      'The completion post lands in the same chat with a timelapse of the whole print and a final photo of the result — proof, not just a green checkmark.',
      'It mentions the person who started the print, so the right human gets the ping and nobody else\'s phone buzzes at 2 a.m.',
    ],
  },
  {
    src: '/screenshots/discord-05-camera-watchdog.png',
    alt: 'Camera alert with Pause, It\'s fine and Stop asking for this print',
    title: 'The camera watchdog spots trouble.',
    body: [
      'While a print runs, the watchdog keeps an eye on the camera feed for the spaghetti moment. When it sees one, you get the photo and three buttons: <strong>Pause</strong>, <strong>It\'s fine</strong>, or <strong>Stop asking for this print</strong>.',
      'It can run on a local detector right on your own hardware — no cloud, no AI endpoint, nothing leaving the house.',
    ],
  },
  {
    src: '/screenshots/discord-06-pause-and-runout.png',
    alt: 'Paused post and runout spool question',
    title: 'Pause or run out of filament? It asks, properly.',
    body: [
      'A paused print and a runout both post to the chat. If a spool ran dry, the spool question walks you through what is loaded now — and answering it settles the spool records honestly, without pretending the print magically resumed.',
      'No silent drops: a print that ends from a pause, by any route, gets named in the chat rather than vanishing.',
    ],
  },
  {
    src: '/screenshots/discord-09-spool-change.png',
    alt: 'Changing a spool, guided',
    title: 'Change a spool, guided.',
    body: [
      'Swapping filament is a four-tap conversation: pick the slot, pick the new spool, decide what happens to the old one, confirm. Print Handy updates the built-in Spoolman records as part of the same flow.',
      'No spreadsheets, no "which slot was the red one in again" — Print Handy remembers what is loaded where.',
    ],
  },
  {
    src: '/screenshots/discord-07-new-spool.png',
    alt: 'New spool prompt and load flow',
    title: 'New spool? It offers it a home.',
    body: [
      'Add a spool in Spoolman and Print Handy notices — it offers the new spool for a slot in chat, so the record and the printer agree from the start.',
      'The same works in reverse: what you load through chat is what Spoolman shows. One set of books, kept for you.',
    ],
  },
]

const current = ref(0)
const enhanced = ref(false)
const count = slides.length
const position = computed(() => `${current.value + 1} / ${count}`)

function goTo(index) {
  current.value = ((index % count) + count) % count
}
function next() {
  goTo(current.value + 1)
}
function previous() {
  goTo(current.value - 1)
}
function onKeydown(event) {
  if (event.key === 'ArrowRight') {
    event.preventDefault()
    next()
  } else if (event.key === 'ArrowLeft') {
    event.preventDefault()
    previous()
  }
}

onMounted(() => {
  enhanced.value = true
})
</script>

<template>
  <div
    class="ph-gallery"
    :class="{ 'ph-gallery--js': enhanced }"
    role="group"
    aria-roledescription="carousel"
    aria-label="Print Handy in Discord, example screenshots"
    tabindex="0"
    @keydown="onKeydown"
  >
    <div
      v-for="(slide, index) in slides"
      :key="slide.src"
      class="ph-slide"
      :class="{ 'ph-slide--active': index === current }"
      :aria-hidden="enhanced && index !== current ? 'true' : undefined"
    >
      <div class="ph-slide-media">
        <img :src="withBase(slide.src)" :alt="slide.alt" />
      </div>
      <div class="ph-slide-caption">
        <p class="ph-slide-title"><strong>{{ slide.title }}</strong></p>
        <!-- Slide copy is the homepage's own story text, kept verbatim. -->
        <p v-for="(paragraph, pIndex) in slide.body" :key="pIndex" v-html="paragraph" />
      </div>
    </div>

    <!-- Controls exist only once JavaScript runs; without it every slide
         is listed and there is nothing for them to do. -->
    <div v-if="enhanced" class="ph-gallery-controls">
      <button type="button" class="ph-gallery-button" aria-label="Previous example" @click="previous">
        ← Previous
      </button>
      <div class="ph-gallery-dots">
        <button
          v-for="(slide, index) in slides"
          :key="`dot-${slide.src}`"
          type="button"
          class="ph-gallery-dot"
          :class="{ 'ph-gallery-dot--active': index === current }"
          :aria-label="`Go to example ${index + 1}: ${slide.title}`"
          :aria-current="index === current ? 'true' : undefined"
          @click="goTo(index)"
        />
      </div>
      <span class="ph-gallery-position" aria-live="polite">{{ position }}</span>
      <button type="button" class="ph-gallery-button" aria-label="Next example" @click="next">
        Next →
      </button>
    </div>
  </div>
</template>
