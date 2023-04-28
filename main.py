from classes.Book import Book
from classes.Member import Member
from classes.PublicLibrary import PublicLibrary

first_book = Book('Les fourberies de Scapin', 'Molière', '9782038713084', True)

print(first_book)

first_member = Member('John', 'Doe', 1)

print(first_member)

public_library = PublicLibrary('Bibliothèque municipale', '7 Rue de la rose, 80000 Amiens')
public_library.add_book_to_library(first_book)
public_library.register_new_member(first_member)
public_library.borrow_book(first_book, first_member)
