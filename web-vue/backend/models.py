# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo para la tabla de proyectos
class Experience(db.Model):
    __tablename__ = 'experiences'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(200), nullable=True)
    time = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    link = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "time": self.time,
            "description": self.description,
            "link": self.link
        }

# Nuevo modelo para la tabla de experiencias
class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(200), nullable=True)
    time = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(500), nullable=True) 
    description = db.Column(db.Text, nullable=True)
    link = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "time": self.time,
            "image": self.image,
            "description": self.description,
            "link": self.link
        }