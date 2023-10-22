from django.contrib import admin
from .models import Usuario, Administrador, Profesional

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'correo']

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'correo']

class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'correo']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Profesional, ProfesionalAdmin)
