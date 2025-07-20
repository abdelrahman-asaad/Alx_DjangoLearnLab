from django.urls import path, include
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    

    # auth URLs
    
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.register, name='signup'),  # 
]
#or
   # path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password_reset...
   # path('signup/', signup_view, name='signup'),  # view للتسجيل


