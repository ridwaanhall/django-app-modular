from django.shortcuts import render
from .models import Product

def landing_page(request):
    products = Product.objects.all()
    return render(request, 'example_module/landing.html', {'products': products})
