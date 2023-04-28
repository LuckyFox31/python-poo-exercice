class Book:
    # -- Magic methods --
    def __init__(self, title: str, author: str, isbn: str, is_available: bool) -> None:
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_available = is_available

    def __str__(self) -> str:
        is_available_sentence = "disponible" if self._is_available else "indisponible"

        return f"""
            -- Informations relatives au livre --
            Titre : {self._title}
            Auteur : {self._author}
            ISBN : {self._isbn}
            Le livre est {is_available_sentence}.
        """

    # -- Getters --

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def is_available(self) -> bool:
        return self._is_available

    # -- Setters --

    @title.setter
    def title(self, new_title: str) -> None:
        self._title = new_title

    @author.setter
    def author(self, new_author: str) -> None:
        self._author = new_author

    @isbn.setter
    def isbn(self, new_isbn: str) -> None:
        self._isbn = new_isbn

    @is_available.setter
    def is_available(self, new_is_available: bool) -> None:
        self._is_available = new_is_available
