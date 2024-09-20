from django.apps import AppConfig


class Test1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.test1'

    def ready(self):
        import apps.test1.signals
        