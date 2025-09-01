#main.py this will be the project entry point

# from my_data import data
# from utils import helpers
# from services import library

# #Add some books to the empty list
# data.add_book("Python Basics", "John Doe")
# data.add_book("Advance Python", "Jane Smith")

# #To display all books in the list
# print("Library Collection:")
# for b in data.get_books():
#     #this prints out the books and their status using functions from data.py and helpers.py
#     print(helpers.format_book(b))

# #To borrow a book
# print("\nBorrowing a book:")

# #this stores the book title and switches the value of available from True to False
# print(library.borrow_book('Python Basics'))
# print(library.borrow_book('Python Basics')) #this prints the book not avaialable

# #Display books again
# print("\nUpdated Library Collection:")
# for b in data.get_books():
#     #this prints the books with their updated status
#     print(helpers.format_book(b))


#main.py for json files
from my_data import data
from utils import helpers
from services import library

def show_books():
    books = data.get_books
    if not books:
        print("No books in the library yet.")
        return
    for i, b in enumerate(books, start=1):
        print(helpers.format_book(b, i))

def main():
    data.load_books() #load books when app starts

    while True:
        print("\n__Library Menue__")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
    
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            data.add_book(title, author)
            print(f"'{title}' by {author} added to library.")
        
        elif choice == "2":
            print("\nLibrary Collection:")
            show_books()

        elif choice == "3":
            title = input("Enter book title to borrow: ")
            print(library.borrow_book(title))

        elif choice == "4":
            title = input("Enter book title to return: ")
            print(library.return_book(title))
        
        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()


