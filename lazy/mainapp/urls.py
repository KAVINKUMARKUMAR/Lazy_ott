from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name = 'home'),
    path('movies/',views.movieView,name= 'movies'),
    path('series/',views.seriesView,name= 'series'),
    path('news/',views.newsView,name= 'news'),
    path('movie/<int:id>/',views.detialView,name= 'detials'),
]