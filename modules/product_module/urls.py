from django.urls import path
from .views import product_landing, product_create, product_delete

app_name = 'product_module'

urlpatterns = [
    path('', product_landing, name='product_landing'),
    path('create/', product_create, name='product_create'),
    path('delete/<int:pk>/', product_delete, name='product_delete'),
]
