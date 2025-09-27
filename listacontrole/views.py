from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, VeiculoForm, UsoForm
from django.http import HttpRequest
from django.contrib import messages
from .models import MotoristaModel, VeiculoModels, UsoModel
import datetime

def listHome(request: HttpRequest):
    if request.method == 'POST':
        if 'form1_submit' in request.POST:
            formulario = ContactForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, 'Motorista cadastrado com sucesso!')
                return redirect('listacontrole:home')
        elif 'form2_submit' in request.POST:
            formulario = VeiculoForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, 'Veículo cadastrado com sucesso!')
                return redirect('listacontrole:home')
        elif 'form3_submit' in request.POST:
            formulario = UsoForm(request.POST)
            if formulario.is_valid():
                uso = formulario.save()
                # Marcar o veículo como em uso (False = Em uso)
                uso.veiculo.status = False
                uso.veiculo.save()
                messages.success(request, 'Uso registrado com sucesso!')
                return redirect('listacontrole:home')
        elif 'finalizar_uso_submit' in request.POST:
            uso_id = request.POST.get('uso_id')
            km_final = request.POST.get('km_final')
            
            try:
                uso = get_object_or_404(UsoModel, id=uso_id)
                
                # Validar KM final
                if km_final and int(km_final) >= uso.km_inicial:
                    uso.km_final = int(km_final)
                    uso.horario_final = datetime.datetime.now().time()
                    uso.save()
                    
                    # Liberar o veículo (True = Disponível)
                    uso.veiculo.status = True
                    uso.veiculo.save()
                    
                    messages.success(request, f'Uso do veículo {uso.veiculo.nome} finalizado com sucesso!')
                else:
                    messages.error(request, 'KM final deve ser maior ou igual ao KM inicial!')
                    
            except (ValueError, TypeError):
                messages.error(request, 'KM final deve ser um número válido!')
            except Exception as e:
                messages.error(request, f'Erro ao finalizar uso: {str(e)}')
                
            return redirect('listacontrole:home')

    motoristas = MotoristaModel.objects.all()
    veiculos = VeiculoModels.objects.all()
    usos = UsoModel.objects.all()
    
    # Criar lista com veículos e seus motoristas atuais
    veiculos_com_motoristas = []
    for veiculo in veiculos:
        # Buscar o último uso não finalizado deste veículo
        uso_atual = UsoModel.objects.filter(
            veiculo=veiculo, 
            horario_final__isnull=True  # Uso ainda não foi finalizado
        ).order_by('-data_criacao').first()
        
        veiculo_info = {
            'veiculo': veiculo,
            'motorista_atual': uso_atual.motorista if uso_atual else None,
            'uso_atual': uso_atual,
            'em_uso': uso_atual is not None
        }
        veiculos_com_motoristas.append(veiculo_info)

    context = {
        'motoristas': motoristas,
        'veiculos': veiculos, 
        'veiculos_com_motoristas': veiculos_com_motoristas,
        'usos': usos,
        'form': ContactForm(),
        'formveiculo': VeiculoForm(),
        'formuso': UsoForm()
    }
    return render(request, 'listacontrole/home.html', context)