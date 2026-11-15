import DefaultTheme from 'vitepress/theme'
import Layout from './Layout.vue'
import ScreenshotGallery from './ScreenshotGallery.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    app.component('ScreenshotGallery', ScreenshotGallery)
  },
}
