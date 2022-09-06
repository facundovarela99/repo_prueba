from django.urls import path
from AppTenis.views import *

urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('sociostenis/', Sociostenis, name='sociostenis'),
    path('tercercategoria/', tercerCategoria, name='tercercategoria'),
    path('damas/', Damas, name='damas'),
    path('cuartacategoria/', cuartaCategoria, name='cuartacategoria'),
    path('busquedaSocio/', busquedaSocio, name='busquedaSocio'),
    path('buscar/', buscar, name='buscar'),
]

