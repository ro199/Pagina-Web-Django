from django.db import models

# Create your models here.
class Heroe(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    altura = models.FloatField()
    fecha_registro = models.DateField()
    habilidades = models.CharField(max_length=200)
    edad = models.IntegerField()