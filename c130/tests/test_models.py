from django.test import TestCase

from c130.models import Character, Location, Episode


class TestModels(TestCase):

    def setUp(self):

        self.character = Character.objects.create(
            name='test',
            status='unknown',
            species='human',
            gender='male',
        )

    
    def test_character_has_correct_values(self):
        self.assertEquals(self.character.name, 'test')
        self.assertEquals(self.character.id, self.character.api_id)
