import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import Components from 'unplugin-vue-components/vite';
import { PrimeVueResolver } from 'unplugin-vue-components/resolvers';
import dotenv from 'dotenv';
dotenv.config();

export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: `http://localhost:3657`, // URL del servidor de Express
        changeOrigin: true,
        secure: false, // Cambia a `false` si estás usando HTTP sin SSL
        //rewrite: (path) => path.replace(/^\/api/, ''), // Elimina /api del inicio de la URL
      },
    },
  },
  plugins: [
    vue(),
    Components({
      resolvers: [PrimeVueResolver()],
    }),
  ],
});
