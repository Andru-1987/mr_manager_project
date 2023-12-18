from django.apps import AppConfig


class AppManagerUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_manager_user'

    def ready(self):
        import app_manager_user.signals 