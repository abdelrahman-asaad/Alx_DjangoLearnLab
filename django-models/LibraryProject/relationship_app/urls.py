from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    

    # auth URLs
    
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.register, name='signup'),  # 

#or
   # path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password_reset...
   # path('signup/', signup_view, name='signup'),  # view للتسجيل






    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),
]


