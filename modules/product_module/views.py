from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Product

def get_user_role(user):
    if user.is_superuser:
        return 'manager'
    elif user.is_authenticated:
        return 'user'
    return 'public'

class RoleRequiredMixin(UserPassesTestMixin):
    required_roles = []

    def test_func(self):
        return get_user_role(self.request.user) in self.required_roles

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to access this page.')
        return redirect('product_module:product_list')

class ProductListView(ListView):
    model = Product
    template_name = 'product_module/product_landing.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['role'] = get_user_role(self.request.user)
        return context

class ProductCreateView(RoleRequiredMixin, CreateView):
    model = Product
    template_name = 'product_module/product_landing.html'
    fields = ['name', 'barcode', 'price', 'stock']
    success_url = reverse_lazy('product_module:product_list')
    required_roles = ['manager', 'user']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Product created successfully!')
        return super().form_valid(form)

class ProductUpdateView(RoleRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_module/product_landing.html'
    fields = ['name', 'barcode', 'price', 'stock']
    success_url = reverse_lazy('product_module:product_list')
    required_roles = ['manager', 'user']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully!')
        return super().form_valid(form)

class ProductDeleteView(RoleRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_module/product_landing.html'
    success_url = reverse_lazy('product_module:product_list')
    required_roles = ['manager']

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Product deleted successfully!')
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'delete'
        return context