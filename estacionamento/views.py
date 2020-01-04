from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, Rotativo
from .forms import PessoaForm, VeiculoForm, RotativoForm

def index(request):
    context = {'mensagem': 'Hello World!'}
    return render(request, 'estacionamento/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'estacionamento/lista_pessoas.html', data)

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'estacionamento/lista_veiculos.html', data)

def lista_rotativos(request):
    rotativos = Rotativo.objects.all()
    form = RotativoForm()
    data = {'rotativos': rotativos, 'form': form}
    return render(request, 'estacionamento/lista_rotativos.html', data)

def cadastra_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('est_lista_pessoas')

def cadastra_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('est_lista_veiculos')

def cadastra_rotativo(request):
    form = RotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('est_lista_rotativos')

def atualiza_pessoa(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('est_lista_pessoas')
    else:
        return render(request, 'estacionamento/atualiza_pessoa.html', data)

def atualiza_veiculo(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('est_lista_veiculos')
    else:
        return render(request, 'estacionamento/atualiza_veiculo.html', data)

def atualiza_rotativo(request, id):
    data = {}
    rotativo = Rotativo.objects.get(id=id)
    form = RotativoForm(request.POST or None, instance=rotativo)
    data['rotativo'] = rotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('est_lista_rotativos')
    else:
        return render(request, 'estacionamento/atualiza_rotativo.html', data)

def deleta_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    
    if request.method == 'POST':
        pessoa.delete()
        return redirect('est_lista_pessoas')
    else:
        return render(request, 'estacionamento/confirma_del_pessoa.html', {'pessoa': pessoa})

def deleta_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    
    if request.method == 'POST':
        veiculo.delete()
        return redirect('est_lista_veiculos')
    else:
        return render(request, 'estacionamento/confirma_del_veiculo.html', {'veiculo': veiculo})

def deleta_rotativo(request, id):
    rotativo = Rotativo.objects.get(id=id)
    
    if request.method == 'POST':
        rotativo.delete()
        return redirect('est_lista_rotativos')
    else:
        return render(request, 'estacionamento/confirma_del_rotativo.html', {'rotativo': rotativo})