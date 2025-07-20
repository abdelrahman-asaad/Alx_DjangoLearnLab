from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library

# Function-based view to list all books
def all_books_view(request):
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