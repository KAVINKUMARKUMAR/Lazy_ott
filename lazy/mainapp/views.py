from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from .models import Nav_banner, Movie_card, generes_card, Actor ,Series_card,Genre
from django.views.generic import DetailView,UpdateView,DeleteView,ListView,CreateView
from .forms import AddmovieForm,AddgenereForm,AddnavForm,AddactorForm,EditmovieForm
@login_required
def homeView(request):
    context = {
        'Nav_banners' : Nav_banner.objects.all(),
        'movies' : Movie_card.objects.all(),
        'series_list': Series_card.objects.all(),  # 👈 Add this line
        'generes' : generes_card.objects.all()
    }
    return render(request, 'home.html', context)



def movieView(request):
    movie_list = Movie_card.objects.all()
    context = {
        'movies' : Movie_card.objects.all(),
        'genres': Genre.objects.all(),
    }
    return render(request, 'movies.html', context)
def seriesView(request):
    context = {
        'Series_card': Series_card.objects.all(),
        'Series_genere': Genre.objects.all(),  # Fix the variable name for genre
    }
    return render(request, 'series.html', context)

def newsView(request):
    context = {

    }
    return render(request, 'news.html', context)
def detailView(request, pk):
    movie = get_object_or_404(Movie_card, pk=pk)
    context = {
        'flim': movie,
        'Nav_banners' : Nav_banner.objects.all(),
        'casts' : Actor.objects.filter(movies__id=pk)

    }
    return render(request, 'movie_detials.html', context)
class AddMovie(CreateView):
    model = Movie_card
    template_name = 'add_movie.html'
    form_class = AddmovieForm
    success_url = '/'
class Addgenere(CreateView):
    model = generes_card
    template_name = 'generes_card.html'
    form_class = AddgenereForm
    success_url = '/'
class Addnav(CreateView):
    model = Nav_banner
    template_name = 'add_nav.html'
    form_class = AddnavForm
    success_url = '/'
class Addactor(CreateView):
    model = Actor
    template_name = 'add_actors.html'
    form_class = AddactorForm
    success_url = '/'
class Editmovie(UpdateView):
    model = Movie_card
    template_name = 'edit_movie.html'
    form_class = EditmovieForm
    success_url = '/'
    
def movies_by_genre(request, genre_id):
    if genre_id == 0:
        movies = Movie_card.objects.all()
    else:
        movies = Movie_card.objects.filter(genere__id=genre_id).distinct()

    movie_data = [{
        'id': movie.id,
        'name': movie.Movie_name,
        'image': movie.img.url,
        'rating': movie.Movie_rating,
    } for movie in movies]

    return JsonResponse({'movies': movie_data})


def movie_list_view(request):
    movies = Movie_card.objects.all()
    genres = Genre.objects.all()
    return render(request, 'your_template.html', {
        'movies': movies,
        'genres': genres
    })

def search_movies(request):
    query = request.GET.get('q', '')
    if query:
        movies = Movie_card.objects.filter(
            Q(Movie_name__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        movies = Movie_card.objects.all()

    data = {
        "movies": [
            {
                "id": movie.id,
                "name": movie.Movie_name,
                "rating": movie.Movie_rating,
                "image": movie.img.url,
            }
            for movie in movies
        ]
    }
    return JsonResponse(data)
def series_by_genre(request, genre_id):
    if genre_id == 0:
        series_list = Series_card.objects.all()
    else:
        series_list = Series_card.objects.filter(Series_genere__id=genre_id)

    data = {
        "series": [
            {
                "id": s.id,  # ✅ This is important
                "name": s.Series_name,
                "image": s.Series_img.url,
                "rating": s.Series_rating
            } for s in series_list
        ]
    }
    return JsonResponse(data)


def SeriesdetailView(request, pk):
    series = get_object_or_404(Series_card, pk=pk)
    context = {
        'sere': series,
        'Nav_banners': Nav_banner.objects.all(),
        'casts': Actor.objects.filter(Series_movies__id=pk)
    }
    return render(request, 'series_detials.html', context)
