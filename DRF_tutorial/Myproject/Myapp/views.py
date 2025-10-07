#from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book, Author, BookDetail, BookReview
from .serializers import BookSerializer, AuthorSerializer, BookDetailSerializer, BookReviewSerializer
from .permissions import isAuthenticatedOrReadOnly, IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset
        author_name = self.request.query_params.get('author', None)
        year = self.request.query_params.get('year', None)

        if author_name:
            queryset = queryset.filter(author__name__icontains=author_name)
        
        if year:
            queryset = queryset.filter(published_date=year)

        return queryset
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().prefetch_related('books')
    serializer_class = AuthorSerializer

class BookDetailViewSet(viewsets.ModelViewSet):
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [isAuthenticatedOrReadOnly]
    

class BookReviewViewSet(viewsets.ModelViewSet):
    queryset = BookReview.objects.all().select_related('book')
    serializer_class = BookReviewSerializer
    permission_classes = [isAuthenticatedOrReadOnly]
    authentication_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def flag(self, request, pk=None):
        review = self.get_object()
        review.flagged = True
        review.save()
        return Response({'status': 'review flagged'}, status=status.HTTP_200_OK)
# Create your views here.
