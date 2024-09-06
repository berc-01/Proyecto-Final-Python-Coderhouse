"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #Incluimos include de django.
from django.conf import settings #Importamos nuestras configuraciones.
from django.conf.urls.static import static #Importamos nuestro static.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')), #Incluimos las urls de la aplicación App.
    path('', include('users.urls')), #Incluimos las urls de la aplicación users.
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #Indicamos el camino que tiene que seguir para detectar las imagenes dentro del proyecto.