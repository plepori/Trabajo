from django import forms
from prueba.models import Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm): #creamos una clase que hereda información de un modelo
    class Meta: # se define la clase meta 
        model = Familiar # el modelo con el que se quiere vincular
        fields = ['nombre', 'direccion', 'dni']

