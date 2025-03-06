from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.management import call_command
from django.urls import include, path
import os
import importlib
from .models import InstalledModule

class ModuleListView(View):
    template_name = 'engine/module_list.html'

    def get(self, request, *args, **kwargs):
        module_dir = os.path.join(settings.BASE_DIR, 'modules')
        modules = [name for name in os.listdir(module_dir) if os.path.isdir(os.path.join(module_dir, name))]
        installed_modules = list(InstalledModule.objects.values_list('name', flat=True))
        return render(request, self.template_name, {'modules': modules, 'installed_modules': installed_modules})

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        module_dir = os.path.join(settings.BASE_DIR, 'modules')
        modules = [name for name in os.listdir(module_dir) if os.path.isdir(os.path.join(module_dir, name))]
        installed_modules = list(InstalledModule.objects.values_list('name', flat=True))

        if action:
            module_name = action.split('_')[1]
            app_label = f'modules.{module_name}'

            if action.startswith('install_'):
                if module_name in modules and module_name not in installed_modules:
                    InstalledModule.objects.create(name=module_name)
                    try:
                        call_command('makemigrations', app_label, interactive=False)
                        call_command('migrate', app_label, interactive=False)
                        messages.success(request, f'Module {module_name} installed successfully. Restart the server to apply changes.')
                    except Exception as e:
                        InstalledModule.objects.filter(name=module_name).delete()
                        messages.error(request, f'Install failed: {str(e)}')

            elif action.startswith('upgrade_'):
                if module_name in modules and module_name in installed_modules:
                    try:
                        call_command('makemigrations', app_label, interactive=False)
                        call_command('migrate', app_label, interactive=False)
                        messages.success(request, f'Module {module_name} upgraded successfully.')
                    except Exception as e:
                        messages.error(request, f'Upgrade failed: {str(e)}')

            elif action.startswith('uninstall_'):
                if module_name in installed_modules:
                    InstalledModule.objects.filter(name=module_name).delete()
                    messages.success(request, f'Module {module_name} uninstalled successfully. Restart the server to apply changes.')

        return redirect('engine:module_list')
