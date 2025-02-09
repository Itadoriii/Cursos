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