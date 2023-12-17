from django.apps import AppConfig


class AppAigasraUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_aigasra_user'

    def ready(self):
        import app_aigasra_user.signals 