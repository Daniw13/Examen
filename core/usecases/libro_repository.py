from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.libro import Libro
from core.entities.autor import Autor

class LibroRepository(ABC):
    @abstractmethod
    def get_all_libros(self) -> List[Libro]:
        pass

    @abstractmethod
    def get_libros_by_title_containing(self, text: str) -> List[Libro]:
        pass

    @abstractmethod
    def get_libros_by_author_country(self, country: str) -> List[Libro]:
        pass

    @abstractmethod
    def get_authors_by_book_genre(self, genre: str) -> List[Autor]:
        pass
