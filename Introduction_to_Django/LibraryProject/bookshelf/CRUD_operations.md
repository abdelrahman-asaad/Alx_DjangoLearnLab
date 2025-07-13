# 📘 Django Shell – CRUD Operations Documentation

هذا الملف يحتوي على تنفيذ وتوثيق كامل لعمليات:
- Create (إنشاء)
- Retrieve (استرجاع)
- Update (تعديل)
- Delete (حذف)

لكائن Book باستخدام Django ORM من داخل الـ shell، مع استخدام التطبيق book_shelf.

---

## 🟢 1. Create – إنشاء كتاب

```python
>>> from bookshelf.models import Book

>>> book = Book.objects.create(
...     title="1984",
...     author="George Orwell",
...     published_date="1949-01-01"
... )

>>> print(book)
# <Book: 1984>
>>> book = Book.objects.get(title="1984")

>>> print(book.title)
# 1984

>>> print(book.author)
# George Orwell

>>> print(book.published_date)
# 1949-01-01
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()

>>> print(book.title)
# Nineteen Eighty-Four
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()

>>> print(book.title)
# Nineteen Eighty-Four
>>> book.delete()
# (1, {'book_shelf.Book': 1})

>>> Book.objects.all()
# <QuerySet []>
