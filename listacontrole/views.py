from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, VeiculoForm, UsoForm
from django.http import HttpRequest
from django.contrib import messages
from .models import MotoristaModel, VeiculoModels, UsoModel
import datetime

def listHome(request: HttpRequest):
    abrir_modal_editar = False
    motorista_editando_id = None
    formeditar = ContactForm()
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
                motorista_selecionado = formulario.cleaned_data.get('motorista')
                veiculo_selecionado = formulario.cleaned_data.get('veiculo')
 
                motorista_usando = UsoModel.objects.filter(motorista = motorista_selecionado, horario_final__isnull = True).exists()
                veiculo_usando = UsoModel.objects.filter(veiculo = veiculo_selecionado, horario_final__isnull = True).exists()

                if motorista_usando:
                    messages.error(request, 'Este motorista já está usando um veículo!')
                    return redirect('listacontrole:home')
                elif veiculo_usando:
                    messages.error(request, 'Este veiculo já está sendo usado por outro motorista!')
                    return redirect('listacontrole:home')
                else:
                    uso = formulario.save()
                    uso.veiculo.status = False
                    uso.veiculo.save()
                    messages.success(request, 'Uso registrado com sucesso!')
                    return redirect('listacontrole:home')
        elif 'finalizar_uso_submit' in request.POST:
            uso_id = request.POST.get('uso_id')
            km_final = request.POST.get('km_final')
            
            try:
                uso = get_object_or_404(UsoModel, id=uso_id)
                
                if km_final and int(km_final) >= uso.km_inicial:
                    uso.km_final = int(km_final)
                    uso.horario_final = datetime.datetime.now().time()
                    uso.save()
                    
                    uso.veiculo.status = True
                    uso.veiculo.save()
                    
                    messages.success(request, f'Uso do veículo {uso.veiculo.nome} finalizado com sucesso!')
                else:
                    messages.error(request, 'KM final deve ser maior ou igual ao KM inicial!')
                    
            except (ValueError, TypeError, None):
                messages.error(request, 'KM final deve ser um número válido!')
            except Exception as e:
                messages.error(request, f'Erro ao finalizar uso: {str(e)}')
                
            return redirect('listacontrole:home')
        elif 'excluir_motorista' in request.POST:
            motorista_id = request.POST.get('motorista_id')
            MotoristaModel.objects.filter(id=motorista_id).delete()
            messages.success(request, 'Motorista excluido com sucesso.')
            return redirect('listacontrole:home')
        elif 'editar_motorista' in request.POST:
            motorista_id = request.POST.get('motorista_id')
            motorista = get_object_or_404(MotoristaModel, id=motorista_id)
            formeditar = ContactForm(instance=motorista)
            abrir_modal_editar = True
            motorista_editando_id = motorista_id
        elif 'form4_submit' in request.POST:
            motorista_id = request.POST.get('motorista_id')
            motorista = get_object_or_404(MotoristaModel, id=motorista_id)
            formulario = ContactForm(request.POST, instance=motorista)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, 'Motorista editado com sucesso!')
                return redirect('listacontrole:home')
            else:
                formeditar = formulario
                abrir_modal_editar = True
                motorista_editando_id = motorista_id
                messages.error(request, 'Erro ao editar o motorista!')


    motoristas = MotoristaModel.objects.all()
    veiculos = VeiculoModels.objects.all()
    usos = UsoModel.objects.all()
    
    veiculos_com_motoristas = []
    for veiculo in veiculos:
        uso_atual = UsoModel.objects.filter(
            veiculo=veiculo, 
            horario_final__isnull=True
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
        'formuso': UsoForm(),
        'formeditar': formeditar,
        'abrir_modal_editar': abrir_modal_editar,
        'motorista_editando_id': motorista_editando_id,
    }
    return render(request, 'listacontrole/home.html', context)