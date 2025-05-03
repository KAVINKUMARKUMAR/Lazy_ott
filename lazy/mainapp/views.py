from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,JsonResponse
from .models import Nav_banner,Movie_card,generes_card,Actor,Genre
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,UpdateView,DeleteView,ListView,CreateView
from .forms import AddmovieForm,AddgenereForm,AddnavForm,AddactorForm,EditmovieForm
@login_required
def homeView(request):
    context = {
        # context data to be pulled from the DB
        'Nav_banners' : Nav_banner.objects.all(),
        'movies' : Movie_card.objects.all(),
        'generes' : generes_card.objects.all()
        # the above line of code is equivalent to SELECT * FROM product_table;
    }
    return render(request, 'home.html', context)


def movieView(request):
    context = {
        'movies' : Movie_card.objects.all(),
        'genres': Genre.objects.all(),
        # the above line of code is equivalent to SELECT * FROM product_table;
    }
    return render(request, 'movies.html', context)
def seriesView(request):
    context = {
        # the above line of code is equivalent to SELECT * FROM product_table;
    }
    return render(request, 'series.html', context)
def newsView(request):
    context = {
        # the above line of code is equivalent to SELECT * FROM product_table;
    }
    return render(request, 'news.html', context)
def detialView(request, id):
    movie = get_object_or_404(Movie_card, pk=id)
    context = {
        'flim': movie,
        'Nav_banners' : Nav_banner.objects.all(),
        'casts' : Actor.objects.filter(movies__id=id)

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
        movies = Movie_card.objects.all()  # Show all if 0 is passed
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