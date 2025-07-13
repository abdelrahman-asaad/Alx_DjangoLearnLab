
---

## 📁 `delete.md`

```markdown
# Delete the book and confirm deletion

```python
>>> from book_shelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Try to retrieve all books
all_books = Book.objects.all()

# Expected output:
# Book deleted successfully; no books in queryset if this was the only one
print(all_books)  # <QuerySet []>
