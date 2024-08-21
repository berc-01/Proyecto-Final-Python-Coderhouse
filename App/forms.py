from django import forms

class UsuarioFormulario(forms.Form): #Creamos el formulario de usuarios.
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()

class MonitoresFormulario(forms.Form): #Creamos el formulario de monitores.
    marca = forms.CharField(max_length=40)
    pulgadas = forms.IntegerField()

class ProcesadoresFormulario(forms.Form): #Creamos el formulario de procesadores.
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=40)

class buscar(forms.Form): #Creamos el formulario para buscar la marca de procesadores.
    marca = forms.CharField(max_length=20)