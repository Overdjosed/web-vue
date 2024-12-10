<template>
    <footer class="footer">
        <div class="footer-content">
            <!-- Sección de Contacto -->
            <div class="contact-section">
                <h3>Contáctanos</h3>
                <ul class="contact-info">
                    <li>
                        <i class="fas fa-map-marker-alt"></i>
                        Calle Erase una vez<br />
                        en un universo muy muy lejano
                    </li>
                    <li>
                        <i class="fas fa-phone-alt"></i>
                        (+34) 670 123 456
                    </li>
                    <li>
                        <i class="fas fa-envelope"></i>
                        lorenayjosepotato@gmail.com
                    </li>
                </ul>
            </div>

            <!-- Sección de la Empresa -->
            <div class="company-section">
                <p>Lorena y Jose es propiedad de PSOE</p>
            </div>
        </div>

        <!-- Sección de Enlaces -->
        <div class="footer-links">
            <ul>
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Proyectos</a></li>
                <li><a href="#">Primer Curso</a></li>
                <li><a href="#">Segundo Curso</a></li>
                <li><a href="#">Contacta</a></li>
            </ul>
        </div>

        <!-- Sección de Derechos -->
        <div class="footer-bottom">
            <p>Lorena y Jose 2024 © · <a href="#">Aviso legal</a> · <a href="#">Privacidad</a> · <a href="#">Cookies</a></p>
        </div>
    </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
    background-color: #111;
    color: white;
    padding: 20px 50px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: 'Noto Sans', sans-serif;
}

.footer-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.contact-section {
    color: white;
    text-align: center;
}

.contact-section h3 {
    margin-bottom: 15px;
}

.contact-info {
    padding: 0;
}

.contact-info li {
    list-style: none;
    margin-bottom: 10px;
}

.contact-info i {
    margin-right: 8px;
    color: #f9c20b;
}

.company-section {
    text-align: center;
    margin-top: 20px;
}

.footer-links ul {
    display: flex;
    gap: 15px;
    margin: 20px 0;
    padding: 0;
    justify-content: center;
}

.footer-links li {
    list-style: none;
}

.footer-links a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

.footer-links a:hover {
    color: #f9c20b;
}

.footer-bottom {
    color: white;
    margin-top: 20px;
    text-align: center;
}

.footer-bottom a {
    color: white;
    margin-left: 10px;
    text-decoration: none;
}

.footer-bottom a:hover {
    color: #f9c20b;
}
</style>
