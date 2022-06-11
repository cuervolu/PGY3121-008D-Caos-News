from django.shortcuts import redirect, render
# incorporar el modelo de Periodista,Area,Categoría
from .models import *
# importar modelo de tablas del User
from django.contrib.auth.models import User
# importar librerias que validan el ingreso o login a una pagina
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib import messages
# importar una librería decoradora , permite evitar el ingreso de usuarios a la página web
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from django.contrib import messages

# Create your views here
usu = ''
cantidad = 0


def cantidad_no_publicados(usuario):
    cantidad = Noticias.objects.filter(
        usuario=usuario, publicado=False).count()
    return cantidad


def index(request):
    noticiasN = Noticias.objects.filter(categoria__nombre = 'Nacional' ,aprobada=True).order_by('-fecha')
    contexto = {"noticias": noticiasN}
    return render(request, "index.html",contexto)


def galeria(request):
    noticias = Noticias.objects.filter(aprobada=True).order_by('-fecha')
    contexto = {"noticias": noticias}
    return render(request, "galeria.html", contexto)


def contacto(request):
    data = {
        'form': ContactoForm(),
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request, 'Tu mensaje fue enviado. Te contactaremos a la brevedad')
        else:
            data['form'] = formulario

    return render(request, "contacto.html", data)


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
    usu = request.user.username  # recuperar nombre de usuario
    noticias = Noticias.objects.filter(usuario=usu)
    cantidad = cantidad_no_publicados(usu)
    contexto = {"noticias": noticias, "cantidad": cantidad}
    return render(request, "panel.html", contexto)


@login_required(login_url='/login/')
def escribir(request):
    data = {
        'form': EscribirForm(initial={'usuario':request.user.username}),
    }
    if request.method == 'POST':
        formulario = EscribirForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            instance=formulario.save(commit=False)
            instance.usuario=request.user
            instance.save()
            # formulario.save()
            messages.success(
                request, 'Tu artículo sera revisado por nuestros administradores. Te avisaremos cuando llegue el resultado.', extra_tags='alerta')
        else:
            print('usuario: ', request.user)
            print(formulario.errors)
            messages.error(
                request, 'Ha habido un error.', extra_tags='fallo')
            data['form'] = formulario

    return render(request, "escribir.html", data)
