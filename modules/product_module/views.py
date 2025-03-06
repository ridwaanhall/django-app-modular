from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from .permissions import has_permission

def get_user_role(request):
    """ Helper function untuk mendapatkan role user. """
    return getattr(request.user, 'role', 'public')

def product_landing(request):
    role = get_user_role(request)
    products = Product.objects.all()
    
    return render(request, 'product_module/product_landing.html', {
        'role': role,
        'products': products
    })

def product_create(request):
    role = get_user_role(request)
    if not has_permission(role, 'create'):
        messages.error(request, "Permission denied.")
        return redirect('product_module:product_landing')

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('product_module:product_landing')
    else:
        form = ProductForm()

    return render(request, 'product_module/product_form.html', {'form': form})

def product_delete(request, pk):
    role = get_user_role(request)
    if not has_permission(role, 'delete'):
        messages.error(request, "Permission denied.")
        return redirect('product_module:product_landing')

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        confirm = request.POST.get('confirm')
        if confirm == 'yes':
            product.delete()
            messages.success(request, "Product deleted successfully!")
        else:
            messages.info(request, "Delete cancelled.")

        return redirect('product_module:product_landing')

    return render(request, 'product_module/product_confirm_delete.html', {'product': product})
