from django.contrib import admin
from .models import Periodista,Area,Categoria,Noticias,Regiones,Contacto,Galeria


class noticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo','fecha','autor','categoria','ubicacion','aprobada']
    search_fields = ['usuario','titulo']
    list_filter = ['aprobada','categoria']
    list_per_page = 10


# Register your models here.
admin.site.register(Periodista)
admin.site.register(Area)
admin.site.register(Categoria)
admin.site.register(Noticias,noticiaAdmin)
admin.site.register(Regiones)
admin.site.register(Contacto)
admin.site.register(Galeria)