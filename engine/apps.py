from django.apps import AppConfig
import os
from django.conf import settings

class EngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engine'

    def ready(self):
        module_dir = os.path.join(settings.BASE_DIR, 'modules')
        if not os.path.exists(module_dir):
            os.makedirs(module_dir)