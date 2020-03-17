from c130.forms import CharacterForm
from django.test import TestCase

class TestForms(TestCase):

    def test_character_valid_data(self):
        form = CharacterForm(data={
            'name': 'formTest',
            'status': 'unknown',
            'species': 'human',
            'gender': 'Male',
        })

        print(form.errors)

    def test_character_invalid_data(self):

        form = CharacterForm(data={
            'name': 'formTest',
            'status': 'unknown',
            'species': 'human',
            'gender': 'male',
        })

        self.assertFalse(form.is_valid())