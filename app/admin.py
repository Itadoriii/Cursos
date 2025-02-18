from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Curso, Compra, Contenido

admin.site.register(Curso)
admin.site.register(Compra)
admin.site.register(Contenido)