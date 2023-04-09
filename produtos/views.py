from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Produtos
from .forms import ProdutoForm

# Create your views here.
def index(request):
    return render(request, 'produtos/index.html', {
        'produtos': Produtos.objects.all()
    })

def view_produto(request, id):
    produto = Produtos.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))    

def add(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            new_cod_prod = form.cleaned_data['cod_prod']
            new_nome = form.cleaned_data['nome']
            new_descricao = form.cleaned_data['descricao']
            new_barra = form.cleaned_data['barra']
            new_valor = form.cleaned_data['valor']
            new_estoque = form.cleaned_data['estoque']
            
            new_produtos = Produtos(
                cod_prod = new_cod_prod,
                nome = new_nome,
                descricao = new_descricao,
                barra = new_barra,
                valor = new_valor,
                estoque = new_estoque
            )
            new_produtos.save()
            return render(request, 'produtos/add.html', {
                'form': ProdutoForm(),
                'success': True
            })
    else:
        form = ProdutoForm()
    return render(request, 'produtos/add.html',{
        'form': ProdutoForm()
    })

def edit(request,id):
    if request.method == 'POST':
        produto = Produtos.objects.get(pk=id)
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return render(request, 'produtos/edit.html', {
                'form': form,
                'success': True
            }) 
    else:
        produto = Produtos.objects.get(pk=id)
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/edit.html',{
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        produto = Produtos.objects.get(pk=id)
        produto.delete()
    return HttpResponseRedirect(reverse('index'))                                  