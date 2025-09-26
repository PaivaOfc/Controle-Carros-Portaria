from django.shortcuts import render
from .forms import ContactForm, VeiculoForm, UsoForm
from django.http import HttpRequest


# Create your views here.

def listHome(request: HttpRequest):
    if request.method == 'POST':
        print('teste')
        if 'form1_submit' in request.POST:
            print('entrou motorista')
        elif 'form2_submit' in request.POST:
            print('entrou veiculo')
        elif 'form3_submit' in request.POST:
            print('entrou uso')


    context = {'form': ContactForm(), 'formveiculo': VeiculoForm(), 'formuso': UsoForm()}
    return render(request, 'listacontrole/home.html', context)