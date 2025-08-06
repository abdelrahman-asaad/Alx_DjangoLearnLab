#from django.shortcuts import render


#creating api to handle books in bookshelf app through add books 'Post' and
#read books'Get' requests

#maybe we can add delete and update books in the future through 'Delete' and 'Put'
# requests

# Create your views here.

#Define a view for your model in the views.py file:
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView): #inherting from ListCraeteAPIView class
    queryset = Book.objects.all() #to get all books in database #queryset used to select the data returned
    serializer_class = BookSerializer


#ListCreateAPIView class is a generic view provided by Django REST Framework that 
# allows you to handle both listing and creating objects in a single view by 
# poviding format.
  
    #___________or____
#from rest_framework.response import Response
#from rest_framework.decorators import api_view #decerator that turns function based view to APIView
#from .models import Book
#from .serializers import BookSerializer

#@api_view(['GET'])       #decerator that accepts only 'get' http requests
#def book_list(request):
#    books = Book.objects.all()  #to get all books in database
#    serializer = BookSerializer(books, many=True)  #to turn all Book objects 'books' into json format , many=True to handle many objects not just one
#    return Response(serializer.data)               #return the response in json format

'''🧠 أشهر الـ Methods:
Method	الاستخدام	مثال عملي
GET	الحصول على بيانات	عرض كل الكتب أو كتاب معيّن
POST	إنشاء بيانات جديدة	إنشاء كتاب جديد في قاعدة البيانات
PUT	تعديل كامل لعنصر موجود	تعديل بيانات كتاب بالكامل
PATCH	تعديل جزئي لعنصر موجود	تعديل العنوان فقط لكتاب
DELETE	حذف عنصر معين	حذف كتاب من قاعدة البيانات

'''