from django.shortcuts import render,redirect
from .models import Publicacion, Usuario
from django.contrib.auth import logout

def login(request):
    if request.method == 'POST':
        # Procesar el inicio de sesión aquí
        # Aquí debes utilizar la función 'auth_login' de Django para autenticar al usuario
        # y establecer la sesión.
        # Verifica si las credenciales son correctas y autentica al usuario.

        # Después de autenticar al usuario con éxito, puedes redirigirlo a la página del menú.
        return redirect('Menu')

    data = {
        # Aquí no necesitas especificar la ruta 'saludMental/' ya que la plantilla está en la carpeta 'templates' en la raíz del proyecto
    }
    return render(request, 'Login.html', data)

def registrar(request):
    if request.method == 'POST':
        correo = request.POST['form1Example1']
        contraseña = request.POST['form1Example2']
        nombre = request.POST['form1Example3']
        foto_de_perfil = request.FILES.get('foto_de_perfil')

        usuario = Usuario(correo=correo, contraseña=contraseña, nombre=nombre, foto_de_perfil=foto_de_perfil)
        usuario.save()
        return redirect('Login')

    data = {}
    return render(request, 'Registrar.html', data)

def grupo(request):
    data = {

    }
    return render(request,'GruposdeApoyo.html',data)



def menu(request):
    data = {
        # Aquí no necesitas especificar la ruta 'saludMental/' ya que la plantilla está en la carpeta 'templates' en la raíz del proyecto
    }
    return render(request, 'Menu.html', data)

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'Menu.html', {'publicaciones': publicaciones})


def logout_view(request):
    logout(request)
    return redirect('Login') 

