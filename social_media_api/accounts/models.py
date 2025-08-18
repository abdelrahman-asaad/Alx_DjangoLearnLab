from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)
#-(Self-referential relationship). >> same class objects relationship
#because CustomUser object (user) can follow users and be followed by users (objects) ,
#  and this all in same "User" table
  
  
    def __str__(self):
        return self.username
