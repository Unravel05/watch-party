from django.contrib import admin
from .models import Movie, Show, MovieReview, ShowReview

# Register your models here.
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(MovieReview)
admin.site.register(ShowReview)