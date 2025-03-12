from django.shortcuts import render, redirect
from .models import Module

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'modular_engine/module_list.html', {'modules': modules})

def install_module(request, module_name):
    module, created = Module.objects.get_or_create(name=module_name, defaults={'installed': True})
    module.installed = True
    module.save()
    return redirect('module_list')

def uninstall_module(request, module_name):
    module = Module.objects.get(name=module_name)
    module.installed = False
    module.save()
    return redirect('module_list')
