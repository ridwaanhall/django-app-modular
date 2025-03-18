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
    
    # You could add sample products here if needed

def upgrade():
    """Upgrade the product module"""
    # Update module metadata or apply any fixes needed during upgrade
    module = ModuleRegistry.objects.get(name='product_module')
    module.version = '1.0.1'  # Increment version
    module.update_date = timezone.now()
    module.save()

def uninstall():
    """Uninstall the product module"""
    # You can add cleanup logic here if needed
    # But the main tables will remain since Django doesn't drop tables on uninstall
    # This is handled by the module engine which disables access to this module