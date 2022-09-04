from django.urls import path
from AppTenis.views import *

urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('sociostenis/', sociostenis, name = 'sociostenis'),
    path('categoriacuarta/', categoriacuarta, name = 'categoriacuarta'),
    path('categoriatercera/', categoriatercera, name = 'categoriatercera'),
    path('damas/', damas, name = 'damas'),
    path('sociosFormulario/', SociosFormulario, name='sociosFormulario'),
    path('tercercatFormulario/', tercerCatFormulario, name='tercercatFormulario'),
    path('damasFormulario/', DamasFormulario, name='damasFormulario'),
    path('cuartacatFormulario/', cuartaCatFormulario, name='cuartacatFormulario'),
    path('busquedaSocio/', busquedaSocio, name='busquedaSocio'),
    path('buscar/', buscar, name='buscar'),
]

