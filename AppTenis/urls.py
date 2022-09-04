from django.urls import path
from AppTenis.views import *

urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('sociostenis/', sociostenis, name = 'sociostenis'),
    path('categoriacuarta/', categoriacuarta, name = 'categoriacuarta'),
    path('categoriatercera/', categoriatercera, name = 'categoriatercera'),
    path('damas/', damas, name = 'damas'),
]
