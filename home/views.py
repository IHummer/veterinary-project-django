from django.shortcuts import render
# importamos tablas para generar conteo
from inventory.models import *
from usuarios.models import *

def index(request):
    productos = Producto.objects.count()
    usuarios = Usuario.objects.count()
    context = {
        'header' : 'Inicio',
        'productos': productos,
        'usuarios': usuarios,
    }
    return render(request, 'index.html', context)