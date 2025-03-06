from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import os
from .models import InstalledModule

class ModuleListView(View):
    template_name = 'engine/module_list.html'

    def get(self, request, *args, **kwargs):
        module_dir = os.path.join(settings.BASE_DIR, 'modules')

        if not os.path.exists(module_dir):
            os.makedirs(module_dir)

        modules = [name for name in os.listdir(module_dir) if os.path.isdir(os.path.join(module_dir, name))]
        installed_modules = list(InstalledModule.objects.values_list('name', flat=True))

        return render(request, self.template_name, {
            'modules': modules,
            'installed_modules': installed_modules
        })

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        module_name = '_'.join(action.split('_')[1:]) if action else None

        if not module_name:
            messages.error(request, "Invalid action!")
            return redirect('engine:module_list')

        module_path = os.path.join(settings.BASE_DIR, 'modules', module_name)

        print(f"Checking module path: {module_path}")

        if not os.path.exists(module_path):
            messages.error(request, f"Module {module_name} not found!")
            return redirect('engine:module_list')

        if action.startswith('install_'):
            if module_name not in InstalledModule.objects.values_list('name', flat=True):
                InstalledModule.objects.create(name=module_name)
                messages.success(request, f'Module {module_name} installed. Restart the server to apply changes.')
        elif action.startswith('uninstall_'):
            InstalledModule.objects.filter(name=module_name).delete()
            messages.success(request, f'Module {module_name} uninstalled. Restart the server to apply changes.')
        elif action.startswith('upgrade_'):
            messages.success(request, f'Module {module_name} upgraded. Apply database migrations if needed.')

        return redirect('engine:module_list')
