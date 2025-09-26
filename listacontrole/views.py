from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, VeiculoForm, UsoForm
from django.http import HttpRequest
from .models import MotoristaModel, VeiculoModels, UsoModel


# Create your views here.

def listHome(request:HttpRequest):
    # motorista = get_object_or_404(MotoristaModel, id=id)
    # veiculo = get_object_or_404(VeiculoModels, id=id)
    # uso = get_object_or_404(UsoModel, id=id)
    if request.method == 'POST':
        print('teste')
        if 'form1_submit' in request.POST:
            formulario = ContactForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('listacontrole:home')
        elif 'form2_submit' in request.POST:
            formulario = VeiculoForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('listacontrole:home')
        elif 'form3_submit' in request.POST:
            formulario = UsoForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('listacontrole:home')


    motoristas = MotoristaModel.objects.all()
    veiculos = VeiculoModels.objects.all()
    usos = UsoModel.objects.all()

    context = {
        'motoristas': motoristas,
        'veiculos': veiculos, 
        'usos': usos,
        'form': ContactForm(),
        'formveiculo': VeiculoForm(),
        'formuso': UsoForm()
    }
    return render(request, 'listacontrole/home.html', context)