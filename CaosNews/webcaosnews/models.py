from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Periodista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='fotos',null=True)
    def __str__(self):
        return self.nombre
    
