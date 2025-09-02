#service/library.py This will handle the business logic

# import my_data.data as data

# def borrow_book(title):
#     for book in data.get_books():
#         #if the newly inputted title already exists and available is True, change the value of available to False and print the return statement
#         if book["title"].lower() == title.lower() and book["available"]:
#             book["available"] = False
#             return f"You have borrowed '{book['title']}'"
#     return "Book not avaialable"

#JSON FORMAT
import my_data.data as data

def borrow_book(title):
    for book in data.get_books():
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            data.save_books()
            return f"You have borrowed '{book[title]}"
    return "Book not available."

def return_book(title):
    for book in data.get_books():
        if book["titlle"].lower() == title.lower() and not book["available"]:
            book["available"] = True
            data.save_books()
            return f"You have returned '{book[title]}'"
    return "Book not found or borrowed"