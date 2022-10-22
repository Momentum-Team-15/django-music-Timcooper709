from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, blank=True, null=True) 
    # ForeignKey represents a OZM relationship. The 'One' is 
    # the field and the 'Many' are from the class it is defined on.
    # (many=more than one)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)

    
    def __str__(self):
        return f"{self.title} by {self.artist}"


