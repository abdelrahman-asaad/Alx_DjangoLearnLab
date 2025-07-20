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
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # بعد التسجيل يوجه المستخدم لصفحة تسجيل الدخول
    template_name = 'registration/signup.html'


