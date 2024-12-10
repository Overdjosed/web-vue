import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/Inicio/HomePage.vue'; // Componente de tu página principal
import NewPage from '../components/Proyectos/Proyectos.vue'; // La nueva página que quieres crear
// import App from '../App.vue'; // Importa el componente App

const routes = [
  { path: '/', component: HomePage }, // Ruta para la página principal
  { path: '/proyect-page', component: NewPage }, // Ruta para la nueva página
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
