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