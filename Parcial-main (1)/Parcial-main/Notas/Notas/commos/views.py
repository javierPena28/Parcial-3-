from collections import UserDict
from imaplib import _Authenticator
from django.shortcuts import render, redirect
from .models import Notas
from django.contrib.auth import authenticate, login


from django.db import IntegrityError


# Create your views here.


def index(request):
    notas= Notas.objects.all()
    return render(request,"index.html",{"notas":notas})

def registrar(request):
    return render(request,"NuevaNota.html")

def registrarNota(request):
    mensaje_error = None

    if request.method == 'POST':
        codigo = request.POST['codigo']
        nota = request.POST['nota']
        fecha = request.POST['fecha']

        # Verifica si ya existe un registro con el mismo código
        existe_registro = Notas.objects.filter(codigo=codigo).exists()

        if not existe_registro:
            # Si no existe, crea el nuevo registro
            notas = Notas.objects.create(codigo=codigo, nota=nota, fecha=fecha)
            return redirect('/')
        else:
            # Si ya existe un registro con el mismo código, muestra un mensaje de error
            mensaje_error = f"Ya existe un registro con el código {codigo}. Intente con otro código."

    # Renderiza la plantilla con el mensaje de error
    return render(request, 'NuevaNota.html', {'mensaje_error': mensaje_error})



def ver(request,codigo):
    nota=Notas.objects.get(codigo=codigo)
    return render(request,"ver.html",{"nota":nota})
    
def edicion(request,codigo):
    nota=Notas.objects.get(codigo=codigo)
    return render(request,"edicion.html",{"nota":nota})

def borrar(request,codigo):

    nota=Notas.objects.get(codigo=codigo)
    nota.delete()
    return redirect('/')

def editarNota(request):
    codigo=request.POST['codigo']
    notas=request.POST['nota']
    fecha=request.POST['fecha']

    nota=Notas.objects.get(codigo=codigo)
    nota.nota=notas
    nota.fehca=fecha
    nota.save()

    
    return redirect('/')




##
def ingresar(request):
  """
  Vista para el botón "Ingresar".

  """

  if request.method == 'POST':
    # Validamos los datos del formulario
    username = request.POST['username']
    password = request.POST['password']

    # Verificamos si el usuario existe
    user = UserDict.objects.filter(username=username).first()

    if user is None:
      return render(request, 'login.html', {
        'error': 'El usuario no existe'
      })

    # Verificamos la contraseña
    if user.check_password(password):
      # Iniciamos sesión al usuario
      login(request, user)

      return redirect('index')
    else:
      return render(request, 'login.html', {
        'error': 'La contraseña es incorrecta'
      })

  return render(request, 'login.html')

##

from django.contrib.auth.models import User
def register(request):
    # ...

    # Redireccionar a la página de inicio de sesión
    return redirect("login")
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        # Validar los datos del formulario
        email = request.POST["email"]
        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST["password"]

        # Validar que el nombre de usuario no exista
        existing_user = User.objects.filter(username=username).exists()
        if existing_user:
            error_message = "El nombre de usuario ya existe."
            return render(request, "register.html", {"error_message": error_message})

        # Crear un nuevo usuario
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
            name=name,
        )

        # Iniciar sesión al usuario
        login(user)

        return redirect(to="home")

    return render(request, "register.html")

 ## loogin


def login(request):
    if request.method == "POST":
        # Obtener las credenciales del formulario
        username = request.POST["username"]
        password = request.POST["password"]

        # Autenticar al usuario
        user = authenticate(username=username, password=password)

         # Iniciar sesión al usuario
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("http://localhost:8000/")
        else:
            error_message = "Las credenciales no son válidas."
            return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")