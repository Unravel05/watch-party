from django.forms import ModelForm
from .models import MovieReview, ShowReview

class MovieReviewForm(ModelForm):
  class Meta:
    model = MovieReview
    fields = ['rating', 'review']

class ShowReviewForm(ModelForm):
  class Meta:
    model = ShowReview
    fields = ['rating', 'review']
