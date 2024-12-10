<template>
    <div class="homepage">
        <!-- Sección superior con el logo y nombres -->
        <section class="intro">
            <div class="logo-container">
                <!-- Logo inventado -->
                <h1>¿Quieres unirte a nuestro equipo? Escribe un proyecto en nuestra página web.</h1>
            </div>
            <router-link to="/proyect-page#formulario" class="project-button">
                <button class="project-button">
                    ESCRIBIR PROYECTO
                </button>
            </router-link>
            </section>
    </div>
</template>

<script setup>
</script>

<style scoped>
/* Estilos de la página principal */
.homepage {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 30px;
    padding-bottom: 30px;
    width: 100%;
    height: 30vh;
    background-color: var(--highlight-color);
}

/* Sección de introducción */
.intro {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
}

.logo-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 30px;
}

.logo svg {
    margin-bottom: 10px;
}

.intro h1 {
    font-size: 2.5rem;
    text-align: center;
    color: #000000;

}

.project-button {
    display: inline-block;
    background-color: #ffffff;
    color: #000000;
    font-weight: bold;
    border-radius: 20px;
    font-size: 1rem;
    text-decoration: none;
    transition: background-color 0.3s ease;
}

.project-button:hover {
    background-color: #ff006a;
}
</style>
