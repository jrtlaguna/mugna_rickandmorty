from django.test import SimpleTestCase
from django.urls import reverse, resolve

from c130.views import (
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

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        resolver = resolve(url)
        self.assertEquals(resolver.func, home)

    def test_character_detail_url_is_resolved(self):
        url = reverse('character-detail', kwargs={'pk': 23} )
        resolver = resolve(url)
        self.assertEquals(resolver.func.view_class, CharacterDetailView)

    def test_character_list_url_is_resolved(self):
        url = reverse('character-list')
        resolver = resolve(url)
        self.assertEquals(resolver.func.view_class, CharacterListView)

    def test_character_create_url_is_resolved(self):
        url = reverse('character-create')
        resolver = resolve(url)
        self.assertEquals(resolver.func.view_class, CharacterCreateView)

    def test_character_update_url_is_resolved(self):
        url = reverse('character-update', kwargs={'pk': 23} )
        resolver = resolve(url)
        self.assertEquals(resolver.func.view_class, CharacterUpdateView)
        
    def test_character_delete_url_is_resolved(self):
        url = reverse('character-delete', kwargs={'pk': 2400} )
        resolver = resolve(url)
        self.assertEquals(resolver.func.view_class, CharacterDeleteView)

    
    def test_location_list_url_is_resolved(self):
        url = reverse('location-list')
        resolver = resolve(url)
        self.assertEquals(resolver.func.view_class, LocationListView)
        

    def test_location_detail_url_is_resolved(self):
        url = reverse('location-detail', kwargs={'pk': 2323})
        resolver = resolve(url)
        self.assertEquals(resolver.func.view_class, LocationDetailView)
    
    def test_episode_list_url_is_resolved(self):
        url = reverse('episode-list')
        resolver = resolve(url)
        self.assertEquals(resolver.func.view_class, EpisodeListView)