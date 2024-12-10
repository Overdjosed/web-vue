# Inicializar backend y frontend

### Terminal 1:

- Crea un nuevo entorno virtual desde la carpeta Backend:

    ```bash
    python -m venv venv
    ```

- Activa el nuevo entorno virtual desde la carpeta Backend:

    ```bash
    # Windows
    venv\Scripts\activate

    # MacOS/Linux
    source venv/bin/activate
    ```

- Instala Flask y otras dependencias desde la carpeta Backend:

    ```bash
    pip install flask flask_sqlalchemy flask_cors flask-httpauth
    ```

- Ejecuta `app.py` desde la carpeta web-vue:

    ```bash
    python backend/app.py
    ```

### Terminal 2:

- Ejecuta el comando desde la carpeta web-vue
```bash
    npm install
```

- Ejecuta el siguiente comando desde la carpeta web-vue
```bash
    npm run dev
```

# Autenticación

## Implementación de Autenticación Simple en nuestro proyecto
Para crear proyectos o modificarlos en la página web el **usuario** es: **'admin'** y la **contraseña** será: **'admin'**

2 Casos:
- Si todo funciona correctamente, el proyecto se añadirá y se limpiarán los campos.
- Si se falla en la contraseña o usuario, aparecerá un error en la web indicando que no se ha podido añadir el contenido y se mantendrán los campos rellenados para volver a intentar la petición.

# Tipos de Autenticación

La autenticación es el proceso de verificar la identidad de un usuario o sistema antes de permitirle acceso a un recurso. Existen diferentes tipos de autenticación, cada uno con sus ventajas y limitaciones.

## 1. Autenticación basada en contraseñas

El método más común, en el que los usuarios proporcionan una combinación de nombre de usuario y contraseña. Aunque es fácil de implementar, las contraseñas pueden ser vulnerables a ataques de fuerza bruta, phishing y otros tipos de hacking.

- **Ejemplos**: Iniciar sesión con usuario y contraseña en una aplicación.
- **Limitaciones**: Las contraseñas débiles o reutilizadas pueden ser comprometidas fácilmente.

## 2. Autenticación basada en tokens

En este método, un usuario se autentica inicialmente y recibe un token (como un JWT, o JSON Web Token) que luego se usa para autenticar sus solicitudes sin tener que enviar sus credenciales repetidamente.

- **Ejemplos**: Autenticación de API con tokens.
- **Ventajas**: Seguridad mejorada al no tener que enviar credenciales con cada solicitud.
- **Limitaciones**: Si un token es robado, puede ser utilizado para acceder hasta que expire o sea revocado.

## 3. Autenticación multifactor (MFA)

Este método requiere dos o más factores de autenticación para verificar la identidad del usuario. Los factores pueden incluir algo que el usuario sabe (contraseña), algo que posee (token, teléfono), y algo que es (huella digital, reconocimiento facial).

- **Ejemplos**: Iniciar sesión con contraseña + código enviado al teléfono.
- **Ventajas**: Seguridad significativamente mejorada.
- **Limitaciones**: Puede ser más complicado y lento para los usuarios.

## 4. Autenticación biométrica

Utiliza características físicas o de comportamiento para autenticar al usuario, como huellas dactilares, reconocimiento facial, escaneo de iris, o incluso patrones de voz.

- **Ejemplos**: Desbloqueo con huella digital o reconocimiento facial en dispositivos móviles.
- **Ventajas**: Difícil de falsificar.
- **Limitaciones**: Privacidad, costos de implementación y posibilidad de errores en la verificación.

## 5. Autenticación basada en certificados

Utiliza certificados digitales para autenticar a un usuario o dispositivo. Los certificados son emitidos por una autoridad de certificación (CA) y son difíciles de falsificar.

- **Ejemplos**: Acceso seguro a redes mediante certificados.
- **Ventajas**: Alta seguridad y autenticación sin necesidad de contraseñas.
- **Limitaciones**: Complejidad en la gestión de certificados y dependencias en la infraestructura PKI (Infraestructura de Clave Pública).

## 6. Autenticación basada en preguntas de seguridad

Requiere que los usuarios respondan preguntas de seguridad, generalmente configuradas por el propio usuario. Este método se usa a menudo como autenticación secundaria o como método de recuperación de cuentas.

- **Ejemplos**: Preguntas como "¿Cuál es el nombre de tu primera mascota?" al intentar recuperar una contraseña.
- **Ventajas**: Fácil de implementar.
- **Limitaciones**: No es muy seguro, ya que la información puede ser conocida o adivinada por otras personas.

## 7. Autenticación OAuth

OAuth es un estándar para la autorización de acceso delegada, que permite a los usuarios dar acceso limitado a su información en una aplicación sin revelar sus credenciales.

- **Ejemplos**: Iniciar sesión en aplicaciones usando cuentas de Google, Facebook o Twitter.
- **Ventajas**: Seguridad y comodidad al no necesitar compartir la contraseña con cada aplicación.
- **Limitaciones**: Dependencia en un tercero y posibles problemas de privacidad.

## 8. Autenticación basada en la ubicación

Este método utiliza la ubicación del usuario para autenticar. Puede ser una autenticación adicional (como en la MFA) o un requisito para acceder a ciertos recursos.

- **Ejemplos**: Acceso permitido solo si el usuario está dentro de una red específica o ubicación geográfica.
- **Ventajas**: Útil como segundo factor en MFA.
- **Limitaciones**: No siempre preciso y puede requerir permisos de ubicación.

---
## Backend

### Explicacion de cada archivo (idea general de porque existe cada cosa)

Explicación de cada uno de los archivos de la carpeta `backend` y su propósito en el proyecto. Estos archivos están organizados para que el proyecto funcione correctamente, tanto en el frontend (interfaz de usuario) como en el backend (servidor).

### 1. **app.py**

- **Qué es:** Este es el archivo principal del servidor backend.
- **Para qué sirve:** Es el punto de entrada para ejecutar el backend de la aplicación. En este archivo está configurado el servidor usando Flask, que es un framework para crear aplicaciones web en Python.
- **Qué hace:**
    - Configura el servidor y define las "rutas" o URLs que pueden usarse para acceder a diferentes partes de la aplicación desde el frontend.
    - Define cómo se manejan los datos de los "proyectos" y "experiencias", como leer (GET), crear (POST), actualizar (PUT) y eliminar (DELETE) datos.
    - Se conecta a la base de datos para gestionar esta información.
- **Por qué es necesario:** Este archivo permite que el frontend se comunique con el backend. Al correr `app.py`, se inicia el servidor que escucha y responde a las solicitudes del frontend.

### 2. **experienceData.json y projectsData.json**

- **Qué son:** Son archivos en formato JSON (JavaScript Object Notation), que es una forma de estructurar datos en texto.
- **Para qué sirven:**
    - Contienen datos de ejemplo iniciales para "experiencias" y "proyectos", respectivamente.
    - Estos archivos se usan para cargar datos en la base de datos cuando el servidor se ejecuta por primera vez, en caso de que no haya datos ya almacenados.
- **Qué hacen:** Cuando el servidor se inicia, `app.py` puede leer estos archivos JSON y copiar su contenido en la base de datos si aún no hay información cargada.
- **Por qué son necesarios:** Facilitan el proceso de inicialización de la base de datos con algunos datos básicos sin necesidad de agregarlos manualmente. Esto es especialmente útil para pruebas y desarrollo.

### 3. **models.py**

- **Qué es:** Este archivo define el "modelo de datos" para la base de datos usando SQLAlchemy, que es una biblioteca en Python para trabajar con bases de datos.
- **Para qué sirve:**
    - Define cómo se estructura cada "proyecto" y "experiencia" en la base de datos. Cada "modelo" en este archivo representa una tabla en la base de datos.
- **Qué hace:**
    - Crea las tablas `projects` y `experiences` en la base de datos con campos específicos como `title`, `description`, `time`, entre otros.
    - Permite al servidor (definido en `app.py`) entender cómo interactuar con la base de datos para guardar, leer, actualizar o eliminar registros.
- **Por qué es necesario:** Sin este archivo, el servidor no sabría cómo almacenar o recuperar los datos de los proyectos y experiencias en la base de datos. `models.py` actúa como una "hoja de instrucciones" para la base de datos.

### 4. **requirements.txt**

- **Qué es:** Este archivo lista todas las bibliotecas o paquetes de Python que el proyecto necesita para funcionar.
- **Para qué sirve:** Es una referencia para que otros desarrolladores (o tú mismo en otro momento) sepan qué bibliotecas instalar para que el proyecto funcione correctamente.
- **Qué hace:** Cuando alguien usa el comando `pip install -r requirements.txt`, se instalan todas las bibliotecas necesarias (como Flask, SQLAlchemy, etc.) en el entorno donde se ejecuta el proyecto.
- **Por qué es necesario:** Garantiza que todos los que trabajen en el proyecto usen las mismas versiones de las bibliotecas, lo que ayuda a evitar problemas de compatibilidad.

### 5. **pycache**

- **Qué es:** Esta es una carpeta generada automáticamente por Python.
- **Para qué sirve:**
    - Contiene archivos de caché (`.pyc`) que son versiones "compiladas" de los archivos Python.
- **Qué hace:** Ayuda a que Python ejecute el código más rápido, ya que no necesita volver a compilar los archivos cada vez que se ejecuta el servidor.
- **Por qué es necesario:** Aunque no es esencial para el funcionamiento, mejora la eficiencia de Python. Sin embargo, esta carpeta se genera automáticamente y se puede borrar sin afectar el código.

### 6. **venv**

- **Qué es:** Es un entorno virtual que contiene una instalación aislada de Python y sus bibliotecas.
- **Para qué sirve:**
    - Permite que el proyecto tenga sus propias versiones de las bibliotecas, sin interferir con las versiones globales de Python en tu sistema.
- **Qué hace:**
    - Al activar este entorno virtual (por ejemplo, con `source venv/bin/activate` en terminales de Linux o `venv\\Scripts\\activate` en Windows), todas las instalaciones de paquetes y ejecuciones de Python se hacen dentro de este entorno.
- **Por qué es necesario:**
    - Mantiene el proyecto organizado y evita problemas de compatibilidad con otras versiones de bibliotecas que podrían estar instaladas globalmente en el sistema.


## Frontend

### Proyectos.vue

### **Parte 1: La Estructura del Template (HTML)**

Este código Vue usa el formato de plantilla (template) para crear la estructura de la página web. Dentro de la etiqueta `<template>`, se define el HTML que se mostrará en la página.

### **1. Navbar**

```html
<Navbar_proyectos></Navbar_proyectos>

```

Aquí se incluye un componente llamado `Navbar_proyectos`. Este componente probablemente sea la barra de navegación en la parte superior de la página.

### **2. Título Principal**

```html
<h1 id="titulo_proyecto">Proyectos</h1>
```

Muestra el título "Proyectos" en la parte superior de la página.

### **3. Sección de Búsqueda**

```html
<section id="contenedor-search">
  <h1><i class="icon-style material-icons-outlined">search</i> Buscador</h1>
  <label for="search">¿Qué quieres buscar? </label>
  <input type="text" id="search" v-model="searchQuery" @input="performSearch" placeholder="Buscar en proyectos y experiencias..." />
</section>

```

Esta sección permite al usuario buscar proyectos o experiencias. El campo de entrada (`<input>`) está enlazado con `v-model="searchQuery"`, lo que significa que cualquier cosa que el usuario escriba se guardará en la variable `searchQuery`. El evento `@input="performSearch"` ejecuta la función `performSearch` cada vez que el usuario escribe algo, haciendo que la búsqueda sea dinámica.

---

### **Parte 2: Listado de Experiencias y Proyectos**

Aquí se muestran dos secciones principales: una para las "Experiencias del Primer Curso" y otra para los "Proyectos del Segundo Curso".

### **1. Experiencias del Primer Curso**

```html
<section id="primer_curso" class="experience-container">
  <h1><i class="icon-style material-icons-outlined">work</i> Primer Curso</h1>
  <div v-for="experience in filteredExperiences" :key="experience.id" class="container">
    <!-- Contenido de la experiencia -->
  </div>
</section>

```

Usa un bucle (`v-for`) para mostrar todas las experiencias de la lista `filteredExperiences`. Cada experiencia contiene su título, subtítulo, fecha y descripción, y un botón "Saber más" que dirige al enlace de la experiencia. Los botones "Modificar" y "Eliminar" también están presentes para cada experiencia, permitiendo editarlos o eliminarlos.

### **2. Proyectos del Segundo Curso**

```html
<section id="segundo_curso" class="experience-container">
  <h1><i class="icon-style material-icons-outlined">code</i> Segundo Curso</h1>
  <div v-for="project in filteredProjects" :key="project.id" class="container">
    <!-- Contenido del proyecto -->
  </div>
</section>

```

Funciona igual que la sección de "Primer Curso", pero en lugar de mostrar experiencias, muestra los proyectos en `filteredProjects`.

Los botones "Modificar" y "Eliminar" también están aquí. Cuando se hace clic en "Modificar", se activa la función `editProject`, y cuando se hace clic en "Eliminar", se activa `deleteProject`. Estas funciones interactúan con el backend.

---

### **Parte 3: Formulario de Añadir o Modificar Contenido**

```html
<section ref="formSection">
  <h1 id="formulario"><i class="icon-style material-icons-outlined">add</i> Añadir o Modificar contenido</h1>
  <form @submit.prevent="submitForm">
    <!-- Campos de entrada para el formulario -->
    <button type="submit">{{ editing ? 'Guardar Cambios' : 'Añadir' }}</button>
  </form>
</section>

```

Este formulario permite al usuario añadir una nueva experiencia o proyecto, o modificar uno existente. Dependiendo de si `editing` es `true` o `false`, el botón cambiará su texto a "Guardar Cambios" o "Añadir".

- **`@submit.prevent="submitForm"`**: Previene el comportamiento por defecto de envío de formulario y ejecuta la función `submitForm`.

### Campos del Formulario:

Cada campo en el formulario (`Título`, `Subtítulo`, `Fecha`, etc.) está enlazado con el objeto `form` en los datos. Los datos que el usuario introduce en el formulario se almacenan automáticamente en este objeto.

---

### **Parte 4: Script (JavaScript)**

En esta sección, el comportamiento y la lógica de la página están definidos. El código incluye el script Vue, que define la estructura de los datos y las funciones que la página utilizará.

```jsx
import Navbar_proyectos from './Navbar_proyectos.vue';
import { getProjects, createProject, updateProject, deleteProject, getExperiences, createExperience, updateExperience, deleteExperience } from '@/plugins/axios';

```

Aquí, se importan componentes y funciones de `axios.js` (como `getProjects` y `createProject`) que hacen peticiones HTTP al backend.

---

### **Definición de Datos**

```jsx
data() {
  return {
    experiences: [],
    projects: [],
    searchQuery: '',
    form: { title: '', time: '', description: '', link: '', type: 'Primer Curso' },
    editing: false,
    editingId: null,
    searchResultsExperiences: [],
    searchResultsProjects: [],
  };
},

```

- `experiences` y `projects`: Almacenan las experiencias y proyectos que vienen del backend.
- `searchQuery`: Almacena el texto ingresado en la barra de búsqueda.
- `form`: Objeto que contiene los datos del formulario.
- `editing`: Define si se está editando una experiencia/proyecto.
- `editingId`: Guarda el ID de la experiencia/proyecto que se está editando.

---

### **Funciones Importantes**

### **1. `loadExperiences` y `loadProjects`**

Estas funciones obtienen datos del backend y los guardan en `experiences` y `projects`.

```jsx
async loadExperiences() {
  const response = await getExperiences();
  this.experiences = response.data;
},
async loadProjects() {
  const response = await getProjects();
  this.projects = response.data;
},

```

### **2. `deleteExperience` y `deleteProject`**

Estas funciones eliminan una experiencia o proyecto del backend, y luego lo eliminan de la lista local para actualizar la interfaz.

```jsx
async deleteExperience(id) {
  await deleteExperience(id);
  this.experiences = this.experiences.filter(experience => experience.id !== id);
},
async deleteProject(id) {
  await deleteProject(id);
  this.projects = this.projects.filter(project => project.id !== id);
},

```

### **3. `editExperience` y `editProject`**

Estas funciones se llaman cuando se hace clic en el botón "Modificar". Llenan el formulario con la información de la experiencia/proyecto que se va a editar.

```jsx
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

```

### **4. `performSearch`**

Esta función filtra las experiencias y proyectos en tiempo real basándose en lo que el usuario escribe en la barra de búsqueda.

```jsx
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

```

### **5. `submitForm`**

Esta función se ejecuta cuando el formulario se envía. Si `editing` es `true`, se actualiza un proyecto/experiencia en el backend usando `updateExperience` o `updateProject`. Si `editing` es `false`, se crea una nueva entrada usando `createExperience` o `createProject`.

```jsx
submitForm() {
  const updatedData = {
    title: this.form.title,
    subtitle: this.form.subtitle || '',
    time: this.form.time || 'Sin fecha',
    description: this.form.description,
    link: this.form.link || '<http://localhost:5173/>',
  };

  if (this.editing) {
    if (this.form.type === 'Primer Curso') {
      updateExperience(this.editingId, updatedData).then(response => {
        const index = this.experiences.findIndex(exp => exp.id === this.editingId);
        this.experiences.splice(index, 1, response.data);
        this.resetForm();
      });
    } else {
      updateProject(this.editingId, updatedData).then(response => {
        const index = this.projects.findIndex(proj => proj.id === this.editingId);
        this.projects.splice(index, 1, response.data);
        this.resetForm();
      });
    }
  } else {
    if (this.form.type ===

 'Primer Curso') {
      createExperience(updatedData).then(response => {
        this.experiences.push(response.data);
        this.resetForm();
      });
    } else {
      createProject(updatedData).then(response => {
        this.projects.push(response.data);
        this.resetForm();
      });
    }
  }
},

```

### **6. `resetForm` y `scrollToForm`**

- `resetForm` limpia el formulario y cambia `editing` a `false`.
- `scrollToForm` desplaza la vista al formulario para mejorar la experiencia del usuario.

---

### **Resumen de la Interacción con el Backend**

Las funciones `getExperiences`, `createExperience`, `updateExperience`, `deleteExperience`, `getProjects`, `createProject`, `updateProject`, y `deleteProject` son llamadas al backend para obtener, crear, actualizar o eliminar datos en la base de datos.

### plugins/axios.py

Este código configura y exporta una instancia de Axios para que el frontend (la parte de la interfaz de usuario) pueda comunicarse con el backend (la parte del servidor) de manera eficiente y organizada. Cada función representa una solicitud HTTP a una URL específica del backend para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre "proyectos" y "experiencias".

Voy a desglosar cada parte para que puedas entenderla mejor:

### 1. **Configuración de Axios**

```jsx
import axios from 'axios';

const instanciaAxios = axios.create({
    baseURL: '<http://localhost:5000>' // URL base del backend de Flask
});

```

Aquí, se importa Axios, una biblioteca de JavaScript que facilita las solicitudes HTTP, y se crea una instancia de Axios con `axios.create()`. Esto permite definir una configuración común para todas las solicitudes que usen esta instancia.

- **`baseURL: '<http://localhost:5000>'`**: Esta es la URL base para todas las solicitudes que se harán al backend. `localhost:5000` significa que el servidor backend (en este caso, Flask) está ejecutándose en la dirección `localhost` (es decir, en tu computadora local) en el puerto `5000`.

    Gracias a esta `baseURL`, cada solicitud en este archivo puede usar solo el segmento final de la URL (como `/projects` o `/experiences`) en lugar de escribir la URL completa cada vez.


### 2. **Funciones para Proyectos**

```jsx
export const createProject = (data) => instanciaAxios.post('/projects', data);
export const getProjects = () => instanciaAxios.get('/projects');
export const updateProject = (id, data) => instanciaAxios.put(`/projects/${id}`, data);
export const deleteProject = (id) => instanciaAxios.delete(`/projects/${id}`);

```

Estas cuatro funciones permiten realizar las operaciones CRUD para "proyectos":

1. **`createProject(data)`**:
    - Usa `instanciaAxios.post()` para hacer una solicitud POST a `/projects`.
    - Envía `data` (la información del proyecto) como el cuerpo de la solicitud.
    - Se usa para crear un nuevo proyecto en el backend.
2. **`getProjects()`**:
    - Usa `instanciaAxios.get()` para hacer una solicitud GET a `/projects`.
    - No requiere parámetros, ya que solo necesita obtener todos los proyectos.
    - Recupera la lista de proyectos almacenados en el backend.
3. **`updateProject(id, data)`**:
    - Usa `instanciaAxios.put()` para hacer una solicitud PUT a `/projects/{id}`, donde `{id}` es el ID del proyecto que queremos actualizar.
    - Envía `data` (los datos modificados del proyecto) en el cuerpo de la solicitud.
    - Sirve para actualizar un proyecto específico en el backend.
4. **`deleteProject(id)`**:
    - Usa `instanciaAxios.delete()` para hacer una solicitud DELETE a `/projects/{id}`, donde `{id}` es el ID del proyecto a eliminar.
    - No necesita cuerpo de solicitud.
    - Elimina el proyecto específico del backend.

### 3. **Funciones para Experiencias**

```jsx
export const createExperience = (data) => instanciaAxios.post('/experiences', data);
export const getExperiences = () => instanciaAxios.get('/experiences');
export const updateExperience = (id, data) => instanciaAxios.put(`/experiences/${id}`, data);
export const deleteExperience = (id) => instanciaAxios.delete(`/experiences/${id}`);

```

Estas cuatro funciones son muy similares a las de proyectos, pero en lugar de trabajar con `/projects`, trabajan con `/experiences`. Esto permite manejar las "experiencias" en el backend de la misma forma:

1. **`createExperience(data)`**:
    - Envía una solicitud POST a `/experiences` con `data` (la información de la experiencia).
    - Crea una nueva experiencia en el backend.
2. **`getExperiences()`**:
    - Envía una solicitud GET a `/experiences` para obtener todas las experiencias.
    - Recupera la lista de experiencias del backend.
3. **`updateExperience(id, data)`**:
    - Envía una solicitud PUT a `/experiences/{id}` con `data` (los datos modificados).
    - Actualiza una experiencia específica en el backend usando su `id`.
4. **`deleteExperience(id)`**:
    - Envía una solicitud DELETE a `/experiences/{id}`.
    - Elimina una experiencia específica en el backend.

### 4. **Exportación por Defecto**

```jsx
export default instanciaAxios;

```

Aquí, se exporta `instanciaAxios` como la exportación por defecto del archivo. Esto significa que otros archivos pueden importar esta instancia para realizar solicitudes HTTP personalizadas. Sin embargo, las funciones `createProject`, `getProjects`, etc., también se exportan de forma individual para su uso directo.

### **Resumen de la Interacción con el Backend**

Estas funciones son la manera en que el frontend se comunica con el backend. Cada función envía una solicitud HTTP al backend Flask:

- **POST** para crear (`createProject`, `createExperience`)
- **GET** para leer (`getProjects`, `getExperiences`)
- **PUT** para actualizar (`updateProject`, `updateExperience`)
- **DELETE** para eliminar (`deleteProject`, `deleteExperience`)

De esta forma, el frontend puede gestionar proyectos y experiencias y sincronizar los cambios en el backend.