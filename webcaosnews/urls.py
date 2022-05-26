from django.contrib import admin
from django.urls import path, include
from .views import index, contacto, panel, signup,deportes,login,terms,politica,nacional,mundo,escribir,cerrar_sesion

urlpatterns = [
    path('', index,name = 'indx'),
    path('contacto/',contacto,name="cont"),
    path('deportes/',deportes,name="dep"),
    path('login/',login,name="log"),
    path('signup/',signup,name="sp"),
    path('terms/',terms,name="terms"),
    path('politica/',politica,name="pol"),
    path('nacional/',nacional,name="nac"),
    path('mundo/',mundo,name="mun"),
    path('escribir/',escribir,name="escr"),
    path('cerrar/',cerrar_sesion,name='cerrar'),
    path('accounts/', include('allauth.urls')),
    path('panel/',panel,name='panel'),
]
