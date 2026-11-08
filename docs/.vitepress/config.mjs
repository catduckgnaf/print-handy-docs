import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Print Handy',
  description: 'Your slicer lives on a desk. You don’t. Share a model link or file, choose filament, review the estimate and approve the job. Runs locally; chat providers, model downloads and optional hosted AI use the network.',
  base: '/print-handy-docs/',
  cleanUrls: true,
  lastUpdated: true,
  head: [
    ['link', { rel: 'icon', href: '/print-handy-docs/favicon.ico' }],
    ['link', { rel: 'apple-touch-icon', href: '/print-handy-docs/apple-touch-icon.png' }],
    ['meta', { name: 'theme-color', content: '#f97316' }],
    ['meta', { property: 'og:title', content: 'Print Handy: Bambu Handy for every printer' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'Print Handy: Bambu Handy for every printer' }],
    ['meta', { name: 'twitter:description', content: 'Bambu Handy for every printer. Drop a model link in Discord, Telegram or Matrix, approve it, walk away. It slices, watches for spaghetti and roasts your model.' }],
    ['meta', { property: 'og:image', content: 'https://catduckgnaf.github.io/print-handy-docs/social-preview.png' }],
    ['meta', { name: 'twitter:image', content: 'https://catduckgnaf.github.io/print-handy-docs/social-preview.png' }],
    ['meta', { property: 'og:description', content: 'Bambu Handy for every printer. Drop a model link in Discord, Telegram or Matrix, approve it, walk away. It slices, watches for spaghetti and roasts your model.' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:url', content: 'https://catduckgnaf.github.io/print-handy-docs/' }],
  ],
  themeConfig: {
    logo: '/logo-dark.png',
    siteTitle: 'Print Handy',
    nav: [
      { text: 'Start here', link: '/guide' },
      { text: 'Demo', link: '/live-demo' },
      { text: 'Printers', link: '/printer-profiles' },
      { text: 'Everyday use', link: '/project-reference' },
      { text: 'Troubleshooting', link: '/troubleshooting' },
    ],
    sidebar: [
      {
        text: 'Guide',
        items: [
          { text: 'Introduction', link: '/guide' },
          { text: 'Live demo', link: '/live-demo' },
          { text: 'Project Reference', link: '/project-reference' },
          { text: 'Multi-part print projects', link: '/projects' },
          { text: 'Listener Domains', link: '/listeners' },
        ],
      },
      {
        text: 'Get started',
        items: [
          { text: 'Docker', link: '/docker' },
          { text: 'Standalone Bot', link: '/standalone' },
          { text: 'Hermes Installation', link: '/install' },
          { text: 'More Than One Printer', link: '/multi-instance' },
          { text: 'Bambu A1 with Docker', link: '/bambu-a1-docker' },
        ],
      },
      {
        text: 'Bots',
        items: [
          { text: 'Discord Bot Setup', link: '/discord-bot-setup' },
          { text: 'Telegram Bot Setup', link: '/telegram-bot-setup' },
          { text: 'Matrix Bot Setup', link: '/matrix-bot-setup' },
          { text: 'Guided Setup & Debugging', link: '/guided-setup-debugging' },
        ],
      },
      {
        text: 'Configuration',
        items: [
          { text: 'YAML Configuration', link: '/configuration-yaml' },
          { text: 'Settings Reference', link: '/settings' },
          { text: 'Web UI', link: '/webui' },
          { text: 'Cloudflare AI endpoints', link: '/cloudflare' },
        ],
      },
      {
        text: 'Printers',
        items: [
          { text: 'Printer Profiles', link: '/printer-profiles' },
          { text: 'Printer support', link: '/printer-support' },
          { text: 'AD5X walkthrough', link: '/ad5x-walkthrough' },
          { text: 'AD5X best practices', link: '/device-ad5x' },
          { text: 'ZMod', link: '/zmod' },
          { text: 'Stock Flashforge', link: '/flashforge-stock' },
          { text: 'Bambu Lab', link: '/bambu-lab' },
          { text: 'Prusa', link: '/prusa' },
          { text: 'Elegoo', link: '/elegoo' },
          { text: 'Creality', link: '/creality' },
          { text: 'Qidi', link: '/qidi' },
          { text: 'Anycubic', link: '/anycubic' },
          { text: 'Sovol', link: '/sovol' },
          { text: 'Snapmaker (U1)', link: '/snapmaker' },
          { text: 'OctoPrint / Marlin', link: '/octoprint-marlin' },
          { text: 'Flash Studio', link: '/flash-studio' },
          { text: 'Printer calibration', link: '/calibration' },
          { text: 'Firmware updates', link: '/firmware-update' },
        ],
      },
      {
        text: 'Working With Models',
        items: [
          { text: 'Intake Limits', link: '/intake-limits' },
          { text: 'Geometry Layout', link: '/geometry-layout' },
          { text: 'CAD Split Plans', link: '/cad-split-plans' },
          { text: 'AI Design', link: '/design' },
          { text: 'Editing a prepared model', link: '/editing' },
          { text: 'Mesh Audit', link: '/mesh-audit' },
          { text: 'Printer Macros', link: '/macros' },
          { text: 'Slicer warnings', link: '/slicer-warnings' },
        ],
      },
      {
        text: 'Troubleshooting',
        items: [
          { text: 'Troubleshooting', link: '/troubleshooting' },
          { text: 'Diagnostics', link: '/diagnostics' },
        ],
      },
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/catduckgnaf/print-handy' },
      { icon: 'discord', link: 'https://discord.gg/mT2Ht3nqZu' },
    ],
    search: {
      provider: 'local',
    },
    editLink: {
      pattern: 'https://github.com/catduckgnaf/print-handy-docs/edit/main/docs/:path',
      text: 'Edit this page on GitHub',
    },
    footer: {
      message: 'Documentation content is copied from <a href="https://github.com/catduckgnaf/print-handy">catduckgnaf/print-handy</a> — that repo\'s <code>docs/</code> directory is the source of truth.',
      copyright: 'Copyright © 2026 catduck. Released under the MIT License.',
    },
  },
})
