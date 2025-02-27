from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Curso, Compra, Contenido

admin.site.register(Curso)
admin.site.register(Compra)
admin.site.register(Contenido)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

class UsuarioAdmin(UserAdmin):
    model = UsuarioPersonalizado
    list_display = ['email', 'nombre', 'is_active', 'is_staff', 'last_login']
    list_filter = ['is_active', 'is_staff']
    ordering = ['email']
    search_fields = ['email', 'nombre']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'direccion', 'telefono', 'archivo_adjunto')}),
        ('Permisos', {'fields': ('is_active', 'is_staff')}),
        ('Fechas', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'nombre', 'is_active', 'is_staff'),
        }),
    )

admin.site.register(UsuarioPersonalizado, UsuarioAdmin)


