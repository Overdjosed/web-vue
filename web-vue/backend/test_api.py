# test_api.py

import unittest
from flask import Flask
from flask_testing import TestCase
from app import app, db, Project, Experience

class APITestCase(TestCase):
    def create_app(self):
        """
        Configura la aplicación en modo de prueba y utiliza una base de datos
        en memoria (sqlite:///:memory:) para que los datos no se guarden de
        forma permanente.
        """
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
        return app

    def setUp(self):
        """
        Crea las tablas de la base de datos antes de cada prueba.
        """
        db.create_all()  # Crear todas las tablas

    def tearDown(self):
        """
        Elimina todas las tablas después de cada prueba para evitar interferencias entre pruebas.
        """
        db.session.remove()
        db.drop_all()  # Eliminar todas las tablas al finalizar cada prueba

    def test_create_project(self):
        response = self.client.post('/projects', json={
            "title": "Nuevo Proyecto",
            "subtitle": "Subtítulo del proyecto",
            "time": "2024-11-01",
            "description": "Descripción del proyecto de prueba",
            "link": "http://example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Nuevo Proyecto', response.json['title'])

    def test_get_projects(self):
        # Primero, creamos un proyecto para probar la obtención
        self.client.post('/projects', json={
            "title": "Proyecto de Prueba",
            "subtitle": "Subtítulo",
            "time": "2024-11-01",
            "description": "Descripción del proyecto",
            "link": "http://example.com"
        })

        response = self.client.get('/projects')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)  # Debe haber al menos un proyecto

    def test_update_project(self):
        # Crear proyecto para actualizar
        response = self.client.post('/projects', json={
            "title": "Proyecto Viejo",
            "subtitle": "Subtítulo",
            "time": "2024-11-01",
            "description": "Descripción vieja",
            "link": "http://example.com"
        })
        project_id = response.json['id']

        # Actualizar proyecto
        response = self.client.put(f'/projects/{project_id}', json={
            "title": "Proyecto Actualizado",
            "description": "Descripción actualizada"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Proyecto Actualizado", response.json['title'])

    def test_delete_project(self):
        # Crear proyecto para eliminar
        response = self.client.post('/projects', json={
            "title": "Proyecto a eliminar",
            "subtitle": "Subtítulo",
            "time": "2024-11-01",
            "description": "Descripción",
            "link": "http://example.com"
        })
        project_id = response.json['id']

        # Eliminar proyecto
        response = self.client.delete(f'/projects/{project_id}')
        self.assertEqual(response.status_code, 204)

        # Verificar que no existe
        response = self.client.get(f'/projects/{project_id}')
        self.assertEqual(response.status_code, 404)

    # Pruebas similares para experiencias
    def test_create_experience(self):
        response = self.client.post('/experiences', json={
            "title": "Nueva Experiencia",
            "subtitle": "Subtítulo de la experiencia",
            "time": "2024-11-01",
            "description": "Descripción de la experiencia de prueba",
            "link": "http://example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Nueva Experiencia', response.json['title'])

    def test_get_experiences(self):
        # Crear una experiencia para probar la obtención
        self.client.post('/experiences', json={
            "title": "Experiencia de Prueba",
            "subtitle": "Subtítulo",
            "time": "2024-11-01",
            "description": "Descripción de la experiencia",
            "link": "http://example.com"
        })

        response = self.client.get('/experiences')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)  # Debe haber al menos una experiencia

if __name__ == '__main__':
    unittest.main()
