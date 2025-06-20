from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("URI"))
db = client["biblioteca"]
coleccion_libros = db["libros"]

class Libro:
    def __init__(self, titulo, autor, anio_publicacion): 
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.isbn_id = None

    def save(self):
        
        
        datos = {
            "🔡Título": self.titulo,
            "🧍Autor": self.autor,
            "⏱️Año de publicación": self.anio_publicacion,
            "isbn_id": self.isbn_id
        }
        resultado = coleccion_libros.insert_one(datos)
        self._id = resultado.inserted_id
        print(f"Libro guardado con ID: {self._id}")

    def update_isbn_id(self, isbn_id):
        filtro = {"_id": ObjectId(self._id)}
        nuevos_valores = {"$set": {"isbn_id": ObjectId(isbn_id)}}
        resultado = coleccion_libros.update_one(filtro, nuevos_valores)
        if resultado.matched_count > 0:
            print("Libro actualizado con el ID del ISBN.")
        else:
            print("Error actualizando el libro.")