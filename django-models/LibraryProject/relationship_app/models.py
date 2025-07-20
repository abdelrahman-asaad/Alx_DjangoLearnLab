from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    class Meta:           #for adding specific permissions
        permissions = [
            ("can_add_book", "Can add book"),      #name in database and name in forms
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

        #___________________________
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)  #User is a built-in class
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

## relationship_app/signals.py

#from django.db.models.signals import post_save
#from django.contrib.auth.models import User
#from django.dispatch import receiver
#from .models import UserProfile

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(user=instance)

## relationship_app/apps.py

#from django.apps import AppConfig

#class RelationshipAppConfig(AppConfig):
#    default_auto_field = 'django.db.models.BigAutoField'
#    name = 'relationship_app'

#    def ready(self):
#        import relationship_app.signals  # ← دا اللي بيفعل الإشارة


##INSTALLED_APPS = [
    
#    'relationship_app.apps.RelationshipAppConfig',
    
#]
