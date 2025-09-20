from django.db import models
from relationship_app.models import Author, Book, library, librarian
# Sample queries demonstrating relationships
def sample_queries():
    # One-to-Many: Get all books by a specific author
    author = Author.objects.first()
    author_books = author.books.all()
    print(f"Books by {author.name}: {[book.title for book in author_books]}")

    # Many-to-Many: Get all libraries that have a specific book
    book = Book.objects.first()
    book_libraries = book.libraries.all()
    print(f"Libraries with the book '{book.title}': {[lib.name for lib in book_libraries]}")

    # One-to-One: Get the librarian of a specific library
    lib = library.objects.first()
    lib_librarian = lib.librarian
    print(f"Librarian of {lib.name}: {lib_librarian.name}")