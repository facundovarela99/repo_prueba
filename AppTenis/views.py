from django.shortcuts import render
from .models import *
from .forms import *


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

def SociosFormulario(request):
    if request.method=='POST':
        form=SociosForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion['nombre']
            apellido=informacion['apellido']
            edad=informacion['edad']
            email=informacion['email']
            socio=SociosTenis(nombre=nombre, apellido=apellido, edad=edad, email=email)
            socio.save()
            return render (request, 'AppTenis/inicio.html',  {"mensaje":"Socio creado"})

    else:
        form=SociosForm()
    return render (request, 'AppTenis/sociosForm.html', {'formulario':form})

def tercerCatFormulario(request):
    if request.method=='POST':
        form=TercerCatForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            edad=info['edad']
            jugador_cat3=CatTercera(nombre=nombre, apellido=apellido, edad=edad)
            jugador_cat3.save()
            return render (request, 'AppTenis/inicio.html',  {"mensaje":"Jugador de tercer categoria CREADO"})

    else:
        form=TercerCatForm()
    return render (request, 'AppTenis/TercerCatForm.html', {'formulario':form})

def DamasFormulario(request):
    if request.method=='POST':
        form=DamasForm(request.POST)
        if form.is_valid():
            inf=form.cleaned_data
            nombre=inf['nombre']
            apellido=inf['apellido']
            edad=inf['edad']
            dama=CatDamas(nombre=nombre, apellido=apellido, edad=edad)
            dama.save()
            return render (request, 'AppTenis/inicio.html',  {"mensaje":"Dama CREADA"})

    else:
        form=DamasForm()
    return render (request, 'AppTenis/DamaForm.html', {'formulario':form})

def cuartaCatFormulario(request):
    if request.method=='POST':
        form=CuartaCatForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            edad=info['edad']
            jugador_cat4=CatCuarta(nombre=nombre, apellido=apellido, edad=edad)
            jugador_cat4.save()
            return render (request, 'AppTenis/inicio.html',  {"mensaje":"Jugador de cuarta categoria CREADO"})

    else:
        form=CuartaCatForm()
    return render (request, 'AppTenis/CUartaCatForm.html', {'formulario':form})

def busquedaSocio(request):
    return render(request, 'AppTenis/busquedaSocio.html')

def buscar(request):
    nombre=request.GET['nombre']
    apellido=request.GET['apellido']
    socios=SociosTenis.objects.filter(nombre=nombre, apellido=apellido)
    return render(request, 'AppTenis/resultadosBusqueda.html', {'socios':socios})