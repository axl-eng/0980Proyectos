from django.apps import AppConfig

class AppNameConfig(AppConfig):
    name = 'app'

    def ready(self):
        from . import urls  # Importa las URL de la aplicación
