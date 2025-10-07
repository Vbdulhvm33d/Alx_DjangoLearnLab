from rest_framework import serializers
from .models import Book, BookDetail, Author, BookReview



class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'days_since_created']
        

    def get_days_since_created(self, obj):
        from datetime import datetime, timezone
        if obj.published_date:
            delta = datetime.now(timezone.utc).date() - obj.published_date
            return delta.days
        

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__'

class BookDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = BookDetail
        fields = '__all__'

class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = BookReview
        fields = '__all__'

        #return (datetime.now)

