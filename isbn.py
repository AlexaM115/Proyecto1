from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("URI"))
db = client["biblioteca"]
coleccion_isbns = db["isbns"]

class ISBN:
    def __init__(self, codigo, editorial, pais_publicacion): 
        self.codigo = codigo
        self.editorial = editorial
        self.pais_publicacion = pais_publicacion
        self.libro_id = None

    def save(self):
        datos = {
            "🔢Código": self.codigo,
            "📖Editorial": self.editorial,
            "🗺️País de publicación": self.pais_publicacion,
            "libro_id": self.libro_id
        }
        resultado = coleccion_isbns.insert_one(datos)
        self._id = resultado.inserted_id
        print(f"ISBN guardado con ID: {self._id}")

    def update_libro_id(self, libro_id):
        filtro = {"_id": ObjectId(self._id)}
        nuevos_valores = {"$set": {"libro_id": ObjectId(libro_id)}}
        resultado = coleccion_isbns.update_one(filtro, nuevos_valores)
        if resultado.matched_count > 0:
            print("ISBN actualizado con el ID del Libro.")
        else:
            print("Error actualizando el ISBN.")