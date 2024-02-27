// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  modules: ['@nuxtjs/tailwindcss', '@pinia/nuxt', 'nuxt-icon', 'nuxt3-leaflet', 'nuxt-swiper','@nuxt/image',],
  runtimeConfig:{
    public: {
      BASE_URL: 'http://localhost:8000',
    },
  },
  vite: {
    server: {
      watch: {
        usePolling: true,
      },
    },
  },

})
