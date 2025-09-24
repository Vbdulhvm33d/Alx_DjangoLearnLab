from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from .views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("admin-dashboard/", views.admin_view, name="admin_view"),
    path("librarian-dashboard/", views.librarian_view, name="librarian_view"),
    path("member-dashboard/", views.member_view, name="member_view"),
]

