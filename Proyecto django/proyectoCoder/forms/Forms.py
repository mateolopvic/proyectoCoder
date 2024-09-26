from django import forms
from proyectoCoder.Models import Barrio

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()
    mail = forms.CharField()
    contrasena = forms.CharField()
    edad = forms.IntegerField()
    
class BarrioFormulario(forms.Form):
    nombre = forms.CharField()
    
class CasaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    cantidad_habitantes = forms.IntegerField()
    barrio = forms.ModelChoiceField(queryset=Barrio.objects.all(), empty_label="Seleccione un barrio")