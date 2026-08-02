from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import GameRound


# Create your tests here.
class GameRoundModelTestCase(TestCase):
    def test_each_game_round_image_urls_must_be_a_list_of_eleven_distinct_urls(self):
        GameRound.objects.create(image_urls=[f"http://picsum.photo/seed/{i}/500" for i in range(1, 12)]).full_clean()

        # dicts need not apply
        with self.assertRaises(ValidationError):
            GameRound.objects.create(
                image_urls={i: f"http://picsum.photo/seed/{i}/500" for i in range(1, 12)}).full_clean()

        # twelve thou shalt not count
        with self.assertRaises(ValidationError):
            GameRound.objects.create(
                image_urls=[f"http://picsum.photo/seed/{i}/500" for i in range(1, 13)]).full_clean()

        # neither count thou ten, excepting that thou then proceed to eleven
        with self.assertRaises(ValidationError):
            GameRound.objects.create(
                image_urls=[f"http://picsum.photo/seed/{i}/500" for i in range(1, 11)]).full_clean()

        # the image urls must be distinct
        with self.assertRaises(ValidationError):
            GameRound.objects.create(
                image_urls=[f"http://picsum.photo/seed/1/500" for i in range(1, 12)]).full_clean()

    def test_default_game_rounds_are_valid(self):
        GameRound.objects.create().full_clean()
