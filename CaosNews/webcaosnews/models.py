from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime


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
    telefono = PhoneNumberField(null=False, blank=False, unique=True,region='CL')
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='fotos',null=True, default='fotos/default_photo.png')
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
    usuario = models.CharField(max_length=60,default='--')
    #id_periodista = models.ForeignKey(Periodista,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='fotos/%Y/%m/%d/',null=False,default='fotos/defecto.png')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    contenido = models.TextField(null=False)
    etiquetas = models.CharField(max_length=150)
    fecha = models.DateField(("Fecha"), default=datetime.date.today)
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
    telefono = PhoneNumberField(null=False, blank=False, unique=False,region='CL')
    mensaje = models.TextField(null=False)
    archivo = models.ImageField(upload_to='archivos_contacto/%Y/%m/%d/',default='fotos/defecto.png')

    def __str__(self):
        return self.pnombre

class Galeria(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to = 'galeria')
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE)

    def __str__(self):
        return 'Número: '+str(self.auto_inc)