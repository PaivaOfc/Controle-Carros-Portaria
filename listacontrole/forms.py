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
        motoristas_em_uso_ids = UsoModel.objects.filter(
            horario_final__isnull=True
        ).values_list('motorista_id', flat=True)
        self.fields['motorista'].queryset = MotoristaModel.objects.exclude(id__in=motoristas_em_uso_ids)
        self.fields['veiculo'].queryset = VeiculoModels.objects.filter(status=True)
        self.fields['data_uso'].widget.attrs.update({'type': 'date'})
        self.fields['horario_inicio'].widget.attrs.update({'type': 'time'})