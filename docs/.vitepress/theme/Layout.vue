<script setup>
import DefaultTheme from 'vitepress/theme'
import { withBase } from 'vitepress'

const { Layout } = DefaultTheme
</script>

<template>
  <Layout>
    <template #home-hero-image>
      <div class="hero-side">
        <img
          class="image-src"
          :src="withBase('/logo-dark.png')"
          alt="Print Handy catduck mascot"
        />
        <div class="hero-badges">
          <a href="https://github.com/catduckgnaf/print-handy/actions/workflows/ci.yml" target="_blank" rel="noreferrer">
            <img src="https://github.com/catduckgnaf/print-handy/actions/workflows/ci.yml/badge.svg" alt="CI" />
          </a>
          <a href="https://github.com/catduckgnaf/print-handy/releases" target="_blank" rel="noreferrer">
            <img src="https://img.shields.io/github/v/release/catduckgnaf/print-handy" alt="GitHub releases" />
          </a>
          <a href="https://github.com/catduckgnaf/print-handy/blob/main/LICENSE" target="_blank" rel="noreferrer">
            <img src="https://img.shields.io/badge/License-AGPL--3.0--only-blue.svg" alt="License: AGPL-3.0-only" />
          </a>
        </div>
      </div>
    </template>
  </Layout>
</template>
