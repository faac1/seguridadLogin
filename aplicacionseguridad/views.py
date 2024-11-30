from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Guardar el usuario y realizar el login automático
            user = form.save()
            login(request, user)
            messages.success(request, 'Te has registrado correctamente!')
            return redirect('login')  # Redirige al home después de registrarse
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})







def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Verificar las credenciales del usuario
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Si las credenciales son correctas, inicia la sesión del usuario
                login(request, user)
                next_url = request.GET.get('next', 'pagprote')  # Redirigir a la página deseada
                messages.success(request, 'Has iniciado sesión correctamente')
                return redirect(next_url)
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # O redirige a donde necesites

@login_required
def pagprote(request):
    return render(request, 'pagprote.html')