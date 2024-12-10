<template>
    <article id="about-us">
    <div style="text-align: left;">
      <h1>
        Sobre Nosotros
      </h1>
    </div>
      <div class="about-me-div">
        <p class="about-me-text">
          Somos Lorena y José y juntos formamos un equipo de 2 personas,
          <span class="highlight">Lorena es la que cuestiona todo</span> y
          <span class="highlight">José el que de alguna forma ya ha programado aquello</span>
          en algún otro lugar.<br /><br />
          Creemos que trabajar en equipo hace que seamos mucho más ágiles y efectivos. Nuestro
          método de trabajo incluye <span class="highlight">planificar, ejecutar y verificar</span>.
          Aunque no hemos realizado muchos proyectos juntos, tenemos experiencia en otros proyectos y somos versátiles y nos gusta aprender bien.<br /><br />
          Para nosotros no existe el hacer las cosas a medias y
          <span class="highlight">si para hacerlo perfecto hay que dar el 100%, aunque el viento vaya en contra, nosotros pondremos el 200%.</span>
        </p>
        <img src="../assets/images/sobre-nosotros-imagen.png" alt="Imagen de José" class="about-me-image" />
      </div>
    </article>
  </template>

  <script>
  export default {
    name: 'AboutUs',
  };
  </script>

  <style scoped>

.about-me-div {
    display: flex;
    flex-direction: row;
    min-width: 500px;
    justify-content: space-between;
    margin-bottom: 100px;
    margin-top: 30px;
  }

  .about-me-text {
    max-width: 70%;
    font-size: medium;
    text-align: left;
  }

  .about-me-image {
    width: 150px;
    height: 150px;
    object-fit: cover;
    border-radius: 50%;
    background-color: #f08cc38f;
    align-self: center;
    padding: 20px;
  }
  </style>
