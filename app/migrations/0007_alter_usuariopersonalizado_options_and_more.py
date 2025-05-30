# Generated by Django 5.1.6 on 2025-02-27 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_usuariopersonalizado_username_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuariopersonalizado',
            options={},
        ),
        migrations.AlterModelManagers(
            name='usuariopersonalizado',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='validado',
        ),
        migrations.AddField(
            model_name='usuariopersonalizado',
            name='nombre',
            field=models.CharField(default='Desconocido', max_length=255),
        ),
        migrations.AlterField(
            model_name='usuariopersonalizado',
            name='archivo_adjunto',
            field=models.FileField(blank=True, null=True, upload_to='archivos/'),
        ),
        migrations.AlterField(
            model_name='usuariopersonalizado',
            name='direccion',
            field=models.CharField(blank=True, default='Desconocido', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usuariopersonalizado',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usuariopersonalizado',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
