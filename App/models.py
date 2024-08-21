from django.db import models

# Create your models here.

class Usuario(models.Model): #Creamos la clase usuario, donde se coloca nombre, apellido y mail.
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()

class Procesadores(models.Model): #Creamos la clase procesadores, marca (Intel o AMD) y modelo (i9 13900K o Ryzen 7 5800x3D por ejemplo).
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)

class Monitores(models.Model): #Creamos la clase monitores, marca (LG, Lenovo, etc) y pulgadas.
    marca = models.CharField(max_length=40)
    pulgadas = models.IntegerField()