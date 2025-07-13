
---

## 📁 `update.md`

```markdown
# Update the title of the book to "Nineteen Eighty-Four"

```python
>>> from bookshelf.models import Book


# Get the book and update title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Expected output:
# Book instance updated successfully
print(book.title)  # Nineteen Eighty-Four
