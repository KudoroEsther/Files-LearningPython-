#main.py this will be the project entry point

from my_data import data
from utils import helpers
from services import library

#Add some books to the empty list
data.add_book("Python Basics", "John Doe")
data.add_book("Advance Python", "Jane Smith")

#To display all books in the list
print("Library Collection:")
for b in data.get_books():
    #this prints out the books and their status using functions from data.py and helpers.py
    print(helpers.format_book(b))

#To borrow a book
print("\nBorrowing a book:")

#this stores the book title and switches the value of available from True to False
print(library.borrow_book('Python Basics'))
print(library.borrow_book('Python Basics')) #this prints the book not avaialable

#Display books again
print("\nUpdated Library Collection:")
for b in data.get_books():
    #this prints the books with their updated status
    print(helpers.format_book(b))
