from django.contrib import admin
from .models import Character, Location, Episode

# Register your models here.



class CharacterAdmin(admin.ModelAdmin):

    ordering = ['api_id']

# class LocationAdmin(admin.ModelAdmin):


class EpisodeAdmin(admin.ModelAdmin):
  
    ordering = ['air_date']


    


admin.site.register(Character, CharacterAdmin),
admin.site.register(Location),
admin.site.register(Episode, EpisodeAdmin)