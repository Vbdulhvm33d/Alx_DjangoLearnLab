from django.db import models
from relationship_app.models import Author, Book, Library, Librarian
# Sample queries demonstrating relationships
def sample_queries():
    # Query all books by a specific author
    author_books = Book.objects.get(author = 'author_name')
    His_books = author_books.books.all()
    print(His_books)
    
    #print(f"Books by {Author.name}: {[book.title for book in author_books]}")

    #Retrieve all books in a library
    book = Library.objects.get(name='Library_name')
    books_in_library = book.books.all()
    print(books_in_library)

    #Retrieve the librarian for a library
    lib = library.objects.first()
    lib_librarian = lib.librarian
    print(f"Librarian of {lib.name}: {lib_librarian.name}")