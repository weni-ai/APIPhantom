from django.conf import settings
from django.utils.module_loading import import_string

from application.fackers import Faker


def get_faker() -> Faker:
    return import_string(settings.FAKER_CLASS)()
