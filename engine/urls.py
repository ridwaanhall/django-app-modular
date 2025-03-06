from django.urls import path
from .views import ModuleListView

app_name = 'engine'

urlpatterns = [
    path('module/', ModuleListView.as_view(), name='module_list'),
]
