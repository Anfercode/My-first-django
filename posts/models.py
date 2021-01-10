"""Post models"""

#Django
from django.db import models

# Create your models here.

class user(models.Model):
    """ User Model """

    uuid = models.UUIDField(unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)