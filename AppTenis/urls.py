from django.urls import path
from AppTenis.views import *

urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('integrantesclub/', Integrantesclub, name='integrantesclub'),
    path('busquedaIntegrante/', busquedaIntegrante, name='busquedaIntegrante'),
    path('buscar/', buscar, name='buscar'),
    path('proveedoresclub/', Proveedoresclub, name='proveedoresclub'),
    path('eventosclub/', Eventosclub, name='eventosclub'),
    path('leerintegrantes/', leerIntegrantes, name='leerintegrantes'),
    path('eliminarIntegrante/<id>', eliminarIntegrante, name='eliminarIntegrante'),
    
]

