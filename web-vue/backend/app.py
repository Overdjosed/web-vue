# backend/app.py
import json
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from models import db, Project, Experience
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

# Útila para determinar la raíz del paquete o módulo actual (app.py)
# Necesario para confifurar rutas
app = Flask(__name__)
# Habilitar CORS (solicitudes) de diferentes orígenes para todas las rutas
CORS(app)
# Configurar la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Para añadir autenticación HTTP
auth = HTTPBasicAuth()

# Usuarios y contraseñas (solo para fines de prueba, evita usar en producción)
users = {
    "admin": generate_password_hash("admin"),
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

# ----------------------
# Funciones para Project
# ----------------------

# Define una ruta para manejar solicitudes GET en la url /projects
@app.route('/projects', methods=['GET'])
# La funcion get_projects() se ejecuta cuando se reciba una solicitud GET
def get_projects():
    projects = Project.query.all()  # Obtiene todos los proyectos en la base de datos
    return jsonify([project.to_dict() for project in projects])  # Devuelve los proyectos en JSON


@app.route('/projects', methods=['POST'])
@auth.login_required
def create_project():
    data = request.json # Obtiene los datos JSON enviados en el cuerpo de la solicitud
    new_project = Project( # Crea una nueva instancia del modelo Project
        title=data['title'],
        subtitle=data.get('subtitle'),
        time=data.get('time'),
        image=data.get('image'),
        description=data.get('description'),
        link=data.get('link')
    )
    # Añade el nuevo proyecto a la base de datos y guarda los cambios
    db.session.add(new_project)
    # Confirma la transacción
    db.session.commit()
    return jsonify(new_project.to_dict()), 201

@app.route('/projects/<int:id>', methods=['PUT'])
def update_project(id):
    data = request.json
    # Busca el proyecto por su id
    project = Project.query.get(id)
    # Si no se encuentra el proyecto, devuelve un error 404
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    project.title = data.get('title', project.title)
    project.subtitle = data.get('subtitle', project.subtitle)
    project.time = data.get('time', project.time)
    project.image = data.get('image', project.image)
    project.description = data.get('description', project.description)
    project.link = data.get('link', project.link)
    db.session.commit()
    # Convierte a JSON y envía la respuesta al cliente
    return jsonify(project.to_dict())

@app.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    project = Project.query.get(id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    db.session.delete(project)
    db.session.commit()
    return '', 204

@app.route('/projects/<int:id>', methods=['GET'])
def get_project(id):
    project = Project.query.get(id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    return jsonify(project.to_dict())

# -------------------------
# Funciones para Experience
# -------------------------

@app.route('/experiences', methods=['GET'])
def get_experiences():
    experiences = Experience.query.all()  # Obtiene todas las experiencias en la base de datos
    return jsonify([experience.to_dict() for experience in experiences])  # Devuelve las experiencias en JSON

@app.route('/experiences', methods=['POST'])
@auth.login_required
def create_experience():
    data = request.json
    new_experience = Experience(
        title=data['title'],
        subtitle=data.get('subtitle'),
        time=data.get('time'),
        description=data.get('description'),
        link=data.get('link')
    )
    db.session.add(new_experience)
    db.session.commit()
    return jsonify(new_experience.to_dict()), 201

@app.route('/experiences/<int:id>', methods=['PUT'])
def update_experience(id):
    data = request.json
    experience = Experience.query.get(id)
    if not experience:
        return jsonify({'error': 'Experience not found'}), 404
    experience.title = data.get('title', experience.title)
    experience.subtitle = data.get('subtitle', experience.subtitle)
    experience.time = data.get('time', experience.time)
    experience.description = data.get('description', experience.description)
    experience.link = data.get('link', experience.link)
    db.session.commit()
    return jsonify(experience.to_dict())

@app.route('/experiences/<int:id>', methods=['DELETE'])
def delete_experience(id):
    experience = Experience.query.get(id)
    if not experience:
        return jsonify({'error': 'Experience not found'}), 404
    db.session.delete(experience)
    db.session.commit()
    return '', 204

@app.route('/experiences/<int:id>', methods=['GET'])
def get_experience(id):
    experience = Experience.query.get(id)
    if not experience:
        return jsonify({'error': 'Project not found'}), 404
    return jsonify(experience.to_dict())


# -------------------------
# Funciones cargar los datos desde los json
# -------------------------

# Obtener la ruta actual de este archivo (app.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo projectsData.json
projects_data_path = os.path.join(current_dir, 'projectsData.json')
experience_data_path = os.path.join(current_dir, 'experienceData.json')

# Cargar datos iniciales desde JSON
def load_projects_from_json():
    # Cargar proyectos desde JSON si la tabla está vacía, esto evita meter duplicados si los datos ya están dentro.
    with open(projects_data_path, 'r', encoding='utf-8') as file:
        projects_data = json.load(file)
        # Si la tabla de proyectos está vacía, cargar los proyectos desde el archivo JSON
        if Project.query.count() == 0:
            for project_data in projects_data:
                new_project = Project(
                    title=project_data['title'],
                    subtitle=project_data.get('subtitle'),
                    time=project_data.get('time'),
                    image=project_data.get('image'),
                    description=project_data.get('description'),
                    link=project_data.get('link')
                )
                db.session.add(new_project)
            db.session.commit()
            print("Proyectos iniciales cargados desde JSON.")
        else:
            print("Los proyectos ya están cargados en la base de datos.")

# Cargar datos iniciales desde JSON
def load_experience_from_json():
    # Cargar proyectos desde JSON si la tabla está vacía
    with open(experience_data_path, 'r', encoding='utf-8') as file:
        experiences_data = json.load(file)
        if Experience.query.count() == 0:
            for experience_data in experiences_data:
                new_project = Experience(
                    title=experience_data['title'],
                    subtitle=experience_data.get('subtitle'),
                    time=experience_data.get('time'),
                    description=experience_data.get('description'),
                    link=experience_data.get('link')
                )
                db.session.add(new_project)
            db.session.commit()
            print("Experiences iniciales cargados desde JSON.")
        else:
            print("Los experiences ya están cargados en la base de datos.")


# Inicializar la base de datos y cargar los datos iniciales
with app.app_context():
    db.create_all()  # Crear las tablas en la base de datos
    load_projects_from_json()  # Cargar proyectos desde el archivo JSON si no existen
    load_experience_from_json()

if __name__ == '__main__':
    app.run(debug=True)