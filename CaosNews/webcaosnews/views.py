from django.shortcuts import render
# incorporar el modelo de Periodista,Area,Categoría
from .models import Periodista, Area, Categoria, Noticias, Regiones, Contacto
# importar modelo de tablas del User
from django.contrib.auth.models import User
# importar librerias que validan el ingreso o login a una pagina
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib import messages
# importar una librería decoradora , permite evitar el ingreso de usuarios a la página web
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request, "index.html")


def contacto(request):
    mensaje = {"msg": ""}
    if request.POST:
        nombre = request.POST.get("txtFirstName")
        apellido = request.POST.get("txtLastName")
        email = request.POST.get("txtEmail")
        telefono = request.POST.get("txtPhone")
        comentario = request.POST.get("txtComments")
        archivo = request.FILES.get("txtFile")
        try: 
            contact = Contacto()
            contact.pnombre = nombre
            contact.appaterno = apellido
            contact.email = email
            contact.telefono = telefono
            contact.mensaje = comentario
            contact.archivo = archivo
            contact.save()
            mensaje = {"msg": "Mensaje enviado correctamente"}
            print(mensaje)
        except Exception as e:
            mensaje = {"msg": "Error al enviar el mensaje", "error": e}
            print(mensaje)
    return render(request, "contacto.html", mensaje)


def deportes(request):
    return render(request, "deportes.html")


def login(request):
    contexto = {"msg": ""}
    if request.POST:
        usuario = request.POST.get("txtEmail")
        logPassword = request.POST.get("txtPassword")
        us = authenticate(username=usuario, password=logPassword)
        if us is not None and us.is_active:
            login_aut(request, us)
            return render(request, "index.html")
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            contexto = {"msg": "Usuario o contraseña incorrecto"}

    return render(request, "login.html", contexto)


def signup(request):
    contexto = {"msg": ""}
    if request.POST:
        u = request.POST.get("txtUsername")
        n = request.POST.get("txtName")
        a = request.POST.get("txtApellido")
        p = request.POST.get("txtPassword")
        e = request.POST.get("txtEmail")
        usu = User()
        usu.username = u
        usu.first_name = n
        usu.last_name = a
        usu.email = e
        usu.set_password(p)
        usu.save()
        contexto = {"msg": "Usuario creado"}
    return render(request, "signup.html", contexto)


def terms(request):
    return render(request, "terms.html")


def politica(request):
    return render(request, "politica.html")


def nacional(request):
    return render(request, "nacional.html")


def mundo(request):
    return render(request, "mundo.html")


def cerrar_sesion(request):
    logout(request)
    return render(request, "index.html")


@login_required(login_url='/login/')
def panel(request):
    return render(request, "panel.html")


@login_required(login_url='/login/')
def escribir(request):
    categorias = Categoria.objects.all()  # Selecciono todos los registros
    contexto = {"items": categorias}
    ubicacion = Regiones.objects.all()  # Selecciono todas las regiones
    contexto["u_items"] = ubicacion
    if request.POST:
        titulo = request.POST.get("txtTitulo")
        portada = request.FILES.get("txtImagen")
        catego = request.POST.get("cboCategoria")
        ubi = request.POST.get("cboUbicacion")
        contenido = request.POST.get("txtNoticia")
        tags = request.POST.get("txtTags")
        # seleccionar el registro completo de la categoría a buscar
        obj_catego = Categoria.objects.get(nombre=catego)
        # seleccionar el registro completo de la ubicacion a buscar
        obj_ubi = Regiones.objects.get(nombre_region=ubi)
        mensaje = "Hola"
        print(mensaje)
        try:
            noticia = Noticias()
            noticia.titulo = titulo
            if portada is not None:
                noticia.portada = portada
                noticia.categoria = obj_catego
                noticia.ubicacion = obj_ubi
                noticia.contenido = contenido
                noticia.etiquetas = tags
                noticia.save()
                mensaje = "Grabo Noticia"
                print(mensaje)
        except Exception as e:
                mensaje = "No grabo noticia"
                print(mensaje)
                print(e)
        contexto["mensaje"] = mensaje

    return render(request, "escribir.html", contexto)
