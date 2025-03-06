from django.urls import path
from . import views

app_name = 'engine'
urlpatterns = [
    path('module/', views.ModuleListView.as_view(), name='module_list'),
]