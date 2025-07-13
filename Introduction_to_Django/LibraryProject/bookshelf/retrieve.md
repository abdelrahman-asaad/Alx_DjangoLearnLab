
---

## 📁 `retrieve.md`

```markdown
# Retrieve all attributes of the book

```python
from book_store.models import Book

# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")

# Expected output:
# Book instance with all attributes displayed
print(book.title)           # 1984
print(book.author)          # George Orwell
print(book.published_date)  # 1949-01-01
