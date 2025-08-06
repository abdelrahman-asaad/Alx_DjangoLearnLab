from .models import Book, Author
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author'] #__all__

    def validate_publication_year(self, value): # Custom validation for publication_year
        if value < 0:
            raise serializers.ValidationError("Publication year cannot be negative.")
        return value     
    
    #should use validate_field_name(self, value):
    #to ensure that the field mentioned is validated correctly

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) 
    # Nested serializer to include books by the author
    # 'many=True' indicates that an author can have multiple books
    #read_only=True means we won't allow creating/updating books through this serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Include books in the serialized output


# Comments:
# - Author model represents a writer with a name field.
# - Book model represents a book that is linked to an Author using a ForeignKey.
# - BookSerializer includes all book fields and validates that the publication_year is not in the future.
# - AuthorSerializer includes the author's name and a nested list of their books.
# - The related_name='books' in the Book model allows reverse access from Author to Book as author.books.all().

# Steps to implement:
# 1. Add models to api/models.py.
# 2. Run: python manage.py makemigrations && python manage.py migrate
# 3. Add serializers to api/serializers.py.

# 4. Test in Django shell:
# >>> from api.models import Author, Book
# >>> a = Author.objects.create(name='George Orwell')
# >>> Book.objects.create(title='1984', publication_year=1949, author=a)
# >>> from api.serializers import AuthorSerializer
# >>> AuthorSerializer(a).data

'''أيوه طبعًا، Step 6: Implement and Test ممكن تنفذها بالكامل من خلال Django Admin Panel أو Django shell.

هنشرح هنا خطوة بخطوة ازاي تختبر الموديلات والـ serializers من خلال Django Admin:

✅ 1. تفعيل الموديلات في Admin Panel
لو لسه ما ضفتش الموديلات في admin، افتح api/admin.py وأضف:

python
نسخ
تحرير
from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)

✅ 2. إنشاء مستخدم أدمن
لو لسه ما عندكش superuser، أنشئه بـ:

bash
نسخ
تحرير
python manage.py createsuperuser

✅ 3. شغل السيرفر وروح على لوحة الإدارة
bash
نسخ
تحرير
python manage.py runserver
ثم افتح الرابط:
http://127.0.0.1:8000/admin
وسجّل دخولك باستخدام الـ superuser.

✅ 4. الاختبار من داخل Admin
🔹 إنشاء Author:
من لوحة التحكم، اختر "Authors"

اضغط على "Add"

أضف الاسم فقط (مثلاً: "George Orwell")

🔹 إنشاء Book:
من "Books"، اضغط "Add"

أدخل البيانات:

Title: "1984"

Publication Year: "1949"

Author: اختر "George Orwell"

لو أدخلت سنة مستقبلية، المفروض يظهر لك الخطأ اللي كتبناه في الـ serializer:

python
نسخ
تحرير
raise serializers.ValidationError("Publication year cannot be in the future.")
لكن خلي بالك:

الـ validation ده بيشتغل في الـ API وليس في الـ Admin panel.
لو عايز تطبقه كمان في الـ admin، لازم تضيف validation داخل models.py أو تعمل custom form.

✅ 5. تشغيل من Django Shell لاختبار الـ Serializer
لو عايز تختبر الـ Serializer يدويًا:

bash
نسخ
تحرير
python manage.py shell
python
نسخ
تحرير
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

author = Author.objects.create(name="Haruki Murakami")
book1 = Book.objects.create(title="Kafka on the Shore", publication_year=2002, author=author)
book2 = Book.objects.create(title="Norwegian Wood", publication_year=1987, author=author)

serializer = AuthorSerializer(author)
print(serializer.data)
هتشوف نتيجة زي:

python
نسخ
تحرير
{
  'name': 'Haruki Murakami',
  'books': [
    {'title': 'Kafka on the Shore', 'publication_year': 2002, 'author': 1},
    {'title': 'Norwegian Wood', 'publication_year': 1987, 'author': 1}
  ]
}'''