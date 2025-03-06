from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.management import call_command
from django.urls import include, path
import os
import importlib

class ModuleListView(View):
    template_name = 'engine/module_list.html'

    def get(self, request, *args, **kwargs):
        module_dir = os.path.join(settings.BASE_DIR, 'modules')
        modules = [name for name in os.listdir(module_dir) if os.path.isdir(os.path.join(module_dir, name))]
        installed_modules = [app.split('.')[-2] for app in settings.INSTALLED_APPS if app.startswith('modules.')]
        return render(request, self.template_name, {'modules': modules, 'installed_modules': installed_modules})

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        module_dir = os.path.join(settings.BASE_DIR, 'modules')
        modules = [name for name in os.listdir(module_dir) if os.path.isdir(os.path.join(module_dir, name))]
        installed_modules = [app.split('.')[-2] for app in settings.INSTALLED_APPS if app.startswith('modules.')]

        if action:
            module_name = action.split('_')[1]
            app_label = f'modules.{module_name}.apps.{module_name.capitalize()}Config'
            if action.startswith('install_'):
                if module_name in modules and app_label not in settings.INSTALLED_APPS:
                    settings.INSTALLED_APPS.append(app_label)
                    try:
                        url_module = importlib.import_module(f'modules.{module_name}.urls')
                        settings.ROOT_URLCONF.__dict__['urlpatterns'].append(
                            path(f'{module_name}/', include(f'modules.{module_name}.urls'))
                        )
                        messages.success(request, f'Module {module_name} installed.')
                    except Exception as e:
                        settings.INSTALLED_APPS.remove(app_label)
                        messages.error(request, f'Install failed: {str(e)}')
            elif action.startswith('upgrade_'):
                if module_name in modules and app_label in settings.INSTALLED_APPS:
                    try:
                        call_command('makemigrations', f'modules.{module_name}', interactive=False)
                        call_command('migrate', f'modules.{module_name}', interactive=False)
                        messages.success(request, f'Module {module_name} upgraded successfully.')
                    except Exception as e:
                        messages.error(request, f'Upgrade failed: {str(e)}')
            elif action.startswith('uninstall_'):
                if app_label in settings.INSTALLED_APPS:
                    settings.INSTALLED_APPS.remove(app_label)
                    messages.success(request, f'Module {module_name} uninstalled.')

        return render(request, self.template_name, {'modules': modules, 'installed_modules': installed_modules})