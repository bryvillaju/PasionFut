from django import forms
from .models import Partido

class PartidoForm(forms.ModelForm):
    class Meta:
        model= Partido
        fields=('Equipo1','Equipo2','GolesEquipo1','GolesEquipo2','Resumen','Fecha_Partido','Fecha_Publicacion',)

