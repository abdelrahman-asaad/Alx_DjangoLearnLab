import django
import os

# إعداد بيئة Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. عرض كل الكتب لمؤلف معين
author_name = 'Ahmed Khaled Tawfik'
author = Author.objects.get(name=author_name) #object
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books_by_author :                                    #for book in author.books.all():  # .books من related_name
    print("-", book.title)
#مثال علي الناتج
#Books by Ahmed Khaled Tawfik:
#- Utopia
#- Ma Waraa Al Tabiaa


# 2. عرض كل الكتب داخل مكتبة معينة
library_name = 'Cairo Library'
library = Library.objects.get(name=library_name)  #object
print(f"\nBooks in {library.name}:")
for book in library.books.all():  # books هي ManyToManyField داخل Library
    print("-", book.title)
#مثال علي الناتج
#Books in Cairo Library:
#- Utopia
#- Harry Potter
#- The Alchemist


# 3. إحضار أمين مكتبة معينة
library_name = 'Cairo Library'
library = Library.objects.get(name=library_name)  #object
librarian = library.librarian  # related_name في OneToOneField
print(f"\nLibrarian of {library.name}: {librarian.name}")
#مثال علي الناتج
#Librarian of Cairo Library: Sara Youssef
