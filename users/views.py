from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserEditForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .models import Imagen

# Create your views here.
def login_request(req):
    msg_login = ""
    if req.method == 'POST':
        form = AuthenticationForm(req, data=req.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(req, user)
                return render(req, "app/inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(req, "users/login.html", {"form": form, "msg_login": msg_login})

def register(req):

    msg_register = ""
    if req.method == 'POST':

        form = UserRegisterForm(req.POST)
        if form.is_valid(): #Si los datos que se han ingresado son válidos, se guardan los datos y se crea un usuario.
            form.save()
            return render(req,"app/inicio.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(req,"users/registro.html", {"form":form, "msg_register":msg_register})

@login_required
def editar_usuario(req):
    usuario = req.user

    if req.method == 'POST':
        miFormulario = UserEditForm(req.POST, req.FILES, instance=usuario)

        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if Imagen.objects.filter(user=usuario).exists():
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()
                else:
                    avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()

            miFormulario.save()

            return render(req, 'app/inicio.html')
    
    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(req, 'users/editar_usuario.html', {'mi_form' : miFormulario, 'usuario' : usuario})

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/editar_contraseña.html'
    success_url = reverse_lazy('EditarUsuario')