import django_filters
from django_filters import CharFilter, ChoiceFilter


from .models import Character

class CharacterFilter(django_filters.FilterSet):
    name = CharFilter(lookup_expr='icontains', label="Name")
    species = CharFilter(lookup_expr='icontains', label="Species")
    # location = CharFilter(lookup_expr='icontains')
    # status = ChoiceFilter(Character.status, lookup_expr='iexact')

    class Meta:
        model = Character
        fields = ['name', 'location', 'status', 'species', 'gender']

