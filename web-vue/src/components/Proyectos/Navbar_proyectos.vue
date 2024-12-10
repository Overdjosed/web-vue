<template>
    
  <header class="navbar" :class="{ sticky: isSticky }">
    <nav>
      <ul class="menu">
        <li><router-link to="/">Home</router-link></li>
        <li><a class="titimepregunto" href="#primer_curso">Primero</a></li>
        <li><a class="titimepregunto" href="#segundo_curso">Segundo</a></li>
        <li><a class="titimepregunto" href="#formulario">Añadir más</a></li>
        <!-- TODO: Añadir enlace a buscador -->
        <li><a class="titimepregunto" href="#contenedor-search"><i class="icon-style material-icons-outlined">search</i> </a></li>
        <li>
          <button class="modo_iluminacion" @click="toggleThemeMode">
            <i class="icon_modo_iluminacion material-icons-outlined">{{ themeIcon }}</i>
          </button>
        </li>
      </ul>
      </nav>
    </header>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isSticky: false,
        isDarkMode: false,
        themeIcon: "wb_sunny", // Inicia con el icono de sol (modo claro)
      };
    },
    mounted() {
      // Añadir los listeners para el efecto sticky y la navegación suave
      window.addEventListener("scroll", this.checkStickyHeader);
      this.setupSmoothScroll();
  
      // Cargar el tema guardado en localStorage
      const savedTheme = localStorage.getItem("theme");
      const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
      this.isDarkMode = savedTheme === "dark" || (!savedTheme && systemPrefersDark);
      this.updateThemeIcon();
    },
    methods: {
      checkStickyHeader() {
        this.isSticky = window.scrollY > 40;
      },
      toggleThemeMode() {
        this.isDarkMode = !this.isDarkMode;
        this.updateThemeIcon();
        document.documentElement.setAttribute("data-theme", this.isDarkMode ? "dark" : "light");
        localStorage.setItem("theme", this.isDarkMode ? "dark" : "light");
      },
      updateThemeIcon() {
        this.themeIcon = this.isDarkMode ? "dark_mode" : "wb_sunny";
      },
      setupSmoothScroll() {
        const headerLinks = document.querySelectorAll(".titimepregunto");
        headerLinks.forEach((link) => {
          link.addEventListener("click", (event) => {
            event.preventDefault();
            const targetId = link.getAttribute("href").replace("#", "");
            document.getElementById(targetId).scrollIntoView({ behavior: "smooth" });
          });
        });
      },
    },
    beforeDestroy() {
      // Eliminar listeners para evitar memory leaks
      window.removeEventListener("scroll", this.checkStickyHeader);
    },
  };
  </script>
  
  <style scoped>
  
  header {
    position: sticky;
    top: 20px; /* Fija el navbar en la parte superior */
    z-index: 1;
    max-width: 580px;
    margin: auto;
}

.navbar {
    background-color: transparent;
    border-radius: 40px;
    margin: auto; /* Esto centra el navbar horizontalmente */
    transition: background-color 0.3s ease, box-shadow 0.3s ease, backdrop-filter 0.3s ease, transform 0.3s ease;
    justify-content: space-between;
}

.navbar.sticky {
    background-color: var(--header-sticky-background-color); /* Fondo grisáceo cuando es sticky */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4); /* Sombra cuando es sticky */
    backdrop-filter: blur(20px); /* Desenfoque del fondo */
    transform: translateY(10px); /* Desplazamiento hacia abajo cuando es sticky */
}

/*Con esto le das el estilo que quieres a la lista menu */
.menu{
    gap: 10px;
    list-style: none;
    margin-left: -40px;
    display: flex;
    align-items: center;
    /* align eje y */
    justify-content: center;
    /* justify eje x */
}

.menu li a {
    color: var(--text-color);
    font-weight: 600;
    text-decoration: none;
    padding: 5px;
    padding-top: 7px;
    padding-bottom: 7px;
    font-size: medium;
}

.menu li a:hover {
    color: rgb(46, 177, 221); /* Cambia el color del texto a azul cuando se pasa el mouse */
}

.modo_iluminacion {
    background-color: transparent;
    color: var(--text-color);
    padding: 5px;
    border: none;
    vertical-align: middle;
}

.modo_iluminacion:hover {
    color: rgb(46, 177, 221); /* Cambia el color del texto a rojo cuando se pasa el mouse */
}

.highlight {
    color: var(--highlight-color); /* Cambia a naranja en modo light, por defecto amarillo en dark */
}
  
</style>
  