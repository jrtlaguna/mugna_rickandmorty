from django.urls import reverse
from django import forms
from django.forms import ModelForm
from .models import Character, Location, Episode



class CharacterForm(ModelForm):

    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={"placeholder": "Name"}))

    class Meta:

        labels = {
            "localImage": 'Image'
        }

        model = Character
        
        fields = '__all__'
        exclude = ['api_id', 'episodes', 'image']
        