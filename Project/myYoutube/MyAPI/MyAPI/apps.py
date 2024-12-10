from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyAPI'

class MyAPIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyAPI'

    def ready(self):
        import MyAPI.signals  # Import signals in the ready() method
