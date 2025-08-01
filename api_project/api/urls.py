from django.urls import path
from .views import BookList 
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
# endpoint for listing all books is /api/books/
# This will allow you to access the list of books via the URL /api/books/

#___________
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('api/', include(router.urls)),
path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
