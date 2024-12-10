<template>
  <Navbar></Navbar>
  <div>
    <main>
      <div class="experience-container">
        <div class="container">
          <div class="text-container">
            <h1 style="margin-bottom: 50px; margin-top: 150px;">Somos Lorena y Jose</h1>
            <h2 style="margin-bottom: 30px;">Actualmente cursando <span class="highlight">3º curso de Grado en Ciencia e Ingeniería de Datos</span> en la Universidad Autónoma de Madrid, España.</h2>
            <p>
              Somos un <span class="highlight">equipo especializado en el análisis de datos</span>, programación concurrente, diseño de software, y más.
              Nos dedicamos a encontrar soluciones personalizadas para cada necesidad, aplicando tecnologías de vanguardia
              como <span class="highlight">Python, Java, React y muchas más.</span>
            </p>
            <p>
              Contamos con amplia experiencia en el desarrollo de aplicaciones de análisis de datos, <span class="highlight">utilizando bases de
              datos relacionales y no relacionales</span> como PostgreSQL y MongoDB. Nuestro enfoque se centra en la eficiencia,
              escalabilidad y calidad.
            </p>
            <div class="icon-section">
              <IconGrid :icons="iconList" />
            </div>
            <div class="button-container">
              <a href="/proyect-page" class="btn-call-to-action">Conoce más</a>
            </div>
          </div>
          <div class="image-container">
            <img :src="sobreNosotrosImagen" alt="Foto del equipo" />
          </div>
        </div>
      </div>
      <ServiceSection />
      <div class="about-us">
        <AboutUs />
      </div>
    </main>
    <Intro />
    <div id="contacto">
      <Footer />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import sobreNosotrosImagen from '/assets/images/imagenproyectos.png';
import IconGrid from '../Inicio/IconGrid.vue';
import ServiceSection from '../Inicio/ServiceSection.vue';
import Intro from '../Inicio/Intro.vue';
import Footer from '../Inicio/Footer.vue';
import Navbar from '../Global/Navbar.vue';
import AboutUs from '../Inicio/AboutUs.vue';
const isDarkMode = ref(false);

if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  isDarkMode.value = true;
}

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  isDarkMode.value = e.matches;
});

import { computed } from 'vue';
const astroIcon = computed(() => isDarkMode.value ? '../assets/icons/Astro_dark.svg' : '../assets/icons/Astro_light.svg');

const iconList = ref([
  { src: '../assets/icons/python.svg', alt: 'Python' },
  { src: '../assets/icons/react.svg', alt: 'React' },
  { src: '../assets/icons/java.svg', alt: 'Java' },
  { src: '../assets/icons/mongodb.svg', alt: 'MongoDB' },
  { src: '../assets/icons/postgresql.svg', alt: 'PostgresSQL' },
  { src: astroIcon.value, alt: 'Astro' },
  { src: '../assets/icons/gdsc.svg', alt: 'GDSC' },
  { src: '../assets/icons/vueuse.svg', alt: 'VueUse' },
]);

</script>

<style scoped>
/* Estructura principal */
main {
  max-width: 1700px; /* Ajustar para que ocupe más espacio */
  margin: auto;
  max-width: 80%;
  text-align: center;
}

/* Perfil */
.perfil {
  margin-top: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.perfil img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  margin-right: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  object-fit: cover;
  background-color: rgba(46, 177, 221, 0.8);
}

.experience-container {
  margin-top: 20px;
  padding: 40px;
  flex-direction: column;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1600px; /* Ajuste para que ocupe más espacio */
  margin: 0 auto;
  margin-bottom: 110px;
}

.text-container {
  flex: 1.5; /* Para que el texto ocupe más espacio */
  padding-right: 20px;
  text-align: left;
}

.image-container {
  flex: 1;
}

.image-container img {
  background-color: rgba(46, 177, 221);
  width: 300px;
  height: auto;
  border-radius: 50%;
  object-fit:cover;
}

.button-container {
  display: flex;
  justify-content: center; /* Centra horizontalmente */
  align-items: center; /* Centra verticalmente si es necesario */
}

.btn-call-to-action {
  display: inline-block;
  background-color: var(--highlight-color);
  color: #030303;
  font-weight: 700;
  margin-top: 10px;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 1rem;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.btn-call-to-action:hover {
  background-color: var(--button-hover-background-color);
}

/* Sección de iconos */
.icon-section {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.icon-section IconGrid {
  display: flex;
  justify-content: space-around;
  gap: 15px;
  padding: 10px;
}

.icon-section IconGrid .icon img {
  width: 30px;
  height: 30px;
}

@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }

  .text-container {
    text-align: center;
    padding-right: 0;
  }

  .image-container img {
    width: 200px;
  }
}
</style>
