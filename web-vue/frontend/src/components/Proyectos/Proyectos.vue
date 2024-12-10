<template>
  <Navbar_proyectos></Navbar_proyectos>
  <main>
    <!-- Campo de búsqueda -->
    <h1 id="titulo_proyecto">Proyectos</h1>

    <section id="contenedor-search">
      <h1><i class="icon-style material-icons-outlined">search</i> Buscador</h1>
      <label for="search">¿Qué quieres buscar? </label>
      <input type="text" id="search" v-model="searchQuery" @input="performSearch" placeholder="Buscar en proyectos y experiencias..." />
    </section>

    <!-- Experiencias del Primer Curso -->
    <section id="primer_curso" class="experience-container">
      <h1><i class="icon-style material-icons-outlined">work</i> Primer Curso</h1>
      <div v-for="experience in filteredExperiences" :key="experience.id" class="container">
        <div class="content-left">
          <div class="sticky-element">
            <span class="circle-marker">•</span>
            <h3 class="title">{{ experience.title }}</h3>
            <h4 class="subtitle">{{ experience.subtitle }}</h4>
            <time class="time-text">{{ experience.time }}</time>
          </div>
        </div>
        <div class="content-right">
          <p>{{ experience.description }}</p>
          <a :href="experience.link" class="link-button" target="_blank">
            Saber más
            <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M9 6l6 6l-6 6"></path>
            </svg>
          </a>
          <div class="button-container">
            <button @click="editExperience(experience)" class="edit-button"><i class="material-icons-outlined">edit</i></button>
            <button @click="deleteExperience(experience.id)" class="delete-button"><i class="material-icons-outlined">delete</i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Proyectos del Segundo Curso -->
    <section id="segundo_curso" class="experience-container">
      <h1><i class="icon-style material-icons-outlined">code</i> Segundo Curso</h1>
      <div v-for="project in filteredProjects" :key="project.id" class="container">
        <div class="content-left">
          <div class="sticky-element">
            <span class="circle-marker">•</span>
            <img :src="project.image || '/default-image.png'" :alt="project.title" class="project-image">
          </div>
        </div>
        <div class="content-right">
          <h2>{{ project.title }}</h2>
          <h4 class="subtitle">{{ project.subtitle }}</h4>
          <time class="time-text">{{ project.time }}</time>
          <p>{{ project.description }}</p>
          <a :href="project.link" class="link-button" target="_blank">
            Saber más
            <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M9 6l6 6l-6 6"></path>
            </svg>
          </a>
          <div class="button-container">
            <button @click="editProject(project)" class="edit-button"><i class="material-icons-outlined">edit</i></button>
            <button @click="deleteProject(project.id)" class="delete-button"><i class="material-icons-outlined">delete</i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- Modal de autenticación -->
    <div v-if="showAuthModal" class="modal-overlay">
      <div class="modal-content">
        <h2>Verificación de Usuario</h2>
        <form @submit.prevent="authenticateUser">
          <label class="auth-username" for="username">Usuario</label>
          <input type="text" id="username" v-model="authForm.username" required />

          <label class="auth-pw" for="password">Contraseña</label>
          <input type="password" id="password" v-model="authForm.password" required />

          <button type="submit">Verificar</button>
        </form>
        <p v-if="authError" class="error">{{ authError }}</p>
      </div>
    </div>

    <!-- Formulario para añadir o modificar experiencias o proyectos -->
    <section ref="formSection">
      <h1 id="formulario"><i class="icon-style material-icons-outlined">add</i> Añadir o Modificar contenido</h1>
      <form @submit.prevent="initiateAuth">
        <div>
          <label for="title">Título <span class="highlight">(obligatorio)</span></label>
          <span class="circle-marker">•</span>
          <input type="text" id="title" v-model="form.title" required>
        </div>
        <div>
          <label for="subtitle">Subtítulo</label>
          <span class="circle-marker">•</span>
          <input type="text" id="subtitle" v-model="form.subtitle">
        </div>
        <div>
          <label for="time">Fecha</label>
          <span class="circle-marker">•</span>
          <input type="text" id="time" v-model="form.time">
        </div>
        <div>
          <label for="description">Descripción <span class="highlight">(obligatorio)</span></label>
          <span class="circle-marker">•</span>
          <textarea id="description" v-model="form.description" required></textarea>
        </div>
        <div>
          <label for="link">Enlace</label>
          <span class="circle-marker">•</span>
          <input type="text" id="link" v-model="form.link">
        </div>
        <div>
          <label for="type">Añadir a:</label>
          <span class="circle-marker">•</span>
          <select v-model="form.type" required>
            <option value="Primer Curso">Primer Curso</option>
            <option value="projects">Segundo Curso</option>
          </select>
        </div>
        <button type="submit">{{ editing ? 'Guardar Cambios' : 'Añadir' }}</button>
      </form>
    </section>
  </main>
</template>

<script>
import Navbar_proyectos from './Navbar_proyectos.vue';
import { getProjects, createProject, updateProject, deleteProject, getExperiences, createExperience, updateExperience, deleteExperience } from '@/plugins/axios';

export default {
  name: 'Proyectos',
  components: {
    Navbar_proyectos,
  },
  data() {
    return {
      experiences: [],
      projects: [],
      searchQuery: '',
      form: {
        title: '',
        time: '',
        description: '',
        link: '',
        type: 'Primer Curso',
      },
      editing: false,
      editingId: null,
      searchResultsExperiences: [],
      searchResultsProjects: [],
      showAuthModal: false,
      authError: '',
      authForm: {
        username: '',
        password: ''
      },
      failedAttempts: 0,
      maxAttempts: 3,
    };
  },
  mounted() {
    this.loadExperiences();
    this.loadProjects();
  },
  computed: {
    filteredExperiences() {
      return this.searchQuery ? this.searchResultsExperiences : this.experiences;
    },
    filteredProjects() {
      return this.searchQuery ? this.searchResultsProjects : this.projects;
    },
  },
  methods: {
    async loadExperiences() {
      const response = await getExperiences();
      this.experiences = response.data;
    },
    async loadProjects() {
      const response = await getProjects();
      this.projects = response.data;
    },
    async deleteExperience(id) {
      await deleteExperience(id);
      this.experiences = this.experiences.filter(experience => experience.id !== id);
    },
    async deleteProject(id) {
      await deleteProject(id);
      this.projects = this.projects.filter(project => project.id !== id);
    },
    editExperience(experience) {
      this.form = { ...experience, type: 'Primer Curso' };
      this.editing = true;
      this.editingId = experience.id;
      this.scrollToForm();
    },
    editProject(project) {
      this.form = { ...project, type: 'projects' };
      this.editing = true;
      this.editingId = project.id;
      this.scrollToForm();
    },
    performSearch() {
      this.searchResultsExperiences = this.experiences.filter(experience =>
        experience.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
        experience.description.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
      this.searchResultsProjects = this.projects.filter(project =>
        project.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
        project.description.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    initiateAuth() {
      this.showAuthModal = true;
      this.authError = '';
      this.failedAttempts = 0;
    },
    async authenticateUser() {
      try {
        const response = await getProjects({
          auth: {
            username: this.authForm.username,
            password: this.authForm.password
          }
        });
        if (response.status === 200) {
          this.showAuthModal = false;
          this.authError = '';
          this.submitForm();
        }
      } catch {
        this.failedAttempts++;
        this.authError = 'Usuario o contraseña incorrectos';
        if (this.failedAttempts >= this.maxAttempts) {
          this.resetForm();
          this.showAuthModal = false;
          this.authError = '';
        }
      }
    },
    async submitForm() {
      const updatedData = {
        title: this.form.title,
        subtitle: this.form.subtitle || '',
        time: this.form.time || 'Sin fecha',
        description: this.form.description,
        link: this.form.link || 'http://localhost:5173/',
      };

      try {
        if (this.editing) {
          if (this.form.type === 'Primer Curso') {
            const response = await updateExperience(this.editingId, updatedData);
            const index = this.experiences.findIndex(exp => exp.id === this.editingId);
            this.experiences.splice(index, 1, response.data);
          } else {
            const response = await updateProject(this.editingId, updatedData);
            const index = this.projects.findIndex(proj => proj.id === this.editingId);
            this.projects.splice(index, 1, response.data);
          }
        } else {
          if (this.form.type === 'Primer Curso') {
            const response = await createExperience(updatedData, this.authForm.username, this.authForm.password);
            this.experiences.push(response.data);
          } else {
            const response = await createProject(updatedData, this.authForm.username, this.authForm.password);
            this.projects.push(response.data);
          }
        }
        this.resetForm();
      } catch (error) {
        console.error("Error al añadir o actualizar el contenido:", error);
      }
    },
    resetForm() {
      this.form = { title: '', subtitle: '', time: '', description: '', link: '', type: 'Primer Curso' };
      this.editing = false;
      this.editingId = null;
    },
    scrollToForm() {
      this.$nextTick(() => {
        this.$refs.formSection.scrollIntoView({ behavior: 'smooth' });
      });
    },
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  text-align: center;
  justify-content: center;
  align-items: center;
  z-index: 9999; /* Aumenta el valor del z-index */
}
.modal-content {
  background: var(--background-color);
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  text-align: center;
}
.error {
  color: red;
}
.auth-pw {
  margin-top: 10px;
  color: var(--text-color);
}

.auth-username {
  margin-top: 10px;
  color: var(--text-color);
}

#search {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 2px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
}

#contenedor-search{
  text-align: left;
  margin-bottom: 20px; /* Espaciado debajo */
  display: block; /* Asegura que sea un bloque que ocupe todo el ancho */
  width: 100%;
}

/* Contenedores, incluse: primer_curso y segundo_curso */

.experience-container {
    margin-top: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
}

/* Cada punto de primer curso y segundo curso */
.container {
  display: grid;
  grid-template-columns: 2fr 3fr;
  gap: 20px;
  padding-bottom: 50px;
  position: relative;
  margin: 0 50px;
}

.container::before {
  content: '';
  position: absolute;
  left: -35px;
  height: 100%;
  width: 2px;
  background-color: var(--timeline-color);
}

.content-left {
    position: relative;
    padding-bottom: 50px;
}

.content-right {
    display: flex;
    flex-direction: column;
    gap: 0.1px;
    padding-bottom: 20px;
    color: var(--secondary-text-color);
}

.link-button {
    align-items: center;
    font-size: 1.125rem;
    font-weight: 500;
    color: var(--highlight-color,yellow);
    text-decoration: none;
}

.link-button:hover {
    color: #826503;
}

.sticky-element {
    position: sticky;
    top: 0;
}

.circle-marker {
position: absolute;
left: -42px;
font-size: 40px;
color: #facc15;
border-radius: 50%;
}

.title {
font-size: 1.5rem;
font-weight: bold;
color: var(--highlight-color, yellow);
}

.subtitle {
font-size: 1.25rem;
font-weight: 600;
color: var(--on-background-color-secondary);
}

.time-text {
font-size: 0.875rem;
opacity: 0.6;
color: var(--text-color);
}
main {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: auto;
      padding: 0 20px;
      max-width: 80%;
      margin-bottom: 100px;
    }

.icon {
  margin-left: 5px;
  width: 20px;
  height: 20px;
  vertical-align: middle;
}

.icon-style {
  vertical-align: middle;
}

.project-image {
  flex:1;
  width: 100%;
  height: auto;
  max-height: 280px;
  border-radius: 20px;
}

ul li a {
  color: var(--button-border-color, rgba(46, 177, 221));
  font-weight: 600;
  padding: 10px;
  padding-top: 7px;
  padding-bottom: 7px;
  font-size: medium;
}

form {
  background-color: var(--background-color);
  padding: 20px;
  max-width: 100%;
  margin: 20px auto;
  color: var(--text-color);
  text-align: center;
}

form label {
  display: block;
  margin-bottom: 7px;
  font-weight: bold;
  color: var(--formulario-color);
}

form input[type="text"],
form textarea,
form select {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: var(--formulario-entradas-border);
  border-radius: 5px;
  background-color: var(--background-color-formulario_entradas);
  color: var(--text-color);
  font-size: 1rem;
}

form input[type="text"]:focus,
form textarea:focus,
form select:focus {
  outline: none;
  border-color: rgb(237, 113, 134);
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.55);
  background-color: var(--background-color-formulario_entradas); /* Mantener el color de fondo */
}

form input[type="password"],
form textarea,
form select {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: var(--formulario-entradas-border);
  border-radius: 5px;
  background-color: var(--background-color-formulario_entradas);
  color: var(--text-color);
  font-size: 1rem;
}

form input[type="text"]:focus,
form textarea:focus,
form select:focus {
  outline: none;
  border-color: rgb(237, 113, 134);
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.55);
}

form button {
  background-color: var(--button-background-color-formulario);
  color: #ffffff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.2rem;
  transition: background-color 0.4s ease, color 0.3s ease;
  width: 150px;
}

form button:hover {
  background-color: var(--button-color-hover-formulario);
}

form div {
  margin-bottom: 15px;
}

form {
  position: relative;
  margin: 0 50px;
}

form::before{
  content: '';
  position: absolute;
  left: -35px;
  height: 100%;
  width: 2px;
  background-color: var(--timeline-color);
}

.highlight {
  color: var(--highlight-color, #ffff00);
}

option {
  background-color: #fff;
  color: #333;
}

#titulo_proyecto {
  font-size: 4.125rem;
  text-align: left;
  display: block;
  width: 100%;
}

.button-container {
  display: flex;
  justify-content: flex-end;
  gap: 5px;
  width: 100%;
}

.delete-button, .edit-button {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #ff4d4d;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  position: relative;
}

.delete-button {
  background-color: #3dd4f6;
}

.delete-button:hover {
  background-color: #ff1a1a;
}

.edit-button {
  background-color: #faa038;
}

.edit-button:hover {
  background-color: #095210;
}

.edit-button:hover::after {
  content: "Modificar";
  position: absolute;
  top: 100%;
  right: 100%;
  transform: translate(5px, -50%);
  background-color: #09521069;
  color: white;
  padding: 10%;
  border-radius: 5px;
  white-space: nowrap;
  font-size: 14px;
}

.delete-button:hover::after {
  content: "Eliminar";
  position: absolute;
  top: 100%;
  left: 100%;
  transform: translate(5px, -50%);
  background-color: #ff1a1a7d;
  color: white;
  padding: 10%;
  border-radius: 5px;
  white-space: nowrap;
  font-size: 14px;
}
</style>
