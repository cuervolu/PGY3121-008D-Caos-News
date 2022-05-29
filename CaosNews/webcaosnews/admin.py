from django.contrib import admin
from .models import Periodista,Area,Categoria,Noticias,Regiones,Contacto

# Register your models here.
admin.site.register(Periodista)
admin.site.register(Area)
admin.site.register(Categoria)
admin.site.register(Noticias)
admin.site.register(Regiones)
admin.site.register(Contacto)