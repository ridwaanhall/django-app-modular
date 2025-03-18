from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseForbidden
from django.urls import reverse
from module_engine.models import ModuleRegistry
from .models import Product, Role, UserRole

def check_module_installed():
    """Check if this module is installed and enabled"""
    try:
        module = ModuleRegistry.objects.get(name='product_module')
        return module.installed and module.enabled
    except ModuleRegistry.DoesNotExist:
        return False

def module_installed_required(view_func):
    """Decorator to check if module is installed before accessing views"""
    def _wrapped_view(request, *args, **kwargs):
        if not check_module_installed():
            messages.error(request, "Product module is not installed or not enabled.")
            return redirect('module_engine:module_list')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def get_user_role(user):
    """Get the highest role of a user"""
    if not user.is_authenticated:
        return 'public'
    
    try:
        user_roles = UserRole.objects.filter(user=user).select_related('role')
        role_names = [ur.role.name for ur in user_roles]
        
        if 'manager' in role_names:
            return 'manager'
        elif 'user' in role_names:
            return 'user'
        else:
            return 'public'
    except:
        return 'public'

@module_installed_required
def product_list(request):
    products = Product.objects.all()
    user_role = get_user_role(request.user)
    
    context = {
        'products': products,
        'user_role': user_role,
    }
    return render(request, 'product_module/product_list.html', context)

@module_installed_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user_role = get_user_role(request.user)
    
    context = {
        'product': product,
        'user_role': user_role,
    }
    return render(request, 'product_module/product_detail.html', context)

@login_required
@module_installed_required
def product_create(request):
    user_role = get_user_role(request.user)
    
    # Check if user has appropriate permissions
    if user_role not in ['manager', 'user']:
        return HttpResponseForbidden("You don't have permission to create products.")
    
    if request.method == 'POST':
        # Simple form processing
        name = request.POST.get('name')
        barcode = request.POST.get('barcode')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        # Validate inputs (very basic validation)
        if not all([name, barcode, price, stock]):
            messages.error(request, "All fields are required.")
            return render(request, 'product_module/product_create.html')
        
        try:
            product = Product.objects.create(
                name=name,
                barcode=barcode,
                price=price,
                stock=stock
            )
            messages.success(request, f"Product '{name}' created successfully.")
            return redirect('product_module:product_detail', pk=product.pk)
        except Exception as e:
            messages.error(request, f"Error creating product: {str(e)}")
    
    return render(request, 'product_module/product_create.html')

@login_required
@module_installed_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user_role = get_user_role(request.user)
    
    # Check if user has appropriate permissions
    if user_role not in ['manager', 'user']:
        return HttpResponseForbidden("You don't have permission to update products.")
    
    if request.method == 'POST':
        # Simple form processing
        name = request.POST.get('name')
        barcode = request.POST.get('barcode')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        # Validate inputs (very basic validation)
        if not all([name, barcode, price, stock]):
            messages.error(request, "All fields are required.")
        else:
            try:
                product.name = name
                product.barcode = barcode
                product.price = price
                product.stock = stock
                product.save()
                messages.success(request, f"Product '{name}' updated successfully.")
                return redirect('product_module:product_detail', pk=product.pk)
            except Exception as e:
                messages.error(request, f"Error updating product: {str(e)}")
    
    context = {
        'product': product,
        'user_role': user_role,
    }
    return render(request, 'product_module/product_update.html', context)

@login_required
@module_installed_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user_role = get_user_role(request.user)
    
    # Check if user has appropriate permissions
    if user_role != 'manager':
        return HttpResponseForbidden("You don't have permission to delete products.")
    
    if request.method == 'POST':
        name = product.name
        product.delete()
        messages.success(request, f"Product '{name}' deleted successfully.")
        return redirect('product_module:product_list')
    
    # If not POST, don't delete, just show confirmation
    context = {
        'product': product,
        'user_role': user_role,
    }
    return render(request, 'product_module/product_delete.html', context)