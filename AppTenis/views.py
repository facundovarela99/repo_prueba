from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def inicio(request):
    return render (request, 'AppTenis/inicio.html')
    
def Integrantesclub(request):
    if request.method=='POST':
        form=IntegranteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            edad=info['edad']
            email=info['email']
            genero=info['genero']
            integrante=IntegrantesClub(nombre=nombre, apellido=apellido, edad=edad, email=email, genero=genero)
            integrante.save()
            integrantes=IntegrantesClub.objects.all()
            return render (request, 'AppTenis/leerintegrantes.html', {'integrantes':integrantes})
    else:
        form=IntegranteForm()
    return render (request, 'AppTenis/integrantesclub.html', {'formulario':form})

def Proveedoresclub(request):
    if request.method=='POST':
        form=ProveedorForm(request.POST)
        if form.is_valid():
            inf=form.cleaned_data
            nombre=inf['nombre']
            ropa=inf['ropa']
            equipo=inf['equipo']
            proveedor=ProveedorIndumentaria(nombre=nombre, ropa=ropa, equipo=equipo)
            proveedor.save()
            return render (request, 'AppTenis/inicio.html', {'mensaje':'Proveedor creado'})
    else:
        form=ProveedorForm()
    return render (request, 'AppTenis/proveedoresclub.html', {'formulario':form})

def Eventosclub(request):
    if request.method=='POST':
        form=eventosForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion['nombre']
            partidos=informacion['partidos']
            evento=eventos(nombre=nombre, partidos=partidos)
            evento.save()
            return render (request, 'AppTenis/inicio.html', {'mensaje':'Evento creado'})
    else:
        form=eventosForm()
    return render (request, 'AppTenis/eventosclub.html', {'formulario':form})
            
def busquedaIntegrante(request):
    return render(request, 'AppTenis/busquedaIntegrante.html', {'mensaje1': 'Ingresar apellido del integrante'})

def buscar(request):
    if request.GET['apellido']:
        apellido=request.GET['apellido']
        integrantes=IntegrantesClub.objects.filter(apellido=apellido)
        return render(request, 'AppTenis/resultadosBusqueda.html', {'integrantes':integrantes})
    else:
        return render(request, 'AppTenis/busquedaIntegrante.html', {'mensaje':'No se detectaron datos. Ingresar integrante'})

def leerIntegrantes(request):
    integrantes=IntegrantesClub.objects.all()
    return render (request, 'AppTenis/leerintegrantes.html', {'integrantes':integrantes})

def eliminarIntegrante(request, id):
    integrante=IntegrantesClub.objects.get(id=id)
    integrante.delete()
    integrantes=IntegrantesClub.objects.all()
    return render (request, 'AppTenis/leerintegrantes.html', {'integrantes':integrantes})

def editarIntegrante(request, id):
    integrante=IntegrantesClub.objects.get(id=id)
    if request.method=='POST': 
        form=IntegranteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            integrante.nombre=info['nombre']
            integrante.apellido=info['apellido']
            integrante.edad=info['edad']
            integrante.email=info['email']
            integrante.genero=info['genero']
            integrante.save()
            integrantes=IntegrantesClub.objects.all() #al editar, me devuelva el formulario vacio (el integrante se editó)
            return render(request, 'AppTenis/leerintegrantes.html', {'integrantes':integrantes})
    else:
        form=IntegranteForm(initial={'nombre':integrante.nombre, 'apellido':integrante.apellido, 'edad':integrante.edad, 'email':integrante.email, 'genero':integrante.genero})
        return render(request, 'AppTenis/editarIntegrante.html', {'formulario':form, 'integrante':integrante})

########### CBV ###########

class IntegrantesList(ListView):
    model = IntegrantesClub
    template_name = 'AppTenis/leerIntegrantesclub.html'

class IntegranteDetalle(DetailView): #DEVUELVE CAMPOS VACIOS (?)
    model = IntegrantesClub
    template_name = 'AppTenis/integrantedetalle.html'

class IntegranteCreacion(CreateView): #Funciona si solo si tengo un template llamado ''integrante_form''????
    model = IntegrantesClub
    success_url = reverse_lazy('integrante_crear')
    fields=['nombre', 'apellido', 'edad', 'email', 'genero']

    #ValueError at /AppTenis/integrante/nuevo
    #Field 'id' expected a number but got 'nuevo'.
class IntegranteUpdate(UpdateView):
    model=IntegrantesClub
    success_url = reverse_lazy('integrante_crear')
    fields=['nombre', 'apellido', 'edad', 'email', 'genero']

#PORQUE AL CREAR O UPDATEAR NO ME DEVUELVE LA LISTA DE INTEGRANTES Y ME DEVUELVE LOS CAMPOS VACIOS (EL INTEGRANTE SE CREó)
########### CBV ###########

########## login logout register ###########

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST['username']
            clave=request.POST['password']
            usuario=authenticate(username=usu, password=clave)
    else:
        form=AuthenticationForm()
        return render(request, 'AppTenis/login.html', {'formulario':form})
        #continuar playground parte 2 minuto 21:44


