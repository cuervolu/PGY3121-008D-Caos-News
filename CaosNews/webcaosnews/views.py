from django.shortcuts import redirect, render, get_object_or_404
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
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q
# importar libreria de conexión HTTP
import requests
from rest_framework import viewsets
# JsonResponse
from django.http import JsonResponse
# Create your views here
usu = ''
cantidad = 0


def cantidad_no_publicados(usuario):
    cantidad = Noticias.objects.filter(
        usuario=usuario, aprobada=False).count()
    return cantidad


def index(request):
    noticias = Noticias.objects.filter(aprobada=True).order_by('-fecha')[:3]
    noticiasN = Noticias.objects.filter(
        categoria__nombre='Nacional', aprobada=True).order_by('-fecha')
    notDeporte = Noticias.objects.filter(
        categoria__nombre='Deportes', aprobada=True).last()
    contexto = {"noticiasN": noticiasN,
                "noticias": noticias, "notDeporte": notDeporte}
    return render(request, "index.html", contexto)


def articulo(request, id):
    noticia = Noticias.objects.get(id=id)
    contexto = {"noticia": noticia}
    return render(request, "articulo.html", contexto)


def buscarArticulo(request):
    if request.method == 'POST':
        searched = request.POST['txtBuscar']
        entity = Noticias.objects.filter(Q(titulo__icontains=searched) | Q(autor__icontains=searched) | Q(
            etiquetas__icontains=searched))  # buscar por titulo, etiquetas  y autor
        return render(request, "buscarArticulo.html", {"buscado": searched, "entity": entity})
    else:
        return render(request, "buscarArticulo.html")
    return render(request, "buscarArticulo.html")


def galeria(request):
    noticias = Noticias.objects.filter(aprobada=True).order_by('-fecha')
    # contexto = {"noticias": noticias}
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(noticias, 5)
        noticias = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': noticias,
        'paginator': paginator
    }
    return render(request, "galeria.html", data)


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
    noticias = Noticias.objects.filter(
        aprobada=True, categoria__nombre='Deportes').order_by('-fecha')
    # contexto = {"noticias": noticias}
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(noticias, 5)
        noticias = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': noticias,
        'paginator': paginator
    }
    return render(request, "deportes.html", data)


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

    return render(request, "registration/login.html", contexto)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login_aut(request, user)
            messages.success(
                request, 'Te has registrado correctamente.')
            # redirigir al home
            return redirect('/')
        data['form'] = formulario
    return render(request, "registration/registro.html", data)


def terms(request):
    return render(request, "terms.html")


def politica(request):
    noticias = Noticias.objects.filter(
        aprobada=True, categoria__nombre='Política').order_by('-fecha')
    # contexto = {"noticias": noticias}
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(noticias, 5)
        noticias = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': noticias,
        'paginator': paginator
    }
    return render(request, "politica.html", data)


def nacional(request):
    noticias = Noticias.objects.filter(
        aprobada=True, categoria__nombre='Nacional').order_by('-fecha')
    # contexto = {"noticias": noticias}
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(noticias, 5)
        noticias = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': noticias,
        'paginator': paginator
    }
    return render(request, "nacional.html", data)


def mundo(request):
    noticias = Noticias.objects.filter(
        aprobada=True, categoria__nombre='Mundo').order_by('-fecha')
    # contexto = {"noticias": noticias}
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(noticias, 5)
        noticias = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': noticias,
        'paginator': paginator
    }
    return render(request, "mundo.html", data)


def cerrar_sesion(request):
    logout(request)
    return render(request, "index.html")


@login_required(login_url='login')
@permission_required('webcaosnews.view_noticias', login_url='login')
def panel(request):
    usu = request.user.username  # recuperar nombre de usuario
    noticias = Noticias.objects.filter(
        usuario=usu, aprobada=False).order_by('-fecha')
    cantidadNoticias = Noticias.objects.filter(usuario=usu).count()
    cantidadNoticiasAprobadas = Noticias.objects.filter(
        usuario=usu, aprobada=True).count()
    cantidad = cantidad_no_publicados(usu)
    try:
        coeficiente = cantidadNoticiasAprobadas / cantidadNoticias
    except ZeroDivisionError as err:
        coeficiente = 0
    porcentaje = round(coeficiente * 100)
    contexto = {"noticias": noticias, "cantidad": cantidad, "cantidadNoticias": cantidadNoticias,
                "cantidadNoticiasAprobadas": cantidadNoticiasAprobadas, "porcentaje": porcentaje}
    return render(request, "panel/panel.html", contexto)


@login_required(login_url='login')
@permission_required('webcaosnews.change_noticias', login_url='login')
@permission_required('webcaosnews.delete_noticias', login_url='login')
@permission_required('webcaosnews.view_noticias', login_url='login')
def listar(request):
    noticias = Noticias.objects.filter(usuario=request.user).order_by('-fecha')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(noticias, 5)
        noticias = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': noticias,
        'paginator': paginator
    }
    return render(request, "panel/listado.html", data)


@login_required(login_url='login')
@permission_required('webcaosnews.change_noticias', login_url='login')
@permission_required('webcaosnews.delete_noticias', login_url='login')
@permission_required('webcaosnews.view_noticias', login_url='login')
def modificarNoticia(request, id):
    Noticia = get_object_or_404(Noticias, id=id)
    data = {
        'form': EscribirForm(instance=Noticia),
    }
    if request.method == 'POST':
        formulario = EscribirForm(
            data=request.POST, files=request.FILES, instance=Noticia)
        imagenNoticia = formulario.files.getlist('ImagenNoticia')
        if formulario.is_valid():
            instance = formulario.save(commit=False)
            instance.save()
            for i in imagenNoticia:
                img = ImagenNoticia(imagen=i, noticia=instance)
                img.save()
                # instance.imagenes.add(img)
            # instance.save()
            print(f'Imagenes: {imagenNoticia}')
            formulario.save()
            messages.success(
                request, 'Tu artículo ha sido modificado', extra_tags='alerta')
            return redirect(to='panel')
        else:
            print(formulario.errors)
            messages.error(
                request, 'Ha habido un error.', extra_tags='fallo')
            data['form'] = formulario
    return render(request, "panel/modificarNoticia.html", data)


@login_required(login_url='login')
@permission_required('webcaosnews.change_noticias', login_url='login')
@permission_required('webcaosnews.delete_noticias', login_url='login')
@permission_required('webcaosnews.view_noticias', login_url='login')
def eliminarNoticia(request, id):
    Noticia = get_object_or_404(Noticias, id=id)
    Noticia.delete()
    messages.success(
        request, 'Tu artículo ha sido eliminado', extra_tags='alerta')
    return redirect(to='list')


@login_required(login_url='login')
@permission_required('webcaosnews.add_noticias', login_url='login')
def escribir(request):
    data = {
        'form': EscribirForm(initial={'usuario': request.user.username}),
    }
    if request.method == 'POST':
        formulario = EscribirForm(data=request.POST, files=request.FILES)
        imagenNoticia = formulario.files.getlist('ImagenNoticia')
        if formulario.is_valid():
            instance = formulario.save(commit=False)
            instance.usuario = request.user
            instance.autor = request.user.first_name + " " + request.user.last_name
            instance.save()
            for i in imagenNoticia:
                img = ImagenNoticia(imagen=i, noticia=instance)
                img.save()
                # instance.imagenes.add(img)
            # instance.save()
            print(f'Imagenes: {imagenNoticia}')
            messages.success(
                request, 'Tu artículo sera revisado por nuestros administradores. Te avisaremos cuando llegue el resultado.', extra_tags='alerta')
        else:
            print('usuario: ', request.user)
            print(formulario.errors)
            messages.error(
                request, 'Ha habido un error.', extra_tags='fallo')
            data = {'form': formulario}

    return render(request, "escribir.html", data)


def galeria_api(request):
    noticias = requests.get("http://127.0.0.1:8000/api/noticias/").json()
    # contexto = {"noticias": noticias}
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(noticias, 5)
        noticias = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': noticias,
        'paginator': paginator
    }
    return render(request, "galeria_api.html", data)
