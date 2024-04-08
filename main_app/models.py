from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Show(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)