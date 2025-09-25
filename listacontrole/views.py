from django.shortcuts import render
from .forms import ContactForm, VeiculoForm, UsoForm
from django.http import HttpRequest


# Create your views here.

def listHome(request: HttpRequest):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        print(form_type)
        if form_type == 'motorista':
            print('entrou motorista')


    context = {'form': ContactForm(), 'formveiculo': VeiculoForm(), 'formuso': UsoForm()}
    return render(request, 'listacontrole/home.html', context)


def CadastroMotorista(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'listacontrole/home.html', {'form': ContactForm(), 'formveiculo': VeiculoForm(), 'formuso': UsoForm()})
    else:
        form = ContactForm()
    return render(request, 'listacontrole/home.html', {'form': form, 'formveiculo': VeiculoForm(), 'formuso': UsoForm()})