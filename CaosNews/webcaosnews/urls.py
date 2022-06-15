from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index,name = 'indx'),
    path('contacto/',contacto,name="cont"),
    path('deportes/',deportes,name="dep"),
    path('login/',login,name="log"),
    path('registro/',registro,name="sp"),
    path('terms/',terms,name="terms"),
    path('politica/',politica,name="pol"),
    path('nacional/',nacional,name="nac"),
    path('mundo/',mundo,name="mun"),
    path('escribir/',escribir,name="escr"),
    # path('cerrar/',cerrar_sesion,name='cerrar'),
    path('templates/registration/login.html', include('allauth.urls')),
    path('panel/',panel,name='panel'),
    path('lo-ultimo/',galeria,name='lUT'),
    path('tinymce/',include('tinymce.urls')),
    path('listar/',listar,name='list'),
    path('modificar-noticia/<id>/',modificarNoticia,name='modNot'),
    path('eliminar-noticia/<id>/',eliminarNoticia,name='elimNot'),
    path('articulo/<id>/',articulo,name='ART'),
    path('buscar-articulo',buscarArticulo,name = 'BUSCARA')
]
