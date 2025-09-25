from django import forms
import datetime

class ContactForm(forms.Form):
    empresas = [
        ('tecelagem', 'São João Tecelagem'),
        ('tinturaria', 'São João Tinturaria'),
        ('doptex', 'DOPTEX'),
        ('corradi', 'Corradi'),
        ('textil', 'Textil da Serra'),
    ]
    name = forms.CharField(label='Nome', max_length=100, required=True)
    cnh = forms.CharField(label='CNH', required=True)
    re = forms.IntegerField(label='RE', required=True)
    empresa = forms.ChoiceField(label='Empresa', choices=empresas, required=True)
    cargo = forms.CharField(label='Cargo', max_length=100, required=True)

class VeiculoForm(forms.Form):
    name = forms.CharField(label='Nome do Veiculo', max_length=100, required=True)
    placa = forms.CharField(label='Placa do Veículo', max_length=7, required=True)
    marca = forms.CharField(label='Marca do Veículo', max_length=50, required=True)
    ano = forms.IntegerField(label='Ano do Veículo', initial='2025', required=True)
    cor = forms.CharField(label='Cor do Veículo', max_length=30, required=True)

class UsoForm(forms.Form):
    Motoristas = [
        ('erik', 'Erik Mendes'),
        ('joao', 'João Silva'),
        ('maria', 'Maria Oliveira'),
        ('carlos', 'Carlos Souza'),
        ('ana', 'Ana Pereira'),
    ]
    Veiculos = [
        ('ford', 'Ford Ka'),
        ('chevrolet', 'Chevrolet Onix'),
        ('volkswagen', 'Volkswagen Gol'),
        ('hyundai', 'Hyundai HB20'),
    ]
    
    motorista = forms.ChoiceField(label='Motorista', choices=Motoristas, required=True)
    veiculo = forms.ChoiceField(label='Veículo', choices=Veiculos, required=True)
    data_uso = forms.DateField(label='Data de Uso', input_formats=['%d/%m/%Y'], widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    hora_uso = forms.TimeField(label='Horario inicio', widget=forms.TimeInput(attrs={'type': 'time'}), required=True)
    km = forms.IntegerField(label='KM Inicial', required=True)
    destino = forms.CharField(label='Destino', max_length=200, required=True)