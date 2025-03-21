from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.profiles'

    def ready(self):
        import modules.profiles.signals
