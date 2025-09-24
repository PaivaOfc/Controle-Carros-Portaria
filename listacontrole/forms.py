from django import forms

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
    re = forms.CharField(label='RE', max_length=6, required=True)
    empresa = forms.ChoiceField(label='Empresa', choices=empresas, required=True)
    cargo = forms.CharField(label='Cargo', max_length=100, required=True)