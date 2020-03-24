from django.db.models.signals import post_save
from .models import Character
from django.dispatch import receiver
from django.template.defaultfilters import slugify




def character(sender, instance, created, **kwargs):

    if created:
        if instance.slug is None:
            print("Slug not found")
            instance.slug = instance.slug


# Add if characters stored used slug
# pre_save.connect(character, sender=Character)