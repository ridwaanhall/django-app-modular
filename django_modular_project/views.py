from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages

def login_page(request):
    if request.user.is_authenticated:
        return redirect('product_module:product_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product_module:product_list')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')