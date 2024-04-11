from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

RATINGS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

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
    
class MovieReview(models.Model):
    date = models.DateField()
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0]
    )
    review = models.CharField(default='')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
    
class ShowReview(models.Model):
    date = models.DateField()
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0]
    )
    review = models.CharField(default='')
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"