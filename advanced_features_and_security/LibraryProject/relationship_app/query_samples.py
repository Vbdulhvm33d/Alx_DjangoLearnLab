from django.db import models
from relationship_app.models import Author, Book, Library, Librarian
# Sample queries demonstrating relationships
def sample_queries():
    # Query all books by a specific author
    def get_books_by_author(author_name):
    # Fetch the author object by name
        author = Author.objects.get(name=author_name)  

    # Get all books written by this author
        books = Book.objects.filter(author=author)  
    
        return books
    
    #print(f"Books by {Author.name}: {[book.title for book in author_books]}")

    #Retrieve all books in a library
book = Library.objects.get(name='library_name')
books_in_library = book.books.all()
print(books_in_library)

    #Retrieve the librarian for a library
lib = Library.objects.first()
lib_librarian = lib.librarian
print(f"Librarian of {lib.name}: {lib_librarian.name}")