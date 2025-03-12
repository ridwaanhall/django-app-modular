from django.urls import path
from .views import module_list, install_module, uninstall_module

urlpatterns = [
    path('module/', module_list, name='module_list'),
    path('module/install/<str:module_name>/', install_module, name='install_module'),
    path('module/uninstall/<str:module_name>/', uninstall_module, name='uninstall_module'),
]
