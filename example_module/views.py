from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def landing_page(request):
    """Menampilkan daftar produk (dapat diakses oleh semua user)"""
    products = Product.objects.all()
    return render(request, 'example_module/landing.html', {'products': products})

@login_required
@permission_required('example_module.add_product', raise_exception=True)
def add_product(request):
    """Hanya User & Manager yang bisa menambah produk"""
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil ditambahkan.")
            return redirect('landing_page')
    else:
        form = ProductForm()
    return render(request, 'example_module/product_form.html', {'form': form})

@login_required
@permission_required('example_module.change_product', raise_exception=True)
def edit_product(request, product_id):
    """Hanya User & Manager yang bisa mengedit produk"""
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil diperbarui.")
            return redirect('landing_page')
    else:
        form = ProductForm(instance=product)
    return render(request, 'example_module/product_form.html', {'form': form})

@login_required
@permission_required('example_module.delete_product', raise_exception=True)
def delete_product(request, product_id):
    """Hanya Manager yang bisa menghapus produk"""
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Produk berhasil dihapus.")
        return redirect('landing_page')
    return render(request, 'example_module/confirm_delete.html', {'product': product})