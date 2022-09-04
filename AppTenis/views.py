from django.shortcuts import render
from .models import *


# Create your views here.
def inicio(request):
    return render (request, 'AppTenis/inicio.html')

def sociostenis(request):
    return render (request, 'AppTenis/sociostenis.html')

def categoriatercera(request):
    return render (request, 'AppTenis/categoriatercera.html')

def categoriacuarta(request):
    return render (request, 'AppTenis/categoriacuarta.html')

def damas(request):
    return render (request, 'AppTenis/damas.html')

