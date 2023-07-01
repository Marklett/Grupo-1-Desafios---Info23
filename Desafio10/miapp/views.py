from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'miapp/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        login_attempts = request.session.get('login_attempts', 0)

        if login_attempts >= 3:
            # Se han superado los intentos de inicio de sesión permitidos
            return redirect('home')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_user(request, user)
            request.session['login_attempts'] = 0
            return redirect('login_exitoso')
        else:
            login_attempts += 1
            request.session['login_attempts'] = login_attempts

            if login_attempts >= 3:
                return redirect('home')

            return render(request, 'miapp/login.html', {'error': 'Usuario o contraseña incorrectos.'})

    return render(request, 'miapp/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request, 'miapp/register.html', {'error': 'El nombre de usuario ya está en uso.'})

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')

    return render(request, 'miapp/register.html')

def login_exitoso(request):
    return render(request, 'miapp/login_exitoso.html')

def logout_view(request):
    logout(request)
    return redirect('home')
