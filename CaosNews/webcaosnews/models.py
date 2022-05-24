from pyexpat import model
from tkinter import CASCADE
from django.db import models

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
    telefono = models.CharField(max_length=50)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='fotos',null=True)
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True),
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Noticias(models.Model):
    id_noticia = models.AutoField(primary_key=True),
    titulo = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='fotos',null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    contenido = models.CharField(max_length=1500)
    etiquetas = models.CharField(max_length=150)
    def __str__(self):
        return self.titulo
    
