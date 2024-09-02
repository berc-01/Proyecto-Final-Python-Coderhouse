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
    nucleos = models.IntegerField()
    hilos = models.IntegerField()
    frecuencia = models.CharField(max_length=40)
    precio = models.IntegerField()
    
    def __str__(self): #Función __str__ para mostrar los datos en el panel admin.
         return f"Marca: {self.marca} - Modelo: {self.modelo} - Núcleos: {self.nucleos} - Hilos: {self.hilos} - Frecuencia: {self.frecuencia}"

class Monitores(models.Model): #Creamos la clase monitores, marca (LG, Lenovo, etc) y pulgadas.
    marca = models.CharField(max_length=40)
    resolucion = models.CharField(max_length=40)
    pulgadas = models.IntegerField()
    hercios = models.CharField(max_length=40)
    precio = models.IntegerField()


    def __str__(self): #Función __str__ para mostrar los datos en el panel admin.
         return f"Marca: {self.marca} - Resolución: {self.resolucion} - Pulgadas: {self.pulgadas} - Hercios: {self.hercios}"
    
class Tarjetas(models.Model): #Creamos la clase tarjetas, marca (AMD o NVIDIA).
    marca = models.CharField(max_length=40)
    serie = models.CharField(max_length=40)
    memoria = models.CharField(max_length=40)
    largo = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self): #Función __str__ para mostrar los datos en el panel admin.
         return f"Marca: {self.marca} - Serie: {self.serie} - Memoria: {self.memoria} - Largo: {self.largo}"
    
class Coolers(models.Model): #Creamos la clase coolers.
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    altura = models.CharField(max_length=40)
    ventilador = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self): #Función __str__ para mostrar los datos en el panel admin.
         return f"Marca: {self.marca} - Tipo: {self.tipo} - Altura: {self.altura} - Ventilador: {self.ventilador}"
 
class Ram(models.Model): #Creamos la clase RAM.
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    capacidad = models.CharField(max_length=40)
    velocidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self): #Función __str__ para mostrar los datos en el panel admin.
         return f"Marca: {self.marca} - Tipo: {self.tipo} - Capacidad: {self.capacidad} - Velocidad: {self.velocidad}"