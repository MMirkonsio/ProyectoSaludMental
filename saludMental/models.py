from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Usuario')
    correo = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electrónico')
    contraseña = models.CharField(max_length=100, verbose_name='Contraseña')
    # Otros campos relacionados con los usuarios (edad, género, etc.)
    creado = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Administrador(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Administrador')
    correo = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electrónico')
    contraseña = models.CharField(max_length=100, verbose_name='Contraseña')
    # Otros campos específicos para administradores (permisos, roles, etc.)
    creado = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'administrador'
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

class Profesional(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Profesional')
    correo = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electrónico')
    contraseña = models.CharField(max_length=100, verbose_name='Contraseña')
    # Otros campos específicos para profesionales (licencia, experiencia, especialización, etc.)
    creado = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'profesional'
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'
