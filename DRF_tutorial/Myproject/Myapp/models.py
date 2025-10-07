from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} from {self.nationality}"
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
class BookDetail(models.Model):
    book = models.OneToOneField(Book, related_name='about', on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    
    def __str__(self):
        return f"Details of {self.book.title}"
    
class BookReview(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    review_text = models.TextField()
    rating = models.IntegerField()
    flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"Review for {self.book.title} with rating {self.rating}"