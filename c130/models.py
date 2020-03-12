from django.db import models
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

    api_id      = models.IntegerField(null=True, unique=True)
    name        = models.CharField(max_length=200, unique=True)
    status      = models.CharField(max_length=200, choices=STATUS)
    species     = models.CharField(max_length=200)
    type        = models.CharField(max_length=200, null=True)
    gender      = models.CharField(max_length=50, choices=GENDER)
    image       = models.CharField(max_length=200, null=True)
    origin      = models.ForeignKey('c130.Location', on_delete=models.CASCADE, null=True, related_name='origin')
    location    = models.ForeignKey('c130.Location', null=True, on_delete=models.CASCADE, related_name='residents')
    episodes    = models.ManyToManyField("c130.Episode", verbose_name="Episodes")
    url         = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
        


class Location(models.Model):
    
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=200, null=True)
    dimension = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def get_residents(self):
        qs = Character.objects.filter(location=self.name)

        return qs



class Episode(models.Model):

    name = models.CharField(max_length=200)
    air_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    code = models.CharField(max_length=200)
    characters = models.ManyToManyField("c130.Character", related_name="Characters")
    url = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True)

    
    def __str__(self):
        return self.name


