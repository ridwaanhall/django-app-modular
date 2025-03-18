"""
URL configuration for django_modular_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('accounts/login/', RedirectView.as_view(url='/login/'), name='login-redirect'),
    path('logout/', views.logout_page, name='logout'),
    path('admin/', admin.site.urls),
    
    path('module/', include('module_engine.urls')),
    path('product/', include('product_module.urls')),
    path('', RedirectView.as_view(url='/module/'), name='home'),
]
