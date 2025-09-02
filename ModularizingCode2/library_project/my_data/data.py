#my_data/data.py this will handle data storage

# books = []

# #defining a function with two arguments; title and author
# def add_book(title, author):
#     #adding a dictionary into the empty list books
#     books.append({"title": title, "author": author, "available": True})

#     #defining a function that calls the contents of the list books
# def get_books():
#     return books

#using json format
import json
import os

FILE_PATH = "library_data.json"
books = []

def load_books():
    """Load books from JSON file if it exists"""
    global books
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            books = json.load(f)

    else:
        books = []

def save_books():
    """Save current books list to JSON file"""
    with open(FILE_PATH, "w") as f:
        json.dump(books, f, indent=4)

def add_book(title, author):
    books.append({"title": title, "author": author, "available": True})
    save_books()

def get_books():
    return books