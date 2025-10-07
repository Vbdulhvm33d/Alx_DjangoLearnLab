#pythonCopy codefrom django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, BookDetailViewSet, BookReviewViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'bookdetails', BookDetailViewSet)
router.register(r'bookreviews', BookReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    

]