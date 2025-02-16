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
    return render(request, 'administracion.html')
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
                    return redirect('administracion')  # Redirige a la página de admin.html
                else:
                    return redirect('user')  # Redirige a la página de user.html
            else:
                messages.error(request, 'Credenciales incorrectas, intenta nuevamente.')
        else:
            messages.error(request, 'No existe un usuario con ese email.')
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print("Datos recibidos:", name, email, password)  # Para depuración

        # Verificar si todos los campos tienen datos
        if not name or not email or not password:
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'register.html')

        # Verificar si el email ya está registrado
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado.')
        else:
            # Crear el usuario (no administrador)
            username = email.split('@')[0]  # Puedes usar otra lógica para el username
            user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
            user.save()

            print("Usuario creado:", user)  # Para depuración
            messages.success(request, 'Cuenta creada con éxito. Ahora puedes iniciar sesión.')
            return redirect('login')
    
    return render(request, 'register.html')



