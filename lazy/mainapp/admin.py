from django.contrib import admin
from .models import Nav_banner,Movie_card,generes_card,Actor,Genre,language

# Create a custom admin interface
class NavBannerAdmin(admin.ModelAdmin):
    list_display = ('Movie_name', 'Movie_about', 'img')  # Fields to display in the list view
    search_fields = ('Movie_name',)  # Enable search functionality by movie name
    list_filter = ('Movie_name',)  # Add a filter option for Movie_name

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'Character_name', 'img')


# Register the model with the custom admin interface
admin.site.register(Nav_banner, NavBannerAdmin)
admin.site.register(Movie_card)
admin.site.register(generes_card)
admin.site.register(Actor,ActorAdmin)
admin.site.register(Genre)
admin.site.register(language)
