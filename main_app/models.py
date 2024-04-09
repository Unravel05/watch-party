from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

# Create your models here.

class Movie(models.Model):
    title = models.CharField(default='')
    genre = models.CharField(default='')
    description = models.TextField(default='')
    poster = models.CharField(default='')
    progress = models.CharField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Show(models.Model):
    title = models.CharField(default='')
    genre = models.CharField(default='')
    season = models.CharField(default='')
    description = models.TextField(default='')
    poster = models.CharField(default='')
    progress = models.CharField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title