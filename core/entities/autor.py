class Autor:
    def __init__(self, nombre: str, pais: str, año_de_nacimiento: int):
        self.nombre = nombre
        self.pais = pais
        self.año_de_nacimiento = año_de_nacimiento

    def __repr__(self):
        return f"Autor(nombre='{self.nombre}', pais='{self.pais}', año_de_nacimiento={self.año_de_nacimiento})"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "pais": self.pais,
            "año_de_nacimiento": self.año_de_nacimiento
        }
