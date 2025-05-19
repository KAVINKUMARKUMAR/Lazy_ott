from django.urls import path
from . import views
from .views import search_movies

urlpatterns = [
    path('', views.homeView, name = 'home'),
    path('movies/',views.movieView,name= 'movies'),
    path('series/',views.seriesView,name= 'series'),
    path('news/',views.newsView,name= 'news'),
    path('movie/<int:pk>/', views.detailView, name='details'),
    path('series/<int:pk>/', views.SeriesdetailView, name='seriesdetails'),
    path('movie/add/',views.AddMovie.as_view(),name='movie_add'),
    path('movie/genere/',views.Addgenere.as_view(),name='genere_add'),
    path('movie/nav/',views.Addnav.as_view(),name='nav_add'),
    path('movie/actor/',views.Addactor.as_view(),name='add_actor'),
    path('movie/editmovie/<int:pk>/',views.Editmovie.as_view(),name='edit_movie'),
    path('movies/genre/<int:genre_id>/', views.movies_by_genre, name='movies_by_genre'),
    path('movies/search/', search_movies, name='search_movies'),
    path('series_by_genre/<int:genre_id>/', views.series_by_genre, name='series_by_genre'),
]