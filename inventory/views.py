from django.shortcuts import render
#añadiendo las tablas
from .models import Categoria, Producto
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(redirect_field_name='')
def index(request):
    return render(request, 'inventario/index.html')
