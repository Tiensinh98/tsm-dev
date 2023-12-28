from django.apps import AppConfig


class TsmAppConfig(AppConfig):
    name = 'tsm_app'
    models_module = 'tsm_app.app_tools.database.models'
    default_auto_field = 'django.db.models.BigAutoField'
