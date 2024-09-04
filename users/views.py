from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm

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
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(req,"app/inicio.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(req,"users/registro.html", {"form":form, "msg_register":msg_register})