from django.contrib import admin
from .models import Character, Location, Episode

# Register your models here.



class CharacterAdmin(admin.ModelAdmin):
    
    list_per_page = 20
    search_fields = ('name',)

    list_display = ('name', 'location', 'status')
    list_filter = (
        ('location', RelatedDropdownFilter),
        ('status', ChoiceDropdownFilter),
        )

    ordering = ['id']



class EpisodeAdmin(admin.ModelAdmin):
  
    ordering = ['air_date']


admin.site.register(Character, CharacterAdmin),
admin.site.register(Location),
admin.site.register(Episode, EpisodeAdmin)