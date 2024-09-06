from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', views.login_request, name="Login"),
    path('accounts/signup', views.register, name="Registro"),
    path('accounts/logout/', LogoutView.as_view(template_name='app/inicio.html'), name="Logout"),
    path('accounts/profile/', views.editar_usuario, name='EditarUsuario'),
    path('cambiarcontraseña/', views.CambiarPassword.as_view(), name='CambiarPassword'),
]