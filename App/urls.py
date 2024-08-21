from django.urls import path #Importamos path de django.
from App import views #Importamos las views de la aplicación (App).

# Create your views here.
urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('procesadores/', views.procesadores, name='procesadores'),
    path('monitores/', views.monitores, name='monitores'),
    path('buscar/', views.buscar),
]