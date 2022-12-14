from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class IntegranteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    email=forms.EmailField()
    genero=forms.CharField(max_length=5)

class ProveedorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    ropa=forms.CharField(max_length=50)
    equipo=forms.CharField(max_length=50)

class eventosForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    partidos=forms.IntegerField()
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label='Ingrese Contraseña', widget=forms.PasswordInput)    
    password2= forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
