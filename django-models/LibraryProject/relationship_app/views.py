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
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [path('login/', login.as_view(template_name='registeration/login.html'), name='login'),]

#creating user logout form
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [path('logout/', logout.as_view(), name='Logout')]

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

