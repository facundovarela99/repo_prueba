from django.contrib import admin

from AppTenis.views import Eventosclub
from .models import *
# Register your models here.

admin.site.register(IntegrantesClub)
admin.site.register(ProveedorIndumentaria)
admin.site.register(eventos)
