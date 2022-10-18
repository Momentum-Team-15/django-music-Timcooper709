from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)


class Album(models.Model):
    user = models.ForeignKey('User', related_name='albums', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', related_name='artist_albums', on_delete=models.CASCADE, 
    blank=True, null=True)
    # ForeignKey represents a OZM relationship. The 'One' is 
    # the field and the 'Many' are from the class it is defined on.
    # (many=more than one)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    favorite = models.BooleanField(default=False)   

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

#class Favorite(models.Model):