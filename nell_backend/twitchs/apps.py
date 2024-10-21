from django.apps import AppConfig


class TwitchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twitchs'

    def ready(self):
        from . import tasks