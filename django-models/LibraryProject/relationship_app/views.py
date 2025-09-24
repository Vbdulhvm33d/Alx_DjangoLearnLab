from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Create your views here.
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library" 

#creating a user profile
#from django.contrib.auth.models import User
#new_user = User.objects.create_user(username='newuser',email='newuser@gmail.com',password='password123')
#new_user.save()

#creating a new user registeration form.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'

#creating user login form
#from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [path('login/', LoginView.as_view(template_name='registeration/login.html'), name='login'),]

#creating user logout form
#from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [path('logout/', LogoutView.as_view(), name='Logout')]

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("login")  # redirect to login page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# --- Helper functions ---
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# --- Views ---
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

