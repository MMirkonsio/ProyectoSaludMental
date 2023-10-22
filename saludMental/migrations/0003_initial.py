# Generated by Django 4.2.4 on 2023-10-21 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('saludMental', '0002_auto_20231021_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Administrador')),
                ('correo', models.EmailField(max_length=100, unique=True, verbose_name='Correo Electrónico')),
                ('contraseña', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
                'db_table': 'administrador',
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Profesional')),
                ('correo', models.EmailField(max_length=100, unique=True, verbose_name='Correo Electrónico')),
                ('contraseña', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Profesional',
                'verbose_name_plural': 'Profesionales',
                'db_table': 'profesional',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Usuario')),
                ('correo', models.EmailField(max_length=100, unique=True, verbose_name='Correo Electrónico')),
                ('contraseña', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
    ]
