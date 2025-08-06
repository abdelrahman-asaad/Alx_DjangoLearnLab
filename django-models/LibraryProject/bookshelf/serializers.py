#-Serialization: DRF simplifies the process of converting complex data structures, such as Django models,
# into formats like JSON or XML, making it suitable for consumption by various clients.
#الوظيفة الأساسية:
#تحويل Model instance إلى JSON → لما تبعت البيانات لمستخدم أو Frontend.
#تحويل JSON إلى Model instance → لما تستقبل بيانات من المستخدم (POST/PUT...).

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # ['title', 'author', 'publication_year']


