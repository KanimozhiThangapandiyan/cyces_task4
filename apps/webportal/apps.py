from django.apps import AppConfig


class WebportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.webportal'

    def ready(self):
        import apps.webportal.signals

