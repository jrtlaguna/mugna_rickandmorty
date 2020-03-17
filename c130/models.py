from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

import re


# Create your models here.

# pattern = "(\d+)$"

class Character(models.Model):

    STATUS = (
        ('Alive', 'Alive'),
        ('Dead', 'Dead'),
        ('unknown', 'Unknown')
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Genderless', 'Genderless'),
        ('unknown', 'Unknown')
    )

    api_id      = models.IntegerField(null=True, unique=True, blank=True, error_messages={'unique': "Character name already exists"})
    name        = models.CharField(max_length=200, unique=True)
    status      = models.CharField(max_length=200, choices=STATUS)
    species     = models.CharField(max_length=200)
    type        = models.CharField(max_length=200, null=True, blank=True)
    gender      = models.CharField(max_length=50, choices=GENDER)
    image       = models.CharField(max_length=200, null=True, blank=True)
    localImage  = models.ImageField(null=True, blank=True, default="profile1.jpg")
    origin      = models.ForeignKey('c130.Location', on_delete=models.CASCADE, null=True, related_name='origin')
    location    = models.ForeignKey('c130.Location', null=True, on_delete=models.CASCADE, related_name='residents')
    episodes    = models.ManyToManyField("c130.Episode", verbose_name="Episodes", blank=True)
    url         = models.CharField(max_length=200, null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'pk': self.id})


    def get_delete_url(self):
        return reverse('character-list')


class Location(models.Model):
    
    name = models.CharField(max_length=200, unique=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    dimension = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    # def get_residents(self):
    #     qs = Character.objects.filter(location=self.name)

    #     return qs



class Episode(models.Model):

    name = models.CharField(max_length=200)
    air_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    code = models.CharField(max_length=200)
    characters = models.ManyToManyField("c130.Character", related_name="Characters", blank=True)
    url = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    
    def __str__(self):
        return self.name


