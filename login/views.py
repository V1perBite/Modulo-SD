from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        
        else:
            form = AuthenticationForm()
        return render(request, 'login', {'form': form})


def register_view(request):
    pass

@login_required
def home_view(request):
    return render(request, 'home')