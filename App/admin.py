from django.contrib import admin
from App.models import Usuario, Procesadores, Monitores, Tarjetas, Coolers, Ram
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Procesadores)
admin.site.register(Monitores)
admin.site.register(Tarjetas)
admin.site.register(Coolers)
admin.site.register(Ram)