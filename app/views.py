from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden

# Decorador para verificar si el usuario es staff o administrador
def is_admin_or_staff(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin_or_staff, login_url='error')
def admin_view(request):
    # Tu lógica para la vista de administración  
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
def error_view(request):
    return render(request, 'error.html')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

User = get_user_model()  # Obtiene el modelo de usuario personalizado

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)  # Autenticar por email

        if user is not None:
            if not user.is_active:
                return redirect("error")  # Usuarios inactivos van a /error
            
            login(request, user)
            
            if user.is_staff:  # Si es admin, va a /administracion
                return redirect("administracion")  
            else:  # Usuarios normales van a /user
                return redirect("user")  

        else:
            return render(request, "login.html", {"error": "Email o contraseña incorrectos"})

    return render(request, "login.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from .forms import RegistroUsuarioForm  # Asegúrate de que el formulario esté bien definido

User = get_user_model()

# views.py
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Hubo un error con el registro. Intenta nuevamente.')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Compra

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Compra, Curso

@login_required
def user_view(request):
    compras = Compra.objects.filter(usuario=request.user).select_related('curso')

    # Si se envía un curso_id por AJAX, devolvemos los detalles en JSON
    curso_id = request.GET.get('curso_id')
    if curso_id:
        curso = get_object_or_404(Curso, id=curso_id)
        contenidos = curso.contenidos.all().values('titulo', 'descripcion', 'archivo', 'video_url')
        data = {
            'titulo': curso.titulo,
            'descripcion': curso.descripcion,
            'contenidos': list(contenidos)
        }
        return JsonResponse(data)

    return render(request, 'user.html', {'compras': compras})


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .models import UsuarioPersonalizado  # Usa tu modelo personalizado

@user_passes_test(is_admin_or_staff)
def admin_view(request):
    # Obtener usuarios no activos
    usuarios_no_activos = UsuarioPersonalizado.objects.filter(is_active=False)
    
    # Puedes añadir el archivo adjunto aquí si lo necesitas
    # Asegúrate de que el modelo de UsuarioPersonalizado tenga un campo de archivo adjunto
    
    return render(request, 'administracion.html', {'usuarios_no_activos': usuarios_no_activos})

from django.shortcuts import redirect, get_object_or_404
from .models import UsuarioPersonalizado  # Usa tu modelo personalizado
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(is_admin_or_staff)
def cambiar_estado_usuario(request, usuario_id):
    # Cambiar a UsuarioPersonalizado
    usuario = get_object_or_404(UsuarioPersonalizado, id=usuario_id)
    
    # Cambiar el estado de activo a True
    if not usuario.is_active:
        usuario.is_active = True
        usuario.save()
    
    return redirect('administracion')
