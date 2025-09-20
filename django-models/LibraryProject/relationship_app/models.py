from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name
    
class librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name
# Create your models here

