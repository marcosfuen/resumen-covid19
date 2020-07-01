from django.forms import ModelForm, Textarea, TextInput, CheckboxInput
from .models import Incidencias
from django.utils.translation import gettext_lazy as _


class IncidenciasForm(ModelForm):
    class Meta:
        model = Incidencias
        fields = ['name', 'address', 'incidencia', 'isResolve', 'startDate']
        labels = {
            'isResolve': _('Resuelta'),
        }
        # help_texts = {
        #     'isResolve': _('Si esta marcado, se le dio respuesta a la Incidencia.'),
        # }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre y Apellidos'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del Abuelito'}),
            'incidencia': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la incidencia'}),
            'isResolve': CheckboxInput(attrs={'class': 'custom-control custom-checkbox'}),
            'startDate': TextInput(attrs={'class': 'form-control', 'type': 'date'}),

        }
