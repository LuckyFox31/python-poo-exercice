from abc import ABC, abstractmethod
from typing import List
from classes.Book import Book
from classes.Member import Member


class Library(ABC):
    # -- Magic methods --
    def __init__(self, name: str, address: str, books_list: List[Book] = [], members_list: List[Member] = []):
        self._name = name
        self._address = address
        self._books_list = books_list
        self._members_list = members_list

    # -- Methods --

    @abstractmethod
    def add_book_to_library(self, new_book: Book) -> None:
        pass

    @abstractmethod
    def remove_book_from_library(self, book_to_remove: Book) -> None:
        pass

    @abstractmethod
    def register_new_member(self, new_member: Member) -> None:
        pass

    @abstractmethod
    def unregister_member(self, member_to_unregister: Member) -> None:
        pass

    # -- Getters --

    @property
    def name(self) -> str:
        return self._name

    @property
    def address(self) -> str:
        return self._address

    @property
    def books_list(self) -> List[Book]:
        return self._books_list

    @property
    def members_list(self) -> List[Member]:
        return self._members_list

    # -- Setters --

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @address.setter
    def address(self, new_address: str) -> None:
        self._address = new_address

    @books_list.setter
    def books_list(self, new_books_list: List[Book]) -> None:
        self._books_list = new_books_list

    @members_list
    def members_list(self, new_members_list: List[Member]) -> None:
        self._members_list = new_members_list
