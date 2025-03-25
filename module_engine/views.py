from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
import importlib
import subprocess
from .models import ModuleRegistry

@login_required
def module_list(request):
    modules = ModuleRegistry.objects.all()
    return render(request, 'module_engine/module_list.html', {'modules': modules})

@login_required
def install_module(request, module_name):
    try:
        module = ModuleRegistry.objects.get(name=module_name)
        
        if module.installed:
            messages.warning(request, f"Module {module_name} is already installed.")
            return redirect('module_engine:module_list')
        
        try:
            # subprocess.run(['python', 'manage.py', 'makemigrations', module_name], check=True)
            subprocess.run(['python', 'manage.py', 'migrate', module_name], check=True)
        except subprocess.CalledProcessError:
            messages.error(request, f"Failed to run migrations for {module_name}.")
            return redirect('module_engine:module_list')
        
        try:
            module_app = importlib.import_module(f"{module_name}.installer")
            installer = getattr(module_app, 'install', None)
            
            if installer and callable(installer):
                installer()
        except (ImportError, AttributeError):
            pass
        
        # Update module status
        module.installed = True
        module.enabled = True
        module.install_date = timezone.now()
        module.update_date = timezone.now()
        module.save()
        
        messages.success(request, f"Module {module_name} installed successfully.")
    except ModuleRegistry.DoesNotExist:
        messages.error(request, f"Module {module_name} not found in registry.")
    except Exception as e:
        messages.error(request, f"Error installing module {module_name}: {str(e)}")
    
    return redirect('module_engine:module_list')

@login_required
def upgrade_module(request, module_name):
    try:
        module = ModuleRegistry.objects.get(name=module_name)
        
        if not module.installed:
            messages.warning(request, f"Module {module_name} is not installed.")
            return redirect('module_engine:module_list')
        
        try:
            # subprocess.run(['python', 'manage.py', 'makemigrations', module_name], check=True)
            subprocess.run(['python', 'manage.py', 'migrate', module_name], check=True)
        except subprocess.CalledProcessError:
            messages.error(request, f"Failed to run migrations for {module_name}.")
            return redirect('module_engine:module_list')
        
        try:
            module_app = importlib.import_module(f"{module_name}.installer")
            upgrader = getattr(module_app, 'upgrade', None)
            
            if upgrader and callable(upgrader):
                upgrader()
        except (ImportError, AttributeError):
            pass
        
        module.update_date = timezone.now()
        module.save()
        
        messages.success(request, f"Module {module_name} upgraded successfully.")
    except ModuleRegistry.DoesNotExist:
        messages.error(request, f"Module {module_name} not found in registry.")
    except Exception as e:
        messages.error(request, f"Error upgrading module {module_name}: {str(e)}")
    
    return redirect('module_engine:module_list')

@login_required
def uninstall_module(request, module_name):
    try:
        module = ModuleRegistry.objects.get(name=module_name)
        
        if not module.installed:
            messages.warning(request, f"Module {module_name} is not installed.")
            return redirect('module_engine:module_list')
        
        try:
            module_app = importlib.import_module(f"{module_name}.installer")
            uninstaller = getattr(module_app, 'uninstall', None)
            
            if uninstaller and callable(uninstaller):
                uninstaller()
        except (ImportError, AttributeError):
            # If no uninstaller found, we continue
            pass
        
        module.installed = False
        module.enabled = False
        module.save()
        
        messages.success(request, f"Module {module_name} uninstalled successfully.")
    except ModuleRegistry.DoesNotExist:
        messages.error(request, f"Module {module_name} not found in registry.")
    except Exception as e:
        messages.error(request, f"Error uninstalling module {module_name}: {str(e)}")
    
    return redirect('module_engine:module_list')