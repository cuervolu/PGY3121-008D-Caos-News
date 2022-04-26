from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def contacto(request):
    return render(request,"contacto.html")

def deportes(request):
    return render(request,"deportes.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def terms(request):
    return render(request,"terms.html")

def politica(request):
    return render(request,"politica.html")

def nacional(request):
    return render(request,"nacional.html")

def mundo(request):
    return render(request,"mundo.html")

def escribir(request):
    return render(request,"escribir.html")