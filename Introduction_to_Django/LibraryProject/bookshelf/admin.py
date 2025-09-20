from django.contrib import admin
from .models import Book

list_display = ('title', 'author', 'publication_year')
search_fields = ('title', 'author')
list_filter = ('publication_year',)

admin.site.register(Book, admin.ModelAdmin)

# Register your models here.
