#utils/helpers.py This will handle helper functions
# def format_book(book):
#     #if the key 'available' is True, status returns 'Available' else it returns 'Borrowed'
#     status = "Available" if book["available"] else "Borrowed"
#     return f"{book["title"]} by {book["author"]} - {status}"

#JSON FORMAT
def format_book(book, index):
    status = "Available" if book["available"] else "Borrowed"
    return f"{index}. {book["title"]} by {book["author"]} - {status}"