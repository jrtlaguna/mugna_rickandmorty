from django.urls import path
from django.conf.urls import handler404

from .views import (
    CharacterListView,
    CharacterDetailView,
    CharacterCreateView,
    CharacterUpdateView,
    CharacterDeleteView,
    LocationListView,
    LocationDetailView,
    EpisodeListView,
    home
    )

urlpatterns = [
    path('', home, name='home'),
    path('characters/', CharacterListView.as_view(), name='character-list'),
    path('characters/<int:pk>', CharacterDetailView.as_view(), name='character-detail'),
    path('characters/create/', CharacterCreateView.as_view(), name='character-create'),
    path('characters/<int:pk>/update/', CharacterUpdateView.as_view(), name='character-update'),
    path('characters/<int:pk>/delete/', CharacterDeleteView.as_view(), name='character-delete'),

    path('locations', LocationListView.as_view(), name='location-list'),
    path('locations/<int:pk>', LocationDetailView.as_view(), name='location-detail'),
    path('episodes', EpisodeListView.as_view(), name='episode-list'),
]


handler404 = 'c130.views.error404'