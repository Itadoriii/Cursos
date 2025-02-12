from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

@login_required
def admin_view(request):
    return render(request, 'admin.html')
@login_required
def user_view(request):
    return render(request, 'user.html')
def curso_view(request):
    return render(request, 'curso.html')
def curso2_view(request):
    return render(request, 'curso2.html')
def curso3_view(request):
    return render(request, 'curso3.html')
def curso4_view(request):
    return render(request, 'curso4.html')
def curso5_view(request):
    return render(request, 'curso5.html')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Obtén el email del formulario
        password = request.POST.get('password')  # Obtén la contraseña del formulario

        # Intentar obtener el usuario con el email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        # Si el usuario existe, autenticarlo
        if user is not None:
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                # Redirige a la página principal u otra según el tipo de usuario
                if user.is_superuser:
                    return redirect('admin')  # Redirige a la página de admin.html
                else:
                    return redirect('user')  # Redirige a la página de user.html
            else:
                messages.error(request, 'Credenciales incorrectas, intenta nuevamente.')
        else:
            messages.error(request, 'No existe un usuario con ese email.')
    return render(request, 'login.html')



