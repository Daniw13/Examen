from typing import List
from core.entities.autor import Autor

class Libro:
    def __init__(self, nombre: str, isbn: str, editorial: str, año_de_publicacion: int, precio: float, autores: List[Autor], genero: str):
        self.nombre = nombre
        self.isbn = isbn
        self.editorial = editorial
        self.año_de_publicacion = año_de_publicacion
        self.precio = precio
        self.autores = autores
        self.genero = genero

    def __repr__(self):
        autores_repr = ", ".join([autor.nombre for autor in self.autores])
        return f"Libro(nombre='{self.nombre}', ISBN='{self.isbn}', Editorial='{self.editorial}', año_de_publicacion={self.año_de_publicacion}, precio={self.precio}, autores=[{autores_repr}], genero='{self.genero}')"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "isbn": self.isbn,
            "editorial": self.editorial,
            "año_de_publicacion": self.año_de_publicacion,
            "precio": self.precio,
            "autores": [autor.to_dict() for autor in self.autores],
            "genero": self.genero
        }
