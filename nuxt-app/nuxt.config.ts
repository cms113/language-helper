import { defineNuxtConfig } from "nuxt";

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  vite: {
    server: {
      watch: {
        usePolling: true,
      },
    },
    define: {
      "process.env.DEBUG": false,
    },
  },
  css: ["mdi/css/materialdesignicons.min.css", "vuetify/lib/styles/main.sass"],
  build: {
    transpile: ["vuetify"],
  },
});
