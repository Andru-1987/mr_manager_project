from django import forms
from .models import Consulta , ArchivoConsulta


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'  # Include all fields from the model

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ConsultaForm, self).__init__(*args, **kwargs)
        
        if user:
            self.fields['usuario_consulta'].initial = user
            self.fields['usuario_consulta'].widget = forms.HiddenInput()