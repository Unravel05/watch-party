from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import Movie, Show

TMDB_API_KEY = '52c430a98c74ec9e45c65e972962aa7b'
TMDB_API_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MmM0MzBhOThjNzRlYzllNDVjNjVlOTcyOTYyYWE3YiIsInN1YiI6IjY2MGVmYmY0YTg4NTg3MDE3Y2VhMjVlNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eNL5Z05d61tQZ1TXUoccaKXxrm3_Nu5IIrme8q4So8Y'
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MmM0MzBhOThjNzRlYzllNDVjNjVlOTcyOTYyYWE3YiIsInN1YiI6IjY2MGVmYmY0YTg4NTg3MDE3Y2VhMjVlNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eNL5Z05d61tQZ1TXUoccaKXxrm3_Nu5IIrme8q4So8Y"
}

# Create your views here.
def home(request):
   return render(request, 'home.html')

def search(request):
    query = request.GET.get('q')
    print(query)

    if query:

        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?query={query}&include_adult=false&language=en-US&page=1", headers=headers)
        print(data.json())
    else:
        return render(request, 'all_media.html', {
           'title': 'Available Media'
        })

    return render(request, 'all_media.html', {
        "data": data.json(),
        "type": request.GET.get("type"),
        "title": f'Results for {query}'
    })

      # query = request.GET.get('q')
      # print(query)

      # if query:
      #   data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?query={query}&include_adult=false&language=en-US&page=1", headers=headers)
      #   print(data.json())
      # else:
      # #   all movies landing page
      #   return render(request, 'all_movies.html', {
      #      "title": 'Movies'
      #   })

      # return render(request, 'all_movies.html', {
      #   "data": data.json(),
      #   "type": request.GET.get("type"),
      #   "title": f'Results for {query}'
      # })

def view_trendings_results(request):
    type = request.GET.get("media_type")
    time_window = request.GET.get("time_window")

    trendings = requests.get(f"https://api.themoviedb.org/3/trending/{type}/{time_window}?api_key={TMDB_API_KEY}&language=en-US")
    return JsonResponse(trendings.json())

def about(request):
   return render(request, 'about.html')

# def shows_index(request):
#    return render(request, 'all_tv_shows.html')

def movies_index(request):
   return render(request, 'all_movies.html')

def party_index(request):
   movies = Movie.objects.all()
   shows = Show.objects.all()
   return render(request, 'party/index.html', {
      'movies': movies,
      'shows': shows
   })

def my_profile(request):
   return render(request, 'my_profile.html')


class MovieCreate(CreateView):
    model = Movie

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ShowCreate(CreateView):
    model = Show

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    # replace '/' with /index
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
