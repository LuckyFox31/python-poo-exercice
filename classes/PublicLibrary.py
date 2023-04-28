from typing import List
from classes.Book import Book
from classes.Library import Library
from classes.Member import Member


class PublicLibrary(Library):
    # -- Magic methods --
    def __init__(self, name: str, address: str, books_list: List[Book] = [], members_list: List[Member] = []):
        super().__init__(name, address, books_list, members_list)

    # -- Methods --

    def add_book_to_library(self, new_book: Book) -> None:
        for book in self._books_list:
            if book.isbn == new_book.isbn:
                print(f"Le livre {new_book.title} est déjà présent dans la bibliothèque {self._name}.")
                return

        self._books_list.append(new_book)
        print(f"Le livre {new_book.title} a été ajouté dans la bibliothèque {self._name}.")

    def remove_book_from_library(self, book_to_remove: Book) -> None:
        for book in self._books_list:
            if book.isbn == book.isbn:
                self._books_list.remove(book_to_remove)
                print(f"Le livre {book_to_remove.title} a été retiré de la bibliothèque {self._name}.")
                return

        print(f"Le livre {book_to_remove.title} n'est pas présent dans la bibliothèque {self._name}.")

    def register_new_member(self, new_member: Member) -> None:
        for member in self._members_list:
            if member.member_id == new_member.member_id:
                print(
                    f"Le membre {new_member.firstname} {new_member.lastname} est déjà inscrit dans la bibliothèque {self._name}.")
                return

        self._members_list.append(new_member)
        print(f"Le membre {new_member.firstname} {new_member.lastname} a été inscrit dans la bibliothèque {self._name}.")

    def unregister_member(self, member_to_unregister: Member) -> None:
        for member in self._members_list:
            if member.member_id == member_to_unregister.member_id:
                self._members_list.remove(member_to_unregister)
                print(
                    f"Le membre {member_to_unregister.firstname} {member_to_unregister.lastname} a été désinscrit de la bibliothèque {self._name}.")
                return

        print(f"Le membre {member_to_unregister.firstname} {member_to_unregister.lastname} n'est pas inscrit dans la bibliothèque {self._name}.")

    def borrow_book(self, book_to_borrow: Book, current_member: Member) -> None:
        if current_member not in self._members_list:
            print(f"Le membre {current_member.firstname} {current_member.lastname} n'est pas inscrit dans la bibliothèque {self._name}.")
            return

        if book_to_borrow not in self._books_list:
            print(f"Le livre {book_to_borrow.title} n'est pas présent dans la bibliothèque {self._name}.")
            return

        current_member.add_book_in_borrowing_list(book_to_borrow)

    def return_book(self, book_to_return: Book, current_member: Member) -> None:
        if current_member not in self._members_list:
            print(f"Le membre {current_member.firstname} {current_member.lastname} n'est pas inscrit dans la bibliothèque {self._name}.")
            return

        if book_to_return not in self._books_list:
            print(f"Le livre {book_to_return.title} n'est pas présent dans la bibliothèque {self._name}.")
            return

        current_member.remove_book_in_borrowing_list(book_to_return)
