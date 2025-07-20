from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show a library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  #اسم التمبليت المستخدم
    context_object_name = 'library_info'                     #اسم المتغير المستخدم في التمبليت


'''<!-- library_detail.html -->
<h1>{{ library_info.name }}</h1>
<ul>
  {% for book in library_info.books.all %}
    <li>{{ book.title }}</li>
  {% endfor %}
</ul>
'''
#_____________
# views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):            #function-based view to sign-up/register
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ← ده السطر اللي بيدور عليه
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

#عشان نقدر نكتب في القالب مثلًا: {{ form }} أو {{ form.username }} وغيره.
#username is attritbtute in UserCreationForm class >>> username, password1 and password2 are attribtutes in UserCreationForm class

#_________________________
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def check_role(role):
    def decorator(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role     #is user in userprofile class 
    return decorator

@user_passes_test(check_role('Admin'))
def admin_view(request):
     return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'member_view.html')

