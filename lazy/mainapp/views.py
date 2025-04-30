from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,JsonResponse
from .models import Nav_banner,Movie_card,generes_card,Actor
# Create your views here.
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