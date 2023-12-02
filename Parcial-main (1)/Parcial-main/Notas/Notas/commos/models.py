from django.db import models
from django.contrib.auth.models import User


class Notas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nota = models.PositiveSmallIntegerField()
    fecha = models.DateField()

class Usuario(models.Model):
    
    class MyModel(models.Model):
    # Bloque de código que debe seguir la definición de clase
        name = models.CharField(max_length=255)
        email = models.EmailField()


