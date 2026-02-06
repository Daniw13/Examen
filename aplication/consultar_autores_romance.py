from typing import List
from core.entities.autor import Autor
from core.usecases.libro_repository import LibroRepository

class ConsultarAutoresLibrosRomance:
    def __init__(self, repository: LibroRepository):
        self.repository = repository

    def execute(self) -> List[Autor]:
        return self.repository.get_authors_by_book_genre("Romance")
