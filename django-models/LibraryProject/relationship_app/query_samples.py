books_by_author = Book.objects.filter(author='John Doe')
books_ordered = Book.objects.order_by('title')
try:
    librarian = Librarian.objects.get(name=library_name)
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for library: {library_name}")

