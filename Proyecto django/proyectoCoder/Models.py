from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.IntegerField()
    mail = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=40)
    edad = models.IntegerField()

class Barrio(models.Model):
    nombre = models.CharField(max_length=40)
    
class Casa(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    cantidad_habitantes = models.IntegerField()
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, related_name='casas')
