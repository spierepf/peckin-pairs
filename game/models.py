from django.core.validators import URLValidator
from django.db import models
from django.core.exceptions import ValidationError

import random

# Create your models here.
validate_url = URLValidator()


def validate_image_urls(value):
    if not isinstance(value, list):
        raise ValidationError("This field must contain a list.")
    if len(value) != 11:
        raise ValidationError("This field must contain exactly eleven entries.")
    for entry in value:
        validate_url(entry)
    if len(set(value)) != len(value):
        raise ValidationError("This field must contain distinct entries.")


def default_image_urls():
    return [f"http://picsum.photo/seed/{i}/500" for i in random.sample(range(1, 100001), 11)]


class GameRound(models.Model):
    image_urls = models.JSONField(default=default_image_urls, validators=[validate_image_urls])
