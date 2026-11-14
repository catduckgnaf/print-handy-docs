import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Print Handy',
  description: 'Design a model with optional AI, or send a model link or file. Print Handy handles slicing and approval, printer management and Pasta Wrapped. Local first, your way, with or without an LLM.',
  base: '/print-handy-docs/',
  cleanUrls: true,
  lastUpdated: true,
  head: [
    ['link', { rel: 'icon', href: '/print-handy-docs/favicon.ico' }],
    ['link', { rel: 'apple-touch-icon', href: '/print-handy-docs/apple-touch-icon.png' }],
    ['meta', { name: 'theme-color', content: '#f97316' }],
    ['meta', { property: 'og:title', content: 'Print Handy: Local first. Local your way.' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'Print Handy: Local first. Local your way.' }],
    ['meta', { name: 'twitter:description', content: 'Design with optional AI or send a model link. Print Handy slices for you, manages printers and spools, and adds Pasta Wrapped and Pasta Cam. Local first. LLM optional.' }],
    ['meta', { property: 'og:image', content: 'https://catduckgnaf.github.io/print-handy-docs/social-preview.png' }],
    ['meta', { name: 'twitter:image', content: 'https://catduckgnaf.github.io/print-handy-docs/social-preview.png' }],
    ['meta', { property: 'og:description', content: 'Design with optional AI or send a model link. Print Handy slices for you, manages printers and spools, and adds Pasta Wrapped and Pasta Cam. Local first. LLM optional.' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:url', content: 'https://catduckgnaf.github.io/print-handy-docs/' }],
  ],
  themeConfig: {
    logo: '/logo-dark.png',
    siteTitle: 'Print Handy',
    nav: [
      { text: 'Start here', link: '/guide' },
      { text: 'Printers', link: '/printer-profiles' },
      { text: 'Everyday use', link: '/project-reference' },
      { text: 'Troubleshooting', link: '/troubleshooting' },
    ],
    sidebar: [
      {
        text: 'Guide',
        items: [
          { text: 'Introduction', link: '/guide' },
          { text: 'Project Reference', link: '/project-reference' },
          { text: 'Multi-part print projects', link: '/projects' },
          { text: 'Listener Domains', link: '/listeners' },
          { text: 'Writing release notes', link: '/release-notes-guide' },
          { text: 'Printer accessories', link: '/accessories' },
          { text: 'Print Handy status voice', link: '/status-voice' },
        ],
      },
      {
        text: 'Get started',
        items: [
          { text: 'Docker', link: '/docker' },
          { text: 'Unraid Community Apps', link: '/docker#unraid-dockerman' },
          { text: 'Home Assistant OS app', link: 'https://github.com/catduckgnaf/print-handy-haos-addon' },
          { text: 'Native installation (standalone bot)', link: '/install' },
          { text: 'More Than One Printer', link: '/multi-instance' },
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
      copyright: 'Copyright © 2026 catduck. Released under the GNU AGPL-3.0-only.',
    },
  },
})
