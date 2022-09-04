from django.db import models

# EL MODELS INTERACTUA CON LA BASE DE DATOS

class SociosTenis(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField()
    def __str__ (self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)+" "+str(self.email)

class CatTercera(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    def __str__ (self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)

class CatCuarta(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    def __str__ (self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)

class CatDamas(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    def __str__ (self):
        return self.nombre+" "+self.apellido+" "+str(self.edad)
