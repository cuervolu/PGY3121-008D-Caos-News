from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Periodista(models.Model):
    id_periodista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField(unique=True)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='fotos',null=True)
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True),
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

    
class Regiones(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_region
class Noticias(models.Model):
    id_noticia = models.AutoField(primary_key=True),
    # id_periodista = models.ForeignKey(Periodista,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='fotos',null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    contenido = models.CharField(max_length=1500)
    etiquetas = models.CharField(max_length=150)
    fecha = models.DateField(auto_now=True)
    ubicacion = models.ForeignKey(Regiones,on_delete=models.CASCADE)
    aprobada = models.BooleanField(default=False)
    comentario = models.TextField(default='--')
    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True),
    pnombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField(unique=True)
    mensaje = models.TextField(null=False)
    archivo = models.FileField(upload_to='fotos',null=True)
