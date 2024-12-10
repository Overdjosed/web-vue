import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': '/src', // Este es el alias para la carpeta src
    },
  },
  build: {
    rollupOptions: {
      external: [], // Asegúrate de que vue-router no esté listado aquí
    },
  },
});
