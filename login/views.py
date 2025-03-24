from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.templatetags.static import static
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'index/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')