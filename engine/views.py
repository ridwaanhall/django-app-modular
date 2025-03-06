from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import os
import importlib

class ModuleListView(View):
    template_name = 'engine/module_list.html'

    def get(self, request, *args, **kwargs):
        module_dir = os.path.join(settings.BASE_DIR, 'modules')
        modules = [name for name in os.listdir(module_dir) if os.path.isdir(os.path.join(module_dir, name))]
        return render(request, self.template_name, {'modules': modules})

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        module_dir = os.path.join(settings.BASE_DIR, 'modules')
        modules = [name for name in os.listdir(module_dir) if os.path.isdir(os.path.join(module_dir, name))]

        if action:
            module_name = action.split('_')[1]
            if action.startswith('install_'):
                if module_name in modules:
                    settings.INSTALLED_APPS.append(f'modules.{module_name}.apps.{module_name.capitalize()}Config')
                    messages.success(request, f'Module {module_name} installed.')
            elif action.startswith('upgrade_'):
                messages.success(request, f'Module {module_name} upgraded.')
            elif action.startswith('uninstall_'):
                if f'modules.{module_name}.apps.{module_name.capitalize()}Config' in settings.INSTALLED_APPS:
                    settings.INSTALLED_APPS.remove(f'modules.{module_name}.apps.{module_name.capitalize()}Config')
                    messages.success(request, f'Module {module_name} uninstalled.')

        return render(request, self.template_name, {'modules': modules})