from django import forms

class UsuarioFormulario(forms.Form): #Creamos el formulario de usuarios.
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()

class MonitoresFormulario(forms.Form): #Creamos el formulario de monitores.
    marca = forms.CharField(max_length=40)
    resolucion = forms.CharField(max_length=40)
    pulgadas = forms.IntegerField()
    hercios = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class ProcesadoresFormulario(forms.Form): #Creamos el formulario de procesadores.
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    nucleos = forms.IntegerField()
    hilos = forms.IntegerField()
    frecuencia = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class TarjetasFormulario(forms.Form): #Creamos el formulario de Tarjetas de video.
    marca = forms.CharField(max_length=40)
    serie = forms.CharField(max_length=40)
    memoria = forms.CharField(max_length=40)
    largo = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class CoolersFormulario(forms.Form): #Creamos el formulario de coolers.
    marca = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=40)
    altura = forms.CharField(max_length=40)
    ventilador = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class RamFormulario(forms.Form): #Creamos el formulario de memorias RAM.
    marca = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=40)
    capacidad = forms.CharField(max_length=40)
    velocidad = forms.IntegerField()
    precio = forms.IntegerField()

class buscar(forms.Form): #Creamos el formulario para buscar la marca de procesadores.
    marca = forms.CharField(max_length=20)