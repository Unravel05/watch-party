from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('shows/', views.shows_index, name='all_tv_shows'),
    path('movies/', views.movies_index, name='all_movies'),
    path('profile/', views.my_profile, name='my_profile'),
    path('movies/party', views.party_index, name='party')
]