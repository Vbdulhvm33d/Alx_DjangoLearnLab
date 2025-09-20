from django.db import models
from relationship_app.models import Author, Book, library, librarian
# Sample queries demonstrating relationships
def sample_queries():
    # Query all books by a specific author
    author = Author.objects.first()
    author_books = author.books.all()
    print(f"Books by {author.name}: {[book.title for book in author_books]}")

    #Retrieve all books in a library
    book = Book.objects.first()
    book_libraries = book.libraries.all()
    print(f"Libraries with the book '{book.title}': {[lib.name for lib in book_libraries]}")

    #Retrieve the librarian for a library
    lib = library.objects.first()
    lib_librarian = lib.librarian
    print(f"Librarian of {lib.name}: {lib_librarian.name}")