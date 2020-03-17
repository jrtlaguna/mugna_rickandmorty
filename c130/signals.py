from django.db.models.signals import post_save
from .models import Character



def character(sender, instance, created, **kwargs):

    if created:
        if instance.api_id is None:
            print('Found no api_id for instance.')
            instance.api_id = instance.id
            print(f"{{instance.name}} api_id set to {{instance.id}}")



post_save.connect(character, sender=Character)