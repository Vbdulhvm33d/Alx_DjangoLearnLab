from django.db import models
from relationship_app.models import Author, Book, Library, Librarian
# Sample queries demonstrating relationships
def sample_queries():
    # Query all books by a specific author
    author_books = Book.objects.get()
    print(f"Books by {Author.name}: {[book.title for book in author_books]}")

    #Retrieve all books in a library
    book = Library.objects.get(name=(Library.name), books.all())
    print(book)

    #Retrieve the librarian for a library
    lib = library.objects.first()
    lib_librarian = lib.librarian
    print(f"Librarian of {lib.name}: {lib_librarian.name}")