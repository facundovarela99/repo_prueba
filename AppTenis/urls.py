from django.urls import path
from AppTenis.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('integrantesclub/', Integrantesclub, name='integrantesclub'),
    path('busquedaIntegrante/', busquedaIntegrante, name='busquedaIntegrante'),
    path('buscar/', buscar, name='buscar'),
    path('proveedoresclub/', Proveedoresclub, name='proveedoresclub'),
    path('eventosclub/', Eventosclub, name='eventosclub'),
    path('leerintegrantes/', leerIntegrantes, name='leerintegrantes'),
    path('eliminarIntegrante/<id>', eliminarIntegrante, name='eliminarIntegrante'),
    path('editarIntegrante/<id>', editarIntegrante, name='editarIntegrante'),
    #cbv
    path('int/list/', IntegrantesList.as_view(), name = 'integrantes_listar'),
    path('integrante/<pk>', IntegranteDetalle.as_view(), name ='integrante_detalle'),
    path('int/nuevo/', IntegranteCreacion.as_view(), name ='integrante_crear'),
    path('integrante/editar/<pk>/', IntegranteUpdate.as_view(), name ='integrante_editar'),
    path('integrante/borrar/<pk>/', IntegranteDelete.as_view(), name ='integrante_editar'),
    #Login register logout
    path('login/', login_request, name ='login'),
    path('register/', register, name ='register'),
    path('logout/', LogoutView.as_view(template_name='AppTenis/logout.html'), name='logout'),
]

