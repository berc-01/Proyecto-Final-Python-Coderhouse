from django.db import models

# Create your models here.

class Usuario(models.Model): #Creamos la clase usuario, donde se coloca nombre, apellido y mail.
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()

    def __str__(self): #Función __str__ para mostrar los datos en el panel admin.
            return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.mail}"

class Procesadores(models.Model): #Creamos la clase procesadores, marca (Intel o AMD) y modelo (i9 13900K o Ryzen 7 5800x3D por ejemplo).
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    
    def __str__(self): #Función __str__ para mostrar los datos en el panel admin.
         return f"Marca: {self.marca} - Modelo: {self.modelo}"

class Monitores(models.Model): #Creamos la clase monitores, marca (LG, Lenovo, etc) y pulgadas.
    marca = models.CharField(max_length=40)
    pulgadas = models.IntegerField()

    def __str__(self): #Función __str__ para mostrar los datos en el panel admin.
         return f"Marca: {self.marca} - Pulgadas: {self.pulgadas}"