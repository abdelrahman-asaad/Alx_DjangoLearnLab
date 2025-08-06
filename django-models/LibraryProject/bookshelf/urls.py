from django.urls import path
from .views import BookListCreateAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name="book_list_create"),
]
#endpoint is: http://localhost:8000/books/