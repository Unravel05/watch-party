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
    path('movies/<int:movie_id>', views.movie_detail, name='movie_detail'),
    path('shows/<int:show_id>', views.show_detail, name='show_detail'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='shows_delete'),
    path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='shows_update'),
    path('movies/<int:movie_id>/add_movie_review/', views.add_movie_review, name='add_movie_review'),
    path('shows/<int:show_id>/add_show_review/', views.add_show_review, name='add_show_review'),
    path("tv/<int:tv_id>/", views.view_show_detail, name="view_tv_detail"),
    path("movie/<int:movie_id>/", views.view_movie_detail, name="view_movie_detail"),
]