import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'; // Importa el archivo de rutas

const app = createApp(App);

app.use(router); // Usa Vue Router
app.mount('#app');