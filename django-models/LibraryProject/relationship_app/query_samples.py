from django.db import models
from relationship_app.models import Author, Book, library, librarian
# Sample queries demonstrating relationships
def sample_queries():
    # Query all books by a specific author
    author_books = Book.objects.get()
    print(f"Books by {Author.name}: {[book.title for book in author_books]}")

    #Retrieve all books in a library
    book = Book.objects.get()
    book_libraries = book.libraries.all()
    print(f"Libraries with the book '{book.title}': {[lib.name for lib in book_libraries]}")

    #Retrieve the librarian for a library
    lib = library.objects.first()
    lib_librarian = lib.librarian
    print(f"Librarian of {lib.name}: {lib_librarian.name}")