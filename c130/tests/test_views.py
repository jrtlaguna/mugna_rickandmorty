from django.test import TestCase, Client
from django.urls import reverse
from c130.models import Character, Location, Episode
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.character = Character.objects.create(
            name='test',
            status='unknown',
            species='human',
            gender='male',
        )


        self.character_list_url = reverse('character-list')
        self.character_detail_url = reverse('character-detail', args=[self.character.id])
        self.character_create_url = reverse('character-create')
        self.character_delete_url = reverse('character-delete', args=[self.character.id])
        self.character_update_url = reverse('character-update', args=[self.character.id])
        self.location_list_url = reverse('location-list')
        self.episode_list_url = reverse('episode-list')

        

    def test_character_list_GET(self):

        response = self.client.get(self.character_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'characters/list.html')

    def test_location_list_GET(self):
  
        response = self.client.get(self.location_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'locations/list.html')


    def test_character_detail_GET(self):
        response = self.client.get(self.character_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'characters/detail.html')

    def test_character_update_POST(self):
        response = self.client.post(self.character_update_url, {
            'name': 'test',
            'status': 'unknown',
            'species': 'human',
            'gender': 'female'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'characters/update.html')



    def test_character_delete_POST(self):
        response = self.client.post(self.character_delete_url)

        self.assertEquals(response.status_code, 302)



    def test_character_create_POST(self):

        response = self.client.post(self.character_create_url, {
            'name': 'test',
            'status': 'unknown',
            'species': 'human',
            'gender': 'male'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'characters/create.html')


    def test_location_detail_GET(self):


        instance = Location.objects.create(
            name= 'Planet1',
            dimension= 'Dimension1',
            type= 'type-0',
        )
        url = reverse('location-detail', kwargs={'pk': instance.id})

        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'locations/detail.html')
