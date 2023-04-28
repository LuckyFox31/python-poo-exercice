from classes.Book import Book
from classes.Member import Member

first_book = Book('Les fourberies de Scapin', 'Molière', '9782038713084', True)

print(first_book)

first_member = Member('John', 'Doe', 1)
first_member.add_book_in_borrowing_list(first_book)

print(first_member)