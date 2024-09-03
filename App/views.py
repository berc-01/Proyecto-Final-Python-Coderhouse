from django.shortcuts import render
from django.http import HttpResponse #Importamos HttpResponse de django.
from App.models import Procesadores #Importamos la clase Procesadores dentro de los modelos de la aplicación.
from App.forms import ProcesadoresFormulario, UsuarioFormulario, MonitoresFormulario, TarjetasFormulario, RamFormulario, CoolersFormulario #Importamos todos los formularios.
from App.models import Monitores, Procesadores, Usuario, Tarjetas, Ram, Coolers #Importamos todos los modelos.

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.
def inicio(req):
    return render(req, 'app/inicio.html')

def buscar(req):
    if  req.GET["marca"]:  
        marca = req.GET['marca'] 
        procesadores = Procesadores.objects.filter(marca__icontains=marca)
        return render(req, "app/resultadosbusqueda.html", {"procesadores":procesadores, "marca":marca})

    else: 
        respuesta = "No enviaste datos"
    
    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)

def usuariosFormulario(req):
    if req.method == 'POST': # Si el formulario fue enviado
        miFormulario = UsuarioFormulario(req.POST) # Creamos un objeto formulario con los datos enviados
        print(miFormulario) # Imprimimos el formulario para depuración

        if miFormulario.is_valid(): # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data # Obtenemos los datos limpios y validados
            usuarios = Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail']) # Creamos un objeto Usuario
            usuarios.save() # Guardamos el curso en la base de datos
            return render(req, "app/inicio.html") # Redirigimos a la página de inicio

    else:
        miFormulario = UsuarioFormulario() # Creamos un formulario vacío para mostrarlo inicialmente

    return render(req, 'app/agregarusuarios.html', {'miFormulario':miFormulario})

def procesadorFormulario(req):
    if req.method == 'POST': # Si el formulario fue enviado
        miFormulario = ProcesadoresFormulario(req.POST) # Creamos un objeto formulario con los datos enviados
        print(miFormulario) # Imprimimos el formulario para depuración

        if miFormulario.is_valid(): # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data # Obtenemos los datos limpios y validados
            procesadores = Procesadores(marca=informacion['marca'], modelo=informacion['modelo'], nucleos=informacion['nucleos'], hilos=informacion['hilos'], frecuencia=informacion['frecuencia'], precio=informacion['precio']) # Creamos un objeto Procesador
            procesadores.save() # Guardamos el curso en la base de datos
            return render(req, "app/inicio.html") # Redirigimos a la página de inicio
        
    else:
        miFormulario = ProcesadoresFormulario() # Creamos un formulario vacío para mostrarlo inicialmente

    return render(req, 'app/agregarprocesador.html', {'miFormulario':miFormulario})

def monitorFormulario(req):
    if req.method == 'POST': # Si el formulario fue enviado
        miFormulario = MonitoresFormulario(req.POST) # Creamos un objeto formulario con los datos enviados
        print(miFormulario) # Imprimimos el formulario para depuración

        if miFormulario.is_valid(): # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data # Obtenemos los datos limpios y validados
            monitores = Monitores(marca=informacion['marca'], modelo=informacion['modelo'], resolucion=informacion['resolucion'], pulgadas=informacion['pulgadas'], hercios=informacion['hercios'], precio=informacion['precio']) # Creamos un objeto Monitor
            monitores.save() # Guardamos el curso en la base de datos
            return render(req, "app/inicio.html") # Redirigimos a la página de inicio
        
    else:
        miFormulario = MonitoresFormulario() # Creamos un formulario vacío para mostrarlo inicialmente

    return render (req, 'app/agregarmonitor.html', {'miFormulario':miFormulario})

def tarjetaFormulario(req):
    if req.method == 'POST': # Si el formulario fue enviado
        miFormulario = TarjetasFormulario(req.POST) # Creamos un objeto formulario con los datos enviados
        print(miFormulario) # Imprimimos el formulario para depuración

        if miFormulario.is_valid(): # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data # Obtenemos los datos limpios y validados
            tarjetas = Tarjetas(marca=informacion['marca'], modelo=informacion['modelo'], serie=informacion['serie'], memoria=informacion['memoria'], largo=informacion['largo'], precio=informacion['precio']) # Creamos un objeto Tarjeta
            tarjetas.save() # Guardamos el curso en la base de datos
            return render(req, "app/inicio.html") # Redirigimos a la página de inicio
        
    else:
        miFormulario = TarjetasFormulario() # Creamos un formulario vacío para mostrarlo inicialmente

    return render (req, 'app/agregartarjeta.html', {'miFormulario':miFormulario})

def coolerFormulario(req):
    if req.method == 'POST': # Si el formulario fue enviado
        miFormulario = CoolersFormulario(req.POST) # Creamos un objeto formulario con los datos enviados
        print(miFormulario) # Imprimimos el formulario para depuración

        if miFormulario.is_valid(): # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data # Obtenemos los datos limpios y validados
            coolers = Coolers(marca=informacion['marca'], modelo=informacion['modelo'], tipo=informacion['tipo'], altura=informacion['altura'], ventilador=informacion['ventilador'], precio=informacion['precio']) # Creamos un objeto Cooler
            coolers.save() # Guardamos el curso en la base de datos
            return render(req, "app/inicio.html") # Redirigimos a la página de inicio
        
    else:
        miFormulario = CoolersFormulario() # Creamos un formulario vacío para mostrarlo inicialmente

    return render (req, 'app/agregarcooler.html', {'miFormulario':miFormulario})

def ramFormulario(req):
    if req.method == 'POST': # Si el formulario fue enviado
        miFormulario = RamFormulario(req.POST) # Creamos un objeto formulario con los datos enviados
        print(miFormulario) # Imprimimos el formulario para depuración

        if miFormulario.is_valid(): # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data # Obtenemos los datos limpios y validados
            ram = Ram(marca=informacion['marca'], modelo=informacion['modelo'], tipo=informacion['tipo'], capacidad=informacion['capacidad'], velocidad=informacion['velocidad'], precio=informacion['precio']) # Creamos un objeto RAM
            ram.save() # Guardamos el curso en la base de datos
            return render(req, "app/inicio.html") # Redirigimos a la página de inicio
        
    else:
        miFormulario = RamFormulario() # Creamos un formulario vacío para mostrarlo inicialmente

    return render (req, 'app/agregarram.html', {'miFormulario':miFormulario})

#CRUD de Procesadores
class ProcesadorListView(ListView):
    model = Procesadores
    context_object_name = "procesadores"
    template_name = "app/procesadores_lista.html"

class ProcesadorDetailView(DetailView):
    model = Procesadores
    template_name = "app/procesador_detalle.html"

class ProcesadorCreateView(CreateView):
    model = Procesadores
    template_name = "app/procesador_agregar.html"
    success_url = reverse_lazy('ListaProcesadores')
    fields = ['marca', 'modelo', 'nucleos', 'hilos', 'frecuencia', 'precio']

class ProcesadorUpdateView(UpdateView):
    model = Procesadores
    template_name = "app/procesador_editar.html"
    success_url = reverse_lazy('ListaProcesadores')
    fields = ['marca', 'modelo', 'nucleos', 'hilos', 'frecuencia', 'precio']

class ProcesadorDeleteView(DeleteView):
    model = Procesadores
    template_name = "app/procesador_borrar.html"
    success_url = reverse_lazy('ListaProcesadores')



#CRUD de Monitores
class MonitorListView(ListView):
    model = Monitores
    context_object_name = "monitores"
    template_name = "app/monitores_lista.html"

class MonitorDetailView(DetailView):
    model = Monitores
    template_name = "app/monitores_detalle.html"

class MonitorCreateView(CreateView):
    model = Monitores
    template_name = "app/monitor_agregar.html"
    success_url = reverse_lazy('ListaMonitores')
    fields = ['marca', 'modelo', 'resolucion', 'pulgadas', 'hercios', 'precio']

class MonitorUpdateView(UpdateView):
    model = Monitores
    template_name = "app/monitor_editar.html"
    success_url = reverse_lazy('ListaMonitores')
    fields = ['marca', 'modelo', 'resolucion', 'pulgadas', 'hercios', 'precio']

class MonitorDeleteView(DeleteView):
    model = Monitores
    template_name = "app/monitor_borrar.html"
    success_url = reverse_lazy('ListaMonitores')



#CRUD de Tarjetas de video
class TarjetaListView(ListView):
    model = Tarjetas
    context_object_name = "tarjetas"
    template_name = "app/tarjetas_lista.html"

class TarjetaDetailView(DetailView):
    model = Tarjetas
    template_name = "app/tarjeta_detalle.html"

class TarjetaCreateView(CreateView):
    model = Tarjetas
    template_name = "app/tarjeta_agregar.html"
    success_url = reverse_lazy('ListaTarjetas')
    fields = ['marca', 'modelo', 'serie', 'memoria', 'largo', 'precio']

class TarjetaUpdateView(UpdateView):
    model = Tarjetas
    template_name = "app/tarjeta_editar.html"
    success_url = reverse_lazy('ListaTarjetas')
    fields = ['marca', 'modelo', 'serie', 'memoria', 'largo', 'precio']

class TarjetaDeleteView(DeleteView):
    model = Tarjetas
    template_name = "app/tarjeta_borrar.html"
    success_url = reverse_lazy('ListaTarjetas')



#CRUD de Coolers
class CoolerListView(ListView):
    model = Coolers
    context_object_name = "coolers"
    template_name = "app/coolers_lista.html"

class CoolerDetailView(DetailView):
    model = Coolers
    template_name = "app/cooler_detalle.html"

class CoolerCreateView(CreateView):
    model = Coolers
    template_name = "app/cooler_agregar.html"
    success_url = reverse_lazy('ListaCoolers')
    fields = ['marca', 'modelo', 'tipo', 'altura', 'ventilador', 'precio']

class CoolerUpdateView(UpdateView):
    model = Coolers
    template_name = "app/cooler_editar.html"
    success_url = reverse_lazy('ListaCoolers')
    fields = ['marca', 'modelo', 'tipo', 'altura', 'ventilador', 'precio']

class CoolerDeleteView(DeleteView):
    model = Coolers
    template_name = "app/cooler_borrar.html"
    success_url = reverse_lazy('ListaCoolers')



#CRUD de RAM
class RamListView(ListView):
    model = Ram
    context_object_name = "ram"
    template_name = "app/ram_lista.html"

class RamDetailView(DetailView):
    model = Ram
    template_name = "app/ram_detalle.html"

class RamCreateView(CreateView):
    model = Ram
    template_name = "app/ram_agregar.html"
    success_url = reverse_lazy('ListaRam')
    fields = ['marca', 'modelo', 'tipo', 'capacidad', 'velocidad', 'precio']

class RamUpdateView(UpdateView):
    model = Ram
    template_name = "app/ram_editar.html"
    success_url = reverse_lazy('ListaRam')
    fields = ['marca', 'modelo', 'tipo', 'capacidad', 'velocidad', 'precio']

class RamDeleteView(DeleteView):
    model = Ram
    template_name = "app/ram_borrar.html"
    success_url = reverse_lazy('ListaRam')


# def leerProcesadores(req):
#     procesadores = Procesadores.objects.all() #Esto me va a traer todos los procesadores registrados.
#     contexto = {"procesadores":procesadores}
#     return render(req, "app/leerprocesadores.html", contexto)

# def leerMonitores(req):
#     monitores = Monitores.objects.all() #Esto me va a traer todos los monitores.
#     contexto = {"monitores":monitores}
#     return render(req, "app/leermonitores.html", contexto)

# def leerTarjetas(req):
#     tarjetas = Tarjetas.objects.all() #Esto me va a traer todas las tarjetas de video.
#     contexto = {"tarjetas":tarjetas}
#     return render(req, "app/leertarjetas.html", contexto)

# def leerCoolers(req):
#     coolers = Coolers.objects.all() #Esto me va a traer todos los coolers.
#     contexto = {"coolers":coolers}
#     return render(req, "app/leercoolers.html", contexto)

# def leerRam(req):
#     ram = Ram.objects.all() #Esto me va a traer todas las RAM.
#     contexto = {"ram":ram}
#     return render(req, "app/leerram.html", contexto)

# def eliminarProcesador(req, procesador_modelo):
#     procesador = Procesadores.objects.get(modelo=procesador_modelo) #Trae el modelo del procesador
#     procesador.delete() #Elimina

#     procesadores = Procesadores.objects.all() #Trae a todos los procesadores
#     contexto = {"procesadores":procesadores}

#     return render(req, "app/leerprocesadores.html", contexto)

# def eliminarMonitor(req, monitor_modelo):
#     monitor = Monitores.objects.get(modelo=monitor_modelo) #Trae el modelo
#     monitor.delete() #Elimina

#     monitores = Monitores.objects.all() #Trae a todos los monitores
#     contexto = {"monitores":monitores}

#     return render(req, "app/leermonitores.html", contexto)

# def eliminarTarjeta(req, tarjeta_modelo):
#     tarjeta = Tarjetas.objects.get(modelo=tarjeta_modelo) #Trae el modelo
#     tarjeta.delete() #Elimina

#     tarjetas = Tarjetas.objects.all() #Trae a todas las tarjetas de video
#     contexto = {"tarjetas":tarjetas}

#     return render(req, "app/leertarjetas.html", contexto)

# def eliminarCooler(req, cooler_modelo):
#     cooler = Coolers.objects.get(modelo=cooler_modelo) #Trae el modelo
#     cooler.delete() #Elimina

#     coolers = Coolers.objects.all() #Trae a todos los coolers
#     contexto = {"coolers":coolers}

#     return render(req, "app/leercoolers.html", contexto)

# def eliminarRam(req, ram_modelo):
#     ram1 = Ram.objects.get(modelo=ram_modelo) #Trae el modelo
#     ram1.delete() #Elimina

#     ram = Ram.objects.all() #Trae a todas las memoria RAM
#     contexto = {"ram":ram}

#     return render(req, "app/leerram.html", contexto)