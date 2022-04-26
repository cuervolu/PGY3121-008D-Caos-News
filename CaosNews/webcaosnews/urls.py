from django.contrib import admin
from django.urls import path
from .views import index, contacto, signup,deportes,login,terms,politica,nacional,mundo,escribir

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
]
