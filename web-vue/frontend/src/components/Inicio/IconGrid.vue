<template>
    <div
      class="icons-grid"
      @mouseover="hover = true"
      @mouseleave="hover = false"
    >
      <div
        v-for="(icon, index) in icons"
        :key="index"
        class="icon"
      >
        <img :src="icon.src" :alt="icon.alt" />
      </div>
    </div>
  </template>

  <script setup>
  import { ref } from 'vue';

  const props = defineProps({
    icons: {
      type: Array,
      required: true
    }
  });

  // Estado para manejar el hover
  const hover = ref(false);
  </script>

  <style scoped>
  /* Grid para los íconos */
  .icons-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    gap: 5px;
    padding: 20px;
    background-color: transparent;
  }

  .icon img {
    width: 40px; /* Íconos más pequeños */
    height: 40px;
    transition: transform 0.3s ease, filter 0.3s ease;
    filter: brightness(0) saturate(100%) invert(61%) sepia(85%) saturate(200%) hue-rotate(185deg) brightness(95%) contrast(95%);
    /* Color inicial azul claro */
  }

  .icons-grid:hover img {
    transform: scale(1.1); /* Aumenta el tamaño de todos los íconos */
    filter: none; /* Elimina el filtro para todos los íconos en hover */
  }

  .icon {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    background-color: rgba(240, 240, 240, 0.9); /* Fondo blanco semi-transparente */
    transition: background-color 0.3s ease;
  }

  .icon:hover {
    background-color: rgba(46, 177, 221, 0.1); /* Fondo azul claro al pasar el cursor */
  }
  </style>
