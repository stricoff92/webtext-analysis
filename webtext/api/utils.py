
import re
import uuid

from django.conf import settings
from django.db.models import Model

def generate_slug(model:Model) -> str:
    while True:
        slug = uuid.uuid4().hex[:settings.SLUG_LENGTH]
        if model is None or not model.objects.filter(slug=slug).exists():
            return slug



VALID_URL_PATT = re.compile(
    r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})")

def is_valid_url(url:str) -> bool:
    return (
        bool(VALID_URL_PATT.match(url))
        and (
            url.startswith("http://")
            or url.startswith("https://")
        )
    )
