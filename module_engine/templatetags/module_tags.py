from django import template
from module_engine.models import ModuleRegistry

register = template.Library()

@register.simple_tag
def is_module_installed(module_name):
    """Check if a module is installed and enabled"""
    try:
        module = ModuleRegistry.objects.get(name=module_name)
        return module.installed and module.enabled
    except ModuleRegistry.DoesNotExist:
        return False