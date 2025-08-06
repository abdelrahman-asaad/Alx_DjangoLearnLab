# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books (GET /books/)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access

#permission_classes is built-in to DRF and allows you to set permissions for the view.


# Retrieve a single book by ID (GET /books/<id>/)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (POST /books/)
class BookCreateView(generics.CreateAPIView): #CreateAPIView is used for creating new objects
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_create(self, serializer):
        # Customize logic (optional)
        serializer.save()

#perfom_create is a built-in method that allows you to customize the save behavior
# when creating a new object. 
# it takes a serializer instance as an argument and allows you to call save() on it.
# This is useful for adding additional logic or fields before saving the object.    



# Update a book (PUT/PATCH /books/<id>/)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book (DELETE /books/<id>/)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

