from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('media/', views.search, name='all_media'),
    path("api/trendings/", views.view_trendings_results, name="trendings"),
    path('profile/', views.my_profile, name='my_profile'),
    path('media/party', views.party_index, name='party'),
    path('movie/<int:movie_id>/save', views.save_movie, name='save_movie'),
    path('tv/<int:tv_id>/save', views.save_tv_show, name='save_tv_show'),
]