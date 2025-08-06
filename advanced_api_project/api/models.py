from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    #because one author can write many books, we use ForeignKey to link Book to Author
    #related_name allows us to access books from an author instance
    def __str__(self):
        return self.title    