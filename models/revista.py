from config.mysqlconnection import connectToMySQL
from flask import flash
from models import usuario

class Revista:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.descripcion = data['descripcion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuarios = []
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO revistas (nombre,descripcion,created_at,updated_at) VALUES (%(nombre)s,%(descripcion)s,NOW(),NOW());"
        return connectToMySQL('esquema_revistas').query_db(query,data)
    
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM revistas;"
        results = connectToMySQL('esquema_revistas').query_db(query)
        revistas = []
        for info in results:
            revista_data = {
                "id": info['id'],
                "nombre": info['nombre'],
                "descripcion": info['descripcion'],
                "created_at": info['created_at'],
                "updated_at": info['updated_at']
            }
            revistas.append(Revista(revista_data))
        return revistas
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM revistas WHERE id = %(id)s;"
        return connectToMySQL('esquema_revistas').query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE revistas SET nombre=%(nombre)s,descripcion=%(descripcion)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('esquema_revistas').query_db(query,data)
    
    @classmethod
    def agregar_suscripcion(cls,data):
        query = "INSERT INTO suscripciones (usuario_id,revista_id) VALUES (%(usuario_id)s,%(revista_id)s);"
        return connectToMySQL('esquema_revistas').query_db(query,data)
    
    @classmethod
    def usuarios_suscritos(cls,data):
        query = "SELECT usuarios.id,usuarios.first_name,usuarios.last_name,usuarios.email,usuarios.password,usuarios.created_at,usuarios.updated_at FROM usuarios JOIN suscripciones ON usuarios.id = suscripciones.usuario_id JOIN revistas ON suscripciones.revista_id = revistas.id WHERE revistas.id=%(id)s GROUP BY usuarios.id;"
        results = connectToMySQL('esquema_revistas').query_db(query,data)
        usuarios = []
        for info in results:
            users_data = {
                "id": info['id'],
                "first_name": info['first_name'],
                "last_name": info['last_name'],
                "email": info['email'],
                "password": info['password'],
                "created_at": info['created_at'],
                "updated_at": info['updated_at']
            }
            usuarios.append(usuario.Usuario(users_data))
        return usuarios
    
    @staticmethod
    def validacion(info):
        is_valid = True
        if len(info['nombre']) < 2:
            flash('El nombre de la revista debe contener al menos 2 caracteres','error')
            is_valid = False
        if len(info['descripcion']) < 10:
            flash('La descripción debe contener al menos 10 caracteres','error')
            is_valid = False
        return is_valid
    
    @classmethod
    def show_revista_by_id(cls,data):
        query = "SELECT * FROM revistas WHERE id=%(id)s;"
        results = connectToMySQL('esquema_revistas').query_db(query,data)
        revista = []
        if not results:
            flash('La revista no existe, intente de nuevo','error')
            return None
        for info in results:
            revista_data = {
                "id": info['id'],
                "nombre": info['nombre'],
                "descripcion": info['descripcion'],
                "created_at": info['created_at'],
                "updated_at": info['updated_at']
            }
            revista.append(Revista(revista_data))
        return revista