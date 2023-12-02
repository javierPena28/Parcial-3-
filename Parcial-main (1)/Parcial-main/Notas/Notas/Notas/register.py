from django.shortcuts import render
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        # Validar los datos del formulario
        email = request.POST["email"]
        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST["password"]

        # Crear un nuevo usuario
        user = User.objects.create_user(
            email=email,
            
            username=username,
            password=password,
        )

        # Iniciar sesión al usuario
        login(request, user)

        return redirect(to="home")

    return render(request, "register.html")