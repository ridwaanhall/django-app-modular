from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils import timezone
from module_engine.models import ModuleRegistry

@receiver(post_migrate)
def register_modules(sender, **kwargs):
    """Register known modules after migrations"""
    if sender.name == 'module_engine':
        # Register the product module if not already registered
        ModuleRegistry.objects.get_or_create(
            name="product_module",
            defaults={
                'version': '1.0.0',
                'installed': False,
                'enabled': False,
                'metadata': {
                    'description': 'Product management module',
                    'author': 'System',
                    'dependencies': []
                }
            }
        )