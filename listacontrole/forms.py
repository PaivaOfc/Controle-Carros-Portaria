from django import forms
from .models import UsoModel, VeiculoModels, MotoristaModel, AgendamentoVeiculo
from datetime import date, time, datetime

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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        motoristas_em_uso_ids = UsoModel.objects.filter(
            horario_final__isnull=True
        ).values_list('motorista_id', flat=True)
        self.fields['motorista'].queryset = MotoristaModel.objects.exclude(id__in=motoristas_em_uso_ids)
        self.fields['veiculo'].queryset = VeiculoModels.objects.filter(status=True)
        self.fields['data_uso'].widget = forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        self.fields['horario_inicio'].widget = forms.TimeInput(attrs={'type': 'time'}, format='%H:%M')

        if not self.instance.pk:
            self.fields['data_uso'].initial = date.today().strftime('%Y-%m-%d')
            self.fields['horario_inicio'].initial = datetime.now().time().strftime('%H:%M')

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = AgendamentoVeiculo
        fields = ['motorista', 'veiculo', 'data_uso', 'horario_uso', 'destino']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields('motorista').queryset = MotoristaModel.objects.filter()
        self.fields('veiculo').queryset = VeiculoModels.objects.filter()
        self.fields['data_uso'].widget = forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        self.fields['horario_uso'].widget = forms.TimeInput(attrs={'type': 'time'}, format='%H:%M')
        if not self.instance.pk:
            self.fields['data_uso'].initial = date.today().strftime('%Y-%m-%d')
            self.fields['horario_uso'].initial = datetime.now().time().strftime('%H:%M')

