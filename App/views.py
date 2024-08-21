from django.shortcuts import render
from django.http import HttpResponse #Importamos HttpResponse de django.
from App.models import Procesadores #Importamos la clase Procesadores dentro de los modelos de la aplicación.
from App.forms import ProcesadoresFormulario, UsuarioFormulario, MonitoresFormulario #Importamos todos los formularios.
from App.models import Monitores, Procesadores, Usuario #Importamos todos los modelos.



# Create your views here.
def inicio(req):
    return render(req, 'app/inicio.html')

def usuarios(req):
    if req.method == 'POST': # Si el formulario fue enviado
        miFormulario = UsuarioFormulario(req.POST) # Creamos un objeto formulario con los datos enviados
        print(miFormulario) # Imprimimos el formulario para depuración

        if miFormulario.is_valid(): # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data # Obtenemos los datos limpios y validados
            usuarios = Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail']) # Creamos un objeto Monitor
            usuarios.save() # Guardamos el curso en la base de datos
            return render(req, "app/inicio.html") # Redirigimos a la página de inicio

    else:
        miFormulario = UsuarioFormulario() # Creamos un formulario vacío para mostrarlo inicialmente

    return render(req, 'app/usuarios.html', {'miFormulario':miFormulario})

def procesadores(req):
    if req.method == 'POST': # Si el formulario fue enviado
        miFormulario = ProcesadoresFormulario(req.POST) # Creamos un objeto formulario con los datos enviados
        print(miFormulario) # Imprimimos el formulario para depuración

        if miFormulario.is_valid(): # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data # Obtenemos los datos limpios y validados
            procesadores = Procesadores(marca=informacion['marca'], modelo=informacion['modelo']) # Creamos un objeto Monitor
            procesadores.save() # Guardamos el curso en la base de datos
            return render(req, "app/inicio.html") # Redirigimos a la página de inicio
        
    else:
        miFormulario = ProcesadoresFormulario() # Creamos un formulario vacío para mostrarlo inicialmente

    return render(req, 'app/procesadores.html', {'miFormulario':miFormulario})

def monitores(req):
    if req.method == 'POST': # Si el formulario fue enviado
        miFormulario = MonitoresFormulario(req.POST) # Creamos un objeto formulario con los datos enviados
        print(miFormulario) # Imprimimos el formulario para depuración

        if miFormulario.is_valid(): # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data # Obtenemos los datos limpios y validados
            monitores = Monitores(marca=informacion['marca'], pulgadas=informacion['pulgadas']) # Creamos un objeto Monitor
            monitores.save() # Guardamos el curso en la base de datos
            return render(req, "app/inicio.html") # Redirigimos a la página de inicio
        
    else:
        miFormulario = MonitoresFormulario() # Creamos un formulario vacío para mostrarlo inicialmente

    return render (req, 'app/monitores.html', {'miFormulario':miFormulario})

def buscar(req):
    if  req.GET["marca"]:  
        marca = req.GET['marca'] 
        procesadores = Procesadores.objects.filter(marca__icontains=marca)
        return render(req, "app/resultadosbusqueda.html", {"procesadores":procesadores, "marca":marca})

    else: 
        respuesta = "No enviaste datos"
    
    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)