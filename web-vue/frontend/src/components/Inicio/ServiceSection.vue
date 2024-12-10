<template>
    <section class="services-section">
        <h2>Descubre nuestra Trayectoria</h2>
        <div class="service-grid">
            <a
                class="service-item"
                v-for="(service, index) in services"
                :key="index"
                :href="service.href"
            >
                <img :src="service.icon" :alt="service.alt" class="mini-icon" />
                <h3>{{ service.title }}</h3>
                <p>{{ service.description }}</p>
            </a>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue';

// Definimos la lista de servicios como un array de objetos
const services = ref([
    {
        icon: '../assets/icons/programming.svg',
        alt: 'Durante Nuestro Primer Curso',
        title: 'Primer Curso',
        description: 'Aprendizaje básico de la Programación.',
        href: '/proyect-page#primer-curso',
    },
    {
        icon: '../assets/icons/data.svg',
        alt: 'Durante Nuestro Segundo Curso',
        title: 'Segundo Curso',
        description: 'Entendimiendo de las Bases del Aprendizaje Automático.',
        href: '/proyect-page#segundo-curso',
    },
    {
        icon: '../assets/icons/rocket.svg',
        alt: 'Proyectos Individuales',
        title: 'Proyectos Individuales',
        description: 'Aplicacando conocimiento en el mundo real.',
        href: '/proyect-page',
    },
]);
</script>

<style scoped>
.services-section {
    text-align: center;
    padding: 50px 20px;
    margin-bottom: 150px;
    margin-top: 30px;
}

.services-section h2 {
    font-size: 2.5rem;
    margin-bottom: 60px;
    color: var(--text-color, #000);
}

.service-grid {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
}

.service-item {
    padding: 20px;
    text-decoration: none;
    transition: transform 0.3s ease;
}

.service-item:hover {
    transform: scale(1.2);
}

.service-item img.mini-icon {
    max-width: 300px;
    width: 60px;
    height: 60px;
    padding: 15px;
    background-color: var(--highlight-color);
    border-radius: 10px;
    text-align: center;
}

.service-item h3 {
    font-size: 1.5rem;
    margin-bottom: 10px;
    color: var(--text-color, #000);
}

.service-item p {
    font-size: 1rem;
    max-width: 300px;
    color: var(--secondary-text-color, #666);
}

/* Responsivo */
@media (max-width: 768px) {
    .service-grid {
        flex-direction: column;
        align-items: center;
    }

    .service-item {
        width: 80%;
    }
}
</style>
