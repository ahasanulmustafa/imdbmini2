from django.apps import AppConfig


class Imdb1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'imdb1'

    def ready(self):
        import imdb1.signals


