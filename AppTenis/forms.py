from django import forms

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
        
    
    
