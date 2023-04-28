from typing import List
from classes.Book import Book


class Member:
    # -- Magic methods
    def __init__(self, firstname: str, lastname: str, member_id: int, borrowing_list: List[Book] = []):
        self._firstname = firstname
        self._lastname = lastname
        self._member_id = member_id
        self._borrowing_list = borrowing_list

    def __str__(self) -> str:
        borrow_book_sentence = "Le membre emprunte actuellement un ou plusieurs livres." if len(
            self._borrowing_list) else "Le membre n'emprunte pas de livre actuellement."

        return f"""
            -- Informations relatives au membre --
            Prénom : {self._firstname}
            Nom : {self._lastname}
            Identifiant : {self._member_id}
            {borrow_book_sentence}
        """

    # -- Methods --

    def add_book_in_borrowing_list(self, new_book: Book) -> None:
        if not new_book.is_available:
            print("Le livre a déjà été emprunté par un autre membre.")
            return

        for book in self._borrowing_list:
            if book.isbn == new_book.isbn:
                print(
                    f"Le livre est déjà présent dans la liste d'emprunt du membre {self._firstname} {self._lastname}.")
                return

        new_book.is_available = False
        self._borrowing_list.append(new_book)
        print(f"Le livre a été ajouté à la liste d'emprunt du membre {self._firstname} {self._lastname}.")

    def remove_book_in_borrowing_list(self, book_to_remove: Book) -> None:
        for book in self._borrowing_list:
            if book.isbn == book_to_remove.isbn:
                self._borrowing_list.remove(book_to_remove)
                book_to_remove.is_available = True
                print(
                    f"Le livre {book_to_remove.title} a été enlevé de la liste d'emprunt de l'utilisateur {self._firstname} {self._lastname}.")
                return

            print(
                f"Le membre {self._firstname} {self._lastname} n'a pas le livre {book_to_remove.title} dans sa liste d'emprunt.")

    # -- Getters --

    @property
    def firstname(self) -> str:
        return self._firstname

    @property
    def lastname(self) -> str:
        return self._lastname

    @property
    def member_id(self) -> int:
        return self._member_id

    @property
    def borrowing_list(self) -> List[Book]:
        return self._borrowing_list

    # -- Setters --

    @firstname.setter
    def firstname(self, new_firsname: str) -> None:
        self._firstname = new_firsname

    @lastname.setter
    def lastname(self, new_lastname: str) -> None:
        self._lastname = new_lastname

    @member_id.setter
    def member_id(self, new_member_id: int) -> None:
        self._member_id = new_member_id

    @borrowing_list.setter
    def borrowing_list(self, new_borrowing_list: List[Book]) -> None:
        self._borrowing_list = new_borrowing_list
