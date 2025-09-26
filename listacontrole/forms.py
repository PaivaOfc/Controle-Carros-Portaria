from django import forms
from .models import UsoModel, VeiculoModels, MotoristaModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = MotoristaModel
        fields = ['nome', 'cnh', 're', 'empresa', 'cargo']

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = VeiculoModels
        fields = ['nome', 'placa', 'marca', 'ano', 'cor']

class UsoForm(forms.ModelForm):
    class Meta:
        model = UsoModel
        fields = ['motorista', 'veiculo', 'data_uso', 'horario_inicio', 'km_inicial', 'destino']
        # horario_final não está incluído porque será preenchido quando o uso terminar
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Torna os campos obrigatórios mais claros
        self.fields['data_uso'].widget.attrs.update({'type': 'date'})
        self.fields['horario_inicio'].widget.attrs.update({'type': 'time'})