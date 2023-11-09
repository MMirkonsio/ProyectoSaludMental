from django.contrib import admin
from .models import Usuario, Administrador, Profesional, Publicacion

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'correo']

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'correo']

class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'correo']

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'etiquetas', 'get_autor', 'fecha_publicacion')

    def get_autor(self, obj):
        return obj.autor.username
    get_autor.short_description = 'Autor'

admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Profesional, ProfesionalAdmin)
