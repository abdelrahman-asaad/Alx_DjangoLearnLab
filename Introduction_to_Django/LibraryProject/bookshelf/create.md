# Create a Book instance

```python
from book_store.models import Book

# Create a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    published_date="1949-01-01"
)

# Expected output:
# A new Book instance with ID (e.g., 1) should be created successfully
# <Book: 1984>
print(book)
