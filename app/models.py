from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UsuarioPersonalizado(AbstractUser):
    # Otros campos personalizados que puedas tener
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_personalizado_set',  # Aquí se cambia el nombre del reverse accessor
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_personalizado_permissions',  # Aquí también se cambia el nombre
        blank=True
    )
from django.db import models
from django.conf import settings

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Compra(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.curso.titulo}"
