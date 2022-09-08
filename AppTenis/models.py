import email
from django.db import models

# EL MODELS INTERACTUA CON LA BASE DE DATOS

class IntegrantesClub(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField()
    genero=models.CharField(max_length=5)
    def __str__(self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+str(self.email)+" "+self.genero

class ProveedorIndumentaria(models.Model):
    nombre=models.CharField(max_length=50)
    ropa=models.CharField(max_length=50)
    equipo=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre+" "+self.ropa+" "+self.equipo

class eventos(models.Model):
    nombre=models.CharField(max_length=50)
    partidos=models.IntegerField()
    def __str__(self):
        return self.nombre+" "+str(self.partidos)

    

