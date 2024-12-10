<template>
  <body>
    <div>
      <router-view></router-view> <!-- Aquí se mostrarán las diferentes vistas -->
    </div>
</body>
</template>

<style scoped>
html {
  scroll-behavior: smooth;
  margin: 0;
  padding: 0;
}

body {
  margin: 0;
  padding: 0;
  background: var(--background-color);
  color: var(--text-color);
  font-family: 'Noto Sans', sans-serif;
  margin-bottom: 0; /* Asegúrate de que no haya margen inferior */
  padding-bottom: 0; /* Asegúrate de que no haya padding inferior */
}
</style>
