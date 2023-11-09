from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Importa el modelo de usuario de Django

class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Usuario')
    correo = models.EmailField(max_length=100, unique=True, verbose_name='Correo Electrónico')
    contraseña = models.CharField(max_length=100, verbose_name='Contraseña')
    foto_de_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True, verbose_name='Foto de Perfil')
    creado = models.DateTimeField(auto_now_add=True)

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
    creado = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'profesional'
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'



class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=255, default='')
    contenido = models.TextField()
    etiquetas = models.CharField(max_length=100, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'publicacion'
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

