from django.contrib.auth.models import User
from django.utils import timezone
from module_engine.models import ModuleRegistry
from .models import Role

def install():
    """Install the product module"""
    # Create default roles
    Role.objects.get_or_create(name='manager')
    Role.objects.get_or_create(name='user')
    Role.objects.get_or_create(name='public')

def upgrade():
    """Upgrade the product module"""
    module = ModuleRegistry.objects.get(name='product_module')
    module.version = '1.0.1'
    module.update_date = timezone.now()
    module.save()

def uninstall():
    """Uninstall the product module"""