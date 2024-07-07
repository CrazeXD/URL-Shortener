from typing import Any
from django.db import models
# import usermodel
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    api_key = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.username

class URL(models.Model):
    url = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.url