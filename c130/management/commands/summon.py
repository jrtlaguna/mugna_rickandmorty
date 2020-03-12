from django.core.management.base import BaseCommand, CommandError

from c130.models import Character, Episode, Location

import requests
from datetime import datetime
import re
# from urllib.parse import urlparse

pattern = "(\d+)$"
headers = {"content-type": "application/json"}

class Command(BaseCommand):
  

    help = 'Downloads and stores all characters, episodes, and locations from Rick and Morty'


    def handle(self, *args, **kwargs):


        character_url = 'https://rickandmortyapi.com/api/character/'
        location_url = 'https://rickandmortyapi.com/api/location/'
        episode_url = 'https://rickandmortyapi.com/api/episode/'

        # character_info = requests.get(character_url).json()
        

        # for i in range(character_info['info']['count']):
            
        #     character = requests.get(url=f'{character_url}{i+1}').json()

        #     if(Character.objects.filter(name=character['name']).exists()):
        #         continue

        #     print(f"Creating character {character['name']}")
        #     instance = Character(
        #         api_id = character['id'],
        #         name = character['name'],
        #         status = character['status'],
        #         species = character['species'],
        #         type = character['type'],
        #         gender = character['gender'],
        #         image= character['image'],
        #         url = character['url'],
        #         created = character['created']
        #     )
            
        #     origin = character['origin']['name']
        #     location = character['location']['name']

        #     if not Location.objects.filter(name=character['origin']['name']).exists():
        #         origin = Location.objects.create(name=origin)
        #     if not Location.objects.filter(name=character['location']['name']).exists():
        #         location = Location.objects.create(name=location)

        #     origin = Location.objects.filter(name=origin)
        #     location = Location.objects.filter(name=location)


        #     instance.origin = origin.first()
        #     instance.location = location.first()
        #     instance.save()

        
        # location_info = requests.get(location_url).json()

        # for i in range(location_info['info']['count']):

        #     location = requests.get(f'{location_url}{i+1}').json()
            
            

        #     if Location.objects.filter(name=location['name']).exists():
        #         instance = Location.objects.filter(name=location['name']).first()
        #         print(f"Updating {instance.name} info.")
        #     else:
        #         instance = Location.objects.create(name=location['name'])
        #         print(f"Creating location {instance.name}")

        #     instance.type = location['type']
        #     instance.dimension = location['dimension']
        #     instance.url = location['url']
        #     instance.created = location['created']
        #     instance.save()

        episode_info = requests.get(episode_url, headers=headers).json()

        for i in range(episode_info['info']['count']):
        
            episode = requests.get(f'{episode_url}{i+1}', headers=headers).json()


            if Episode.objects.filter(name=episode['name']).exists():
                print(f"Episode {episode['name']} already exists.")
                instance = Episode.objects.filter(name=episode['name']).first()
            else:
                print(f"creating episode {episode['name']}")
                instance = Episode.objects.create(name=episode['name'])

            instance.air_date = datetime.strptime(episode['air_date'], '%B %d, %Y').date()
            instance.code = episode['episode']
            instance.url = episode['url']
            instance.created = episode['created']

            characters = map(get_url_id, episode['characters'])

            instance.characters.add(*characters)
            
            
            # ids = []

            # ids.append(*characters)
            # print(instance.id)
            

            for character in episode['characters']:
                try:
                    c = Character.objects.filter(api_id = get_url_id(character)).first()
                    print(c)
                    c.episodes.add(instance.id)
                    c.save()
                except Exception:
                    continue
                

            instance.save()


                


        
def get_url_id(string):
    return re.search(pattern, string).group(0)


