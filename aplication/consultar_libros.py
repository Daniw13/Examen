from typing import List
from core.entities.libro import Libro
from core.usecases.libro_repository import LibroRepository

class ConsultarTodosLosLibros:
    def __init__(self, repository: LibroRepository):
        self.repository = repository

    def execute(self) -> List[Libro]:
        return self.repository.get_all_libros()

class ConsultarLibrosPorNombreAlgebra:
    def __init__(self, repository: LibroRepository):
        self.repository = repository

    def execute(self) -> List[Libro]:
        return self.repository.get_libros_by_title_containing("algebra")

class ConsultarLibrosPorAutoresFranceses:
    def __init__(self, repository: LibroRepository):
        self.repository = repository

    def execute(self) -> List[Libro]:
        return self.repository.get_libros_by_author_country("Francia")
