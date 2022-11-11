from django.shortcuts import render
from blog.models import Configuracion

# Create your views here.

def index(request):
    return render(request, "blog/index.html")

def index(request):
    configuracion = Configuracion.objects.get(id=1) # te trae el primer diccionario de la lista
    return render(request, 'blog/index.html',{'configuracion':configuracion})

