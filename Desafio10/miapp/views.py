from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import UserForm, LoginForm
from .models import Users


def home(request):
    return render(request, 'miapp/home.html')

#funcion para loguearse como usuario registrado

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Credenciales inválidas. Intente nuevamente.')
    else:
        form = LoginForm()

    return render(request, 'miapp/login.html', {'form': form})

#funcion para registrar nuevos usuarios

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                form.add_error('password', 'Las contraseñas no coinciden.')
            else:
                user = User.objects.create_user(
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = password,
                )
                user.save()
                # Realizar acciones adicionales si es necesario
                return redirect('login')
    else:
        form = UserForm()

    return render(request, 'miapp/register.html', {'form': form})

#-------------------------------------

def login_exitoso(request):
    return render(request, 'miapp/login_exitoso.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'miapp/profile.html', {'user': user})