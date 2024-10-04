from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Asegúrate de tener una URL llamada 'home' en tu urls.py
            return redirect('http://127.0.0.1:8000/admin/')
        else:
            # Si el usuario no existe o la contraseña es incorrecta, muestra un mensaje de error
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html', {})
