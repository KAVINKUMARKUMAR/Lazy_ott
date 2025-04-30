from django.db import models
from datetime import date

# Create your models here.
class Nav_banner(models.Model):
    Movie_name = models.CharField(max_length=255) # VARCHAR
    Movie_about = models.TextField()
    img = models.ImageField(upload_to='Movies/')

    def __str__(self):
        return f"Nav_banner: {self.Movie_name}"
    
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    Character_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='cast/')

    def __str__(self):
        return self.name
    
class Movie_card(models.Model):
    Movie_name = models.CharField(max_length=250)
    Movie_rating = models.FloatField()
    img = models.ImageField(upload_to='Movies/')
    movie_poster = models.ImageField(upload_to='Poster/',default="00")
    release_date = models.DateField(default=date.today)
    language = models.ManyToManyField(language,related_name='language')
    genere = models.ManyToManyField(Genre,related_name='generes')
    movie_type = models.CharField(max_length=250,default='popular')
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=100,default='India')
    Revenue = models.IntegerField(default=0)
    Runtime = models.IntegerField(default=0)
    description = models.TextField(default='No description available')
    cast = models.ManyToManyField(Actor,related_name='movies')

    def __str__(self):
        return f"movie_card: {self.Movie_name}"
    
class generes_card(models.Model):
    gen_name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='generes/')

    def __str__(self):
        return f"movie_card: {self.gen_name}"
