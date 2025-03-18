from django.contrib import admin
from .models import Role, UserRole, Product

admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(Product)