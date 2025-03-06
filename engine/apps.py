from django.apps import AppConfig
import os
import importlib
from django.conf import settings

class EngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engine'

    def ready(self):
        module_dir = os.path.join(settings.BASE_DIR, 'modules')
        if os.path.exists(module_dir):
            for module_name in os.listdir(module_dir):
                if os.path.isdir(os.path.join(module_dir, module_name)):
                    try:
                        importlib.import_module(f'modules.{module_name}.urls')
                    except ImportError:
                        continue
        else:
            os.makedirs(module_dir)