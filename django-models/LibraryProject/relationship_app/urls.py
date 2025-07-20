from django.urls import path, include
from .views import list_books, LibraryDetailView, SignUpView

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    

    # auth URLs
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password_reset...
    path('signup/', views.SignUpView.as_view(), name='signup'),  # view للتسجيل
]

]
