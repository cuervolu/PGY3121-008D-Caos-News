from django.contrib import admin
from .models import Periodista,Area,Categoria,Noticias,Regiones

# Register your models here.
admin.site.register(Periodista)
admin.site.register(Area)
admin.site.register(Categoria)
admin.site.register(Noticias)
admin.site.register(Regiones)