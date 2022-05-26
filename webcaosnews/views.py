from django.shortcuts import render
# incorporar el modelo de Periodista,Area,Categoría
from .models import Periodista,Area,Categoria,Noticias
#importar modelo de tablas del User
from django.contrib.auth.models import User
# importar librerias que validan el ingreso o login a una pagina
from django.contrib.auth import authenticate,logout,login as login_aut
from django.contrib import messages
#importar una librería decoradora , permite evitar el ingreso de usuarios a la página web
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    return render(request,"index.html")

def contacto(request):
    return render(request,"contacto.html")

def deportes(request):
    return render(request,"deportes.html")

def login(request):
    contexto = {"msg": ""}
    if request.POST:
        usuario = request.POST.get("txtEmail")
        logPassword = request.POST.get("txtPassword") 
        us = authenticate(username=usuario,password=logPassword)
        if us is not None and us.is_active:
            login_aut(request,us)
            return render(request,"index.html")
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            contexto = {"msg": "Usuario o contraseña incorrecto"}
            
    return render(request,"login.html", contexto)

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
    return render(request,"signup.html", contexto)

def terms(request):
    return render(request,"terms.html")

def politica(request):
    return render(request,"politica.html")

def nacional(request):
    return render(request,"nacional.html")

def mundo(request):
    return render(request,"mundo.html")

def cerrar_sesion(request):
    logout(request)
    return render(request,"index.html")


@login_required(login_url='/login/')
def panel(request):
    return render(request,"panel.html")

@login_required(login_url='/login/')   
def escribir(request):
    categorias = Categoria.objects.all() #Selecciono todos los registros
    contexto = {"items":categorias}
    if request.POST:
        titulo = request.POST.get("txtTitulo")
        portada = request.FILES.get("txtImagen")
        catego = request.POST.get("cboCategoria")
        contenido = request.POST.get("txtNoticia")
        tags = request.POST.get("txtTags")
        #seleccionar el registro completo de la categoría a buscar
        obj_catego = Categoria.objects.get(nombre=catego)
        mensaje = "rrrrrr"
        try:
            noticia = Noticias()
            noticia.titulo = titulo
            if portada is not None:
                noticia.portada=portada
            noticia.categoria=obj_catego
            noticia.contenido=contenido
            noticia.tags=tags
            noticia.save()
            mensaje = "Grabo Noticia"
        except:
            mensaje = "No grabo noticia"
        contexto["mensaje"] = mensaje
        
    return render(request,"escribir.html",contexto)